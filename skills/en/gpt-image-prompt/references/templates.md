# GPT Image scenario templates

How to use: find the matching section, take the template, replace what is in [brackets], and delete lines you do not need. A template is a starting point: keep the structure and add or cut to fit the user's request.

These general templates keep a short official-style exclusion line at the end, which suits text-heavy and product work. For anthro character and scene images, use the all-positive method in `kemono-character-sheets.md` instead.

## Contents

1. Photoreal portrait / lifestyle photo
2. Product image / e-commerce hero shot
3. Transparent product cut-out
4. Poster / ad (text hierarchy)
5. Infographic / explainer / flow chart
6. UI mockup
7. Slide / data chart
8. Logo
9. Comic / multi-panel storyboard / grid
10. Character design sheet (consistency anchor)
11. Edits: outfit swap, background swap, object removal, light or weather, translation, sketch to render, style transfer, local replacement
12. Multi-image composite
13. First frames and reference images for video models (Seedance and others)
14. Structured JSON form (complex product renders)
15. Compact skeleton

---

## 1. Photoreal portrait / lifestyle photo

Key points: write "who shot it, in what situation"; keep real imperfections; give the person a framing, a gaze, and an interaction; use one dominant shooting frame. Suggested 1024×1536, medium.

```text
A real photo, [portrait 2:3], [how it was shot: e.g. "a moment caught casually by a friend on a phone", "a natural-light portrait for a magazine interview"].
Person: [age range, features, hairstyle, clothing material and colour], [doing what], gaze [looking where / not at the camera], [framing: half body / full body in frame].
Scene: [place, time], with [3–6 specific objects] in the background.
Light: [source + direction, e.g. "warm evening light slanting in through the window on the left, leaving the shadow of the window frame on the wall"].
Keep real skin texture, pores, strands of hair, and creases in the clothes, with natural proportions; no skin smoothing or beautifying, no over-sharpening, no studio look. No text or watermark anywhere in the picture.
```

Example:

```text
A real photo, portrait 2:3, like a moment caught casually by a friend on a phone. A watch repairer in his sixties, short greying hair, a loupe pushed up on his forehead, an old dark blue work jacket, bent over lifting a tiny gear with tweezers, not looking at the camera, half body in frame. The scene is a watch-repair stall of under ten square metres on an old street: opened pocket watches in the glass counter, a dozen wall clocks showing different times, a steaming cup of tea under the desk lamp. Light: afternoon daylight from the doorway plus the warm yellow pool of the desk lamp. Keep the wrinkles on his face and the calluses on his hands, with wear at the jacket cuffs; no skin smoothing, no studio lighting. No text or watermark anywhere in the picture.
```

## 2. Product image / e-commerce hero shot

Key points: lock the product's shape, material, and label text. If there is a photo of the real item, upload it as a reference and write "keep the product's shape, colour, and label exactly the same". Props serve the selling point. E-commerce hero shots are usually 1:1.

```text
A commercial product photograph, [square 1:1], for [an e-commerce hero shot / the top of a detail page / a social ad].
Subject: [product name, shape, material, colour; the label text "___"], placed [centre, slightly low / on the right third], taking about [60%] of the frame.
(With a reference image) Follow the product in Image 1, keeping its shape, proportions, colour, label text, and logo position exactly the same.
Scene and props: set on [surface material], with [2–4 props that echo the selling point, e.g. "cut limes, ice cubes, mint leaves"] around it.
Light: [softbox side light / rim light from behind / natural window light], with [real highlights / condensation droplets / a frosted finish] on the product's surface and a natural contact shadow beneath.
Palette: [3 colours]. Background [simple / blurred], with empty space at upper right for selling-point text (no text in this image).
No extra logos, no invented brand names, no watermark, no extra text.
```

## 3. Transparent product cut-out

Set `background=transparent` in the API, with png or webp output.

```text
Cut out the product in Image 1 and place it on a fully transparent background, centred, with a suitable margin all round. Keep the product's shape, proportions, and colour, with label text sharp and readable, and leave the product itself unchanged. Clean edges with no white fringe, halo, or leftover background; no shadow, no reflection, no checkerboard, no background elements at all.
```

## 4. Poster / ad

