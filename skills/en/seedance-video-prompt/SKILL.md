---
name: seedance-video-prompt
description: Use when the user asks to write, rewrite, or debug a video prompt for ByteDance Seedance 2.5 (Dreamina, CapCut, Jimeng, Doubao, Pippit, Volcengine Ark / BytePlus ModelArk doubao-seedance-2-5; also works for Seedance 2.0). Strongest on western-fantasy and anthro (furry / kemono) characters in a realistic CG look, with cel-shaded and hand-painted styles also covered — dialogue scenes with Japanese lines, muzzle lip-sync, ear and tail acting, fights, and close-ups. Covers 4–30 second clips with a focus on 30 seconds — second-by-second shot lists, one-take or multi-shot structure, camera moves, @image/@video/@audio reference roles, character consistency, sound, first/last frames, keyframes, storyboard grids, video editing and extension — and general subjects such as ads, short drama, and music-synced promos. Trigger phrases include "Seedance prompt", "Dreamina video prompt", "turn this script or storyboard into a video prompt", "30 second AI video".
summary: Turn an idea, script, storyboard, or reference set into a submit-ready Seedance 2.5 video prompt, with a tested method for realistic-CG anthro and western-fantasy scenes.
version: 2.1.0
tags: [seedance, video-generation, prompt-engineering, storyboard, furry, kemono, fantasy]
---

# Seedance 2.5 video prompts (4–30 seconds, focus on 30)

Seedance 2.5 (released late July 2026) generates 4–30 second videos with sound in a single run. It takes up to 50 multimodal references and supports integer-second timestamps, video editing, and video extension. Thirty seconds is twice the 2.0 limit of 15, and the hard part changes with it: the question is no longer "does the frame look good" but "what is each stretch of these 30 seconds doing". If you describe one image and stretch it to 30 seconds, the model repeats actions, drifts in the middle, and cuts at random. The core method is therefore: **a time budget per segment + one change per segment + a visible end state written for every segment**.

The anthro parts of this skill come from the author's own production of 30 second shorts with adult male anthro characters who speak Japanese: lots of dialogue, some fights, heavy use of camera moves and close-ups. The characters in the examples (Kael, Gerard and others) and the three example lines (realistic, cel-shaded, hand-painted fantasy) are demonstrations only. Swap in the user's own characters and style. For general subjects, skip the anthro parts.

Prompts in this edition are written in English, with Japanese dialogue kept in Japanese. A Chinese edition of the same skill, with Chinese prompt templates for Jimeng, lives in the source repository.

## What to deliver

Deliver in this order by default. When the user says "prompt only", give items 3 and 4 only.

1. **Plan in one sentence**: the core event, the structure (one take in N segments / N shots), and key assumptions. Skip it when the user already supplied a complete shot list.
2. **Asset list**: which references to upload, numbered in order of each character's first appearance, and what each one is responsible for. With no references, write "Text-to-video only, ready to use". Cite only assets the user really has. Recommend leaving out any asset this clip does not need.
3. **Full prompt**: in one `text` code block, containing only what can be submitted as is: picture, camera, sound, dialogue, and time ranges. Aspect ratio, total duration, resolution, frame rate, and the audio switch stay out of the prompt [official sd25-pe].
4. **Platform settings**: aspect ratio, duration, resolution, audio on or off, written outside the code block. Default to a 480p draft first and 720p once it looks right. On Jimeng the page defaults to draft mode, so switch manually before a final render [author-tested; test run]. Edit, first/last frame, and extension tasks lock some parameters automatically. When the user's request conflicts with a lock, add one "Parameter note:" line saying what to change before submitting [official sd25-pe].
5. **Dialogue draft** (only when the user gave no dialogue text): 1–2 suggested Japanese lines in the character's voice, with the meaning and the mora count, headed "Draft, not in the prompt". Put them inside {} only after the user confirms.
6. **Adjustable items** (optional, at most 3): what the user is most likely to want changed, such as the final image, the framing of one shot, or whether to add music.

## Workflow

### 0. Read the user's creator profile first

Before writing, read `references/creator-profile.md` if it exists. It is the user's own optional profile, filled in from `references/creator-profile.template.md`: each series' aspect ratio, style line, point of view and dialogue language; each character's identifying trait, voice and speech habits; the fixed section order and favourite shots; and past failures. With no profile, write from what the user says in the conversation. For any appearance detail the profile does not record, write "as in @Image N" and never invent design details for the user. Then read by task:

- Anthro dialogue scenes: `references/kemono-jp-drama.md`
- Fights, close-ups, high-impact camera moves: `references/combat-closeups.md`
- How many shots in 30 seconds, and how to get an anime / TV drama / film feel: `references/shot-grammar.md`
- Starting from a finished example: `references/templates-kemono.md` (six 30 second templates in the fixed section order)

### 1. Identify the entry point

An idea only / character, product, or scene images / a reference video (confirm first whether the user wants its action, camera work, rhythm, or transitions; do not copy everything by default) / a script (keep story, dialogue, and ending; fill in visuals and timing) / a precise shot list (keep seconds, order, and asset roles; fill gaps and point out conflicts) / editing an existing video / extending an existing video / first and last frames or keyframes. Entry points can combine.

### 2. Ask only what changes the result

One round at most, three questions at most: What event do you want to show, and what image does it end on? How long, landscape or portrait, what style? Which assets do you have, and which must be kept?

When the user's description already covers most of these, do not ask. Write the prompt, list the assumptions you made in the plan, and invite corrections. Stop to ask only when the event, the ending, or the asset roles are completely unclear.

When the user says "just write it", or only a little is missing, use defaults and flag them in the plan:
- **Users with a profile**: use the series defaults in `references/creator-profile.md`; aspect ratio and duration go in platform settings only. The three example lines in this skill are: realistic line, 16:9, hyper-real cinematic picture, first person; cel-shaded line, 21:9, 3D cel shading; hand-painted fantasy line, 21:9, hand-painted western fantasy illustration; each clip 30 seconds. If the point of view is not recorded, ask first. If the user says "just write it", use third person and mark it as an assumption.
- **Users without a profile**: with no duration given and simple content, suggest 10–15 seconds; 16:9; write the style as visible traits, such as "realistic cinematic look: natural light, shallow depth of field, restrained colour".
- Sound defaults to "The only sounds are ambience, action sounds, and dialogue". Picture defaults to "The picture is clean footage".

