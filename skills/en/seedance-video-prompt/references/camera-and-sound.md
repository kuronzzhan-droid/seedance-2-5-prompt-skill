# Camera and sound glossary

## When to read this file

Look terms up here when writing framing, camera position, camera movement, transitions, light, and sound. When writing dialogue labels for Japanese-speaking characters, look up voice, register, first-person pronouns, and readings (section 11). This is a quick-reference sheet; the fuller treatments are elsewhere:

- How many shots to cut in 30 seconds, and how to get the feel of Japanese animation, TV drama, or film: `shot-grammar.md`
- Fight camera work, impact, and close-ups: `combat-closeups.md`
- The full workflow for anthro Japanese dialogue (mora counting, muzzle lip sync, shot/reverse shot, avoiding subtitles, voice references): `kemono-jp-drama.md`
- Whole-prompt structure and complete examples: `templates-30s.md`

Evidence tags: [official] Volcano Ark Seedance 2.5 docs, the Xiaoyunque official handbook, the official sd25-pe skill; [official 2.0] stated in the 2.0 guide and not restated for 2.5; [multi-source] two or more unofficial sources agree, including industry convention; [single source] one source only; [inference] derived from the material, not tested on Seedance; [author-tested] the author's production notes and lessons learned; [test run] one generation on Jimeng on 2026-10-28.

## Contents

1. Writing principles
2. Framing
3. Camera position and angle
4. Camera movement
5. Named camera moves
6. Transitions
7. Lens parameters → visible results
8. Light
9. Sound symbols and dialogue lines
10. Ambience, sound effects, music, and positive wording
11. Japanese voice and register
12. Sources

## 1. Writing principles

- Write common terms directly. Write rare terms as "term + what it acts on + how the picture changes + foreground/background relation + direction or speed". Write named moves as "move name + what it acts on + start position + direction of travel + end position" [official sd25-pe].
- One main camera move per range, with direction and speed [official 2.0]. Write subject motion and camera motion separately, as in "he walks toward frame right; the camera pans right to follow" [single source]. For more camera variety, change moves between ranges [multi-source].
- Camera moves have a motive: the camera rises as the character stands, and settles at the moment the character stops [multi-source].
- Every "example wording" below is a positive description and can be pasted as is [author-tested: negative wording damages detail].

## 2. Framing

Official vocabulary: extreme wide, wide, medium, close, close-up [official].

| Framing | What is in frame | Common use |
|---|---|---|
| Extreme long / extreme wide | People very small, environment dominant | Opening to establish place, closing on open space |
| Long / wide | Full figure plus a good deal of environment | The relation between figure and space; fights use it first to establish positions [multi-source] |
| Medium | Knees or waist up | Action, conversation |
| Medium close | Chest up | Conversation, expression plus gesture |
| Close | Shoulders up | Emotion; the speaker gets a chest-up close shot, the camera steady during the line, then back to medium afterward [author-tested] |
| Close-up | A face or a single object | Emotional peaks, product detail; the tightest close-up in the clip is saved for the turning point [multi-source] |
| Extreme close-up / macro | Eyes, fingertips, material texture | Texture, suspense; on anthro characters, an ear tip, nose, whiskers, or tail tip [inference] |

## 3. Camera position and angle

Positions in the official vocabulary: low angle, high angle, first person, three-quarter side, over the shoulder [official]. Also in common use: eye level, low camera looking up, top-down (directly overhead), Dutch angle (tilted frame), phone selfie view, in-car or dashcam view, CCTV view.

| What to write | Example (paste as is) | Basis |
|---|---|---|
| Camera height | Eye level, camera at chest height, locked off | Author-tested: state camera height in every shot |
| Low-camera close-up | The camera sits on the wooden floor, shooting boots coming down step by step | Author-tested |
| Over the shoulder | The listener's blurred shoulder and ear in the foreground; past them, the speaker's face in three-quarter view | Official shot examples; anthro wording in `kemono-jp-drama.md` 3.1 |
| The axis | The camera always stays on the window side of the line between the two; A always looks frame right, B always looks frame left | Official (Xiaoyunque example, sd25-pe: anchor to fixed objects such as a door, table, or window) |
| First person | The camera is "my" eyes, at my eye height; whoever speaks to me looks straight into the lens | "First person" is in the official vocabulary; the line-by-line rewrite is inference, see `shot-grammar.md` 6.1 |

## 4. Camera movement

