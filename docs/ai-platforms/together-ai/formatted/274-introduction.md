---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction

Large Language Models (LLMs) offer powerful general capabilities, but often require **fine-tuning** to excel at specific tasks or understand domain-specific language. Fine-tuning adapts a trained model to a smaller, targeted dataset, enhancing its performance for your unique needs.

This guide provides a step-by-step walkthrough for fine-tuning models using the Together AI platform. We will cover everything from preparing your data to evaluating your fine-tuned model.

We will cover:

1. **Dataset Preparation:** Loading a standard dataset, transforming it into the required format for supervised fine-tuning on Together AI, and uploading your formatted dataset to Together AI Files.
2. **Fine-tuning Job Launch:** Configuring and initiating a fine-tuning job using the Together AI API.
3. **Job Monitoring:** Checking the status and progress of your fine-tuning job.
4. **Inference:** Using your newly fine-tuned model via the Together AI API for predictions.
5. **Evaluation:** Comparing the performance of the fine-tuned model against the base model on a test set.

By following this guide, you'll gain practical experience in creating specialized LLMs tailored to your specific requirements using Together AI.

>   **ℹ️ Info**
>
> ### Fine-tuning Guide Notebook

  Here is a runnable notebook version of this fine-tuning guide: [Fine-tuning Guide Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
