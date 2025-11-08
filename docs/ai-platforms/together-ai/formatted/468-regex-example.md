---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Regex example

All the models supported for JSON mode also support regex mode. Here's an example using it to constrain the classification.
```py
  import together

  client = together.Together()

  completion = client.chat.completions.create(
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are an AI-powered expert specializing in classifying sentiment. You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative.",
          },
          {"role": "user", "content": "Wow. I loved the movie!"},
      ],
      response_format={
          "type": "regex",
          "pattern": "(positive|neutral|negative)",
      },
  )

  print(completion.choices[0].message.content)
```
```typescript
  import Together from "together-ai";
  const together = new Together();

  async function main() {
    const completion = await together.chat.completions.create({
      model: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      temperature: 0.2,
      max_tokens: 10,
      messages: [
        {
          role: "system",
          content:
            "You are an AI-powered expert specializing in classifying sentiment. You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative.",
        },
        {
          role: "user",
          content: "Wow. I loved the movie!",
        },
      ],
      response_format: {
        type: "regex",
        // @ts-ignore
        pattern: "(positive|neutral|negative)",
      },
    });

    console.log(completion?.choices[0]?.message?.content);
  }

  main();
```
```bash
  curl https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      "messages": [
        {
          "role": "user",
          "content": "Return only an email address for Alan Turing at Enigma. End with .com and newline."
        }
      ],
      "stop": ["\n"],
      "response_format": {
        "type": "regex",
        "pattern": "\\w+@\\w+\\.com\\n"
      },
      "temperature": 0.0,
      "max_tokens": 50
    }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
