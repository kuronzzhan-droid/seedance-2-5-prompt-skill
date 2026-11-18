---
name: gpt-image-prompt
description: Use when the user wants an image made or edited with GPT Image (ChatGPT image generation, gpt-image-2, GPT Image 2.5 Flare/Sunburst), or wants an image prompt written or improved. Strongest on western-fantasy and anthro (furry / kemono) characters in a realistic CG look, with cel-shaded and hand-painted styles also covered — character sheets, expression sheets, stills, and first frames or character references for video models. Also handles posters, ads, product shots, infographics, slides, UI mockups, logos, comic panels, photoreal portraits, outfit or background swaps, and text-heavy layouts. Returns a paste-ready prompt, size and quality settings, and single-change follow-up edits. Use it even when the user never says "prompt".
summary: Turn an idea, draft, or set of reference images into a GPT Image prompt that works first time, with a tested method for realistic-CG anthro and western-fantasy character sheets.
version: 2.1.0
tags: [gpt-image, image-generation, prompt-engineering, character-design, furry, kemono, fantasy]
---

# GPT Image prompt optimisation

Goal: translate "the image the user wants" into a **visual specification** that GPT Image executes reliably.

Why write it this way: from GPT Image 2 onward the generation pipeline includes reasoning, so the model reads long text in full and follows it literally. A good prompt therefore reads like a design brief (purpose, canvas, content, text, constraints all stated) and not like a string of style words. The Stable Diffusion / Midjourney habit of "masterpiece, best quality, 8K, trending on artstation" does almost nothing here and only dilutes what matters.

The anthro part of this skill comes from the author's tested practice: drawing adult male anthro characters (design sheets, expression sheets, stills) for western-fantasy stories, mainly in a realistic CG look, then feeding those images to Seedance for video. Before drawing anthro characters read `references/kemono-character-sheets.md`. If `references/creator-profile.md` exists (the user's own optional creator profile, filled in from `references/creator-profile.template.md`), read it first too. Skip both for general subjects.

## Delivery format

Reply like this by default:

1. **Prompt**: in one `text` code block, ready to paste.
2. **Settings**: model / size (pixels) / quality / background / number of images. These are set as API parameters and stay out of the prompt. In the ChatGPT web page or app the user can adjust almost none of them: drop this item, write the aspect ratio into the prompt, and mention only features the interface really has (see the last item under "Models and parameters").
3. **Assumptions** (if any): one line listing the choices you made for the user, so they can change them.
4. **What to change next round**: 1–2 single-change edit instructions that anticipate the likeliest problem (usually small text, hands, brand elements, character consistency). Common anthro problems and their fixes are all written as a positive "change only this": drawn as a human with animal ears → "Change only the character's head to a complete wolf head with a long muzzle, the face covered in fur; keep clothing, pose, composition, and light as they are"; wrong finger count → "Change only both hands to canine paw-hands, four fingers and a thumb; keep everything else as it is"; an identifying trait moved → "Move only the scar back to its position in Image 1; keep everything else as it is".

When the user says "just the prompt" or similar, use the short form: no questions, code block first, then at most 2–3 lines (assumptions + the one edit instruction most likely to be needed). Give the code block alone only when the user explicitly says "no explanation, code only".

The prompt language follows the user. Text to be rendered on the image always stays exactly as the user gave it, untranslated and unpolished.

## Workflow

### 1. Identify the task type

| Type | Typical request | First acceptance check |
|---|---|---|
| Text-to-image | A photo, illustration, or render from scratch | Subject, composition, style |
| Text-heavy | Posters, ads, infographics, UI, slides, charts, menus, packaging | Every character correct, clear hierarchy |
| Edit | One change only: outfit, background, object removal, light or weather, translating text | The change is right and nothing else moved |
| Multi-image composite | Person + clothing + scene + style from several references | Each element from the right source, unified lighting |
| Series consistency | Picture books, storyboards, e-commerce sets, one character across scenes | Character or product consistent across images |
| Anthro characters | Design sheets, expression sheets, stills, single-view references and empty plates for video | Species anatomy, identifying traits, hand structure, and proportions match the original art |

