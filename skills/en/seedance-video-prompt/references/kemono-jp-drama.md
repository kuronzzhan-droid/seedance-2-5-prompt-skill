# Japanese dialogue scenes for anthro characters in Seedance 2.5

## When to read this file

Read it when shooting dialogue, monologue, or quiet character scenes with anthro characters who speak Japanese, or when fitting Japanese lines into a 30 second shot list. It covers four things SKILL.md does not go into: keeping an anthro on model, writing and timing Japanese lines, shooting shot/reverse shot and reaction shots inside one generation, and suppressing subtitles. For anthro shots with no dialogue (fights included), only section 1 applies.

Evidence tags: **official** = Volcengine Ark, Pippit, or ByteDance Seed documentation and technical reports, or the official sd25-pe skill; **multi-source**; **single source**; **inference** = derived from the material, not tested; **author-tested** = the author's own failure log; **test run** = a single generation on Jimeng on 2026-10-28.

## Contents

1. Anthro on screen: character cards, drift prevention, telling look-alikes apart, fur, muzzle lip-sync, ear and tail acting
2. Japanese dialogue: format, voice and register, mora timing, kana rewriting, testing a short line first, voice references
3. Dialogue coverage inside one generation: shot/reverse shot and the axis, reaction and causality, ma, the dialogue ledger, first person
4. Subtitle prevention
5. Complete example: Kael × Gerard, 7 shots
6. Troubleshooting
7. Pre-delivery checklist
8. Sources

## 1. Anthro on screen

### 1.1 Character card: species as anatomy, plus one trait only he has

Write only "wolf anthro" and the model may return a human with animal ears, a green-skinned orc, or a real four-legged wolf (the ambiguity of the term is known; its effect on output is inference). The Japanese fandom's "kemono level" scale varies from person to person, so a bare level number is unreliable too (multi-source). So write the species as visible anatomy, leave build to the reference image, give each character one identifying trait nobody else has, and repeat it at every mention.

```text
Kael: black wolf anthro, adult male, a complete wolf head with a long muzzle, black fur over the whole body, upright on two legs, canine paw-hands (four fingers and a thumb); the trait only he has: a red scarf. Appearance and clothing follow @Image1 and @Image2.
```

| Character (example cast) | Trait only he has | Easily confused with |
|---|---|---|
| Kael (black wolf, amber eyes) | Red scarf; in the ship and deep-sea arcs, the gold bamboo-leaf pattern on a black high-collar outfit + a red sash | Gerard (also a wolf) |
| Gerard (white wolf knight, blue eyes) | The scar on his face (position as in the reference) + a blue-and-white cape | Kael |
| Seren (dragon prince with silver-white and blue scales, blue eyes) | Pink ear fins + a silver-white horned crown | Sil (author-tested: they have been mixed up) |
| Sil (blue-and-white ichthyosaur dragon) | The sea fork in his hand (when a prop is the trait, write him holding it in every shot) | Seren; his brother Sid (whose trait is a deep blue-violet body) |
| Varek (black panther) | Violet-blue crystals on the left forearm | Kern.V (also a black panther) |
| Kern.V (black panther, gold-green slit pupils) | A silver crescent tattoo (position as in the reference) | Varek |
| Kinovi (avian assassin) | A feather mantle + cold blue eyes (only the mysterious black crow has red eyes) | Other avian characters |
| Bobo (white-maned lion) | A house robe | Magnus (biker outfit), Zanni |

Reference images: every character on screen gets his own images attached to every clip. "Same as the previous segment" does not work (author-tested). The example character sheets put front, back, and head on one sheet; crop them to single views before feeding Seedance: one head, one full-body front, and a separate back view if needed. Official guidance says several views on one image are easily read as several different people (official). Downscaling references to no more than the output resolution reduces fingerprint-like texture (the official FAQ is about dense texture such as grass and leaves; applying it to fur is inference).

### 1.2 Stopping drift into beast or human

| Drift | Trigger | Positive wording |
|---|---|---|
| Becomes a real animal | Entering water, swimming (author-tested: Gunnar became a real orca in the water) | Gunnar keeps the anthro posture and clothing of @Image N in the water: torso upright, arms pulling through the water |
| Goes on all fours | "Half-squatting", "crouching" (author-tested) | On one knee, torso upright |
| Becomes human or a "human with animal ears" | Words like "animal ears, cat ears, kemonomimi" (multi-source) | A complete wolf head with a long muzzle, fur over the face, a moist black nose |
| Background figures become human | Only "passers-by" or "customers" (author-tested) | The tavern's customers are two bear sailors and a fox waiter |
| Teeth become human teeth | One reviewer saw a non-human character's teeth flip between human and non-human (single source, tested on a cyborg; applying it to anthros is inference) | Shows a wolf's canines when speaking |
| Eyes become human or glow | "Normal human eyes" (inference); strong emotion words such as "fanatical, utterly shocked" (official FAQ) | The eyes are the amber animal eyes of @Image1, with a soft catchlight |