Key points: layout first, content second; all text in quotes, given exactly; state the hierarchy (what is largest). Check with the "three-glance test": the first glance identifies the theme, the second reads the selling point, the third finds the details.

Assign text slots by importance: largest = theme or shop name, then = selling point or offer, then = time and place, with a call to action optional. If the user gave only a shop name, a date, and an offer, set only those three and do not pad. For illustrated posters, state how the "paper colour" relates to the "scene" (e.g. "the edges of the main visual bleed out in watercolour to an off-white paper ground") so that "plain ground" and "full-bleed scene" do not contradict each other.

For print (door posters, display stands, roll-up banners):
- Choose the ratio from the finished size: 60×90 cm and 80×120 cm boards are 2:3 (1536×2304 through the API); A4/A3/A2 paper is about 1:1.41 (1440×2032 through the API; in ChatGPT choose 2:3 and trim after leaving a white margin); an 80×200 cm roll-up banner is 2:5 (1152×2880 through the API).
- Keep text at least 5% of the image width away from the edges.
- The model's long edge is usually around 1536–2560 pixels (larger sizes are experimental). For A3 and above, upscale first or ask the print shop to confirm sharpness.
- Do not have the model draw QR codes or barcodes; add real ones in post.

```text
Design a [portrait 2:3 (shop print) / 3:4 (social post)] [event / new product / brand] poster for [a shop display stand / a subway lightbox / social media], readable from a distance.
Layout: the top third is the title area, the middle is the main visual, the bottom is an information bar; generous margins all round, with text and image not overlapping.
Main visual: [subject + action + setting + light].
Style: [a specific style anchor, e.g. "modern Chinese, restrained empty space, rice-paper texture"], palette [3–4 colours].
Render only the following text ([language], clear strokes, no misspellings):
- Title: "[title]" (largest, [typeface character], [colour], centred)
- Subtitle: "[subtitle]" (below the title, medium size)
- Information: "[time / place / price]" (bottom information bar, small but clear)
- Call to action: "[CTA]" (lower right)
Each text item appears once; no other text, no garbled characters, no invented logos or sponsor marks.
```

Example:

```text
Design a portrait 3:4 poster for a new milk tea, for a shop lightbox, readable from a distance. Layout: the top third is the title area, the middle is the main visual, the bottom is a price bar, generous margins all round. Main visual: a clear plastic cup of cold-brew oolong milk tea, fine droplets on the cup wall, a few golden osmanthus blossoms floating inside, against a blurred late-autumn ginkgo tree and warm orange flecks of sunset light. Style: fresh Japanese-style commercial photography, in milk-coffee brown, osmanthus gold, and dark green.
Render only the following text (English, clear letterforms, no misspellings):
- Title: "Osmanthus Cold-Brew Oolong" (largest, rounded bold sans-serif, dark coffee brown, centred)
- Subtitle: "The first sweet sip of autumn" (below the title, medium, light weight)
- Price bar: "Regular $4 | Large $5" (bottom, white text on a dark green rounded strip)
Each text item appears once; no other text, no garbled characters, no invented logos.
```

## 5. Infographic / explainer / flow chart

Key points: state the audience and the process to explain; fix the layout zones first; give labels exactly; one flat icon style throughout; clear arrow direction. Use high for dense small text. Use only real or user-supplied data.

```text
A [portrait 2:3] infographic on [topic], for [audience, e.g. "upper primary school pupils"], to explain [a process / a structure / a comparison].
Layout zones: the title "[title]" at the top; in the middle [N] steps arranged [top to bottom / left to right], each with a flat icon + a number + a short label; one summary sentence "[summary]" at the bottom.
Step labels (render exactly): 1 "[ ]" 2 "[ ]" 3 "[ ]" 4 "[ ]".
Style: flat vector, icons with one line weight, white background, [2–3 main colours], arrows pointing clearly to the next step, labels large enough to read.
No extra decoration, no text too small to read, no invented data.
```

## 6. UI mockup

Key points: describe the product as if it had already shipped; write hierarchy, spacing, real interface elements, and realistic data; avoid wording like "concept art"; use an invented product name.

