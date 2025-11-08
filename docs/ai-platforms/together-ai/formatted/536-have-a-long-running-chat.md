---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Have a long-running chat

To build a chatbot with Together AI, we'll need an API route that accepts an array of messages, and a page with a form that lets the user submit new messages. The page will also need to store the entire history of messages between the user and the AI assistant.

**1. Create an API route**

Make a new POST route that takes in a `messages` array and returns a chat completion as a stream:
```javascript
// app/api/chat/route.ts
import Together from "together-ai";

const together = new Together();

export async function POST(request: Request) {
  const { messages } = await request.json();

  const res = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages,
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

**2. Create a page**

Create a form to submit a new message, and some React state to stores the `messages` for the session. In the form's submit handler, send over the new array of messages, and use the `ChatCompletionStream` helper to read the stream and update the last message with the LLM's response.
```javascript
// app/page.tsx
"use client";

import { FormEvent, useState } from "react";
import Together from "together-ai";
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

export default function Chat() {
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState<
    Together.Chat.Completions.CompletionCreateParams.Message[]
  >([]);
  const [isPending, setIsPending] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setPrompt("");
    setIsPending(true);
    setMessages((messages) => [...messages, { role: "user", content: prompt }]);

    const res = await fetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({
        messages: [...messages, { role: "user", content: prompt }],
      }),
    });

    if (!res.body) return;

    ChatCompletionStream.fromReadableStream(res.body)
      .on("content", (delta, content) => {
        setMessages((messages) => {
          const lastMessage = messages.at(-1);

          if (lastMessage?.role !== "assistant") {
            return [...messages, { role: "assistant", content }];
          } else {
            return [...messages.slice(0, -1), { ...lastMessage, content }];
          }
        });
      })
      .on("end", () => {
        setIsPending(false);
      });
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <input
            placeholder="Send a message"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button type="submit" disabled={isPending}>
            Submit
          </button>
        </fieldset>
      </form>

      {messages.map((message, i) => (
        <p key={i}>
          {message.role}: {message.content}
        </p>
      ))}
    </div>
  );
}
```

You've just built a simple chatbot with Together AI!

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
