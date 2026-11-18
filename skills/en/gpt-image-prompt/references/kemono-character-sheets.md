# Anthro character images: design sheets, expressions, mouth shapes, Seedance references, and Japanese text in images

## When to read this file

Read it when making anthro character images with GPT Image 2 / 2.5 (in the ChatGPT web page or through the API): character design sheets, expression sheets, mouth-shape sheets, single-view references and empty camera plates for Seedance, first frames and keyframes, and comic pages with Japanese text. Read only the section you need. General method (text, edits, multi-image composites) is in SKILL.md and `templates.md`. When both skills are installed, the identifying traits and voices of the full sample cast are in `references/kemono-jp-drama.md` 1.1 and 2.2 of seedance-video-prompt, and how these images are used in video (dialogue, muzzle lip sync, shots) is in the same `kemono-jp-drama.md`.

Tags: [official] OpenAI, Volcano Ark, and Xiaoyunque official docs and the official sd25-pe skill; [multi-source] two or more unofficial sources agree; [single source] one unofficial source only; [inference] derived from the material, not tested; [author-tested] the author's own setups and lessons learned; [test run] one local generation on 2026-10-28. The last two are also single sources.

## Contents

1. Fixed wording and the character section
2. Style lines for the three art-style lines
3. Character design sheet (fixed layout)
4. Expression sheet: ears, tail, muzzle
5. Mouth-shape sheet: a lip-sync reference for Japanese
6. Single-view references and empty camera plates for Seedance
7. First frames, last frames, and keyframes
8. Japanese text in images: balloons, vertical text, ruby, typefaces, hand-drawn sound effects
9. ChatGPT practice and single-point edits
10. Check before delivering
11. Sources

## 1. Fixed wording and the character section