### 1.3 Telling look-alike characters apart

- Carry the identifying trait at every mention: "the black wolf Kael (red scarf)", "the white wolf Gerard (blue-and-white cape)", and use only that one label throughout (official: define a subject by 2–3 stable traits, then keep using the same label). When designing new characters, separate species, fur colour, and the warmth of their clothing from the start; two different species are steadier than two of the same (inference).
- Keep them out of the same frame where possible. When they share one, state each position relative to a fixed object such as a table or door. To swap front and back, write the blocking (author-tested).
- Upload references in order of first appearance, bind one character per line, and put names in the prompt, not on the image (official).
- Lock the head count: "The whole clip has only two characters, Kael and Gerard, and each appears exactly once in frame" (a positive rewrite of the official anti-duplicate sentence).
- Mounts and riders get mixed up (author-tested): give dialogue to the rider only and write the mount as an ordinary animal: "Only the rider speaks; the mount is an ordinary horse with its mouth naturally closed, snorting now and then".

### 1.4 Fur and moving details

- Name which part of the fur moves, which way, and how it looks once it settles (single source, third party). Prefer slow, gentle, small movements (official 2.0).
- In 2.5, fur tends to be blown as one sheet, so write the fine tremble at the tips separately (single source + inference).
- State where the light is, for example "the light source is off-screen left". "Backlit" alone puts a halo over the head (author-tested).
- A white-maned lion's (Bobo's) large mane has an odd outline from a low angle; shoot level or slightly from above (single source: interview with an anthro animation character designer).
- For wet fur write "the fur is wet into separate strands and clings to the body" (inference). In the sound section, write only the rain you want. Official FAQ: water, waves, and echo in the prompt tend to produce bubbling and echo noise in the audio.

```text
A light breeze comes from off-screen left: the long fur on Kael's neck and the fine fur at his ear tips tremble with the wind, and the end of the red scarf sways slightly; when the wind stops, fur and scarf slowly settle.
```

### 1.5 Muzzle lip-sync for Japanese

There are no public tests of Seedance 2.5 lip-sync on anthro muzzles (none found in Chinese, Japanese, or English). The table below is transferable experience. Before a real shoot, make a 4–8 second lip-sync test clip (inference).

| Situation | Wording (placed before the line) | Basis |
|---|---|---|
| Every speaking shot | The muzzle and lower jaw open and close with each syllable while he speaks, and the mouth closes when he finishes | The official example says "lips and jaw sync precisely to every word"; applying it to a muzzle is inference |
| ま row (ma mi mu me mo) | The lips close clearly | Single source: interview with the CG director of an anthro 3DCG anime |
| ば and ぱ rows | The lips close as well | Inference (also bilabials) |
| Low voice, muttering | The muzzle opens only slightly | Single source (same interview) |
| Long-muzzled characters | Speak in three-quarter profile | Same interview: a long muzzle facing the camera looks too long and can hide the eyes |
| Camera | Medium close-up or tighter, the whole muzzle in frame, hands and cups below chest level, head steady while speaking | The official example asks fingers to stay clear of the mouth; the rest is third-party experience |
| Beaks (if an avian character has one) or a visor (Rolf) | Put key lines in voice-over, on a back view, or over the listener's reaction shot | Inference: a beak or visor cannot make closed-lip sounds |

Write lip-sync requirements before the line, as general description. Do not name a specific syllable of the line after it ("lips close on め"). The official FAQ says repeating words after a line with added notes tends to trigger subtitles. The speaking character's main reference should be a head image with a closed mouth and neutral expression (third party + inference).

### 1.6 Ears, tail, whiskers, and fur as acting

Write emotion as visible action, not "blushes" or "his eyes light up" (author-tested; official also asks for observable behaviour). Choose 2–3 details per emotional turn (official). Use the same ear or tail action at most twice in a clip (inference).

| Emotion | Ears | Tail | Muzzle, whiskers, fur, gaze |
|---|---|---|---|
| Alert | Both ears upright, turned to the sound | Tail tip stops | Whiskers forward, pupils widen |
| Holding back anger | Both ears pressed flat back | Tail rigid | Bridge of the nose wrinkles, canine tips show, hackles rise |
| Low, reluctant to part | Both ears droop outward | Tail hangs low near the legs | Gaze drops, whiskers droop |
| At ease | Both ears relaxed outward | Tail sways slowly side to side | Slow blink, long exhale, whiskers move with the breath |
| Awkward | One ear turns back | Tail tip flicks quickly in small movements | Gaze shifts away, a hand comes up to rub the back of the neck |

Basis: Wikipedia's cat and dog body-language articles plus anthro animation interviews (the ears turn to a sound first; a tail that never moves looks stiff, multi-source). The mapping to specific emotions is inference. Felines differ from canines: a fast tail lash in a feline mostly means irritation (inference).

