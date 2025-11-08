---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy Finetuned Command Models from AWS Marketplace

> This document provides a guide for bringing your own finetuned models to Amazon SageMaker.

This document shows you how to deploy your own finetuned [HuggingFace Command-R model](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) using Amazon SageMaker. More specifically, assuming you already have the adapter weights or merged weights from your own finetuned Command model, we will show you how to:

* Merge the adapter weights with the weights of the base model if you only bring the adapter weights;
* Export the merged weights to the TensorRT-LLM inference engine using Amazon SageMaker;
* Deploy the engine as a SageMaker endpoint to serve your business use cases;

You can also find a [companion notebook](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/finetuning/Deploy%20your%20own%20finetuned%20command-r-0824.ipynb) with working code samples.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
