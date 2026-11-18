# Seedance 2.5: 30-second examples and templates

## When to read this file

Read it when you are writing a 30-second prompt from scratch and want a ready-made structure to start from. Every example is an original, complete prompt that shows one structure. Borrow the structure and rewrite the content for the user's request; do not carry the people, cities, or props of an example into an unrelated video.

The examples here are general human or animal subjects. Anthro scenes with Japanese dialogue have their own complete examples: dialogue in `kemono-jp-drama.md` section 5, fights in `combat-closeups.md` section 10, and one prompt per art-style line in `shot-grammar.md` section 8. When you apply a structure from this file to anthro characters, write the lines in the original Japanese with the label "Japanese", and add species anatomy and identifying traits as in `kemono-jp-drama.md` section 1.

All examples follow these rules (basis in section 11):
- The prompt states only the wanted state; exclusions are rewritten as positives [author-tested: negative wording damages detail; the official sd25-pe skill also adds no generic negative constraints automatically].
- Aspect ratio, total duration, resolution, frame rate, and the sound switch go in "Platform settings:" after the code block, never in the prompt [official sd25-pe]. Time ranges such as "0–7 s" are creative content and stay in. Default to a 480P or sample-mode test first, then 720P once it works [author-tested].
- Sound symbols: music (), sound effects <>, dialogue {}, subtitles 【】 [official]. Section labels are plain words with a colon, dialogue goes only in {}, and when marking sound effects with <>, character names take no angle brackets [official sd25-pe].
- Dialogue line: `Name (language, voice, emotion, to whom): {line}`, written in the range where it happens, each line once in the whole clip. Only one person speaks per range; everyone else present "listens quietly with their mouth closed" [official sd25-pe + author-tested].
- Each range has "Ends with: …" as a visible state. In a one-take clip each range opens with "Without cutting, the camera keeps…", and when crossing between spaces the camera's route is written out [test run]. Ambience is written through to the last second [author-tested].

## Contents

1. One take: everyday story (pure text-to-video)
2. Multi-shot drama: 9 shots with dialogue (character and scene images)
3. Product ad: 6 shots (character image + product image)
4. Talking-head recommendation: phone selfie view
5. Action chase: fast cutting + background music
6. Cut to the beat: city tourism promo (@Audio1 sets the beat)
7. First and last frames / multiple keyframes
8. Video editing / video extension / re-shooting a segment
9. Longer than 30 seconds: stitching segments
10. Compact skeleton
11. Sources

## 1. One take: everyday story (pure text-to-video)

Structure notes: five time ranges, with no "Shot N" [single source]; one change and one "Ends with" per range; a 2-second hold at the end. The two lines belong to two people and are split, one speaker per range, into 15–19 s and 19–23 s. Test run (2026-10-28, Jimeng 720P): an older version of this prompt (which still carried "total duration 30 seconds, 16:9" and a string of negative constraints) was hard-cut at 7.38 s, at the boundary between 0–7 s and 7–15 s, jumping from outside the door straight to a front-side position inside the shop; that was the only cut. The two lines landed at 15.7 s and 20.2 s, on time. The backpack drifted from black to dark blue. One extra line appeared at the start (to be re-tested). So this version opens every range with "Without cutting, the camera keeps…", writes the route across the threshold at 7 s, and states under Sound that there are only two lines. When continuity matters more, merge the two lines into one and go back to four ranges.

