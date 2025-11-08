---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Effect AI SDK

You can use the [Effect AI SDK](https://www.npmjs.com/package/@effect/ai) to integrate OpenRouter with your Effect applications. To get started, install the following packages:

* [effect](https://www.npmjs.com/package/effect): the Effect core (if not already installed)
* [@effect/ai](https://www.npmjs.com/package/@effect/ai): the core Effect AI SDK abstractions
* [@effect/ai-openrouter](https://www.npmjs.com/package/@effect/ai-openrouter): the Effect AI provider integration for OpenRouter
* [@effect/platform](https://www.npmjs.com/package/@effect/platform): platform-agnostic abstractions for Effect
```bash
npm install effect @effect/ai @effect/ai-openrouter @effect/platform
```
Once that's done you can use the [LanguageModel](https://effect.website/docs/ai/getting-started/#define-an-interaction-with-a-language-model) module to define interactions with a large language model via OpenRouter.
```typescript title="TypeScript"
  import { LanguageModel } from "@effect/ai"
  import { OpenRouterClient, OpenRouterLanguageModel } from "@effect/ai-openrouter"
  import { FetchHttpClient } from "@effect/platform"
  import { Config, Effect, Layer, Stream } from "effect"

  const Gpt4o = OpenRouterLanguageModel.model("openai/gpt-4o")

  const program = LanguageModel.streamText({
    prompt: [
      { role: "system", content: "You are a comedian with a penchant for groan-inducing puns" },
      { role: "user", content: [{ type: "text", text: "Tell me a dad joke" }] }
    ]
  }).pipe(
    Stream.filter((part) => part.type === "text-delta"),
    Stream.runForEach((part) => Effect.sync(() => process.stdout.write(part.delta))),
    Effect.provide(Gpt4o)
  )

  const OpenRouter = OpenRouterClient.layerConfig({
    apiKey: Config.redacted("OPENROUTER_API_KEY")
  }).pipe(Layer.provide(FetchHttpClient.layer))

  program.pipe(
    Effect.provide(OpenRouter),
    Effect.runPromise
  )
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
