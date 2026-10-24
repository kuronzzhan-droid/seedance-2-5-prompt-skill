# 网上技巧的取舍

2026-10-19 和 10-24 联网查了 Seedance 2.5 的官方与社区教程、公开的 Seedance 提示词 Skill，以及 OpenAI 的出图提示词指南。下面记录哪些写进了技能、哪些没写以及原因。判断标准：和用户在《兜风日》等项目里实测的规则冲突时，以实测为准。

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

## 社区实测（第二轮）

知乎、X 上的几篇实测长文（如 [302.AI 实测](https://zhuanlan.zhihu.com/p/2070915165789466937)、[拆 200 条提示词的总结](https://x.com/cheerselflin/article/2085591217841250326)）的站点不允许抓取正文，下面只用了能读到全文的社区来源：

- [dexhunter/seedance2-skill（中文版 SKILL.md）](https://github.com/dexhunter/seedance2-skill/blob/main/zh/SKILL.md)
- [琥云：拆解官方提示词语法与 50 套模板](https://www.huyunjiaoyu.cn/article/102775.html)
- [18183：Seedance 2.5 提示词技巧](https://m.18183.com/gonglue/202608/39tmj6m6.html)
- [HeigeAI：GPT Image 2 动漫提示词](https://www.heigeai.com/en/prompts/anime/)

采用的：

| 技巧 | 来源 | 写进了哪里 |
|---|---|---|
| 二维动画会被自动加立体光影和金属反光，金属玻璃写成平涂加硬边高光，道具选扁平的 | 琥云 | `positive-prompting.md` 第 8 节 |
| 写实真人清晰脸部不能作参考，会被拦截 | dexhunter Skill | `platform-settings.md` 第 4 节 |
| 一条提示词的参考素材控制在十个左右 | 18183 | `platform-settings.md` 第 4 节 |
| 延长时界面时长选新增部分的长度 | dexhunter Skill | SKILL.md“视频延长” |
| 出图画风写到具体年代和类型；设定图逐个点名视图；换姿势时附定稿图；小细节出图后逐件对照 | HeigeAI | `gpt-image-prompts.md` 第 2 节 |

没有采用的：

| 技巧 | 来源 | 原因 |
|---|---|---|
| 提示词控制在 200—400 字，过长会丢指令 | 18183 | 用户多镜头片实测一千三到一千五百字稳定出片；短提示词适合单镜头 |
| 30 秒固定拆成三段各 10 秒 | 18183 | 实测五到九个镜头、单镜三到七秒，按动作容量分配 |
| 用不同括号标记配乐、音效、台词、字幕 | 琥云 | 用户实测用“用某某的声音参考的音色……说：「台词」”已稳定。第三轮查到方舟官方也写了这套括号，改为待测，见下文 |
| 二维动画加“无立体光影、无金属反光”限制词 | 琥云 | 采用了它指出的问题，改成正面写法 |
| 一镜到底写“全程不要切镜头” | dexhunter Skill | 改成正面写法“一个连续镜头，一镜到底” |
| 末尾附“胶片颗粒”等风格修饰词 | dexhunter Skill | 三渲二要干净平整，颗粒会破坏画面；写实路线另议 |
| 总素材不超过 12 个、音频不超过 15 秒 | dexhunter Skill | 这是 2.0 时代的限制，2.5 的 30 秒档上限见 `platform-settings.md` |

## 第三轮：社区热度和官方核对（2026-10-24）

用 grok 查 X 和网页，用 Gemini 查网页，Seedance 2.5 和 GPT Image 各一路，合并后 137 条，约一半是官方来源。下面的关键条目都打开原页核对过。完整报告和每条的热度、证据等级在用户电脑上：`E:\sora——picture\狼骑士\_工具\提示词对比测试_20261019\技巧调研_20261024\技巧调研报告.md`。

来源：

- BytePlus ModelArk（方舟）：[Dreamina Seedance 2.5 prompt guide](https://docs.byteplus.com/ko/docs/modelark/seedance-2-5-prompt-guide)，下文简称“方舟官方指南”
- 方舟官方 Skill：sd25-pe，专门改写 Seedance 2.5 提示词，只改写不提交
- 社区 Skill：LearnPrompt/awesome-seedance（2.2k star，案例追溯原帖并复测）、wuyoscar/GPT-Image2-Skill（约 5.9k star，设定图、表情表、分镜表模板）、Emily2040/seedance-2.0（7.9k star，针对 2.0）、openai/codex 自带的 imagegen skill
- X 实测帖（都附出片）：@ZentrixHQ（866 赞）、@techhalla（254 赞）、@bmx_ai13（526 赞）、@ichelpark

采用的：

| 技巧 | 来源 | 写进了哪里 |
|---|---|---|
| 2.5 认整数秒的时间段（2.0 只认镜头序号），每段内容量和时长相当 | 方舟官方指南 | SKILL.md“设计时间轴” |
| 每段写清结束时的状态，用来卡住切点 | 社区 | SKILL.md“设计时间轴” |
| 多角色的参考图按首次出场顺序编号 | 方舟官方指南 | SKILL.md“写素材映射” |
| 同一角色有两种形态时，每种形态单独一张参考图 | @ZentrixHQ | SKILL.md“写素材映射” |
| 首尾帧要用首尾帧模式，提示词里写“图1是首帧”锁不住构图 | 方舟官方指南 | SKILL.md“首尾帧” |
| 复杂任务拆成先参考生成、再编辑两步 | 方舟官方指南 | SKILL.md“智能/高级编辑” |
| 三渲二写具体工艺，再附一张只管画风的参考图 | 社区共识 | SKILL.md“21:9 三渲二画风” |
| 宫格分镜要逐格对应时间段，否则只被当作风格图 | @bmx_ai13 | `official-guide.md` 第 9 节 |
| Codex 内置出图用的是 gpt-image-2，对话模型只负责调度 | OpenAI 官方文档 | `gpt-image-prompts.md` 第 4 节 |
| 设定图之外加一张比例参考图 | @techhalla | 技能里已有，见 `positive-prompting.md` 第 3、9 节 |
| 改图一次只改一处，必须不变的区域改完合成回原图 | 方舟官方指南、OpenAI | 技能里已有，见 `gpt-image-prompts.md` 第 3 节 |

和实测规则冲突、改为对比测试的：

| 技巧 | 来源 | 冲突在哪 |
|---|---|---|
| 三视图拆成几张单视图分别输入，一张图里只放一个视角 | 方舟官方指南；社区反映拼图式三视图易出分身、变脸 | 用户一直整张喂 16:9 三栏设定图 |
| “不要字幕”“不要 bgm”这两类否定有效 | 方舟官方指南 | 用户规则是通篇零否定词，目前写“画面是干净的影像”“全段是海风……” |
| 声音用括号区分：( ) 配乐、< > 音效、{ } 台词、【】字幕 | 方舟官方指南 | 用户实测用「」加“用某某的声音参考的音色”，校验器也按「」检查台词绑定 |
| 用 sd25-pe 改写提示词 | 方舟官方 Skill | 未实测改写后是否保留用户的正面写法和六段骨架 |
| 参考图用粗糙的手绘设定图，精修插画会让出片发腻 | X @Iancu_ai | 用户的设定图是 GPT Image 精修图 |
| 经 API 用更新的出图模型，对比 Codex 内置的 gpt-image-2 | OpenAI | 用户目前只经 Codex 出图 |

没有采用的：

| 技巧 | 来源 | 原因 |
|---|---|---|
| 中文提示词控制在 500 字以内 | Gemini 引用的网页 | 原页打不开，和方舟官方指南及用户一千三到一千五百字的实测都不符 |
| 一条 Reddit 帖、一篇 CSDN 文的技巧 | Gemini 引用 | 原页打不开，编号和日期对不上，按来源存疑处理 |

## 可以以后再考虑的

- video-director Skill 有一份行为测试集（输入场景加期望的输出约束），可以借鉴来给本技能做回归测试。
- 首尾帧参考可以稳定构图，这次没有实测样本，等用到时再补规则。
