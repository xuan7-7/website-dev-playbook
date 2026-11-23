#!/usr/bin/env python3
'''批量图片转 WebP 并压体积。依赖 Pillow。'''
import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("需要 Pillow：pip install pillow")


def main():
    ap = argparse.ArgumentParser(description="批量图片转 WebP")
    ap.add_argument("src", help="源目录")
    ap.add_argument("dst", help="输出目录")
    ap.add_argument("--max-side", type=int, default=1600)
    ap.add_argument("--quality", type=int, default=76)
    ap.add_argument("--target-kb", type=int, default=0, help="超过则自动降质量")
    args = ap.parse_args()

    src, dst = Path(args.src), Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)
    exts = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp"}
    total = 0
    for f in sorted(src.rglob("*")):
        if f.suffix.lower() not in exts:
            continue
        im = Image.open(f)
        if max(im.size) > args.max_side:
            ratio = args.max_side / max(im.size)
            im = im.resize((round(im.width * ratio), round(im.height * ratio)), Image.LANCZOS)
        q = args.quality
        out = dst / (f.stem + ".webp")
        while True:
            im.save(out, "WEBP", quality=q, method=6)
            size = out.stat().st_size
            if not args.target_kb or size <= args.target_kb * 1024 or q <= 40:
                break
            q -= 6
        total += out.stat().st_size
        print(f"{f.name} -> {out.name} {size/1024:.1f}KB q={q}")
    print(f"共 {total/1024:.1f}KB")


if __name__ == "__main__":
    main()
