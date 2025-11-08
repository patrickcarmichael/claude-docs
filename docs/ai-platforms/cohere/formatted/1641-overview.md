---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

Cohere chat models (Comand R and Command R+) are fantastic generally capable models out of the box. To further adopt our models for specific tasks, there are several strategies like prompt engineering, RAG, tool use, finetuning. In this cookbook, we will focus on finetuning. While the other strategies involve careful and intelligent orchestration of our models out of the box, finetuning involves modifying the weights to specialize the model for a task at hand. This requires careful investment of time and resources from data collection to model training. This is typically employed when all other strategies fall short.

Our finetuning service allows customization of our latest Command R model (command-r-08-2024) with LoRA based finetuning which gives users the the ability to control model flexibility depending on their task. Additionally, we extended the training context length to 16384 tokens giving users the ability to user longer training data points which is typical for RAG, agents, and tool use. In this cookbook, we will showcase model customization via our [Finetuning API](https://cohere-preview-6021ac31-6091-4dd4-a195-dc3456f6883c.docs.buildwithfern.com/reference/createfinetunedmodel) and also show you how to monitor loss functions for your finetuning jobs using the [Weights & Biases integration](#sec_wandb). Please note that you can do the same via the UI. You can find a detailed guide for that [here](https://cohere-preview-6021ac31-6091-4dd4-a195-dc3456f6883c.docs.buildwithfern.com/docs/fine-tuning-with-the-cohere-dashboard).

We will finetine our Command R model on the task of conversational financial question answering. Specifically, we finetune our model on [ConvFinQA](https://github.com/czyssrs/ConvFinQA) dataset. In this task, the output expected from the model is a domain specific language (DSL) that we will potentially feed into a downstream application. LLMs are known to be bad at arithmetics. Hence, instead of computing the answer, the task here is to extract the right numbers from the context and applying the right sequence of predicates and to strictly follow the DSL to ensure minimal error rates in the downstream application that may consume the DSL output from our model. Prompt engineering proves to be rather brittle for such tasks as it is hard to make sure the model follows the exact syntax of the DSL. Finetuning the model gives that guarantee.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
