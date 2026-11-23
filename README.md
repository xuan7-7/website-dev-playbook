# website-dev-playbook

面向**静态内容站**的建站技能：把「需求 → 技术栈确认 → 骨架 → 设计系统 → 页面 → 性能 → 验证部署」拆成可执行流程，并带案例库、检查清单与可选脚本。

## 边界（先读这条）

- **美化**：先了解用户的美化需求与风格主题；有美化类技能/插件就交给它，没有时按用户给的风格/主题执行阶段 D 的「美化流程」。主体仍负责结构、功能、性能与上线。
- **不包含后端能力**：登录、支付、实时协作、SSR/数据库不适用。
- **未经实测的内容不写成硬规则**：需要时先做小样验证，再写入流程。

## 安装

### 方式一：DSH 技能库（推荐）

技能库面板 → 安装 → 粘贴本仓库地址（或上传整个仓库 zip）；不要只装单个 `SKILL.md`，否则会缺 `flows/`、`references/`。安装后热加载。

### 方式二：手动放入技能目录

```powershell
Copy-Item -Recurse .\website-dev-playbook "$env:USERPROFILE\.dsh\skills\website-dev-playbook"
```

重启 DSH（或触发技能重新扫描）后生效。

## 触发示例

- "帮我做一个静态博客 / 作品集 / 落地页"
- "手机上标题换行了 / 页面能左右拖"
- "暗色模式下字看不清 / 选中项看不出"
- "图片加载太慢 / 图片被裁掉了"
- "上线前帮我检查一遍"
- "部署后样式丢了 / 部署到 GitHub Pages"

## 结构（单技能 + 内部流程）

```
website-dev-playbook/
├── SKILL.md                     总纲：原则、阶段、路由（唯一技能入口）
├── flows/                       9 条内部流程（资源文件，不单独收录）
│   ├── dark-mode/FLOW.md
│   ├── responsive-navigation/FLOW.md
│   ├── mobile-adaptation/FLOW.md
│   ├── media-assets/FLOW.md
│   ├── performance/FLOW.md
│   ├── qa-launch/FLOW.md
│   ├── deployment/FLOW.md
│   ├── troubleshooting/FLOW.md
│   └── decision-options/FLOW.md
├── references/                  按需读取的长文（骨架、内容模型、计数、评测、案例）
├── scripts/                     可选脚本
└── CHANGELOG.md
```

技能入口只有根目录 `SKILL.md` 一个；`flows/` 下是内部流程文件（`FLOW.md`，不是 `SKILL.md`），不参与技能发现。

## 可选脚本

| 脚本 | 用途 | 依赖 |
|---|---|---|
| `flows/media-assets/scripts/compress-images.py` | 批量转 WebP + 压体积 | Pillow |
| `flows/media-assets/scripts/fade-edges.py` | 边缘淡化/模糊 + 透明 WebP | Pillow + numpy |
| `flows/media-assets/scripts/font-subset.py` | 按用字生成 woff2 子集 | fonttools |
| `flows/performance/scripts/page-weight.py` | 构建产物体积统计 | 无 |
| `flows/qa-launch/scripts/check-links.py` | 站内链接 404 扫描 | 无 |
| `scripts/check-skill-budget.py` | SKILL.md 行数/token 预算检查 | 无 |
| `scripts/check-orphan-assets.py` | 未被引用的静态资源审计 | 无 |

脚本都是可选的：不装 Pillow/numpy/fonttools 也能用主流程，只在执行对应脚本时需要。

## 维护

- 版本与变更：见 `CHANGELOG.md`
- 描述或结构调整后：跑 `references/evals.md` 的用例回归
- 预算检查：`python scripts/check-skill-budget.py .`

## License

MIT，见 `LICENSE`。
