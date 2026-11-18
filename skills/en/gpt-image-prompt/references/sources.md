# Research sources and version notes (research date: 2026-10-28)

The models change quickly. When the user asks about parameters, prices, or new features, go by the official OpenAI docs; this file is only a snapshot from the research date.

## Version timeline

| Date | Version | Notes |
|---|---|---|
| Announced 2025-03-25, in the API 2025-04-23 | GPT Image 1 (`gpt-image-1`) | The "GPT-4o image generation" |
| 2025-10-06 | `gpt-image-1-mini` | Low-cost version |
| 2025-12-16 | GPT Image 1.5 (`gpt-image-1.5`) | ChatGPT Images; more precise edits, faster |
| 2026-04 | GPT Image 2 (`gpt-image-2`) | ChatGPT Images 2.0; reasoning added to generation, a large jump in text rendering |
| 2026-09-08 | GPT Image 2.5: `gpt-image-2.5-flare` / `gpt-image-2.5-sunburst` | Flare for speed, Sunburst for quality; `-2026-09-08` snapshots exist; ChatGPT gained Sketch, templates, and comments on the image |

## Official sources (highest priority)

- OpenAI image prompting guide (covers 2.5 Flare/Sunburst): https://developers.openai.com/api/docs/guides/image-prompting
- OpenAI Cookbook image prompting guide (GPT Image 2 era, the page is marked archived): https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- Model pages: https://developers.openai.com/api/docs/models/gpt-image-2.5-flare , https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst
- Image generation guide (including mask-edit requirements): https://developers.openai.com/api/docs/guides/image-generation

Key conclusions from the official guides:
- Order: background/scene → subject → key details → constraints; state the purpose first (ad, UI, infographic) to set the level of polish.
- Any format works (paragraphs, lists, JSON-like, labels); for production use a fixed, scannable template.
- Text: in quotes or ALL CAPS, with typeface, size, colour, and position; spell rare words letter by letter; state the number of occurrences and ask for no extra text.
- Edits: "change only X / keep everything else", repeating the keep-list every round; use compositing for pixel-identical regions.
- Multiple images: refer to each input by index + role, and say how they combine.
- Parameters go in the API, not the prompt; raise quality as needed; above 2560×1440 is experimental.
- Do not describe UI in concept-art language; do not use studio wording for realistic scenes; do not carry GPT Image 1 settings over unchanged.

## Community and third parties (for experience)

- wuyoscar/gpt_image_2_skill (GitHub, about 5.9k stars, with 2.5 material and a gallery of 162 prompts): https://github.com/wuyoscar/gpt_image_2_skill . Main points: text in quotes, canvas and layout before the subject, JSON for complex product renders, fixed zones for infographics, UI written like a product spec, consistency constraints for multi-panel images, negatives aimed only at strong priors, stating Simplified or Traditional for dense Chinese layouts and ruling out garble.
- The "six-part" form from freestylefly/awesome-gpt-image-2: subject and task → composition and layout → visual style and materials → text requirements → aspect ratio and output → constraints and exclusions.
- atlabs GPT Image 2.5 guide: fix the quality level by hand when comparing; change one variable at a time; a 4×4 pure-white design sheet for character consistency; a styled sheet background contaminates later scenes. https://www.atlabs.ai/blog/gpt-image-2.5-prompt-guide-2026-flare-vs-sunburst-quality-steps-and-consistent-characters
- Morphic ChatGPT Images 2.0 guide: reasoning plans the layout only in Thinking/Pro modes; it renders Latin, Chinese, Japanese, Korean, Hindi, and Bengali text; up to 10 images at a time. https://morphic.com/resources/how-to/chatgpt-images-2.0-guide
- Wikipedia, "GPT Image" (version timeline): https://en.wikipedia.org/wiki/GPT_Image

## Unconfirmed or disputed points

- "Words at the start of the prompt carry the most weight": several third-party articles say so, and the official docs do not mention it. Keeping the habit does no harm (purpose and canvas go first).
- "2.5 supports up to 16 reference images / native 4K": from third-party pages. The official size limit is a 3840 long edge, with anything above 2560×1440 experimental; the docs do not state a reference-image count.
- Figures such as "about 99%" text accuracy have no reliable source.
- Whether `input_fidelity` has any effect on 2.5 is unconfirmed; for `gpt-image-2` the docs say not to pass it. Some gpt-image-2 edit examples in the old Cookbook still pass `input_fidelity="high"`, contradicting the parameter table.
- Entry points and availability of ChatGPT features (Thinking mode, Sketch, circle-and-comment) vary by account and region; go by the actual interface.
