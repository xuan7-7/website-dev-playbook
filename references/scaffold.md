# 工程骨架与 URL 约定

## 目录结构（静态站参考）

```
src/
  layouts/Base.astro        # 头、导航、页脚、主题切换、统计脚本
  components/               # 卡片、标签、分类导航、图标
  pages/                    # 路由
  content.config.ts         # collections schema（字段默认值）
  styles/global.css         # @theme token + base 层 + 暗色覆盖
  utils/url.ts              # 统一加 base 前缀
public/assets/              # 图片、图标、下载物
assets-src/                 # 原图（不部署）
```

## url() 约定（子路径部署必做）

```ts
const base = import.meta.env.BASE_URL.replace(/\/$/, '');
export const url = (p: string) => `${base}${p.startsWith('/') ? p : `/${p}`}`;
```

所有 `href`/`src` 走 `url()`，否则 GitHub Pages 等子路径部署必 404。

## 样式工程注意

- 自定义 token 放 `@theme`；基础元素样式放 `@layer base`，别裸写覆盖 utility
- **动态拼接的 class 不会被编译**（如运行期 `classList.toggle('bg-[#2b2333]')`）→ 改用固定 CSS 类（`.cat-tab.is-active`）
- 任意值颜色会绕过主题变量，暗色模式用属性选择器覆盖或改成 token
- 同一元素上 `!important` 的通用规则会压过状态类，状态类也要 `!important`（见案例 0004）

## BASE 路径判断

`document.location.pathname` 在子路径部署时会带 base 前缀（如 `/repo/notes/`），直接 `pathname.startsWith("/notes")` 会匹配失败：

- 先剥 base 再判断：`const p = location.pathname.slice(base.length) || "/"`
- 统一使用剥后的路径，不要混用含 base / 不含 base 的字符串
- 生成链接仍然走 `url()`，两者职责分开
