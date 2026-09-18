#!/usr/bin/env python3
"""Submit changed site URLs to IndexNow.

Designed for GitHub Actions on pushes to main. With --all it submits every
URL in sitemap.xml; otherwise it maps changed HTML files between two commits
to their canonical public URLs and submits only those URLs.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HOST = "diegojplopez.com"
BASE = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"
ROOT = Path(__file__).resolve().parents[1]
KEY_FILE = ROOT / "f7feadb4bf9e0f91e49dcd381e947601.txt"
SITEMAP = ROOT / "sitemap.xml"


def key_value() -> str:
    key = KEY_FILE.read_text(encoding="utf-8").strip()
    if not (8 <= len(key) <= 128) or not all(c.isalnum() or c == "-" for c in key):
        raise ValueError("IndexNow key file is missing or malformed")
    return key


def url_for_repo_path(path: str) -> str | None:
    path = path.replace("\\", "/").lstrip("./")
    if path == "index.html":
        return BASE + "/"
    if path.endswith("/index.html"):
        return BASE + "/" + path[: -len("index.html")]
    if path.endswith(".html"):
        return BASE + "/" + path
    return None


def changed_urls(before: str, after: str) -> list[str]:
    cmd = ["git", "diff", "--name-only", before, after, "--", "*.html"]
    result = subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True, text=True)
    urls = {url for line in result.stdout.splitlines() if (url := url_for_repo_path(line.strip()))}
    return sorted(urls)


def sitemap_urls() -> list[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(SITEMAP)
    return sorted({n.text.strip() for n in tree.findall(".//sm:loc", ns) if n.text})


def submit(urls: list[str], *, dry_run: bool = False) -> int:
    if not urls:
        print("No changed HTML URLs to submit.")
        return 0

    key = key_value()
    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": f"{BASE}/{key}.txt",
        "urlList": urls,
    }
    print("IndexNow URLs:")
    for url in urls:
        print(f"  {url}")

    if dry_run:
        print("Dry run only; no request sent.")
        return 0

    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "diegojplopez-site-indexnow/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            code = response.getcode()
            body = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        code = exc.code
        body = exc.read().decode("utf-8", errors="replace")

    print(f"IndexNow response: HTTP {code}")
    if body:
        print(body[:1000])

    # 200 = accepted; 202 = accepted with key validation pending.
    return 0 if code in (200, 202) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", help="Git commit before the push")
    parser.add_argument("--after", help="Git commit after the push")
    parser.add_argument("--all", action="store_true", help="Submit every URL in sitemap.xml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.all:
        urls = sitemap_urls()
    else:
        if not args.before or not args.after:
            parser.error("--before and --after are required unless --all is used")
        urls = changed_urls(args.before, args.after)

    return submit(urls, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
