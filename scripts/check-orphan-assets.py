#!/usr/bin/env python3
# 扫描 public 下未被 src 引用的资源（孤儿资产）。
import argparse
import sys
from pathlib import Path

EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".svg", ".ico", ".woff2", ".woff", ".ttf"}


def main():
    ap = argparse.ArgumentParser(description="检查未被引用的静态资源")
    ap.add_argument("--src", default="src")
    ap.add_argument("--public", default="public")
    args = ap.parse_args()
    src, public = Path(args.src), Path(args.public)
    if not src.is_dir() or not public.is_dir():
        raise SystemExit("src 或 public 目录不存在")
    text = ""
    for p in src.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".astro", ".ts", ".js", ".tsx", ".jsx", ".md", ".mdx", ".css", ".json", ".yml", ".yaml"}:
            text += p.read_text(encoding="utf-8", errors="ignore")
    orphans = []
    for f in sorted(public.rglob("*")):
        if f.is_file() and f.suffix.lower() in EXTS:
            rel = "/" + f.relative_to(public).as_posix()
            if f.name not in text and rel not in text:
                orphans.append(rel)
    if orphans:
        print("未被引用的资源：")
        for o in orphans:
            print(" ", o)
        sys.exit(1)
    print("资源引用检查通过")


if __name__ == "__main__":
    main()