| Move | Example wording (paste as is) | Notes |
|---|---|---|
| Push in | The camera pushes slowly in on her face and settles at a close shot | For realisation or resolve, push very slowly from medium close to close-up [multi-source] |
| Pull back | The camera pulls back to reveal the whole room | |
| Pan (horizontal) | The camera pans in place from left to right across the whole street | |
| Tilt (vertical) | The camera tilts up from the character's shoes to the sky | The body turns in place; to raise the camera itself, write "rises" |
| Track (lateral) | The camera tracks right, parallel to the character | Foreground, figure, and distance sliding at different speeds give a paper-layer parallax [multi-source] |
| Follow | The camera follows one metre behind the character | Side follow: the camera moves right parallel with him [author-tested] |
| Orbit | Centred on the product, the camera orbits clockwise at an even speed for half a circle | State centre, direction, and speed [official: Xiaoyunque 360° example] |
| Short arc | The camera arcs right around the two by about 15 degrees and stops on the same side | The author's usual 10–15° [author-tested]; beyond about 90° the two swap screen sides [inference] |
| Rise / descend | The camera rises slowly from the ground to roof height | |
| Slow reveal | The camera tilts slowly up from the feet, revealing in turn the belt, the pauldron, and the face | State the bottom-to-top order [author-tested] |
| Handheld | Slight handheld shake, the camera now and then lagging half a beat and catching up with the character | Say who it follows and how much it shakes [official] |
| Locked off | The camera is fixed and the frame holds steady; only the characters move | Keep slight motion in breath, fabric, and fur [single source] |
| Crash zoom | A rapid zoom in, the frame tightening very fast from a medium shot to a close-up of the window and stopping | Crash zoom is expanded as a rare term [inference, following the official rule] |

## 5. Named camera moves

Officially listed as usable by name: one take, Hitchcock zoom, aerial, FPV, bullet time, handheld, speed ramp [official]. Add parameters after the name:

- **One take**: no cuts at all, with the camera's route linking several spaces. Write it in time ranges, not "Shot 1 / Shot 2" [single source]. Open each range with "Without cutting, the camera keeps…", and when crossing spaces write the route, for example "Without cutting, the camera keeps following him across the threshold into the shop, around the left of the counter to his front". Test run: the breakfast-shop example was hard-cut at 7.38 s, the boundary between two ranges, jumping from outside the door straight into the shop [test run]. When continuity matters, cut down to 3 ranges, or split into two clips joined by first/last frames or extension. When the spaces do not connect, do not ask for "one take" and "an instant change of scene" together. Complete example in `templates-30s.md` section 1.
- **Hitchcock zoom (dolly zoom)**: the camera pushes in while the focal length widens, the character staying the same size in frame while the background stretches away, for shock or vertigo. State how large the subject stays and how the background changes [official].
- **Aerial**: state changes of height and direction, as in "skimming low over the river, then rising slowly".
- **FPV**: write path, speed, and turns, as in "flying fast along the roof ridge, through the gap between two chimneys, then turning right" [official].
- **Bullet time**: write the frozen instant and the orbit direction, as in "the spray hangs in the air and the camera turns half a circle counter-clockwise around the subject" [official].
- **Speed ramp**: write where it slows, where it returns to real time, and what frame it ends on [official]. Give it to only 1–2 key moments per clip [multi-source].
- **Rack focus**: official wording "rack focus, the focus shifting smoothly: the tree that was sharp in the foreground blurs, and the person in the background gradually comes into focus" [official]. Add the second it happens and who the focus moves from and to.
- **Whip pan**: official wording "at second 5 the camera tracks fast to the left; when the foreground bookshelf fully covers the screen, switch to the next scene, and after the switch the camera keeps moving left at a similar speed" [official: Xiaoyunque].

## 6. Transitions

Foreground wipe (an object enters from the left and covers the lens, and when it clears the scene is new), whip pan, character spin, object morph (the swirl in a coffee cup becomes a starry sky), push-through (the camera pushes through a window into the next scene), defocus transition, match cut (joined by the same shape or action), hard cut. State the second it happens, how, and what frame it arrives at.

Sound can make a transition too: the next scene's sound starts about a second early (J-cut), or the last line carries over into the next picture (L-cut) [multi-source: film editing convention]. Wording: "from second 14 <the bell of a tram pulling in> starts first, and at second 15 the picture hard-cuts to the platform". The model may not hit this accurately, so try a sample first [inference].

## 7. Lens parameters → visible results

