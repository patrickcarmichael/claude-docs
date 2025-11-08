---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an instance of the Vectorstore class with the given sources

vectorstore = Vectorstore(raw_documents)
```
```mdx
Loading documents...
Embedding document chunks...
Indexing document chunks...
Indexing complete with 137 document chunks.
```
We can test if the retrieval is working by entering a search query.
```python PYTHON
vectorstore.retrieve("Prompting by giving examples")
```
```mdx
[{'title': 'Advanced Prompt Engineering Techniques',
  'text': 'Few-shot Prompting\n\nUnlike the zero-shot examples above, few-shot prompting is a technique that provides a model with examples of the task being performed before asking the specific question to be answered. We can steer the LLM toward a high-quality solution by providing a few relevant and diverse examples in the prompt. Good examples condition the model to the expected response type and style.',
  'url': 'https://docs.cohere.com/docs/advanced-prompt-engineering-techniques'},
 {'title': 'Crafting Effective Prompts',
  'text': 'Incorporating Example Outputs\n\nLLMs respond well when they have specific examples to work from. For example, instead of asking for the salient points of the text and using bullet points “where appropriate”, give an example of what the output should look like.',
  'url': 'https://docs.cohere.com/docs/crafting-effective-prompts'},
 {'title': 'Advanced Prompt Engineering Techniques',
  'text': 'In addition to giving correct examples, including negative examples with a clear indication of why they are wrong can help the LLM learn to distinguish between correct and incorrect responses. Ordering the examples can also be important; if there are patterns that could be picked up on that are not relevant to the correctness of the question, the model may incorrectly pick up on those instead of the semantics of the question itself.',
  'url': 'https://docs.cohere.com/docs/advanced-prompt-engineering-techniques'}]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
