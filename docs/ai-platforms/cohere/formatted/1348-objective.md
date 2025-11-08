---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Objective

In this notebook we explore how to setup a [Cohere ReAct Agent](https://github.com/langchain-ai/langchain-cohere/blob/main/libs/cohere/langchain_cohere/cohere_agent.py) to answer questions over tables in Apple's SEC10K 2020 form. We show how this can be done with two variants of a Langchain Python tool, one that requires you to pass the full path of the dataframe and another that requires the dataframe objects to be loaded in memory. While there is no major difference between the two approaches, we present both to show how to manage files that are loaded in memory vs files in storage.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
