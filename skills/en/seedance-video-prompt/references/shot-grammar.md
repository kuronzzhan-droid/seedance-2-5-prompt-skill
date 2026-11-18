# Shot grammar: how anime, TV drama, and film arrange shots

## When to read this file

Read it when deciding how many shots a 30 second video gets, how long each runs, how dialogue is covered, and how the camera moves, or when the result should feel "like anime / like a TV drama / like a film". The first half compares shot arrangement in the three media, each with paste-ready phrases. The second half applies it to the three example lines (realistic, cel-shaded, hand-painted fantasy): defaults, shot counts for 30 seconds, and complete examples. Line format and Japanese timing are in `kemono-jp-drama.md`; fights and close-ups are in `combat-closeups.md`. They are not repeated here.

Evidence tags: [official] Volcengine Ark and Pippit documentation or the official sd25-pe skill; [multi-source] two or more sources agree, including accepted industry convention; [single source] one study or one interview; [inference] derived from the material, not tested on Seedance; [author-tested] settings, habits, and failures from the author's production notes; [test run] one generation on Jimeng on 2026-10-28. Figures for TV drama and film come mainly from US, UK, and Korean studies; no shot statistics were found for Japanese live-action drama.

## Contents

1. Comparison at a glance
2. Key figures and how far to trust them
3. Anime
4. TV drama
5. Film
6. The three example lines: default shot grammar
7. How many shots in 30 seconds
8. Complete examples for the three lines
9. Common deviations
10. Sources

## 1. Comparison at a glance

| | Anime (TV) | TV drama | Film |
|---|---|---|---|
| Average per shot | About 3–4 s (derived from shot counts) | About 3–6 s | About 4.3 s, about 2 s in action |
| Shots in 30 s [inference] | 8–10 | 6–10 | Dialogue 4–7, fights 6–10 |
| How the camera moves | Characters move little, the camera moves: pans, pushes and pulls, layered parallax; fast orbits in fights | Mostly static, saved for emotional push-ins and walk-and-talks | Moves only with a motive, stops when the motive ends |
| Dialogue | Cuts back and forth between single close shots, often hiding the mouth, lines off-screen | Wide → over the shoulder → single close shot, cutting with the speaker | Shot/reverse shot or walk-and-talk; few lines, behaviour and hands tell the story |
| Close-ups | Many and fragmentary: eyes, hands, teeth, feet | An emotional push-in to a single close-up, then hold | Saved for the turning point, short and clean |
| Light and colour | Flat cel colouring + glow and light beams added in compositing | Daily dramas high-key and flat; prestige dramas low-key with sources in frame | Motivated low-key light, one palette for the whole film |
| Signature devices | Ma cutaways, freezing into a painting, impact frames | Reaction shots, flashbacks, the end-of-episode freeze | Staging in depth, match cuts, sound leading the cut |

The differences are tendencies, not hard lines: prestige streaming dramas borrow film technique heavily, with single-camera shooting, wide aspect ratios, and whole episodes in one take [multi-source].

## 2. Key figures and how far to trust them

| Medium | Measure | Value | Confidence |
|---|---|---|---|
| TV anime | Shots per episode (30 minute slot, about 20 minutes of content) | Commonly about 300, up to about 400; everyday "moe" shows routinely over 400, some episodes over 450; atmosphere-heavy shows about 230, occasionally under 200 | [multi-source] compositing interviews + critics' counts |
| TV anime | Average per shot | About 3.0–4.4 s | [inference] converted from the row above, not measured |
| Anime film | Shots in a film of about 2 hours | About 1,800 (about 4 s each) | [single source]; seconds are [inference] |
| Manga (the source of anime storyboards) | Panel framing | Japanese manga: multi-character panels 47%, single-character 43%, detail close-ups 10%; US comics about 60%, 35%, 5% | [single source]; extending to anime is [inference] |
| TV drama | Average shot length, first season of three US prestige dramas | 3.4 / 4.4 / 4.5 s, shortest in the one with most fighting | [single source] |
| TV drama | High-rated Korean dramas, 2004–08 | Average shot length: historical 5.51 s, family 6.24 s, melodrama 6.34 s; close-up share 55.84% / 18.58% / 28.72%; long shots 1.34–3.18%; moving shots 1.10–3.56% | [single source] |
| TV drama | Average scene | Korean 55–62 s, US 73–133 s | [multi-source] (two studies) |
| Film | Average shot length | About 10.5 s in 1930–55 → about 4.3 s in 1990–2015; 2–4 s is common now | [multi-source] |
| Film | Action films | About 2 s per shot (about 3,200 shots in a 105 minute action film) | [multi-source] |
| Film | Share of shots with camera movement | 16% (1959) → 6% (1999): movement concentrates in fewer shots | [single source], small sample |
| Film | Dialogue scenes among mid-film shots | About 60% | [single source] |
| Film | Intimate drama vs spectacle (first 30 minutes) | Close-ups 18% vs 9%; spectacle has about 3 times the long shots | [single source] |
| Film | Simultaneous sound layers | At most about 5 per 5 seconds or so; about 2.5 when they crowd one frequency band | [single source] |
| Seedance | Official examples | 9 shots in 30 s (3/3/4/4/4/4/3/3/2 s); a 13 s dialogue example cuts 8 shots, one short line each | [official] |
| Seedance | Pippit's advice | Split 30 s into 4–6 time ranges, otherwise the second half tends to go off course | [official] |
| Seedance | Timestamps | Integer seconds only, so 1 s is the shortest shot; a time range is an event budget, not a frame-accurate cut | [official] |

Average shot length is a mean, and a few very long shots pull it up. Treat it as a rhythm target, not a rule [multi-source].

## 3. Anime

Mostly TV anime. In animation the editing rhythm is fixed at the storyboard stage, not cut out of footage afterwards [multi-source], which is the same way of working as writing a timed shot list for Seedance. Paste-ready phrases follow the table; appearance is always left to the reference images.

