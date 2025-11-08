---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Command A Reasoning Model

> Command A Reasoning excels in tool use, agentic workflows, and complex problem-solving. It has 111 billion parameters and a 256k context length.

<ModelShowcase
  model={{
  name: 'Command A Reasoning',
  id: 'command-a-reasoning-08-2025',
  capabilities: [
    Capability.Reasoning,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  specs: {
    contextWindow: '256,000',
    maxOutputTokens: '32,000',
    knowledgeCutoff: 'June 1, 2024',
    
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatCompletions,
  ],
}}
/>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