### 2. Fill only the gaps that change the result

Worth asking about: purpose or placement, aspect ratio, **the exact text that must appear**, identity or brand elements that must be kept, style direction. Ask at most 3 at once. If the user says "just write it", use defaults and list them under Assumptions:

- Aspect ratio: printed shop posters, portraits, phone portrait screens → 2:3; portrait social posts → 3:4; landscape scenes, slides, covers → 16:9; square social images, logos → 1:1. With a creator profile, use the series ratio in the profile. For A-series paper or roll-up banners, see the print notes in `references/templates.md` section 4.
- Style: when the user gives a mood word (cosy, premium, techy, heritage…), pick the medium from that first; otherwise infer from purpose (ad → commercial photography; explainer → flat vector infographic; UI → the look of a real product screenshot). The model cannot read a mood word by itself, so translate it into concrete controls, for example:
  - Cosy → warm side light, off-white paper grain, rounded or handwritten type, watercolour and coloured-pencil illustration or warm-light lifestyle photography
  - Premium → large empty areas, low-saturation palette, thin serif type, a single light source
  - Techy → dark background, cool accents, geometric grid, glowing hairlines, sans-serif type
  - Chinese heritage (guochao) → vermilion, ink black, and gold, calligraphic or Song-style titles, traditional patterns as borders
- Copy: use what the user gave, word for word. When they gave none, do not invent long copy; place one placeholder title with a reminder to replace it, or make a text-free version.
- Facts such as dates and prices are used as written. If a date does not match today (already past, say) or lacks a year or weekday, do not complete it yourself; ask the user to confirm in one sentence.

### 3. Write to a structure

The officially recommended order: **purpose and canvas → scene/background → subject → key details → constraints**. Use labelled sections for complex requests; a sentence or two is enough for simple ones. Keep it as short as possible, but be specific wherever specifics matter.

General skeleton (trim as needed; not every field has to be filled):

```text
Purpose / canvas: a 2:3 portrait ___ (poster / product hero shot / infographic / realistic photo…), for ___.
Scene: place, time, weather; 5–12 specific objects in the environment.
Subject: who or what, appearance, pose, action, gaze, interaction with objects; position and size in frame.
Composition and camera: framing, viewpoint / camera position, foreground-midground-background, where the empty space is; how it was shot (e.g. "casual phone snapshot", "the feel of an 85mm portrait lens").
Light and colour: source type + direction (e.g. "the source is a window at off-screen left, soft morning light"); a palette of 3–4 specific colours; key materials.
Style / medium: a specific, bounded style anchor (e.g. "Swiss grid typography + screen-print texture", "Japanese cel animation").
Text: the only text in the image is the following: title "___" (position, typeface character, colour, hierarchy); subtitle "___"…; each appears once. Surfaces such as packaging, cups, signs, and tablecloths stay plain.
Constraints: must keep ___; then, for the default mistakes the model makes most, 1–3 positive "only…" or "keep…" lines, e.g. "the only brand mark in the image is the one already on the product in Image 1".
```

Write constraints as positives first. In the author's tests, negative wording (do not / no / avoid) damages detail; OpenAI's own guidance is to write exclusions straight into the prompt (the API has no negative-prompt parameter). The compromise: character and scene images use positive wording throughout. Text-heavy images (posters, infographics, UI) keep one official-style exclusion by default, "there is no other text besides the above", because a local poster test rendered every character correctly with that sentence in place. Everywhere else, add 1–2 exclusion sentences only when positive wording fails to suppress a default mistake (fake logos, garbled small text, extra people), and say in the reply that this is negative wording.

