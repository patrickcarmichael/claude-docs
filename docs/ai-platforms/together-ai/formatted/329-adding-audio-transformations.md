---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Adding audio transformations

Once we have a transcription, users can transform it using LLMs. We support summarization, extraction, and custom transformations:
```tsx
import { createTogetherAI } from "@ai-sdk/togetherai";
import { generateText } from "ai";

const transformText = async (prompt: string, transcription: string) => {
  const togetherAI = createTogetherAI({
    apiKey: process.env.TOGETHER_API_KEY,
  });

  const { text } = await generateText({
    prompt: `${prompt}\n\nTranscription: ${transcription}`,
    model: togetherAI("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
  });

  return text;
};
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
