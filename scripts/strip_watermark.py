#!/usr/bin/env python3
"""去除生成图右下角的浅色工具水印（就地覆盖，不裁剪、不改画面）。

背景：ImageGen 输出的图常在右下角带一层极淡的「AI生成」水印（亮度仅比背景低
几个灰阶，肉眼放大才明显）。直接用阈值检测很难定位，因为背景本身并非纯白、
且页面底边还常带一条渐暗纹理。

做法：在画面右下角划一个「安全矩形」——该矩形内不含任何画内内容——然后把每行
左侧近邻的背景色水平外推填入。这样既能抹掉水印，又保留了背景原有的垂直渐变，
不会产生色带接缝。

用法：
    python3 strip_watermark.py <图片目录> [--x-ratio 0.75] [--y-ratio 0.94] [--backup]

先用 probe.py 风格的方式确认安全矩形内确实没有画内内容，再执行本脚本。
"""
import argparse
import os
import shutil
import sys

import numpy as np
from PIL import Image

SAMPLE_W = 16


def strip(path, x_ratio, y_ratio, backup):
    img = Image.open(path).convert("RGB")
    a = np.array(img).astype(np.uint8)
    h, w, _ = a.shape
    x_cut, y_cut = int(w * x_ratio), int(h * y_ratio)
    if x_cut <= SAMPLE_W or y_cut >= h:
        return "skip (参数越界)"
    if backup:
        raw = os.path.join(os.path.dirname(path), "raw")
        os.makedirs(raw, exist_ok=True)
        dst = os.path.join(raw, os.path.basename(path))
        if not os.path.exists(dst):
            shutil.copy2(path, dst)
    out = a.copy()
    for y in range(y_cut, h):
        col = np.median(a[y, x_cut - SAMPLE_W:x_cut].astype(int), axis=0).astype(np.uint8)
        out[y, x_cut:w] = col
    Image.fromarray(out).save(path)
    return "ok  覆盖 x[%d,%d] y[%d,%d]" % (x_cut, w - 1, y_cut, h - 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory")
    ap.add_argument("--x-ratio", type=float, default=0.75)
    ap.add_argument("--y-ratio", type=float, default=0.94)
    ap.add_argument("--no-backup", action="store_true",
                    help="不把原图备份到 raw/（默认会备份）")
    args = ap.parse_args()

    if not os.path.isdir(args.directory):
        sys.exit("目录不存在: %s" % args.directory)

    n = 0
    for f in sorted(os.listdir(args.directory)):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            print("%-40s %s" % (f, strip(os.path.join(args.directory, f),
                                         args.x_ratio, args.y_ratio,
                                         not args.no_backup)))
            n += 1
    print("处理 %d 张；原图备份在 raw/" % n)


if __name__ == "__main__":
    main()
