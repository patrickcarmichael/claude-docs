---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Technical Notes

Now, we'll discuss some details of our underlying models that should be kept in mind.

### Language Limitations

This model is designed to excel at English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Chinese, and Arabic, and to generate in 13 other languages well. It will sometimes respond in other languages, but the generations are unlikely to be reliable.

### Sampling Parameters

A model's generation quality is highly dependent on its sampling parameters. Please consult [the documentation](https://docs.cohere.com/docs/advanced-generation-hyperparameters) for details about each parameter and tune the values used for your application. Parameters may require re-tuning upon a new model release.

### Prompt Engineering

Performance quality on generation tasks may increase when examples
are provided as part of the system prompt. See [the documentation](https://docs.cohere.com/docs/crafting-effective-prompts) for examples on how to do this.

### Potential for Misuse

Here we describe potential concerns around misuse of the Command R models, drawing on the NAACL Ethics Review Questions. By documenting adverse use cases, we aim to empower customers to prevent  adversarial actors from leveraging customer applications for the following malicious ends.

The examples in this section are not comprehensive; they are meant to be more model-specific and tangible than those in the Usage Guidelines, and are only meant to illustrate our understanding of potential harms. Each of these malicious use cases violates our Usage Guidelines and Terms of Use, and Cohere reserves the right to restrict API access at any time.

* **Astroturfing:** Generated text used to provide the illusion of discourse or expression of opinion
  by members of the public, on social media or any other channel.
* **Generation of misinformation and other harmful content:**  The generation of news or other
  articles which manipulate public opinion, or any content which aims to incite hate or mischaracterize a group of people.
* **Human-outside-the-loop:** The generation of text that could be used to make important decisions about people, without a human-in-the-loop.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
