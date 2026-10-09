# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## 角色段（线稿版，2026-10-08 起）

```text
Recurring IP character required:
xiaoan, a small sun-headed creature drawn in the SAME black pen line-art language as everything else — it must NOT look like a colored sticker pasted on top:
- The round face has a slightly wobbly BLACK pen outline. Inside the face keep it white or at most a very pale light butter-cream tint like faint watercolor on paper — NOT a solid saturated yellow disc, NO gradient, NO glossy highlight, NO 3D volume, NO drop shadow.
- Around the head: 10-14 SHORT rays, and THE RAYS MUST BE ORANGE, NOT BLACK. This is essential: the orange rays plus the two orange blush dots are the ONLY warm-colour identity of this character — if the rays come out black, the character loses its identity. Draw each ray in ORANGE ink as a SINGLE THIN HAIRLINE stroke of the SAME line weight as the black pen lines used everywhere else in the drawing — one quick flick of a fine orange pen, tapering slightly at its outer end, like a thin scratch of orange ink. Uneven in length and direction, never arranged in an even clock-face pattern. A ray must NEVER look like a thick bar, a rounded capsule, a cigarette, a matchstick, a tab, a rectangle or a filled shape. If any ray is thicker than the black ink lines of the drawing, it is WRONG. If the rays come out black instead of orange, it is WRONG.
- Face details: two upward-curving closed happy arc eyes drawn in black, one small curved black smiling mouth, exactly two small solid orange cheek blush dots. KEEP these three; do NOT turn the eyes into black dots; do NOT make the expression blank or deadpan.
- Body: two EXTREMELY thin black hairline legs — single pen strokes, like matchstick-thin lines — sometimes thin black arms. No muscular calves, no thick limbs, no body volume. The head is clearly bigger than the body.
xiaoan must perform the core conceptual action, not decorate the scene. It reads as warm and friendly through its FACE, not through color fill. Still clean sparse hand-drawn line art, not a glossy mascot poster.
```

## 完整模板

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red and blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no glossy mascot poster, no children's illustration, no realistic UI. Every single object in the picture — including the character — is drawn in the SAME black pen line-art language. Nothing anywhere is a solid saturated color block; keep everything white inside the outlines.

{角色段：粘贴上面的「角色段（线稿版）」}

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：xiaoan 在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for all line art, xiaoan's outline and limbs, boxes and main text. Orange ONLY as thin line strokes for xiaoan's rays and as its two small blush dots — never as a large solid filled area, and never for arrows, paths or any other element. Blue for the main flow, arrows, paths and automation direction, and for secondary notes or system state. Red only for key warnings, problems and results.

SIZE AND SCALE (CRITICAL — this is the easiest thing to get wrong):
The surrounding structure is the main subject; xiaoan is a small worker inside it, never the largest object in the frame. The sun face diameter must be NO MORE than about 1/6 of the canvas height (roughly 15-17%) — this is a HARD LIMIT, not a target. Keep the rays SHORT — each ray extends only about 25-30% of the face radius beyond the rim — so the whole character including its rays must stay within about 25% of the canvas height and about 20% of the canvas width. When xiaoan carries, pushes or lifts an oversized object, the CHARACTER MUST NOT GROW — shrink the object instead so the character stays small; a big action never justifies a big character. Total saturated orange-yellow pixel area belonging to the character (rays + blush) must stay under about 0.5% of the canvas. Preserve at least 50% blank white space. Do NOT scale xiaoan up to fill the frame.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 3-5 short handwritten Chinese labels, each written once on a single line and never split or wrapped by the drawing, and never repeat the same label twice on one image. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not arrange xiaoan's rays in an even clock-face pattern. Do not fill any object (cards, boxes, paper, bricks) with beige, kraft-paper color or grey — keep them white inside black outlines. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.

