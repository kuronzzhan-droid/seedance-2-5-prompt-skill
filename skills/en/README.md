# Anthro Fantasy Film Kit for Seedance 2.5 and GPT Image

Three Agent Skills for making AI images and video of **western-fantasy stories with anthro (furry / kemono) characters**. The main look is **realistic CG** (real fur, leather, and light, with faces that act), and two more styles are covered: cel-shaded anime and hand-painted fantasy illustration. General subjects such as ads, short drama, posters, and product shots work too.

The rules come from the author's own production of anthro short films, checked against the official Volcano Ark Seedance 2.5 prompt guide, the official sd25-pe skill, and OpenAI's image prompting guide. Every rule carries an evidence tag: [official], [multi-source], [single source], [inference], or [author-tested], so you can see what is documented and what is one creator's experience.

## What is in the pack

| Skill | What it does |
|---|---|
| `seedance-video-prompt` | Turns an idea, script, storyboard, or set of references into a submit-ready Seedance 2.5 video prompt (4–30 s, focused on 30 s), with an asset list, platform settings, and dialogue drafts. Includes dedicated references for anthro dialogue scenes, fights and close-ups, shot grammar across anime, TV drama, and film, a camera and sound glossary, and six complete 30-second templates. |
| `gpt-image-prompt` | Turns an idea or reference-image request into a GPT Image prompt (GPT Image 2 / 2.5), with settings and single-change follow-up edits. Includes a fixed method for anthro design sheets, expression sheets, mouth-shape sheets, single-view references and empty plates for video, and Japanese text in images. |
| `kemono-short-film-craft` | A whole production method for anthro short films: three checks before starting, iterating a character from sketch to 4K final, scenes, directing a story into 30-second segments, review, edit, and release. |

The three skills are independent. Install one, or all three for a full short-film workflow: craft for story and direction, image for character and scene references, video for the clips.

## What makes it different

- **Anthro characters that stay anthro.** Species written as visible anatomy, one identifying trait per character, paw-hands, muzzle lip-sync, and acting through ears and tail, so characters do not collapse into humans with animal ears.
- **Thirty seconds planned by the second.** A time budget per segment, one change per segment, and a visible end state for every segment, which is what keeps a 30-second clip from repeating or drifting.
- **Positive wording throughout.** Exclusions are rewritten as "the only … is …", which protects detail; official negative phrasing is kept only as a troubleshooting fallback.
- **Dialogue that lands on the right mouth.** One speaker per time range, everyone else "listens quietly with his mouth closed", lines written once where they happen.
- **Evidence tags and sources.** Each reference file ends with its sources, and unconfirmed claims are marked as such.

## Good to know

- The sample cast speaks Japanese, and the example dialogue is kept in Japanese inside otherwise English prompts. The format works for any language: change the language label and the line.
- Reference tokens are written `@Image1`, `@Video1`, `@Audio1`. On Jimeng (the Chinese site) the same tokens appear as `@图片1` and so on; use whatever the platform inserts.
- Model versions, prices, and platform features are a snapshot from late October 2026. When in doubt, the platform interface and official docs win.
- Each skill has a `references/creator-profile.template.md`. Copy it to `creator-profile.md` and fill in your own series, characters, and lessons learned; the skill reads it before writing.

## Install

- **Claude (web or desktop)**: zip each of the three skill folders separately and upload them under Skills in settings.
- **Claude Code**: copy the three folders into `~/.claude/skills/` (all projects) or a project's `.claude/skills/`.
- **Other tools that support Agent Skills**: place the folders in that tool's skills directory.

Then just ask, for example: "Write a 30-second night conversation between two wolf knights", "Make a design sheet for a German shepherd knight", or "Check whether this short-film story is ready to start".
