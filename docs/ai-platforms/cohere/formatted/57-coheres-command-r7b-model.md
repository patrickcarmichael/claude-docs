---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Command R7B Model

> Command R7B is the smallest, fastest, and final model in our R family of enterprise-focused large language models. It excels at RAG, tool use, and agents.

<ModelShowcase
  model={{
  name: 'Command R7B',
  id: 'command-r7b-12-2024',
  capabilities: [
    Capability.Reasoning,
    Capability.Multilingual,
    Capability.ToolUse,
    Capability.Citation,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.StructuredOutputs,

  ],
  pricing: { input: 0.0375, output: 0.15 },
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