```text
Overall setup: realistic documentary look: natural light, restrained colour, light grain; a cool-warm contrast of early morning, low sun coming from the street corner at off-screen left. One take: a gimbal-stabilised handheld follow shot, the camera moving continuously, smooth and slow, from the first second to the last; the whole clip is one continuous shot.
One-line summary: early morning at a breakfast shop in an old quarter; the camera follows from across the street into the shop, watches the cook lift the lid off the first steamer of buns and hand them to the first customer, a schoolboy, then follows the boy out and rises to rest on the street corner lit by the rising sun.

Characters and scene:
The cook: a man in his fifties, round face, close-cropped hair, a white chef's cap, a dark blue apron dusted with flour, sleeves rolled to the elbow.
The schoolboy: a boy of about ten, a red school jacket, a plain black backpack.
Scene: a small breakfast shop on a corner of the old quarter; two tiers of bamboo steamers at the door giving off white steam; dough and a rolling pin on a wooden board; outside, a flagstone lane and a few parked bicycles; day is just breaking and the sky grades from deep blue to orange.

Timeline:
0–7 s (establishing, outside): medium-long shot, the camera across the street at door height, pushing slowly forward across the lane; the steam, lit by morning light from off-screen left, billows upward; the cook works at the steamers with his back to the camera. Ends with: the camera one step outside the threshold, medium shot, the cook at centre frame, still with his back to the camera.
7–15 s (through the door, lifting the lid): Without cutting, the camera keeps moving along an arc that bends right: across the threshold into the shop, around from behind the cook to his front right; the cook lifts the lid of the top steamer with both hands, a great cloud of steam rises and reveals neat rows of plump white buns, and he wipes the sweat from his forehead with the back of his hand. Ends with: close shot, the steaming buns filling the lower half of frame, the cook's face behind the steam.
15–19 s (the boy orders): Without cutting, the camera keeps easing back half a step at the cook's front right, bringing the doorway into the left of frame; the boy runs up to the door from outside, out of breath. The schoolboy (English, a clear boy's voice, breathless and happy, to the cook): {Two pork buns, please!} The cook listens quietly with his mouth closed, smiling and nodding. Ends with: the boy standing in the doorway, both hands on the straps of his black backpack.
19–23 s (handing over the buns): Without cutting, the camera keeps a medium close shot, adjusting slightly with the action, focus moving from the buns to the boy's outstretched hands; the cook puts two buns in a paper bag and holds it out. The cook (English, a warm middle-aged male voice, smiling, to the boy): {Careful, they're hot!} The boy, mouth closed, takes the bag in both hands. Ends with: the boy holding the bag in both hands, turning toward the door at frame left.
23–30 s (sunrise at the corner): Without cutting, the camera keeps following the boy left across the threshold, then on the street rises slowly to second-floor height; the boy runs along the flagstones toward the corner at frame left, the sun rises at the end of the street, and golden light fills the whole lane and the drifting steam. Ends with: high long shot, the boy's small figure in the sunlight, the frame holding steady for about 2 seconds.

Sound: the only sounds are ambience, action sounds, and two lines of dialogue. 0–30 s: <the hiss of steam from the steamers>, <a distant bicycle bell>, and <early-morning birdsong> continue to the last second; second 9 <the soft knock of a bamboo lid lifted>; second 21 <the rustle of a paper bag>; from second 24 <the boy's footsteps on the flagstones>. There are two lines in the whole clip; the rest of the time both keep their mouths closed.
Keep consistent: the only two people in the clip are the cook and the boy, and passers-by on the far street are blurred background silhouettes; the cook's cap and apron and the boy's red jacket and black backpack are the same throughout; after leaving, the boy always runs toward the corner at frame left; the picture is clean documentary footage, with text only on signs that belong to the scene; fingers are distinct, and the number of buns in the steamer is stable.
```

Platform settings: 16:9, 30 s, sound on. Make a 480P sample first and look closely at the boundaries at 7 s and 15 s for a cut.

## 2. Multi-shot drama: 9 shots with dialogue (character and scene images)

Structure notes: uses the 9-shot duration split of the official 30-second example (3/3/4/4/4/4/3/3/2 s) [official]. Bind the assets first, then write the subjects and picture requirements, then shot by shot the framing, action, line, and "Ends with". Where the official example writes "strictly exclude", this version uses a positive "Picture and headcount:" instead [author-tested]. For anthro characters do not reuse "natural human eyes" from here; write "the amber animal eyes of @ImageN" [inference, see `kemono-jp-drama.md` 1.2].

```text
Assets:
@Image1: the father's appearance, use only face shape, hairstyle, build, and clothing.
@Image2: the daughter's appearance, use only face shape, hairstyle, and clothing.
@Image3: the high-speed rail platform, use only the spatial structure, canopy shape, and colour tone.

Overall setup: realistic cinematic look, the cool overhead light of an early-morning platform against warm reflections on the train windows; 9 shots, hard cuts between shots, the pace slow, then fast, then settling.
One-line summary: a father sees his daughter off to university in another city from a high-speed rail platform, presses a thermos into her hands just before she boards, and after the doors close the two say goodbye through the window.
Subjects: the father (appearance follows @Image1): about fifty, a dark grey jacket, carrying his daughter's backpack. The daughter (appearance follows @Image2): eighteen, a ponytail, a white sweatshirt, pulling a light blue suitcase.
Picture and headcount: the picture is clean realistic cinematic footage, platform signs blurred in the background; the only two main people are the father and the daughter, and travellers far down the platform are blurred background silhouettes.

Shots:
Shot 1 (0–3 s): extreme long shot, high camera looking down on the platform, a white high-speed train standing still; father and daughter walk in from frame right, very small. Ends with: the two reaching the centre of frame.
Shot 2 (3–6 s): medium follow shot, the camera backing away ahead and to the side of them; the daughter pulls her suitcase, the father walks on her left carrying the backpack, both with mouths closed. Ends with: the two slowing in front of the carriage door.
Shot 3 (6–10 s): close shot of the daughter; she stops and looks back. The daughter (English, a clear young female voice, forcing lightness, to her father): {Dad, this is far enough.} The father, off-screen, listens quietly with his mouth closed. Ends with: the daughter closing her mouth, looking at her father.
Shot 4 (10–14 s): close shot of the father; he nods, unzips the backpack, and takes out a silver thermos. The father (English, a low middle-aged male voice, quiet, a little clumsy, to his daughter): {It's hot water. For the ride.} The daughter, off-screen, listens quietly with her mouth closed. Ends with: the father holding the thermos out to her.
Shot 5 (14–18 s): close-up, the thermos passing from the father's rough hand into the daughter's, the two hands touching briefly. Ends with: the thermos in the daughter's hands only.
Shot 6 (18–22 s): medium shot, the daughter boards, the door closes behind her, she turns and comes close to the window. Ends with: the daughter standing inside the window, both hands around the thermos.
Shot 7 (22–25 s): over-the-shoulder shot from inside the carriage, her blurred shoulder in the foreground; the father stands on the platform waving, working to lift the corners of his mouth. Ends with: the father's hand stopped in mid-air.
Shot 8 (25–28 s): close shot of the daughter through the window; she hugs the thermos, her eyes red, tears held at the rims, and waves gently. Ends with: her palm flat against the window glass.
Shot 9 (28–30 s): long shot, the train pulls slowly away out of frame left, the father alone at the centre of the platform, the frame holding steady. Ends with: only the father's back on the platform.

Sound: the only sounds are ambience, action sounds, and two lines of dialogue. 0–30 s: <the blurred voice of a platform announcement> and <the low hum of the train's air conditioning> continue to the last second; seconds 3–6 <suitcase wheels rolling on the floor>; second 20 <the pneumatic sound of doors closing>; second 28 <the train pulling out>. There are two lines in the whole clip; the rest of the time both keep their mouths closed.
Keep consistent: both people's looks, clothing, the suitcase, and the thermos are the same throughout; on the platform the father is always on the daughter's left; the train always leaves toward frame left; both have natural human eyes with a soft catchlight.
```

