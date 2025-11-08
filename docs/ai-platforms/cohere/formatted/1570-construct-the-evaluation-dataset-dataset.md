---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Construct the evaluation dataset \[#dataset]

We are interested in evaluating summarization in real-world, enterprise use cases, which typically have two distinguishing features as compared to academic summarization benchmarks:

* Enterprise use cases often focus on specific summarization objectives, e.g. "summarize action items".
* Enterprise use cases often feature specific instruction constraints, e.g. "summarize in bullets with each bullet under 20 words".

Therefore, we must first create a dataset that contains diverse summarization prompts. We will do this programmatically by building prompts from their components, as defined below:

* Prompt = text (e.g. transcript to be summarized) + instruction
* Instruction = instruction objective (e.g. "summarize action items") + modifiers
* Modifiers = format/length modifiers (e.g. "use bullets") + style/tone modifiers (e.g. "do not mention names") + ...

First, we define the prompt that combines the text and instructions. Here, we use a very basic prompt:
```python PYTHON
prompt_template = """## meeting transcript

{transcript}

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
