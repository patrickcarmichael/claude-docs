---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Solution

In this notebook, we propose a simple but effective solution to the challenge defined above: We create a [Langchain ReAct Agent](https://github.com/langchain-ai/langchain-cohere/blob/main/libs/cohere/langchain_cohere/cohere_agent.py) that has access to a deterministic tool that extracts the alphanumeric patterns in the query, and returns a dictionary in which the keys are the parameters, and the values the extracted patterns. The output of the tool is then used to generate the final request.

Using such a tool is just one of the possibilities that the Agent has to generate the query. As we will see below, when a more semantic understanding of the query is required, we can ignore the tool and leverage the linguistic capabilities of the LLM powering the Agent to generate the final output.

With this approach, we bring together the best of two worlds: the ability of LLMs to use tools and generate outputs and the reliability and efficiency of deterministic functions.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
