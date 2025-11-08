---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup the agent

agent = Agent(
    model,
    system_prompt="Be concise, reply with one sentence.",
)

result = agent.run_sync('Where does "hello world" come from?')
print(result.data)
```

Learn more in our [PydanticAI Guide](https://docs.together.ai/docs/pydanticai) and explore our [PydanticAI Agents notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/PydanticAI/PydanticAI_Agents.ipynb).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
