"""Synthetic reporting + dry-run email; explicitly approved, optional AI review."""
from __future__ import annotations

import argparse
import csv
import html
import json
import os
import random
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

CHANNELS = ("Digital", "Retail", "Wholesale")
CURRENCIES = ("SU",)


def synthetic_records(seed: int = 2026) -> list[dict]:
    rng = random.Random(seed)
    return [
        {
            "id": f"SYN-{i:04d}",
            "month": f"2026-{month:02d}",
            "channel": channel,
            "amount": rng.randint(90, 990),
        }
        for month in range(1, 5)
        for channel in CHANNELS
        for i in range((month - 1) * 9 + CHANNELS.index(channel) * 3 + 1,
                       (month - 1) * 9 + CHANNELS.index(channel) * 3 + 4)
    ]


def summarize(records: list[dict]) -> dict:
    seen = set()
    grouped = defaultdict(lambda: {"orders": 0, "revenue_su": 0})
    for record in records:
        if not isinstance(record, dict) or any(
            field not in record for field in ("id", "month", "channel", "amount")
        ):
            raise ValueError("missing synthetic record field")
        record_id, month, channel, amount = (
            record["id"], record["month"], record["channel"], record["amount"]
        )
        if not isinstance(record_id, str) or not record_id.strip():
            raise ValueError("invalid synthetic record ID")
        if record_id in seen:
            raise ValueError("duplicate synthetic ID")
        seen.add(record_id)
        if not isinstance(month, str) or not re.fullmatch(r"[0-9]{4}-(0[1-9]|1[0-2])", month):
            raise ValueError("invalid synthetic report month")
        if channel not in CHANNELS or type(amount) is not int or amount < 0:
            raise ValueError("invalid synthetic record")
        key = (month, channel)
        grouped[key]["orders"] += 1
        grouped[key]["revenue_su"] += amount
    if not records:
        raise ValueError("report requires at least one synthetic record")
    by_month_channel = [
        {"month": month, "channel": channel, **stats}
        for (month, channel), stats in sorted(grouped.items())
    ]
    return {
        "dataset": "FICTIONAL / NOT ACTUAL BUSINESS DATA",
        "unit": "synthetic units",
        "rows": len(records),
        "revenue_su": sum(item["revenue_su"] for item in by_month_channel),
        "by_month_channel": by_month_channel,
    }


def render_report(report: dict) -> str:
    rows = "\n".join(
        "<tr>" + "".join(f"<td>{html.escape(str(row[field]))}</td>"
                        for field in ("month", "channel", "orders", "revenue_su")) + "</tr>"
        for row in report["by_month_channel"]
    )
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Synthetic Revenue Brief</title>
<style>
body{{background:#0a1020;color:#e7f4fc;font:16px/1.5 system-ui;margin:0;padding:38px}}
main{{max-width:930px;margin:auto}}h1{{color:#85eaf1}}.badge{{color:#b9a5ff}}
table{{border-collapse:collapse;width:100%;margin-top:22px}}th,td{{border:1px solid #39485e;padding:10px;text-align:left}}
th{{background:#14263c}}tr:nth-child(even){{background:#101e30}}
</style></head><body><main>
<p class="badge">ENGINEERING LAB / FICTIONAL DATA</p>
<h1>Automated Revenue Brief</h1><p>Original synthetic dataset; no confidential data or live email sends.</p>
<p><strong>{report["rows"]}</strong> records · <strong>{report["revenue_su"]:,}</strong> synthetic units</p>
<table><caption>Monthly revenue by fictional channel</caption><thead><tr>
<th scope="col">Month</th><th scope="col">Channel</th><th scope="col">Orders</th><th scope="col">Revenue (SU)</th>
</tr></thead><tbody>{rows}</tbody></table>
<p>Generated for demonstration only. Values are not business forecasts.</p>
</main></body></html>"""


def email_preview(report: dict) -> str:
    msg = EmailMessage()
    msg["From"] = "demo@example.invalid"
    msg["To"] = "reviewer@example.invalid"
    msg["Subject"] = "[DRY RUN] Synthetic monthly report — approval required"
    msg.set_content(
        f"This is an unsent email preview.\n"
        f"Fictional rows: {report['rows']}\n"
        f"Fictional revenue: {report['revenue_su']} synthetic units.\n"
        "No SMTP connection exists in this lab.\n"
    )
    return msg.as_string()


def ai_review(report: dict, provider: str, allow_network: bool, approved: bool) -> str:
    if not (allow_network and approved):
        raise PermissionError("AI API access requires --allow-network and --approved")
    config = {
        "openai": ("OPENAI_API_KEY", "OPENAI_MODEL", "https://api.openai.com/v1/responses"),
        "anthropic": ("ANTHROPIC_API_KEY", "ANTHROPIC_MODEL", "https://api.anthropic.com/v1/messages"),
    }
    if provider not in config:
        raise ValueError("unsupported AI provider")
    key_env, model_env, endpoint = config[provider]
    key, model = os.getenv(key_env), os.getenv(model_env)
    if not key or not model:
        raise ValueError(f"set both {key_env} and {model_env} (never commit them)")
    safe_payload = json.dumps({
        "unit": report["unit"],
        "rows": report["rows"],
        "revenue_su": report["revenue_su"],
        "by_month_channel": report["by_month_channel"],
    }, sort_keys=True)
    prompt = ("Review this fictional aggregate report. Write 3 brief observations, "
              "mention limitations, and do not invent business context:\n" + safe_payload)
    if provider == "openai":
        data = {"model": model, "input": prompt, "max_output_tokens": 450}
        headers = {"Authorization": f"Bearer {key}"}
    else:
        data = {"model": model, "max_tokens": 450, "messages": [{"role": "user", "content": prompt}]}
        headers = {"x-api-key": key, "anthropic-version": "2023-06-01"}
    req = urllib.request.Request(
        endpoint, data=json.dumps(data).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = json.load(response)
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError("AI request failed; review network/configuration") from exc
    if provider == "openai":
        parts = [part.get("text", "") for item in payload.get("output", [])
                 for part in item.get("content", []) if part.get("type") == "output_text"]
    else:
        parts = [part.get("text", "") for part in payload.get("content", [])
                 if part.get("type") == "text"]
    narrative = "\n".join(parts).strip()
    if not narrative:
        raise ValueError("provider returned no readable text")
    return narrative


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("output/ai-demo"))
    parser.add_argument("--provider", choices=("none", "openai", "anthropic"), default="none")
    parser.add_argument("--allow-network", action="store_true")
    parser.add_argument("--approved", action="store_true")
    args = parser.parse_args(argv)
    if args.provider != "none" and not (args.allow_network and args.approved):
        parser.error("provider requires --allow-network and --approved")
    report = summarize(synthetic_records())
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (args.output / "report.html").write_text(render_report(report), encoding="utf-8")
    (args.output / "email-preview.eml").write_text(email_preview(report), encoding="utf-8")
    audit = {"workflow": "synthetic-report", "send_email": False,
             "provider": args.provider, "status": "dry-run" if args.provider == "none" else "ai-review-only"}
    if args.provider != "none":
        # Only synthetic aggregate data is sent; provider output is never emailed automatically.
        narrative = ai_review(report, args.provider, args.allow_network, args.approved)
        (args.output / "untrusted-ai-review.txt").write_text(narrative + "\n", encoding="utf-8")
    (args.output / "workflow-audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print("Generated original synthetic report and UNSENT email preview at", args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
