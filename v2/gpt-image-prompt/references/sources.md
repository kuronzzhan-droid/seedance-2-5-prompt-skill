# 调研来源与版本说明（调研日期：2026-10-28）

模型更新很快。用户问到参数、价格或新功能时，以 OpenAI 官方文档为准；这里的内容只是调研当天的快照。

## 版本时间线

| 时间 | 版本 | 要点 |
|---|---|---|
| 2025-03-25 发布，2025-04-23 上线 API | GPT Image 1（`gpt-image-1`） | 即“GPT-4o 图像生成” |
| 2025-10-06 | `gpt-image-1-mini` | 低成本版 |
| 2025-12-16 | GPT Image 1.5（`gpt-image-1.5`） | ChatGPT Images；编辑更精确，速度更快 |
| 2026-04 | GPT Image 2（`gpt-image-2`） | ChatGPT Images 2.0；生成过程引入推理，文字渲染大幅提升 |
| 2026-09-08 | GPT Image 2.5：`gpt-image-2.5-flare` / `gpt-image-2.5-sunburst` | Flare 速度优先，Sunburst 质量优先；有 `-2026-09-08` 快照；ChatGPT 端新增草图（Sketch）、模板、图上评论 |

## 官方来源（优先级最高）

- OpenAI 图像提示词指南（已覆盖 2.5 Flare/Sunburst）：https://developers.openai.com/api/docs/guides/image-prompting
- OpenAI Cookbook 图像提示词指南（GPT Image 2 时期，页面已标记归档）：https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- 模型页：https://developers.openai.com/api/docs/models/gpt-image-2.5-flare 、https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst
- 图像生成指南（含蒙版编辑要求）：https://developers.openai.com/api/docs/guides/image-generation

官方指南里的关键结论：
- 顺序：背景/场景 → 主体 → 关键细节 → 约束；先说明用途（广告、UI、信息图）来设定精致度。
- 格式不限（段落、列表、类 JSON、标签都可以），生产环境建议用固定、易扫读的模板。
- 文字：加引号或全大写，写字体、字号、颜色、位置；生僻词逐字母拼写；写明出现次数，不要多余文字。
- 编辑：“只改 X / 其余保持不变”，每轮重复保留清单；像素级不变用合成。
- 多图：按序号 + 角色引用每张输入图，并说明如何组合。
- 参数放在 API 里，不要写进提示词；quality 按需提高；超过 2560×1440 为实验性。
- 不要用概念图语言描述 UI；写实场景不要用影棚化的措辞；不要直接沿用 GPT Image 1 的设置。

## 社区与第三方（经验参考）

- wuyoscar/gpt_image_2_skill（GitHub，约 5.9k star，含 2.5 资料和 162 条提示词图库）：https://github.com/wuyoscar/gpt_image_2_skill ，要点：文字加引号、画布与版式写在主体前面、复杂产品渲染用 JSON、信息图用固定分区、UI 写得像产品需求、多格图要写一致性约束、负面词只针对强先验、中文密集排版要写明简繁体并禁止乱码。
- freestylefly/awesome-gpt-image-2 的“六段式”：主体与任务 → 构图版式 → 视觉风格与材质 → 文字要求 → 画幅与输出 → 约束与排除。
- atlabs GPT Image 2.5 指南：比较时手动固定质量档；一次只改一个变量；4×4 纯白背景设定图做角色一致性；设定图背景带风格会污染后续场景。https://www.atlabs.ai/blog/gpt-image-2.5-prompt-guide-2026-flare-vs-sunburst-quality-steps-and-consistent-characters
- Morphic ChatGPT Images 2.0 指南：思考/Pro 模式下才有推理规划布局；可渲染拉丁文、中文、日文、韩文、印地文、孟加拉文；单次最多 10 张。https://morphic.com/resources/how-to/chatgpt-images-2.0-guide
- Wikipedia “GPT Image” 条目（版本时间线）：https://en.wikipedia.org/wiki/GPT_Image

## 未经官方证实或说法不一的地方

- “提示词开头的词权重最大”：多篇第三方文章这样说，官方没有提到。保留这个习惯无害（把用途和画布放最前）。
- “2.5 支持最多 16 张参考图 / 原生 4K”：来自第三方页面。官方的尺寸上限是长边 3840，超过 2560×1440 属实验性；参考图数量官方未写明。
- 文字准确率“约 99%”之类的数字没有可靠出处。
- `input_fidelity` 在 2.5 上是否生效没有证实；`gpt-image-2` 官方要求不传。旧 Cookbook 的部分 gpt-image-2 编辑示例仍然传了 `input_fidelity="high"`，和参数表矛盾。
- ChatGPT 端各功能（Thinking 模式、Sketch、圈选评论）的入口和可用范围随账号与地区变化，以实际界面为准。