No music by default. Music the model invents is hard to remove and tends to fight the edit; scoring in post is easier to control. If the user wants music, write genre, tempo, and start and end seconds in (), for example "(gentle solo piano, about 70 BPM, fading out by second 25)", and change the sound sentence so it includes music and stays consistent.

### 3. Design before writing

1. **One-sentence story**: one main character + one main place + one clear goal + one main turn + one final image. That is as much story as 30 seconds can tell well. More characters, places, and events make each of them blurry.
2. **Choose the structure**:
   - **One take** (continuous long shot): split into 3–4 time segments and write "One take: the camera moves continuously from the first second to the last; the whole clip is a single continuous shot". Describe by time range, not "Shot 1 / Shot 2", which reads as a request to cut [single source]. Segment boundaries are where a one-take most often gets cut. In a 2026-10-28 test on Jimeng, a 30 second breakfast-shop one-take had its only hard cut at 7.38 s, right on the boundary between "0–7s" and "7–15s", jumping from outside the door to inside the shop [test run, once; that prompt still carried parameters and negative constraints]. So from the second segment on, open each segment with "The camera keeps moving and…", and when crossing spaces, write the camera's path, for example "The camera keeps moving, follows the cook across the threshold into the shop, and swings from behind him to his front right". When continuity matters a lot, cut down to 3 segments, or split into two clips joined by extension. This wording has not been re-tested, so check the segment boundaries in the draft.
   - **Multi-shot edit**: 5–9 shots of 2–6 seconds each, written "Shot N (a–b s)", with "hard cut" between shots. This skill's default is five to nine shots timed by the second [author-tested]. The official 30 second example has 9 shots lasting 3/3/4/4/4/4/3/3/2 seconds [official]. Every extra shot is one more chance of error.
   - **Dialogue scenes: prefer multi-shot**. In community tests, a one-take dialogue shot failed three times out of three to get both accurate line timing and silence at the end [single source: drama-skills tests].
3. **Allocate time**: see "Timeline" below. One main change per segment.
4. **Write end states**: end each segment with one sentence of "what can be seen directly in the frame" (where the character stands, what is in the hands, what framing the camera stops on). The next segment starts from that state. This is what keeps 30 seconds from drifting. With hard cuts, time and place may jump (hallway → kitchen), but costume, prop positions, and left/right placement carry over. When the place changes, state the new place at the start of the next shot.
5. **Dialogue ledger** (when there is dialogue, narration, or a voice reference; check it yourself before writing, and keep it out of the prompt): one row per time range — speaker, on or off screen, addressed to whom, the line, language, mora count and minimum duration, which audio clip, and what everyone else present is doing. Check range by range: each line appears once; at most one speaker per range; no range that should carry speech or an audio clip is written as silent; speakers and audio clips are not swapped; every line comes from the user's own text; at most two voice references per clip [official sd25-pe; author-tested]. A sample ledger is in `references/kemono-jp-drama.md` 3.4.
6. **A rhythm that holds attention**: cold open, with the event in second 1 and the setting after it. Put one visible event in the first 2 seconds of every segment, one turn in the relationship in the middle, and hold on one image for the last 3 seconds. In a series, the first 10 seconds decide whether viewers stay [author-tested: an episode with a slow opening had a clearly higher 3 second bounce rate than usual].

### 4. Write in the fixed section order

The official order is: asset references → one-sentence overview → segments (timestamps or "Shot N") → camera, environment, sound, and mood that run through the whole clip [official]. This skill's fixed sections are compatible with it and are the default: style → references → characters → scene layout → light → sound → timed shot list → ambience [author-tested].

Section labels are plain words followed by a colon. Do not use 【】 for labels: in the official symbol table 【】 means subtitles, and labels written that way have shown up as on-screen text [multi-source community reports].

```text
Style: ___ (visible traits: medium, line, colouring, light. With a creator profile, copy the style line from creator-profile.md word for word)
(optional) Overview: ___ in ___, ___, ending on ___.
References: (delete this section if there are no assets; one asset per line, each with a short name)
@Image1 (___, head): use only ___'s head fur colour, eyes, ear shape, and muzzle length.
@Image2 (___, full body): use only ___'s clothing, accessories, and body proportions.
@Image3 (___): use only the layout, materials, and light of ___.
@Audio1 (___'s voice): provides only ___'s timbre, pace, and tone; the words follow the text.
Characters: The whole clip has only two characters, ___ and ___, and each appears exactly once in frame.
___: ___ anthro, adult male, ___ (species anatomy); the trait only he has: ___. Appearance follows @Image1 and @Image2. ___ speaks with the voice of @Audio1.
___: … (one line per character on screen)
Each keeps his own fur colour, clothing, and identifying trait throughout.
Scene layout: ___ is on the ___ side of ___, ___ is on the ___ side of ___; the camera always stays on the ___ side of the line between them.
Light: The key light is off-screen ___, ___.
Sound: The only sounds are ambience, action sounds, and dialogue. There are ___ lines in the whole clip, and only one person speaks in any time range. The picture is clean footage.
Shots:
Shot 1 (0–___ s): ___ framing, camera at ___ height, facing ___, camera ___; place: ___. Foreground ___, background ___. ___ (a chain of small continuous actions). Moving details: ___. Expression: ears ___, eyes ___. Ends with: ___.
Shot 2 (___–___ s): hard cut, continuing from the previous shot: ___. Name (Japanese, voice, emotion, to whom): {line} ___ listens quietly with his mouth closed. Ends with: ___.
…
Ambience: 0–30 s: <___> continues to the last second; second ___ <___>.
```

On Jimeng and Doubao the reference tokens are `@图片1`, `@视频1`, `@音频1`. Use whatever token the platform inserts when the asset is attached.

