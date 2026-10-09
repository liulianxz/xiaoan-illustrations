# QA Checklist

## 必过项

- 是 16:9 横版（ImageGen 实际出 1536×1024 = 3:2，可接受，不要硬裁）。
- 背景是干净白底。
- 有 xiaoan。
- xiaoan 承担核心动作，不只是装饰。
- xiaoan 的表情是可爱的：**两条向上弯的黑弧笑眼 + 一个小弧嘴 + 脸颊两团圆腮红**，与原始头像一致。
- **xiaoan 的脸是黑色手绘轮廓 + 留白（或极淡奶油色），不是实心饱和黄圆。**
- **xiaoan 的光芒是橙色细线条，不是实心橙块。**
- **角色自带的饱和橙黄像素 ≤ 画布 0.5%**（用 `scripts/measure_weight.py` 实测；旧色块版是 7.13%，线稿版是 0.15%）。
- 橙色只以细线（光芒）和小点（腮红）的形式出现，画面里没有任何大面积实心饱和色块。
- xiaoan 的光芒长短错落，不是均匀的钟表刻度。
- 没有复刻旧案例构图，而是为当前文章生成了新隐喻。
- 画面有创意、有意思。
- 简洁清爽，主体不超过画面约 60%。
- **xiaoan 是画面里的「小工作者」**：脸直径约 1/6 画布高，含光芒整体不超过画面高约 25%；周围的结构/物件才是主体。
- 一张图只讲一个核心结构。
- 中文标注少、短、能读，且每个词只出现一次、不被画面断行切开。
- 所有物件都是纯黑线稿，内部留白，没有米色 / 牛皮纸色 / 灰色填充。
- 蓝色用于主流程、箭头、路径或补充说明。
- 红色只用于重点、问题、提醒或结果。

## 失败信号

出现以下情况，重生成或局部编辑：

- 左上角有“常见坑 / Workflow / 系统架构图 / 路线图”等标题。
- **xiaoan 表情呆板：画成小黑点眼、平嘴线，或者把腮红丢了。**（最高频的失败项之一）
- **xiaoan 的脸画成实心饱和黄色块，带高光或立体感。**（旧版画法，等于贴纸；第二高频失败项）
- **光芒画成实心橙色块。**
- **光芒画成黑色细线（丢橙）：线条细度对了，但颜色归到了黑色线稿里，角色只剩两个橙点。**（第三高频失败项；`measure_weight.py` 角色框塌到 `90×18`~`134×38` 即可判定）
- xiaoan 的光芒排成均匀放射的钟表刻度。
- 箭头或路径用了橙色，与 xiaoan 撞色。
- xiaoan 变成精致商业吉祥物（有阴影、渐变、立体感、厚描边），或变成表情包。
- 画面像 PPT、课程课件、正式流程图。
- 元素太多、箭头太多、节点太多。
- 文字变成大段解释，或标注被画面切开成两半。
- 背景有纸纹、阴影、渐变、米色、噪点。
- 真实 UI 截图或科技感界面。
- 中文错字严重或标注不可读。
- **xiaoan 太大：脸占画布高 1/4 以上，成了画面里最大最抢眼的对象。**
- 同一个标注词在一张图里出现两次（模型爱做“强调式”重复）。
- 纸箱、砖块、书本等物件被填了米色 / 牛皮纸色 / 灰色，本该是纯黑线稿白底。
- 画面太死板，没有荒诞隐喻。
- 和 `assets/examples/` 里的旧案例构图过于相似。

## 迭代方法

