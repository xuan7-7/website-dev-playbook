---
name: website-deployment
description: 静态托管部署（GitHub Pages 参考）：site/base、workflow、推送协议、失败排查、线上验证。用户说"部署/上线/推上去/部署后404/工作流失败"时用；本地开发不要用。
---

# 部署流

1. `site` 域名正确；子路径填 `base: '/<repo>'`；资源全走 `url()`。
2. Settings → Pages → Source 选 GitHub Actions；确认分支。
3. 复制 `assets/workflow.yml`，改构建命令/产物目录；锁文件提交。
4. 本地 build + 预览，确认子路径全通。
5. 本地预览给用户 → 确认「推」→ commit+push → 等 Actions 成功。
6. 线上验证：关键页 200、元素存在、禁用缓存核对新 CSS（见 `references/live-verify.md`）；失败读日志修一处再重试。

设置与排查见 `references/pages-settings.md`。边界：遵守总纲 §8；不擅自改仓库设置。
