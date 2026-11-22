#!/usr/bin/env python3
'''统计静态构建产物体积：总量、图片、字体、JS、CSS。'''
import argparse
from collections import defaultdict
from pathlib import Path

BUDGETS = {
    "image": 150 * 1024,
    "font": 150 * 1024,
    "js": 60 * 1024,
    "css": 30 * 1024,
}


def group(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".svg"}:
        return "image"
    if ext in {".woff2", ".woff", ".ttf", ".otf"}:
        return "font"
    if ext == ".js":
        return "js"
    if ext == ".css":
        return "css"
    return "other"


def main():
    ap = argparse.ArgumentParser(description="构建产物体积统计")
    ap.add_argument("dir", nargs="?", default="dist")
    args = ap.parse_args()
    root = Path(args.dir)
    if not root.is_dir():
        raise SystemExit(f"目录不存在: {root}")
    sizes = defaultdict(int)
    for p in root.rglob("*"):
        if p.is_file():
            sizes[group(p)] += p.stat().st_size
    total = sum(sizes.values())
    for k, v in sorted(sizes.items(), key=lambda kv: -kv[1]):
        budget = BUDGETS.get(k)
        mark = ""
        if budget:
            mark = " OK" if v <= budget else f" OVER(>{budget//1024}KB)"
        print(f"{k:6} {v/1024:8.1f}KB{mark}")
    print(f"total  {total/1024:8.1f}KB")


if __name__ == "__main__":
    main()
