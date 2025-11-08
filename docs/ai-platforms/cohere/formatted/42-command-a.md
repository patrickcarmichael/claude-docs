---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Command A

> Command A is a performant mode good at tool use, RAG, agents, and multilingual use cases. It has 111 billion parameters and a 256k context length.

<ModelShowcase
  model={{
  name: 'Command A',
  id: 'command-a-03-2025',
  capabilities: [
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  pricing: { input: 2.50, output: 10.0 },
  specs: {
    contextWindow: '256,000',
    maxOutputTokens: '8,000',
    knowledgeCutoff: 'June 1, 2024',
    customSpecs: [
      {
        name: "Hardware",
        value: "Requires two GPUs to run (A100s / H100s)"
      }
    ]
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
