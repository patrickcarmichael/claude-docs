---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

```python
  from pydantic_ai import Agent
  from pydantic_ai.models.openai import OpenAIModel
  from pydantic_ai.providers.openai import OpenAIProvider

  # Connect PydanticAI to LLMs on Together

  model = OpenAIModel(
      "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      provider=OpenAIProvider(
          base_url="https://api.together.xyz/v1",
          api_key=os.environ.get("TOGETHER_API_KEY"),
      ),
  )

  # Setup the agent

  agent = Agent(
      model,
      system_prompt="Be concise, reply with one sentence.",
  )

  result = agent.run_sync('Where does "hello world" come from?')
  print(result.data)
```

### Output

```
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
