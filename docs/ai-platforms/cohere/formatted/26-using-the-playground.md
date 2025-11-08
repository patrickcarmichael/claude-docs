---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using the Playground

In the next few sections, we'll walk through how to interact with both supported models via the Playground.

### Chat

The [Chat endpoint](https://docs.cohere.com/reference/chat) provides a response (i.e. language or code) to a prompt. You can use the Chat Playground to generate text or code, answer a question, or create content. It looks like this:

<img src="file:b7ccf357-724b-4ff4-9fb1-8debf3e75066" />

Your message goes in the `Message...` box at the bottom, and you can pass a message by hitting `Enter` or by clicking the `Send` button.

You can customize the model's behavior with the `System message`, which is a prompt that guides the model as it generates output. You can learn more about how to craft an effective system message in our [dedicated guide](https://docs.cohere.com/docs/preambles).

To customize further *within* the Playground, you can use the panel on the right:

<img src="file:e91b179d-e1da-4e80-b87d-05c90f0883e6" />

Here's what's available:

* `Model`: Choose from a list of our generation models (we recommend `command-a-03-2025`, the default).
* `Functions`: Function calling allows developers to connect models to external functions like APIs, databases, etc., take actions in them, and return results for users to interact with. Learn more in [tool use](https://docs.cohere.com/docs/tool-use) docs.
* `JSON Mode`: This is part of Cohere's [structured output](https://docs.cohere.com/docs/structured-outputs) functionality. When enabled, the model's response will be a JSON object that matched the schema that you have supplied. Learn more in [JSON mode](https://docs.cohere.com/docs/parameter-types-in-json).
* Under `Advanced Parameters`, you can customize the `temperature` and `seed`. A higher temperature will make the model more creative, while a lower temperature will make the model more focused and deterministic, and seed can help you keep outputs consistent. Learn more [here](https://docs.cohere.com/docs/predictable-outputs).
* Under `Advanced Parameters`, you'll also see the ability to turn on reasoning. This will cause the model to consider the implications of its response and provide a justification for its output. More information will be available as we continue to roll out this feature.

### Embed

The [Embed](https://docs.cohere.com/reference/embed) model enables users to create numerical representations for strings, which comes in handy for semantic search, topic modeling, classification tasks, and many other workflows. You can use the Embed Playground to test this functionality, and it looks like this:

<img src="file:15e519bc-ef61-4273-b6ab-badaf8db8ae6" />

To create embeddings through the Playground, you can either use `Add input` to feed the model your own strings, or you can use `Upload a file`. If you select `Run`, you'll see the two-dimensional visualization of the strings in the `OUTPUT` box.

As with Chat, the Playground's Embed model interface offers a side panel where you can further customize the model:

<img src="file:422d1062-10bc-42ea-81af-fd56ff82c80d" />

Here's what's available:

* `Model`: Choose from a list of our embedding models (we recommend `embed-v4.0`, the default).
* `Truncate`: This allows you to specify how the API will handle inputs longer than the maximum token length.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
