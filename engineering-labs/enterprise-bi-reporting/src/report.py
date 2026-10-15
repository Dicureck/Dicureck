#!/usr/bin/env python3
"""Synthetic BI pipeline. Offline only; never accesses real company systems."""
from __future__ import annotations
import argparse
import csv
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from html import escape
from pathlib import Path
import json
import re

COLUMNS = ("order_id", "sale_date", "region", "channel", "revenue_su", "cost_su", "budget_su")
REGIONS = {"North", "Central", "South"}
CHANNELS = {"Digital", "Partner"}
CENT = Decimal("0.01")


def read_sales(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(COLUMNS):
            raise ValueError("CSV columns must match the published data contract exactly")
        rows = []
        identifiers = set()
        for line, raw in enumerate(reader, start=2):
            if None in raw or any(value is None for value in raw.values()):
                raise ValueError(f"Line {line}: missing or extra CSV fields")
            ident = raw["order_id"]
            if not re.fullmatch(r"S[0-9]{4}", ident) or ident in identifiers:
                raise ValueError(f"Line {line}: invalid or duplicate order_id")
            identifiers.add(ident)
            try:
                sold = date.fromisoformat(raw["sale_date"])
            except ValueError as exc:
                raise ValueError(f"Line {line}: invalid sale_date") from exc
            if sold.isoformat() != raw["sale_date"]:
                raise ValueError(f"Line {line}: sale_date must be YYYY-MM-DD")
            if raw["region"] not in REGIONS or raw["channel"] not in CHANNELS:
                raise ValueError(f"Line {line}: unknown region or channel")
            row = {"order_id": ident, "sale_date": sold.isoformat(),
                   "month": sold.strftime("%Y-%m"), "region": raw["region"],
                   "channel": raw["channel"]}
            for field in ("revenue_su", "cost_su", "budget_su"):
                value = raw[field]
                if not re.fullmatch(r"[0-9]+[.][0-9]{2}", value):
                    raise ValueError(f"Line {line}: {field} needs nonnegative two-decimal units")
                try:
                    amount = Decimal(value)
                except InvalidOperation as exc:
                    raise ValueError(f"Line {line}: invalid {field}") from exc
                if not amount.is_finite() or amount < 0 or amount != amount.quantize(CENT):
                    raise ValueError(f"Line {line}: invalid monetary precision")
                row[field] = amount
            if row["cost_su"] > row["revenue_su"]:
                raise ValueError(f"Line {line}: cost exceeds revenue; explicitly rejected in demo")
            rows.append(row)
    if not rows:
        raise ValueError("CSV must contain at least one sale")
    return rows


def totals(rows: list[dict]) -> dict:
    revenue = sum((r["revenue_su"] for r in rows), Decimal("0.00"))
    cost = sum((r["cost_su"] for r in rows), Decimal("0.00"))
    budget = sum((r["budget_su"] for r in rows), Decimal("0.00"))
    margin = revenue - cost
    variance = revenue - budget
    return {
        "orders": len(rows), "revenue_su": f"{revenue:.2f}", "cost_su": f"{cost:.2f}",
        "budget_su": f"{budget:.2f}", "margin_su": f"{margin:.2f}",
        "margin_pct": f"{(margin / revenue * 100).quantize(CENT):.2f}" if revenue else None,
        "budget_variance_su": f"{variance:.2f}",
        "budget_variance_pct": f"{(variance / budget * 100).quantize(CENT):.2f}" if budget else None,
    }


def group(rows: list[dict], *fields: str) -> list[dict]:
    buckets = defaultdict(list)
    for row in rows:
        buckets[tuple(row[f] for f in fields)].append(row)
    return [{**dict(zip(fields, values)), **totals(group_rows)}
            for values, group_rows in sorted(buckets.items())]


def report(rows: list[dict]) -> dict:
    output = {
        "fixture": "independent fictional orders; financial units are not a currency",
        "grain": "one row per synthetic order",
        "period": {"start": min(r["sale_date"] for r in rows),
                   "end_inclusive": max(r["sale_date"] for r in rows)},
        "overall": totals(rows),
        "by_month": group(rows, "month"),
        "by_region": group(rows, "region"),
        "by_channel": group(rows, "channel"),
        "by_month_region": group(rows, "month", "region"),
    }
    # Reconcile exact decimals and record counts for each aggregation grain.
    for grouping in ("by_month", "by_region", "by_channel", "by_month_region"):
        summaries = output[grouping]
        if sum(v["orders"] for v in summaries) != len(rows):
            raise AssertionError(f"order counts differ for {grouping}")
        for key in ("revenue_su", "cost_su", "budget_su", "margin_su", "budget_variance_su"):
            if sum((Decimal(v[key]) for v in summaries), Decimal("0")) != Decimal(output["overall"][key]):
                raise AssertionError(f"{key} discrepancy in {grouping}")
    return output


def render_html(rows: list[dict], summary: dict) -> str:
    # JSON is embedded in a script: escape '<' to prevent premature </script> termination.
    payload = json.dumps([{
        "month": r["month"], "region": r["region"], "channel": r["channel"],
        "revenue": float(r["revenue_su"]), "cost": float(r["cost_su"]),
        "budget": float(r["budget_su"])
    } for r in rows], separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    heading = escape("Enterprise Business Intelligence | Synthetic Sales")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{heading}</title><style>
:root{{color-scheme:dark;font-family:system-ui,Segoe UI,sans-serif;background:#090f1d;color:#f2f6ff}}
*{{box-sizing:border-box}}body{{max-width:1120px;margin:auto;padding:clamp(20px,5vw,48px)}}
main{{display:grid;gap:24px}}header{{border-bottom:1px solid #31435b;padding-bottom:24px}}
small,.muted{{color:#aabdd3}}h1{{font-size:clamp(30px,5vw,50px);margin:6px 0}}
label{{display:flex;gap:12px;align-items:center;flex-wrap:wrap}}select{{font:inherit;background:#15243c;color:#f2f6ff;padding:9px 14px;border:1px solid #52708f;border-radius:7px}}
.cards{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}}
.card,.panel{{background:#111d30;border:1px solid #34465c;border-radius:12px;padding:24px}}
.card strong{{font-size:clamp(20px,2.5vw,32px);display:block;margin-top:12px;font-variant-numeric:tabular-nums}}
.card small{{font-size:12px}}h2{{font-size:22px;margin-top:0}}
.bars{{display:grid;gap:13px}}.bar-row{{display:grid;grid-template-columns:90px 1fr 130px;align-items:center;gap:10px}}
.track{{height:18px;border-radius:6px;background:#20324a;overflow:hidden}}
.fill{{height:100%;background:linear-gradient(90deg,#35dce1,#a89aff);border-radius:6px}}
.legend{{color:#9de9eb;font-size:12px}}
table{{width:100%;border-collapse:collapse;text-align:left}}th,td{{padding:10px;border-bottom:1px solid #34465c}}
td:nth-child(n+2){{text-align:right;font-variant-numeric:tabular-nums}}
footer{{color:#aabdd3;font-size:13px}}a{{color:#77e9f0}}:focus-visible{{outline:3px solid #77e9f0}}
@media(max-width:700px){{.cards{{grid-template-columns:repeat(2,1fr)}}.bar-row{{grid-template-columns:65px 1fr 85px}}.card{{padding:13px}}}}
</style></head><body><main><header><small>ORIGINAL ENGINEERING LAB / OFFLINE · SYNTHETIC DATA</small>
<h1>{heading}</h1><p class="muted">An independent fictional reporting exercise. All values are synthetic units, not real currency or client results.</p>
<label for="region">Region filter <select id="region"><option value="All">All regions</option><option>Central</option><option>North</option><option>South</option></select></label></header>
<section class="cards" aria-label="Key performance indicators">
<div class="card"><small>Orders</small><strong id="orders">—</strong></div>
<div class="card"><small>Revenue (SU)</small><strong id="revenue">—</strong></div>
<div class="card"><small>Margin (%)</small><strong id="margin">—</strong></div>
<div class="card"><small>Budget variance (SU)</small><strong id="variance">—</strong></div></section>
<section class="panel"><h2>Monthly Revenue · Fictional Units</h2><div id="bars" class="bars" role="img" aria-label="Monthly revenue bars generated from synthetic order records"></div></section>
<section class="panel"><h2>Regional Breakdown</h2><table><thead><tr><th scope="col">Region</th><th scope="col">Orders</th><th scope="col">Revenue SU</th><th scope="col">Margin SU</th></tr></thead><tbody id="regions"></tbody></table></section>
<footer>Source code, formulas, SQL and report template are documented in the engineering lab. No external calls, tracking, secrets or user data. <a href="https://github.com/Dicureck/Dicureck/tree/main/engineering-labs/enterprise-bi-reporting">Inspect source ↗</a></footer></main>
<script>const SALES={payload};const select=document.getElementById("region");const format=n=>n.toLocaleString("en-US",{{maximumFractionDigits:2,minimumFractionDigits:2}});
function display(){{const rows=SALES.filter(r=>select.value==="All"||r.region===select.value);
const total=k=>rows.reduce((a,r)=>a+r[k],0);
const revenue=total("revenue"),cost=total("cost"),budget=total("budget");
document.getElementById("orders").textContent=rows.length.toLocaleString("en-US");
document.getElementById("revenue").textContent=format(revenue);
document.getElementById("margin").textContent=revenue?format((revenue-cost)/revenue*100)+"%":"N/A";
document.getElementById("variance").textContent=format(revenue-budget);
const months=[...new Set(SALES.map(r=>r.month))].sort();const max=Math.max(1,...months.map(m=>rows.filter(r=>r.month===m).reduce((a,r)=>a+r.revenue,0)));
const bars=document.getElementById("bars");bars.replaceChildren();
for(const m of months){{const amount=rows.filter(r=>r.month===m).reduce((a,r)=>a+r.revenue,0);
const row=document.createElement("div");row.className="bar-row";
const month=document.createElement("span");month.textContent=m;
const track=document.createElement("div");track.className="track";
const fill=document.createElement("div");fill.className="fill";fill.style.width=(100*amount/max).toFixed(1)+"%";track.append(fill);
const label=document.createElement("span");label.className="legend";label.textContent=format(amount);row.append(month,track,label);bars.append(row);}}
const body=document.getElementById("regions");body.replaceChildren();
for(const name of ["Central","North","South"]){{const group=rows.filter(r=>r.region===name);if(!group.length)continue;
const tr=document.createElement("tr");for(const value of [name,String(group.length),format(group.reduce((a,r)=>a+r.revenue,0)),format(group.reduce((a,r)=>a+r.revenue-r.cost,0))]){{const td=document.createElement("td");td.textContent=value;tr.append(td)}}body.append(tr);}}
}}
select.addEventListener("change",display);display();</script></body></html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Synthetic sales reporting, offline only")
    parser.add_argument("--input", type=Path, default=Path(__file__).resolve().parents[1] / "fixtures/sales.csv")
    parser.add_argument("--out", type=Path, default=Path("output/enterprise-bi"))
    args = parser.parse_args()
    rows = read_sales(args.input)
    result = report(rows)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "report.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (args.out / "dashboard.html").write_text(render_html(rows, result), encoding="utf-8")
    print(f"Generated synthetic report: {result['overall']['orders']} rows, {result['overall']['revenue_su']} revenue SU")


if __name__ == "__main__":
    main()