Acting keys for the example cast (author-tested): Kael "gives his feelings away with his ears first", so write the ears before the line. Gerard "is all ears and tail, with wording that stays formal", so keep the line formal and leave the contrast to ears and tail. Kinovi "feather mantle puffing up = heartbeat". Write subtext as the contrast between the words and the body: in the same shot where Kinovi says 「別に。……温かいだけだ。」, the feathers of his mantle slowly fluff up (inference).

## 2. Japanese dialogue

### 2.1 Line format

```text
Kael (Japanese, a low male voice in a cold big-brother manner, flat, to Gerard): {もう休め。}
```

- Format: `Name (Japanese, voice, emotion, to whom): {Japanese text}`. The official recommendation is "Character line (emotion): text"; state the language before any non-Chinese line; label every speaker individually, since one declaration at the top is not enough (official). Prompt body in one language and dialogue in another is how the official examples are written (official).
- Write each line once, in the time range or shot where it happens. The Sound section gives only the line count. Hesitation and interruption go into the line as 「……」 and 「——」 (official example).
- One language per line (official 2.0). Use the original kanji and kana, not romaji (third party). Keep translations outside the prompt for your own reference; next to {} they may be spoken aloud or turned into subtitles (inference).
- For volume write "quiet but forceful", not "loudly", which raises pitch. Say character names rarely in lines: platforms may rewrite them, and they can trip copyright filters (author-tested).
- In the Sound section write "generate audio strictly from the line text, spoken word for word to the end" (a positive rewrite of the official constraint).

### 2.2 Voice cards and register

One fixed voice description per character, copied unchanged into every speaking shot, with the manner repeated each shot as well (multi-source, community). In one 10 shot test where only the voice quality was repeated, shots with gentle lines pulled the delivery soft (single source). Personality comes mostly from how the character speaks: first-person pronoun, level of politeness, and sentence endings written into the line itself (the idea of yakuwarigo, role language; inference). Kansai and other dialects have no public tests; accuracy takes several tries (inference).

| Character | Voice card (example cast) | Register, written into the line | Canonical line |
|---|---|---|---|
| Kael | A low male voice in a cold big-brother manner | Shows care in the tone of an order; the half-sentence after the order is the real feeling | 「……これは命令だ。」 |
| Gerard | A stiff, earnest middle-aged male voice | Archaic knightly speech (「承知した」「〜殿」), short sentences, formal wording; evolves by story stage, never skipping ahead | 「承知した。」 |
| Seren | A bright young male voice | Warm, clingy; quiet when thwarted | 「……もう一回。」 |
| Seris | Commanding and low | Brief, like passing judgement; does not praise, refills the cup instead | Per script |
| Kinovi | As in the voice reference | Cold | 「別に。……温かいだけだ。」 |

Voice descriptions can also be written in Japanese: low = 低い声, husky = ハスキー, deep and seasoned = 渋い声. There is no comparison test of which language works better (multi-source, community). With a voice reference, the voice card is only a supplement; see 2.6.

### 2.3 From speech rate to duration

Count Japanese in morae, not characters: each kana is 1 mora; a contracted sound (きゃ, しょ) counts as 1 with its preceding kana; っ, ん, and ー count 1 each; kanji count by their reading.

| Data | Value | Source |
|---|---|---|
| Read speech (ATR corpus) | 7.11 morae/s | NINJAL CSJ report |
| Spontaneous speech (CSJ) | 8.01 morae/s | Same |
| Native natural conversation | 7.55 morae/s | Nishi 2018 |
| Japanese read speech | 7.84 syllables/s (pauses over 150 ms removed) | Pellegrino et al. 2011 |
| Easiest for non-native listeners | 320–360 morae/min, about 5.3–6 morae/s | Prafiyanto et al. 2018 |
| Calm narration (industry rule of thumb) | 250–300 characters per minute | luft tool page |
| Seedance community experience | Characters ÷ 6 plus padding sets the shot length; allow about 1 extra second per line; lip-sync blurs on single lines over about 8 s (2.0 era) | loglog.blue, wavespeed, cutout.pro |

The studies agree that native speakers run about 7–8 morae per second (multi-source). Planning values for Seedance (inference, not tested on Seedance): 5–6 morae per second for restrained dialogue, no more than 7 for ordinary conversation; add about 1 second per line; add half a second to a second for 「……」; split lines over about 20 morae across two shots. There is no official pace parameter, only words such as "slow pace" (official).

| Line | Reading | Morae | Spoken in about | Range at least |
|---|---|---|---|---|
| 「もう休め。」 | もうやすめ | 5 | 0.8–1 s | 2 s |
| 「承知した。」 | しょうちした | 5 | 0.8–1 s | 2 s |
| 「……もう一回。」 | もういっかい | 6 | 1–1.2 s | 3 s |
| 「……これは命令だ。」 | これはめいれいだ | 8 | 1.3–1.6 s | 3–4 s |
| 「別に。……温かいだけだ。」 | べつに／あたたかいだけだ | 11 | 1.8–2.2 s | 4–5 s |

### 2.4 Kana rewriting and hard words