| Dimension | Convention, and how it applies to Seedance | Basis |
|---|---|---|
| Aspect ratio and composition | TV is 16:9. Some theatrical sequels switch to widescreen to set themselves apart, holding the wide frame with detailed backgrounds. Every shot starts from a layout drawing: dialogue uses a calm standard-to-telephoto view with the camera between shoulder and waist height; fights use wide-angle exaggerated perspective, with fists and blades enlarged in the foreground. Low angles show strength, high angles lay out the situation; in a stand-off the weaker side is often on the left facing right; shooting past a foreground object or shoulder is common | 16:9 [inference: common knowledge, no statistics seen]; widescreen [single source]; composition [multi-source] |
| Framing mix | Dialogue is mostly single close shots and bust shots cut back and forth, with two-shots used only to establish positions; the setting is given to scenery-only long shots | [inference]: extended from manga panel statistics |
| Rhythm and shot length | About 3–4 s per shot, with seconds fixed in the storyboard; each director's shot-length style is very stable. "Ma" is left between lines and before actions: a held frame, or a cutaway with ambience only | [multi-source]; seconds [inference] |
| Camera movement | "The drawing moves little, the camera moves": animation runs on threes (8 drawings a second), characters hold one pose with only mouth, eyes, and hair moving, and motion comes from pans, pushes, pulls, or whole layers sliding across the frame. Foreground, character, and background are separate layers travelling at different speeds, producing paper-cutout parallax. Modern fights use fast orbits and violent push-pulls → stillness with movement, which also asks the model for less complex body action | [multi-source]; the benefit for the model [inference] |
| Dialogue coverage | Mouths are hidden to save drawing: the speaker has his back to camera, shows only a profile, is far away, or is blocked, and the camera stays on the listener's reaction; inner monologue plays over a still image with a closed mouth; only decisive lines get careful lip-sync → Seedance gives lip movement to any visible mouth, so state who is off-screen and that the on-screen character's mouth is closed | [multi-source]; lip movement [inference] |
| Fights | Hold, burst, hold: freeze to gather before the strike, burst through very few poses, freeze on the hit; smears, speed lines, an impact frame flashing on the hit; a key strike replayed from 2–3 angles → wording in `combat-closeups.md`; leave replays to duplication in post and write each action once in the prompt | [multi-source]; write once [official] |
| Close-ups | Many detail close-ups smaller than a character: an eye (pupil contracting), a clenched hand, gritted teeth, a footstep, placed at the emotional peak or the instant before a decision. Anthros: the ears turn to a sound, then flatten; the tail must move; long muzzles take three-quarter profile (hand drawing can quietly shorten a muzzle by angle, 3D cannot); avoid very low angles on large manes | [multi-source]; manes [single source] |
| Transitions | Mostly clean hard cuts; the peak of emotion or action freezes into a detailed hand-painted still held for 1–2 s; split screen for phone calls and stand-offs; at an emotional point the background flips to an abstract one such as flat colour or focus lines | [multi-source] |
| Light and colour | Cel colouring: flat base colour + one hard-edged shadow layer + a few highlights, clean lines; detailed hand-painted backgrounds are deliberately distinct from flat-coloured characters; the whole palette shifts with time of day. Compositing adds glow, diffusion, slanting light beams, lens flare, and depth of field; theatrical versions darken the picture so light stands out, and realistic TV shows lower contrast and saturation | [multi-source] |
| Sound | Picture first, voices after, with emotion carried by the voice actors; music is chosen from a library and laid onto the picture; music stops before a key line to leave silence, and fight sound effects are exaggerated → Seedance generates sound and picture together, so you can write which second the silence and the accent fall on | [multi-source]; last sentence [inference] |

```text
Rhythm: 9 shots in all with clean hard cuts between them: dialogue shots 3–4 s each, emotional close-ups 2 s, 1–2 s per shot in the action burst.
Stillness with movement: Magnus holds one still standing pose; only his blink, the fine fur at his ear tips, and the hem of his clothes move in the wind. The camera pans slowly across the frame and gradually pushes in, the foreground railing, the character, and the distant sky travelling as three layers, the foreground fastest and the sky slowest, like layered paper cutouts in parallax.
Dialogue with the mouth hidden: Rolf stands in the left foreground with his back to camera, showing only his shoulder and the side edge of his visor; Magnus is in the right middle ground, listening quietly with his mouth closed, both ears turned toward Rolf. Rolf (back to camera, Japanese, voice as in @Audio2, calm, to Magnus): {line}
Ma: after the previous line the picture is almost still for about 2 seconds with both mouths closed: only a tail tip swaying slowly and tree shadows moving outside the window; the only sounds are <cicadas> and <wind>.
Detail close-ups: extreme close-up of an eye, the pupil contracting sharply once, the eye keeping the colour in @Image1 with a soft catchlight; then a hand close-up, a clawed beast hand slowly closing into a fist, the knuckles tightening one by one.
Cel and compositing: 2D cel colouring, flat fur colours with a single hard-edged shadow layer and a few highlights, clean outlines; the background has a detailed hand-painted texture, leaning orange-violet at dusk; the light source is off-screen back left, a soft bright rim glows along the fur, and dust glitters in the slanting beams.
```

The gap between theatrical and TV versions is mostly resources: theatrical versions have more drawings and smoother motion and borrow more live-action language (rack focus, longer shots) [multi-source]. 3DCG also lets a single scene run longer, with a rhythm closer to live action [single source]. Overusing manga symbols (sweat drops, anger veins) and abstract backgrounds turns a realistic anthro story into comedy [inference].

## 4. TV drama

TV drama has the most mature dialogue grammar: to shoot dozens of scenes a day, it breaks a scene into a fixed set of camera positions and cuts among them [multi-source]. Thirty seconds is shorter than one TV scene, so arrange it as a compressed scene [inference]. Paste-ready phrases follow the table.

| Dimension | Convention, and how it applies to Seedance | Basis |
|---|---|---|
| Aspect ratio and composition | Landscape 16:9, faces and key action in the centre, only setting at the sides. Prestige streaming dramas often letterbox to 2:1 to look like film (platform specs tend not to go wider than 2:1). Vertical short drama is a different grammar (full-screen heads, vertical stacking); all three example lines are landscape, so it does not apply | [multi-source] |
| Framing mix | One speaking face per shot, mostly medium close-up to close shot; the wide shot appears once at the start. Close-up share varies a lot by genre (about 19%–56% in Korean dramas); long shots are only 1%–3% | Convention [multi-source]; shares [single source] |
| Rhythm and shot length | A cut every 3–6 s, following the speaker; shorter in tension and action, longer in melodrama, faster in US sitcoms (median 2.0–5.3 s). "A cut every 7–8 seconds" is a 1990s rule and out of date | [multi-source]; sitcoms and the old rule [single source] |
| Camera movement | Dialogue positions are static or drift very slowly; moving shots are only about 1%–4%. Movement is kept for walk-and-talks (the camera retreating ahead of the characters), establishing openings, and emotional push-ins. Two cameras at once is now common, one on a stabiliser. Romance climaxes often orbit the couple half a turn to a full turn with slow motion and strings → an orbit beyond about 90° swaps left and right, see `combat-closeups.md` section 5 | [multi-source]; the swap [inference] |
| Dialogue coverage | Standard coverage: establishing wide → two-shot → over the shoulder → single close shot, with all shot/reverse shots on one side of the 180-degree line; the same camera angle keeps returning within a scene | [multi-source] (accepted practice) |
| Fights | Cut faster and tighter than dialogue: one camera on a wide shot for positions, one on a long lens for hits and faces; handheld, camera from high down to eye level; long unbroken takes rehearsed for weeks, as in film, are rare | [multi-source] |
| Close-ups | When a character realises, decides, or senses danger, the camera pushes slowly from medium close-up to a single close-up and holds into the next shot. East Asian romance favours long-lens big close-ups with soft frontal light, and is criticised for over-smoothed skin → for anthros write "every strand of fur distinct" | [multi-source] |
| Transitions | Almost all hard cuts; the cut comes with the change of speaker, often to the listener before the line ends, and the listener often reacts before it ends; 1–2 s flashbacks at emotional peaks; episodes end on a suspense close-up or freeze; openings go straight into conflict → Seedance cannot cut accurately mid-sentence, so to "cut to the listener early", write the whole line as an off-screen line inside the listener's shot | [multi-source]; the short-drama "hook in the first 3 seconds" [single source]; time ranges as a budget [official]; the rewrite [inference] |
| Light and colour | Sitcoms and daily dramas are high-key and flat (key to fill near 1:1), everything visible. Prestige dramas are low-key, the light appearing to come from lamps and windows in frame, with deep shadows. Traditional TV has deep focus with everything sharp; the streaming era uses large formats and long lenses (85–135mm for faces), shallow depth of field, and deliberate rack focus | [multi-source] |
| Sound | Music marks the climax: the theme comes in after the last line, over the held close-up; Korean dramas reuse an OST track as the theme of one couple | [multi-source] |