Anthro character images always use three sections: "Style:", "Picture / camera:", "Character:". The aspect ratio opens the Style section (the ChatGPT web page has no parameter panel). With a creator profile, copy the style line from creator-profile.md as is. Describe appearance part by part: fur colour zones, eyes, hands, clothing materials. Fix quantities, for example "three to five large colour masses". For a clean image write "matte flat colour, little detail" [author-tested].

### 4. Add the scene-specific notes

When you reach a specific type, open the matching reference file and read only the section you need:
- Anthro identity cards, design sheets, expression sheets, single views and empty plates for Seedance, Japanese typesetting: `references/kemono-character-sheets.md`
- Photoreal portraits, product and e-commerce, transparent cut-outs, posters and ads, infographics, UI, slide charts, logos, comic panels, character design, edits, multi-image composites, reference images for video models, structured JSON prompts: `references/templates.md`

### 5. Check before delivering

- Do the aspect ratio in the prompt and the size in the settings agree? (16:9 in the text must not be paired with 1024×1536.)
- Is every piece of text to be shown in quotation marks, exact, and given a position? Does it say "each appears once"?
- Any empty adjectives left (premium, beautiful, high quality, 8K, masterful)? Replace them with visible nouns, materials, and light.
- Any contradictions? ("Minimal" yet "rich in detail"; "top-down" yet "looking up"; "pure white background" yet "city street".)
- Edits: is there "change only X" plus a full keep-list? Is it one change per round?
- Are constraints all positive "only…" and "keep…" lines? Are exclusions for stubborn default mistakes limited to 1–2 and flagged in the reply as negative wording?
- Anthro characters: are species anatomy, the trait only he has, hand structure, and clothing materials written? Is build left to the reference image? Is the light source given as a side of the off-screen space? Do background figures have a stated species?
- Is the style written as visible traits (medium, line, colouring, light, palette), with no artist, director, studio, or title named?
- Review: give the image to one reviewing model only, then zoom to 100% yourself. Look first at whether the face is an animal face and at hand and foot structure. Hand uncertain calls to the user instead of stacking votes from several models [author-tested].

## Core techniques (with reasons)

**1. Set purpose and canvas before the subject.** Purpose decides the level of polish and the layout language; an ad, a UI, and a casual snapshot are entirely different. Layout is written before detail, otherwise the model spends its "detail budget" on the subject and improvises the layout.

**2. Specific nouns beat adjectives.** "A convenience store late at night" is weaker than "promo stickers on the chiller, a wet doormat, neon reflections on the glass, steam from the oden pot by the till". Rule of thumb: 5–12 specific nouns for the scene plus 2–4 material or light constraints. Material, light, and palette are three separate controls; write them separately and do not wave them through with "premium".

**3. Text rendering is a strength of GPT Image and the area that most needs rules.**
- Put all text to appear in quotation marks, exactly as given; state position, typeface character, colour, size hierarchy, and number of occurrences (e.g. "appears once").
- Add "the only text in the image is the above, and each appears once".
- Brand names, rare words, and error-prone words can be spelled letter by letter (e.g. B-L-O-O-M). For Chinese, state "Simplified Chinese" and ask for clear strokes with every character matching the source. For Japanese, state "Japanese (Japanese kanji forms and kana)" and give the source text exactly.
- Copy numbers, dates, and prices as written and add "numbers in Arabic numerals", or "20% off" may be spelled out in words.
- Name the surfaces where extra text tends to appear: packaging, cups, signs, blackboards, tablecloths, screens, and write "these surfaces stay plain". Shopfront images often sprout decorative words like "BAKERY", "OPEN", "COFFEE"; if they still appear, remove them with a "change only this" edit.
- When text has ranks, layer it by importance: largest is the theme or shop name, then the selling point or offer, then time and place; a call to action is optional. If the user gave only a few sentences, do not pad with a subtitle or call to action.
- Small text and dense information (infographics, slides, the back of a package) need medium or high quality. Long passages can still go wrong: iterate block by block and proofread every character by hand at the end.

