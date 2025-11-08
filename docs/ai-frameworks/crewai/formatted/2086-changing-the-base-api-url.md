---
title: "Crewai: Changing the Base API URL"
description: "Changing the Base API URL section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Changing the Base API URL


You can change the base API URL for any LLM provider by setting the `base_url` parameter:

```python Code theme={null}
llm = LLM(
    model="custom-model-name",
    base_url="https://api.your-provider.com/v1",
    api_key="your-api-key"
)
agent = Agent(llm=llm, ...)
```

This is particularly useful when working with OpenAI-compatible APIs or when you need to specify a different endpoint for your chosen provider.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Using Local Models with Ollama](./2085-using-local-models-with-ollama.md)

**Next:** [Conclusion →](./2087-conclusion.md)
