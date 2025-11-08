---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating the transcription API with tRPC

Our backend uses tRPC to provide end-to-end type safety. Here's our transcription endpoint:
```tsx
import { Together } from "together-ai";
import { createTogetherAI } from "@ai-sdk/togetherai";
import { generateText } from "ai";

export const whisperRouter = t.router({
  transcribeFromS3: protectedProcedure
    .input(
      z.object({
        audioUrl: z.string(),
        language: z.string().optional(),
        durationSeconds: z.number().min(1),
      })
    )
    .mutation(async ({ input, ctx }) => {
      // Call Together AI's Whisper model
      const togetherClient = new Together({
        apiKey: process.env.TOGETHER_API_KEY,
      });

      const res = await togetherClient.audio.transcriptions.create({
        file: input.audioUrl,
        model: "openai/whisper-large-v3",
        language: input.language || "en",
      });

      const transcription = res.text as string;

      // Generate a title using LLM
      const togetherAI = createTogetherAI({
        apiKey: process.env.TOGETHER_API_KEY,
      });

      const { text: title } = await generateText({
        prompt: `Generate a title for the following transcription with max of 10 words: ${transcription}`,
        model: togetherAI("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
        maxTokens: 10,
      });

      // Save to database
      const whisperId = uuidv4();
      await prisma.whisper.create({
        data: {
          id: whisperId,
          title: title.slice(0, 80),
          userId: ctx.auth.userId,
          fullTranscription: transcription,
          audioTracks: {
            create: [
              {
                fileUrl: input.audioUrl,
                partialTranscription: transcription,
                language: input.language,
              },
            ],
          },
        },
      });

      return { id: whisperId };
    }),
});
```

The beauty of tRPC is that our frontend gets full TypeScript intellisense and type checking for this API call.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
