# CHANGELOG

## 1.4.1 — 2026-11-23
- 新增发布必需文件：`README.md`、`LICENSE`（MIT）、`.gitignore`
- frontmatter 增加 `license` 字段

## 1.4.0 — 2026-11-23
- 补 BASE 路径判断陷阱（scaffold + 故障表）
- 更新 GitHub Pages workflow 模板为实测可用版本（checkout v7 / withastro v6 / deploy-pages v5）
- 新增 `references/content-model.md`（字段默认值、分类编号、前后篇、视图持久化）
- 新增 `references/counters.md`（第三方计数器 id 唯一、失败降级、计数口径）
- 线上验证补状态码检查与禁用缓存核对（qa/live-verify + deployment）
- 新增 `scripts/check-orphan-assets.py`（孤儿资产审计）

## 1.3.0 — 2026-11-23
- 子技能 SKILL.md 压缩到 ≤15 行（步骤合并，细节留在 references）
- 总纲阶段流程 A–G 移入 `references/phases.md`，总纲只保留路由与原则
- 新增 `scripts/check-skill-budget.py`：行数/估算 token 预算检查（总纲 110L/2800tok，子技能 15L/320tok）

## 1.2.0 — 2026-11-23
- 新增「安全边界」与「维护与版本」章节（总纲 §8、§9）
- 各子技能补充边界声明
- 新增 `references/maintenance.md`（依赖表、复核清单）
- 新增「不含网站美化」边界声明

## 1.1.0 — 2026-11-23
- 拆分为总纲 + 8 个专题子技能（暗色、响应式、图片、性能、验证、部署、故障、决策）
- 新增 `references/`（骨架、评测、案例）、`assets/`（清单/模板/workflow）、`scripts/`（5 个）
- 新增案例层：索引 + 10 条 CASE（通用条目引用）

## 1.0.0 — 2026-11-23
- 初版：核心原则 + 阶段流程 + 工程骨架
