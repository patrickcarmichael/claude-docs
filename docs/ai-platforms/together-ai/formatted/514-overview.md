---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

[nanochat](https://github.com/karpathy/nanochat) is Andrej Karpathy's end-to-end ChatGPT clone that demonstrates how a full conversational AI stack, from tokenizer to web UI—can, be trained and deployed for \$100 on 8×H100 hardware. In this guide, you'll learn how to train and deploy nanochat using Together's [Instant Clusters](https://api.together.ai/clusters).

The entire process takes approximately 4 hours on an 8×H100 cluster and includes:

* Training a BPE tokenizer on [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
* Pretraining a base transformer model
* Midtraining on curated tasks
* Supervised fine-tuning for conversational alignment
* Deploying a FastAPI web server with a chat interface

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
