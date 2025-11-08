---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool Calling

Source: https://docs.fireworks.ai/guides/function-calling

Connect models to external tools and APIs

Tool calling (also known as function calling) enables models to intelligently select and use external tools based on user input. You can build agents that access APIs, retrieve real-time data, or perform actions—all through [OpenAI-compatible](https://platform.openai.com/docs/guides/function-calling) tool specifications.

**How it works:**

1. Define tools using [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step) (name, description, parameters)
2. Model analyzes the query and decides whether to call a tool
3. If needed, model returns structured tool calls with parameters
4. You execute the tool and send results back for the final response

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
