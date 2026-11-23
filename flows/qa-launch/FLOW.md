# 验证上线流

1. 构建通过；锁文件已提交；`node_modules` 未入库。
2. 链接：内部链接走 `url()`；`flows/qa-launch/scripts/check-links.py dist` 扫 404。
3. 逐页按 `flows/qa-launch/assets/qa-checklist.md` 勾选（亮暗、390px、空状态、无开发日志）。
4. 交互：二级导航点空白/Esc 收起；头部单行；主题持久无闪；统计失败不影响页面。
5. 本地预览给用户，确认「推」后才部署。
6. 线上验证：关键页 200、元素存在、强刷正常（`flows/qa-launch/references/live-verify.md`）。

边界：遵守总纲 §8；线上只读验证。