Allowed text items (exhaustive): {标注词1}, {标注词2}, {标注词3}
Do not repeat any word twice, do not add any other Chinese text, do not add a heading or subtitle.
```

> 末尾的 `Allowed text items (exhaustive)` 三行是实测有效的一条：不写这句，模型常自己加标题或重复标注；写了之后标注基本一次到位。

## 用图生图锁定角色一致性（推荐）

纯文生图时 xiaoan 的表情细节、光芒数量、腮红位置每次都漂。把原始头像作为参考图传进去，可显著提高一致性：

- 参考图：公众号头像（太阳笑脸），已固定存于 skill 内 `assets/xiaoan-avatar-reference.jpg`，直接用该绝对路径传入，不用临时找图。
- `input_fidelity` 设 **`low`**。
  - 这一点和常规做法相反，但实测**必要**：保真度设 `high` 会把参考图的实心饱和黄、玻璃高光、立体感一起搬进来，角色重新变成贴纸。
  - 设 `low` 只借「太阳轮廓 / 笑眼弧 / 弧嘴 / 腮红」这几个语义特征，画法允许大改。
- 提示词里显式点明「借什么、不要借什么」，实测一次成功：

```text
CRITICAL: KEEP the closed smiling arc eyes, the small curved smiling mouth and the two round cheek blush dots. Do NOT turn the eyes into black dots. Do NOT make the expression blank or deadpan. But IGNORE the reference image's solid saturated color fill, its glossy highlight and its 3D shading - this version must read as light hand-drawn line art, not a glossy sticker.
```

- 生成后若表情变成黑点眼 / 平嘴线 / 丢了腮红，属于必须重生成或局部编辑的失败项。

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强怪诞感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make xiaoan more central to the conceptual action. xiaoan should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse and hand-drawn, while keeping xiaoan's cheerful smiling face.
```

恢复笑眼与腮红（模型把表情画成呆板黑点眼时用）：

```text
Edit the provided image. Change the character's eyes to two upward-curving closed smiling arcs, replace the mouth with one small curved smiling mouth, and add two round orange blush dots on the cheeks. Remove the plain dot eyes and the flat mouth line, and remove any eye highlights. Keep the black pen face outline, the thin orange line rays, the body, all line work, all Chinese labels and the composition otherwise exactly unchanged.
```

压回色块（模型又把脸画成实心饱和黄、或光芒画成实心橙块时用）：

```text
Edit the provided image. Redraw the character's sun face as a black hand-drawn pen outline with a white or very pale butter-cream interior; remove the solid saturated yellow fill, the glossy highlight and any shading. Redraw the rays as thin orange pen line strokes instead of solid orange blobs. Keep the closed smiling arc eyes, the small curved smiling mouth, the two blush dots, everything else unchanged.
```

## 实测教训：光芒「变细」和「保橙」必须同时写（2026-10-08）

**现象**：想修正「光芒像圆头胶囊 / 香烟」的偏差，把提示词里「发丝细线」写到极硬（`SINGLE THIN HAIRLINE ... like a thin scratch of ink`），结果 4 张里有 4 张模型把光芒直接画成了**黑色细线**——线条细度达标了，但橙色没了。

**判别方法**：`scripts/measure_weight.py` 输出的 `角色框` 尺寸会直接暴露：
- 正常（含光芒）：约 `200×200` ~ `350×290`
- 光芒丢色（只剩腮红）：塌成约 `90×18` ~ `134×38`，`orange%` 掉到 `0.0x%`

**根因**：一旦「细」是唯一被强调的属性，模型会把它归到「黑色线稿」这一套线里——毕竟全画面 99% 的线都是黑的。橙色必须作为**并列的显式约束**出现，模型才会把它当独立的颜色属性处理。

**对策**：角色段里必须同时出现两句，缺一不可：
1. `THE RAYS MUST BE ORANGE, NOT BLACK`
2. `If the rays come out black instead of orange, it is WRONG.`

**效率经验**：这两句一旦漏写，重生成会白烧一轮 credits。角色段改动后建议先只出 1 张验证，再批量跑。

**尺寸上限的另一漏洞（2026-10-08 三轮实测）**：即使尺寸段写全，凡画面要求 xiaoan「抱 / 推 / 举一个超大物件」，模型会把**角色**等比放大去匹配物件（实测角色框高 754px = 画布 74%，上限 25%）。对策已写进 SIZE AND SCALE 段：`When xiaoan carries, pushes or lifts an oversized object, the CHARACTER MUST NOT GROW — shrink the object instead`。验证方法：`measure_weight.py` 的 `角色框` 高应 ≤ 约 280px（25% × 1024），宽 ≤ 约 310px（20% × 1536），双角色构图另算。
