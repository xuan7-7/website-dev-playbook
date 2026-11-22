#!/usr/bin/env python3
# 检查 SKILL.md 行数与估算 token 是否超预算。
import re
import sys
from pathlib import Path

BUDGET = {"main": (110, 2800), "sub": (15, 320)}


def est(text):
    cjk = len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff]", text))
    return round(cjk + (len(text) - cjk) / 3.5)


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    rows = []
    for p in sorted(root.rglob("SKILL.md")):
        text = p.read_text(encoding="utf-8")
        lines = len(text.rstrip("\n").split("\n"))
        kind = "main" if p.parent == root else "sub"
        max_lines, max_tok = BUDGET[kind]
        tok = est(text)
        status = "OK" if lines <= max_lines and tok <= max_tok else "OVER"
        rows.append((str(p.relative_to(root)), lines, tok, max_lines, max_tok, status))
    for name, lines, tok, ml, mt, status in rows:
        print(f"{name:44} {lines:3}L {tok:5}tok  budget {ml}L/{mt}tok  {status}")
    bad = [r for r in rows if r[5] == "OVER"]
    print("超预算:", len(bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
