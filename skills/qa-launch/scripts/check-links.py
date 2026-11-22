#!/usr/bin/env python3
'''粗略检查 dist 内站内链接目标是否存在（HTML href/src 相对/根路径）。'''
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not root.is_dir():
        raise SystemExit(f"目录不存在: {root}")
    bad = []
    for page in root.rglob("*.html"):
        text = page.read_text(encoding="utf-8", errors="ignore")
        for raw in LINK_RE.findall(text):
            if raw.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "javascript:")):
                continue
            path = unquote(urlparse(raw).path)
            if not path:
                continue
            target = root / path.lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                bad.append((page.relative_to(root), raw))
    if bad:
        print(f"发现 {len(bad)} 个可能失效的站内链接：")
        for page, raw in bad[:50]:
            print(f"  {page} -> {raw}")
        sys.exit(1)
    print("站内链接检查通过")


if __name__ == "__main__":
    main()