- Write easily misread kanji in kana: 飯 → メシ (author-tested). In a community test 「焙煎」 was read 「ばいこう」; in hiragana the reading was right, though the intonation still could not be changed (single source). Rewrite only words that are actually misread; converting a lot to kana can upset the rhythm of the sentence (third party).
- Names, technique names, coined words: do not say them if you can avoid it (author-tested); if you must, write them in katakana (multi-source, community). The same applies to a name before Gerard's 「〜殿」.
- Write digits as they are read: 「3人」 becomes 「さんにん」 (third party: digits and symbols should be written as speakable words).
- A word keeps being misread: upload an audio clip containing only that word and write "@Audio3 provides only pronunciation and intonation; the voice follows @Audio1". In community tests the timbre was sometimes carried over too, and the voice had to be changed back with video editing (single source). This is a third audio clip, beyond the rule of thumb of two voice references per clip, so use it only in single-character shots (inference).

### 2.5 Japanese is a relative weak spot: test a short line first

- Seedance 2.0 technical report: for Japanese image-to-video, the audio score for "says what the prompt says" (APF) is 3.13, against 4.20 for English (official, 2.0 data; no Japanese evaluation published for 2.5). Community opinion varies: some find pronunciation and intonation quite natural with matching lip-sync, though intonation cannot be steered; others report it often does not say the specified words (multi-source, third party).
- Method: run a 4–5 second 480p draft with one character and one line to confirm timbre, reading, and muzzle lip-sync, then write the 30 second clip (multi-source). Reference price (2026-10): on Jimeng a 30 second 480p draft costs 270 credits and 720p costs 600 (author-tested).
- When the picture is right and only one line is misread, edit just that line with video editing (wording from the official edit example; not yet seen tested on Japanese):

```text
Edit the video: modify only Kael's line at 12–17 s in @Video1, changing it to Japanese {……これは命令だ。}; timbre and emotion stay as they are, and the lip movement changes word for word with the new line; all other picture, action, camera, and ambience stay as they are.
```

### 2.6 Voice references: specs and binding

| Item | Requirement | Basis |
|---|---|---|
| Format | wav or mp3, each under 15 MB | Official |
| Length | 2–30 s each, at most 10 clips, 30 s total across all audio; 5–10 s each works best | Official |
| Content | Clean solo voice with no music, reverb, or other voices; natural pauses of 150–400 ms between sentences | Third party (multi-source); the pause figure is single source (2.0 era) |
| Clips per run | Bind at most two voice references, one speaker per shot | Author-tested (the official limit is 10) |
| Source | Your own recording or a licensed synthetic voice; a real voice actor needs their permission | Multi-source |

Binding (official): with two images each, write "Image 1 and Image 2 are Kael, matched to Audio 1; Image 3 and Image 4 are Gerard, matched to Audio 2". With one image each, write "Image 1 is Kael; Image 1 uses the voice of Audio 1". Numbering is the order of first appearance; if the upload order changes, change the numbers in the prompt to match (official). Audio provides only timbre, accent, pace, and emotion; the words follow the text (official sd25-pe). When the timbre is off, add a detailed voice description to the prompt and bring the tone of the line close to the reference audio (official 2.0). A third speaker uses a voice card only, or moves to the next clip (inference). Web UIs may differ from the API docs on audio inputs and limits; follow the UI.

## 3. Dialogue coverage inside one generation

### 3.1 Rules

| Rule | Wording | Basis |
|---|---|---|
| One speaker per shot | Only one speaker in any time range; everyone else present "listens quietly with his mouth closed" | Official sd25-pe; author-tested. Official admits lip-sync in multi-person scenes is a weak spot |
| Shot/reverse shot + over the shoulder | The listener's blurred shoulder and ear in the foreground, shooting past them at the speaker's front or three-quarter profile; swap for the reverse | Official storyboard example (over-the-shoulder with a back as foreground); keeping the speaker in the background is inference |
| Anchor the axis to fixed objects | State each person's position relative to the table, door, or window and which side of the line between them the camera is on; repeat each eyeline in every shot | Official (Pippit example, sd25-pe) |
| Orbit | A short arc (the author uses 10–15°) stays on the original side. Beyond about 90° left and right swap: either stop back on the original side or cut to a two-shot to re-establish | Author-tested; inference |
| Framing tightens with emotion | Positions do not change: two-shot medium → over-the-shoulder close → single close → face close-up, then back to medium | Multi-source (official storyboard example, Pippit test article) |
| Close shots for speech | Narrow to chest-up, 50–65mm for close shots, camera steady during the line, pull back to medium afterwards | Author-tested |
| Shot length | Dialogue shots about 3–5 s, about 6–9 shots in 30 s | TV drama average shot length is 3.4–6.3 s (multi-source); the conversion is inference |

```text
Kael sits at the left end of the small wooden table with the window behind him; Gerard sits at the right end with the door behind him. The camera always stays on the stove side of the line from Kael to Gerard, continuing the positions of the previous shot: Kael always looks toward screen right, Gerard always looks toward screen left.
```

