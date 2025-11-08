---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompt engineering

Prompting is at the heart of working with LLMs. The prompt provides context for the text that we want the model to generate. The prompts we create can be anything from simple instructions to more complex pieces of text, and they are used to encourage the model to produce a specific type of output.

In this section, we'll look at a couple of prompting techniques.

The first is to add more specific instructions to the prompt. The more instructions you provide in the prompt, the closer you can get to the response you need.

The limit of how long a prompt can be is dependent on the maximum context length that a model can support (in the case Command A, it's 256k tokens).

Below, we'll add one additional instruction to the earlier prompt: the length we need the response to be.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