**4. Realistic photos: write "how this photo was taken", not a pile of camera settings.** State "a real photo / photorealistic / casual phone snapshot / professional photography", then the lens feel, light, time, and occasion. Realism keeps imperfection: pores, fine lines, creased clothes, wear, everyday clutter in the background. Realistic scenes do not use wording like "studio-perfect, airbrushed, retouched" [official]. For anthro fur write: the direction of fur flow, zones of long and short fur, the rim light through the fur tips given which off-screen side the source is on, wet fur clumping into locks, sharp whiskers [inference]. Camera settings are only appearance hints, not a physical simulation. Pick one dominant shooting frame; too many settings fight each other.

**5. People: write framing, gaze, and interaction.** For example "full body in frame, looking down at the book in his hands and not at the camera".

**6. Constraints as positive "only…" and "keep…".** Rewrite exclusions as positives first: "the only text in the image is the following three items", "Kael is the only character in the whole image", "the hands are canine paw-hands, four fingers and a thumb, with a clear and stable structure". Add 1–2 exclusion sentences only when positive wording cannot suppress a default mistake, and flag them in the reply (text-heavy images are the exception, see step 3).

**7. An edit = one change + one keep-list.** Pattern: "Change only ___ to ___; keep everything else as it is: the person's identity / expression / pose, composition, camera position, light, background, existing text." Rewrite the keep-list every round, because drift accumulates across rounds; change one thing per round. For regions that must stay pixel-identical, composite the edited part back onto the original, since a prompt cannot lock pixels.

**8. Multiple references: number + role + how to combine.** "Image 1: product photo (keep shape and label); Image 2: style reference (take only palette and brushwork); Image 3: scene." Then say how they combine. In a composite, ask for consistent light direction, perspective, scale, and contact shadows so nothing looks pasted on.

**9. Consistency: make an anchor first, then reuse it.** Generate one complete anchor image of the character or product. A multi-view design sheet on a pure white background is steadiest, because a styled background carries its light into later images. After that, attach the anchor every time, restate the key traits in the prompt, and describe only the new scene.

Anthro characters: write one fixed "identity card" and copy it unchanged into every image. Write the species as visible anatomy (for a wolf: a complete wolf head with a long muzzle, fur over the whole body, upright on two legs), then fur colour zones, eyes, hands (for canines "canine paw-hands, four fingers and a thumb"; other species follow the reference image), one trait only he has, and clothing piece by piece with materials. Leave build to the reference image with no build adjectives, and write light as "the source is off-screen left" [author-tested; the anatomy wording is inference]. The design-sheet layout is fixed: front full body, back full body, and a head close-up in one image, with height and head-to-body ratio matching the original art across all three views [author-tested]. Before feeding Seedance, crop to single views (one head, one full-body front), remove names and annotations, and keep the aspect ratio within 0.4–2.5 [official]. Video references always use the 4K finals [author-tested]; if a fingerprint-like texture appears, downscale to no more than the video's output resolution [official troubleshooting advice]. Full method in `references/kemono-character-sheets.md`.

**10. Iterate: one variable at a time.** Get a clean base version, then look at the image and name exactly what is wrong (which character, which region, which relation), then make a single-point change ("a little warmer light", "restore the original background"). Tell the causes apart: blurry small text or thin detail → raise quality; wrong content or composition → change the prompt. References like "the same style as before" drift, so rewrite key constraints every round.

## Models and parameters (as of 2026-10; the OpenAI docs are authoritative)

| Model | API ID | Use |
|---|---|---|
| GPT Image 2.5 Flare | `gpt-image-2.5-flare` | Speed first: everyday images, quick direction tests; quality on par with GPT Image 2 |
| GPT Image 2.5 Sunburst | `gpt-image-2.5-sunburst` | Quality first: fine edits, complex layouts, subject fidelity |
| GPT Image 2 | `gpt-image-2` | Compatibility with existing workflows (released 2026-04, the first with reasoning in generation) |
| gpt-image-1.5 / 1 / 1-mini | — | Older; only for migration or cheap batch drafts |

