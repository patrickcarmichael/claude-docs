---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Command R Model

> Command R is a conversational model that excels in language tasks and supports multiple languages, making it ideal for coding use cases.

<ModelShowcase
  model={{
  name: 'Command R',
  id: 'command-r-08-2024',
  capabilities: [
    Capability.Reasoning,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  pricing: { input: 0.15, output: 0.60 },
  specs: {
    contextWindow: '128,000',
    maxOutputTokens: '4,000',
    knowledgeCutoff: 'June 1, 2024',
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatV1,
    Endpoint.ChatCompletions,
  ],
}}
/>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