- One take: replace "Shots:" with "Segments:" written by time range, and open each segment after the first with "The camera keeps moving and…".
- When the user gave no time ranges and did not ask for second-level control (see "Timeline"), replace "Shots:" with "Phase one: Starts with: …; Main event: …; Ends with: …".
- For assets that are uploaded but unused in this clip, add an "Unused assets:" line after References and list each number: "@Image4 and @Audio2 are idle in this clip; its characters, scene, props, action, camera, and sound come only from the assets given roles above." [official sd25-pe requires listing each one; the positive wording is this skill's rewrite and has not been tested separately]
- Other subjects: replace the character lines with appearance, clothing, and a signature prop. With an asset, write "appearance follows @Image1" and do not describe it again.

Full examples: anthro subjects in `references/templates-kemono.md`; one-take narrative, 9 shot drama, product ad, talking head, action, beat-synced music, first/last frames, edit, extension, and stitching in `references/templates-30s.md`. Read the section closest to the request and borrow its structure, not its content.

### 5. Self-check before delivery

- The prompt contains no aspect ratio, total duration, resolution, frame rate, or audio switch; those are in platform settings. Time ranges stay in [official sd25-pe].
- The prompt is positive throughout: things to exclude are written as "only…" and "stays… throughout". No quality, stability, watermark, subtitle, or duplicate-character constraints were added that the user did not ask for [official sd25-pe; author-tested].
- The timeline runs continuously from 0 to the total duration and the segments add up to it. Each segment has one main change and one main camera move, with subject motion and camera motion written separately. Each segment has "Ends with: …".
- One take: every segment after the first opens with "The camera keeps moving and…", and crossings between spaces have a written path [test run].
- Assets: numbering matches upload order, sorted by first appearance; one line binds one character, prop, or scene; each says "use only" which part; uploaded but unused assets are each listed under "Unused assets:" [official sd25-pe].
- Head count, clothing, prop ownership, and left/right placement stay continuous. Every anthro character has species anatomy and one trait only he has; every background figure has a species [author-tested].
- Every shot states foreground and background from the camera's position. No shot has three or more people taking turns to speak [single source: drama-skills tests].
- The dialogue ledger was checked range by range: every line comes from the user's text, appears once, in its own range; one speaker per range, everyone else with mouths closed; Japanese mora counts fit [official sd25-pe; inference].
- Cause before effect: the viewer sees the trigger clearly before the reaction close-up [official sd25-pe].
- Every shot restates clothing state (cape, gloves, sword sheathed or in hand) and hands (the species' hand, five fingers, claw colour). Clothing written only under Characters is ignored. Small props have colour and shape ("an old red-copper coin"); accessories have a size [author-tested].
- First/last frames and keyframes use standalone sentences: "@Image N is the first frame." "@Image N is the last frame." [official sd25-pe]
- Sound: music (), sound effects <>, dialogue {}; ambience runs to the last second; the sound setup is consistent from start to end [official; author-tested].
- The ending holds on a definite image. Empty words such as "premium, cinematic, silky" have been replaced by concrete camera description.

## Core techniques for 30 seconds

### Timeline: timed shots, or phases without numbers

- This skill's default is five to nine shots timed by the second [author-tested]. Seedance 2.5 responds to integer-second timestamps; 2.0 responds only to shot numbers [official].
- Use integer seconds, running continuously from 0 to the total duration, with no overlaps and no gaps. Three forms work: ranges ("0–3 s"), points ("at second 5"), and relative time ("3 seconds later") [official]. A key instant inside a range (an impact, a beat hit) can be marked separately with "at second X".
- Time ranges are an event budget, not frame-accurate cut points. Community tests show cuts landing 0.3–0.5 s off, so decimals are pointless [single source: drama-skills tests]. Do not use timestamps to control frequency ("shakes his head 3 times in one second") [official].
- Match the amount of content to the length of each range. Too little and the model improvises; too much and it over-cuts or drops plot. When events are too dense, merge minor events and reduce the number of ranges instead of subdividing further [official].
- When the user gave no time ranges and did not ask for second-level control, follow official sd25-pe and use unnumbered "Phase one / two / three", each with one main change of state. Do not invent ranges like "0–8 s" just because the platform duration is 30 seconds [official sd25-pe].
- When the user's seconds do not add up to the platform duration, point it out and ask whether to change the seconds or the duration [official sd25-pe].

### Common 30 second allocations

| Type | Allocation |
|---|---|
| One-take narrative | 0–7 establish / 7–15 develop / 15–23 turn or climax / 23–30 close and hold |
| Four-part | 0–6 set the scene / 6–14 medium follow shot develops / 14–23 close-up or change builds the climax / 23–30 ending |
| Three-act | 0–8 setup / 8–20 development and turn / 20–30 climax and resolution |
| Product ad (problem → solution) | 0–3 hook / 3–9 pain point / 9–15 product enters / 15–20 key turn / 20–26 emotional high / 26–30 product end card |
| Story-led brand ad (product enters late) | 0–3 hook / 3–11 setup / 11–17 emotional turn and line / 17–22 product enters naturally / 22–26 emotional high / 26–30 product end card |
| 9 shot drama (official example) | 0–3 / 3–6 / 6–10 / 10–14 / 14–18 / 18–22 / 22–25 / 25–28 / 28–30 |
| Talking-head recommendation | 0–3 hook line / 3–10 pain point and product / 10–18 demo / 18–26 experience / 26–30 call to action |
| Beat-synced music | Cut on the beat: at 120 BPM one bar is 2 seconds, cuts land on bars; slow down for the last 6–10 seconds |
| Realistic line, anthro dialogue (7 shots) | 2–3 s opening → single close shots following the lines, 3–5 s each → listener reaction + slow push → close-up on the turning line, 4–5 s → settle to a held ending [inference, see shot-grammar.md] |
| Cel-shaded line, everyday dialogue (9 shots) | 3–4 s per line, 2 s emotional close-ups, plus one 2–3 s "ma" cutaway with ambience only [inference] |
| Hand-painted fantasy line, narrative (6 shots) | 5–6 s opening → 3–5 s middle shots → 5 s or more held ending [inference] |
| Fight (6–9 shots) | One exchange per 2–4 s range, each with "Ends with", see combat-closeups.md section 9 [inference] |

For shot counts: recomputed from shot data on 2,356 films, 30 seconds of dialogue is about 5 shots (about 6 s each), Ghibli-style animation about 6, and action about 9 (about 3.3 s each). Two-shots hold longer than singles, and tighter framings hold shorter [multi-source: DataReel recomputation]. Give every time window at least about 3 seconds. Sub-second instants such as impact frames go inside a window, not in a range of their own [single source: visual-skills]. The table is a starting point: when the user supplies the story order, allocate in that order. The middle (about 12–20 s) is where repetition and drift happen most, so always give it one specific change and one definite camera move.

### Assets (omni reference)

- Numbering follows upload order (@Image1, @Video1, @Audio1). Upload multiple characters in order of first appearance so numbers follow appearance order. Names are bound in the prompt, not by text written on the image [official].
- One line defines one character, group, prop, or scene and which assets it uses. Write "Kael is @Image1 and @Image2", "Gerard is @Image3 and @Image4", not a range sentence like "Kael and Gerard follow @Image1 to @Image4" [official sd25-pe]. When one character uses several images (head + full body), state that these images together define this one character and that there is only one of him in frame. Each character on screen uses his own solo image [official sd25-pe].
- For each asset write which part to use, for example "@Image1 (Kael, head): use only Kael's black head fur, amber eyes, and ear shape", "@Video1: use only the fight choreography and camera rhythm; character appearance follows @Image1 and @Image3" [official requires stating what is referenced; "use only" is the author's wording]. When a scene image or reference video contains people, lock it under Characters: "The only characters in this clip are Kael and Gerard". If people still leak in, add the official sentence "do not use the people in the image" (negative wording, for troubleshooting).
- When an asset is already accurate, only point to it ("follow the action and camera of @Video1 strictly, in the same order as the video") and do not restate details. Restated text can fight the asset [official].
- Typical roles: character images fix face, fur colour, and clothing; product images fix packaging, material, and logo position; scene images fix space, palette, and light; reference videos fix action, camera, and rhythm; audio fixes beat, mood, and voice.
- Voice references: bind at most two per clip, one speaker per shot [author-tested]. 5–10 seconds of clean solo voice works best [official; multi-source]. Bind with "Image 1 and Image 2 are Kael; Kael speaks with the voice of @Audio1". Audio provides only timbre, pace, and tone; the words follow the text [official sd25-pe]. Use only voices you recorded or have a licence for.
- Limits: 30 images (each up to 4K), 10 videos, 10 audio clips, 50 assets in total, with audio and video each totalling 30 seconds or less. When over the limit, add an "Asset note:" in the reply saying what to remove before submitting [official]. Stable range: 1–8 subjects for subject images; 1–5 subjects for subject audio and video, 5–10 seconds each [official]. The usual setup (head and full-body image per character on screen, one scene image, at most two voice clips) sits inside this range. The more assets there are, the more precisely their roles must be written.
- Several views of one subject work better uploaded as separate single-view images than combined into one sheet [official]. Keep image aspect ratios between 0.4 and 2.5 [official; author-tested: Pippit rejects images outside it]. Use the final 4K images as character references, not small web outputs [author-tested]. If fingerprint-like texture appears, downscale the inputs to no more than the output resolution [official troubleshooting advice].
- Photos of real animals (pets, mounts, ordinary birds): use only breed, coat pattern, ears, and build, ideally from a full-body photo [inference]. Anthro characters are not handled as animals; see "Anthro characters" below.
- Characters without a reference image: give 2–3 fixed appearance anchors (fur colour or hairstyle, the colour and material of the clothes, one accessory), write "wears the same ___ throughout", and use few face close-ups. Characters with reference images get their own images attached to every clip, and the whole character line is rewritten each time, never "same as the previous clip" [author-tested]. For more stability, make reference images with GPT Image first.
- First and last frames: one standalone role sentence each, at the very start of the prompt: "@Image1 is the first frame." "@Image2 is the last frame." After each, a new sentence states what the image defines, for example "This first frame defines both characters' positions, facing, prop positions, and the camera direction." [official sd25-pe] The first frame sets the output aspect ratio, and the two frames must share an aspect ratio or the last frame is stretched [official]. Note: in omni reference mode, "@Image1 is the first frame" gives a similar opening, not a locked one. To lock the opening frame, use the platform's first/last frame mode (in the API, role `first_frame` / `last_frame`) [official: similar but not identical; community tests report low similarity].
- Multiple keyframes: open with "Use @Image1 to @Image N in order as keyframes.", then one line per image, "@Image2 defines the second keyframe: ___ (the visible state at that moment).", with continuous action written between frames [official sd25-pe]. Keyframes are states to pass through, not frames to stop on. Separate single images align more accurately than a grid [official].
- Storyboard grids: 15 panels or fewer, in clean line art or stick figures, with little text [official]. Open with "@Image1 provides the shot order and rough composition of a nine-panel storyboard, read left to right and top to bottom; use only the shot order and composition.", then give the overall story, then fill in per panel the action, camera, and style the board lacks. For strict alignment, switch to keyframes [official]. When making the board with GPT Image, also make a picture-only version (no speech bubbles or text), because text on the image can be carried into the video [official].
- Grey-box / 3D previs: state which elements of the previs to follow (camera, action, light) and map each primitive to a specific subject or prop. To follow its lighting changes, say "follow the lighting changes" explicitly [official].

### Anthro characters

An anthro character stands upright, wears clothes, and talks. Do not handle him as an "animal": performance, dialogue, and muzzle lip-sync are written as for a character. Details in `references/kemono-jp-drama.md` section 1.

- Write the species as visible anatomy plus one trait only he has, and repeat the trait every time he is mentioned. For example: "Kael: black wolf anthro, adult male, a complete wolf head with a long muzzle, black fur over the whole body, upright on two legs, canine paw-hands (four fingers and a thumb); the trait only he has: a red scarf. Appearance and clothing follow @Image1 and @Image2." [author-tested; the anatomy wording is inference]
- Leave build to the reference image and write no body-type adjectives. For details the profile lacks, write "as in @Image N" [author-tested].
- Write poses concretely: "on one knee, torso upright". "Half-squatting" gets drawn on all fours [author-tested].
- In water or swimming, write "Gunnar keeps the anthro posture and clothing of @Image N in the water: torso upright, arms pulling through the water". He has been drawn as a real orca when he entered the water [author-tested].
- Give every background figure a species, for example "the tavern's customers are two bear sailors and a fox waiter". Generic passers-by get drawn as humans [author-tested].
- Keep look-alike characters (Seren and Sil, a mount and its rider) out of the same frame where possible. When they share a frame, state each one's position relative to a fixed object such as a table or door, and write the blocking if they swap front and back [author-tested].
- Write eyes as "the amber animal eyes of @Image1, with a soft catchlight" (colour from the profile or reference). "Normal human eyes" may put human eyes on an animal face [inference].
- When real animals are also present, give dialogue to characters only, for example "Only the rider speaks; the mount is an ordinary horse with its mouth naturally closed, snorting now and then" [inference; official requires stating the speaker].

### Camera moves and film language

- One main camera move per segment (push, pull, pan, track, follow, orbit, crane, handheld, static), with direction and speed. Stack a push, an orbit, and a crane in one segment and the model drops some of them.
- Write subject motion and camera motion separately: "the character walks toward screen right; the camera tracks left with him".
- State positions as foreground and background from the camera: "the foreground is the soft blur of Kael's left shoulder and ear; the background is Gerard from the chest up". In community tests, writing only "facing each other across a table" failed 9 times out of 9; with foreground and background written from the camera position it succeeded 3 times out of 3 [single source: drama-skills tests]. Shots where three people take turns speaking tend to assign lines to the wrong speaker, so keep dialogue scenes to two-person compositions [single source].
- Hold screen direction: if a character enters from the left and moves right, keep that direction for the whole clip. Keep the camera on one side of the line between the two characters, anchor each person to a fixed object (table, door, mainmast), and repeat left/right and eyeline in every shot [official]. An orbit beyond about 90° makes the two swap sides on screen. A short 10–15° arc still ends on the original side [author-tested; inference].
- Popular moves can be named directly: one take, dolly zoom, aerial, FPV, bullet time, handheld, speed ramp. Include the subject it acts on, start point, direction, and end point [official].
- "Translate" niche terms: term + subject it acts on + what changes in frame + foreground/background relation + direction or speed. Focal length and aperture may be written, but describing the visible result is more reliable ("the background melts into soft bokeh" is steadier than "f/1.4") [official].
- For transitions, state when and how they trigger (foreground wipe, whip pan, a character turning, an object morphing, a push/pull or focus change).
- More terms in `references/camera-and-sound.md`; fight camera work and close-ups in `references/combat-closeups.md`; arranging shots the anime, TV drama, or film way in `references/shot-grammar.md`.

### Performance and realism

- Write emotion as something visible. For anthro characters use ears, tail, eyeline, muzzle, and fur first, for example "Kael's ears press back for a moment, then rise again, and his eyes move to the window". Do not write "blushes" or "his eyes light up" [author-tested; official asks for observable behaviour]. An ear-and-tail table is in `references/kemono-jp-drama.md` 1.6.
- Write a reaction as a causal chain: trigger → pause to take it in → first reaction → the body follows → afterglow of the previous emotion → end state. For each beat write 1–3 details that are readable at the current framing, with their size ("the tip of his ear twitches slightly"). Listing brow, eyes, nose, and mouth one by one produces emoji-style switching [multi-source: official sd25-pe and several community skills agree].
- Cause before effect: when a character changes expression or action because of something, show the cause clearly first, then the reaction. If cause and reaction fit in one frame, put them in one composition. If they are far apart, link them with one shift of gaze or one camera move. Do not push in to a pure face close-up before the cause is clear [official sd25-pe].
- Write a pause as its own time range containing small visible actions and ambience, with everyone's mouth closed. Hesitation and interruption go into the line itself as 「……」 and 「——」 [official example; the standalone pause range is inference]. Write subtext as the contrast between what is said and what the body does [inference].
- Strong emotion words (fanatical, utterly shocked, murderous) can make eyes glow. Replace them with ordinary description plus the eyes' own colour and a soft catchlight [official FAQ]. Only when positive wording fails, add the official sentence "the character's eyes do not glow" (negative wording, for troubleshooting).
- Keep action general and give detail only to the one or two most memorable moves. Write each action once [official].
- In still passages keep breathing, fur, fabric, and the environment slightly alive; a static camera is not a frozen frame. For fur, state which part moves and which way, for example "a light breeze from off-screen left makes the long fur on Kael's neck and the fine fur at his ear tips tremble with the wind" [inference].
- For realism, write photographic language: which off-screen side the light comes from, shallow depth of field, fur direction and long/short fur zones, clothing creases, everyday clutter in the setting; for human characters, skin texture. "Backlit" alone puts a halo over the head; write "the key light is off-screen back left and draws a thin bright rim along the ears and shoulders" [author-tested].

### Sound and dialogue

- Sound symbols follow the official table: music (), sound effects <>, dialogue {}, subtitles 【】 [official: the 2.5 tutorial's symbol rules; sd25-pe agrees]. Dialogue goes only in {}. When marking sound effects with <>, do not put angle brackets around character names [official sd25-pe].
- Dialogue line: `Name (language, voice, emotion, to whom): {line}`, for example "Kael (Japanese, a low male voice in a cold big-brother manner, quiet but forceful, to Gerard): {……これは命令だ。} Gerard listens quietly with his mouth closed." The official recommendation is "Character line (emotion): text", with the language stated before any non-Chinese line and every speaker labelled one by one [official]. The "voice" and "to whom" slots are the author's additions [author-tested]. Add regional accents and dialects only when the user specifies them [official sd25-pe].
- Write each line in the time range or shot where it happens, once in the whole clip. The Sound section says only "N lines in the whole clip" and does not repeat the text.
- Only one person speaks per time range; everyone else present "listens quietly with his mouth closed". In ranges with no dialogue, write that those present keep their mouths closed [official sd25-pe; test run: an unwritten line appeared once at 0–1 s, not yet re-tested]. When a line plays over the listener's reaction shot, write "X (off-screen, Japanese, …): {…}" and keep the on-screen character's mouth closed [inference]. For inner monologue, first write "X's muzzle is closed", then "X (V.O., Japanese, …): {…}" [official example].
- Emotion and tone go in the parentheses before the line. After the line, go straight to the next action or "Ends with". Do not repeat words from the line or add tone notes after it; the official FAQ says this tends to trigger subtitles [official].
- For volume write "quiet but forceful", not "loudly" (which raises pitch). Rewrite hard-to-read kanji in kana (飯 → メシ). Avoid digits in lines (sources disagree on how they are read). Say character names rarely: platforms may rewrite them, and they can trip copyright filters [author-tested; multi-source].
- Duration: estimate Japanese by mora. Restrained dialogue runs 5–6 morae per second, plus about 1 second per line; split lines over about 20 morae across two shots [inference, basis in `references/kemono-jp-drama.md` 2.3]. English runs about 2.5–3 words per second at a normal pace [inference]. Officially more than ten languages are supported natively, Japanese included; in the 2.0 technical report Japanese scored below English on "says what the prompt says", so test one line at 480p before a final render [official; multi-source].
- Write sound effects by physical source ("rain hitting a tin roof", "the creak of a wooden door being pulled open") in the same second as the action. Run ambience to the last second or the second half may go silent [author-tested].
- For scenes at sea, in night rain, or underwater, name only one or two specific sources (wind, rigging, creaking planks) and say little about water, waves, or echo: the official FAQ says such descriptions tend to bring bubbling and echo noise [official].
- For subtitles and music, start positive: "The only sounds are ambience, action sounds, and dialogue", "The picture is clean footage; text appears only on signs that belong to the scene" [author-tested]. If the reference video itself has subtitles, switch to one without. Landscape in platform settings also lowers the chance of subtitles [official]. If they still appear, add the official wording "the picture shows no subtitles", or remove them with video editing (negative wording, for troubleshooting).

### Use only the dialogue the user gave

- The user supplied the lines: use them word for word, adding only speaker, language, voice, emotion, and addressee. Add no sentences before or after [official sd25-pe]. Do not alter Japanese the user wrote.
- The user gave only the intent ("Kael tells Gerard to go and rest", "the two start arguing") and no text: write no {} in the prompt. Show the intent through action, pauses, gaze, and the other character's reaction, with mouths closed [official sd25-pe]. In the reply's "Dialogue draft", give 1–2 Japanese lines in the character's voice, marked "Draft, not in the prompt", with meaning and mora count. Put them in {} after the user confirms.
- The user gave lines in their own language and the film is in Japanese: translate them into Japanese in the character's register, put them in {}, and attach the original alongside in the reply, marked "Translation, please confirm". This is translating the user's own lines, not inventing [inference].
- The user wants a character to speak and bound a voice, but gave no line: keep the role "X speaks with the voice of @Audio N", put the line in "Dialogue draft" for the user to fill, and invent nothing in the prompt [official sd25-pe].
- Canonical lines from a character's profile (Kael's 「……これは命令だ。」, Seren's 「……もう一回。」) go in {} only when the script uses them. When a character's way of speaking changes over the story, check which stage this episode is at before writing his lines and do not skip ahead. If the profile does not say, remind the user in the draft to check [author-tested].

### Editing, extension, and partial reshoots

- **Editing**: the prompt must contain one of "edit the video / add / delete / remove / modify / replace / change to" [official]. Order: declare the original video the only master → edit target → edit scope (limited by timestamps) → what stays the same, closing with a scope sentence: "Apart from the objects explicitly modified above, every other visible character, prop, and background element in @Video1 stays exactly as it is" [official sd25-pe]. Describe the change from A to B. Originals of 20 seconds or less work best; change one thing at a time [official]. When only one Japanese line is misread, edit just that line; example in `references/kemono-jp-drama.md` 2.5.
- **When a reference video is only an action reference**: the words above turn the task into an edit, and an edit locks the original's aspect ratio and duration. So write "Following the fight choreography and camera rhythm of @Video1, generate…" and bind character appearance with images [inference from the official edit trigger words]. When the reference video's aspect ratio or duration differs from the target (for example a 16:9 rehearsal video for a 21:9 final), follow the sentence stating the generation goal with "Note that this is not a video edit." [official sd25-pe]
- **Extension**: the prompt must contain one of "extend forward / extend backward / continue" [official]. To extend backward (after the end), first describe the state of the original's last frame (pose, props, background, camera position, light, sound, direction of motion), then the new content. To extend forward (before the start), write the original's first frame as the end state of the new part. State that each subject is the same continuous object throughout, for example "one Kael, one Gerard, a single continuous shot from start to end" [official sd25-pe]. Extending a video Seedance 2.5 itself generated joins most naturally; community tests joined seamlessly 3 times out of 3 [official; single source]. Long conversations suit extension into one continuous long shot; fights suit generating in parts and cutting [official 2.0].
- **Partial reshoot** (Pippit and similar platforms): select only the stretch that needs changing and change one thing at a time. The tighter the selection, the cheaper it is.
- Full patterns in `references/templates-30s.md` section 8.

### Beyond 30 seconds

Split into several prompts of 30 seconds or less, cut at natural shot boundaries. Each one restarts timing at 0, rewrites the style line, character lines, clothing, and light, and re-attaches each on-screen character's own reference images. Never write "same as the previous clip": the model cannot see the previous clip [author-tested]. The end state of one clip is the start state of the next. Three ways to join:

- The low-effort way: upload the previous clip's last frame as an ordinary reference image and write "@Image N (last frame of the previous clip): use only the two characters' positions, facing, and the camera position" [author-tested].
- To lock the opening frame: use first/last frame mode, with the previous clip's last frame as the next clip's first frame (the API can return the last frame). The first frame sets the aspect ratio [official].
- For seamless motion: run "extend backward" on the previous clip directly [official; single-source test].

## Platforms and parameters (as of 2026-10; official docs and the platform UI take precedence)

- Entry points: Dreamina and CapCut internationally, BytePlus ModelArk for the API; in China Jimeng, Doubao, and Pippit (web and app) and Volcengine Ark (model ID `doubao-seedance-2-5-260628`). Similarly named sites such as seedance.tv are not ByteDance.
- Duration: 4–30 seconds, or -1 to let the model choose. Aspect ratio: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, adaptive. Resolution: 480p, 720p, 1080p (the app can upscale to 4K). Output mp4 or mov.
- Jimeng web: measured in 2026-10 at 270 credits for a 30 second 480p draft and 600 credits for 720p (prices change; check the page). The page defaults to "Seedance 2.5 (draft mode)", so switch manually before a final render. One clip takes about 6–10 minutes [author-tested; test run].
- In the API, first/last frame mode and edit and extension tasks require `ratio` set to `adaptive`. Set an edit task's `duration` to -1; the output may differ from the original by about 0.3 s, and there is no gap when the input is a Seedance 2.5 video [official]. First/last frames given with `content.role` = `first_frame` / `last_frame` lock the aspect ratio. Using `reference_image` and naming the first and last frames in the prompt does not lock it, and the result is similar but not identical [official].
- Through the API, @Image N corresponds to the order of same-type items in the content array (follow the official doc examples).
- With Seedance 2.0: 15 second limit per run, about 9 images, 3 videos, and 3 audio clips. 2.0 does not respond to timestamps, only shot numbers, so write "Shot 1 / Shot 2" and compress the timeline into 15 seconds [official; the asset limit is third-party].
- Prompt length: a 30 second multi-shot prompt in English usually needs 400–900 words. Official sd25-pe sets no limit; when it gets long, compress repeated style words and constraints first. Community experience is that overlong, over-detailed prompts generate more slowly and are blocked by moderation more often. When the platform truncates or warns about length, cut scene clutter and repeated constraints first, and keep asset roles, the timeline, end states, and dialogue.

## Troubleshooting

| Symptom | Usual cause | Fix |
|---|---|---|
| Repeated action or drift in the middle | The middle has no camera move or turn | Give the middle one specific change and one definite camera move |
| A one-take is cut at a segment boundary | The spaces are far apart, or the prompt says "Shot 1/2/3" | Write by time range; open each later segment with "The camera keeps moving and…"; write the path across spaces; drop to 3 segments [test run: 7.38 s] |
| More shots than written | Content too dense | Merge minor events, use fewer segments [official] |
| Face changes, two characters blend or swap | Numbering does not match order of appearance; no identifying trait | Upload in order of first appearance and renumber; one character per line; repeat his unique trait at every mention [official; author-tested] |
| Extra or duplicate characters | Head count not locked | "The whole clip has only two characters, Kael and Gerard, and each appears exactly once in frame" |
| Anthro turns into a real animal, goes on all fours, or becomes a human with animal ears | Entering water, "half-squatting", or only "wolf anthro" | Write species anatomy and a concrete pose, see "Anthro characters" [author-tested] |
| Background figures become human | Only "passers-by" or "customers" | Give each background figure a species [author-tested] |
| Positions and eyelines scrambled | Only a relation such as "across the table" | Write foreground and background from the camera in every shot; repeat left/right and eyeline [single-source test] |
| A line is spoken by the wrong character, or two mouths move | Both in frame with no statement of who speaks and who listens | One speaker per range, others "listen quietly with mouths closed"; move the line to the speaker's single close shot [official] |
| An unwritten line appears at the start | The opening range does not say those present keep their mouths closed | Write closed mouths in the opening range, and "N lines in the whole clip" under Sound [test run, not yet re-tested] |
| Speaking pitch too high | "Loudly" | Change to "quiet but forceful" [author-tested] |
| A line bleeds into another character's shot, or uses the other voice | Two people and two voice clips in one clip | Move the line to the speaker's solo shot. If it still bleeds, generate a 4–5 s insert with only his image and audio and replace that line; cheaper than rerunning 30 seconds [author-tested] |
| A supporting character speaks without opening his mouth, or bystanders mouth along | "His mouth barely opens", or no statement of who speaks | Speaker: "opens his mouth to speak, mouth opening and closing"; others: "mouth stays closed, standing quietly" [author-tested] |
| An accessory, scar, braid, or bandage jumps to another character or multiplies | The trait was written once, or the plot no longer needs it | State ownership and count: "the only braid in his mane is this one on the left", "the bandage wraps only the index finger"; give the other character's accessory a material and colour to tell them apart; delete scars and gauze the plot no longer needs [author-tested] |
| An accessory keeps growing | Named but not sized, or already large in the reference | Write size and fit: "a small lip ring, tight against the lower lip"; if it still grows, check the reference image first [author-tested] |
| An extra hand or extra fingers when hugging or sharing a cloak | Both hands' actions written at once | Write one arm's action only, lock the camera, hide the other hand behind the body or cloak, write "five fingers spread" [author-tested] |
| Background figures grow human faces | Occupation nouns (fisherman, old woman, old sailor) | Species first: "a goat-headed anthro with a pair of curved horns, a long muzzle, and fur on the hands", occupation after [author-tested] |
| A crowd becomes all one species | One sentence for the whole crowd | Write species row by row and position by position: "two goat-headed anthros in the front row, one gull-headed anthro in the second" [author-tested] |
| Sung lyrics are spoken, or run into the next shot | The voice reference only has speech; no singing duration given | Write "opens his mouth and sings, drawing out each syllable", put ♪ before and after the lyric, state from which second to which, allow about 5 s per sung line; if still spoken, use a humming voice reference or replace the vocal in post [author-tested] |
| A prop's name is drawn literally (the knot of a "pretzel knot" becomes real bread) | The prop was described by comparing it to food or another object | Describe the shape instead: "a small heart-shaped knot" [author-tested] |
| Japanese misread | Rare kanji, digits, character names | Rewrite in kana; avoid digits in lines; when only one line is wrong, fix it with video editing |
| No sound in the second half | Ambience not written to the end | Write ambience to the last second [author-tested] |
| A mount or pet opens its mouth and talks | Dialogue with no speaker stated | "Only the rider speaks; the mount is an ordinary horse with its mouth naturally closed" |
| A small detail given only in text drifts (a black schoolbag turns dark blue) | Text loses to the model's defaults | Put key colours and prop states in a reference image, or write them again in the shot where they enter frame [test run; inference] |
| Subtitles appear | Notes added after a line; reference video has subtitles; portrait | Emotion before the line; a subtitle-free asset; landscape in platform settings; if that fails, add the official "the picture shows no subtitles" (negative wording, for troubleshooting) or delete them with video editing [official] |
| Heading-like text appears in the picture | Section labels were written in 【】 (which also means subtitles in the official table) | Use plain labels such as "Style:" [multi-source community experience] |
| Background music will not go away | Generated by default | Start with "The only sounds are ambience, action sounds, and dialogue". If that fails, follow the official FAQ and exclude the whole family of music words (music, background music, BGM, score, instrumental, melody) once at the start and once at the end (negative wording, for troubleshooting), or separate the vocals in post [official] |
| Glowing eyes | Strong emotion words | Ordinary description plus eye colour and a soft catchlight; if that fails, add "the character's eyes do not glow" (negative wording, for troubleshooting) [official FAQ] |
| Bubbling or echo at sea or in rain | Water, waves, or echo in the prompt | Name only one or two specific sound sources (wind, rigging, creaking planks) [official FAQ] |
| Fingerprint-like texture | Input image resolution above output | Lower the input resolution [official] |
| Storyboard grid out of order, or the picture is static | More than 15 panels | Keep to 15 or fewer, or switch to keyframes [official] |
| A jump at the join after extension | The original's ending state was not described | Describe the last-frame state in full before the new action [official] |
| Rejected by copyright review | Usually one full-body reference image | Remove that image and retry [author-tested] |
| A complex task keeps failing | Too much in one run | Split into several generations or edits and assemble in post [official] |

## Boundaries

- When a real person's photo or voice (voice actors included) is used as a reference, remind the user that the person's permission is needed and that platform review may block it. Seedance 2.5 does not accept reference images or videos containing real human faces [official].
- Original characters only: no names of existing animation or game characters in dialogue or prompts. Write style as visible traits, not as a director, studio, or title. State "adult male" for characters.
- Write fights as staged combat between original adult characters: strikes land on a blade, armour, or a blocking arm; force shows as sparks, dust, scratches in metal, and tears in cloth; write "both characters' fur and clothing stay intact and clean throughout". See `references/combat-closeups.md` section 7 [official sd25-pe; multi-source].
- When moderation rejects a prompt, treat it first as a false positive: remove wording likely to be misjudged ("bloodthirsty, biting"; replace summary words like "sexy" with specific cut and material), remove the reference image that triggers the copyright check, and retry [multi-source; author-tested]. If the content is compliant and still blocked, use the platform's feedback or appeal channel. This skill does not provide wording for getting around face review or content review: face review exists to stop real people being put into videos without consent, and evasion can also get the account banned.
- Text, prices, formulas, and brand marks that must be exact are better added in post than generated.
- This skill writes prompts. It does not submit generation jobs for the user by default. Actual platform capability follows the current UI and official docs; do not invent parameters or syntax.

## Reference files

- `references/creator-profile.template.md`: creator profile template. The user fills it in and saves it as `references/creator-profile.md`; read that before writing.
- `references/kemono-jp-drama.md`: Japanese dialogue scenes for anthro characters: character cards, drift prevention, muzzle lip-sync, ear and tail acting, line format, mora timing, voice binding, shot/reverse shot, reaction shots, ma, the dialogue ledger, subtitle prevention, with a complete 7 shot Kael × Gerard example.
- `references/combat-closeups.md`: fights, close-ups, and high-impact camera moves: how to write one exchange, wind-up → burst → freeze, the axis, weapon stability, compliant staged combat, the close-up toolbox, a 30 second fight rhythm table.
- `references/shot-grammar.md`: shot arrangement compared across anime, TV drama, and film; default shot grammar for the three example lines; how many shots in 30 seconds.
- `references/templates-kemono.md`: six 30 second templates in the fixed section order (night-deck dialogue, a fantasy fight, first-person everyday scene, a character-reveal montage, dialogue turning into combat, a dusk ride).
- `references/templates-30s.md`: 30 second examples for general subjects, plus first/last frame, keyframe, edit, extension, and stitching templates.
- `references/camera-and-sound.md`: quick tables for framing, camera position, camera moves, transitions, light, sound symbols and dialogue lines, and Japanese voice and register.
- `references/sources.md`: research sources, version information, and which claims are not officially confirmed.

## Sources

Researched 2026-10-28. Tags: [official] [multi-source] [single source] [inference]; [author-tested] is the author's own production notes and failure log; [test run] is a single generation on Jimeng on 2026-10-28.

- Official: Volcengine Ark, Seedance 2.5 prompt guide https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide ; English version https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5-prompt-guide
- Official: Volcengine Ark, Seedance 2.5 tutorial (sound symbols, asset limits, real-face restriction) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Official: sd25-pe skill 0.1.1 (parameter separation, no automatic generic negative constraints, unused assets, one subject per line, dialogue ledger, no invented dialogue, cause before effect, first-frame role sentence, phases versus numeric ranges, edit scope closure, single instance in extension) https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip
- Official: Pippit, Seedance 2.5 handbook https://www.xiaoyunque.com/tutorials/seedance-2-5
- Single source: zenstory-ai/drama-skills, Seedance 2.5 test notes (foreground/background from the camera, cut offsets, one-take dialogue, extension joins) https://github.com/zenstory-ai/drama-skills
- Single source: smixs/visual-skills (time windows of about 3 s or more) https://github.com/smixs/visual-skills
- Multi-source: DV DataReel shot data (recomputed 30 second shot budget) https://datareel.distantviewing.org/
- Single source: Morphed (time ranges instead of "Shot 1/2/3" for one takes) https://morphed.app/blog/seedance-2-5-prompts
- Other community sources, version information, and unconfirmed claims are in `references/sources.md`.
