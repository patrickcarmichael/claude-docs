---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ask a single question

To ask a question with Together AI, we'll need an API route, and a page with a form that lets the user submit their question.

**1. Create the API route**

Make a new POST route that takes in a `question` and returns a chat completion as a stream:
```javascript
// app/api/answer/route.ts
import Together from "together-ai";

const together = new Together();

export async function POST(request: Request) {
  const { question } = await request.json();

  const res = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: question }],
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

**2. Create the page**

Add a form that sends a POST request to your new API route, and use the `ChatCompletionStream` helper to read the stream and update some React state to display the answer:
```javascript
// app/page.tsx
"use client";

import { FormEvent, useState } from "react";
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setIsLoading(true);
    setAnswer("");

    const res = await fetch("/api/answer", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    if (!res.body) return;

    ChatCompletionStream.fromReadableStream(res.body)
      .on("content", (delta) => setAnswer((text) => text + delta))
      .on("end", () => setIsLoading(false));
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me a question"
          required
        />

        <button disabled={isLoading} type="submit">
          Submit
        </button>
      </form>

      <p>{answer}</p>
    </div>
  );
}
```

That's it! Submitting the form will update the page with the LLM's response. You can now use the `isLoading` state to add additional styling, or a Reset button if you want to reset the page.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
