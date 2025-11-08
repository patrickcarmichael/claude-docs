---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup Client & Helper Functions

```python
  import asyncio
  import json
  import together
  from pydantic import ValidationError
  from together import AsyncTogether, Together

  client = Together()
  async_client = AsyncTogether()


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


  def JSON_llm(user_prompt: str, schema, system_prompt: str = None):
      try:
          messages = []
          if system_prompt:
              messages.append({"role": "system", "content": system_prompt})

          messages.append({"role": "user", "content": user_prompt})

          extract = client.chat.completions.create(
              messages=messages,
              model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
              response_format={
                  "type": "json_object",
                  "schema": schema.model_json_schema(),
              },
          )
          return json.loads(extract.choices[0].message.content)

      except ValidationError as e:
          error_message = f"Failed to parse JSON: {e}"
          print(error_message)
```
```typescript
  import assert from "node:assert";
  import Together from "together-ai";
  import { Schema } from "zod";
  import zodToJsonSchema from "zod-to-json-schema";

  const client = new Together();

  export async function runLLM(userPrompt: string, model: string) {
    const response = await client.chat.completions.create({
      model,
      messages: [{ role: "user", content: userPrompt }],
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }

  export async function jsonLLM<T>(
    userPrompt: string,
    schema: Schema<T>,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model: "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      messages,
      response_format: {
        type: "json_object",
        // @ts-expect-error Expected error
        schema: zodToJsonSchema(schema, {
          target: "openAi",
        }),
      },
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");

    return schema.parse(JSON.parse(content));
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
