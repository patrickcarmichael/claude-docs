---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Command A Translate Model

> Command A Translate is a state of the art model performant in 23 languages. It has a context length of 16K tokens and 111B parameters.

<ModelShowcase
  model={{
  name: 'Command A Translate',
  id: 'command-a-translate-08-2025',
  capabilities: [
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  specs: {
    contextWindow: '8,000',
    maxOutputTokens: '8,000',
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
