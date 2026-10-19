# 网上技巧的取舍

2026-10-19 联网查了 Seedance 2.5 的官方与社区教程、公开的 Seedance 提示词 Skill，以及 OpenAI 的出图提示词指南。下面记录哪些写进了技能、哪些没写以及原因。判断标准：和用户在《兜风日》等项目里实测的规则冲突时，以实测为准。

## 来源

- Dreamina 官方：[Seedance 2.5 Prompt Guide](https://dreamina.capcut.com/seedance/seedance-2-5-prompt)
- Picsart：[Seedance 2.5 prompting guide: tips for 30-second takes](https://picsart.com/blog/seedance-2-5-prompting-guide/)
- 开源 Skill：[liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director)
- OpenAI：[GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)、[Image prompting](https://developers.openai.com/api/docs/guides/image-prompting)

## 采用的

| 技巧 | 来源 | 写进了哪里 |
|---|---|---|
| 一个镜头只给一种运镜，运镜写在光线和情绪之前 | Dreamina、Picsart | SKILL.md“30 秒主动镜头结构” |
| 明确写镜头数或“一镜到底”，防止随机切镜 | Dreamina | SKILL.md“出片不对时的调整顺序” |
| 物理互动先写起因再写结果 | Picsart | SKILL.md“30 秒主动镜头结构” |
| 开头埋小物件、结尾回收 | Dreamina | SKILL.md“30 秒主动镜头结构” |
| 换镜方式直接点名（匹配剪辑、甩镜） | Dreamina | SKILL.md“30 秒主动镜头结构” |
| 一次只改一层，按“参考 → 镜头结构 → 运镜 → 画风声音”排查 | Dreamina、Picsart | SKILL.md“出片不对时的调整顺序” |
| 角色参考默认管整个人，背景、姿势、裁切、光线由正文决定 | video-director Skill | SKILL.md“写素材映射” |
| 出图参考图编号并写用途、角色锚点、一轮只改一件事并重写保持清单 | OpenAI | `gpt-image-prompts.md` |

## 没有采用的

| 技巧 | 来源 | 原因 |
|---|---|---|
| 把短的排除句集中放在末尾（如“无背景音乐、无对白”） | Dreamina、OpenAI | 用户 10-04、10-05、10-11 三次确认只写正面描述；否定词损伤细节，还会被其中的名词带偏 |
| 每个节拍重复写角色的固定外貌特征来防止跑偏 | Dreamina | 实测让参考图管外貌、正文只写名字更稳；Seedance 正文重复外貌会和参考图抢控制。出图提示词例外，见 `gpt-image-prompts.md` 第 2 节 |
| 最多 50 个混合输入 | Dreamina、Picsart | 用户实际使用的平台 30 秒档上限是 30 张图、10 条音频，见 `platform-settings.md`；实测一条附六到八张图最稳 |
| 默认每个节拍 6—8 秒 | Dreamina | 多镜头片实测单镜三到七秒、长镜头七到十二秒，按动作容量分配 |
| 用 “photorealistic” 开启写实 | OpenAI | 只适用于超写实路线，三渲二会被拉向写实 |
| 后期选项（超分到 4K、插帧、配乐生成） | Dreamina | 是界面功能，不属于提示词写法 |

## 可以以后再考虑的

- video-director Skill 有一份行为测试集（输入场景加期望的输出约束），可以借鉴来给本技能做回归测试。
- 首尾帧参考可以稳定构图，这次没有实测样本，等用到时再补规则。