Focal length, aperture, and shutter can only be a supplement; the visible result has to be written out [official sd25-pe].

| Parameter you want | More reliable wording |
|---|---|
| 24mm wide angle | A strong sense of space, near objects look large, slight stretching at the frame edges |
| 50–65mm (the usual range for speaking close shots) | Perspective close to the human eye, a rounded figure, a moderately blurred background [author-tested] |
| 85mm portrait lens | The background compressed and blurred, a rounded figure |
| Telephoto | The character and the crowd behind pressed into one layer, the background melting into soft blocks of colour [multi-source] |
| f/1.4 wide aperture | The background blurred into soft discs of light |
| Fast shutter | Water drops and strands of hair frozen sharp in the air |
| Slow shutter | Headlights drawing light trails, the crowd blurred into flowing shadows |

## 8. Light

State where the light comes from, who it falls on, and what shadow it leaves. Write direction as a position, such as "the source is off-screen left". Writing only "backlit" produces a halo above the head [author-tested].

| What you want | Steadier wording |
|---|---|
| Backlight | The source is off-screen at rear left; a thin bright rim runs along the character's ears and shoulders, the face in soft shadow |
| Window light | Daylight comes in through the window at frame left, lighting half the face, the other half in soft shadow |
| Golden hour | Low warm-gold evening sun from off-screen right, shadows stretched long |
| Top light (oppressive) | Light falls from a hanging lamp directly overhead, the eye sockets and under the jaw in shadow |
| Under light (unease) | Light rises from the embers below, the lower half of the face brightest |
| Low-key light | Light comes only from the oil lamp in frame and the moonlight outside the window; the room is dark overall, with outlines and fur texture still readable in the shadows [multi-source] |
| Volumetric light | A beam slants in from a high window at off-screen upper left, through dust hanging in the air |

Also useful: overcast soft light, mixed neon light, practical sources in frame (a desk lamp, a phone screen, candlelight, headlights). Keep one colour scheme through the whole clip, for example "shadows lean teal, lamplight and fur lean warm gold" [multi-source].

## 9. Sound symbols and dialogue lines

### 9.1 Official symbols

| Content | Symbol | Example |
|---|---|---|
| Music | `()` | `(soft piano playing in the background)` |
| Sound effect | `<>` | `<a bell ringing in the distance>` |
| Dialogue | `{}` | `{……これは命令だ。}` |
| Subtitle | `【】` | `【Chapter One: Departure】` |

Basis: the Seedance 2.5 tutorial states "sound is distinguished with special characters: music uses (), sound effects use <>, dialogue uses {}, subtitles use 【】", and the sd25-pe symbol table is identical [official]. (`sources.md` once recorded this as "only a convention"; the 2.5 tutorial states it as a rule.)

- 【】 means subtitles in the symbol table, yet official examples also use it for section headings. This skill therefore writes section labels as plain words with a colon, such as "Style:", so no heading is drawn into the picture. Dialogue goes only in {} [official + inference].
- When marking sound effects with <>, character names take no angle brackets; write the plain name [official sd25-pe].
- For non-Chinese dialogue, state the language before the line. Label every speaker one by one; one declaration at the top is not enough [official].

### 9.2 Dialogue lines

Format: `Name (language, voice, emotion, to whom): {line}`. Write it in the time range or shot where the line happens, each line once in the whole clip. The "Sound:" section gives only the total count and does not repeat the lines [official + author-tested].

| Situation | Wording (Japanese lines from the sample character setups) |
|---|---|
| Speaking on screen | Kael (Japanese, a low male voice in a cold big-brother manner, quiet but forceful, to Gerard): {……これは命令だ。} Gerard listens quietly with his mouth closed. |
| Off-screen line, picture on the listener's face | The picture is a close shot of Kael, mouth closed, his ears pressing back once first. Gerard (off-screen, Japanese, a stiff, strait-laced middle-aged male voice, solemn, to Kael): {承知した。} |
| Speaking to "me" (first person) | Seren looks into the lens. Seren (Japanese, a bright boyish male voice, quiet, to me): {……もう一回。} |
| Inner monologue | Kael's muzzle is closed, his gaze on the window. Kael (V.O., Japanese, a low male voice in a cold big-brother manner, to himself): {line} |
| Narration | Narrator (V.O., English, a steady male voice, calm, to the audience): {line} |
| Other languages | Tom (English, a gentle young male voice, relaxed, to the clerk): {Just a coffee, please.} Add a regional accent only when the user specifies one, for example "natural, colloquial American English" [official sd25-pe] |

