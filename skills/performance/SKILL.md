---
name: website-performance
description: 性能预算与优化：测基线、图片/字体/背景/依赖/第三方脚本优化、复测达标。用户说"加载慢/太重/Lighthouse 低/上线前优化"时用；新功能不要用。
---

# 性能优化流

1. 定预算（默认见 `references/budgets.md`）。
2. 测基线：总重、首屏图、字体、JS/CSS gzip、Lighthouse 移动分（`scripts/page-weight.py`）。
3. 按性价比优化：图片 → 字体子集 → 背景分断点 → 去未用依赖 → CSS 收敛 → 第三方延迟。
4. 同法复测，记录 before/after。
5. 未达标继续优化或向用户说明取舍。

预算与反模式见 `references/budgets.md`。边界：遵守总纲 §8；Lighthouse 先确认环境。
