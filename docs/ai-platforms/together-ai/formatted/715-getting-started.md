---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting started

1. ### Create a new Mastra project

   First, create a new Mastra project using the CLI:
```bash
   pnpm dlx create-mastra@latest
```
   During the setup, the system prompts you to name your project, choose a default provider, and more. Feel free to use the default settings.

2. ### Install dependencies

   To use Together AI with Mastra, install the required packages:
```bash
     npm i @ai-sdk/togetherai
```
```bash
     yarn add @ai-sdk/togetherai
```
```bash
     pnpm add @ai-sdk/togetherai
```

3. ### Configure environment variables

   Create or update your `.env` file with your Together AI API key:
```bash
   TOGETHER_API_KEY=your-api-key-here
```
4. ### Configure your agent to use Together AI

   Now, update your agent configuration file, typically `src/mastra/agents/weather-agent.ts`, to use Together AI models:
```typescript src/mastra/agents/weather-agent.ts theme={null}
   import 'dotenv/config';
   import { Agent } from '@mastra/core/agent';
   import { createTogetherAI } from '@ai-sdk/togetherai';

   const together = createTogetherAI({
     apiKey: process.env.TOGETHER_API_KEY ?? "",
   });

   export const weatherAgent = new Agent({
     name: 'Weather Agent',
     instructions: `
         You are a helpful weather assistant that provides accurate weather information and can help planning activities based on the weather.
         Use the weatherTool to fetch current weather data.
   `,
     model: together("zai-org/GLM-4.5-Air-FP8"),
     tools: { weatherTool },
    // ... other configuration
   });

   (async () => {
     try {
       const response = await weatherAgent.generate(
         "What's the weather in San Francisco today?",
       );
       console.log('Weather Agent Response:', response.text);
     } catch (error) {
       console.error('Error invoking weather agent:', error);
     }
   })();
```
5. ### Running the application

   Since your agent is now configured to use Together AI, run the Mastra development server:
```bash
     npm run dev
```
```bash
     yarn dev
```
```bash
     pnpm dev
```

   Open the [Mastra Playground and Mastra API](https://mastra.ai/en/docs/server-db/local-dev-playground) to test your agents, workflows, and tools.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