The official selection strategy: get a complex task working on Sunburst, then try the same prompt on Flare and switch if quality holds. If an existing GPT Image 2 workflow is good enough, try Flare directly for speed. The API has no generic `gpt-image-2.5` ID: when the user says only "GPT 2.5", ask whether they want Flare or Sunburst, or choose for them and say why.

- **quality**: `low / medium / high`, with `xhigh / max` added in 2.5; default `auto`. Raise it step by step as needed; higher is not always better (max is much slower). When comparing models, fix the quality by hand and do not use auto.
- **size**: width and height are multiples of 16, long edge ≤ 3840, aspect ≤ 3:1, total pixels between 655,360 and 8,294,400; above 2560×1440 is experimental. Common sizes: 1024×1024 (1:1), 1024×1536 (2:3), 1536×1024 (3:2), 1536×2048 (3:4), 2048×1152 (16:9), 1152×2048 (9:16), 2048×2048, 3840×2160 (4K, experimental). For 21:9 use 2688×1152. Writing "4K" in the prompt does not change the actual resolution.
- **background**: for a transparent background use `transparent` with png or webp (jpeg does not support it). Do not ask for a "checkerboard background" in the prompt; that paints a fake checkerboard.
- **input_fidelity**: do not pass it to `gpt-image-2`, which always processes input images at high fidelity.
- **n**: several variants at once, good for logos and composition exploration.
- **4K finals** (the author's workflow): explore directions in the ChatGPT web page first, and go to the API once the look is settled. Finals use `images.edit` from the original reference images, not an upscale of a small web image; model `gpt-image-2.5-sunburst`, `quality: high`, with 2:3 portrait topping out at 2352×3520 (about 8.29 MP in total; 2560×3840 returns a 400 and is not charged). Each image came to about US$0.32 in practice; budget on that and report the spend each round [author-tested, 2026-11].
- **ChatGPT web / app**: with no parameter panel, write the aspect ratio into the prompt (e.g. "landscape 16:9"). For complex layouts and infographics, Thinking mode lets the model plan the layout first. The 2.5-era ChatGPT also has sketch-to-image, templates, and circling a region on the image to comment for a local change; prefer circling for local edits. The web page sometimes downgrades the model, and when results get clearly worse, start a new chat and rerun [author-tested]. Go by the interface.

## Limits

- Real people's likenesses, celebrities, and adaptations of others' work: remind the user that they need the rights, and that platform moderation may block it. Default to original characters and original brands.
- Styles are written without naming an artist, director, studio, or title; break them into visible traits, for example "thick-paint digital painting, clear directional brushstrokes, warm rim light, a low-saturation background".
- Original characters only, stated as "adult male"; clothing is written as specific cut and material. Bare-chested characters are occasionally stopped by moderation; rerunning once is enough [author-tested].
- Data, dates, prices, and medical or scientific content on an image: use only what the user supplied or what has been verified, never invented, and proofread after generation.
- Other image models (Midjourney, Jimeng image, Nano Banana, and so on) can borrow the "structure + quoted text + constraints" method, but the parameter section does not apply.

## Reference files

- `references/creator-profile.template.md`: the creator profile template. Once filled in and saved as `references/creator-profile.md`, it is read before drawing characters.
- `references/kemono-character-sheets.md`: anthro identity cards, design sheets (front full body + back full body + head close-up), expression sheets, mouth-shape references, single-view references and empty plates for Seedance, Japanese typesetting. Read before drawing anthro characters.
- `references/templates.md`: copy-ready templates and examples by scenario.
- `references/sources.md`: research sources, the version timeline, and which claims are not officially confirmed. Read when the user asks about model versions, whether parameters are current, or whether a claim is official.