```text
A compressed scene: Shot 1 (0–2 s) a wide shot establishing Kael and Gerard seated across a small wooden table; Shot 2 (2–6 s) past Gerard's blurred white ear and shoulder at Kael speaking; Shot 3 (6–10 s) the reverse, past Kael's blurred red scarf at Gerard answering; the camera always stays on the stove side of the line between them.
A line over the listener's face: the picture is Gerard alone in close shot, mouth closed, ears slowly pressing back, eyes dropping to the cup on the table. Kael (off-screen, Japanese, a low male voice in a cold big-brother manner, quiet but forceful, to Gerard): {……これは命令だ。} Ends with: Gerard's ears flat against his head, mouth still closed.
Emotional push-in: the camera pushes very slowly from a medium close-up to a face close-up and settles, the background gradually blurring; Kael's ears press back for a moment, then slowly rise again, and his breathing slows.
Walk-and-talk: the two walk side by side down a corridor, the camera retreating smoothly directly ahead of them and holding a two-shot medium throughout; light from the wall lamps sweeps across their faces and fur from both sides in turn.
Motivated low-key light: light comes only from the oil lamp in frame and moonlight outside the window, the room dark overall; one side of the face has a warm highlight, the other falls into shadow, with outline and fur texture still readable in the dark areas.
End-of-episode hook: the last shot is a close-up of Kael's face; both ears snap toward the door and the picture freezes for about 1 second; the only sound left is <wind outside the window>.
```

## 5. Film

A film is controlled by one director across the whole work and cares about the whole: the rhythm arc, the progression of focal lengths, one palette throughout [multi-source]. Contemporary films do not cut slowly. The difference is that each shot conveys one thing, camera movement has a motive, and the tightest framing is saved for the turn [multi-source]. Paste-ready phrases follow the table.

| Dimension | Convention, and how it applies to Seedance | Basis |
|---|---|---|
| Aspect ratio and composition | Big films mostly use 2.39:1 widescreen (over two thirds of the US top 100 from 1996–2015); intimate realistic dramas often use 1.85:1. Wide frames have spare room at left and right, filled three ways: balance a single figure against background set dressing; put the subject dead centre; or let the other character fill that side in the next reverse shot. Little headroom. Marks of anamorphic lenses: horizontally stretched flares, vertically oval bokeh, straight lines bowing slightly at the edges | [multi-source]; two thirds [single source] |
| Framing mix | Open on a long or extreme long shot for place, time, and characters, then move closer step by step; spectacle has more long shots, intimate drama more close-ups. Staging in depth: one thing each in foreground, middle ground, and background, shifting emphasis by blocking, often ending with the character closer to the camera than at the start. Shallow depth of field leads the eye to one face or one object; when two planes both matter, rack focus within the shot | [multi-source] |
| Rhythm and shot length | Contemporary average about 4.3 s per shot, and 2–4 s is common; each shot conveys one piece of information: a look, a gesture, or an object. The whole film has a rhythm arc: long shots with little movement in the setup, a darker picture in the middle, the shortest and brightest shots at the start of the climax, longer and quieter shots again at the end. The counter-trend is the showpiece long take | [multi-source]; rhythm arc [single source] |
| Camera movement | Moves only with a motive, starting and stopping with it: a slow push on a realisation, a rise to reveal scale or to close, a stabiliser following someone walking; a camera that drifts all the time reads as decoration. Two extremes of focal length: wide and close to exaggerate the foreground, long for singles and over-the-shoulders, flattening space. As tension rises the lenses get longer and the camera lower; the release gets the widest view in the film | [multi-source]; lens and height progression [single source] |
| Dialogue coverage | Two kinds: standing singles and over-the-shoulder shot/reverse shot; or walk-and-talk with the camera retreating directly ahead. Establishing shots are brief, so screen direction and eyelines keep strictly to the 180-degree rule. Behaviour, faces, and hands tell the story; lines are few | [multi-source] |
| Fights | Two grammars: the "impressionistic" one, handheld and chaotic, about 2 s a shot, cutting away before the action settles; and the "legible" one, where every shot can be read: enough long shots to keep bearings, pause–exchange–pause, a centred subject, so even 2 s cuts read clearly → use the legible one for Seedance | [multi-source]; the choice [inference] |
| Close-ups | The tightest framing is kept for the turning point, with medium shots and over-the-shoulders before it; close-ups are shorter than wide shots, and the cleaner the background the faster they read | [multi-source] |
| Transitions | About 99% hard cuts; match on action, graphic match, and sound leading or trailing the cut (J and L cuts) hide the cut or join meaning; cross-cutting speeds up as lines converge; montage compresses time. Choose the cut by emotion first (the six criteria of editing: emotion 51%, story 23%, rhythm 10%, eye trace 7%, two-dimensional plane 5%, three-dimensional space 4%), with the viewer's eye in the same region of the frame on both sides of the cut | [multi-source]; 99% and the six criteria [single source] |
| Light and colour | Light appears to come from windows, lamps, and signs in frame; low-key and high-contrast, shaping faces with shadow; one palette throughout, commonly teal-blue shadows with warm skin and fur. Hollywood pictures have been getting darker for decades | [multi-source]; darker [single source] |
| Sound | Few, clear layers with dialogue first: at most about 5 layers per 5 seconds or so; subjective sound (suddenly muffled, ringing ears) for impact; well-handled silence is powerful | Layers [single source]; the rest [multi-source] |

