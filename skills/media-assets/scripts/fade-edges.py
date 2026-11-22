#!/usr/bin/env python3
'''边缘淡化/模糊预处理：生成带透明渐隐的 WebP。依赖 Pillow + numpy。'''
import argparse
from pathlib import Path

try:
    import numpy as np
    from PIL import Image, ImageFilter
except ImportError:
    raise SystemExit("需要 Pillow 与 numpy")


def main():
    ap = argparse.ArgumentParser(description="边缘淡化/模糊")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--fade", type=float, default=0.16, help="边缘渐隐比例")
    ap.add_argument("--blur", type=float, default=18, help="模糊半径")
    ap.add_argument("--blur-left", action="store_true", help="仅左侧模糊")
    ap.add_argument("--quality", type=int, default=82)
    args = ap.parse_args()

    img = Image.open(args.src).convert("RGB")
    w, h = img.size
    blurred = img.filter(ImageFilter.GaussianBlur(args.blur))
    yy, xx = np.mgrid[0:h, 0:w]

    if args.blur_left:
        sharp = np.clip((xx / w - 0.04) / 0.26, 0, 1)
    else:
        cx, cy = w / 2, h / 2
        r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / np.sqrt(cx ** 2 + cy ** 2)
        sharp = np.clip((0.85 - r) / 0.40, 0, 1)

    mixed = Image.composite(img, blurred, Image.fromarray((sharp * 255).astype(np.uint8)))

    dx = np.minimum(xx, w - 1 - xx) / (w * args.fade)
    dy = np.minimum(yy, h - 1 - yy) / (h * args.fade)
    alpha = np.clip(np.minimum(np.minimum(dx, dy), 1.0), 0, 1) ** 1.4
    out = mixed.convert("RGBA")
    out.putalpha(Image.fromarray((alpha * 255).astype(np.uint8)))
    Path(args.dst).parent.mkdir(parents=True, exist_ok=True)
    out.save(args.dst, "WEBP", quality=args.quality, method=6)
    print("saved", args.dst, Path(args.dst).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
