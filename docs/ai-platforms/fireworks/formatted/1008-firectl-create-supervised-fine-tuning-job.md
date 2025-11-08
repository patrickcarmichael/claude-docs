---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl create supervised-fine-tuning-job

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-supervised-fine-tuning-job

Creates a supervised fine-tuning job.
```
firectl create supervised-fine-tuning-job [flags]
```

### Examples

```
firectl create sftj \
	--base-model llama-v3-8b-instruct \
	--dataset sample-dataset \
	--output-model name-of-the-trained-model

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