Three fixed sections: "Style:" → "Picture / camera:" → "Character:" [author-tested]. When the image carries text, add a "Text:" section [inference, based on OpenAI's text guidance].

| Habit | Wording | Source |
|---|---|---|
| Aspect ratio in the text | The first sentence says "landscape 16:9" or "landscape 21:9": the ChatGPT web page has no parameter panel. Through the API, pixel size and quality go in the parameters; "4K" in the prompt cannot change resolution | Author-tested; official |
| Appearance part by part | Species anatomy → fur colour zones → eyes → hands → feet → clothing (material and colour piece by piece) → the trait only he has | Author-tested |
| Species as anatomy | "A complete wolf head with a long muzzle, black fur over the whole body, upright on two legs". Words like "animal ears", "cat ears", or "kemonomimi" pull the face toward a human one | Multi-source |
| Hands | For canines (Kael, Gerard, Wachhund) write "canine paw-hands, four fingers and a thumb"; hands of other species follow Image 1 | Author-tested; the split by species is inference |
| Feet and build | A barefoot character gets a sentence of its own, with the feet following the original art. For build write only "full-body proportions follow Image 1", with no build adjectives | Author-tested |
| Fixed quantities | "Three views", "two rows of three, six panels in all", "three to five large colour masses", "the only text is the following two items" | Author-tested |
| A clean picture | Add "matte flat colour, little detail". This suits the two 2D lines and empty plates; the hyper-realistic line needs realistic fur and does not take it | Author-tested; the scope is inference |
| Light | State which off-screen side the source is on. "Backlit" produces a halo above the head (the note does not say on which platform, so write it this way for both images and video) | Author-tested |
| Positive wording | Write the wanted state. To exclude something, write "the only things in the picture are ___" | Author-tested: negative wording damages detail |
| Style | Write the visible technique, not an artist, studio, or title: OpenAI restricts imitation of living artists' styles, and there are community reports of prompts with IP names being blocked on Jimeng | Multi-source (press); single source |
| Expression | Write what the ears, tail, gaze, muzzle, and fur do, not "blushing" or "his eyes light up" | Author-tested |
| Several images | Number each and state its job: "Image 1 is Gerard's original art; use only the character design and full-body proportions" | Official |
| Marks | Place scars, tattoos, and crystals by body part and the character's own left and right ("above the character's own left eye") | Single source; fewer left-right flips is inference |

The character section is written in full for every image, and copied unchanged every time for the same character [official: reuse the character reference and restate appearance constraints]. Parts not written here are given as "follows Image 1"; do not invent design details for the user [author-tested]. In the shipboard and deep-sea chapters Kael wears a black high-collared New Year outfit (gold bamboo-leaf pattern, red sash), and whether the scarf is present in those chapters follows the reference image [author-tested]:

```text
Kael: black wolf anthro, adult male, a complete wolf head with a long muzzle, black fur over the whole body, upright on two legs. Eyes: amber. The hands are canine paw-hands, four fingers and a thumb. The trait only he has: a red scarf. Clothing, fur colour zones, muzzle length, ear shape, feet, and tail follow Image 1; full-body proportions follow Image 1.
Gerard: white wolf anthro knight, adult male, a complete wolf head with a long muzzle, white fur over the whole body, upright on two legs. Eyes: blue. The hands are canine paw-hands, four fingers and a thumb. Clothing: a blue-and-white cloak; the rest of the clothing follows Image 1. The trait only he has: a scar on his face, its position and shape following Image 1. Fur colour zones, muzzle length, ear shape, feet, and tail follow Image 1; full-body proportions follow Image 1.
```

## 2. Style lines for the three art-style lines

| Line | First sentence | Technique (in every image) | Scene light and colour (only in empty plates, first frames, stills) |
|---|---|---|---|
| Realistic line | Landscape 16:9 | Hyper-realistic cinematic footage: like a frame shot by a film camera; realistic fur layering, clear fur-flow direction, distinct zones of long and short fur; clear texture in cloth, metal, and leather | State the light source position per scene. First person: the camera is "my" eyes |
| Cel-shaded line | Landscape 21:9 | Cel-shaded anime look: flat fur colours, one layer of hard-edged shadow plus a few highlights, clean outlines | Per scene |
| Hand-painted fantasy line | Landscape 21:9 | Hand-painted western fantasy illustration, fine ink line with light watercolour washes | Backgrounds like the painted backgrounds of an animated film; warm golden slanting sun and light shafts, dark foreground, bright midground, pale violet-blue distance |

- The style content is [author-tested]. "Like a frame shot by a film camera" and "clear texture in cloth, metal, and leather" translate "hyper-realistic" into visible traits [inference]; the cel-shading items are the visible traits of cel colouring [multi-source].
- Design sheets, expression sheets, mouth-shape sheets, and single views use only the "Technique" column, with a plain light grey background and even flat light: a styled background carries its light into later images [single source], and scene light is left to empty plates and first frames [inference]. Characters with white fur or silver-white scales (Gerard, Bobo's white mane, Seren) lose their outline on pure white, hence light grey [inference].
- GPT images and Seedance video use the same style line [multi-source]. References for the cel-shaded and hand-painted fantasy lines must be made to the style line: when the references lean realistic and the prompt does not stress the style, the video drifts to realism [official 2.0].
- Fur: for realism write "length + texture + colour + light", as in "longer, fuller fur at the neck; the source is off-screen left and draws a thin bright rim on the fur tips" [single source]. For cel shading add "the fur is drawn as clumped pointed tufts with clear edges" [inference].

## 3. Character design sheet (fixed layout)

Fixed layout: front full body, back full body, and a head close-up in one image, proportions following the original art, never drawn shorter [author-tested]. Changing art-style line changes only the technique in "Style:". If the figure came out short, use a single-point edit from section 9.

| Point | What to do | Source |
|---|---|---|
| Original art as Image 1 | Write "use only the character design and full-body proportions of Image 1; the technique follows Style". A new character with no original art: make one front full-body anchor image first, and make the sheet once it is approved | Author-tested; official (make a reusable character reference first) |
| Preventing a short figure | Fix the layout in words: the two full-body views align at head top and foot sole, complete from ear tips to soles, each about nine tenths of the image height; height, head-to-body ratio, and leg length match Image 1 | Author-tested; the wording is inference |
| Head close-up | Three-quarter view, mouth naturally closed, neutral expression, so it can be cropped straight for Seedance. A long muzzle facing the lens looks too long and hides the eyes | Official 2.0 (neutral expression is best for head shots); multi-source |
| Back view | The whole tail visible, the same length as in the front view | Multi-source (leave room for the tail, check the tail root) |
| Aspect ratio | Landscape 16:9: three views fit, and a cropped single panel is about 0.6 wide-to-high, inside Seedance's 0.4–2.5 | Inference; the range is official |
| No text | No names or annotations by default, so a crop can go straight to Seedance; keep an annotated version separately for people | Official (Seedance does not rely on text in images, and text in references triggers subtitles) |
| Locking the design | Attach the approved image every time, restate the character section, and add "Same character, same facial features, proportions, and color palette as image 1." If it drifts, go back to the approved image and redo; do not keep editing the drifted one | Official (wording adapted from the official example); multi-source |
| Sharpness | A design sheet is information-dense: through the API use 2048×1152 at high. If one panel is soft, redo only that panel | Single source; the size fits the official spec |

```text
Style: landscape 16:9, hyper-realistic cinematic footage: realistic fur layering, clear fur-flow direction, distinct zones of long and short fur, clear texture in cloth and leather. Plain light grey background, even flat light.
Picture / camera: one character design sheet with three views in the same image: the left third is the front full body, the middle third is the back full body, and the right third is a head close-up (the head and a little neck, three-quarter view facing image left, mouth naturally closed, neutral expression, the head about half the image height). The two full-body views share one scale, with head tops and foot soles aligned on the same horizontal lines, complete from ear tips to soles with the whole tail in frame, each about nine tenths of the image height; in the back view the whole tail is visible and the same length as in the front view. Height, head-to-body ratio, and leg length in all three views match Image 1. The only things in the picture are these three views and the light grey background.
Character: Image 1 is Gerard's original art; use only the character design and full-body proportions, with the technique following Style. (Gerard's character section from section 1) Same character, same facial features, proportions, and color palette as image 1.
```

## 4. Expression sheet: ears, tail, muzzle

| Point | What to do | Source |
|---|---|---|
| Panel count | 3–6 expressions, made from the approved design sheet. Small panels go soft: redo only the soft panel, or split into two sheets of three | Multi-source; redoing one panel is single source, splitting is inference |
| Channel by channel | Each panel states ears, tail, muzzle (mouth corners, teeth, bridge of the nose), eyes and gaze, and neck fur. Ears, tail, and brow are the main expressive tools of an anthro character | Multi-source (anthro ref-sheet guides, anthro animation interviews) |
| A held instant | "The tail swung to one side of the body and held", "both ears pressed flat to the head". "Swaying" or "trembling" means nothing in a still | Inference |
| Composition | Each panel runs from head top to mid-thigh, the body turned three-quarter, the tail showing at the side; camera, framing, and light identical across panels | Inference |
| Use in Seedance | The main reference is still the neutral closed-mouth head. When one clip needs a specific expression, crop only that panel and attach it. Too large a change of expression makes the face drift in video | Single source + inference |

The emotion wording is the same set as `kemono-jp-drama.md` 1.6 in the Seedance skill, turned into still states [animal body language and anthro animation interviews: multi-source; the mapping to specific emotions: inference]:

| Emotion | Ears | Tail | Muzzle, eyes, fur |
|---|---|---|---|
| Calm (baseline panel) | Naturally upright | Relaxed, hanging | Muzzle closed, gaze level |
| Alert | Upright, both turned to the sound | Tip held in mid-air | Pupils wide, gaze toward the sound |
| Holding back anger | Pressed flat back against the head | Rigid | Bridge of the nose wrinkled, upper lip slightly lifted to show canine tips, fur raised along neck and back |
| Low | Drooping to the sides | Hanging low against the legs | Gaze on the ground |
| At ease | Relaxed, opening slightly outward | Hanging loosely to one side | Eyes half closed, muzzle relaxed |
| Awkward | One turned back | Tip raised | Gaze averted, one hand at the back of the neck |

- Different species have different channels [inference; the character facts are author-tested]: for felines (Bobo, Magnus, Zanni, Varek, Kern.V) a fast tail lash mostly means irritation; Seren uses his pink ear fins; Kinovi uses his feather mantle, and the mantle flaring is his heartbeat; Rolf's face is a rigid faceplate, so expression goes to head angle, shoulders, and hands; Seris, the ichthyosaur, the orca, and the equines follow their reference images.
- Each character's own acting key [author-tested] and how to use it [inference]: Kael "gives himself away with his ears first", so add a "won't admit it" panel (muzzle shut tight, ears lowered all the same); for Gerard "all the charm is in the ears and tail", so his sheet concentrates the change there and keeps the muzzle composed; Bobo "freezes for half a beat when someone looks after him", so add a "frozen" panel (both ears bolt upright, one hand stopped in mid-air).

```text
Style: landscape 16:9, hyper-realistic cinematic footage: realistic fur layering, clear fur-flow direction. Plain light grey background, even flat light.
Picture / camera: one expression sheet, two rows of three, six panels in all, with thin white gutters between panels. Each panel is a close shot of the same character from head top to mid-thigh, the body turned three-quarter toward image left, the tail showing at one side of the body; camera, framing, and light are identical in all six, and only the state of the ears, tail, muzzle, eyes, and neck fur changes. The only things in the picture are the six panels of the character and the light grey background. The six panels, from top left to bottom right:
1 Calm: both ears naturally upright, tail relaxed and hanging, muzzle closed, gaze level and ahead.
2 Alert: both ears upright and turned together toward image left, tail tip held in mid-air, pupils wide.
3 Holding back anger: both ears pressed flat back against the head, tail rigid, bridge of the nose wrinkled, upper lip slightly lifted to show the canine tips, fur raised along the neck and back.
4 Won't admit it: muzzle shut tight, mouth corners down, gaze turned toward image right, yet both ears lowered to the sides.
5 Low: both ears drooping to the sides, tail hanging low against the legs, gaze on the ground.
6 At ease: both ears relaxed outward, tail hanging loosely to one side, eyes half closed, muzzle relaxed.
Character: Image 1 is the approved Kael design sheet. (Kael's character section from section 1) All six panels are the same character, with muzzle length, ear shape, fur colour zones, and clothing matching Image 1.
```

## 5. Mouth-shape sheet: a lip-sync reference for Japanese

A mouth-shape sheet is not a "mouth dictionary" fed to Seedance: Seedance fits mouth shapes to whatever mouth is visible according to the line [inference]. Its use is to settle how this character looks with his mouth open (lip line, jaw opening, which teeth show, the colour of tongue and mouth), to check finished clips against, and to crop one panel as a reference when needed.

| Panel | Corresponds to | Muzzle | Source |
|---|---|---|---|
| 1 Closed | Not speaking, end of a sentence | Muzzle naturally closed, the lip line one continuous line | The three basic mouths of limited animation: open, half open, closed [single source] |
| 2 Lips together | The ma row; ba and pa rows | Upper and lower lips pressed firmly together | Ma row [single source: interview with the CG director of an anthro 3DCG anime]; ba and pa rows [inference] |
| 3 Half open | i, e, and the transitions between most sounds | Jaw slightly open, showing the tips of the upper and lower canines | The three mouths [single source]; the vowel mapping [inference] |
| 4 Open | a | Jaw open, showing upper and lower canines and the front of the tongue | As above |
| 5 Rounded | u, o | Mouth corners drawn forward, the opening small and round | [inference]; most viseme schemes are designed for human mouths and read differently on a long muzzle [single source] |
| 6 Low voice | Muttering, talking to himself | Muzzle open only a slit | [single source: the same interview] |

- All six panels are the same head: three-quarter view, with head position, eyes, and ears identical, and only muzzle and jaw changing [inference]. A short wide muzzle suits big openings; mouth shapes on a long muzzle are drawn with restraint [single source]. Write the teeth as this species' teeth: "the teeth that show are a wolf's canines"; one review saw a non-human character's teeth jump between human and animal teeth [single source]. Tongue and mouth colour follow Image 1.
- Feeding Seedance: the main reference is panel 1 or the head close-up from the design sheet. An open-mouthed or snarling image as the main reference makes speaking mouth shapes unstable [single source]. To test whether panel 4 steadies the teeth, attach it only to a 4–8 s single-character lip-sync test shot and write "use only the look of the teeth and mouth when open" [inference, untested].
- A beak (Kinovi, if he has one) or a faceplate (Rolf) cannot form closed-lip sounds, so make no mouth-shape sheet and put key lines off-screen or on the character's back [inference].

```text
Style: landscape 16:9, hyper-realistic cinematic footage: realistic fur layering, with the short fur around the muzzle and the lip line clear. Plain light grey background, even flat light.
Picture / camera: one mouth-shape sheet, two rows of three, six panels in all, with thin white gutters between panels. Each panel is a head close-up of the same character, from head top to just below the chin, three-quarter view facing image left; head position, angle, eyes, and both ears are exactly the same in all six, and only the opening of muzzle and jaw changes. The only things in the picture are the six heads and the light grey background. The six panels, from top left to bottom right:
1 Closed: muzzle naturally closed, the lip line one continuous line.
2 Lips together: upper and lower lips pressed firmly together.
3 Half open: jaw slightly open, showing the tips of the upper and lower canines.
4 Open: jaw open, showing the upper and lower canines and the front of the tongue.
5 Rounded: mouth corners drawn forward, the opening small and round.
6 Low voice: muzzle open only a slit.
Character: Image 1 is the approved Gerard design sheet. (Gerard's character section from section 1) The teeth that show are a wolf's canines, and tongue and mouth colour follow Image 1. All six panels are the same character, matching Image 1.
```

## 6. Single-view references and empty camera plates for Seedance

### 6.1 Single-view references

| Requirement | What to do | Source |
|---|---|---|
| Split into single images | Per character: one head, one full-body front, and a separate back view if needed | Official (several views in one image are easily read as several subjects; split multiple views into multiple images) |
| Head | Only the head and a little neck, neutral expression, mouth naturally closed, three-quarter view for a long muzzle | Official 2.0 (little shoulder and neck in head shots); multi-source |
| Facing | Make it facing the way the shot faces: if he looks frame right in the video, the reference faces right too. If both are needed, make one of each with an edit, "turn only the head toward image right". Mirroring moves scars, tattoos, and crystals to the other side | Author-tested (do not attach references facing the opposite way); inference |
| Clean | Plain background, flat light, this one character only, no text on the image | Official |
| Aspect ratio | 0.4–2.5; beyond it Pippit returns error 99999. Leave extra background left and right when cropping from a design sheet. ChatGPT can output 3:1 images, which need cropping first | Official; author-tested; single source (press) |
| Size | 300–6000 pixels per side, under 30 MB, and no larger than the video output resolution (1280×720 for 720P landscape). Fur is a dense texture, and an oversized image can produce a fingerprint-like texture | Official; test run; the point about fur is inference |
| Style, version | The same style line as the video. Attach only current versions (keep your own list of "references currently in use") and leave out old, wrong images | Official 2.0; author-tested |
| Attach every time | Every character appearing in a clip gets his own images in that clip, uploaded in order of first appearance, with names bound in the prompt | Author-tested; official |
| Count | 2–3 images per character, 4–6 for a two-character scene | Inference (Xiaoyunque handbook: 1–8 per subject is steady) |
| Rejected | A copyright-review rejection is usually triggered by one full-body reference; remove that one and retry | Author-tested |

```text
Following Image 1 (the approved design sheet), change only the composition: one portrait 2:3 full-body image of a single character, standing front on, complete from ear tips to soles with the whole tail in frame, with background left on both sides. Plain light grey background, even flat light, this one character only in the picture. Fur colours, muzzle, hands, feet, clothing, and full-body proportions match the front full-body view of Image 1.
Following Image 1, change only the composition: one 1:1 head close-up showing the head and a little neck, three-quarter view facing image right, mouth naturally closed, neutral expression. Plain light grey background, even flat light, this one head only in the picture. Fur colours, muzzle length, ear shape, eye colour, and the positions of marks such as scars and tattoos match Image 1.
```

### 6.2 Empty camera plates

For a hard camera position, first make an empty plate from that position and upload it as the scene reference [author-tested].

| Point | What to do | Source |
|---|---|---|
| Aspect and style | The same as that clip (16:9 or 21:9), with the full style line including scene light | Inference |
| A specific camera position | State height, facing, tilt, and how much of the frame the foreground takes: "the camera sits on the ground, about a fist's height above it, tilted slightly up" | Author-tested (ground-level low cameras are a regular choice); the wording is inference |
| Light | The same sentence as "Light:" in the video prompt, with the source position | Author-tested |
| Scene only | Write "the only things in the picture are ___"; in Seedance a scene image supplies only space, materials, and light | Official sd25-pe |
| Axis for dialogue scenes | Draw the fixed objects from "Scene layout:" in their places (table, window, door), with the camera on the side where the lens will be | Official (positions anchored to fixed objects); inference |
| Binding | In Seedance write "@ImageN (___ empty plate): use only the height and facing of this camera position and ___" | Author-tested |

Realistic line, ground-level empty plate (the scene is an example and pairs with template 4 in `templates-kemono.md` of the Seedance skill):

```text
Style: landscape 16:9, hyper-realistic cinematic footage: like a frame shot by a film camera, with the texture of the flagstones and the fine dust in their gaps clear.
Picture / camera: an empty plate. The camera sits on the flagstone floor of a corridor, about a fist's height above it, tilted slightly up, facing down the corridor; the gaps between the foreground flagstones take the lower third of the image, and the open archway at the corridor's end sits at centre, slightly high. A row of tall windows runs along image left, and cold white morning light slants down from off-screen upper left, laying window-shaped patches of light on the flagstones. The only things in the picture are the corridor, the flagstones, the tall windows, and the archway.
```

Hand-painted fantasy line, courtyard empty plate (the scene is an example and demonstrates "fixed quantities" and "matte flat colour, little detail"; a low-detail plate also has less dense texture such as grass and leaves, which the official guide says tends to produce fingerprint-like texture [official + inference]):

```text
Style: landscape 21:9, hand-painted western fantasy illustration, fine ink line with light watercolour washes, matte flat colour, little detail; the background like a painted background from an animated film. Warm golden slanting sun and light shafts, dark foreground, bright midground, pale violet-blue distance; the picture is built from four large colour masses: the dark of the near flagstones, the sunlit open ground in the midground, two light shafts, and the pale violet-blue city wall in the distance.
Picture / camera: an empty plate, eye level, the camera at a person's waist height, facing the flagstone ground at the centre of the courtyard; a wooden post at image left and a wooden door at image right; two light shafts slant into the courtyard from off-screen upper left and fall on the centre of the open ground. The only things in the picture are the courtyard, the wooden post, the wooden door, the flagstones, and the light shafts.
```

## 7. First frames, last frames, and keyframes

| Point | What to do | Source |
|---|---|---|
| Aspect ratio | The same as the video. In first-frame mode the output ratio follows the first frame; if first and last frames differ, the last frame is stretched | Official |
| First-frame content | The picture at the video's first second, with the characters before the action begins, the action happening only after this frame: mouth closed for a speaking shot, wound-up and ready for a fight | Inference |
| Last frame | Edit the first frame in the same conversation ("change only ___ to ___; keep everything else as it is") so subject and layout stay put. Only one-take or single-scene clips need one | Single source; official (single-point edits); inference |
| Keyframes | One beat each: full body in frame, both feet visible, which hand holds the weapon stated; the composition leaves room for movement and orbiting | Official; leaving room is single source |
| Seedance wording | Keyframes are uploaded as ordinary reference images. A fixed first frame gets its own "@ImageN is the first frame."; for several, "Use @Image1 to @ImageN in order as keyframes" goes in the first sentence | Official |
| Character references | Besides the first frame, each character still gets his own single views; the previous clip's last frame is only for fixing positions | Author-tested; official sd25-pe |
| Background figures | Give each a species: "the dockhands are two bear anthros". In the realistic line "I" am the only human | Author-tested |
| Grids | Use when only rough structure is needed: 15 panels or fewer, read left to right, clean line art, no text on the image. This runs opposite to right-to-left Japanese comics | Official; the direction clash is inference |
| Jimeng subject library | Not available in first/last frame and smart multi-frame modes | Single source |

First-frame example, leading into shot 1 of section 5 in `kemono-jp-drama.md` of the Seedance skill (that example is written in third person; when shooting the realistic line in first person, change the camera to "my" eyes). Images 1 and 2 are the two characters' single views, and Image 3 is a room plate made as in 6.2:

```text
Style: landscape 16:9, hyper-realistic cinematic footage: realistic fur layering, clear fur-flow direction, distinct zones of long and short fur; clear texture in the wooden table, the clay cup, and the cloth.
Picture / camera: the picture at the video's first second. Two-shot, medium, eye level, the camera at the chest height of a seated person; room layout and camera position follow Image 3. Kael sits at the left end of a small wooden table with the window behind him, looking toward image right; Gerard sits at the right end with the door behind him, looking toward image left. A steaming cup rests on the table on Kael's side, one of Kael's hands on it; Gerard sits bolt upright, his gaze on the cup. Both have their mouths closed. The key light is an oil lamp directly above the table, warm yellow, shining down; cold blue night light comes through the window behind Kael and draws a thin bright rim on his ears and shoulders.
Character: the only two characters in the image are Kael and Gerard, one of each. Image 1 is Kael and Image 2 is Gerard; use only their appearance. Image 3 is the room plate; use only the room layout, furniture positions, and camera position.
(Kael's and Gerard's character sections from section 1)
```

Binding in Seedance (the official first-frame sentence, made positive; numbering follows Seedance's upload order and is unrelated to the GPT image numbers above; Gerard's two images are written the same way):

```text
@Image1 is the first frame.
This first frame defines both characters' positions and poses, the cup's position, the room layout, and the camera direction at the start of the video.
@Image2 (Kael, head): use only Kael's black head fur, amber eyes, ear shape, and muzzle length; the first-frame composition follows @Image1.
@Image3 (Kael, full body): use only Kael's clothing, red scarf, and full-body proportions; the first-frame composition follows @Image1.
```

## 8. Japanese text in images: balloons, vertical text, ruby, typefaces, hand-drawn sound effects

- Expectations: Japanese improved clearly from GPT Image 2 [multi-source, press relaying OpenAI]. On vertical text OpenAI itself says there is still work to do [single source, interview]. Small text and exact text placement are officially listed limitations [official]. No public evidence was found that 2.5 fixed vertical text. In a local test run the ChatGPT web page rendered three passages of Chinese on a 1024×1536 poster with every character correct [test run; Chinese, not Japanese].
- Text to be drawn into the image is given exactly in 「」 or quotation marks [official: put requested text in quotes]. {} is Seedance's dialogue symbol and is used only in video prompts.

| Item | Wording | Source |
|---|---|---|
| Exact text | Each passage exactly, in 「」; state position, direction, typeface, colour, and number of occurrences; write "the only text in the picture is the following N items, each appearing once"; proofread character by character afterward | Official |
| Vertical text (縦書き) | State "縦書き" and give the text column by column from right to left: right column 「…」, left column 「…」. One or two columns per balloon, large type. No more than about 11 full-width characters per column | Multi-source; 11 characters is borrowed from Japanese subtitle standards, and the borrowing is inference |
| Reading order | "Japanese manga, read from top right to bottom left", with each panel's position marked: コマ1 (top right, large) | Multi-source |
| Typeface | Describe it: Mincho-like (thin serif), bold Gothic, brush lettering, thick marker handwriting. For dialogue write "manga typesetting style: kanji in bold Gothic, kana in a bold Mincho-like face (antique style, アンチック体)". Named fonts cannot be reproduced | Multi-source; whether アンチック体 is understood is inference |
| Hand-drawn sound effects (描き文字) | A sentence of its own: one or two katakana words, with stroke, angle, colour, position, and count | Inference |
| Ruby (ルビ) | Add in post where possible. To generate it, annotate only one or two words, to the right of the kanji in vertical text and above in horizontal text, at an enlarged size | Inference; positions follow Japanese subtitle standards |
| Glyph forms | Write "kanji in Japanese glyph forms" and name characters that differ between Chinese and Japanese forms, such as 気、戦、剣、話、読; check these first afterward | Inference |
| Quality | Do not use low for a lot of text: in one test, Japanese in balloons was badly garbled at low, mostly fine at medium, and cleaner at high. Through the API start at high. For several consecutive pages in ChatGPT use Thinking mode (paid tiers, up to 8 images at once with the character kept consistent) | Single source; multi-source (press) |
| Changing text | One place at a time: circle or comment on that region and write "change only the balloon in コマ2 to vertical 「…」; keep everything else as it is". Or make a version with blank balloons and letter it in post | Official; multi-source |
| Feeding Seedance | Make a separate picture-only version: "remove all balloons, text, and hand-drawn sound effects; keep everything else as it is". A reference with text carries the text into the video as subtitles or garble | Official |
| A Japanese sign needed in the video | Use GPT to make an image containing only that text and give it to Seedance as a text reference | Official (Seedance: make text that must display accurately into an image) |

Example: a right-opening page of three panels. 「……これは命令だ。」 and 「承知した。」 come from the sample character setups [author-tested]; the story is an example:

```text
Style: portrait 2:3, a Japanese black-and-white manga page: black ink line, screentone shading, fine hatching in the backgrounds.
Picture / camera: a right-opening page read from top right to bottom left, three panels in all, with white gutters between them; the panels contain only artwork, balloons, and the specified hand-drawn sound effect.
コマ1 (top right, large): Kael pushes a cup in front of Gerard, his gaze turned to the window, both ears lowered to the sides.
コマ2 (top left, small): a close shot of Gerard, sitting bolt upright, both ears upright and forward.
コマ3 (bottom tier, wide): Gerard rises to his feet, torso upright, the hem of his cloak lifting.
Text: the only text in the picture is the following three items, each appearing once; kanji in Japanese glyph forms, large type, clear strokes:
1. On the right of コマ1, one white oval balloon with a thin black outline, vertical text (縦書き) in two columns: right column 「……これは」, left column 「命令だ。」
2. On the left of コマ2, one white oval balloon, vertical text in one column: 「承知した。」
3. At the upper right of コマ3, one hand-drawn sound effect 「ザッ」, katakana, thick brush strokes, set at an angle, white with a black edge.
Dialogue typeface: manga typesetting style, kanji in bold Gothic, kana in a bold Mincho-like face.
Character: the only two characters on the page are Kael and Gerard; Image 1 is Kael and Image 2 is Gerard. (The two character sections from section 1)
```

Known failures:

| Failure | Fix | Source |
|---|---|---|
| Vertical text comes out horizontal | Add "吹き出しのセリフは縦書き" and give the text column by column | Multi-source |
| Panels laid out from top left | Change only the layout in the same conversation; if still wrong, generate panel by panel and assemble | Multi-source |
| Panel numbers such as "1⃣" appear | Write "the panels contain only artwork, balloons, and the specified hand-drawn sound effect"; if they persist, circle and delete | Single source; the positive wording is inference |
| Garbled or jagged text in balloons | Raise the quality and redo block by block | Single source |
| Text too small | Write "large type" and reduce characters and columns per balloon | Single source |
| Kanji in Simplified Chinese forms | Name Japanese glyph forms and check character by character | Inference |
| Characters or other panels change when text is edited | One place at a time, restating the keep-list each round; for pixel-identical results composite the edited part back onto the original | Official |

## 9. ChatGPT practice and single-point edits

| Situation | What to do | Source |
|---|---|---|
| A bare-chested character is occasionally stopped by moderation | Rerun the same prompt once | Author-tested |
| A more alluring outfit is wanted | Write the specific cut, material, and way it is worn (e.g. "the shirt open to the chest"), following the original art. There are community reports of summary words like "sexy" being blocked on Jimeng; no data for GPT | Author-tested; single source; inference |
| The web page silently uses a weaker model | Start a new chat and rerun | Author-tested |
| You cannot tell whether it was downgraded | In the test the page did not show a model name and reasoning effort read Extra High; if results get clearly worse, start a new chat | Test run; inference |
| After starting a new chat | Upload the approved design sheet again and paste the character section unchanged. References like "as above" or "same as before" do not cross chats | Official (rewrite key constraints every round); inference |
| Model and quality | Flare/Sunburst and quality cannot be chosen in ChatGPT (a community claim, unconfirmed). Through the API, design sheets, expression sheets, mouth-shape sheets, and comic pages with text use Sunburst at high; single views can try Flare | Single source; the official selection strategy; the quality level is inference |
| A set in one go | Thinking mode makes up to 8 images of the same character at once (paid tiers) | Multi-source (press) |
| Local edits | In 2.5 you can circle or comment on the image to change only that place; one place at a time; if it drifts, go back to the approved image and redo | Official; multi-source |
| Complex staging | In 2.5 a stick-figure sketch with @Sketch can serve as a composition reference | Multi-source (press); using it for staging is inference |

Single-point edit sentences for common anthro failures. The pattern is OpenAI's "change one thing, keep the rest" [official]. Of the failure types, human-with-ears and four-legged are [multi-source], teeth is [single source], and the rest are [inference]:

| Failure | Edit sentence (replace per character) |
|---|---|
| Drawn as a human with animal ears | Change only the character's head to a complete wolf head with a long muzzle, the face covered in fur; keep clothing, pose, composition, and light as they are. |
| Crouched, on all fours | Change only the pose to standing upright on two legs, torso upright; keep everything else as it is. |
| Wrong finger count | Change only both hands to canine paw-hands, four fingers and a thumb on each; keep everything else as it is. |
| Tail missing | Add only a tail extending from the lower back, its length and colour following Image 1; keep everything else as it is. |
| Scar or tattoo on the wrong side | Move only the scar back to its position in Image 1; keep everything else as it is. |
| Drawn short | Change only the height, head-to-body ratio, and leg length of the full-body views back to the proportions of Image 1; keep everything else as it is. |
| Looks too young | Change only the head-to-body ratio, muzzle length, and eye size back to the proportions of Image 1; keep everything else as it is. |
| Teeth look human | Change only the teeth that show to a wolf's canines; keep everything else as it is. |
| Extra text appears | Remove only all text from the picture; keep everything else as it is. |

## 10. Check before delivering

- [ ] Three sections, "Style:", "Picture / camera:", "Character:", plus "Text:" when there is text; the first sentence states the aspect ratio
- [ ] The style line matches the art-style line; design, expression, and mouth-shape sheets and single views use only the technique, on plain light grey with flat light
- [ ] Each character: species anatomy + adult male + the appearance in the setup + the trait only he has; anything the setup leaves out is "follows Image 1"; no build adjectives
- [ ] Fixed quantities: three views, six panels, N text items
- [ ] The whole prompt is positive wording (scan for "no", "not", "without", "avoid", "never")
- [ ] Design sheet: front full body + back full body + head close-up, proportions following the original art
- [ ] Images for Seedance: single, plain background, no text, facing matches the shot, aspect 0.4–2.5, no larger than the video resolution, same style as the video
- [ ] First frame: same aspect ratio, before the action begins, the speaker's mouth closed
- [ ] Japanese: exact text in 「」 with direction, position, typeface, and count; proofread character by character afterward; a separate picture-only version for Seedance
- [ ] The reply includes: size and quality for the API route, assumptions, and the one single-point edit most likely to be needed

## 11. Sources

Research date 2026-10-28. [author-tested] the author's production notes and [test run] the sample-run notes are local files compiled that day and have no URL.

[official]
- OpenAI image prompting guide (reusable character references, restating appearance constraints, "Same facial features, proportions, and color palette", changing one thing, quoting text with position and typeface, asking for no extra text and proofreading, one beat per comic panel, comparing medium and high for small text): https://developers.openai.com/api/docs/guides/image-prompting ; image generation guide (limits of text placement and sharpness, and of cross-image consistency): https://developers.openai.com/api/docs/guides/image-generation ; ChatGPT image docs (editing a selected region): https://learn.chatgpt.com/docs/image-generation
- Volcano Ark, Seedance 2.5 prompt guide (splitting multiple views into separate images, uploading in order of first appearance, keyframes in the first sentence, first and last frames sharing a ratio, fingerprint-like texture, grids of 15 panels or fewer, making accurately displayed text into an image): https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide ; Seedance 2.5 tutorial (reference aspect ratio 0.4–2.5, 300–6000 pixels per side, under 30 MB): https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Volcano Ark, Seedance 2.0 prompt guide (head shot plus full-body shot, multiple views read as multiple subjects, realistic references making an animated style drift, removing text from references): https://docs.volcengine.com/docs/82379/2222480 ; Xiaoyunque, Seedance 2.5 official handbook (1–8 images per subject, little text on grids): https://www.xiaoyunque.com/tutorials/seedance-2-5
- sd25-pe skill 0.1.1 (the "@ImageN is the first frame." sentence, keyframes input as ordinary references, scene images supplying only space, material, and light, positions anchored to fixed objects, the first frame locking the aspect ratio): https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip

[multi-source]
- Anthro anatomy and degrees of "kemono" (ear words pulling toward a human face): https://dic.pixiv.net/a/ケモノ ; https://techhowto.blog/posts/stablediffusion-prompt-furry/ ; https://www.ocmaker.ai/blog/how-to-create-anthropomorphic-animals ; tails and marks: https://spicyapi.ai/blog/furry-ai-art-models-and-prompts ; ref sheets and expression panel counts, ears and tail as the main expressive tools, redoing one panel: https://myfurryrefsheet.com/furry-refsheet/ ; https://myfurryrefsheet.com/how-to-draw-furries-anatomy-guide/ ; https://image-2.net/blog/gpt-image-2-character-reference-sheet/
- Anthro animation acting (ears react first, tails, the difficulty of a long muzzle face-on; closed lips on the ma row and the small muttering mouth are single source): https://animeanime.jp/article/2019/10/30/49323_2.html ; https://www.scrmbl.com/post/studio-orange-beastars-interview ; animal body language: https://en.wikipedia.org/wiki/Cat_body_language ; https://en.wikipedia.org/wiki/Body_language_of_dogs
- Three-quarter view for speaking shots: https://www.cutout.pro/learn/blog-seedance-2-0-audio-guide/ ; one style line on both sides, the last frame edited from the first, large expression changes drifting: https://lemgen.org/blog/gpt-image-character-sheet-before-seedance ; https://github.com/corneliusbraithwaite9/gpt-image-2-seedance-2-5-workflow
- Cel colouring: https://realsound.jp/movie/2020/12/post-677025_4.html ; https://www.mhlw.go.jp/content/11901000/001152417.pdf ; https://zh.moegirl.org.cn/%E8%B5%9B%E7%92%90%E7%92%90
- Japanese rendering, vertical text, and right-to-left reading: https://engadget.com/ai/chatgpt-images-20-is-better-at-rendering-non-latin-text-190000153.html ; https://morphic.com/resources/how-to/chatgpt-images-2.0-guide ; https://www.ipentec.com/document/ai-image/image-generation-create-comic-page-with-panel-layout-with-gpt-image-2 ; https://youmind.com/ar/prompts/manga-cafe-ai-dialogue-34485 ; https://note.com/tata_15/n/ne39d4e665f8c ; https://note.com/yoya48/n/n2c69a9f5bbe1 ; describing typefaces: https://note.com/creative_edge/n/ne18280b7618d ; https://note.com/fond_harte4678/n/n0613203d8757 ; https://news.mynavi.jp/article/font-history-48/
- ChatGPT Images 2.0 / 2.5 features (Thinking up to 8 images, 3:1 to 1:3, Sketch, comment-style edits): https://the-decoder.com/openais-chatgpt-images-2-0-thinks-before-it-generates-adding-reasoning-and-web-search-to-image-creation/ ; https://k-tai.watch.impress.co.jp/docs/news/2103621.html ; https://community.openai.com/t/introducing-gpt-images-2-5-in-the-api-and-chatgpt/1395897 ; https://datanorth.ai/news/openai-launches-chatgpt-images-2-5 ; https://9to5mac.com/2026/09/08/openai-releases-chatgpt-images-2-5-with-sharper-details-and-more-precise-editing/
- Restrictions on living artists' styles (press): https://techcrunch.com/2025/03/28/openai-peels-back-chatgpts-safeguards-around-image-creation/ ; https://www.infoq.com/news/2025/04/gpt-4o-images

[single source]
- Vertical text "still has issues" (interview): https://www.watch.impress.co.jp/docs/topic/2105435.html ; the three mouths of limited animation: https://news.mynavi.jp/techplus/article/kurieita-22/ ; viseme schemes designed for human mouths: https://wiki.vrchat.com/wiki/Visemes ; restrained mouth shapes on long muzzles: https://fursonafy.com/how-to-draw-furry-poses-and-proportions-a-beginners-guide/
- Open-mouthed or snarling references destabilising mouth shapes: https://www.seedance.tv/blog/seedance-2-5-lip-sync-issues ; teeth jumping between human and animal: https://www.aitoolssme.com/blogs/seedance-2-5 ; styled backgrounds contaminating later images: https://www.atlabs.ai/blog/gpt-image-2.5-prompt-guide-2026-flare-vs-sunburst-quality-steps-and-consistent-characters ; fur as "length + texture + colour + light": https://www.flowpixai.com/prompt-engineering/pet-ai-painting-description.html
- Mode limits of the Jimeng subject library: https://zhuanlan.zhihu.com/p/2073815177141674951 ; words like "sexy" and prompts with IP names blocked on Jimeng: https://www.tahou.com/article/212586151215904773
- Japanese subtitle standards (characters per line in vertical text, ruby position): https://partnerhelp.netflixstudios.com/hc/en-us/articles/215767517-Japanese-Timed-Text-Style-Guide-v4-0 ; the jarring look of mixed Chinese and Japanese glyph forms: https://gigazine.net/news/20211029-your-code-displays-japanese-wrong ; sound-effect words short, large, with space around them: https://zenn.dev/satofun/articles/8fa0283ccd4e74

[inference] Every item tagged [inference] in the text states its basis in the same sentence or row.
