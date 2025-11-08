---
title: "Llamaindex: Fallback & Failover Patterns"
description: "Fallback & Failover Patterns section of Llamaindex documentation"
source: "https://llamaindex.com"
last_updated: "2025-11-08"
---

## Fallback & Failover Patterns


LlamaIndex supports implementing fallback chains:

1. **Primary**: High-quality provider (OpenAI, Claude)
2. **Secondary**: Reliable fallback (Cohere, Together AI)
3. **Tertiary**: Cost-optimized backup (Mistral, Groq)
4. **Final**: Local fallback (Ollama)

Benefits:
- Enhanced reliability
- Automatic cost optimization
- Graceful degradation under high load

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Selection Criteria](./07-selection-criteria.md)

**Next:** [Performance Considerations →](./09-performance-considerations.md)