```text
A real screenshot of a phone app (not concept art), iPhone portrait, product name "[invented name]", an app for [purpose].
Screen: [home / detail / checkout]. From top to bottom: a navigation bar showing "[screen title]"; [cards / a list / a chart] showing [specific data, e.g. "Spent this month $3,280.50"]; a primary button reading "[button text]"; a bottom tab bar reading "Home", "Stats", "Me" in that order.
Design language: [light / dark] theme, main colour [colour], rounded cards, an 8pt spacing grid, a clear system typeface, icons with one line weight.
Text sharp and aligned, no garbled characters; no decoration beyond the device, no real brands.
```

## 7. Slide / data chart

Key points: landscape (e.g. 1536×864 or 2048×1152) + high; state the deliverable, the hierarchy, and real figures; for a minimal look, explicitly rule out clip art, stock photos, gradients, and shadows.

```text
One 16:9 presentation slide, title "[title]" (upper left, large bold).
The left 60% is a [bar chart / line chart]: x-axis "[x-axis name]", y-axis "[unit]", data: [A 12, B 18, C 25], with the value on top of each bar.
The right 40% is three bullet points (exact): "[point 1]" "[point 2]" "[point 3]".
A small footnote at lower right: "Source: [source]".
Style: white ground, two colours (dark blue and grey), ample empty space, thin axis lines; no clip art, no stock photos, no gradients or shadows, no extra decoration.
```

## 8. Logo

Key points: write the brand's personality and where it will be used; flat, simple, scalable; transparent background (parameter transparent); use `n` for several options at once.

```text
Design an original logo for the brand "[brand name]". The brand is [industry / product], with a [e.g. "warm, dependable, slightly playful"] personality.
Mark: [the core idea, e.g. "a leaf combined with a speech bubble"], flat, geometric, clean lines, recognisable at 16 pixels.
The wordmark "[brand name]" uses [typeface character], set [beside / below] the mark.
No more than 2 colours: [colours]. Transparent background with generous margins; no background, no shadows or 3D effects, no watermark, no other text.
```

## 9. Comic / multi-panel storyboard / grid

Key points: state the panel count and reading order first; one visual beat per panel; write the shared character traits, palette, and light; give dialogue exactly.

```text
A [portrait] [4-panel] comic, read top to bottom, with clear white gutters between panels. One art style: [style]; one character: [character anchor description].
Panel 1: [framing], [action / expression], speech balloon "[line]".
Panel 2: …
Panel 3: …
Panel 4: [twist / punchline], speech balloon "[line]".
The character's appearance, clothing, and palette stay the same in every panel; only the dialogue above appears, with no other text.
```

## 10. Character design sheet (consistency anchor)

Use it as the reference image for every later scene. A pure white background is steadiest. (For anthro characters, use the fixed layout in `kemono-character-sheets.md` section 3, which uses light grey.)

```text
A character reference sheet, landscape 16:9, pure white background.
Character: [name], [age / species], [face shape, features, hairstyle and colour], [body proportions], [clothing: material and colour of each piece], [signature accessory / prop].
Arrangement: on the left, front, side, and back full-body standing views (one scale); at upper right, 4 expression close-ups (happy, surprised, angry, sad); at lower right, 3 detail close-ups of accessories or props.
Even flat light with no cast shadows; art style [realistic / 3D / Japanese animation]; no text other than the character's name "[name]".
```

For video models, also generate front, side, and back each as a separate single-view image. Video models read separate single views more reliably than a combined sheet.

## 11. Edits

General pattern: **change only [X] + keep everything else + keep-list + exclusions**. Repeat the keep-list every round and change one thing per round.

Outfit swap (virtual try-on):

```text
Replace the clothing of the person in Image 1 with the [jacket / dress] in Image 2. Keep the person's face, skin tone, build, hairstyle, expression, and pose exactly the same; the garment's cut, colour, and fabric texture match Image 2, draping and creasing naturally with the pose, with light and shadow matching the original. Background, camera position, and composition unchanged; no added accessories, text, logos, or watermark.
```

Background swap / placing a person in a new scene:

```text
Place the person from Image 1 in [new scene]. Keep the person's identity, features, hairstyle, clothing, and pose unchanged. Re-match the light on the person, the skin reflections, and the contact shadow at the feet to the light direction of the new scene, with sound perspective and scale, so it reads as a real photo from a single shoot; no pasted-on look, no cinematic grading.
```

Object removal:

