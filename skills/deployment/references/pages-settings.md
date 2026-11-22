# GitHub Pages 设置与失败排查

## 仓库设置
- Settings → Pages → Build and deployment → Source: GitHub Actions
- 确认 workflow 的 `on.push.branches` 与实际默认分支一致
- 自定义域：先在 Pages 填域名，再加 CNAME 记录

## 常见失败

| 现象 | 根因 | 修法 |
|---|---|---|
| 资源 404 | 绝对路径/未配 base | 全站 `url()`；检查 `base` |
| 部署无权限 | Pages 未开 / workflow 权限缺 | 开 Pages；补 `permissions` |
| workflow 不触发 | 分支名不匹配 / 仓库禁用 Actions | 改 branches；检查 Actions 设置 |
| 构建失败 | 依赖缺失 / 私有 registry | 本地先构建通过；锁文件用公共源 |
| 页面 404 | base 与路由不匹配 | 检查 base、尾部斜杠、链接生成 |
| 更新不生效 | 缓存 / workflow 未跑 | 强刷；确认 Actions 成功记录 |