```text
Widescreen composition: Wachhund stands at the left third of the frame, the right side left open to plains and ridgelines running into the distance, with very little headroom.
Staging in depth: within one static shot, the foreground is Kael's blurred shoulders and red scarf, Gerard stands speaking in the middle ground, and in the background the wooden door is pushed open and a bear waiter walks in with a tray; then Gerard walks toward the camera, going from medium to close shot, all in one continuous shot.
Motivated movement: as Gerard stands, the camera rises slowly with him; he stops and the camera settles with him; the moment he understands the line, the camera pushes in very slowly to a face close-up and stays still once it arrives.
A close-up saved for the turn: every earlier shot is a medium or over-the-shoulder; only this shot cuts for the first time to a big face close-up, brow to jaw in frame, the background blurred clean, held for about 2 seconds.
Behaviour in place of lines: this shot has only action and ambience: Kael slowly sets down the cup, claw tips tightening on the rim, eyes moving to the window. Ends with: his hand resting by the cup, both ears toward the window.
Low-key light and one palette: the only light source is the window on screen right; cold white moonlight lights half the face and draws a rim along the fur while the other half falls into deep shadow; shadows lean teal-blue, fur leans warm gold, with fine film grain.
```

Fine devices such as rack focus, lens progression, anamorphic flares, and sound leading the cut may be beyond the model. Test them on their own at 480p before relying on them [inference].

## 6. The three example lines: default shot grammar

Platform settings: realistic line 16:9, cel-shaded and hand-painted fantasy lines 21:9, all 30 seconds with audio on, 480p draft first [author-tested]. Aspect ratio, duration, resolution, and audio switch go in platform settings only, never in the prompt [official]. Convey width through composition (which side the character is on, what fills the other side); do not write ratio numbers or "black bars top and bottom" [inference: bars eat picture]. A wide frame with detailed background art "holds" [single source], so shots can run a little longer than 16:9 TV anime [inference].

### 6.1 Realistic line: hyper-real film + TV-style dialogue + first person

| Item | Default | Basis |
|---|---|---|
| Structure | Dialogue in 7 hard-cut shots (6–8). One takes only for passages where "I" move through space, compressed to 3–4 segments, each opening with "The camera keeps moving and…" | Section 7; test run |
| Rhythm template | Establish 2–3 s → single close shots following the lines, 3–5 s each → listener reaction + slow push → close-up on the turning line, 4–5 s → settle to a held ending | The TV scene compressed to 30 s [inference] |
| Framing | Chest-up close shots for speech (the author uses 50–65mm, writing "the character reads as three-dimensional, the background moderately blurred" with it), pulling back to medium afterwards; the tightest close-up in the clip goes only to the turning line | Author-tested; a focal length only supplements the visible result [official]; film [multi-source] |
| Camera movement | Camera steady during lines; movement follows motive only: I turn my head → pan, someone stands → rise, a line sinks in → slow push | TV drama, film [multi-source] |
| Light and colour | Light comes from sources visible in the scene, with the off-screen side stated; opening a door or lighting a lamp changes the light along the way; one palette throughout: cool shadows, warm lamplight and fur | Film [multi-source]; author-tested |
| Sound | Dialogue clearest, 1–2 kinds of ambience written to the last second; default "The only sounds are ambience, action sounds, and dialogue" | Film [single source]; author-tested |
| Ending | One of two: a TV-style hook (a reaction close-up frozen for about 1 s), or a film-style long hold (last shot 4 s or more) | TV drama [multi-source]; film [single source] |

| Third-person wording | First-person rewrite |
|---|---|
| Establishing wide shot | The wide view I see as I walk in or sit down, at the height of my eyeline |
| Over the shoulder | The foreground becomes what is in front of me: table edge, cup, chessboard, railing, blurred |
| Shot/reverse shot | A shift of gaze: the camera pans from one person to the other, as if I turn my head; or a plain hard cut |
| Where the speaker looks | Straight into the camera when speaking to me; toward screen left or right when speaking to someone else, the same direction for the same person throughout |
| The axis | Each person's position relative to me is fixed throughout, anchored to the table, door, or window |
| When I speak | Me (off-screen, Japanese, voice as in @Audio N, emotion, to whom): {…}; the people in frame listen quietly with mouths closed |
| My hands | In frame only when needed, hands and sleeves as in the reference; with no reference, show only what I see |

Basis: "first person" is in the official 2.5 camera vocabulary [official]; the row-by-row rewrite is [inference], consistent with `kemono-jp-drama.md` 3.1. Give every character in frame a species and "I am the only human" follows naturally (generic figures get drawn as human, [author-tested]).

### 6.2 Cel-shaded line: 3D cel shading + anime rhythm

| Item | Default | Basis |
|---|---|---|
| Style line | First, in every clip: 3D-modelled, coloured in 2D cel style (flat colour + one hard-edged shadow layer + a few highlights), clean outlines, backgrounds like detailed hand painting. When references lean realistic, convert them to the same style with GPT Image first | Cel [multi-source]; an unclear style drifts to realism [official 2.0] |
| Structure | 9 hard-cut shots (8–10): 3–4 s per line, 2 s emotional close-ups, plus one 2–3 s "ma" cutaway | TV anime [inference]; the official 30 s example is also 9 shots [official] |
| Wide frame | Side-on lateral tracking for two characters abreast; a single character on one side with scenery on the other; in shot/reverse shot each takes one side of the frame | Film widescreen [multi-source] |
| Framing | Mostly alternating single close shots, two-shot mediums only to establish positions; scenery goes to long-shot cutaways | Anime [inference] |
| Camera movement | A 3D scene can do orbits and follows with true perspective, but one main move per segment; still passages use layered parallax tracking | Anime [multi-source]; one move per segment [official] |
| Dialogue | Rolf's face is a rigid visor: his lines play with his back to camera, off-screen, or over the listener's close shot; only Magnus's key lines get a frontal or three-quarter close shot | Anime hiding the mouth [multi-source]; the visor [inference] |
| Light and colour | Shift the whole palette by time of day (orange-violet at dusk); state the off-screen side of the light | [multi-source]; author-tested |
| Sound | About 1 s of ambience only before a key line; action sound effects can be more exaggerated than in a realistic film | [multi-source] |

### 6.3 Hand-painted fantasy line: hand-painted western fantasy + animated-film rhythm

| Item | Default | Basis |
|---|---|---|
| Style line | The line from fragment one in `combat-closeups.md` (fine ink line, pale washes, hand-painted backgrounds, warm golden slanting sun and light shafts, dark near, bright middle, pale violet-blue far), copied unchanged into every clip | Author-tested |
| Structure | Narrative in 6 shots (5–7); fights follow `combat-closeups.md` section 9 | Animated film at about 4 s per shot [inference] |
| Rhythm arc | A 5–6 s opening shot → 3–5 s in the middle → one short climax → a last shot of 5 s or more, held | Film rhythm arc [single source]; compressed to 30 s [inference] |
| Framing and depth | Extreme long shots for fantasy settings, letting the environment tell the story; use the style's three layers "dark near, bright middle, pale violet-blue far" for staging in depth: the character walks from the bright middle ground into the dark foreground | Film [multi-source]; author-tested |
| Camera movement | Layered parallax tracking (foreground foliage, middle-ground character, distant mountains); motivated moves such as a slow push or a rise; one rack focus at most | Anime, film [multi-source]; the count [inference] |
| Dialogue | Film style: mostly mediums and over-the-shoulders, few lines, hands and eyelines telling the story; the tightest close-up saved for the turn | Film [multi-source] |
| Transitions | At most one "freeze into a more detailed illustration" per clip, held about 1 s, at the peak of emotion or action | Anime [multi-source]; the count [inference] |
| Sound | Dialogue + 1–2 kinds of ambience; for music, write genre and start and end seconds in () | Symbols [official]; film [single source] |

