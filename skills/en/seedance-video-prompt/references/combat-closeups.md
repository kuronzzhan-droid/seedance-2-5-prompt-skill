# Fights, close-ups, and camera moves (anthro characters, Seedance 2.5)

## When to read this file

- The clip has a stand-off, a strike, a block, a chase, or weapons clashing.
- You want high-impact techniques: orbit, crash zoom, whip pan, FPV, speed ramp, impact frames, speed lines, smears.
- You need close-ups of eyes, claws, a hand on a hilt, a foot on planks, ears, a tail, a scar, or a rack focus or low angle.
- A generated fight came out with scrambled direction, a deformed weapon, a character on all fours, or was blocked by moderation.

General wording for dialogue and character consistency is in SKILL.md; this file covers fights and close-ups only. The examples use the example cast; any detail their profiles do not record is written "as in @Image N". Example plots only demonstrate the wording.

Tags: [official] = Volcengine Ark, Pippit, or Dreamina documentation and the official sd25-pe skill; [multi-source] = two or more non-official sources agree; [single source] = one source only, including the author's own tests; [inference] = derived from the material, not yet tested. Most anthro-specific wording is inference, so before a final render test the hardest stretch on its own at 480p or in draft mode.

## Contents

1. Three overall principles
2. Writing one exchange clearly
3. Rhythm and impact
4. Camera-move phrase bank
5. Screen direction and the axis
6. Keeping weapons, clothing, and limbs stable
7. Compliant staged combat
8. The close-up toolbox
9. A 30 second fight rhythm table
10. Three paste-ready fragments
11. Complex moves and partial redo
12. Troubleshooting
13. Sources

## 1. Three overall principles

1. **One attack-and-defence exchange per range, with "Ends with" written.** A time range is an event budget, not a frame-accurate cut point; too much in one range causes over-cutting or dropped plot [official].
2. **One main camera move per range.** Asking for push, pull, pan, and track at once makes the picture unstable [official]. For variety, hard cut to a different move between ranges [multi-source].
3. **Write effects as things that happen in the picture.** Impact frames, speed lines, and smears are animation terms; "impact frame" and "speed lines" do not appear in the official docs [inference: not found in this search], so state what is seen, for how long, and how many times.

## 2. Writing one exchange clearly

Write five things per exchange. Community Seedance 2.5 skills, Japanese fight guides, and the official Pippit knight example all break it down this way [multi-source]. The "Starts with / Main event / Ends with" structure comes from official sd25-pe [official].

| Element | What to write | Example |
|---|---|---|
| Initiator | Who strikes first, who defends | Kern.V strikes first, Wachhund defends |
| Start and distance | Where each stands, how far apart, which foot carries the weight | The two are about five paces apart, Kern.V's weight on his back foot |
| Path | From where to where, with which hand, along what line | Kern.V bursts three steps from right to left, the throwing knife in his right hand driving in a level straight line at Wachhund's shoulder |
| Contact point | On a weapon, on armour, or on a blocking arm | The knife tip strikes the middle of the longsword blade |
| Result | Written as "Ends with": distance, who holds the weapon, weight, left/right position | Ends with: Kern.V knocked back one step, the knife still in his right hand, the two about three paces apart |

- One exchange per 2–4 second range [inference]. For a combination, write at most three numbered beats in one range, "first strike / second strike / third strike", each a different move [inference, based on the official Pippit knight example].
- Do not control a combination's frequency with timestamps ("three punches in one second"); write numbered beats [official].
- Keep action general, give detail only to the one or two most memorable moves, and write each action once [official].

| Counter-example (for contrast only) | Positive rewrite (paste-ready) |
|---|---|
| Kern.V spins, jumps, and kicks three times, leaving Wachhund's face covered in blood. | Kern.V uses the momentum of his turn for one spinning back kick, his instep sweeping at Wachhund's silver pauldron; Wachhund is knocked back half a step and a little dust rises from the flagstones under his feet; Kern.V lands with his feet set apart front and back, torso upright, the throwing knife still in his right hand. |

## 3. Rhythm and impact

Japanese hand-drawn fight rhythm is "hold, burst, hold" (tame and tsume): freeze to gather before the strike, burst through very few poses, then freeze again on the follow-through [multi-source]. Readable film fights are likewise "pause, a run of attack and defence, pause" [multi-source]. Each wording below can go straight into the matching shot.

