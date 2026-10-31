# 调研来源与版本说明（调研日期：2026-10-28）

模型和平台更新很快。用户问到参数、价格或新功能时，以火山方舟官方文档和平台界面为准；这里只是调研当天的快照。

## 版本信息

- Seedance 2.0：单次最长 15 秒；参考素材上限约为图片 9 张、视频 3 段、音频 3 段（第三方对比文章的说法）。
- Seedance 2.5：火山引擎 2026-06-23 预告，2026-07-31 发布，同日上线即梦和豆包。单次 4–30 秒，最多 50 个参考素材（图片 30 张、视频 10 段、音频 10 段），支持整数秒时间戳、多视图主体参考、自由画幅、mov 输出、视频编辑和延长、样片模式、返回尾帧。API 模型 ID：`doubao-seedance-2-5-260628`。

## 官方来源（优先级最高）

- 火山方舟《Doubao Seedance 2.5 提示词指南》：https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide （另一个入口：https://docs.volcengine.com/docs/82379/2607689 ）
- 火山方舟《Doubao Seedance 2.5 教程》（API 参数、生成模式、素材限制）：https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- 小云雀《Seedance 2.5 官方手册》（产品功能、素材建议、提示词规则）：https://www.xiaoyunque.com/tutorials/seedance-2-5

官方指南里的关键结论：
- 顺序：素材指代 → 一句话概述 → 分段情节（时间戳或“镜头 N”）→ 贯穿全片的机位、环境、声音和氛围。
- 素材按上传顺序编号，在文本里逐一绑定，写清分工；素材够准时只做指代。
- 时间戳用整数秒、连续不留空，三种写法（区间 / 时间点 / 相对时间）；内容量要和时长匹配；不要用时间戳控制频次。
- 30 秒示例是 9 个镜头：3/3/4/4/4/4/3/3/2 秒；先写素材绑定、主体设定、环境、整体风格和严格排除，再写分镜头。
- 首尾帧、关键帧在第一句写明；宫格分镜 15 格以内，用简洁线稿；要严格对齐就改用关键帧。
- 编辑和延长靠关键词识别；编辑时 `ratio` 为 adaptive、`duration` 为 -1，建议输出 mov。
- 热门运镜可以直接写，小众术语要加描述；情绪写成可观察的表现；强情绪可能导致眼睛发光。
- 台词推荐“角色台词（情绪）：内容”；背景音乐、音效、台词分开描述；字幕约束目前无法完全避免。
- 常见问题：文字拼错、角色错位、指纹状纹理、编辑时长偏差、背景音乐残留等的处理办法（已写进 SKILL.md 的翻车排查表）。

## 媒体报道

- TechNode（发布报道）：https://technode.com/2026/07/31/bytedance-launches-seedance-2-5-video-generation-model/
- 财新（发布预告）：https://www.caixinglobal.com/2026-06-24/bytedance-targets-july-launch-of-upgraded-ai-video-model-102456839.html
- 搜狐（样片模式）：https://www.sohu.com/a/1079644751_122066678

## 社区与第三方（经验参考）

- XiaoJieAi66/XiaoJieAigc-seedance-2-5-video-prompt（社区 Seedance 2.5 Skill）：https://github.com/XiaoJieAi66/XiaoJieAigc-seedance-2-5-video-prompt ，要点：先问三个关键问题；每份素材写“参考什么、保留什么、不参考什么”；每段写“时间区间 → 景别机位 → 主体初始状态 → 可见动作和路径 → 摄影机运动或焦点 → 结束画面 → 与下一段的连接”；主体运动和相机运动分开写；实体、影子和倒影分开写；固定机位不等于画面冻结。
- AI星球转述的官方指南长文：https://www.aixq.cc/59824.html （阶段法“开始时 / 主要事件 / 结束时”、编辑时先定唯一母版、延长先写尾帧状态、无缝转场的写作顺序）
- Higgsfield 提示词库：https://higgsfield.ai/blog/seedance-2-5-prompting-guide （全局风格 → 场景 → 角色 → 地点 → 首帧站位 → 逐镜头 → 镜头 → 物理 → 光线 → 音频；锁定人数、屏幕方向和轴线；台词绑定时间点）
- Morphed：https://morphed.app/blog/seedance-2-5-prompts （一镜到底用时间区间而不是“Shot 1/2/3”；中段约 12–18 秒最容易漂移；1–2 份素材最稳，超过 6 份左右分工容易串）
- PicLumen：https://www.piclumen.com/blog/seedance-2-5-ai-video-generator-prompt-guide/ （每份素材只承担一项任务；身份交给素材，提示词只管动作）
- seedance.tv：https://www.seedance.tv/blog/seedance-2-5-prompt-guide （一段 1–2 个运镜；图生视频只描述动作和运镜，不复述图里已有的内容）

## 未经官方证实或说法不一的地方

- “原生 4K”：API 文档只列了 480p、720p、1080p；4K 是即梦、小云雀等 App 里的超分功能。
- 小云雀手册称“超长视频最长约 5 分钟原生直出”：这是平台功能，不是 API 单次生成的能力。
- 台词和声音的符号（已更正）：火山方舟《Seedance 2.5 教程》写明“声音用特殊字符区分：音乐用 ()、音效用 <>、台词用 {}、字幕用 【】”，官方 sd25-pe 的符号表相同，所以这是官方规则，不只是惯例。官方示例同时把【】用作段落标签；如果画面里冒出像段落标题的字，把标签换成 ■ 或纯文字。（早先依据 AI星球转述写的“方括号表示字幕”有误。）
- 第三方 SEO 攻略页（atlabs、cometapi、framia、seedance.tv 等）参数常互相矛盾，有的来自 API 转售商，只作参考；seedance.tv 和字节无关。
- “720p 的提示词跟随度最好”：个人经验，没有系统验证。
- 不同平台的积分价格、分辨率选项和素材上限可能不同，以平台界面为准。