## 7. How many shots in 30 seconds

| Style and passage | Shots (default) | Length per shot | Basis |
|---|---|---|---|
| Arithmetic baseline | 30 s ÷ average shot length: classic film at 10.5 s gives about 3 shots, contemporary film at 4.3 s about 7, TV anime at 3–4 s 8–10, TV drama at 3–5 s 6–10, action film at 2 s about 15 | — | [inference] |
| Realistic line, dialogue | 6–8 (7) | Opening 2–3 s; lines 3–5 s; turning close-up 4–5 s | TV drama + film [inference] |
| Realistic line, one take | 1 shot, 3–4 segments | 7–10 s per segment | Test run |
| Realistic line, fight | 9 (6 for safety) | 2–4 s | `combat-closeups.md` section 9 |
| Cel-shaded line, everyday and dialogue | 8–10 (9) | Lines 3–4 s; close-ups 2 s; ma 2–3 s | TV anime [inference]; official 9 shots [official] |
| Cel-shaded line, action | 9–10 | 2–3 s; 1–2 s in the burst, at most 3 such shots in a row | Anime [multi-source]; the cap [inference] |
| Hand-painted fantasy line, narrative | 5–7 (6) | Opening 5–6 s; middle 3–5 s; ending 5 s or more | Animated film + film [inference] |
| Hand-painted fantasy line, fight | 9 (6 for safety) | 2–4 s | `combat-closeups.md` section 9 |

- Place the lines first: each Japanese line takes morae ÷ 5–6 plus about 1 second, which gives the minimum length of its shot (conversion in `kemono-jp-drama.md` 2.3) [inference]. The remaining seconds go to reactions, cutaways, and action.
- A 1 second shot holds one visible change. A 1–2 second shot carries at most one very short line [official].
- Shot count follows events: when events are too dense, drop shots instead of subdividing [official sd25-pe]. Every extra shot is one more chance of an error or a changed face [inference]. This skill's default of 5–9 shots covers the defaults of all three lines [author-tested].
- The middle (about 12–20 s) is where repetition and drift happen most; give it one definite change and one definite camera move [single source, see SKILL.md].

## 8. Complete examples for the three lines

Plots, settings, and sample lines in the three examples are for demonstration; replace them with your own script. 「……もう一回。」 and 「……これは命令だ。」 come from the example cast's profiles. Character appearance is written only as far as the profiles record it; the rest is left to the references.

### 8.1 Realistic line, first-person dialogue (8 shots)

Demonstrates: a subjective establishing view, single close shots looking into the camera, a shift of gaze in place of shot/reverse shot, a listener reaction, the tightest close-up saved for the turn, a change of light when a door opens. Assets uploaded in order of first appearance: @Image1 and @Image2 Seren, @Image3 and @Image4 Kael, @Image5 the room, @Audio1 Seren's voice, @Audio2 Kael's voice. Platform settings: 16:9, 30 seconds, audio on; 480p draft first, 720p once it looks right.

```text
Style: Hyper-real cinematic picture in first person: the camera is my eyes (I am a human), at the height of my eyeline seated at the table. Fur and scales have realistic layering; ears, ear fins, and fabric move naturally with each action. The picture is clean cinematic footage.
References:
@Image1 (Seren, head): use only Seren's scale colours, blue eyes, silver-white horned crown, and pink ear fins.
@Image2 (Seren, full body): use only Seren's clothing and body proportions.
@Image3 (Kael, head): use only Kael's black head fur, amber eyes, ear shape, and muzzle length.
@Image4 (Kael, full body): use only Kael's clothing, red scarf, and body proportions.
@Image5 (room): use only the layout of the inn room and the positions and materials of the small wooden table, window, and door.
Characters: Only two characters appear in frame, Seren and Kael, each exactly once; I exist only as the camera.
Seren: dragon anthro prince, silver-white and blue scales, blue eyes; the traits only he has: pink ear fins and a silver-white horned crown. Appearance, build, and apparent age as in @Image1 and @Image2; speaks with the voice of @Audio1, which provides only timbre, pace, and tone.
Kael: black wolf anthro, adult male, a complete wolf head with a long muzzle, black fur over the whole body, upright on two legs, canine paw-hands (four fingers and a thumb); the trait only he has: a red scarf. Appearance as in @Image3 and @Image4; speaks with the voice of @Audio2, which provides only timbre, pace, and tone.
Scene layout: A small room on the upper floor of an inn. I sit at one end of a small wooden table, the window on my left with an oil lamp on its sill; Seren sits across the table facing me; the door is on my right. A wooden chessboard lies open on the table. Once Kael appears he stays standing in the doorway.
Light: The key light is the oil lamp on the sill, warm yellow from screen left onto Seren's face and ear fins; once the door opens, cold white light from the corridor falls from screen right onto Kael and draws a thin bright rim along his ears and red scarf.
Sound: The only sounds are ambience, action sounds, and the two characters' Japanese dialogue. Voices are clean and clear; generate audio strictly from the line text, spoken word for word to the end. There are three lines in the whole clip, and only one person speaks in any time range.
Shots:
Shot 1 (0–3 s): Subjective medium shot, static. Seren sits across the chessboard staring at it, mouth closed; the blurred table edge and a few pieces are in the foreground. Ends with: Seren raising his eyes to me.
Shot 2 (3–7 s): Hard cut, Seren chest-up in close shot, looking straight into the camera, camera steady, the character three-dimensional and the background moderately blurred. His pink ear fins slowly droop against the sides of his face; his mouth opens and closes with each syllable as he speaks. Seren (Japanese, the bright young male voice of @Audio1, quiet after a setback, to me): {……もう一回。} Ends with: Seren's mouth closed, still looking at me.
Shot 3 (7–10 s): Hard cut, subjective view, the camera slowly tilts down to the chessboard as if I look down: only a few pieces remain, lamplight wavering on them. Ends with: the camera resting on the board.
Shot 4 (10–13 s): Hard cut, subjective medium shot. <the creak of a door being pushed open> The camera pans right from Seren to the doorway, as if I turn my head: Kael stands in the door frame with cold corridor light on him; both keep their mouths closed. Ends with: Kael in the centre of the frame.
Shot 5 (13–17 s): Hard cut, Kael chest-up in close shot, three-quarter profile looking toward Seren on screen left, camera steady. Before he speaks both ears press back once; his muzzle and lower jaw open and close with each syllable. Kael (Japanese, the low male voice in a cold big-brother manner of @Audio2, flat, to Seren): {もう寝ろ。} Seren, off-screen, listens quietly with his mouth closed. Ends with: Kael's mouth closed, ears upright again.
Shot 6 (17–20 s): Hard cut, Seren in close shot, static. He looks at Kael on screen right, then brings his eyes back to me, ear fins lifting halfway and dropping again; mouth closed. Ends with: Seren's eyes resting on my face.
Shot 7 (20–24 s): Hard cut, a close-up of Kael's face, the tightest framing in the clip, brow to jaw in frame, static. His eyes are on Seren at screen left, ears slowly relaxing outward; his muzzle and lower jaw open and close with each syllable. Kael (Japanese, the low male voice in a cold big-brother manner of @Audio2, quiet but forceful, to Seren): {……これは命令だ。} Seren, off-screen, listens quietly with his mouth closed. Ends with: Kael's mouth closed.
Shot 8 (24–30 s): Hard cut, subjective medium shot. Kael turns and walks into the corridor, the door closing softly behind him as the cold light narrows to a thin line and disappears <a door closing softly>; the camera then pans left back to Seren: he holds the closed chessboard in both arms, ear fins slowly rising, looking at me. Ends with: only the lamp's warm light in the room, the frame holding steady for about 2 seconds.
Ambience: 0–30 s: <the faint crackle of the oil lamp flame> and <distant wind outside the window> continue to the last second.
```

