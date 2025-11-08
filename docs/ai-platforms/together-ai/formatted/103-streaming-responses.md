---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming responses

Since models can take some time to respond to a query, Together's APIs support streaming back responses in chunks. This lets you display results from each chunk while the model is still running, instead of having to wait for the entire response to finish.

To return a stream, set the `stream` option to true.
```python
  import os
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
```
```shell
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	],
        "stream": true
       }'
       
  ## Response will be a stream of Server-Sent Events with JSON-encoded payloads. For example:

  ## 
  ## data: {"choices":[{"index":0,"delta":{"content":" A"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":330,"text":" A","logprob":1,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}

  ## data: {"choices":[{"index":0,"delta":{"content":":"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":28747,"text":":","logprob":0,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}

  ## data: {"choices":[{"index":0,"delta":{"content":" Sure"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":12875,"text":" Sure","logprob":-0.00724411,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