- Only one person speaks per range; everyone else present is written as "listens quietly with his mouth closed" [official sd25-pe + author-tested].
- Hesitation and interruption go straight into the line: 「……」「——」 [official example].
- Emotion goes in the parentheses before the line. Repeating words from the line after it, or adding notes like "X pauses afterward", tends to trigger subtitles [official FAQ].
- Keep translations of the line outside the prompt. Placed next to {}, a translation may be spoken or turned into a subtitle [inference].

## 10. Ambience, sound effects, music, and positive wording

| Category | Example wording | Notes |
|---|---|---|
| Ambience | 0–30 s: <rain on a corrugated metal roof> and <the low hum of a distant tram> continue to the last second | Write it to the last second, or the second half may go silent [author-tested] |
| Action sound | Second 12 <the creak of a wooden door pulled open> | Name the physical source, in the same second as the action; replace "atmospheric sound effects" with a concrete source |
| Music | (soft solo piano, about 70 BPM, fading out at second 25) | State genre, tempo, and start and end seconds |
| Designed silence | From second 16 all other sound cuts off, leaving only <a heartbeat> | |
| Quiet before a key line | (low strings) enter at second 3 and stop one beat before the line at second 9, leaving about 1 second of quiet with only breathing and ambience | Common in Japanese animation [multi-source] |
| Subjective sound | At the moment of the hit all sound goes muffled, leaving only <ringing in the ears> and <a heartbeat>, returning after two seconds | Common in film [multi-source] |
| Music at the climax | After the last line, as the camera rests on the close-up, (lyrical strings fade in) | Common in TV drama [multi-source] |
| Layers | Dialogue clearest, only one or two kinds of ambience | About 5 layers per 5 seconds as a ceiling [single source] |

Writing water, waves, or echoes in a prompt tends to produce bubbling, reverb, and howl in the audio [official FAQ]. For rainy nights, seashores, and caves, write only one or two concrete sources, and write "the echo of an announcement" as "a blurred announcement voice".

### Exclusions written as positives

| To exclude | Positive wording | Basis |
|---|---|---|
| Background music | The only sounds are ambience, action sounds, and dialogue | Author-tested |
| Extra lines | There are two lines in the whole clip; the rest of the time everyone keeps their mouth closed | The positive form of the official "listen with mouth closed" |
| Narration | The only voices in the clip are the lines of characters on screen | Inference |
| Animals talking | The crow is an ordinary bird that makes only crow calls; the lines are spoken only by Jay | Official: state who speaks; the positive rewording is inference |
| Subtitles | The picture is clean footage, with text only on signs that belong to the scene | Author-tested |
| "Loudly" was written | Quiet but forceful | Author-tested: "loudly" raises the pitch |
| Singing, humming | Spoken in a normal speaking tone | Single source: atmosphere prompts occasionally turn a voice into humming |

Official fallbacks when positive wording fails (negative wording, for troubleshooting only): for subtitles write "the picture shows no subtitles" [official sd25-pe]; for background music write "the audio keeps only character voices, ambience, and action sounds", then exclude the music synonyms (music, background music, BGM, score, instrumental, melody, synth effects, atmospheric pad) once at the start and once at the end of the prompt [official FAQ].

## 11. Japanese voice and register

### 11.1 Voice cards

Each character gets one fixed voice description, placed in the "voice" slot of the dialogue label and copied unchanged into every speaking shot [multi-source]. Changing a single adjective can change the apparent age and texture of the voice [single source]. If only the timbre is repeated and not the manner, shots with gentle lines will soften the manner [single source]. The official 2.0 example of a voice description: "speaks with the voice of @Audio1, a low, thick, warm middle-aged male voice with a fine grain" [official 2.0]. With a voice reference, the voice card is only a supplement. The sample characters' voice cards are in `kemono-jp-drama.md` 2.2.

### 11.2 Voice descriptors: English ↔ Japanese

There is no comparison test of which language works better for descriptors; the community uses both, and Chinese descriptors too [multi-source].