### 8.2 Cel-shaded line (9 shots)

Demonstrates: a style line locking the style, layered parallax tracking, side-on tracking in a wide frame, alternating single close shots, a ma cutaway, a visored character's line played off-screen. With no motorcycle reference, delete @Image5 and state the motorcycles' colours. Platform settings: 21:9, 30 seconds, audio on; in the 480p draft, check above all whether the style has drifted to realism.

```text
Style: 3D cel-shaded animation: 3D-modelled characters, motorcycles, and setting, coloured in 2D cel style with flat colour areas, each with a single hard-edged shadow layer and a few highlights, outlines clean and even; backgrounds like detailed hand-painted art. The picture has a soft glow, with thin beams in the slanting sun. The picture is clean animated footage.
References:
@Image1 (Magnus, head): use only Magnus's head fur colour, eyes, and face shape.
@Image2 (Magnus, full body): use only Magnus's biker outfit and body proportions.
@Image3 (Rolf, head): use only Rolf's rigid visor and head.
@Image4 (Rolf, full body): use only Rolf's clothing and body proportions.
@Image5 (motorcycles): use only the look and colours of the two motorcycles.
Characters: The whole clip has only two characters, Magnus and Rolf, and each appears exactly once in frame.
Magnus: lion anthro, upright on two legs, clawed beast hands with the finger count as in the reference; the trait only he has: a biker outfit. Appearance as in @Image1 and @Image2; speaks with the voice of @Audio1, which provides only timbre, pace, and tone.
Rolf: an upright anthro, species and appearance as in @Image3 and @Image4; the trait only he has: his face is one rigid visor. Speaks with the voice of @Audio2, which provides only timbre, pace, and tone.
Scene layout: A mountain road at dusk, with a lookout with a stone railing on the outside of a bend. Magnus is always on screen left, Rolf always on screen right; the two motorcycles travel from screen left to screen right.
Light: The setting sun hangs low above the far mountains directly ahead of the lookout, drawing a warm orange rim along both characters' outlines; the sky grades from orange to violet.
Sound: The only sounds are ambience, action sounds, and the two characters' Japanese dialogue. There are two lines in the whole clip, and only one person speaks in any time range.
Shots:
Shot 1 (0–3 s): Extreme long shot, an empty view of ridgeline, road, and sunset clouds. The camera pans slowly right, the foreground railing, the middle-ground road, and the distant ridges and clouds travelling as three layers, the foreground fastest and the distance slowest; two motorcycles enter far off from screen left, very small. Ends with: the two motorcycles reaching the centre of the frame.
Shot 2 (3–6 s): Hard cut, side-on medium shot, the camera moving right parallel to Magnus. He rides, the fur on his neck and the hem of his biker outfit blown back by the wind. Ends with: Magnus glancing toward screen right.
Shot 3 (6–9 s): Hard cut, side-on medium shot, the camera moving right parallel to Rolf; a streak of sunlight slides across his visor. Ends with: Rolf's motorcycle slowing.
Shot 4 (9–13 s): Hard cut, two-shot medium, static. The two park at the lookout's stone railing <engines cutting out>, get off, and stand side by side at the railing, Magnus on the left and Rolf on the right, looking at the far mountains. Ends with: both standing facing the mountains, mouths closed.
Shot 5 (13–17 s): Hard cut, Magnus in close shot, three-quarter profile looking toward screen right, camera steady. His mouth opens and closes with each syllable as he speaks. Magnus (Japanese, voice as in @Audio1, relaxed, to Rolf): {……いい風だな。} Rolf, off-screen, listens quietly. Ends with: Magnus's mouth closed, eyes narrowing.
Shot 6 (17–19 s): Hard cut, Rolf in close shot, three-quarter side view, static. His visor faces the far mountains and his shoulders slowly loosen with one long exhale. Ends with: Rolf standing quietly.
Shot 7 (19–22 s): Hard cut, an empty shot of only the setting sun, clouds, and far mountains, static, the clouds drifting slowly; both characters are off-screen. Ends with: the lower edge of the sun touching the ridgeline.
Shot 8 (22–26 s): Hard cut, Magnus in close shot, static, listening quietly with his mouth closed, both ears turned toward screen right. Rolf (off-screen, Japanese, voice as in @Audio2, calm, to Magnus): {……ああ。} Ends with: the corners of Magnus's mouth relaxing, eyes returning to the mountains.
Shot 9 (26–30 s): Hard cut, extreme long shot of the two from behind, static: two figures side by side at the railing, the two motorcycles parked nearby, the sun sinking behind the ridge and the sky turning violet. Ends with: the frame holding steady for about 3 seconds.
Ambience: 0–30 s: <wind passing over the railing> continues to the last second; 0–11 s: <the even engine note of two motorcycles>.
```

### 8.3 Hand-painted fantasy line, narrative without dialogue (6 shots)

Demonstrates: the rhythm arc (long opening → middle → one burst → long hold), layered parallax, staging in depth, a motivated slow push, the only freeze-into-painting in the clip, behaviour in place of lines. Platform settings: 21:9, 30 seconds, audio on; test the freeze shot on its own at 480p first.

