# 性能预算与反模式

| 项目 | 预算（静态博客参考） | 测量方法 |
|---|---|---|
| 首屏 JS | ≤60KB gzip | 构建产物/DevTools |
| CSS | ≤30KB gzip | 构建产物 |
| 字体 | ≤150KB 总量 | woff2 文件大小 |
| 首屏图片 | ≤150KB | 图片文件 |
| 页面总重 | ≤400KB | DevTools Network |
| 本地加载 | ≤1.5s | 本地预览计时 |
| Lighthouse 移动 | Performance ≥85 | Lighthouse |

## 高收益顺序

1. 图片压到 WebP + 正确尺寸
2. 字体子集化
3. 背景图按断点加载 + preload
4. 去掉未用依赖/大库；图标按需引入
5. CSS 只在 base 层写元素样式
6. 第三方脚本延迟加载，失败不阻塞

## 反模式

首屏塞大图、整包引入图标库、每页重复引入字体、`backdrop-filter` 满屏、统计脚本同步加载、base64 内联大图。
