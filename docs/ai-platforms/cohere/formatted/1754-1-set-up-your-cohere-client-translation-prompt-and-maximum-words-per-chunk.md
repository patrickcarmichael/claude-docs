---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Set up your Cohere client, translation prompt and maximum words per chunk 

import cohere

co = cohere.ClientV2("<YOUR API KEY>")
model = "command-a-translate-08-2025"

target_language = "Spanish"
prompt_template = "Translate everything that follows into {target_language}:\n\n"
max_words = 15  # Set your desired maximum number of words per chunk

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
