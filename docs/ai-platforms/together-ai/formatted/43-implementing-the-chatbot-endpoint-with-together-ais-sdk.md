---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implementing the chatbot endpoint with Together AI’s SDK

Let’s install Together AI’s node SDK:
```jsx
npm i together-ai
```

and use it to query Llama 3.1 8B Turbo:
```jsx
// api/chat/route.js
import { Together } from 'togetherai';

const together = new Together();

export async function POST(req) {
  const json = await req.json();

  const res = await together.chat.completions.create({
    model: 'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
    messages: json.messages,
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

Since we’re passing the array of messages directly from our React app, and the format is the same as what Together’s `chat.completions.create` method expects, our API handler is mostly acting as a simple passthrough.

We’re also using the `stream: true` option so our frontend will be able to show partial updates as soon as the LLM starts its response.

We’re read to display our chatbot’s first message in our React app!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
