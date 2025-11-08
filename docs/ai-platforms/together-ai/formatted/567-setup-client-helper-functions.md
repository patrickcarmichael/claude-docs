---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup Client & Helper Functions

```python
  import asyncio
  import together
  from together import AsyncTogether, Together

  client = Together()
  async_client = AsyncTogether()


  def run_llm(user_prompt: str, model: str, system_prompt: str = None):
      messages = []
      if system_prompt:
          messages.append({"role": "system", "content": system_prompt})

      messages.append({"role": "user", "content": user_prompt})

      response = client.chat.completions.create(
          model=model,
          messages=messages,
          temperature=0.7,
          max_tokens=4000,
      )

      return response.choices[0].message.content


  # The function below will call the reference LLMs in parallel

  async def run_llm_parallel(
      user_prompt: str,
      model: str,
      system_prompt: str = None,
  ):
      """Run a single LLM call with a reference model."""
      for sleep_time in [1, 2, 4]:
          try:
              messages = []
              if system_prompt:
                  messages.append({"role": "system", "content": system_prompt})

              messages.append({"role": "user", "content": user_prompt})

              response = await async_client.chat.completions.create(
                  model=model,
                  messages=messages,
                  temperature=0.7,
                  max_tokens=2000,
              )
              break
          except together.error.RateLimitError as e:
              print(e)
              await asyncio.sleep(sleep_time)
      return response.choices[0].message.content
```
```typescript
  import assert from "node:assert";
  import Together from "together-ai";

  const client = new Together();

  export async function runLLM(
    userPrompt: string,
    model: string,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model,
      messages,
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
