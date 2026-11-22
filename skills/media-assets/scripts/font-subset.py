#!/usr/bin/env python3
'''按字符集生成 woff2 子集。需要 fonttools（pip install fonttools brotli）。'''
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="字体子集化")
    ap.add_argument("font", help="源字体 ttf/otf")
    ap.add_argument("out", help="输出 woff2 路径")
    ap.add_argument("--text-file", required=True, help="包含全站用字的文本文件")
    args = ap.parse_args()

    chars = Path(args.text_file).read_text(encoding="utf-8")
    uniq = "".join(dict.fromkeys(chars))
    tmp = Path(args.out).with_suffix(".chars.txt")
    tmp.write_text(uniq, encoding="utf-8")
    cmd = [
        sys.executable, "-m", "fontTools.subset", args.font,
        f"--text-file={tmp}", "--flavor=woff2", f"--output-file={args.out}",
        "--layout-features=*", "--no-hinting", "--desubroutinize",
    ]
    subprocess.run(cmd, check=True)
    tmp.unlink(missing_ok=True)
    print("saved", args.out, Path(args.out).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