| Technique | Paste-ready wording | Notes |
|---|---|---|
| Wind-up → burst | Before the strike the two hold still for about 1 second: weight on the back foot, shoulders, back, and neck fur tense, only fur tips and hems moving in the wind; the next instant he bursts forward, and only the opening pose and the finishing pose are visible; after the finish he holds for half a second | "About 1 second" and "half a second" are soft targets; 2.5 honours integer-second timestamps only [official] |
| Impact frame, anime | At the instant of the hit the picture flashes a single frame in inverted black and white, then returns at once to the original colours; this is the only flash in the clip | The animation term is "shock frame" [multi-source]. Japanese broadcast guidelines limit flashing and high-contrast inversion to no more than 3 times a second in principle [single source, primary document], and the model flashes on its own, so state it happens once |
| Impact frame, hand-drawn ink | At the instant of contact the picture becomes a single frame of black ink line on white paper, then returns at once to pale colour wash; this is the only flash in the clip | The monochrome impact frame translated into the hand-painted fantasy line's medium [inference] |
| Impact frame, realistic | At the instant of the hit the picture pauses for about half a second, and the camera shakes once with the impact, then steadies | Pippit mecha example: "the hit lands extremely fast, followed by a half-second pause", "a slight shake after the freeze" [official] |
| Freeze | At the instant the blades cross the picture freezes for 1 second, then resumes | Relative time such as "freezes for 1 second" is officially supported [official] |
| Speed lines | Anime: during this strike the background becomes white speed lines along the direction of the charge, returning to the original background on the finish. Hand-drawn: several thin ink speed lines trail behind the weapon. Realistic: the background streaks into motion blur along the direction of movement | Anime wording [multi-source]; motion blur for a realistic style [inference] |
| Smear | The swinging arm and blade stretch into a curved afterimage trail, while the face and eyes stay sharp and stable | A smear is a distorted drawing that creates the illusion of motion [multi-source]. One third-party guide warns that smears distort the face along with the limb, so give them to the arm and weapon only [single source] |
| Speed ramp / slow motion | Only this strike slows: from the moment the blade touches the throwing knife it slows markedly for about 1 second, sparks hang in the air, then it snaps back to real-time speed; everything else is real-time speed | Give it to only 1–2 decisive contacts per clip [multi-source]. State where it slows, where it resumes, and what image it stops on [official] |
| Cutting on action | Hard cut to a close shot midway through Wachhund's parry of the knife; the next shot picks up the second half of the same parry | Write the cut as an action event that lands in motion, not on a still pose [multi-source]. Leave frame-accurate cuts to post [official: time ranges are a budget] |
| Impact shake | On the hit the camera shakes once with the impact and steadies at once | Pippit mecha example [official] |

- Replaying one strike from two or three angles (repeat cuts) is common in Japanese animation [multi-source], but official advice is to write each action once [official]. For that effect, duplicate the shot in an editor afterwards.
- The sound can drop out before a key strike, but state the second it returns, for example "at second 20 the wind drops out, leaving only the two characters' breathing; at second 21 <a metallic clash> lands and the wind returns, continuing to the last second". Using silence to set off an impact is a convention of animation and film [multi-source]. In the author's tests, when ambience was not written to the last second the second half could go silent [single source, author-tested].

## 4. Camera-move phrase bank

Formula: move name + subject it acts on + start point + direction + end point [official]. One per range. Handheld counts as one, so do not stack an orbit or crash zoom on it [multi-source]. In the examples Wachhund is on screen left and Kern.V on screen right.

| Move | Use | Paste-ready wording | Basis |
|---|---|---|---|
| Orbit | Decisive clash, reveal | Centred on the point where the two blades meet, a medium shot orbits slowly to the right through about 60 degrees and stops; it is one continuous shot and ends on the original side of the line between the two | State centre, direction, angle [official]; starting from the side with an arc under 90 degrees stays on the same side of the line [inference] |
| Short arc | Stand-off, before and after a line | Close shot, the camera arcs slowly to the left around Kael through about 15 degrees and settles | The author's usual 10–15° arc [single source, author's habit] |
| Crash zoom | The moment of impact, pushing to the contact point or the eyes | At the instant of contact the camera crash-zooms in, the frame tightening very fast from a medium shot to a close-up of the contact point, and stops | [multi-source]; niche terms expanded into what changes on screen [official] |
| Whip pan | Between exchanges, turning to the counter-attacker or a reaction | The camera whips fast to the right from Wachhund to Kern.V with horizontal motion blur, and keeps moving right at a similar speed after it arrives | Continue the same direction and speed after the whip [official: Pippit whip-pan transition] |
| FPV | Opening that lays out the space | An FPV view dives from the masthead, skims the deck between two rows of rigging, and slows to a stop beside the two characters | Write path, speed, turns [official] |
| Handheld | Close-quarters grappling | Handheld follows Wachhund with slight shake, the subject sharp; on the hit it shakes once with the impact and quickly steadies | Pippit knight example: "slight handheld shake but the subject stays sharp" [official] |
| Bullet time | Once per clip at most | At the instant blade and throwing knife meet the action nearly freezes, sparks and falling leaves hang in the air, the camera orbits right around the contact point through about 60 degrees, then real-time speed resumes | State which action freezes and the orbit direction [official] |
| Side tracking | Chase, charge | The camera tracks left parallel to Kern.V, who stays in the centre of the frame | The author's usual shot [single source, author's habit]; a centred subject stays readable through fast cuts [multi-source] |
| Low wide angle looking up | Stand-off, the dominant side's entrance | Low wide-angle shot looking up, the sword tip reaching toward the lens enlarged in the foreground, the eaves behind tilting upward | Looking up reads as powerful; action uses wide lenses to exaggerate the foreground [multi-source] |

## 5. Screen direction and the axis