Platform settings: 16:9, 30 s, sound on.

## 3. Product ad: 6 shots (character image + product image)

Structure notes: hook → pain point → product enters → key turn → emotional peak → product end frame. The product image gets "keep the shape strictly". Brand text is added in post: the prompt says only "a clean empty area above", and notes like "reserved for post" stay outside the prompt [official sd25-pe: write only what can be submitted]. The voice-over is written in the shot where it happens [author's convention].

```text
Assets:
@Image1: the lead's appearance, use only face, hairstyle, and clothing.
@Image2: the product, white wireless noise-cancelling earbuds and charging case; keep shape, colour, material, and indicator-light position strictly.

Overall setup: urban commercial look, the cool tones of rush hour against the warm tones of a quiet moment; 6 shots, hard cuts between shots.
One-line summary: in a packed, noisy rush-hour subway the lead puts in the earbuds of @Image2, the world goes quiet at once, and she finally relaxes into a smile.

Shots:
Shot 1 (0–3 s, hook): close-up, swaying hand straps and shoulders pressed together in a subway car, slight handheld shake. Ends with: one strap swinging to the centre of frame.
Shot 2 (3–9 s, pain point): medium close shot, the lead (@Image1) squeezed against the door, frowning with her eyes shut, a passenger beside her talking into a raised phone; the camera pushes slowly in on her face. Ends with: she opens her eyes and looks down at the charging case in her hand.
Shot 3 (9–15 s, product enters): close-up, her thumb flips open the charging case of @Image2 and she takes out an earbud, the indicator light coming on; macro lens, shallow depth of field, soft highlights on the product's surface. Ends with: the earbud at her fingertips, near her right ear.
Shot 4 (15–20 s, key turn): close shot, she fits the earbud into her right ear; at second 16 the surrounding noise cuts off at once, leaving only her soft breathing; the crowd in the car becomes gentle slow motion. Ends with: her shoulders dropping.
Shot 5 (20–26 s, emotional peak): medium shot, the camera slowly orbits her half a circle, the city sliding past the window turned warm gold by morning light; she leans by the door, mouth closed, its corners lifting at ease. Voice-over (V.O., English, a gentle young female voice, calm, to the audience): {Put the world on mute.} Ends with: her looking out the window, morning light on her face.
Shot 6 (26–30 s, product end frame): close-up, the earbuds go back into the charging case and the lid closes; the product sits centred in the lower half of frame with a clean pale empty area above it, the frame holding steady. Ends with: the charging case at rest, centre frame, slightly low.

Sound: 0–15 s: <wheels grinding on rails>, <a station announcement>, and <voices in the car blurred into one mass>; from second 16 these cut off, leaving only <her soft breathing> and a very faint room tone, continuing to the last second; second 27 <the crisp click of a lid closing>. The only line in the clip is the voice-over in shot 5.
Keep consistent: the product's shape, colour, and indicator-light position match @Image2, and the only brand item in frame is the product of @Image2; the picture is clean advertising footage, with the area above in shot 6 kept empty; the lead's appearance is the same throughout; when she holds the earbud her fingers sit flush on its surface, and the earbud sits securely in her ear with a clear edge.
```

Platform settings: 9:16, 30 s, sound on; brand text and logo are composited in post onto the empty area in shot 6. Portrait produces subtitles more readily than landscape [official 2.0]; if they appear, remove them with video editing [official].

## 4. Talking-head recommendation: phone selfie view (one take)

Structure notes: the camera is a selfie view from start to finish. Lines are short and colloquial, and each fits its allotted time. Reactions are written as visible actions (raised eyebrows, a nod), not "her eyes light up" [author-tested]. The call to action comes last.

```text
Assets:
@Image1: the creator's appearance, use only face, hairstyle, and clothing.
@Image2: the product, a mint-green portable blender cup; keep shape, colour, and button position consistent.

Overall setup: a real phone front-camera selfie view (UGC style): the creator holds the phone in one hand at arm's length, with slight natural shake; a home kitchen, mid-morning daylight from a window at off-screen left; one take, the same continuous selfie shot throughout.
Characters and scene: the creator: a woman in her twenties, appearance follows @Image1, relaxed and natural, as if chatting with a friend. Scene: a bright home kitchen; on the counter a cutting board, orange chunks, a bowl of ice, and the blender cup of @Image2.

Timeline:
0–3 s (opening hook): the creator leans in to the lens and raises one eyebrow. The creator (English, a bright young female voice, exaggerated, to camera): {Stop buying bottled juice!} Ends with: her moving the phone back a little.
3–10 s (prep): Without cutting, the camera keeps the selfie view, the counter entering the lower half of frame; she drops orange chunks and a few ice cubes into the cup. The creator (English, a bright young female voice, casual, to camera): {Orange chunks in, a little ice.} Ends with: the cup holding orange chunks and ice.
10–18 s (demo): Without cutting, the camera keeps the selfie view; she lifts the cup to the lens and presses the button, and the fruit spins fast and turns to juice. The creator (English, a bright young female voice, pleased with herself, to camera): {One press, thirty seconds.} Ends with: even orange juice in the cup.
18–26 s (tasting): Without cutting, the camera keeps the selfie view; she opens the lid and takes a sip, pauses half a second, her eyebrows go up, the corners of her mouth lift, and she nods twice. The creator (English, a bright young female voice, surprised, to camera): {It really tastes fresh-squeezed.} Ends with: the cup resting beside her chin.
26–30 s (call to action): Without cutting, the camera keeps the selfie view; she holds the cup up beside her face and smiles at the lens. The creator (English, a bright young female voice, friendly, to camera): {Link's in the comments.} Ends with: a waist-up frame of her and the product together, holding steady.

Sound: the only sounds are the creator's voice and real kitchen ambience. 0–30 s: <faint kitchen room tone> continues to the last second; second 6 <ice cubes clinking>; seconds 11–14 <the hum of the blender motor>; second 19 <the soft pop of a lid opening>. There are five lines in the whole clip, lip-synced to the words.
Keep consistent: the phone front-camera selfie view holds throughout; the only product in frame is the blender cup of @Image2, its shape matching @Image2; the picture is clean phone selfie footage; when she grips the cup her fingers sit flush on its body, with a clear edge between hand and cup.
```

Platform settings: 9:16, 30 s, sound on.

## 5. Action chase: fast cutting + background music

Structure notes: 11 shots, cut points on the action (take-off, landing, turn). Screen direction holds through the whole chase. Background music is written in () with its start and end seconds. The crow is an ordinary animal, written as "it makes only crow calls, and the lines are spoken only by Jay", which is the positive way to say "the animal does not talk" [official: state who speaks; the positive rewording is inference]. For anthro stand-offs, strikes, and weapon fights see `combat-closeups.md`.

```text
Overall setup: realistic action-film look, low golden evening sun from off-screen right putting a bright rim on the figures; 11 shots, hard cuts between shots, cut points on the action (take-off, landing, turn), fast first and slower at the end.
One-line summary: across the rooftops of a dense urban village a young man chases, parkour-style, a crow that has made off with his keys, finally trades half a piece of bread for them, and sits side by side with the crow on a roof watching the sunset.

Characters and scene:
Jay: a man in his early twenties, short hair, a yellow T-shirt, dark grey joggers, white trainers; his key ring hangs on a red lanyard.
The crow: a black crow with glossy feathers, an ordinary bird that makes only crow calls, carrying Jay's red-lanyard key ring in its beak.
Scene: tightly packed urban-village rooftops, corrugated metal roofs, air-conditioner units, bedsheets on washing lines, old TV aerials, gaps about a metre wide between buildings; towers and the setting sun in the distance.

Shots:
Shot 1 (0–2 s): close-up, the crow picks the red-lanyard key ring off a windowsill and flaps away toward frame right. Ends with: the crow leaving frame right.
Shot 2 (2–4 s): close shot of Jay, leaning out of the window, eyes wide. Jay (English, a clear young male voice, urgent and forceful, to the crow): {Hey! My keys!} Ends with: one hand braced on the windowsill.
Shot 3 (4–7 s): wide shot, Jay climbs out of the window onto the roof and runs toward frame right. Ends with: him reaching the first air-conditioner unit.
Shot 4 (7–10 s): FPV view flying low right behind Jay; he vaults two air-conditioner units in a row, the camera rising and falling with his jumps. Ends with: him sprinting at the gap between buildings.
Shot 5 (10–13 s): low camera looking up, Jay leaps the gap between two buildings from left to right; the moment he is airborne turns to slow motion (a speed ramp), returning to normal speed on landing. Ends with: both feet planted firmly on the opposite metal roof, knees bent to absorb it.
Shot 6 (13–16 s): side tracking shot, the camera moving right parallel with Jay; he ducks under white bedsheets lifted by the wind on a washing line. Ends with: the sheets falling back into place behind him.
Shot 7 (16–19 s): medium shot, the crow lands on an old TV aerial and cocks its head toward frame left; Jay, in the background, slows down out of breath. Ends with: Jay stopping below the aerial.
Shot 8 (19–22 s): medium close shot, Jay kneels on one knee on the metal roof, takes half a piece of bread from his pocket, and holds his hand out to the crow. Jay (English, a clear young male voice, panting, soft, to the crow): {Trade you?} Ends with: the bread resting on his open palm.
Shot 9 (22–25 s): close-up, the crow hops down from the aerial, drops the key ring on the metal roof, and takes the bread. Ends with: the key ring lying on the metal, the crow holding the bread.
Shot 10 (25–28 s): medium shot, Jay picks up the keys laughing and sits down on the roof; the crow lands a metre from him. Ends with: man and bird sitting side by side, facing the sunset at frame right.
Shot 11 (28–30 s): aerial long shot, the camera pulling back and up, the rooftops of the urban village running together, the small silhouettes of man and bird side by side facing the sunset, the frame holding steady. Ends with: the two silhouettes still at the roof's edge.

Sound: (light plucked strings with drums, about 120 BPM, entering at second 4, fading out at second 22); after second 22 only <wind> and <distant city traffic>, continuing to the last second. Seconds 1 and 23 <a crow's call>; seconds 4–16 <footsteps on metal roofing> and <the hum of air-conditioner units>; second 14 <bedsheets flapping in the wind>; second 23 <the bright clatter of keys on metal>. There are two lines in the whole clip, both spoken by Jay.
Keep consistent: Jay's yellow T-shirt and the keys' red lanyard are the same throughout; during the chase Jay always runs from frame left to frame right; there is only ever the same one black crow; the picture is clean cinematic footage; when Jay lands his legs sit naturally, with clear edges between his body, the roof, and the sheets.
```

Platform settings: 16:9, 30 s, sound on.

## 6. Cut to the beat: city tourism promo (@Audio1 sets the beat)

Structure notes: in the first 20 s, one shot every 2 s (one bar at 120 BPM in 4/4) [inference: arithmetic]; the last 10 s slow into one continuous long take to close. Each scene image covers one landmark only. Signs are kept blurred so the model does not draw wrong lettering [official: limited text ability].

```text
Assets:
@Audio1: background music and beat reference; the whole clip uses this music and cut points follow its drum hits.
@Image1: a cluster of riverside stilt houses at night, use only the building forms and warm gold lighting.
@Image2: a light-rail train passing through a residential block, use only the building structure and track position.
@Image3: a cross-river cable car, use only the cabin colour and the view over the river.

Overall setup: city tourism promo style, warm gold night lighting against a deep blue night sky, a clear and open picture; the first 20 s cut fast on the beat of @Audio1, one shot every 2 s; the last 10 s slow into one continuous aerial long take.
One-line summary: a riverside mountain city built into its slopes, cut from the lanes at nightfall to the whole city with every light on.

Timeline:
0–2 s: close-up, old street lamps beside stone steps coming on one after another. Ends with: every lamp in frame lit.
2–4 s: medium shot, steam rising at the door of a hotpot restaurant, diners' hands raising glasses. Ends with: two glasses touching.
4–6 s: low camera looking up, tier upon tier of stilt houses (see @Image1) lighting up in the dusk. Ends with: the whole cluster ablaze with light.
6–8 s: side tracking shot, a light-rail train passing through the middle of a residential block (see @Image2). Ends with: the tail of the train leaving frame.
8–10 s: FPV view diving fast down a steep stepped alley. Ends with: the camera reaching the mouth of the alley.
10–12 s: close shot, brown-sugar syrup poured over a bowl of ice jelly at a riverside stall. Ends with: syrup covering the surface.
12–14 s: a cable-car cabin (see @Image3) gliding slowly above the river, silhouettes of visitors in its windows. Ends with: the cabin at the centre of frame.
14–16 s: time-lapse, traffic on a river bridge drawing light trails. Ends with: light trails covering the deck.
16–18 s: medium shot, a young person on a rooftop raising a phone to shoot the night view, the screen's glow on their face. Ends with: them pressing the shutter.
18–20 s: whip-pan transition, the camera whipping up to the night sky. Ends with: a frame of deep blue night sky.
20–30 s: continuous aerial long take, the camera starting low over the river, rising slowly and pulling back, the confluence of two rivers and the lights of the whole mountain city gradually filling the frame. Ends with: the wide view holding steady for the last 3 seconds.

Sound: (the music of @Audio1 runs through the whole clip); sound effects are limited to light ambience in sync with the picture: second 3 <the bright clink of glasses>, second 6 <the rumble of a passing light-rail train>, from second 12 <river wind> continuing to the last second; people in frame keep their mouths naturally closed, and the clip has only music and ambience.
Keep consistent: cut points in the first 20 s align with the drum hits of @Audio1; shop signs and street signs sit in the shallow-focus blur, showing only blocks of colour and light, and the picture is clean footage; building structures follow the matching images, with straight, stable lines.
```

Platform settings: 16:9, 30 s, sound on; @Audio1 no longer than 30 s (the total limit for reference audio) [official].

## 7. First and last frames / multiple keyframes

First and last frames: each gets its own standalone role sentence at the very top, "@Image1 is the first frame." "@Image2 is the last frame.", not merged into one sentence [official sd25-pe].

```text
@Image1 is the first frame.
This first frame defines the girl's position, how she sits, the layout of the desk and window, and the camera direction.
@Image2 is the last frame.
This last frame defines her hand reaching out of the window, the snowflake in her palm, and the final close-up composition.
Realistic style, one take.
0–4 s: starting from the first frame, the girl sits at the desk by the window and looks up and out; snow begins to fall outside. Ends with: her gaze resting on the snowflakes outside.
4–8 s: Without cutting, the camera keeps pushing in slowly; she stands, pushes the window open, and reaches out to catch snowflakes, a smile on her face. Ends with: her hand out of the window, palm up.
8–10 s: Without cutting, the camera keeps pushing in to a close-up of her outstretched hand and the snowflake in her palm, moving naturally into the last frame. Ends with: the picture matching the last frame.
Her clothing and the room stay consistent with the first frame; the only sounds are <wind outside the window> and at second 5 <the creak of a wooden window pushed open>, the wind continuing to the last second; the picture is clean footage.
```

Platform settings: duration 10 s, sound on. In first/last frame mode the first frame sets the aspect ratio, and the two images must share one or the last frame is stretched [official sd25-pe].

Multiple keyframes (separate single images align more accurately than a grid [official]):
```text
Use @Image1 to @Image5 in order as keyframes.
@Image1 is the first frame.
@Image5 is the last frame.
Watercolour animation style, one take, with continuous camera movement carrying naturally between keyframes; the whole clip is one continuous shot.
0–6 s: starting from @Image1 (a wheat field at dawn, a little fox poking its head out between the ears of wheat), the camera tracks slowly right with it and reaches @Image2 (the fox drinking, head down, at a stream). Ends with: the fox standing head down at the stream.
6–13 s: Without cutting, the camera keeps following behind the fox; a falling leaf drifts past the lens, and the fox chases it from the stream through the bushes at the wood's edge into a clearing, reaching @Image3 (it and a hedgehog looking at each other). Ends with: the fox and the hedgehog standing face to face.
13–21 s: Without cutting, the camera keeps following the two animals, one behind the other, through a stand of ferns, rising slowly from low down, reaching @Image4 (a hillside at dusk, the backs of the two animals). Ends with: the two animals side by side on the hillside.
21–30 s: Without cutting, the camera keeps pushing in slowly as the light fades, and finally settles on @Image5 (at sunset, the fox curled up asleep in a tree hollow). Ends with: the picture matching @Image5, holding steady.
The fox's fur colour, build, and blue scarf stay consistent throughout; each keyframe's picture appears near its time. The only sounds are <wind rustling through wheat and leaves> and <birdsong in the woods>, continuing to the last second.
```

Platform settings: 30 s, sound on; @Image1 sets the aspect ratio [official], and all 5 keyframes are made at the same ratio (for example all 16:9) [inference].

Storyboard grids (15 panels or fewer [official]): first write "@Image1 provides the shot order and rough composition of a nine-panel storyboard, read left to right and top to bottom; use only the shot order and composition" (the positive form of the official sd25-pe wording), then the overall story, then fill in per panel the action, camera, and style the board lacks. Put little text on the board; text on the image can be carried into the video [official].

## 8. Video editing / video extension / re-shooting a segment

An edit takes one source video as its only master and states the goal, the scope limited by timestamps, and what stays as it is. An extension first states the state of the boundary frame [official sd25-pe]. Split complex changes into several simple edits [official FAQ].

Replacing a prop:
```text
Edit the video: use @Video1 as the only master.
Edit goal: replace the paper map in the lead's hands at 8–14 s with a black phone.
Edit scope: change only this prop within 8–14 s; the phone keeps the timing, hand movement, occlusion, and exit of the original map.
Keep as is: the person's face, clothing, movement, and expression, and the background, camera position, light, and all sound; apart from this prop, every other visible person, prop, and background element in @Video1 stays as it is.
```

Platform settings: an edit keeps the aspect ratio and basic duration of @Video1, and the output may be a few tenths of a second shorter; source videos of 20 s or less work best [official]. On the Jimeng web page, go by the editing entry shown in the interface.

Replacing the background:
```text
Edit the video: use @Video1 as the only master and replace the background, an office, with the seaside terrace in @Image1. Change only the area outside the person's outline; the person's face, hairstyle, clothing, movement, lip movement, and lines stay as they are; adjust the ambient light on the person to the light direction of the new background so the picture looks like a single shoot.
```

Platform settings: as above.

Changing a line (audio edit):
```text
Edit the video: use @Video1 as the only master and change only the lead's line at 3–6 s to: The lead (English, keeping the original voice and tone): {I'll be right back.} Keep the length of her speech, with lip movement changing to match the new line; the picture, background sound, and other lines stay as they are.
```

Platform settings: as above. Japanese lines work the same way: the label says "Japanese" and {} holds the original Japanese; a complete example of changing one of Kael's lines is in `kemono-jp-drama.md` 2.5.

Extending forward in time (state the end of the source video first):
```text
Extend @Video1 from its end.
The first frame of the extension continues directly from the last frame of @Video1: the girl stands at the rooftop railing with her back to the camera, the reel of a red kite in her right hand, the setting sun at frame right, the camera in a medium shot moving slowly right, the ambience wind and distant traffic.
0–5 s: Without cutting, the camera keeps moving right to her side; the kite flies steadily high up, and she looks back toward frame right and smiles. Ends with: her standing side-on, the reel still in her right hand.
5–10 s: Without cutting, the camera keeps pulling back slowly to a wide shot; a small boy runs in from frame right, she puts the reel in his hands, and both look up at the kite. Ends with: the reel in the boy's hands only, the two shoulder to shoulder with heads tilted back.
The only sounds are <wind> and <distant traffic>, continuing to the last second. The girl's clothing, the kite's colour, and the light continue from @Video1, and the whole clip is one continuous shot; the girl, the boy, and the kite are each the same continuous object throughout: one girl, one boy, one kite.
```

Platform settings: extension length 10 s, sound on; the aspect ratio follows @Video1 [official]. The official extension example recommends MOV output, and extending a video generated by Seedance 2.5 itself joins most naturally [official].

Extending backward in time (write the first frame of the source video as the end state):
```text
Extend @Video1 from its start.
The extension happens before @Video1 begins: the girl pushes open the iron door to the rooftop and steps out with the folded kite in her hand, walks to the railing, and launches the kite; during this time the girl is the only person in frame.
The last frame of the extension matches the first frame of @Video1: she stands at the railing with her back to the camera, the reel in her right hand, the kite already in the air.
The only sounds are <wind>, <distant traffic>, and at second 1 <the creak of an iron door pushed open>; wind and traffic continue to the last second. The girl is the same continuous object throughout, her clothing and the kite matching @Video1.
```

Platform settings: extension length 8 s, sound on; the aspect ratio follows @Video1 [official].

Re-shooting a segment (a feature of the Xiaoyunque app [official: Xiaoyunque handbook]; whether the Jimeng web page has an equivalent was not confirmed in the research): cut out only the segment that needs changing, and change only one of expression, action, or prop at a time. Write the instruction as "in this segment, change ___ from ___ to ___; keep everything else as it is".

## 9. Longer than 30 seconds: stitching segments

Write clip 1 to 30 s, with a stable, joinable end state in its last range, for example:
```text
23–30 s (close): … Ends with: medium shot, the lead standing at the middle of the footbridge, a closed blue umbrella in her left hand, facing frame right, the street lamps just on, light rain falling; the camera still.
```

Export the last frame of clip 1 (the API can return the last frame directly [official]) and use it as the first frame of clip 2:
```text
@Image1 is the first frame.
Realistic cinematic style, a rainy evening street: cool blue tones, the warm light of street lamps, fine rain, reflections on the ground.
Character: the lead, appearance matching the first frame: a white trench coat, shoulder-length hair, a blue umbrella.
0–6 s: starting from the state of the first frame, she turns and walks down the steps of the footbridge… Ends with: …
The only sounds are <fine rain>, <distant traffic>, and <her footsteps>, continuing to the last second.
```

Platform settings: 30 s, sound on; in first-frame mode the first frame sets the aspect ratio, the same as clip 1 [official].

You can also use "extend from its end" on clip 1 directly (see section 8). Long conversations and dialogue scenes that build emotionally suit extension into one continuous long take; fights suit separate segments cut together [official 2.0]. Every clip declares the characters, clothing, light, and sound again and attaches again the reference images of every character on screen; the previous clip's last frame is only for fixing positions [author-tested]. Never write "as above" or "same as the previous clip" in a prompt: the model cannot see the previous clip.

## 10. Compact skeleton

A blank version of the structure above, for quick drafting. Brackets are slots to fill, not text to submit.

```text
Overall setup: [style, described by visible traits], [light: where the source is, e.g. "low sun from off-screen left"]. One take: the camera keeps moving from the first second to the last. (Multi-shot: N shots, hard cuts between shots.)
References: @Image1: [character], use only [face, fur or hair, outfit]. @Video1: use only the camera move and rhythm of [a–b] s. @Audio1: [character]'s voice / the beat.
One-line summary: [who] in [where] [does what]; ends on [final frame].
Characters and scene: [species, one trait only this character has, clothing, props; or "appearance follows @Image1"]. [Space, key objects, light direction, time of day].
Timeline:
0–6 s (setup): [framing and angle]; [subject's start state and action]; [camera move]. Ends with: [visible end state].
6–14 s (development): Without cutting, the camera keeps [route through the space, e.g. "moving across the threshold into the shop"]; … Ends with: …
14–23 s (turn / climax): … [Name] ([language], [voice], [emotion], to [listener]): {[line]} [Other character] listens quietly with his mouth closed. Ends with: …
23–30 s (payoff): Without cutting, the camera keeps …; holds on [final frame] for 2 seconds.
(Multi-shot: "Shot 2 (6–14 s): hard cut, [framing] … Ends with: …")
Sound: the only sounds are ambience, sound effects, and the written lines. 0–30 s: <[ambience source]> continues to the last second; second [N] <[sound effect]>. Music only if wanted: ([style], [tempo], second [a] to second [b]). [N] lines in total, each written once in its own range.
Keep consistent: the same face, fur or hair, outfit, and props throughout; exactly [N] characters, one of each on screen; screen direction stays left to right; clean footage, with text only on signs that belong to the scene; hands keep a clear, stable structure.
```

Platform settings: 30 s, 16:9, sound on. Duration, aspect ratio, resolution, and the sound switch go in the platform UI or API fields, outside the prompt.

## 11. Sources

Research date 2026-10-28. Entry points and parameters on the Jimeng web page may differ from the Ark API docs; go by the interface [multi-source].

- Official: Volcano Ark, Seedance 2.5 prompt guide (duration split of the 30 s 9-shot example, first/last frames and keyframes stated in the first sentence, grids of 15 panels or fewer with little text, keyframes more accurate than grids, keywords for editing and extension, stating the last-frame state before extending, MOV output in the extension example, splitting complex tasks, subtitle FAQ) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide
- Official: Volcano Ark, Seedance 2.5 tutorial (sound symbols, reference audio totalling 30 s or less, edits locking aspect ratio and duration with slightly shorter output, returning the last frame) https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5
- Official: sd25-pe skill 0.1.1 (parameters stay out of the prompt, write only what can be submitted, no automatic generic negative constraints, the exact sentence "@ImageN is the first frame.", the first frame locking the aspect ratio, first and last frames sharing a ratio, closed scope for edits, single instances in extensions, listening with mouth closed in multi-person dialogue, <> and character names, source videos of 20 s or less for edits) https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip
- Official: Xiaoyunque, Seedance 2.5 official handbook (segment re-shoot is a Xiaoyunque feature) https://www.xiaoyunque.com/tutorials/seedance-2-5
- Official (2.0 guide, not restated for 2.5): landscape gives fewer subtitles than portrait; extension for dialogue scenes, separate segments for fights https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-0-prompt-guide
- Test run: 2026-10-28, Jimeng Seedance 2.5 in final mode, 720P, 30 s, the breakfast-shop one take (hard cut at 7.38 s, lines at 15.7 s and 20.2 s, backpack colour drift, an extra line at the start still unconfirmed), from the sample-run notes. The test used the Chinese version of the prompt.
- Author-tested: the author's production notes, 2026-10-28 (negative wording damages detail, "her eyes light up" rewritten as visible action, ambience written to the last second, "backlight" producing glow, re-attaching references in every clip, the last frame used only to fix positions, 480P and 720P credit costs).
- Single source (third party): Morphed (time ranges instead of "Shot 1/2/3" for one-take clips) https://morphed.app/blog/seedance-2-5-prompts
- Inference: one bar at 120 BPM in 4/4 = 2 s (arithmetic); the wording for anthro eyes; one aspect ratio for multiple keyframes; the positive wording for animals such as the crow that "do not talk".
