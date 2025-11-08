---
title: "Crewai: Common Issues and Solutions"
description: "Common Issues and Solutions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Common Issues and Solutions


<Tabs>
  <Tab title="Authentication">
    <Warning>
      Most authentication issues can be resolved by checking API key format and environment variable names.
    </Warning>

    ```bash  theme={null}
    # OpenAI
    OPENAI_API_KEY=sk-...

    # Anthropic
    ANTHROPIC_API_KEY=sk-ant-...
    ```
  </Tab>

  <Tab title="Model Names">
    <Check>
      Always include the provider prefix in model names
    </Check>

    ```python  theme={null}
    # Correct
    llm = LLM(model="openai/gpt-4")

    # Incorrect
    llm = LLM(model="gpt-4")
    ```
  </Tab>

  <Tab title="Context Length">
    <Tip>
      Use larger context models for extensive tasks
    </Tip>

    ```python  theme={null}
    # Large context model
    llm = LLM(model="openai/gpt-4o")  # 128K tokens
    ```
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Features and Optimization](./203-advanced-features-and-optimization.md)

**Next:** [Memory →](./205-memory.md)