- 表情太呆板 / 把笑眼腮红画没了：强调 `two upward-curving closed happy arc eyes`、`one small curved smiling mouth`、`two round cheek blush dots`、`keep the reference character's cute face`、`do NOT add dot eyes`、`do NOT make the expression blank or deadpan`；或改用「恢复笑眼与腮红」的局部编辑提示。
- **角色色块太重 / 有贴纸感**：强调 `the face has a slightly wobbly BLACK pen outline`、`keep it white or at most a very pale light butter-cream tint`、`the rays are thin ORANGE PEN LINE STROKES, not thick filled orange blobs`、`IGNORE the reference image's solid saturated color fill, its glossy highlight and its 3D shading`。用图生图时把 `input_fidelity` 从 `high` 降到 `low`；或改用「压回色块」的局部编辑提示。
- 角色太大 / 抢焦点：强调 `xiaoan must be SMALL and compact`、`the sun face diameter is only about 1/6 of the canvas height`、`the rays are SHORT`、`the surrounding structure is the main subject, not the character`、`preserve at least 50% blank white space`。
- 太普通：让 xiaoan 成为动作主体，加入一个奇怪但成立的隐喻。
- 太复杂：删节点，只保留一个动作和 3-5 个短标注。
- 光芒太规整：强调 `rays of uneven length and direction, not arranged in an even clock-face pattern`。
- 撞色：把画面里所有橙色元素收回到 xiaoan 身上，箭头改蓝。
- 太像精致商业插画：强调 `still clean sparse hand-drawn line art`、`not a glossy mascot poster`、`not a children's book illustration`，删掉阴影与渐变。
- 太 PPT：去掉标题、边框、整齐网格和过多箭头，改成手绘场景。
- 太像旧案例：保留核心意思，换掉主物件和 xiaoan 动作。
- 文字错：优先局部编辑；错得多就重生成并减少标注数量。
- **光芒改细之后丢了橙**：见下表——「细」和「橙」必须并列写死，只写一个会被模型二选一。
- **角色段（角色描述）改动后，先只出 1 张验证再批量跑**：角色段的每条约束都会互相挤压（细 vs 橙、小 vs 可见），一次改多条时批量的翻车成本约等于重跑一整轮 credits。

## 实测交付基线（2026-10-08）

线稿版试片 `01-71-days-lineart` 实测：**角色饱和色 0.15%，全画面墨迹 2.37%**。后续批次照这个量级对齐——角色色块在 0.1%–0.5% 之间都算正常，超过 1% 基本可以判定滑回色块版了。

**判据优先级高于百分数**：先看 `measure_weight.py` 输出的 `角色框` 尺寸。含光芒的正常角色框约 `200×200` ~ `355×290`；若塌成 `90×18` ~ `134×38` 的扁条，说明框内只圈到了两个腮红点、光芒已经丢色，无论 `orange%` 显示多少都要重做。

## 本机实测高频偏差与对策（2026-10-08，首批 8 张）

线稿化后的第一批 8 张，色块问题彻底消失（0.02%–0.12%），但暴露出 4 类新偏差。**去水印后请务必用 `scripts/measure_weight.py` 过一遍，橙色占比异常低（<0.03%）通常意味着光芒丢色。**

| 偏差 | 表现 | 对策（写进提示词） |
|---|---|---|
| **光芒丢橙** | 光芒被画成黑色细线，角色只剩两个橙点（橙色占比掉到 0.02%，角色框塌成 90×18~134×38） | **必须两句并列写，缺一不可**：① `THE RAYS MUST BE ORANGE, NOT BLACK` ② `If the rays come out black instead of orange, it is WRONG.` 单独强调「细」会把光芒归到黑色线稿里——实测 5 张里 4 张翻车，写了②的那张幸存 |
| **光芒偏粗** | 光芒画成短橙条 / 圆头小胶囊，不是发丝线 | 加 `hairline, one single stroke, the same thinness as a pencil line — not a rounded lozenge, not a bar, not a tab`（**务必与上面那两句同时写**，否则细度达标了颜色又丢） |
| **关键动作丢失** | 写了"被绊倒"却站着、"钉进桌面"却只是站着写（动作被弱化成静态站姿） | 把动作写成**进行时+身体状态**：`caught mid-fall, body tipped forward already past balance, one foot still behind`；不要只写 `trips over` |
| **标注颜色跑偏** | 指定的蓝色/红色标注渲染成黑色 | 颜色约束逐条点名到具体标注词，最后再加一句 `Every label must be in the color assigned to it above; no label may be left black.` |
| **数量与标注不符** | 标注写"五个闹钟"只画 3 个 | 数字类标注加 `COUNT CAREFULLY: there must be EXACTLY N ... not fewer and not more.`（实测一次修好） |

另外：**生成必须一张一条串行。** 并行调用时 `output_dir` 会被后一次覆盖，所有图落到同一目录，且同秒完成的两张会同名互删——实测两轮都踩，4 张变 3 张。

## 交付判断

高质量图应该让读者先觉得“有点怪但很亲切”，然后 1 秒内看懂结构。

如果第一眼像教程页或商业海报，而不是白纸上的怪诞产品草图，就不合格。

如果第一眼先看到**一块黄色圆饼**、再看到动作，也不合格——那是旧版的病。
