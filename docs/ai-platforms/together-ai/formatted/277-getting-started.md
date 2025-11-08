---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

**Prerequisites**

1. **Register for an account**: Sign up at [Together AI](https://api.together.xyz/settings/api-keys) to get an API key.

2. **Set up your API key**:
```bash
   export TOGETHER_API_KEY=your_api_key_here
```

3. **Install the required libraries**:
```bash
   # Python

   pip install -U together datasets transformers tqdm
```

**Choosing Your Model**

The first step in fine-tuning is choosing which LLM to use as the starting point for your custom model:

* **Base models** are trained on a wide variety of texts, making their predictions broad
* **Instruct models** are trained on instruction-response pairs, making them better for specific tasks

For beginners, we recommend an instruction-tuned model:

* *meta-llama/Meta-Llama-3.1-8B-Instruct-Reference* is great for simpler tasks
* *meta-llama/Meta-Llama-3.1-70B-Instruct-Reference* is better for more complex datasets and domains

You can find all available models on the Together API [here](/docs/fine-tuning-models).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
