#!/usr/bin/env python3
"""Render GitHub public repository telemetry to a standalone SVG.

No third-party image services, no dependencies beyond the Python standard library.
Statistics concern public GitHub repositories, not professional experience.
"""

from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

USER = "Dicureck"
OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "telemetry.svg"
API = "https://api.github.com"


def get_json(path: str, token: str = ""):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Dicureck-portfolio-telemetry", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(f"{API}{path}", headers=headers)
    with urlopen(req, timeout=30) as response:
        return json.load(response)


def collect_metrics(user: str, get=get_json):
    repos = []
    for page in range(1, 11):
        batch = get(f"/users/{user}/repos?type=owner&sort=updated&per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("Unexpected GitHub API response for repository list")
        repos.extend(batch)
        if len(batch) < 100:
            break
    public = [r for r in repos if not r.get("private") and not r.get("fork") and not r.get("archived")]
    skills_bytes = {}
    for repo in public:
        if repo.get("name", "").lower() == user.lower():
            continue  # A profile README is not a programming project.
        owner = repo.get("owner", {}).get("login", user)
        name = repo["name"]
        language_data = get(f"/repos/{owner}/{name}/languages")
        if not isinstance(language_data, dict):
            raise ValueError(f"Unexpected language payload for {name}")
        for language, size in language_data.items():
            skills_bytes[language] = skills_bytes.get(language, 0) + int(size)
    return {
        "public_repos": len(public),
        "stars": sum(int(r.get("stargazers_count") or 0) for r in public),
        "languages": sorted(skills_bytes.items(), key=lambda x: (-x[1], x[0])),
        "active_linguist_repos": sum(1 for r in public if r.get("language")),
    }


def render_svg(metrics: dict, updated: dt.datetime | None = None) -> str:
    updated = updated or dt.datetime.now(dt.timezone.utc)
    date = escape(updated.strftime("%d %b %Y · %H:%M UTC"))
    langs = metrics["languages"][:5]
    total = sum(v for _, v in metrics["languages"])
    palette = ["#48D9FF", "#8B98FF", "#B68DFF", "#44C8B5", "#F2BE7A"]
    rows = []
    if total:
        for i, (language, count) in enumerate(langs):
            pct = count / total * 100
            bar_w = max(4, 490 * pct / 100)
            y = 190 + i * 30
            rows.append(f'<text x="300" y="{y+13}" font-size="15" fill="#DDE6FA">{escape(language[:18])}</text>')
            rows.append(f'<rect x="465" y="{y}" width="490" height="15" rx="7" fill="#1B2949"/>')
            rows.append(f'<rect x="465" y="{y}" width="{bar_w:.1f}" height="15" rx="7" fill="{palette[i]}"/>')
            rows.append(f'<text x="965" y="{y+13}" text-anchor="end" font-size="14" fill="#B8C8E5">{pct:.1f}%</text>')
    else:
        rows.append('<text x="305" y="236" font-size="17" fill="#B8C8E5">GitHub is indexing repository languages.</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="375" viewBox="0 0 1000 375" role="img" aria-label="GitHub portfolio repository telemetry">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#10182B"/><stop offset="1" stop-color="#1A1634"/></linearGradient>
    <linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#4DDCFF"/><stop offset="1" stop-color="#AF8CFF"/></linearGradient>
  </defs>
  <rect x="1" y="1" width="998" height="373" rx="16" fill="url(#bg)" stroke="#324468" stroke-width="2"/>
  <rect x="35" y="35" width="5" height="48" rx="2" fill="url(#a)"/>
  <text x="58" y="56" fill="#EFF5FF" font-size="24" font-weight="bold" font-family="DejaVu Sans, Arial, sans-serif">PUBLIC REPOSITORY TELEMETRY</text>
  <text x="58" y="78" fill="#8CADD1" font-size="13" font-family="DejaVu Sans, Arial, sans-serif">Source: GitHub public API · {date}</text>
  <line x1="275" y1="105" x2="275" y2="335" stroke="#33435F"/>
  <text x="45" y="157" fill="#58D9FF" font-size="46" font-weight="bold" font-family="DejaVu Sans, Arial, sans-serif">{metrics['public_repos']}</text>
  <text x="45" y="183" fill="#B8C8E5" font-size="16" font-family="DejaVu Sans, Arial, sans-serif">PUBLIC REPOSITORIES</text>
  <text x="45" y="272" fill="#B58CFF" font-size="46" font-weight="bold" font-family="DejaVu Sans, Arial, sans-serif">{metrics['stars']}</text>
  <text x="45" y="298" fill="#B8C8E5" font-size="16" font-family="DejaVu Sans, Arial, sans-serif">TOTAL STARS</text>
  <text x="300" y="150" fill="#DDE6FA" font-size="19" font-weight="bold" font-family="DejaVu Sans, Arial, sans-serif">Languages in public repository code</text>
  <g font-family="DejaVu Sans, Arial, sans-serif">{''.join(rows)}</g>
  <text x="300" y="345" fill="#8CADD1" font-size="12" font-family="DejaVu Sans, Arial, sans-serif">Code-byte distribution. Not a proficiency ranking or career experience metric.</text>
</svg>'''


def main():
    user = os.environ.get("PORTFOLIO_GITHUB_USER", USER)
    token = os.environ.get("GITHUB_TOKEN", "")
    # Adapter so tests can pass an API function without credentials.
    metrics = collect_metrics(user, lambda path: get_json(path, token))
    content = render_svg(metrics)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Rendered {OUTPUT.name}: {metrics['public_repos']} public repos, {len(metrics['languages'])} detected languages")


if __name__ == "__main__":
    main()