| English | Japanese | Basis |
|---|---|---|
| Low, deep | 低い声・低音ボイス | Multi-source |
| Husky, smoky | ハスキー・しゃがれ声 | Multi-source |
| Rich and resonant | 渋い・深みのある声 | Multi-source |
| Young man's voice | 20代の青年の声 | Multi-source |
| Boy's voice | 少年声 | Multi-source |
| Seasoned middle-aged man | 渋い中年男性の声 | Multi-source |
| Light, almost breathy | 息まじりの軽い声 | Single source (English wording "a light, almost breathy voice") |
| Commanding | 威厳のある声 | Inference (direct translation) |
| Bright | 明るく張りのある声 | Inference |
| Stiff, strait-laced | 生真面目で抑揚の少ない声 | Inference |
| Cold | 冷ややかな声 | Inference |

A community all-Japanese form: 「日本語、標準語、中性的で幼く少し眠たげ、冒頭だけ必死な早口」, in the order language, accent, timbre, change of pace [single source].

### 11.3 Register and first-person pronouns: write them into the line itself

Much of personality lies in how a character speaks. The first-person pronoun, the level of politeness, and the sentence endings written into the line itself are more controllable than "a hearty tone" in the parentheses. One character keeps the same pronoun and endings through the whole clip [inference, based on yakuwarigo, "role language"]. "An old-fashioned knightly manner" in the parentheses is only a supplement; the Sound section then adds "generate the audio strictly from the written lines, spoken word for word to the end" (a positive rewrite of the official constraint).

| Register | Markers in the line | Example |
|---|---|---|
| Polite (teineigo) | 〜です、〜ます | 「承知しました。」 |
| Plain (tameguchi) | 〜だ、〜だろ、〜ぞ | 「行くぞ。」 |
| Rough colloquial | 〜じゃねえ、〜だろうが | 「……まだ、終わっちゃいねえ。」 |
| Old-fashioned samurai / knightly | 拙者、〜でござる、〜いたそう; Gerard's 「承知した」 and 「〜殿」 | 「拙者が相手をいたそう。」 |
| Kansai dialect | ほんま、〜へん、〜やな; label it "Japanese, Kansai dialect (Osaka accent)" | 「ほんま、しゃあないやっちゃな。」 |

The wording comes from community examples and inference. Kansai and other dialects have no public test results, and whether the pitch accent comes out right takes several rolls to find out [inference].

| First-person pronoun | Impression |
|---|---|
| 俺 / オレ | Rugged, direct |
| 僕 | Gentle |
| 私 | Restrained, formal |
| わし | Older |
| 拙者 | Samurai manner |
| 自分 | Athletic, soldierly |

[inference: role language is an academic concept and carries stereotypes, so use it deliberately]. Which pronoun each character uses follows the sample setups. Have a native speaker check Japanese lines written by Claude; third-party guides also recommend a native check of pronunciation [single source].

### 11.4 Japanese wording for the emotion slot (optional)

| English | Japanese |
|---|---|
| Flat | 淡々と |
| Quiet but forceful | 低く抑えた、芯のある声で |
| Muttering under the breath | ぼそっと |
| Solemn | 改まった口調で |
| Hesitant | ためらいがちに |
| With a laugh in the voice | 笑いを含んだ声で |
| To himself | 独り言のように |

[inference: direct translations, untested]. For volume write "quiet but forceful"; "loudly" raises the pitch [author-tested].

### 11.5 Readings, pauses, and pace

- Write hard-to-read kanji in kana: 飯 → メシ [author-tested]. In one community test 「焙煎」 was read 「ばいこう」; in hiragana the reading came out right, though the intonation still would not change [single source]. Change only words that are actually misread; converting a lot to kana can upset the rhythm of the whole sentence [single source].
- Names, technique names, and coined words: leave them unspoken where possible, and write them in katakana when they must be said [author-tested + multi-source].
- Write numbers as they are read: 「3人」 → 「さんにん」 [single source].
- Convert pace to duration by mora: restrained dialogue at 5–6 morae per second, ordinary conversation at no more than 7 per second, plus about 1 second per line [inference]. Counting rules and a table of examples are in `kemono-jp-drama.md` 2.3.
- When one word is misread again and again: upload an audio clip containing only that word's reading and write "@Audio3 is for reading and intonation only; the voice follows @Audio1". Sometimes the voice is carried off too [single source].

### 11.6 Binding voice references

Write "Image 1 is Kael, and Image 1 speaks with the voice of Audio 1". With two images per character write "Image 1 and Image 2 are Kael, matched to Audio 1". Upload and number in order of first appearance [official]. A clean single-speaker clip of 5–10 s works best [official]; bind two voice references at most per prompt [author-tested]. The audio supplies only timbre, accent, pace, and emotion; the words follow the text [official sd25-pe]. Specs are in `kemono-jp-drama.md` 2.6.