First-person scenes (the realistic line): the camera is "my" eyes. Shot/reverse shot becomes a shift of gaze: the speaker looks into the camera, and the camera turns from one person to the other. Over-the-shoulder becomes an object in the foreground. The axis stays: both characters' left/right positions relative to "me" are fixed for the whole clip, anchored to the table or door (inference).

### 3.2 Reaction shots and causal order

- Show the cause clearly, then the reaction. If both fit in one frame, use one composition. If they are far apart, link them with one shift of gaze or a cut. Do not push in to a pure face close-up before the cause is established (official sd25-pe).
- Give the listener his own reaction shot doing one quiet, visible thing (the official examples include pure reaction shots; third parties advise the same). TV editing often cuts to the listener's reaction before the speaker finishes (multi-source).
- A key line can play over the listener's face: the picture is Gerard in close-up, "Gerard keeps his mouth closed, ears slowly pressing back", and the line is labelled "Kael (off-screen, Japanese, …): {…}". Japanese animation often saves lip-sync this way (multi-source), and for anthros it also sidesteps the risk of muzzle lip-sync (inference). Seedance gives lip movement to any mouth it can see, so always state who is off-screen and that the on-screen character's mouth is closed (inference). The official 2.0 report says audio-visual rhythm stays tight even when the speaker is not in frame (official, 2.0 data).
- Inner monologue: first "Kael's muzzle is closed", then "Kael (V.O., Japanese, a low male voice in a cold big-brother manner, to himself): {…}" (the official example writes "lips closed" plus "says (V.O.)").

### 3.3 Ma: write the pause as its own time range

Japanese animation works with "ma": deliberate space between lines and before actions, holding only small movements and ambience (multi-source). In Seedance, write the pause as a separate time range containing small visible actions and ambience, with everyone's mouth closed (a wording assembled from official rules; inference). Do not write "a beat of pause after '休め'" after the line: the official FAQ says repeating words after a line with added notes triggers subtitles. See shot 3 in section 5.

### 3.4 Dialogue ledger (check before writing; keep it out of the prompt)

Official sd25-pe asks for a record per time range of: speaker, whether voiced, line text, audio role, language, on or off screen. Add "to whom" and "who the camera is on". The ledger for the example in section 5:

| Shot | Speaker (on/off screen, to whom) | Line | Morae → at least | Audio | Others |
|---|---|---|---|---|---|
| 1 (0–4 s) | — | — | — | — | Both with mouths closed |
| 2 (4–8 s) | Kael, on screen, to Gerard | {もう休め。} | 5 → 2 s | Audio 1 | Gerard in the foreground, listening with his mouth closed |
| 3 (8–12 s) | — | — | — | — | Gerard with mouth closed, reacting with ears and tail |
| 4 (12–17 s) | Kael, on screen, to Gerard | {……これは命令だ。} | 8 → 3–4 s | Audio 1 | Gerard off-screen |
| 5 (17–21 s) | Gerard, on screen, to Kael | {承知した。} | 5 → 2 s | Audio 2 | Kael in the foreground, listening with his mouth closed |
| 6–7 (21–30 s) | — | — | — | — | Mouths closed |

Check range by range: each line appears once; at most one speaker per range; every line is marked Japanese; no more than two audio clips, with numbers matching; the morae fit; the speaker's muzzle is clearly visible, or the line is explicitly off-screen.

## 4. Subtitle prevention

| Practice (official: far fewer in 2.5 than in 2.0, but "cannot currently be avoided entirely") | Basis |
|---|---|
| Emotion goes in the parentheses before the line; after the line, do not repeat its words or add notes on tone, expression, or action | Official 2.5 FAQ |
| Each line on its own line, in its own time range | The fix given in the official FAQ |
| The reference video itself has no subtitles; otherwise a "no subtitles" request may fail | Official 2.5 |
| Remove text from reference images: names and labels on character sheets, speech bubbles, sound-effect lettering; bind character names in the prompt | Official (2.0 advises removing non-essential text; 2.5 does not rely on labels in the image) |
| Landscape in platform settings (16:9 or 21:9, as all three example lines are) | Official 2.0: subtitles are clearly less likely in landscape than portrait (not restated for 2.5) |
| Dialogue only in {}; 【】 is the subtitle symbol in the official table, so use plain labels such as "Style:" | Official symbol table + inference |
| Positive description in the Sound section: "The picture is clean cinematic footage" | Author's convention |
| If they still appear: delete the subtitles with video editing (the official edit capability includes subtitle removal) or reroll. The official wording "the picture shows no subtitles" is negative and kept for troubleshooting only | Official |

The official FAQ contrast, adapted to Japanese:

```text
Tends to produce subtitles: Kael says {もう休め。これは命令だ。}, pausing after "休め" and stressing "命令".
Recommended (split across two shots):
Kael (Japanese, a low male voice in a cold big-brother manner, flat, to Gerard): {もう休め。}
Kael (Japanese, a low male voice in a cold big-brother manner, quiet but forceful, to Gerard): {……これは命令だ。}
```

