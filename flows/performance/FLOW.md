# 性能优化流

1. 定预算（默认见 `flows/performance/references/budgets.md`）。
2. 测基线：总重、首屏图、字体、JS/CSS gzip、Lighthouse 移动分（`flows/performance/scripts/page-weight.py`）。
3. 按性价比优化：图片 → 字体子集 → 背景分断点 → 去未用依赖 → CSS 收敛 → 第三方延迟。
4. 同法复测，记录 before/after。
5. 未达标继续优化或向用户说明取舍。

预算与反模式见 `references/budgets.md`。边界：遵守总纲 §8；Lighthouse 先确认环境。
