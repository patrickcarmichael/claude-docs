---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Vercel AI SDK

*The Vercel AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.*

Install both the Vercel AI SDK and Together.ai's Vercel package.
```bash
npm i ai @ai-sdk/togetherai
```

Import the Together.ai provider and call the generateText function with Kimi K2 to generate some text.
```typescript
import { togetherai } from "@ai-sdk/togetherai";
import { generateText } from "ai";

async function main() {
  const { text } = await generateText({
    model: togetherai("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
  });

  console.log(text);
}

main();
```

Learn more in our [Together AI - Vercel AI SDK Guide](https://docs.together.ai/docs/using-together-with-vercels-ai-sdk).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