## 5. Complete example: Kael × Gerard, 7 shots

Written in this skill's fixed section order. 「……これは命令だ。」 and 「承知した。」 come from the example cast's profiles; 「もう休め。」 and the plot are examples, to be replaced by the script. Scene and clothing details are left to the reference images. For first-person shooting on the realistic line, see the end of 3.1.

Assets, uploaded in order of first appearance: @Image1 Kael head, @Image2 Kael full-body front, @Image3 Gerard head, @Image4 Gerard full-body front, @Image5 the room; @Audio1 Kael's voice, @Audio2 Gerard's voice (5–10 s each, clean solo recordings).

```text
Style: Hyper-real cinematic picture with realistic layered fur: clear fur direction, distinct long and short fur zones; ears, tails, and fabric move naturally with each action.

References:
@Image1 (Kael, head): use only Kael's black head fur, amber eyes, ear shape, and muzzle length.
@Image2 (Kael, full body): use only Kael's clothing, red scarf, and body proportions.
@Image3 (Gerard, head): use only Gerard's white head fur, blue eyes, scar position, and muzzle length.
@Image4 (Gerard, full body): use only Gerard's clothing, blue-and-white cape, and body proportions.
@Image5 (room): use only the room layout and the positions and materials of the small wooden table, window, door, and stove.

Characters: The whole clip has only two characters, Kael and Gerard, and each appears exactly once in frame.
Kael: black wolf anthro, adult male, a complete wolf head with a long muzzle, black fur over the whole body, upright on two legs, canine paw-hands (four fingers and a thumb); the trait only he has: a red scarf. Image 1 and Image 2 are Kael; Kael speaks with the voice of @Audio1, which provides only timbre, pace, and tone.
Gerard: white wolf anthro knight, adult male, a complete wolf head with a long muzzle, white fur over the whole body, upright on two legs, canine paw-hands (four fingers and a thumb); the traits only he has: the scar on his face and a blue-and-white cape. Image 3 and Image 4 are Gerard; Gerard speaks with the voice of @Audio2, which provides only timbre, pace, and tone.
Each keeps his own fur colour, scar, scarf, and cape throughout; both show a wolf's canines when speaking; eyes keep the colours in the references, with a soft catchlight.

Scene layout: Kael sits at the left end of the small wooden table with the window behind him; Gerard sits at the right end with the door behind him. The camera always stays on the stove side of the line from Kael to Gerard, continuing the positions of the previous shot: Kael always looks toward screen right, Gerard always looks toward screen left.

Light: The key light is an oil lamp hanging directly above the table, warm yellow, shining down; cold blue night light comes through the window behind Kael and draws a thin bright rim along his ears and shoulders.

Sound: The only sounds are ambience, action sounds, and the two characters' Japanese dialogue. Voices are clean and clear with standard pronunciation; generate audio strictly from the line text, spoken word for word to the end. There are three lines in the whole clip, and only one person speaks in any time range. The picture is clean cinematic footage.

Shots:
Shot 1 (0–4 s): Two-shot medium, eye level, camera at chest height, static. Kael slides a steaming cup in front of Gerard; Gerard sits bolt upright, eyes on the cup; both keep their mouths closed. Moving details: the lamp flame wavers, steam rises from the cup, the tip of Gerard's tail sways slowly beside his chair. Ends with: the cup resting in front of Gerard, Kael's hand drawn back to the table edge.
Shot 2 (4–8 s): Hard cut, over-the-shoulder close shot. Gerard's blurred white ear and shoulder are in the right foreground; past them, Kael in three-quarter profile with his whole muzzle in frame, camera steady. As Kael speaks, his muzzle and lower jaw open and close with each syllable, and his lips close clearly on closed-lip sounds. Kael (Japanese, a low male voice in a cold big-brother manner, flat, to Gerard): {もう休め。} Gerard listens quietly with his mouth closed. Ends with: Kael's mouth closed, eyes resting on Gerard's face.
Shot 3 (8–12 s): Hard cut, Gerard alone in close shot, three-quarter profile looking toward screen left, camera steady, both mouths closed. Gerard's ears first turn together toward Kael, then slowly lower to the sides, and his tail tip stops; his eyes move from Kael's face to the cup and back to Kael's face. The only sounds are the crackle of the oil lamp and the wind outside the window. Ends with: Gerard still seated, ears half lowered, mouth closed.
Shot 4 (12–17 s): Hard cut, Kael alone in close shot, three-quarter profile looking toward screen right; the camera pushes in very slowly to a face close-up and settles, the whole muzzle in frame throughout. Kael's ears press back for a moment, then rise again; as he speaks, his muzzle and lower jaw open and close with each syllable, and his lips close clearly on closed-lip sounds. Kael (Japanese, a low male voice in a cold big-brother manner, quiet but forceful, to Gerard): {……これは命令だ。} Gerard, off-screen, listens quietly with his mouth closed. Ends with: Kael's mouth closed, eyes moving to the window.
Shot 5 (17–21 s): Hard cut, over-the-shoulder close shot. Kael's blurred black ear and red scarf are in the left foreground; past them, Gerard in three-quarter profile. Gerard straightens his torso, ears upright and forward; as he speaks, his muzzle and lower jaw open and close with each syllable. Gerard (Japanese, a stiff, earnest middle-aged male voice, solemn, to Kael): {承知した。} Kael listens quietly with his mouth closed. Ends with: Gerard rising from his chair, torso upright.
Shot 6 (21–26 s): Hard cut, medium shot, eye level, static, the camera still on the stove side, the door on screen right. Gerard walks to the door and pulls it open, stops for one step, ears turning back toward Kael, tail hanging close to his legs; then he walks out and the door closes softly behind him. Ends with: the door closed, lamplight wavering on the door panel.
Shot 7 (26–30 s): Hard cut, Kael alone in close shot, three-quarter profile, static. Kael looks at the cup on the table, ears slowly lowering to the sides, tail tip resting beside the chair; with his mouth closed he lets out a long breath, whiskers moving with it. Ends with: Kael sitting alone at the table, eyes on the cup, the frame holding steady for about 2 seconds.

Ambience: 0–30 s: <wind outside the window> and <the faint crackle of the oil lamp flame> continue to the last second; second 1 <the base of a cup sliding across a wooden table>; second 22 <the creak of a wooden door being pulled open>; second 25 <a wooden door closing softly>.
```

