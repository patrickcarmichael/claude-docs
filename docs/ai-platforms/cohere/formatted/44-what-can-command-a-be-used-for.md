---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What Can Command A Be Used For?

Command A is excellent for:

* Tool use - With [tool use](https://docs.cohere.com/docs/tool-use), Command models can be given tools such as search engines, APIs, vector databases, etc., which can expand their baseline functionality. Command A excels at tool use, exhibiting particular strength in using tools in real-world, diverse, and dynamic environments. In addition, Command A is good at avoiding unnecessarily calling tools, which is an important aspect of tool-use in practical applications.
* Agents - As this is being written, [agents](https://docs.cohere.com/docs/multi-step-tool-use) are among the most exciting frontiers for large language models. Command A’s multistep tool use capabilities allow it to power fast and capable REACT agents. When set up as an internet-augmented research agent, for example, Command A ably completes tasks that require breaking down complex questions into subgoals, and also performs favorably in domains that utilize complex reasoning and active information seeking.
* Retrieval augmented generation - [Retrieval Augmented Generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) refers to the practice of ‘grounding’ model outputs in external data sources, which can increase accuracy. Command A is exceptionally good at generating responses in conversational tasks, attending over long inputs, and extracting and manipulating numerical information in financial settings.
* Multilingual use cases - The model is trained to perform well in 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Chinese, Arabic, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian. It has been trained to respond in the language of the user, or follow instructions to output a response in a different language. It also excels at performing cross-lingual tasks, such as translation or answering questions about content in other languages.

### Command A is Chatty

By default, the model is interactive and optimized for conversation, meaning it is verbose and uses markdown to highlight code. To override this behavior, developers should use a system instruction which asks the model to simply provide the answer and to not use markdown or code block markers. To learn more, consult our documentation on [system instructions](https://docs.cohere.com/docs/system-instructions).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