```text
Style: Hand-painted western fantasy illustration: fine ink outlines, pale colour washes, backgrounds like the background paintings of a hand-drawn animated film; warm golden slanting sun and shafts of light, dark in the near ground, brightest in the middle distance, pale violet-blue far away. The picture is clean illustrated footage.
References: @Image1 "German shepherd": use only Wachhund's face, fur colours, and clothing. @Image2 "longsword": use only the longsword's shape, length, and colour. @Image3 "courtyard": use only the layout of the flagstone courtyard, the stone well, and the light.
Characters: The whole clip has only one character, Wachhund. Wachhund: German shepherd anthro, black-masked face, amber eyes; cream linen shirt, silver pauldron, grey-blue cape; canine paw-hands (four fingers and a thumb); appearance and build as in @Image1. The longsword is as in @Image2, the only one in the clip, its blade straight and rigid, always in his right hand.
Scene and light: A flagstone courtyard with a stone well at its centre; the slanting sun is off-screen back left, shafts of light falling into the courtyard from upper left.
Sound: The only sounds are ambience and action sounds; Wachhund keeps his mouth closed throughout, with only the sound of breathing.
Shot 1 (0–6 s): Extreme long shot, the camera tracking slowly right: dark foreground foliage, the sunlit courtyard in the middle ground, and pale violet-blue mountains in the distance travel as three layers, the foreground fastest and the distance slowest. Wachhund stands by the well with his back to camera, sword in his right hand, its tip angled at the flagstones, the hem of the grey-blue cape moving in the wind. Ends with: Wachhund at the left third of the frame, open distant mountains on the right.
Shot 2 (6–10 s): Hard cut, medium shot, static, with staging in depth inside the one shot: Wachhund turns and walks step by step from the bright middle ground toward the camera, leaving the shaft of light for the dark foreground and becoming a close shot. Ends with: he stops in front of the camera, amber eyes looking toward screen right.
Shot 3 (10–13 s): Hard cut, hand close-up, eye level, static. The canine paw-hand tightens on the hilt, claw tips drawn in against it, the knuckles tightening slowly one by one. Ends with: the hand steady on the hilt.
Shot 4 (13–18 s): Hard cut, close shot. At the moment he raises his eyes to the distance, the camera pushes in very slowly to a face close-up and settles, the light shafts behind dissolving into soft golden bokeh. Ends with: the close-up holding, eyes sharp.
Shot 5 (18–23 s): Hard cut, wide side view, static. Wachhund grips the sword in both hands and swings one cut from lower left to upper right, several thin ink lines trailing the blade <the whistle of a blade cutting air>; at the instant the sword stops at its highest point the picture freezes into an illustration with finer brushwork, the corners darkening while the centre keeps normal brightness, held about 1 second before motion resumes. Ends with: the sword tip angled at the sky, the cape slowly settling.
Shot 6 (23–30 s): Hard cut, extreme long shot, the camera slowly rising to look down. Wachhund lowers the sword, its tip toward the flagstones, and stands at the centre of the courtyard; shafts of light slant down from upper left, and the distant mountains are pale violet-blue. Ends with: the frame holding steady on the high wide view for about 3 seconds.
Ambience: 0–30 s: <wind through the courtyard and leaves scraping the flagstones> continues to the last second.
```

## 9. Common deviations

| Symptom | Change this first |
|---|---|
| More shots than written, or a one-take cut at a segment boundary | Open each segment with "The camera keeps moving and…", write the camera's path; drop to 3 segments [test run] |
| Cel-shaded or hand-painted turns realistic or looks like a 3D render | Style line first, in every clip; convert references to the target style first [official 2.0] |
| Cutting too fine, faces changing, costumes jumping | Return to the default shot counts in section 7 and merge minor shots [inference] |
| A line does not finish inside a 1–2 s shot | Move it to a shot long enough (morae ÷ 5–6 + 1 s) [inference] |
| The sides of a wide frame are empty | Use the three fills in section 5: balance character against set, centre the subject, or let the next reverse shot fill the other side [multi-source] |
| Freezes and flashes everywhere | Write "the only freeze in the clip", at most 1–2 per clip; flashes no more than 3 a second [single source, primary document] |
| "My" body or another human appears in first person | Write "I exist only as the camera"; give every character in frame a species [author-tested] |
| No film feel | Write light position, depth of field, a unified palette, and motivated movement; do not rely on adding black bars [inference] |

## 10. Sources

Researched 2026-10-28. The figures and the conventions of the three media come from a dedicated study of shot arrangement; the Seedance wording comes from official docs and the anthro study. A few pages (TV Tropes, Artforum) could not be opened directly and are cited from search summaries.

Official:
- [official] Volcengine Ark, Seedance 2.5 prompt guide (integer-second timestamps, the 30 s 9 shot example, the 13 s 8 shot dialogue example, "first person" as a camera term): https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide
- [official] Volcengine Ark, Seedance 2.0 prompt guide (one move per shot, 2D/3D styles drifting to realism): https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-0-prompt-guide ; https://docs.volcengine.com/docs/82379/2222480
- [official] sd25-pe skill 0.1.1 (parameter separation, time ranges as event budget, fewer ranges when events are dense, the camera-move formula, photographic terms written as visible results, vignette wording, listening with mouths closed): https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip
- [official] Pippit, Seedance 2.5 handbook (30 s in 4–6 parts): https://www.xiaoyunque.com/tutorials/seedance-2-5

Anime:
- [multi-source] Shot counts, rhythm, ma, hidden mouths in dialogue: https://cgworld.jp/interview/201709-chronosruler-3.html ; https://animeanime.jp/article/2015/09/18/24952_2.html ; https://journals.sagepub.com/doi/10.1177/1746847713487472 ; https://gigazine.net/gsc_news/en/20191228-eizouken-mari-motohashi-interview ; https://nofilmschool.com/2013/09/master-of-ma-director-hayao-miyazaki-set-to-retire ; https://news.mynavi.jp/techplus/article/kurieita-22/ ; https://animenation.net/blog/?p=12849 ; https://realsound.jp/movie/2016/09/post-2808.html ; https://cgworld.jp/terms/%E3%82%A2%E3%83%95%E3%83%AC%E3%82%B3.html
- [multi-source] Limited animation, sliding layers, composition: https://cgworld.jp/terms/%E3%83%AA%E3%83%9F%E3%83%86%E3%83%83%E3%83%89%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3.html ; https://gwern.net/doc/anime/2015-chang.pdf ; https://www.mechademia.net/2012/08/22/book-review-the-anime-machine/ ; https://janica.jp/course/perspective/history04_handout.pdf ; https://history.siggraph.org/?p=141604 ; https://www.clipstudio.net/oekaki/archives/152740 ; [single source] manga panel statistics: https://pmc.ncbi.nlm.nih.gov/articles/PMC3449338/
- [multi-source] Fights, impact frames, orbits, replays: https://animetudes.com/2021/07/09/the-kanada-style-now/ ; https://www.sakugabooru.com/wiki/show?title=impact_frames ; https://www.sakugabooru.com/wiki/show?title=background_animation ; https://cgworld.jp/article/202203-jujutsukaisen.html ; https://tvtropes.org/pmwiki/pmwiki.php/Main/RepeatCut ; [single source, primary document] https://www.tcnet.ne.jp/wp-content/uploads/community_ch/broadcasting-plan-standard/standard_Exhibit.pdf
- [multi-source] Freezing into a painting, split screen, abstract backgrounds, cel, compositing, sound: https://anime.eiga.com/news/column/hikawa_rekishi/111098/ ; https://en.wikipedia.org/wiki/Osamu_Dezaki ; https://www.japanesewithanime.com/2020/04/background-effects.html ; https://ja.wikipedia.org/wiki/漫符 ; https://realsound.jp/movie/2020/12/post-677025.html ; https://realsound.jp/movie/2020/12/post-677025_4.html ; https://cgworld.jp/article/202303-chainsawman3.html ; https://www.mhlw.go.jp/content/11901000/001152417.pdf ; https://realsound.jp/book/2025/03/post-1958046.html
- [multi-source] Anthro performance: https://animeanime.jp/article/2019/10/30/49323_2.html ; https://www.scrmbl.com/post/studio-orange-beastars-interview ; [single source] manes: https://scrmbl.com/post/yusuke-yoshigaki-bna-interview . Theatrical versus TV: [multi-source] https://toyokeizai.net/articles/-/384527 ; [single source] about 1,800 shots: https://news.mynavi.jp/techplus/article/20100511-ibaradezi/ ; [single source] a widescreen sequel: https://press.moviewalker.jp/news/article/1064939/p2/

