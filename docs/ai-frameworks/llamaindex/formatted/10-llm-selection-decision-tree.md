---
title: "Llamaindex: LLM Selection Decision Tree"
description: "LLM Selection Decision Tree section of Llamaindex documentation"
source: "https://llamaindex.com"
last_updated: "2025-11-08"
---

## LLM Selection Decision Tree


```
1. Need latest capabilities?
   → Yes: OpenAI GPT-4, Claude 3 Opus, Gemini
   → No: Proceed to 2

2. Have strict privacy requirements?
   → Yes: Ollama, LlamaCPP, Self-hosted vLLM
   → No: Proceed to 3

3. Cost is critical?
   → Yes: Mistral, Together AI, Groq
   → No: Proceed to 4

4. Need real-time low latency?
   → Yes: Groq, Fireworks
   → No: OpenAI, Claude, Gemini acceptable

5. Require vision capabilities?
   → Yes: OpenAI, Claude 3, Gemini
   → No: Any provider works

6. Enterprise requirements?
   → Yes: Azure OpenAI, AWS Bedrock, Anthropic Enterprise
   → No: Any provider acceptable
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Performance Considerations](./09-performance-considerations.md)

**Next:** [Resources →](./11-resources.md)