Platform settings: 16:9, 30 seconds, audio on; 480p draft first, 720p once it looks right.

## 6. Troubleshooting

| Symptom | Usual cause | Fix |
|---|---|---|
| A line is spoken by the other character, or two mouths move | Both in frame with no statement of who speaks and who listens | One speaker per shot; write "X listens quietly with his mouth closed"; move the line to the speaker's single close shot (official) |
| An unwritten line appears at the start | The opening range does not say those present keep their mouths closed | Write "N lines in the whole clip" and closed mouths in the opening range (seen once in the test run, not yet re-tested) |
| Look-alikes swap; real animal, all fours; background figures turn human | The trait is not repeated, numbering is off; underwater, "half-squatting", generic passers-by | See 1.3 and 1.2 |
| Japanese misread or spoken with a Chinese accent | Hard kanji, names, digits; lines not individually marked Japanese | See 2.1 and 2.4; when only one line is wrong, edit that line with video editing |
| Muzzle lip-sync does not match | Line too long, full face or pure profile, something in front of the mouth, turning the head while speaking | Shorten the line, three-quarter profile, steady head; if that fails, go off-screen or to a reaction shot |
| Speaking pitch too high | "Loudly" | Change to "quiet but forceful" (author-tested) |
| No sound in the second half | Ambience not written to the end | Write ambience to the last second (author-tested) |
| Glowing eyes | Strong emotion words | Ordinary description (official) plus eye colour and a soft catchlight; if that fails, add the official negative sentence "the eyes do not glow" |
| Background music appears | The model gets around a single word with synonyms | Start with "The only sounds are ambience, action sounds, and dialogue"; if that fails, follow the official practice and exclude the family of music words once at the start and once at the end (negative wording, as a fallback) |

## 7. Pre-delivery checklist

- [ ] Every character on screen has his own references (head + full body, single views), one per line, numbered in order of first appearance
- [ ] Every character has species anatomy and one trait only he has, repeated at every mention; background figures have species; poses are concrete
- [ ] Emotion is written as actions of ears, tail, gaze, muzzle, and fur, with 2–3 details per turn
- [ ] Every line is `Name (Japanese, voice, emotion, to whom): {Japanese text}`, written once, in its own time range
- [ ] Morae ÷ 5–6 + 1 s fits the range; lines over about 20 morae are split
- [ ] Hard kanji, names, and digits are in kana or spelled as read; names are rarely spoken; no "loudly"
- [ ] No more than two voice references, "Image N matched to Audio N" lined up, 5–10 s each, 30 s total at most
- [ ] One speaker per range, everyone else "listens quietly with his mouth closed"; off-screen lines say who is off-screen
- [ ] The axis is written as positions relative to fixed objects and the side the camera is on; eyelines repeat in every shot
- [ ] Cause before reaction; pauses are their own time ranges
- [ ] No repetition or notes after lines; no text or subtitles in reference images or videos; landscape in platform settings
- [ ] The prompt is positive throughout; aspect ratio, duration, resolution, and audio switch are in platform settings
- [ ] Every shot has "Ends with"; ambience runs to the last second
- [ ] A short line was tested at 480p for timbre and muzzle lip-sync

## 8. Sources

Researched 2026-10-28. Third-party sites with "seedance" in the name are not ByteDance. Author-tested: the author's production notes (characters, voices, failures). Test run: one 30 second Seedance 2.5 generation on Jimeng. Both compiled 2026-10-28.

