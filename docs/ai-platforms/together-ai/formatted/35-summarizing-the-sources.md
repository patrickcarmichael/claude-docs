---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Summarizing the sources

Now that we have the text content from each source, we can pass it along with a prompt to Together to get a final answer.

Let’s install Together’s node SDK:
```jsx
npm i together-ai
```

and use it to query Llama 3.1 8B Turbo:
```jsx
import { Together } from "togetherai";

const together = new Together();

export async function POST(req) {
  const json = await req.json();

  // Since exa already gave us the content of the pages we can simply use it 
  const results = json.sources

  // Ask Together to answer the question using the results but limiting content
  // of each page to the first 10k characters to prevent overflowing context
  const systemPrompt = `
    Given a user question and some context, please write a clean, concise
    and accurate answer to the question based on the context. You will be
    given a set of related contexts to the question. Please use the
    context when crafting your answer.

    Here are the set of contexts:

    <contexts>
    ${results.map((result) => `${result.content.slice(0, 10_000)}\n\n`)}
    </contexts>
  `;
  const runner = await together.chat.completions.stream({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: json.question },
    ],
  });

  return new Response(runner.toReadableStream());
}
```

Now we’re read to read it in our React app!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