- Fixed wording, repeated once per range: "A is always on screen left, facing right; B is always on screen right, facing left; the camera is always on the <fixed object> side of the line between them" [multi-source]. Anchoring to something that does not move (a door, a stone well, a ship's rail) holds better than left and right alone [official].
- After an orbit or bullet time, bring the camera to rest on the original side. If it overshoots, cut to a wide shot to re-establish positions [inference].
- When the two swap places, write the path, for example "Kern.V runs left across the front of Wachhund and stops on screen left". Look-alike characters swap if the blocking is not written [single source, author-tested].
- Keep one direction of travel through a chase, for example always running from screen left to screen right [multi-source].
- Stand-offs in Japanese animation often put the weaker side on the left facing right and the stronger opponent on the right facing left [single source].
- The author's dialogue scenes use same-side shot/reverse shot without crossing the line; fight coverage likewise keeps the camera on one side of the line throughout [single source, author's habit].
- First person (realistic line): the camera is "my" eyes, so positions are written "directly in front of me / on my left". When someone steps between me and the opponent, state which side they enter the frame from [inference].

## 6. Keeping weapons, clothing, and limbs stable

| Risk | Positive wording (paste-ready) | Basis |
|---|---|---|
| Weapon deforms or lengthens | There is only this one longsword in the whole clip; its blade is straight and rigid, its length stays the same, and it stays in Wachhund's hands | Give props a count and an owner [official]; state rigidity and length [single source] |
| Weapon changes hands or owners | The longsword belongs only to Wachhund; the throwing knives belong only to Kern.V, with their look and number as in @Image3 | [official] |
| Too many kinds of move | Wachhund uses only cuts and parries; Kern.V uses only straight thrusts and throws | With one attack grammar the model keeps executing the same set of moves [single source] |
| Battle damage inconsistent | The slit cut into the hem of the grey-blue cape stays from the moment it appears to the end | Damage accumulates and never heals [single source] |
| Limbs twist in fast action | One simple action per beat, with more than an arm's length between the two; link actions by momentum: "carrying the momentum of the turn, he brings the sword up" | Add transitions [official]; widen the distance and reduce simultaneous contact; spinning jump kicks and sharp turns deform most [multi-source] |
| Beast-hand anatomy breaks | The hands are clawed beast hands, with finger and claw counts as in the reference, clear and stable in structure; when gripping the sword the claw tips are drawn in against the hilt | [inference] |
| Tail and long fur look solid | On the turn the tail and neck fur swing out with momentum and spring back; on a leap the tail extends straight for balance | [inference] |
| A low stance becomes all fours | Feet set apart front and back, knees bent, torso upright; for a fall write "on one knee, torso upright" | "Half-squatting" produces all fours [single source, author-tested] |
| Becomes a real animal in water | Sil keeps his upright anthro form in the water too, both hands on the sea fork | Gunnar turned into a real orca in the water [single source, author-tested] |
| One character becomes two | Each character appears exactly once in the same frame | Anti-duplicate [official] (the official sentence is negative; this is the positive form) |
| Costume changes between separately generated clips | Re-attach each character's own references to every clip; the previous clip's last frame is used only to fix positions | [single source, author-tested] |

## 7. Compliant staged combat

There are no public violence-moderation rules for Jimeng in mainland China [inference: not found in this search], and moderation outcomes have a random element [multi-source]. The wording below helps compliant fictional fights avoid false positives. It is not for dressing up gore.

| To express | Positive wording (paste-ready) | Basis |
|---|---|---|
| Framing at the start | Staged combat between original adult anthro characters, clean and crisp, like a martial demonstration | [multi-source] |
| A hit | Strikes land on a blade, armour, or a blocking arm; force shows as sparks, dust, scratches in metal, and slits cut in cloth | Pippit knight example "heavy metal clash, sparks flying" [official]; [multi-source] |
| Injury, defeat | Loses balance and steps back twice, drops to one knee with torso upright; the weapon leaves his hand and falls on the flagstones | [multi-source] |
| Overall condition | Both characters' fur, skin, and clothing stay intact and clean throughout | Keep skin, clothing, and props intact when injury is feigned or narrowly avoided [official: sd25-pe] |
| Anger, menace | Both ears pressed flat back, the bridge of the nose wrinkled to show the canines, hackles raised, tail rigid | Emotion as physical detail [official]; the ear and tail channel [inference]; words like "bloodthirsty, biting, ferocious" get blocked easily [multi-source, community] |
| The eyes | The eyes are natural animal eyes with only an ordinary moist highlight | Strong emotion words can make eyes glow [official] |
| Weapon types | Cold weapons: sword, throwing knife, sea fork | Dreamina's guidelines restrict firearms, ammunition, and explosives; cold weapons are not listed [official, international] |

When rejected, remove possibly sensitive wording and retry. Copyright rejections are usually triggered by one full-body reference image; remove that one and retry [single source, author-tested]. The same prompt may also pass on another attempt [multi-source, community].

## 8. The close-up toolbox