- Official: Volcengine Ark, Seedance 2.5 prompt guide (line format, closed mouths in multi-person scenes, over-the-shoulder storyboards, causal reveal, subtitle and glowing-eye FAQ, water noise, editing a line) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide ; English https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5-prompt-guide
- Official: Volcengine Ark, Seedance 2.5 tutorial (sound symbols, audio specs, subtitle removal by editing) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Official: Volcengine Ark, Seedance 2.0 prompt guide (marking Japanese, fewer subtitles in landscape, head shot plus full-body shot, voice description, 2–3 stable traits) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-0-prompt-guide ; https://docs.volcengine.com/docs/82379/2222480
- Official: sd25-pe skill 0.1.1 (dialogue ledger, listening with mouths closed, positions by stable objects, causal reveal, parameter separation) https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip
- Official: Pippit, Seedance 2.5 handbook (axis wording, over-the-shoulder wording, voice binding) https://www.xiaoyunque.com/tutorials/seedance-2-5 ; multi-source: Pippit test article (fixed positions, tightening framing) https://www.xiaoyunque.com/articles/seedance-2-5-ai-film-studio
- Official (2.0 data): Seedance 2.0 technical report (Japanese APF, off-screen voice, multi-person lip-sync weakness) https://arxiv.org/pdf/2604.14148 ; official: 2.5 launch blog (multi-subject interaction still to improve) https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- Multi-source (academic and industry, speech rate): https://clrd.ninjal.ac.jp/csj/misc/preliminary/6_1.html ; https://digitalcommons.usf.edu/seatj/2018/conference/29 ; https://www.cambridge.org/core/journals/language/article/abs/crosslanguage-perspective-on-speech-information-rate/73064B3F77E7CE81C42CAB29B4393F80 ; https://www.jstage.jst.go.jp/article/ast/39/2/39_E1731/_article/-char/ja ; https://www.luft.co.jp/cgi/youtube-script-duration.php
- Single source (Japanese tests, community): loglog.blue (voice repeated per shot, characters ÷ 6, the 焙煎 misreading) https://loglog.blue/spicelemon/seedance-2-5/ ; GENEL (a pronunciation clip carrying off the timbre) https://note.com/genel/n/nf329685c68a9 ; CBA Games (often says the wrong words) https://ai.cbagames.jp/2026/08/24/seedance-2-5-review/
- Third-party experience (multi-source): https://wavespeed.ai/blog/ai-guides/ai-lip-sync-dialogue-scenes-with-seedance-2-5/ ; https://www.cutout.pro/learn/blog-seedance-2-0-audio-guide/ ; https://www.seedance.tv/blog/how-to-keep-voices-consistent-in-seedance-2-5 ; https://www.seedance.tv/blog/seedance-2-5-supported-languages ; https://www.seedance.tv/ja/blog/seedance-2-5-lip-sync-issues ; single source (pauses between sentences) https://crepal.ai/blog/aivideo/blog-seedance-2-0-lip-sync-voiceover-fix/ ; basis for inferences: role language https://www.jpf.go.jp/j/project/japanese/teach/tsushin/bookshelf/201111.html , voice actors opposing unlicensed generation https://animeanime.jp/article/2024/10/16/87146.html
- Anthro performance: interviews with the director and CG director of an anthro 3DCG anime (ears react first, tail sway, lips closing on the ま row, small mouth for muttering, long muzzles are hard head-on; the ま row point is single source) https://animeanime.jp/article/2019/10/30/49323_2.html ; https://www.scrmbl.com/post/studio-orange-beastars-interview ; single source (mane at low angles) https://scrmbl.com/post/yusuke-yoshigaki-bna-interview ; anthro appearance and fur: multi-source (kemono levels, animal-ear words) https://dic.pixiv.net/a/ケモノ ; https://techhowto.blog/posts/stablediffusion-prompt-furry/ ; animal body language https://en.wikipedia.org/wiki/Cat_body_language ; https://en.wikipedia.org/wiki/Body_language_of_dogs ; single source (naming which fur moves) https://higgsfield.ai/blog/seedance-2-5-prompting-guide ; single source (fur moving as one sheet in 2.5) https://note.com/creative_edge/n/nc9f095edf474 ; single source (teeth flipping) https://www.aitoolssme.com/blogs/seedance-2-5
- Dialogue coverage (multi-source): https://arxiv.org/abs/2002.06923 ; https://www.koreascience.or.kr/article/CFKO200921553663688.pdf ; https://faculty.salisbury.edu/~axsharma/MyWebs/EFP/gramtv.html ; https://www.davidbordwell.net/blog/2007/05/27/intensified-continuity-revisited/ ; https://en.wikipedia.org/wiki/Reaction_shot
- Ma and off-screen lines (multi-source): https://nofilmschool.com/2013/09/master-of-ma-director-hayao-miyazaki-set-to-retire ; https://animeanime.jp/article/2015/09/18/24952_2.html ; https://animenation.net/blog/?p=12849 ; https://news.mynavi.jp/techplus/article/kurieita-22/
