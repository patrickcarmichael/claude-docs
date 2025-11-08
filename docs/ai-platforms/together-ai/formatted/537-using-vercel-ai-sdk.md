---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using Vercel AI SDK

The Vercel AI SDK provides React hooks that simplify streaming and state management. Install it with:
```bash
npm i ai @ai-sdk/togetherai
```

The API route uses `streamText` instead of the Together SDK directly:
```javascript
// app/api/chat/route.ts
import { streamText, convertToModelMessages } from "ai";
import { createTogetherAI } from "@ai-sdk/togetherai";

const togetherAI = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY,
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: togetherAI("meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    messages: convertToModelMessages(messages),
  });

  return result.toUIMessageStreamResponse();
}
```

The page uses the `useChat` hook which handles all message state and streaming automatically:
```javascript
// app/page.tsx
"use client";

import { useChat } from "@ai-sdk/react";
import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");
  const { messages, sendMessage } = useChat();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      sendMessage({
        role: "user",
        parts: [{ type: "text", text: input }],
      });
      setInput("");
    }
  };

  return (
    <div>
      {messages.map((message) => (
        <div key={message.id}>
          <strong>{message.role}:</strong>
          {message.parts.map((part, i) =>
            part.type === "text" ? <span key={i}> {part.text}</span> : null
          )}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Send a message"
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
