# AI prompt skills for anthro fantasy short films (Seedance 2.5 + GPT Image)

English | [简体中文](README.md)

Three Agent Skills, installable in Claude and other agent tools, for making AI images and video of **western-fantasy stories with anthro (furry / kemono) characters**. The main look is **realistic CG**, and cel-shaded anime and hand-painted fantasy illustration are covered as well. General subjects (ads, short drama, posters, product shots) work too.

The content comes from the author's own production of anthro short films, checked against the official Volcano Ark prompt guide, the official sd25-pe skill, and OpenAI's guide, with community experience as a supplement. Every rule carries an evidence tag: [official], [multi-source], [single source], [inference], [author-tested]. Research date 2026-10-28, covering **Seedance 2.5 (4–30 s, focused on 30 s)** and **GPT Image 2 / 2.5 (Flare, Sunburst)**.

## The three skills

| Skill | What it does |
|---|---|
| `seedance-video-prompt` | Turns an idea, script, storyboard, or references into a Seedance 2.5 video prompt, with an asset list, platform settings, and dialogue drafts. Dedicated references for anthro dialogue scenes, fights, and close-ups, plus six complete 30-second templates |
| `gpt-image-prompt` | Turns an idea or reference-image request into a GPT Image prompt, with settings and follow-up edits. Fixed methods for anthro design sheets, expression sheets, mouth-shape sheets, and single-view references and empty plates for video |
| `kemono-short-film-craft` | A whole production method for anthro short films: three checks before starting, character iteration from sketch to 4K final, scenes, directing a story into 30-second segments, review, edit, and release |

The skills are independent; install one, or all three for a full short film.

## Repository layout

| Path | Contents |
|---|---|
| `skills/en/` | The three skills in English (English prompt templates, Japanese dialogue kept as written). `skills/en/README.md` is the pack overview |
| `skills/zh/` | The three skills in Chinese |
| `docs/资源与社区推荐.md` | A recommended list of GitHub repos, communities, books, and tools, and sources to avoid (Chinese) |
| `legacy/seedance-2-5-prompt/` | The first version of the skill, with its validator script and tests, kept as an archive |
| `tools/build_pack.py` | Builds the English edition into one skill-pack zip |

Each skill's `references/` holds a `creator-profile.template.md`: copy it to `creator-profile.md` and fill in your own series, characters, and lessons learned, and the skill reads it before writing. Keep that profile local.

## Install

- **Claude (web or desktop)**: zip each of the three folders under `skills/en/` separately and upload them under Skills in settings.
- **Claude Code**: copy the three folders into `~/.claude/skills/` or a project's `.claude/skills/`.
- **Other tools that support Agent Skills**: place the folders in that tool's skills directory.

Then just ask, for example: "Write a 30-second night conversation between two wolf knights" or "Make a design sheet for a German shepherd knight".

---

## GPT Image quick reference: the 10 most useful lessons

1. **Purpose and canvas before the subject.** "A 3:4 portrait poster for a shop lightbox" goes first, so the model plans the layout first.
2. **Specific nouns beat adjectives.** "Premium, 8K, masterful" do almost nothing; use 5–12 specific objects + a light direction + 3–4 colours.
3. **All text to appear goes in quotes, exactly as given,** with position, typeface character, hierarchy, and number of occurrences.
4. **Constraints as positive "only…" and "keep…".** In the author's tests negative wording damages detail. Text-heavy posters are the exception and keep one line, "there is no other text besides the above".
5. **Anthro characters start with an identity card:** species anatomy, fur colour zones, eyes, paw-hands (four fingers and a thumb), one trait only he has, clothing piece by piece with materials; build is left to the reference image.
6. **Design sheets use a fixed layout:** front full body, back full body, and a head close-up in one image, with proportions matching the original art; crop to single views and remove text before feeding Seedance.
7. **An edit = one change + a keep-list.** Rewrite the keep-list every round and change one thing per round.
8. **Number multiple references and give each a role** (Image 1 character, Image 2 clothing, Image 3 scene), and ask for unified lighting.
9. **Parameters go in parameters.** Size, quality, and transparent background are set in the API; the ChatGPT web page has no parameter panel, so write the aspect ratio into the prompt.
10. **Choosing a model:** 2.5 Flare for speed, 2.5 Sunburst for finish. If results in the ChatGPT web page get clearly worse, start a new chat.

## Seedance 2.5, 30 seconds: the 12 most useful lessons

1. **Thirty seconds is not ten seconds stretched.** Split it into 5–9 shots, or a one-take in 3–4 ranges; use whole seconds, written continuously from 0 to 30.
2. **One change per range, with a visible end state.** The next range picks up from that state.
3. **Aspect ratio, duration, and resolution stay out of the prompt** and go in the platform settings (official sd25-pe). Time ranges stay in.
4. **Positive descriptions only, with no generic negative constraints added automatically.** "No background music" becomes "the only sounds are ambience, action sounds, and dialogue"; official negative sentences are kept only for troubleshooting.
5. **In a one-take, range boundaries are where cuts sneak in** (7.4 s in a test run). From the second range on, open each with "Without cutting, the camera keeps…", and write how the camera crosses between spaces.
6. **Dialogue format:** `Name (language, voice, emotion, to whom): {line}`. Each line once, in the shot where it happens; one speaker per range, with everyone else "listening quietly with his mouth closed".
7. **Sound symbols follow the official table:** music (), sound effects <>, dialogue {}, subtitles 【】. Write ambience through to the last second.
8. **Anthros are not animals:** write species anatomy and one trait only he has; give background figures a species; write "kneeling on one knee, torso upright", not "half-crouching". Emotion is written as what ears, tail, and gaze do.
9. **Write positions per camera as foreground and background.** In a community test, "facing each other across a table" alone failed 9 times out of 9; with foreground and background written for each shot it succeeded 3 out of 3.
10. **Write reactions as a causal chain:** trigger → a pause to take it in → first reaction → the body follows → afterglow → end state. Let the audience see the cause before the reaction close-up.
11. **Use only the lines the user gave.** When they gave none, the skill's "dialogue draft" stays outside the prompt until confirmed.
12. **Test cheaply:** a 480P sample first, then 720P once it works. Beyond 30 seconds, split into several clips or extend from the end.

---

## Main sources

- Volcano Ark, Seedance 2.5 prompt guide: https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide
- Volcano Ark, Seedance 2.5 tutorial (API): https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Official sd25-pe skill 0.1.1: https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip
- Xiaoyunque, Seedance 2.5 official handbook: https://www.xiaoyunque.com/tutorials/seedance-2-5
- OpenAI image prompting guide (including GPT Image 2.5): https://developers.openai.com/api/docs/guides/image-prompting

Community and other material: see `docs/资源与社区推荐.md` and the `references/sources.md` in each skill.
