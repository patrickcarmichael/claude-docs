---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tips for Effective Evaluation

<Accordion title="Prompt Structure for Evaluation">
  To make the most of the Evaluation tool, structure your prompts with clear input and output formats. For example:
```
  In this task, you will generate a cute one sentence story that incorporates two elements: a color and a sound.
  The color to include in the story is:
  <color>
  {{COLOR}}
  </color>
  The sound to include in the story is:
  <sound>
  {{SOUND}}
  </sound>
  Here are the steps to generate the story:
  1. Think of an object, animal, or scene that is commonly associated with the color provided. For example, if the color is "blue", you might think of the sky, the ocean, or a bluebird.
  2. Imagine a simple action, event or scene involving the colored object/animal/scene you identified and the sound provided. For instance, if the color is "blue" and the sound is "whistle", you might imagine a bluebird whistling a tune.
  3. Describe the action, event or scene you imagined in a single, concise sentence. Focus on making the sentence cute, evocative and imaginative. For example: "A cheerful bluebird whistled a merry melody as it soared through the azure sky."
  Please keep your story to one sentence only. Aim to make that sentence as charming and engaging as possible while naturally incorporating the given color and sound.
  Write your completed one sentence story inside <story> tags.
```
  This structure makes it easy to vary inputs (\{\{COLOR}} and \{\{SOUND}}) and evaluate outputs consistently.
</Accordion>

<Tip>
  Use the 'Generate a prompt' helper tool in the Console to quickly create prompts with the appropriate variable syntax for evaluation.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