- **Cause before effect**: show the trigger in a medium shot first (a blade closing in, the opponent starting to speak), then cut or push to the close-up [official].
- **Few and precise**: at most one detail close-up per exchange [single source]. Save the tightest framing for the turning point, and hold close-ups for less time than wide shots [multi-source].
- **Three-quarter profile for long muzzles**: head-on flattens the muzzle and hides the eyes [multi-source].
- **Avoid very low angles on characters with large manes** (white-maned Bobo, for example): the mane's outline goes odd from below [single source].
- **Little action in hand and claw close-ups**: video models are generally weak at hand close-ups [single source].
- **Make an empty plate first for hard camera positions**: for ground-level low angles and extreme close-ups, generate an empty shot from that position as a reference image [single source, author-tested].
- **Speaking close-ups**: chest-up, camera steady during the line, pulling back to medium afterwards [single source, author's habit], with the whole muzzle in frame [inference]. With 50–65mm for a close shot, also write the visible result "the character reads as three-dimensional, the background moderately blurred"; a focal length can only supplement the visible result, never replace it [official].

| Part | Paste-ready wording | Camera and focus | Where it goes |
|---|---|---|---|
| Eyes | Extreme close-up: the amber eye fills half the frame and the pupil contracts sharply once; it is a natural animal eye with a moist highlight | Eye level, background fully blurred | After the trigger is clear; the moment before the decisive strike |
| Hand on the hilt | Detail close-up: a clawed beast hand grips the hilt, claw tips drawn in against it, the knuckles tightening one by one | Eye level, static | The one-second hold of the wind-up |
| Claws | Close-up: claw tips extend from the fingertips and drag along the flat of the blade, raising a string of small sparks | Side on, static | The instant the claws come out, once per exchange |
| Foot on planks | Low-angle close-up, the camera against the deck planks: a foot (boot or bare, as in @Image2) steps into frame and the plank dips slightly <the dull thud of a step on wood> | Camera at ground level tilted slightly up, sharp wood grain in the foreground | Entrance, opening; leads into "slowly revealed from the feet up" |
| Ears | Close shot: the ears snap toward the direction of the sound, then slowly press flat back | Three-quarter rear | Before the opponent speaks or strikes; Kael's feelings show in his ears first |
| Tail | Medium shot: the tail goes from a gentle sway to rigid and still | Side on, framing wide enough for the whole tail | During the wind-up hold; Gerard's feelings show mostly in ears and tail |
| Scar | Close shot: the old healed scar on Gerard's face (position as in @Image1, described by the character's own left and right), the fur parting to either side of it | Side light, source off-screen to one side | The reset beat, before a line |
| Feather mantle | Kinovi's feather mantle flares all at once, then slowly folds back against his shoulders | Medium shot | The moment his heart rate jumps |
| Blade edge | Extreme close-up: cold light slides along the edge from guard to tip, the blade straight | Eye level, shallow depth of field | The instant before a strike |

