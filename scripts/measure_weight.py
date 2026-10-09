#!/usr/bin/env python3
"""测量 xiaoan 配图的「视觉重量」，用来判断有没有滑回旧的饱和色块画法。

用法：
    python3 scripts/measure_weight.py <目录或图片路径> [更多路径...]

输出每张图的：
    - 角色饱和橙黄像素占画面比例（线稿版基线 ≤0.5%，旧色块版约 7%）
    - 全画面墨迹占比（黑线密度，线稿版约 2-3%）
    - 角色外接框尺寸

判定阈值（与 references/qa-checklist.md 一致）：
    <= 0.5%   线稿版，正常
    0.5-1.0%  偏重，看一眼是不是光芒画粗了
    > 1.0%    基本可判定滑回色块版，重生成或局部编辑
"""
import sys
import glob
import os

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("需要 numpy 与 Pillow：pip install numpy pillow")


def measure(path):
    rgb = np.array(Image.open(path).convert("RGB")).astype(int)
    h, w, _ = rgb.shape
    R, G, B = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    # 饱和橙黄：排除红标注（G 很低）与米色物件（R-B 差值小）
    orange = ((R - B) > 150) & (G > 120) & (R > 200)

    gray = np.array(Image.open(path).convert("L")).astype(int)
    ink = (gray < 200).mean() * 100.0

    res = {
        "path": path,
        "w": w,
        "h": h,
        "orange_px": int(orange.sum()),
        "orange_pct": orange.sum() / (h * w) * 100.0,
        "ink_pct": ink,
    }
    ys, xs = np.where(orange)
    if len(xs):
        # 用 1%–99% 分位框，避免个别游离像素把外接框撑大
        x0, x1 = np.percentile(xs, [1, 99])
        y0, y1 = np.percentile(ys, [1, 99])
        res["bbox"] = (int(x1 - x0 + 1), int(y1 - y0 + 1))
    else:
        res["bbox"] = None
    return res


def verdict(pct):
    if pct <= 0.5:
        return "OK 线稿版"
    if pct <= 1.0:
        return "偏重"
    return "疑似色块版"


def main(argv):
    targets = argv[1:]
    if not targets:
        targets = ["."]
    files = []
    for t in targets:
        if os.path.isdir(t):
            files += sorted(glob.glob(os.path.join(t, "*.png")))
        else:
            files.append(t)
    if not files:
        sys.exit("没找到 png")

    print("%-34s %10s %9s %8s   %s" % ("file", "size", "orange%", "ink%", "verdict"))
    print("-" * 78)
    for f in files:
        try:
            r = measure(f)
        except Exception as e:
            print("%-34s ERROR %s" % (os.path.basename(f), e))
            continue
        bb = "%dx%d" % r["bbox"] if r["bbox"] else "-"
        print("%-34s %10s %8.2f%% %7.2f%%   %s  (角色框 %s)"
              % (os.path.basename(f), "%dx%d" % (r["w"], r["h"]),
                 r["orange_pct"], r["ink_pct"], verdict(r["orange_pct"]), bb))


if __name__ == "__main__":
    main(sys.argv)
