#!/usr/bin/env python3
"""Refresh only the managed activity block in the GitHub profile README.

The script uses GitHub's public REST API and Python's standard library.
It never merges, pushes, or changes any other README text.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import html
import json
import os
from pathlib import Path
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen

USERNAME = "Manantra"
START = "<!-- PROFILE_ACTIVITY:START -->"
END = "<!-- PROFILE_ACTIVITY:END -->"
API_ROOT = "https://api.github.com"
PR_LINK = re.compile(r"^https://github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)/pull/(\d+)$")
MAX_PRS = 8
MAX_PER_REPO = 3
MAX_REPOS = 5


def github_json(path: str):
    if not path.startswith("/"):
        raise ValueError("Expected GitHub REST API path")
    token = os.environ.get("GH_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Manantra-profile-activity-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(API_ROOT + path, headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def markdown_label(text: str) -> str:
    clean = " ".join(str(text).split())
    clean = clean[:120] + ("…" if len(clean) > 120 else "")
    # Markdown label escaping AND HTML text escaping, for untrusted PR titles.
    clean = html.escape(clean, quote=False)
    return re.sub(r"([\\`*_\[\]()~])", r"\\\1", clean)


def recent_upstream_prs() -> list[dict]:
    query = urlencode({
        "q": f"is:pr is:merged author:{USERNAME}",
        "sort": "updated", "order": "desc", "per_page": "100",
    })
    results = github_json("/search/issues?" + query).get("items", [])
    candidates = []
    for item in results:
        match = PR_LINK.fullmatch(item.get("html_url", ""))
        if not match or match.group(1).lower() == USERNAME.lower():
            continue
        # Fetch actual merged_at, so closed-but-unmerged PRs are never shown
        # and the entries can be sorted by merge date rather than update date.
        details = github_json(f"/repos/{match.group(1)}/{match.group(2)}/pulls/{match.group(3)}")
        merged = details.get("merged_at")
        if not merged:
            continue
        candidates.append({
            "owner": match.group(1), "repo": match.group(2),
            "number": int(match.group(3)),
            "title": item.get("title", "Untitled contribution"),
            "url": item["html_url"], "merged_at": merged,
        })
        if len(candidates) >= 35:
            break
    candidates.sort(key=lambda r: r["merged_at"], reverse=True)
    selected, per_repo = [], Counter()
    for item in candidates:
        key = (item["owner"].lower(), item["repo"].lower())
        if per_repo[key] >= MAX_PER_REPO:
            continue
        selected.append(item)
        per_repo[key] += 1
        if len(selected) >= MAX_PRS:
            break
    return selected


def recently_active_repos() -> list[dict]:
    repos = github_json(f"/users/{USERNAME}/repos?" + urlencode({
        "type": "owner", "sort": "pushed", "direction": "desc", "per_page": "100",
    }))
    return [r for r in repos if
            r.get("owner", {}).get("login", "").lower() == USERNAME.lower()
            and r.get("name", "").lower() != USERNAME.lower()
            and not r.get("fork") and not r.get("archived")
            and not r.get("private")][:MAX_REPOS]


def render_activity(prs: list[dict], repos: list[dict]) -> str:
    lines = [
        "### Recently merged upstream contributions",
        "",
        "Automatically gathered from my merged pull requests in other people's repositories.",
        "",
    ]
    if prs:
        for p in prs:
            repo_label = markdown_label(f"{p['owner']}/{p['repo']}")
            repo_url = f"https://github.com/{p['owner']}/{p['repo']}"
            title = markdown_label(p["title"])
            merged_day = p["merged_at"][:10]
            lines.append(f"- **[{repo_label}]({repo_url})** — [{title} · #{p['number']}]({p['url']}) · merged {merged_day}")
    else:
        lines.append("No recent merged upstream pull requests found.")
    lines += ["", "### Recently active original repositories", ""]
    if repos:
        for r in repos:
            name = markdown_label(r["name"])
            url = f"https://github.com/{USERNAME}/{r['name']}"
            desc = markdown_label(r.get("description") or "Open-source project")
            lines.append(f"- **[{name}]({url})** — {desc}")
    else:
        lines.append("No public original repositories found.")
    lines += [
        "", "<sub>Automated snapshot from the GitHub API. Updates arrive as draft pull requests and are published only after review.</sub>",
    ]
    return "\n".join(lines)


def replace_block(readme: str, generated: str) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must have exactly one start and end marker")
    before, _, rest = readme.partition(START)
    _, _, after = rest.partition(END)
    return f"{before}{START}\n{generated.rstrip()}\n{END}{after}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--check", action="store_true", help="Only verify whether README would change")
    args = parser.parse_args()
    original = args.readme.read_text(encoding="utf-8")
    generated = render_activity(recent_upstream_prs(), recently_active_repos())
    updated = replace_block(original, generated)
    if updated == original:
        print("Profile activity is already up to date.")
        return 0
    if args.check:
        print("Profile activity is out of date.")
        return 1
    args.readme.write_text(updated, encoding="utf-8")
    print("Updated managed activity section in", args.readme)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
