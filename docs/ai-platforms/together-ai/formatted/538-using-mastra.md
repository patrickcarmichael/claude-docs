---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using Mastra

Mastra is an AI framework that provides built-in integrations and abstractions for building AI applications. Install it with:
```bash
npm i @mastra/core
```

The API route uses Mastra's Together AI integration:
```javascript
// app/api/chat/route.ts
import { Agent } from "@mastra/core/agent";
import { NextRequest } from "next/server";

const agent = new Agent({
  name: "my-agent",
  instructions: "You are a helpful assistant",
  model: "togetherai/meta-llama/Llama-3.3-70B-Instruct-Turbo"
});

export async function POST(request: NextRequest) {
  const { messages } = await request.json();

  const conversationHistory = messages
    .map((msg: { role: string; content: string }) => `${msg.role}: ${msg.content}`)
    .join('\n');

  const streamResponse = await agent.stream(conversationHistory);
  
  const encoder = new TextEncoder();
  const readableStream = new ReadableStream({
    async start(controller) {
      for await (const chunk of streamResponse.textStream) {
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(chunk)}\n\n`));
      }
      controller.close();
    },
  });

  return new Response(readableStream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    },
  });
}
```

The page uses Mastra's chat hooks to manage conversation state:
```javascript
// app/page.tsx
"use client";

import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages([...newMessages, { role: "assistant", content: "" }]);
    setInput("");

    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: newMessages }),
    });

    const reader = res.body?.getReader();
    const decoder = new TextDecoder();
    let assistantMessage = "";

    if (reader) {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const lines = decoder.decode(value).split("\n");
        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const chunk = JSON.parse(line.slice(6));
            assistantMessage += typeof chunk === "string" ? chunk : "";
            setMessages((prev) => [
              ...prev.slice(0, -1),
              { role: "assistant", content: assistantMessage }
            ]);
          }
        }
      }
    }
  };

  return (
    <div>
      {messages.map((m, i) => (
        <div key={i}>
          <strong>{m.role}:</strong> {m.content}
        </div>
      ))}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Send a message" />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

***


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
