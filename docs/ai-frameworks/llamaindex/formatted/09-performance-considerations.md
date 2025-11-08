---
title: "Llamaindex: Performance Considerations"
description: "Performance Considerations section of Llamaindex documentation"
source: "https://llamaindex.com"
last_updated: "2025-11-08"
---

## Performance Considerations


### Latency Rankings

1. Groq (50-200ms) - Ultra-fast
2. Fireworks (100-300ms) - Very fast
3. Together AI (200-400ms) - Fast
4. OpenAI (300-800ms) - Standard
5. Claude (300-800ms) - Standard
6. Ollama (depends on hardware) - Variable

### Throughput Optimization

- Use vLLM for batch inference
- Implement token budgeting
- Cache common prompts
- Use streaming for UI responsiveness

### Cost Optimization Strategies

- Use cheaper models for classification
- Reserve expensive models for complex reasoning
- Implement prompt caching
- Use batch APIs when available
- Monitor token usage per provider

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Fallback & Failover Patterns](./08-fallback-failover-patterns.md)

**Next:** [LLM Selection Decision Tree →](./10-llm-selection-decision-tree.md)