```text
Remove [the red umbrella held by the passer-by on the right] and fill in a plausible background. Change nothing else anywhere.
```

Light / weather:

```text
Change this photo to [a winter evening with light snow]: cold blue-grey tones, a thin layer of snow on roofs and ground, snowflakes drifting in the air. Change only the ambient light and weather; buildings, people, object positions, camera position, and composition stay exactly the same.
```

Translating text in an image:

```text
Translate all the [source language] text in the image into [target language]. Replace only the wording, keeping the original typeface style, size hierarchy, colour, position, and layout, without re-laying it out; all other visual elements stay exactly the same.
```

Sketch to render:

```text
Render this hand-drawn sketch as [a realistic interior visualisation]. Keep the sketch's layout, proportions, perspective, and the position of every object strictly; add real materials ([oak flooring, a linen sofa, brass lamps]) and [afternoon daylight]. Add no objects or text that are not in the sketch.
```

Style transfer:

```text
Draw [new subject / new scene] in the style of Image 1 ([palette, brushwork, paper texture, grain]). Borrow only the style, without copying the composition or content of Image 1; white background, no extra elements.
```

Local replacement:

```text
Replace every chair in the picture with [a pale solid-wood chair]. Keep the camera position, light, shadows, table, and everything else unchanged.
```

## 12. Multi-image composite

```text
Image 1: [photo of a person] (keep face, hairstyle, build); Image 2: [clothing] (keep cut and fabric); Image 3: [photo of a scene] (as the background); Image 4: [style reference] (take only tone and grain).
Generate a [portrait 2:3] realistic photo: the person from Image 1 wearing the clothing from Image 2, standing in the scene of Image 3 [position / action], with the overall tone following Image 4.
One light direction, from [direction]; perspective, scale, contact shadows, and reflections consistent between person and environment; do not change the person's features; no added text or logos.
```

## 13. First frames and reference images for video models (Seedance and others)

- First frame: the same aspect ratio as the video (16:9 video, 16:9 image); the composition is the picture at the video's first second; the characters are in the state before the action begins; no text on the image.
- Character references: front, side, and back each as a separate single-view image, on a plain background with flat light, full body complete, no text. This suits video models better than a combined three-view sheet.
- No over-sharpening and no cluttered background. The image resolution need not exceed the video's output resolution (the Seedance docs note that too high a resolution can produce a fingerprint-like texture).
- First and last frames share an aspect ratio, and the last frame should be a state the first frame can plausibly reach through the action.

## 14. Structured JSON form (complex product renders)

When environment, subject, materials, lighting, particles, and moving elements all need control at once, a JSON-like structure is easier to steer. Keys name the visual subsystems and values state specific, visible constraints:

```text
{
  "canvas": "2:3 portrait, commercial advertising photography, sharp foreground, visible micro-texture",
  "environment": {"background": "warm orange gradient studio backdrop", "lighting": "softbox at upper right + rim light from rear left", "atmosphere": ["fine drifting mist", "soft out-of-focus highlights"]},
  "subject": {"product": "cold-brew coffee in a frosted glass bottle", "materials": ["frosted glass", "condensation droplets on the bottle", "kraft paper label"], "composition": "bottle tilted 15°, centre frame, slightly low"},
  "dynamic_elements": [{"object": "coffee beans", "state": "suspended in the air"}, {"object": "coffee", "state": "a thick arc splashing from the bottle mouth"}],
  "text": "the label reads only \"COLD BREW\"; no other text anywhere",
  "avoid": ["cheap e-commerce banner look", "plastic CG look", "invented brand logos"]
}
```

## 15. Compact skeleton

```text
Create a [2:3 portrait] [photo / poster / infographic / UI screen] for [use case].
Scene: [place, time, weather, 5–12 concrete objects].
Subject: [who/what, appearance, pose, action, gaze, interaction], placed [where, how large].
Composition and camera: [shot size, angle, foreground/background, negative space]; [capture context, e.g. "candid phone photo"].
Light and colour: [light source + direction]; palette [3–4 colours]; materials [list].
Style: [a specific, bounded style anchor].
Text: render only these exact strings: title "[...]" ([position, type style, colour, size]); subtitle "[...]". No other text.
Constraints: keep [...]; no watermark, no logos, no extra text; [1–3 targeted avoids].
```
