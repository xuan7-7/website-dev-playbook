# 技能评测：触发与执行

用法：改描述或结构后逐条跑；记录「是否触发」「关键步骤是否执行」。触发命中不要求 100%，但同义说法必须覆盖。

| # | 用户说法 | 期望触发 | 关键步骤（至少） |
|---|---|---|---|
| 1 | 帮我把这个博客搭起来 | 总纲 | 阶段 A/B/B2，先问技术栈 |
| 2 | 我想做成二次元风格的站 | 总纲 | 风格小样确认后再做 |
| 3 | 晚上看页面字看不清 | dark-mode | 对比度扫描 + 态可见 |
| 4 | 手机上标题换行了 | responsive-navigation | 单行 + 溢出「⋯」 |
| 5 | 菜单点旁边收不起来 | responsive-navigation | outside-click + Esc |
| 6 | 图片加载太慢了 | performance / media-assets | 测基线 + 压缩 |
| 7 | 图片被裁掉一半 | media-assets | object-position 分断点 |
| 8 | 字体有字变成方块 | media-assets | 重新生成子集 |
| 9 | 上线前帮我检查一遍 | qa-launch | 构建/页面/交互/线上 |
| 10 | 部署后样式全丢了 | deployment / troubleshooting | base/url() 排查 |
| 11 | 这个方案你帮我选 | decision-options | A/B/C + 其他 |
| 12 | 以前是不是遇到过这个 | 案例层 | 查 index 对应 CASE |

反例（不应触发总纲）：纯后端接口设计、支付回调、数据库建模。