## 12. Sources

Research date 2026-10-28. Third-party sites with "seedance" in their names are not official ByteDance sites.

- Official: Volcano Ark, Seedance 2.5 prompt guide (vocabulary for framing, camera movement, and position; wording for named moves and rare terms; the rack-focus example; dialogue format; listening with mouth closed; over-the-shoulder shots; FAQ on subtitles, background music, and water noise) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide
- Official: Volcano Ark, Seedance 2.5 tutorial (the sound symbol table, stating the language before non-Chinese lines, reference audio specs) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Official: sd25-pe skill 0.1.1 (symbol table, <> and character names, labelling each speaker, the formula for camera terms, "the picture shows no subtitles", regional accents only when specified, audio supplying timbre only) https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip
- Official: Xiaoyunque, Seedance 2.5 official handbook and prompt guide (axis wording, whip-pan wording, 360° orbit, parameters for named moves) https://www.xiaoyunque.com/tutorials/seedance-2-5 ; https://www.xiaoyunque.com/tutorials/seedance-2-5-prompt-guide
- Official 2.0: Seedance 2.0 prompt guide (one camera move per shot, labelling the language of Japanese lines, the voice description example) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-0-prompt-guide
- Single source (third party): time ranges for one-take clips https://morphed.app/blog/seedance-2-5-prompts ; separating subject motion and camera motion, slight motion kept on a locked-off camera https://github.com/XiaoJieAi66/XiaoJieAigc-seedance-2-5-video-prompt
- Multi-source (camera convention): the emotional push-in https://www.panavision.com/highlights/highlights-detail/5-ways-one-camera-move-can-be-used-to-different-effect ; motivated camera movement https://hazlitt.net/node/10611811 ; telephoto and wide angle https://www.davidbordwell.net/blog/2007/01/16/shot-consciousness/ ; layered parallax https://cgworld.jp/terms/%E3%83%AA%E3%83%9F%E3%83%86%E3%83%83%E3%83%89%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3.html ; low-key light and a unified palette https://studiobinder.com/blog/what-is-motivated-lighting-in-film , https://petapixel.com/2017/02/23/orange-teal-look-popular-hollywood/ ; further sources for establishing positions first in fights, changing moves between ranges, and saving close-ups for the turn are in `combat-closeups.md` section 13 and `shot-grammar.md` section 10
- Multi-source (sound convention): J and L cuts https://en.wikipedia.org/wiki/J_cut ; sound layers and subjective sound https://transom.org/2005/walter-murch/ ("about 5 layers per 5 seconds" comes from this piece alone), https://nofilmschool.com/saving-private-ryan-sound-design ; stopping the music before a key line in Japanese animation https://realsound.jp/book/2025/03/post-1958046.html ; the theme song entering at a TV drama climax https://toyokeizai.net/articles/-/421384
- Community (Japanese voice and readings): descriptors and the all-Japanese form https://mkanime.ai/seedance-2-5-prompts ; breathy voice wording https://youmind.com/video-prompts/japanese-dialogue-animation-prompt-9215 ; repeating the voice in every shot, the 焙煎 misreading https://loglog.blue/spicelemon/seedance-2-5/ ; reusing the voice card word for word https://www.seedance.tv/blog/how-to-keep-voices-consistent-in-seedance-2-5 ; kana and number readings https://www.seedance.tv/ja/blog/seedance-2-5-lip-sync-issues ; a pronunciation reference carrying off the voice https://note.com/genel/n/nf329685c68a9 ; humming https://www.cutout.pro/learn/blog-seedance-2-0-audio-guide/ ; dialect labels https://runware.ai/docs/models/bytedance-seedance-2-5/guides/multilingual ; native-speaker checks https://www.seedance.tv/blog/seedance-2-5-supported-languages
- Basis for inference: role language (Kinsui Satoshi) https://www.jpf.go.jp/j/project/japanese/teach/tsushin/bookshelf/201111.html ; https://www.kinokuniya.co.jp/f/dsg-01-9784000068277
- Author-tested: the author's production notes, 2026-10-28 (camera habits, 50–65mm close shots, 10–15° short arcs, "backlit" producing a halo, "loudly" raising pitch, ambience written to the last second, 飯 → メシ, two voice references, character voices and lines). Test run: sample-run notes, 2026-10-28 (the hard cut at 7.38 s).
