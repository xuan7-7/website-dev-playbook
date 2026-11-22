# 维护、依赖与复核

## 版本信息

- 当前版本：1.2.0
- 最后验证：2026-11-23
- 适配范围：静态内容站（Astro/Hugo/Eleventy/纯 HTML）+ GitHub Pages 类静态托管
- 变更记录：`CHANGELOG.md`

## 依赖表

| 位置 | 依赖 | 缺失时 |
|---|---|---|
| 技能本身 | 无 | — |
| `media-assets/scripts/compress-images.py` | Pillow | 先问用户是否允许安装，或改用系统图像工具 |
| `media-assets/scripts/fade-edges.py` | Pillow + numpy | 同上 |
| `media-assets/scripts/font-subset.py` | fonttools（含 brotli） | 同上 |
| `performance/scripts/page-weight.py` | 仅标准库 | — |
| `qa-launch/scripts/check-links.py` | 仅标准库 | — |
| `scripts/check-skill-budget.py` | 仅标准库 | — |
| `scripts/check-orphan-assets.py` | 仅标准库 | — |
| Lighthouse 相关 | 浏览器/Node 环境 | 先确认可用，不擅自安装 |

## 复核清单（触发后逐项过）

- [ ] 框架/托管平台是否大版本升级（Astro、GitHub Actions、Pages 规则）
- [ ] 描述的触发词是否仍符合用户说法（跑 `references/evals.md`）
- [ ] 子技能之间描述是否重叠（同一句症状被两个技能抢）
- [ ] 脚本是否仍可运行（`--help` + 一个小样本）
- [ ] 文档中的命令/版本是否过时
- [ ] 本次复核后更新版本号、日期、CHANGELOG
