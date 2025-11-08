---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use GPT-OSS API

These models are only available to Build Tier 1 or higher users. Since reasoning models produce longer responses with chain-of-thought processing, we recommend streaming tokens for better user experience:
```python
  from together import Together

  client = Together()  # pass in API key to api_key or set a env variable

  stream = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[
          {
              "role": "user",
              "content": "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?",
          }
      ],
      temperature=1.0,
      top_p=1.0,
      reasoning_effort="medium",
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
```
```typescript
  import Together from "together-ai";
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "openai/gpt-oss-120b",
    messages: [{ 
      role: "user", 
      content: "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?" 
    }],
    temperature: 1.0,
    top_p: 1.0,
    reasoning_effort: "medium",
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "openai/gpt-oss-120b",
       	"messages": [
            {"role": "user", "content": "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?"}
       	],
          "temperature": 1.0,
          "top_p": 1.0,
          "reasoning_effort": "medium",
          "stream": true
       }'
```

This will produce the response below:
```plain
{
  "id": "o669aLj-62bZhn-96b01dc00f33ab9a",
  "object": "chat.completion",
  "created": 1754499896,
  "model": "openai/gpt-oss-120b",
  "service_tier": null,
  "system_fingerprint": null,
  "kv_transfer_params": null,
  "prompt": [],
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "**Short answer:**  \nNo. From “All roses are flowers” and “Some flowers are red” ...",
        "tool_calls": [],
        "reasoning": "We need to answer the logic puzzle. Statement: All roses ..."
      },
      "logprobs": null,
      "finish_reason": "stop",
      "seed": null
    }
  ],
  "usage": {
    "prompt_tokens": 96,
    "total_tokens": 984,
    "completion_tokens": 888
  }
}
```

To access just the chain-of-thought reasoning you can look at the `reasoning` property:
```plain
We need to answer the logic puzzle. The premise: "All roses are flowers" (i.e., every rose is a flower). "Some flowers are red" (there exists at least one flower that is red). Does this entail that some roses are red? In standard syllogistic logic, no; you cannot infer that. Because the red flower could be a different type. The conclusion "Some roses are red" is not guaranteed. It's a classic syllogism: All R are F, Some F are R (actually some F are red). The conclusion "Some R are red" is not valid (invalid). So answer: No, we cannot conclude; we need additional assumption like "All red flowers are roses" or "All red things are roses". Provide explanation.

Hence final answer: no, not necessarily; situation possible where all roses are yellow etc.

Thus solve puzzle.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
