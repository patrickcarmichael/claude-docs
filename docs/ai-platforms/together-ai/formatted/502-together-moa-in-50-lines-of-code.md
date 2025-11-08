---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Together MoA in 50 lines of code

To get to get started with using MoA in your own apps, you'll need to install the Together python library, get your Together API key, and run the code below which uses our chat completions API to interact with OSS models.

1. Install the Together Python library
```bash
pip install together
```

2. Get your [Together API key](https://api.together.xyz/settings/api-keys) & export it
```bash
export TOGETHER_API_KEY='xxxx'
```

3. Run the code below, which interacts with our chat completions API.

This implementation of MoA uses 2 layers and 4 LLMs. We’ll define our 4 initial LLMs and our aggregator LLM, along with our prompt. We’ll also add in a prompt to send to the aggregator to combine responses effectively. Now that we have this, we’ll simply send the prompt to the 4 LLMs and compute all results simultaneously. Finally, we'll send the results from the four LLMs to our final LLM, along with a system prompt instructing it to combine them into a final answer, and we’ll stream results back.
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
