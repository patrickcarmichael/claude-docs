---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Long-Form Text Strategies with Cohere

> This discusses ways of getting Cohere's LLM platform to perform well in generating long-form text.

<AuthorsContainer
  authors={[
    {
      name: "Ania Bialas",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/c5dc5a3-Ania.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Long_form_General_Strategies.ipynb" />

Large Language Models (LLMs) are becoming increasingly capable of comprehending text, among others excelling in document analysis. The new Cohere model, [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-v01), boasts a context length of 128k, which makes it particularly effective for such tasks. Nevertheless, even with the extended context window, some documents might be too lengthy to accommodate in full.

In this cookbook, we'll explore techniques to address cases when relevant information doesn't fit in the model context window.

We'll show you three potential mitigation strategies: truncating the document, query-based retrieval, and a "text rank" approach we use internally at Cohere.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
