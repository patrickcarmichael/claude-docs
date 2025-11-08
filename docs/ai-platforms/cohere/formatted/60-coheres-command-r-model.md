---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Command R+ Model

> Command R+ is Cohere's optimized for conversational interaction and long-context tasks, best suited for complex RAG workflows and multi-step tool use.

<ModelShowcase
  model={{
  name: 'Command R+',
  id: 'command-r-plus-08-2024',
  capabilities: [
    Capability.Reasoning,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  pricing: { input: 2.50, output: 10.0 },
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