TV drama:
- [single source, one study each] Shot length, framing, scene length: https://arxiv.org/abs/2002.06923 ; https://www.koreascience.or.kr/article/CFKO200921553663688.pdf ; https://www.koreascience.or.kr/article/JAKO201532434263732.pdf ; https://anthology.ach.org/volumes/vol0003/sitcom-form-function-pacing-production-in-of-u-s/10.63744@yHo626es4FhQ.pdf
- [multi-source] Dialogue coverage, reaction shots, walk-and-talk, aspect ratio: https://faculty.salisbury.edu/~axsharma/MyWebs/EFP/gramtv.html ; https://www.davidbordwell.net/blog/2007/05/27/intensified-continuity-revisited/ ; https://en.wikipedia.org/wiki/Reaction_shot ; https://en.wikipedia.org/wiki/Walk_and_talk ; https://acmag.com.au/2017/12/01/cross-shooting-techniques-with-russell-bacon-acs/ ; https://www.tvbeurope.com/production-post/at-least-10-takes-per-episode-and-that-drone-shot-netflix-reveals-secrets-to-adolescence ; https://en.wikipedia.org/wiki/Univisium ; https://www.newsshooter.com/2019/10/14/netflix-updates-its-cameras-and-image-capture-list/ ; https://www.chinawriter.com.cn/n1/2026/0709/c419388-40756435.html ; https://www.woshipm.com/share/6022557.html
- [multi-source] Push-ins, close-ups, light and depth of field, flashbacks, episode endings, theme songs: https://www.panavision.com/highlights/highlights-detail/5-ways-one-camera-move-can-be-used-to-different-effect ; https://www.arri.com/news-en/alexa-in-south-korea ; https://m.gmw.cn/toutiao/2026-04/08/content_38692781.htm ; https://www.fdtimes.com/pdfs/japanese/116FDTJ-4.01-221102.pdf ; https://www.mentalfloss.com/entertainment/tv/inside-lighting-design-makes-all-sitcoms-look-same ; https://nofilmschool.com/why-movies-and-tv-are-dark ; https://series.unibo.it/article/download/9161/10214 ; https://seoulbeats.com/2014/03/k-drama-formula-part-one-pilot-episode/ ; https://www.wgfoundation.org/blog/2021/11/17/serialized-drama ; https://realsound.jp/movie/2021/06/post-797647_2.html ; https://toyokeizai.net/articles/-/421384 ; [single source] the hook in the first 3 seconds: https://c.m.163.com/news/a/L30RCS1005340TH8.html

Film:
- [multi-source] Shot length and shot counts: https://pmc.ncbi.nlm.nih.gov/articles/PMC5256470/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3485803/ ; https://offscreen.com/view/shyamalan ; https://stephenfollows.com/many-shots-average-movie/ ; https://www.davidbordwell.net/blog/2007/08/17/unsteadicam-chronicles/ ; https://vashivisuals.com/the-fastest_cut/
- [multi-source] Aspect ratio and composition: https://stephenfollows.com/film-vs-digital/ ; https://www.davidbordwell.net/blog/2016/02/10/off-center-mad-maxs-headroom/ ; https://www.davidbordwell.net/blog/2014/03/26/the-grand-budapest-hotel-wes-anderson-takes-the-43-challenge/ ; https://filmdaft.com/a-beginners-guide-to-anamorphic-lenses/
- [multi-source] Framing, depth, close-ups, behaviour telling the story: https://cinemetrics.uchicago.edu/article/ae7c9433-9d9e-4ef0-bfe2-7a7b4f5b9042 ; https://www.davidbordwell.net/blog/?p=32808 ; https://www.davidbordwell.net/blog/2007/02/09/walk-the-talk/ ; https://news.cornell.edu/node/285439 ; https://www.davidbordwell.net/blog/2008/02/13/hands-and-faces-across-the-table/
- [multi-source] Camera movement, focal length, and fights: https://hazlitt.net/node/10611811 ; https://reframe.sussex.ac.uk/post-cinema/1-2-shaviro/ ; https://www.davidbordwell.net/blog/2008/12/28/a-glance-at-blows/ ; https://www.inverse.com/entertainment/55687-john-wick-chapter-3-director-interview-why-ballet-matters ; [single source] lens and height progression: https://slashfilm.com/793246/how-sidney-lumet-used-different-eye-levels-to-create-tension-in-12-angry-men
- [multi-source] Editing, transitions, light and colour: https://en.wikipedia.org/wiki/Match_cut ; https://en.wikipedia.org/wiki/J_cut ; https://en.wikipedia.org/wiki/Cross-cutting ; https://studiobinder.com/blog/what-is-motivated-lighting-in-film ; https://petapixel.com/2017/02/23/orange-teal-look-popular-hollywood/ ; [single source] the six criteria of editing: https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch ; [single source] sound layers and silence: https://transom.org/2005/walter-murch/

Author's material:
- [author-tested] Production notes (compiled 2026-10-28): aspect ratios and styles of the three lines, character table, 5–9 shots per clip, 50–65mm close shots, light written by off-screen position, generic figures drawn as humans, ambience written to the last second.
- [test run] One 30 second Seedance 2.5 generation on Jimeng on 2026-10-28: a one-take was hard cut once at second 7, on the boundary between two segments.
- [inference] The "shots in 30 seconds" figures, the defaults for the three lines, and the first-person rewrite in this file are all derived from the material above and have not been tested item by item on Seedance.
