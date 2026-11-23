---
name: website-media-assets
description: 图片与素材：WebP 压缩、尺寸体积、响应式背景、hero 取景、边缘淡化、字体子集、防下载边界。用户说"图片太大/糊/变形/被裁""字体缺字/方块"时用；只改文案不要用。
---

# 图片与素材流

1. 原图放 `assets-src/`，成品放 `public/assets/`；删外部源文件，确认版权。
2. 定尺寸转 WebP（照片1600、插画1200、缩略图600，质量70–80）。
3. 压体积：背景≤50KB、卡片≤40KB、头像≤10KB；批量用 `scripts/compress-images.py`。
4. 响应式加载：首屏背景 preload，其余 lazy；写宽高防 CLS。
5. hero 取景按断点设 `object-position`；淡化/边缘模糊用 `scripts/fade-edges.py`。
6. 字体子集用 `scripts/font-subset.py`，总量≤150KB；防下载只抬门槛，如实说明。

参数见 `references/image-presets.md`。边界：遵守总纲 §8；脚本缺依赖先问。
