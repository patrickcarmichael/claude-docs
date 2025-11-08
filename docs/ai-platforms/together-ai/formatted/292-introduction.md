---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction

Function calling (also called *tool calling*) enables LLMs to respond with structured function names and arguments that you can execute in your application. This allows models to interact with external systems, retrieve real-time data, and power agentic AI workflows.

Pass function descriptions to the `tools` parameter, and the model will return `tool_calls` when it determines a function should be used. You can then execute these functions and optionally pass the results back to the model for further processing.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