Basis for the table: eye and ear reactions [multi-source]; extreme close-ups of animal paws are achievable, and Dreamina's official examples include them [official, international]; the foot on planks is one of the author's usual shots [single source, author's habit]; Kael's ears, Gerard's ears and tail, and Kinovi's "mantle flaring = heartbeat" come from the example cast's profiles [single source, example profiles]; claw, tail, scar, and blade-edge wording [inference].

Rack focus and low angle:

```text
Rack focus: static camera, focus shifts smoothly from Kael's left ear in the foreground to the hyena anthro at the ship's rail in the distance: the ear gradually softens while the hyena anthro goes from blurred to sharp.
Low angle: the camera sits against the ground tilted slightly up, the grain of the planks sharp in the foreground, the character's feet and lower legs filling the lower half of the frame.
```

A rack focus must say from whom to whom the focus moves and how the sharpness of each changes [official]. Looking up makes a character read as powerful [multi-source].

## 9. A 30 second fight rhythm table

A strikes first, B defends. Each range has one exchange and one main camera move, and ends with "Ends with".

| Time | Section | Shot (framing, camera, the one main move) | Action and sound | Ends with |
|---|---|---|---|---|
| 0–3 s | Establish | Wide, low angle, static or slow lateral track | The two face off; establishes left/right positions, the axis, and the anchor; only fur and hems move in the wind; ambience starts at second 0 | The two about five paces apart, weapons held ready |
| 3–6 s | First exchange (one attack, one defence) | Medium, side on, static | A holds about 1 second, then bursts forward; the attack lands on B's weapon; one flash at contact (the only one in the clip) | The two thrown apart, about three paces between them |
| 6–9 s | Counter | Cut midway through the rebound from the parry; close shot, light handheld shake, subject sharp | B uses the momentum for one counter-strike, speed lines or motion blur trailing the weapon | The two facing each other again, weapons pointed at each other |
| 9–11 s | Reaction | Medium first so the cause is clear, then a crash zoom to an extreme close-up of the eyes | The pupil contracts once, both ears press back, whiskers tremble | The close-up holds, the eye sharp |
| 11–14 s | Reset beat (ma) | Medium, static | Open the distance, reset stances, catch breath; if a line is needed it goes here, one short line from one speaker while the other listens quietly with his mouth closed | The two back at the starting distance |
| 14–18 s | Second exchange (three beats) | Medium, side tracking | First strike a thrust, second a horizontal sweep, third a downward cut, all landing on weapon or armour | One side back half a step, weight on the back foot |
| 18–21 s | Decisive strike | Static camera, the only speed ramp in the clip | At contact it slows for about 1 second, sparks and falling leaves hang, then it snaps back to real-time speed | The weapon knocked aside |
| 21–25 s | Outcome | Hard cut; medium shot orbits right about 60 degrees and stops on the original side | A weapon leaves a hand; one side on one knee, torso upright | The two back in their original left and right positions |
| 25–30 s | Close | Wide, slowly pulling back and rising | Weapons lowered; a final line can go here; ambience continues to the last second | The frame holds steady |

- Why 9 ranges: the official 30 second example has 9 shots (3/3/4/4/4/4/3/3/2 s) [official]. Japanese TV animation averages about 3–4 s per shot, so 30 seconds holds 8–10 shots at a comparable density [inference, from multi-source shot counts]. Slow opening, shortest shots at the climax, and a return to longer, calmer shots at the end [single source]. The allocation in this table is [inference], combining the official Pippit knight example (2–3 s per range) with community fight templates.
- For safety, merge into 6 ranges: establish / first exchange plus counter / reaction plus reset / second exchange / decisive strike plus outcome / close. Pippit generally advises splitting 30 seconds into 4–6 parts, otherwise the second half tends to go off course [official]. Every extra range is one more chance of error [inference].
- For music, write genre and timing in (), for example "(low taiko enters at second 18 and stops at second 25)" [official: music uses ()]. The default is "The only sounds are ambience, action sounds, and dialogue".
- Dialogue goes in the reset beat and the close: long lines during intense action tend to scramble lip-sync [inference, based on community experience].
- A one-take fight: compress to 3–4 ranges, open each with "The camera keeps moving and…", and write the camera's path. In one of the author's tests a hard cut appeared at the boundary between two ranges [single source, test run]. Fights can also be generated in parts and cut in post, as officially advised [official].
- Test the densest ranges, 4–7, on their own at 480p or in draft mode first [inference].

## 10. Three paste-ready fragments

Fragments one and three are the opening and ending of the same prompt; fill in 9–18 s from rows 4–6 of the rhythm table. Wachhund and Kern.V have no voice cards in this example, so the fragments carry no dialogue. With voice references, add one line in the reset beat and change the Sound sentence "both keep their mouths closed throughout". Change who wins to suit your script.

### Fragment one: hand-painted fantasy line, establish and first exchange (0–9 s)

Demonstrates: the five elements, wind-up → burst, a single impact frame, cutting on action, an axis anchor.

```text
Style: Hand-painted western fantasy illustration: fine ink outlines, pale colour washes, backgrounds like the background paintings of a hand-drawn animated film; warm golden slanting sun and shafts of light, dark in the near ground, brightest in the middle distance, pale violet-blue far away. Speed is shown with speed lines drawn in fine ink.
References:
@Image1 "German shepherd": use only Wachhund's face, fur colours, and clothing.
@Image2 "longsword": use only the shape, length, and colour of Wachhund's longsword.
@Image3 "black panther": use only Kern.V's face, fur colour, tattoo, bare feet, and throwing knives.
@Image4 "courtyard": use only the layout of the flagstone courtyard, the stone well, and the light.
Characters: The whole clip has only these two characters, both adult male anthros, upright on two legs, with clawed beast hands that are clear and stable in structure.
Wachhund: German shepherd anthro, black-masked face, amber eyes; cream linen shirt, silver pauldron, grey-blue cape; appearance and build as in @Image1. The longsword is as in @Image2, the only one in the clip, its blade straight and rigid, always in his hands.
Kern.V: black panther anthro, gold-green slit pupils, a silver crescent tattoo (position as in @Image3); barefoot; the look and number of his throwing knives as in @Image3.
Scene and positions: A flagstone courtyard with the stone well in the centre of the background behind the two, and the courtyard's wooden gate on the camera's side. Wachhund is always on screen left, facing right; Kern.V is always on screen right, facing left; the camera is always on the gate side of the line between them.
Light: The slanting sun is off-screen back left; shafts of light fall into the courtyard from upper left and draw a warm golden rim along both characters' fur.
Sound: The only sounds are ambience and action sounds; both keep their mouths closed throughout, with only breathing. Wind through the courtyard and leaves scraping the flagstones run from second 0 to the last second; action sound effects are written in their shots.
Shot 1 (0–3 s): Wide, low angle, static. The two face off about five paces apart: Wachhund holds the sword in both hands, its tip angled at the flagstones; Kern.V holds one throwing knife between the fingers of his right hand, feet set apart front and back, torso upright. Both are completely still; only the cape hem and fur tips move in the wind. Ends with: Kern.V's weight on his back foot.
Shot 2 (3–6 s): Medium, side on, static. Kern.V holds for about 1 second, then bursts three steps from right to left, the knife in his right hand driving in a level straight line at Wachhund's shoulder; Wachhund raises the longsword upright in front of his shoulder and the knife tip strikes the middle of the blade. <the crisp metallic ring of a knife striking a blade> At the instant of contact the picture becomes a single frame of black ink line on white paper, then returns at once to pale colour wash; this is the only flash in the clip. Ends with: Kern.V knocked back one step, the knife still in his right hand.
Shot 3 (6–9 s): Hard cut midway through Wachhund's parry, close shot, slight handheld shake, subject sharp. Carrying the force of the parry, Wachhund brings the longsword down in a diagonal cut at the knife in Kern.V's hand, several thin ink speed lines trailing the blade; Kern.V twists aside to his back right, and the edge passes a fist's width from his chest. <the whistle of a blade cutting air> Ends with: the two about three paces apart, squared up again, Wachhund's sword tip pointing at Kern.V.
```

### Fragment two: realistic line, first-person close-up sequence (0–13 s)

Demonstrates: a low-angle foot on planks, a slow reveal from the feet up, a rack focus, a speaking close shot, a background figure with a stated species. The opponent is a character made up for the demonstration. Without a voice reference, delete @Audio1 and describe the voice in words.

```text
Style: Hyper-real cinematic picture with real layered fur, the tips trembling in the sea wind; first-person view, I am a human, and the camera is my eyes. The picture is clean footage.
References:
@Image1 "black wolf head": use only Kael's face, ears, amber eyes, and fur colour.
@Image2 "black wolf full body": use only Kael's clothing, red scarf, red sash, and feet.
@Audio1 "Kael's voice": use only Kael's timbre and way of speaking.
Characters:
Kael: black wolf anthro, amber eyes, red scarf; a black high-collar outfit with a gold bamboo-leaf pattern, tied with a red sash; appearance and build as in @Image1 and @Image2.
Opponent: an adult male spotted hyena anthro sailor, tawny fur with dark spots, a notch missing from his left ear, a curved blade in his right hand.
The whole clip has only three people: Kael, the opponent, and me.
Scene and light: The wooden deck of a ship at dusk, the rail on screen right. The setting sun is low and off-screen front right, drawing a warm rim around the fur of Kael's back.
Sound: Sea wind, rigging slapping the mast, and the low creak of the hull's planks run from second 0 to the last second; Kael speaks the only line in the clip.
Shot 1 (0–3 s): Low-angle close-up, the camera against the deck planks, static. I am lying on the deck, my view running forward along the gaps between planks. Kael's foot steps into frame from the left and stops directly in front of me, and the plank dips slightly. <the dull thud of a step on wood> Ends with: Kael's feet and lower legs in the lower half of the frame, the end of the red scarf hanging down from the top.
Shot 2 (3–6 s): The camera tilts slowly up from his feet, revealing in turn the red sash, the gold bamboo-leaf pattern on the black high-collar outfit, the red scarf lifted by the wind, and finally the black ears upright and facing forward. Ends with: the upper half of Kael's back.
Shot 3 (6–9 s): Static camera. Focus shifts smoothly from Kael's left ear in the foreground to the hyena anthro at the ship's rail in the distance: the ear gradually softens while the hyena anthro goes from blurred to sharp, holding the curved blade across his chest. Ends with: focus resting on the hyena anthro.
Shot 4 (9–13 s): Close shot, chest-up, camera steady. Kael turns his head to a three-quarter profile, his amber eyes natural animal eyes with a moist highlight; before he speaks, the ear on my side turns back once. The hyena anthro in the distance watches quietly with his mouth closed.
Kael (Japanese, the cold low male voice of @Audio1, quiet but forceful, concern held under a tone of command, to me): {下がってろ。……これは命令だ。}
Ends with: Kael turning back to face the hyena anthro, his tail held low and still behind him, the red scarf blown toward screen left.
```

### Fragment three: continuing fragment one, decisive strike and close (18–30 s)

Demonstrates: the only speed ramp in the clip, an orbit that ends on the original side, an outcome written positively, weapon and costume consistency.

```text
Shot 7 (18–21 s): Medium, side on, static, the only speed ramp in the clip. Wachhund bursts two steps from left to right, both hands on the sword, cutting diagonally up from lower left to upper right; at the same moment Kern.V throws the knife in his right hand from right to left. At the instant the blade touches the knife the picture slows markedly, the knife is knocked aside by the blade with a small burst of sparks, and the sparks and wind-lifted leaves hang in the air for about 1 second before it snaps back to real-time speed. <the metallic clash of a blade deflecting a knife> Ends with: the knife spinning toward upper screen right, Wachhund's sword stopped above his right side.
Shot 8 (21–25 s): Hard cut, medium shot, centred on the flagstones between the two, the camera orbits slowly right through about 60 degrees and stops; it is one continuous shot and ends on the gate side of the line between them. The knife comes down and sticks into the wooden post at the courtyard's edge on screen right, its handle quivering; Kern.V, knocked off balance, drops to one knee with his torso upright and his right hand empty; Wachhund's sword tip stops a fist's width from Kern.V's shoulder. <the dull thud of a knife sinking into wood> Ends with: Wachhund still on screen left, Kern.V still on screen right.
Shot 9 (25–30 s): Wide, the camera slowly pulls back and rises to look down. Wachhund lowers the sword, its tip toward the flagstones; Kern.V stands, feet planted firmly on the stone, gold-green slit pupils on Wachhund, ears slowly rising. Both characters' fur, clothing, and the grey-blue cape are intact and clean, the cape hem swaying in the wind. Ends with: the frame holding steady on a high wide view of the two looking at each other three paces apart, shafts of light slanting into the courtyard from upper left.
Consistency: The longsword is only in Wachhund's hands, its blade straight, its length constant; Kern.V's knives, bare feet, and tattoo are the same throughout; both characters' left and right positions are the same throughout; each character appears exactly once in the same frame.
Ambience: wind and leaves scraping the flagstones continue to the last second.
```

## 11. Complex moves and partial redo

- **Action reference video**: write "@Video1 provides only the fight choreography and camera rhythm; character appearance follows @Image1 and @Image3" [official: Pippit asset roles]. Seedance 2.5 does not accept reference images or videos with real human faces [official]: film your own rehearsal with bodies only and faces covered, or use a 3D grey-box. For a grey-box, keeping only the torso is advised; if limbs are included, the full action sequence must be supplied [official], and the same goes for a tail [inference].
- **Beat-by-beat keyframes**: when poses must be accurate beat by beat, generate one beat per image with GPT Image (full body in frame, both feet visible, which hand holds the weapon stated) and open the prompt with "Use @Image1 to @Image N in order as keyframes" [official]. When rough structure is enough, use a clean line-art grid of 15 panels or fewer [official].
- **Partial redo**: when only one stretch is broken, edit those seconds: "Edit @Video1, modifying only Wachhund's sword swing at 8–10 s, changing it to a single diagonal cut from above with the blade straight; all other characters, positions, camera, dialogue, and sound effects stay as they are." Edit inputs of 20 seconds or less work best, and an edit locks the original's duration and aspect ratio [official].
- **Fights in parts, dialogue by extension**: generate fights in parts and cut them; use video extension for long conversations [official: 2.0 guide].

## 12. Troubleshooting

| Symptom | Change this first |
|---|---|
| Attacks with no origin, scrambled direction | Rewrite the exchange with the five elements in section 2 |
| The middle turns to mush | One exchange per range; more than an arm's length between the two; make this beat a wider, shorter shot [multi-source] |
| The sword bends, lengthens, or moves to someone else's hand | Give the weapon its own line: the only one, whose it is, straight and rigid, constant length, with a reference image |
| A character goes on all fours | Change "half-squatting / crouching low" to "on one knee, torso upright" or "feet set apart front and back, torso upright" |
| The two swap sides | Repeat left/right positions and the anchor in every range; end orbits on the original side; write the blocking for any swap |
| A continuous shot is cut at a range boundary | Open each range with "The camera keeps moving and…", write the camera's path, reduce to 3–4 ranges |
| The picture keeps flashing | Write "the only flash in the clip" on the impact frame; at most 1–2 per clip |
| Slow motion everywhere | Name the single speed ramp and write "real-time speed" for the rest |
| Glowing eyes | Remove words like "killing intent, berserk, beast awakening" and write "natural animal eyes with an ordinary moist highlight" [official] |
| Blocked by moderation | Use the positive wording in section 7; remove the triggering full-body reference and retry |
| Bubbling or echo at sea or in rain | State the sounds you want (wind, rigging, creaking planks) and say little about waves, spray, or echo [official: descriptions of water, waves, and echo can bring bubbling or echo noise] |
| Lip-sync scrambled | Move the line to the reset beat or the close, close shot with a static camera, one speaker per range |

## 13. Sources

Official:
- [official] Volcengine Ark, Doubao Seedance 2.5 prompt guide: https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5-prompt-guide (integer-second timestamps, content load, popular camera moves, rack focus, freeze, glowing eyes, water noise, keyframes and grids, editing)
- [official] Volcengine Ark, Doubao Seedance 2.5 tutorial: https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-5 (sound symbols, real-face asset restriction, wording for whip pans and fast cutting)
- [official] Volcengine Ark, Seedance 2.0 prompt guide: https://ark.volcengine.com/region:cn-beijing/docs/seedance-2-0-prompt-guide (one move per shot, transitions between actions, fights in parts and dialogue by extension, externalised emotion, grey-box)
- [official] Volcengine Ark sd25-pe skill 0.1.1: https://arkdocs.tos-cn-beijing.volces.com/skills/artifacts/video-generation/sd25-pe/0.1.1/sd25-pe-0.1.1.zip (Starts with / Main event / Ends with, the camera-move formula, cause before effect, staying intact when injury is feigned, prop ownership, stable objects as anchors)
- [official] Volcengine Ark portrait asset guide: https://ark.volcengine.com/region:cn-beijing/docs/seedance-portrait-asset-guide
- [official] Pippit, Seedance 2.5 handbook: https://www.xiaoyunque.com/tutorials/seedance-2-5 (knight and mecha examples, cut points, whip-pan transition, one side of the axis, reference video for action and rhythm only, 30 seconds in 4–6 parts)
- [official] Pippit, Seedance 2.5 prompt guide: https://www.xiaoyunque.com/tutorials/seedance-2-5-prompt-guide (suggested wording for popular camera moves)
- [official, international] Dreamina Seedance 2.5 page: https://dreamina.capcut.com/seedance/how-to-use-seedance-2-5 ; community guidelines: https://dreamina.capcut.com/clause/dreamina-community-guidelines
- [official] OpenAI image prompting guide: https://developers.openai.com/api/docs/guides/image-prompting (beat-by-beat keyframes, full body in frame)

Community experience with Seedance fights:
- [multi-source] Higgsfield: https://higgsfield.ai/blog/seedance-2-5-prompting-guide (cutting on action, slow motion only on named beats); its "one attack grammar" and "damage only accumulates" are [single source]
- [multi-source] seedance.tv fight guide: https://www.seedance.tv/ja/blog/seedance-2-5-fight-scene-prompt (exchange structure, widening distance, original adult characters and staged wording); its "one detail insert only" and "rigidity wording" are [single source]
- [multi-source] seeddance2.app: https://seeddance2.app/blog/seedance-2-fight-scene-guide (spinning jump kicks deform, whip pans and crash zooms)
- [multi-source] community Seedance 2.5 skill: https://github.com/XiaoJieAi66/XiaoJieAigc-seedance-2-5-video-prompt ; a Japanese creator on note.com: https://note.com/takaweekendprog/n/nfe59410129c3 (initiator, start, path, landing point; left/right positions in every range)
- [single source] elser.ai: https://www.elser.ai/news/seedance-2-5-anime-prompts-elser-ai-characters (smears distort faces)
- [single source] creaa.ai: https://creaa.ai/ja/seedance-2-tsukaikata (hand close-ups are a weak spot)
- [multi-source, community] sensitive wording: https://www.17golang.com/article/511632.html , https://www.tahou.com/article/212586151215904773

Animation and film conventions:
- [multi-source] Hold, burst, hold and smears: https://animetudes.com/2021/07/09/the-kanada-style-now/ , https://pedia.3rd-in.co.jp/wiki/%E5%8B%95%E7%94%BB%20%28%E3%82%A2%E3%83%8B%E3%83%A1%E5%88%B6%E4%BD%9C%29 , https://doi.org/10.34370/jjas.21.2_3
- [multi-source] Impact frames and speed lines: https://www.sakugabooru.com/wiki/show?title=impact_frames , https://blog.sakugabooru.com/glossary/ , https://japanesewithanime.com/2020/03/line-effects.html
- [single source, primary document] NHK and JBA, guidelines on image techniques in animation: https://www.tcnet.ne.jp/wp-content/uploads/community_ch/broadcasting-plan-standard/standard_Exhibit.pdf
- [multi-source] Low angles and wide lenses: https://janica.jp/course/perspective/history04_handout.pdf ; [single source] strong and weak sides in a stand-off: https://www.clipstudio.net/oekaki/archives/152740
- [multi-source] Repeat cuts: https://tvtropes.org/pmwiki/pmwiki.php/Main/RepeatCut , https://gwern.net/doc/anime/2015-chang.pdf
- [multi-source] Anthro performance (ears react first, tail, three-quarter profile for long muzzles): https://animeanime.jp/article/2019/10/30/49323_2.html , https://www.scrmbl.com/post/studio-orange-beastars-interview
- [single source] Large manes at low angles: https://scrmbl.com/post/yusuke-yoshigaki-bna-interview
- [multi-source] Readable fights, centred composition: https://www.davidbordwell.net/blog/2008/12/28/a-glance-at-blows/ , https://www.davidbordwell.net/blog/2016/02/10/off-center-mad-maxs-headroom/
- [multi-source] Tight framings saved for turning points: https://news.cornell.edu/node/285439 , https://www.davidbordwell.net/blog/2007/05/27/intensified-continuity-revisited/
- [single source] Rhythm arc: https://pmc.ncbi.nlm.nih.gov/articles/PMC5256470/
- [multi-source] Match on action, the 180-degree rule, rack focus: https://en.wikipedia.org/wiki/Match_cut , https://en.wikipedia.org/wiki/180-degree_rule , https://en.wikipedia.org/wiki/Deep_focus
- [multi-source] TV animation shot counts (basis for 8–10 shots in 30 seconds): https://cgworld.jp/interview/201709-chronosruler-3.html , https://animeanime.jp/article/2015/09/18/24952_2.html
- [multi-source] Silence setting off an impact: https://realsound.jp/book/2025/03/post-1958046.html , https://transom.org/2005/walter-murch/

Author's material:
- [single source, author-tested] The author's production notes (compiled 2026-10-28): character table, prompt habits, and failure log (half-squat to all fours, real animal in water, look-alikes swapping, references attached to every clip, ambience to the last second, a full-body reference triggering a copyright rejection, empty plates first for hard camera positions).
- [single source, test run] A Seedance 2.5 generation on Jimeng on 2026-10-28: a one-take had one hard cut at the boundary between two ranges.
