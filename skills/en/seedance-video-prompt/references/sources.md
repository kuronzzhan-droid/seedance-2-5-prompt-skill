# Research sources and version notes (research date: 2026-10-28)

The model and the platforms change quickly. When the user asks about parameters, prices, or new features, go by the official Volcano Ark docs and the platform interface; this file is only a snapshot from the research date.

## Versions

- Seedance 2.0: up to 15 s per generation; reference limits of about 9 images, 3 videos, and 3 audio clips (according to third-party comparison articles).
- Seedance 2.5: previewed by Volcano Engine on 2026-06-23, released 2026-07-31, live the same day on Jimeng and Doubao. 4–30 s per generation, up to 50 reference assets (30 images, 10 videos, 10 audio clips), whole-second timestamps, multi-view subject references, free aspect ratios, mov output, video editing and extension, sample mode, last-frame return. API model ID: `doubao-seedance-2-5-260628`.

## Official sources (highest priority)

- Volcano Ark, Doubao Seedance 2.5 prompt guide: https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide (alternative entry: https://docs.volcengine.com/docs/82379/2607689 )
- Volcano Ark, Doubao Seedance 2.5 tutorial (API parameters, generation modes, asset limits): https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Xiaoyunque, Seedance 2.5 official handbook (product features, asset advice, prompt rules): https://www.xiaoyunque.com/tutorials/seedance-2-5

Key conclusions from the official guide:
- Order: asset references → one-line summary → the story in ranges (timestamps or "Shot N") → camera, environment, sound, and mood that run through the whole clip.
- Assets are numbered in upload order and bound one by one in the text, each with its job stated. When an asset is accurate enough, just point to it.
- Timestamps are whole seconds, continuous with no gaps, in three forms (range / point / relative time). The amount of content has to fit the duration. Do not use timestamps to control frequency.
- The 30 s example is 9 shots: 3/3/4/4/4/4/3/3/2 s. It writes asset binding, subjects, environment, overall style, and strict exclusions first, then the shots.
- First/last frames and keyframes are stated in the first sentence. Storyboard grids stay at 15 panels or fewer, in clean line art. For strict alignment, switch to keyframes.
- Editing and extension are recognised by keywords. For edits, `ratio` is adaptive and `duration` is -1, with mov output recommended.
- Named camera moves can be written directly; rare terms need a description. Emotion is written as observable behaviour. Strong emotion can make eyes glow.
- The recommended dialogue form is "Character line (emotion): text". Background music, sound effects, and dialogue are described separately. Subtitle constraints cannot yet be fully guaranteed.
- FAQ: how to handle misspelled text, misplaced characters, fingerprint-like texture, duration drift in edits, leftover background music, and so on (already in the troubleshooting table of SKILL.md).

## Press coverage

- TechNode (launch report): https://technode.com/2026/07/31/bytedance-launches-seedance-2-5-video-generation-model/
- Caixin (launch preview): https://www.caixinglobal.com/2026-06-24/bytedance-targets-july-launch-of-upgraded-ai-video-model-102456839.html
- Sohu (sample mode): https://www.sohu.com/a/1079644751_122066678

## Community and third parties (for experience)

- XiaoJieAi66/XiaoJieAigc-seedance-2-5-video-prompt (a community Seedance 2.5 skill): https://github.com/XiaoJieAi66/XiaoJieAigc-seedance-2-5-video-prompt . Main points: ask three key questions first; for each asset write "what to use, what to keep, what not to use"; for each range write "time range → framing and position → subject's start state → visible action and path → camera movement or focus → end frame → link to the next range"; separate subject motion from camera motion; write the object, its shadow, and its reflection separately; a locked-off camera does not mean a frozen picture.
- AI Xingqiu's long write-up of the official guide: https://www.aixq.cc/59824.html (the phase form "Starts with / Main event / Ends with", fixing a single master before editing, stating the last-frame state before extending, the writing order for seamless transitions)
- Higgsfield prompt library: https://higgsfield.ai/blog/seedance-2-5-prompting-guide (global style → scene → characters → location → first-frame positions → shot by shot → camera → physics → light → audio; locking headcount, screen direction, and axis; binding lines to time points)
- Morphed: https://morphed.app/blog/seedance-2-5-prompts (time ranges instead of "Shot 1/2/3" for one take; the middle, around 12–18 s, drifts most easily; 1–2 assets are steadiest, and beyond about 6 the jobs start to bleed into each other)
- PicLumen: https://www.piclumen.com/blog/seedance-2-5-ai-video-generator-prompt-guide/ (one job per asset; identity goes to the asset, and the prompt handles only action)
- seedance.tv: https://www.seedance.tv/blog/seedance-2-5-prompt-guide (1–2 camera moves per range; for image-to-video describe only action and camera, without restating what the image already shows)

## Unconfirmed or disputed points

- "Native 4K": the API docs list only 480p, 720p, and 1080p. 4K is an upscaling feature in apps such as Jimeng and Xiaoyunque.
- The Xiaoyunque handbook claims "extra-long video, up to about 5 minutes generated natively": that is a platform feature, not something a single API generation can do.
- Symbols for dialogue and sound (corrected): the Volcano Ark Seedance 2.5 tutorial states "sound is distinguished with special characters: music uses (), sound effects use <>, dialogue uses {}, subtitles use 【】", and the official sd25-pe symbol table is identical, so this is an official rule and not just a convention. Official examples also use 【】 for section labels. Because heading-like text has turned up in generated pictures, this skill writes labels as plain words. (An earlier note, based on the AI Xingqiu write-up, that "square brackets mean subtitles" was wrong.)
- Third-party SEO guide pages (atlabs, cometapi, framia, seedance.tv, and others) often contradict each other on parameters, and some come from API resellers; treat them as reference only. seedance.tv is unrelated to ByteDance.
- "720p follows prompts best": personal experience, not systematically verified.
- Credit prices, resolution options, and asset limits can differ between platforms; go by the platform interface.
