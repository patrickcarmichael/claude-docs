**Navigation:** [← Previous](./01-vercel-documentation.md) | [Index](./index.md) | [Next →](./03-build-output-configuration.md)

---

# Usage & Billing

Copy page

Ask AI about this page

Last updated October 21, 2025

The AI Gateway provides endpoints to monitor your credit balance, track usage, and retrieve detailed information about specific generations.

## [Base URL](#base-url)

The Usage & Billing API is available at the following base URL:

`https://ai-gateway.vercel.sh/v1`

## [Supported endpoints](#supported-endpoints)

The AI Gateway supports the following Usage & Billing endpoints:

*   [`GET /credits`](#credits) - Check your credit balance and usage information
*   [`GET /generation`](#generation-lookup) - Retrieve detailed information about a specific generation

## [Credits](#credits)

Check your AI Gateway credit balance and usage information.

Endpoint

`GET /credits`

Example request

TypeScriptPython

credits.ts

```
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;
 
const response = await fetch('https://ai-gateway.vercel.sh/v1/credits', {
  method: 'GET',
  headers: {
    Authorization: `Bearer ${apiKey}`,
    'Content-Type': 'application/json',
  },
});
 
const credits = await response.json();
console.log(credits);
```

credits.py

```
import os
import requests
 
api_key = os.getenv("AI_GATEWAY_API_KEY") or os.getenv("VERCEL_OIDC_TOKEN")
 
response = requests.get(
    "https://ai-gateway.vercel.sh/v1/credits",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
)
 
credits = response.json()
print(credits)
```

Sample response

```
{
  "balance": "95.50",
  "total_used": "4.50"
}
```

Response fields

*   `balance`: The remaining credit balance
*   `total_used`: The total amount of credits used

## [Generation lookup](#generation-lookup)

Retrieve detailed information about a specific generation by its ID. This endpoint allows you to look up usage data, costs, and metadata for any generation created through the AI Gateway. Generation information is available shortly after the generation completes. Note much of this data is also included in the `providerMetadata` field of the chat completion responses.

Endpoint

`GET /generation?id={generation_id}`

Parameters

*   `id` (required): The generation ID to look up (format: `gen_<ulid>`)

Example request

TypeScriptPython

generation-lookup.ts

```
const generationId = 'gen_01ARZ3NDEKTSV4RRFFQ69G5FAV';
 
const response = await fetch(
  `https://ai-gateway.vercel.sh/v1/generation?id=${generationId}`,
  {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
  },
);
 
const generation = await response.json();
console.log(generation);
```

generation-lookup.py

```
import os
import requests
 
generation_id = 'gen_01ARZ3NDEKTSV4RRFFQ69G5FAV'
 
response = requests.get(
    f"https://ai-gateway.vercel.sh/v1/generation?id={generation_id}",
    headers={
        "Authorization": f"Bearer {os.getenv('AI_GATEWAY_API_KEY')}",
        "Content-Type": "application/json",
    },
)
 
generation = response.json()
print(generation)
```

Sample response

```
{
  "data": {
    "id": "gen_01ARZ3NDEKTSV4RRFFQ69G5FAV",
    "total_cost": 0.00123,
    "usage": 0.00123,
    "created_at": "2024-01-01T00:00:00.000Z",
    "model": "gpt-4",
    "is_byok": false,
    "provider_name": "openai",
    "streamed": true,
    "latency": 200,
    "generation_time": 1500,
    "tokens_prompt": 100,
    "tokens_completion": 50,
    "native_tokens_prompt": 100,
    "native_tokens_completion": 50,
    "native_tokens_reasoning": 0,
    "native_tokens_cached": 0
  }
}
```

Response fields

*   `id`: The generation ID
*   `total_cost`: Total cost in USD for this generation
*   `usage`: Usage cost (same as total\_cost)
*   `created_at`: ISO 8601 timestamp when the generation was created
*   `model`: Model identifier used for this generation
*   `is_byok`: Whether this generation used Bring Your Own Key credentials
*   `provider_name`: The provider that served this generation
*   `streamed`: Whether this generation used streaming (`true` for streamed responses, `false` otherwise)
*   `latency`: Time to first token in milliseconds
*   `generation_time`: Total generation time in milliseconds
*   `tokens_prompt`: Number of prompt tokens
*   `tokens_completion`: Number of completion tokens
*   `native_tokens_prompt`: Native prompt tokens (provider-specific)
*   `native_tokens_completion`: Native completion tokens (provider-specific)
*   `native_tokens_reasoning`: Reasoning tokens used (if applicable)
*   `native_tokens_cached`: Cached tokens used (if applicable)

Generation IDs: Generation IDs are included in chat completion responses as the [`id`](https://platform.openai.com/docs/api-reference/chat/object#chat/object-id) field as well as in the provider metadata returned in the response.

--------------------------------------------------------------------------------
title: "AI SDK"
description: "TypeScript toolkit for building AI-powered applications with React, Next.js, Vue, Svelte and Node.js"
last_updated: "null"
source: "https://vercel.com/docs/ai-sdk"
--------------------------------------------------------------------------------

# AI SDK

Copy page

Ask AI about this page

Last updated October 9, 2025

The [AI SDK](https://sdk.vercel.ai) is the TypeScript toolkit designed to help developers build AI-powered applications with [Next.js](https://sdk.vercel.ai/docs/getting-started/nextjs-app-router), [Vue](https://sdk.vercel.ai/docs/getting-started/nuxt), [Svelte](https://sdk.vercel.ai/docs/getting-started/svelte), [Node.js](https://sdk.vercel.ai/docs/getting-started/nodejs), and more. Integrating LLMs into applications is complicated and heavily dependent on the specific model provider you use.

The AI SDK abstracts away the differences between model providers, eliminates boilerplate code for building chatbots, and allows you to go beyond text output to generate rich, interactive components.

## [Generating text](#generating-text)

At the center of the AI SDK is [AI SDK Core](https://sdk.vercel.ai/docs/ai-sdk-core/overview), which provides a unified API to call any LLM.

The following example shows how to generate text with the AI SDK using OpenAI's GPT-5:

```
import { generateText } from 'ai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Explain the concept of quantum entanglement.',
});
```

The unified interface means that you can easily switch between providers by changing just two lines of code. For example, to use Anthropic's Claude Sonnet 3.7:

```
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
 
const { text } = await generateText({
  model: anthropic('claude-3-7-sonnet-20250219'),
  prompt: 'How many people will live in the world in 2040?',
});
```

## [Generating structured data](#generating-structured-data)

While text generation can be useful, you might want to generate structured JSON data. For example, you might want to extract information from text, classify data, or generate synthetic data. AI SDK Core provides two functions ([`generateObject`](https://sdk.vercel.ai/docs/reference/ai-sdk-core/generate-object) and [`streamObject`](https://sdk.vercel.ai/docs/reference/ai-sdk-core/stream-object)) to generate structured data, allowing you to constrain model outputs to a specific schema.

The following example shows how to generate a type-safe recipe that conforms to a zod schema:

```
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';
 
const { object } = await generateObject({
  model: 'openai/gpt-5',
  schema: z.object({
    recipe: z.object({
      name: z.string(),
      ingredients: z.array(z.object({ name: z.string(), amount: z.string() })),
      steps: z.array(z.string()),
    }),
  }),
  prompt: 'Generate a lasagna recipe.',
});
```

## [Using tools with the AI SDK](#using-tools-with-the-ai-sdk)

The AI SDK supports tool calling out of the box, allowing it to interact with external systems and perform discrete tasks. The following example shows how to use tool calling with the AI SDK:

```
import { generateText, tool } from 'ai';
import { openai } from '@ai-sdk/openai';
 
const { text } = await generateText({
  model: 'openai/gpt-5',
  prompt: 'What is the weather like today in San Francisco?',
  tools: {
    getWeather: tool({
      description: 'Get the weather in a location',
      inputSchema: z.object({
        location: z.string().describe('The location to get the weather for'),
      }),
      execute: async ({ location }) => ({
        location,
        temperature: 72 + Math.floor(Math.random() * 21) - 10,
      }),
    }),
  },
});
```

## [Getting started with the AI SDK](#getting-started-with-the-ai-sdk)

The AI SDK is available as a package. To install it, run the following command:

pnpmyarnnpmbun

```
pnpm i ai
```

See the [AI SDK Getting Started](https://sdk.vercel.ai/docs/getting-started) guide for more information on how to get started with the AI SDK.

## [More resources](#more-resources)

*   [AI SDK documentation](https://sdk.vercel.ai/docs)
*   [AI SDK examples](https://sdk.vercel.ai/examples)
*   [AI SDK guides](https://sdk.vercel.ai/docs/guides)
*   [AI SDK templates](https://vercel.com/templates?type=ai)

--------------------------------------------------------------------------------
title: "Adding a Model"
description: "Learn how to add a new AI model to your Vercel projects"
last_updated: "null"
source: "https://vercel.com/docs/ai/adding-a-model"
--------------------------------------------------------------------------------

# Adding a Model

Copy page

Ask AI about this page

Last updated March 19, 2025

If you have integrations installed, scroll to the bottom to access the models explorer.

## [Exploring models](#exploring-models)

To explore models:

1.  Use the search bar, provider select, or type filter to find the model you want to add
2.  Select the model you want to add by pressing the Explore button
3.  The model playground will open, and you can test the model before adding it to your project

### [Using the model playground](#using-the-model-playground)

The model playground lets you test the model you are interested in before adding it to your project. If you have not installed an AI provider through the Vercel dashboard, then you will have ten lifetime generations per provider (they do not refresh, and once used, are spent) regardless of plan. If you _have_ installed an AI provider that supports the model, Vercel will use your provider key.

You can use the model playground to test the model's capabilities and see if it fits your projects needs.

The model playground differs depending on the model you are testing. For example, if you are testing a chat model, you can input a prompt and see the model's response. If you are testing an image model, you can upload an image and see the model's output. Each model may have different variations based on the provider you choose.

The playground also lets you also configure the model's settings, such as temperature, maximum output length, duration, continuation, top p, and more. These settings and inputs are specific to the model you are testing.

### [Adding a model to your project](#adding-a-model-to-your-project)

Once you have decided on the model you want to add to your project:

1.  Select the Add Model button
2.  If you have more than one provider that supports the model you are adding, you will be prompted to select the provider you want to use. To select a provider, press the Add Provider button next to the provider you want to use for the model
3.  Review the provider card which displays the models available, along with a description of the provider and links to their website, pricing, and documentation and select the Add Provider button
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  You'll be redirected to the provider's website to complete the connection process
6.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider and model settings, view usage, and more

## [Featured AI integrations](#featured-ai-integrations)

[

### xAIMarketplace native integration

An AI service with an efficient text model and a wide context image understanding model.

](/docs/ai/xai)[

### GroqMarketplace native integration

A high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture.

](/docs/ai/groq)[

### falMarketplace native integration

A serverless AI inferencing platform for creative processes.

](/docs/ai/fal)[

### DeepInfraMarketplace native integration

A platform with access to a vast library of open-source models.

](/docs/ai/deepinfra)

[

### PerplexityMarketplace connectable account

Learn how to integrate Perplexity with Vercel.

](/docs/ai/perplexity)[

### ReplicateMarketplace connectable account

Learn how to integrate Replicate with Vercel.

](/docs/ai/replicate)[

### ElevenLabsMarketplace connectable account

Learn how to integrate ElevenLabs with Vercel.

](/docs/ai/elevenlabs)[

### LMNTMarketplace connectable account

Learn how to integrate LMNT with Vercel.

](/docs/ai/lmnt)[

### Together AIMarketplace connectable account

Learn how to integrate Together AI with Vercel.

](/docs/ai/togetherai)[

### OpenAIGuide

Connect powerful AI models like GPT-4

](/docs/ai/openai)

--------------------------------------------------------------------------------
title: "Adding a Provider"
description: "Learn how to add a new AI provider to your Vercel projects."
last_updated: "null"
source: "https://vercel.com/docs/ai/adding-a-provider"
--------------------------------------------------------------------------------

# Adding a Provider

Copy page

Ask AI about this page

Last updated March 19, 2025

When you navigate to the AI tab, you'll see a list of installed AI integrations. If you don't have installed integrations, you can browse and connect to the AI models and services that best fit your project's needs.

## [Adding a native integration provider](#adding-a-native-integration-provider)

1.  Select the Install AI Provider button on the top right of the AI dashboard page.
2.  From the list of Marketplace AI Providers, select the provider that you would like to install and click Continue.
3.  Select a plan from the list of available plans that can include both prepaid and post-paid plans.
    *   For prepaid plans, once you select your plan and click Continue:
        *   You are taken to a Manage Funds screen where you can set up an initial balance for the prepayment.
        *   You can also enable auto recharge with a maximum monthly spend. Auto recharge can also be configured at a later stage.
4.  Click Continue, provide a name for your installation and click Install.
5.  Once the installation is complete, you are taken to the installation's detail page where you can:
    *   Link a project by clicking Connect Project
    *   Follow a quickstart in different languages to test your installation
    *   View the list of all connected projects
    *   View the usage of the service

For more information on managing native integration providers, review [Manage native integrations](/docs/integrations/install-an-integration/product-integration#manage-native-integrations).

## [Adding a connectable account provider](#adding-a-connectable-account-provider)

If no integrations are installed, browse the list of available providers and click on the provider you would like to add.

1.  Select the Add button next to the provider you want to integrate
2.  Review the provider card which displays the models available, along with a description of the provider and links to their website, pricing, and documentation
3.  Select the Add Provider button
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more

Once you add a provider, the AI tab will display a list of the providers you have installed or connected to. To add more providers:

1.  Select the Install AI Provider button on the top right of the page.
2.  Browse down to the list of connectable accounts.
3.  Select the provider that you would like to connect to and click Continue and follow the instructions from step 4 above.

## [Featured AI integrations](#featured-ai-integrations)

[

### xAIMarketplace native integration

An AI service with an efficient text model and a wide context image understanding model.

](/docs/ai/xai)[

### GroqMarketplace native integration

A high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture.

](/docs/ai/groq)[

### falMarketplace native integration

A serverless AI inferencing platform for creative processes.

](/docs/ai/fal)[

### DeepInfraMarketplace native integration

A platform with access to a vast library of open-source models.

](/docs/ai/deepinfra)

--------------------------------------------------------------------------------
title: "Vercel Deep Infra IntegrationNative Integration"
description: "Learn how to add the Deep Infra native integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/deepinfra"
--------------------------------------------------------------------------------

# Vercel Deep Infra Integration

Native Integration

Copy page

Ask AI about this page

Last updated June 26, 2025

[Deep Infra](https://deepinfra.com/) provides scalable and cost-effective infrastructure for deploying and managing machine learning models. It's optimized for reduced latency and low costs compared to traditional cloud providers.

This integration gives you access to the large selection of available AI models and allows you to manage your tokens, billing and usage directly from Vercel.

## [Use cases](#use-cases)

You can use the [Vercel and Deep Infra integration](https://vercel.com/marketplace/deepinfra) to:

*   Seamlessly connect AI models such as DeepSeek and Llama with your Vercel projects.
*   Deploy and run inference with high-performance AI models optimized for speed and efficiency.

### [Available models](#available-models)

Deep Infra provides a diverse range of AI models designed for high-performance tasks for a variety of applications.

### Some available models on Deep Infra

DeepSeek R1 Turbo

**Type:** Chat

A generative text model

DeepSeek R1

**Type:** Chat

A generative text model

DeepSeek V3

**Type:** Chat

A generative text model

Llama 3.1 8B Instruct Turbo

**Type:** Chat

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.3 70B Instruct Turbo

**Type:** Chat

Llama 3.3 is an auto-regressive language model that uses an optimized transformer architecture.

DeepSeek R1 Distill Llama 70B

**Type:** Chat

A generative text model

Llama 4 Maverick 17B 128E Instruct

**Type:** Chat

Meta's advanced natively multimodal model with a 17B parameter mixture-of-experts architecture (128 experts) that enables sophisticated text and image understanding, supporting 12 languages.

Llama 4 Scout 17B 16E Instruct

**Type:** Chat

Meta's natively multimodal model with a 17B parameter mixture-of-experts architecture that enables text and image understanding, supporting 12 languages.

## [Getting started](#getting-started)

The Vercel Deep Infra integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select Deep Infra from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/deepinfra ai
    ```
    
10.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2
    3import { deepinfra } from '@ai-sdk/deepinfra';4import { streamText } from 'ai';5
    6// Allow streaming responses up to 30 seconds7export const maxDuration = 30;8
    9export async function POST(req: Request) {10  // Extract the `messages` from the body of the request11  const { messages } = await req.json();12
    13  // Call the language model14  const result = streamText({15    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),16    messages,17  });18
    19  // Respond with the stream20  return result.toDataStreamResponse();21}22
    ```
    

#### [Using the CLI](#using-the-cli)

1.  Add the provider to your project using the [Vercel CLI `install`](/docs/cli/install) command
    
    terminal
    
    ```
    vercel install deepinfra
    ```
    
    During this process, you will be asked to open the dashboard to accept the marketplace terms if you have not installed this integration before. You can also choose which project(s) the provider will have access to.
2.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/deepinfra ai
    ```
    
3.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2
    3import { deepinfra } from '@ai-sdk/deepinfra';4import { streamText } from 'ai';5
    6// Allow streaming responses up to 30 seconds7export const maxDuration = 30;8
    9export async function POST(req: Request) {10  // Extract the `messages` from the body of the request11  const { messages } = await req.json();12
    13  // Call the language model14  const result = streamText({15    model: deepinfra('deepseek-ai/DeepSeek-R1-Distill-Llama-70B'),16    messages,17  });18
    19  // Respond with the stream20  return result.toDataStreamResponse();21}22
    ```
    

## [More resources](#more-resources)

[

### Deep Infra Website

Learn more about Deep Infra by visiting their website.

](https://deepinfra.com/)[

### Deep Infra Pricing

Learn more about Deep Infra pricing.

](https://deepinfra.com/pricing)[

### Deep Infra Documentation

Visit the Deep Infra documentation.

](https://deepinfra.com/docs)[

### Deep Infra AI SDK page

Visit the Deep Infra AI SDK reference page.

](https://sdk.vercel.ai/providers/ai-sdk-providers/deepinfra)

--------------------------------------------------------------------------------
title: "Vercel ElevenLabs IntegrationConnectable Account"
description: "Learn how to add the ElevenLabs connectable account integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/elevenlabs"
--------------------------------------------------------------------------------

# Vercel ElevenLabs Integration

Connectable Account

Copy page

Ask AI about this page

Last updated June 26, 2025

[ElevenLabs](https://elevenlabs.io) specializes in advanced voice synthesis and audio processing technologies. Its integration with Vercel allows you to incorporate realistic voice and audio enhancements into your applications, ideal for creating interactive media experiences.

## [Use cases](#use-cases)

You can use the Vercel and ElevenLabs integration to power a variety of AI applications, including:

*   Voice synthesis: Use ElevenLabs for generating natural-sounding synthetic voices in applications such as virtual assistants or audio-books
*   Audio enhancement: Use ElevenLabs to enhance audio quality in applications, including noise reduction and sound clarity improvement
*   Interactive media: Use ElevenLabs to implement voice synthesis and audio processing in interactive media and gaming for realistic soundscapes

### [Available models](#available-models)

ElevenLabs offers models that specialize in advanced voice synthesis and audio processing, delivering natural-sounding speech and audio enhancements suitable for various interactive media applications.

### Some available models on ElevenLabs

Eleven English v2

**Type:** Audio

The highest quality English text-to-speech model.

Eleven English v1

**Type:** Audio

The original ElevenLabs English text-to-speech model.

Eleven Multilingual v1

**Type:** Audio

A multilingual text-to-speech model. This has been surpassed by the Eleven Multilingual v2 model.

Eleven Multilingual v2

**Type:** Audio

A multilingual text-to-speech model that supports 28 languages.

Eleven Turbo v2

**Type:** Audio

The fastest text-to-speech model. Only English is supported.

Eleven Turbo v2.5

**Type:** Audio

A highly optimized, low-latency text-to-speech model supporting 32 languages.

## [Getting started](#getting-started)

The Vercel ElevenLabs integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select ElevenLabs from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @elevenlabs/elevenlabs-js
    ```
    
10.  Connect your project using the code below:
    
    index.ts
    
    ```
    1// index.ts2import { ElevenLabsClient, play } from '@elevenlabs/elevenlabs-js';3
    4const elevenlabs = new ElevenLabsClient({5  apiKey: 'YOUR_API_KEY', // Defaults to process.env.ELEVENLABS_API_KEY6});7
    8const audio = await elevenlabs.textToSpeech.convert('JBFqnCBsd6RMkjVDRZzb', {9  text: 'The first move is what sets everything in motion.',10  modelId: 'eleven_multilingual_v2',11});12
    13await play(audio);14
    ```
    

## [More resources](#more-resources)

[

### ElevenLabs Website

Learn more about ElevenLabs by visiting their website.

](https://elevenlabs.io)[

### ElevenLabs Pricing

Learn more about ElevenLabs pricing.

](https://elevenlabs.io/pricing)[

### ElevenLabs Documentation

Visit the ElevenLabs documentation.

](https://elevenlabs.io/docs)

--------------------------------------------------------------------------------
title: "Vercel fal IntegrationNative Integration"
description: "Learn how to add the fal native integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/fal"
--------------------------------------------------------------------------------

# Vercel fal Integration

Native Integration

Copy page

Ask AI about this page

Last updated June 26, 2025

[fal](https://fal.ai/) enables the development of real-time AI applications with a focus on rapid inference speeds, achieving response times under ~120ms. Specializing in diffusion models, fal has no cold starts and a pay-for-what-you-use pricing model.

## [Use cases](#use-cases)

You can use the [Vercel and fal integration](https://vercel.com/marketplace/fal) to power a variety of AI applications, including:

*   Text-to-image applications: Use fal to integrate real-time text-to-image generation in applications, enabling users to create complex visual content from textual descriptions instantly
*   Real-time image processing: Use fal for applications requiring instantaneous image analysis and modification, such as real-time filters, enhancements, or object recognition in streaming video
*   Depth maps creation: Use fal's AI models for generating depth maps from images, supporting applications in 3D modeling, augmented reality, or advanced photography editing, where understanding the spatial relationships in images is crucial

### [Available models](#available-models)

fal provides a diverse range of AI models designed for high-performance tasks in image and text processing.

### Some available models on fal

Stable Diffusion XL

**Type:** Image

Run SDXL at the speed of light

Creative Upscaler

**Type:** Image

Create creative upscaled images.

FLUX.1 \[dev\] with LoRAs

**Type:** Image

Super fast endpoint for the FLUX.1 \[dev\] model with LoRA support, enabling rapid and high-quality image generation using pre-trained LoRA adaptations for personalization, specific styles, brand identities, and product-specific outputs.

Stable Diffusion XL

**Type:** Image

Run SDXL at the speed of light

Veo 2 Text to Video

**Type:** Video

Veo creates videos with realistic motion and high quality output. Explore different styles and find your own with extensive camera controls.

Wan-2.1 Image to Video

**Type:** Video

Wan-2.1 generates high-quality videos with excellent visual quality and motion diversity from still images. Bring your photos to life with natural, fluid movement.

## [Getting started](#getting-started)

The Vercel fal integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select fal from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @fal-ai/client
    ```
    
10.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/fal/proxy/route.ts
    
    ```
    1// app/api/fal/proxy/route.ts2
    3import { route } from '@fal-ai/serverless-proxy/nextjs';4
    5export const { GET, POST } = route;6
    ```
    

#### [Using the CLI](#using-the-cli)

1.  Add the provider to your project using the [Vercel CLI `install`](/docs/cli/install) command
    
    terminal
    
    ```
    vercel install fal
    ```
    
    During this process, you will be asked to open the dashboard to accept the marketplace terms if you have not installed this integration before. You can also choose which project(s) the provider will have access to.
2.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @fal-ai/client
    ```
    
3.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/fal/proxy/route.ts
    
    ```
    1// app/api/fal/proxy/route.ts2
    3import { route } from '@fal-ai/serverless-proxy/nextjs';4
    5export const { GET, POST } = route;6
    ```
    

## [More resources](#more-resources)

[

### fal Website

Learn more about fal by visiting their website.

](https://fal.ai/)[

### fal Pricing

Learn more about fal pricing.

](https://fal.ai/pricing)[

### fal Documentation

Visit the fal documentation.

](https://fal.ai/docs)[

### fal AI SDK page

Visit the fal AI SDK reference page.

](https://sdk.vercel.ai/providers/ai-sdk-providers/fal)

--------------------------------------------------------------------------------
title: "Vercel Groq IntegrationNative Integration"
description: "Learn how to add the Groq native integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/groq"
--------------------------------------------------------------------------------

# Vercel Groq Integration

Native Integration

Copy page

Ask AI about this page

Last updated June 26, 2025

[Groq](https://groq.com/) is a high-performance AI inference service with an ultra-fast Language Processing Unit (LPU) architecture. It enables fast response times for language model inference, making it ideal for applications requiring low latency.

## [Use cases](#use-cases)

You can use the [Vercel and Groq integration](https://vercel.com/marketplace/groq) to:

*   Connect AI models such as Whisper-large-v3 for audio processing and Llama models for text generation to your Vercel projects.
*   Deploy and run inference with optimized performance.

### [Available models](#available-models)

Groq provides a diverse range of AI models designed for high-performance tasks.

### Some available models on Groq

DeepSeek R1 Distill Llama 70B

**Type:** Chat

A generative text model

Distil Whisper Large V3 English

**Type:** Audio

A distilled, or compressed, version of OpenAI's Whisper model, designed to provide faster, lower cost English speech recognition while maintaining comparable accuracy.

Llama 3.1 8B Instant

**Type:** Chat

A fast and efficient language model for text generation.

Mistral Saba 24B

**Type:** Chat

Mistral Saba 24B is a specialized model trained to excel in Arabic, Farsi, Urdu, Hebrew, and Indic languages. Designed for high-performance multilingual capabilities, it delivers exceptional results across a wide range of tasks in these languages while maintaining strong performance in English. With a 32K token context window and tool use capabilities, it's ideal for complex multilingual applications requiring deep language understanding and regional context.

Qwen QWQ 32B

**Type:** Chat

Qwen QWQ 32B is a powerful large language model with strong reasoning capabilities and versatile applications across various tasks.

Whisper Large V3

**Type:** Audio

A state-of-the-art model for automatic speech recognition (ASR) and speech translation, trained on 1M hours of weakly labeled and 4M hours of pseudo-labeled audio. Supports 99 languages with improved accuracy over previous versions.

Whisper Large V3 Turbo

**Type:** Audio

A faster version of Whisper Large V3 with reduced decoding layers (4 instead of 32), providing significantly improved speed with minimal quality degradation. Supports 99 languages for speech recognition and translation.

Llama 3.3 70B Instruct Turbo

**Type:** Chat

Meta's Llama 3.3 is an auto-regressive language model that uses an optimized transformer architecture. Supports 128K context length and multilingual processing.

Llama 4 Scout 17B 16E Instruct

**Type:** Chat

Meta's natively multimodal model with a 17B parameter mixture-of-experts architecture that enables text and image understanding, supporting 12 languages.

## [Getting started](#getting-started)

The Vercel Groq integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select Groq from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/groq ai
    ```
    
10.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2
    3import { groq } from '@ai-sdk/groq';4import { streamText } from 'ai';5
    6// Allow streaming responses up to 30 seconds7export const maxDuration = 30;8
    9export async function POST(req: Request) {10  // Extract the `messages` from the body of the request11  const { messages } = await req.json();12
    13  // Call the language model14  const result = streamText({15    model: groq('llama-3.1-8b-instant'),16    messages,17  });18
    19  // Respond with the stream20  return result.toDataStreamResponse();21}22
    ```
    

#### [Using the CLI](#using-the-cli)

1.  Add the provider to your project using the [Vercel CLI `install`](/docs/cli/install) command
    
    terminal
    
    ```
    vercel install groq
    ```
    
    During this process, you will be asked to open the dashboard to accept the marketplace terms if you have not installed this integration before. You can also choose which project(s) the provider will have access to.
2.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/groq ai
    ```
    
3.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2
    3import { groq } from '@ai-sdk/groq';4import { streamText } from 'ai';5
    6// Allow streaming responses up to 30 seconds7export const maxDuration = 30;8
    9export async function POST(req: Request) {10  // Extract the `messages` from the body of the request11  const { messages } = await req.json();12
    13  // Call the language model14  const result = streamText({15    model: groq('llama-3.1-8b-instant'),16    messages,17  });18
    19  // Respond with the stream20  return result.toDataStreamResponse();21}22
    ```
    

## [More resources](#more-resources)

[

### Groq Website

Learn more about Groq by visiting their website.

](https://groq.com/)[

### Groq Pricing

Learn more about Groq pricing.

](https://groq.com/pricing)[

### Groq Documentation

Visit the Groq documentation.

](https://console.groq.com/docs/overview)[

### Groq AI SDK page

Visit the Groq AI SDK reference page.

](https://sdk.vercel.ai/providers/ai-sdk-providers/groq)

--------------------------------------------------------------------------------
title: "Vercel LMNT IntegrationConnectable Account"
description: "Learn how to add LMNT connectable account integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/lmnt"
--------------------------------------------------------------------------------

# Vercel LMNT Integration

Connectable Account

Copy page

Ask AI about this page

Last updated June 26, 2025

[LMNT](https://lmnt.com/) provides data processing and predictive analytics models, known for their precision and efficiency. Integrating LMNT with Vercel enables your applications to offer accurate insights and forecasts, particularly useful in finance and healthcare sectors.

## [Use cases](#use-cases)

You can use the Vercel and LMNT integration to power a variety of AI applications, including:

*   High quality text-to-speech: Use LMNT to generate realistic speech that powers chatbots, AI-agents, games, and other digital media
*   Studio quality custom voices: Use LMNT to clone voices that will faithfully reproduce the emotional richness and realism of actual speech
*   Reliably low latency, full duplex streaming: Use LMNT to enable superior performance for conversational experiences, with consistently low latency and unmatched reliability

## [Getting started](#getting-started)

The Vercel LMNT integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select LMNT from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i lmnt-node
    ```
    
10.  Connect your project using the code below:
    
    index.ts
    
    ```
    1// index.ts2import Speech from 'lmnt-node';3
    4const speech = new Speech(process.env.LMNT_API_KEY);5const voices = await speech.fetchVoices();6const firstVoice = voices[0].id;7const synthesis = await speech.synthesize('Hello World!', firstVoice, {8  format: 'mp3',9});10writeFileSync('/tmp/output.mp3', synthesis.audio);11
    ```
    

## [More resources](#more-resources)

[

### LMNT Website

Learn more about LMNT by visiting their website.

](https://lmnt.com/)[

### LMNT Pricing

Learn more about LMNT pricing.

](https://lmnt.com/pricing)[

### LMNT Documentation

Visit the LMNT documentation.

](https://docs.lmnt.com)

--------------------------------------------------------------------------------
title: "Vercel & OpenAI Integration"
description: "Integrate your Vercel project with OpenAI's powerful suite of models."
last_updated: "null"
source: "https://vercel.com/docs/ai/openai"
--------------------------------------------------------------------------------

# Vercel & OpenAI Integration

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel integrates with [OpenAI](https://platform.openai.com/overview) to enable developers to build fast, scalable, and secure [AI applications](https://vercel.com/ai).

You can integrate with [any OpenAI model](https://platform.openai.com/docs/models/overview) using the [AI SDK](https://sdk.vercel.ai), including the following OpenAI models:

*   GPT-4o: Understand and generate natural language or code
*   GPT-4.5: Latest language model with enhanced emotional intelligence
*   o3-mini: Reasoning model specialized in code generation and complex tasks
*   DALL·E 3: Generate and edit images from natural language
*   Embeddings: Convert term into vectors

## [Getting started](#getting-started)

To help you get started, we have built a [variety of AI templates](https://vercel.com/templates/ai) integrating OpenAI with Vercel.

## [Getting Your OpenAI API Key](#getting-your-openai-api-key)

Before you begin, ensure you have an [OpenAI account](https://platform.openai.com/signup). Once registered:

1.  ### [Navigate to API Keys](#navigate-to-api-keys)
    
    Log into your [OpenAI Dashboard](https://platform.openai.com/) and [view API keys](https://platform.openai.com/account/api-keys).
    
2.  ### [Generate API Key](#generate-api-key)
    
    Click on Create new secret key. Copy the generated API key securely.
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fopenai%2Fenv-vars.png&w=3840&q=75)
    
    Always keep your API keys confidential. Do not expose them in client-side code. Use [Vercel Environment Variables](/docs/environment-variables) for safe storage and do not commit these values to git.
    
3.  ### [Set Environment Variable](#set-environment-variable)
    
    Finally, add the `OPENAI_API_KEY` environment variable in your project:
    
    .env.local
    
    ```
    OPENAI_API_KEY='sk-...3Yu5'
    ```
    

## [Building chat interfaces with the AI SDK](#building-chat-interfaces-with-the-ai-sdk)

Integrating OpenAI into your Vercel project is seamless with the [AI SDK](https://sdk.vercel.ai/docs).

Install the AI SDK in your project with your favorite package manager:

pnpmyarnnpmbun

```
pnpm i ai
```

You can use the SDK to build AI applications with [React (Next.js)](https://sdk.vercel.ai/docs/getting-started/nextjs-app-router), [Vue (Nuxt)](https://sdk.vercel.ai/docs/getting-started/nuxt), [Svelte (SvelteKit)](https://sdk.vercel.ai/docs/getting-started/svelte), and [Node.js](https://sdk.vercel.ai/docs/getting-started/nodejs).

## [Using OpenAI Functions with Vercel](#using-openai-functions-with-vercel)

The AI SDK also has full support for [OpenAI Functions (tool calling)](https://openai.com/blog/function-calling-and-other-api-updates).

Learn more about using [tools with the AI SDK](https://sdk.vercel.ai/docs/foundations/tools).

--------------------------------------------------------------------------------
title: "Vercel Perplexity IntegrationConnectable Account"
description: "Learn how to add Perplexity connectable account integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/perplexity"
--------------------------------------------------------------------------------

# Vercel Perplexity Integration

Connectable Account

Copy page

Ask AI about this page

Last updated June 26, 2025

[Perplexity API](https://perplexity.ai/) specializes in providing accurate, real-time answers to user questions by combining AI-powered search with large language models, delivering concise, well-sourced, and conversational responses. Integrating Perplexity via its [Sonar API](https://sonar.perplexity.ai/) with Vercel allows your applications to deliver real-time, web-wide research and question-answering capabilities—complete with accurate citations, customizable sources, and advanced reasoning—enabling users to access up-to-date, trustworthy information directly within your product experience.

## [Use cases](#use-cases)

You can use the Vercel and Perplexity integration to power a variety of AI applications, including:

*   Real-time, citation-backed answers: Integrate Perplexity to provide users with up-to-date information grounded in live web data, complete with detailed source citations for transparency and trust.
*   Customizable search and data sourcing: Tailor your application's responses by specifying which sources Perplexity should use, ensuring compliance and relevance for your domain or industry.
*   Complex, multi-step query handling: Leverage advanced models like Sonar Pro to process nuanced, multi-part questions, deliver in-depth research, and support longer conversational context windows.
*   Optimized speed and efficiency: Benefit from Perplexity's lightweight, fast models that deliver nearly instant answers at scale, making them ideal for high-traffic or cost-sensitive applications.
*   Fine-grained output control: Adjust model parameters (e.g., creativity, repetition) and manage output quality to align with your application's unique requirements and user expectations.

### [Available models](#available-models)

The Sonar models are each optimized for tasks such as real-time search, advanced reasoning, and in-depth research. Please refer to Perplexity's list of available models [here](https://docs.perplexity.ai/models/model-cards).

### Some available models on Perplexity API

Sonar Pro

**Type:** Chat

Perplexity's premier offering with search grounding, supporting advanced queries and follow-ups.

Sonar

**Type:** Chat

Perplexity's lightweight offering with search grounding, quicker and cheaper than Sonar Pro.

## [Getting started](#getting-started)

The Vercel Perplexity API integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select Perplexity API from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/perplexity ai
    ```
    
10.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2import { perplexity } from '@ai-sdk/perplexity';3import { streamText } from 'ai';4
    5// Allow streaming responses up to 30 seconds6export const maxDuration = 30;7
    8export async function POST(req: Request) {9  // Extract the `messages` from the body of the request10  const { messages } = await req.json();11
    12  // Call the language model13  const result = streamText({14    model: perplexity('sonar-pro'),15    messages,16  });17
    18  // Respond with the stream19  return result.toDataStreamResponse();20}21
    ```
    

## [More resources](#more-resources)

[

### Perplexity API Website

Learn more about Perplexity API by visiting their website.

](https://perplexity.ai/)[

### Perplexity API Pricing

Learn more about Perplexity API pricing.

](https://docs.perplexity.ai/guides/pricing)[

### Perplexity API Documentation

Visit the Perplexity API documentation.

](https://docs.perplexity.ai/)

--------------------------------------------------------------------------------
title: "Vercel Pinecone IntegrationConnectable Account"
description: "Learn how to add Pinecone connectable account integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/pinecone"
--------------------------------------------------------------------------------

# Vercel Pinecone Integration

Connectable Account

Copy page

Ask AI about this page

Last updated September 24, 2025

[Pinecone](https://pinecone.io/) is a [vector database](/guides/vector-databases) service that handles the storage and search of complex data. With Pinecone, you can use machine-learning models for content recommendation systems, personalized search, image recognition, and more. The Vercel Pinecone integration allows you to deploy your models to Vercel and use them in your applications.

### What is a vector database?

A vector database is a database that stores and searches for vectors. In this context, a vector represents a data point mathematically, often termed as an embedding.

An embedding is data that's converted to an array of numbers (a vector). The combination of the numbers that make up the vector form a multi-dimensional map used in comparison to other vectors to determine similarity.

Take the below example of two vectors, one for an image of a cat and one for an image of a dog. In the cat's vector, the first element is `0.1`, and in the dog's vector `0.2`. This similarity and difference in values illustrate how vector comparison works. The closer the values are to each other, the more similar the vectors are.

vectors

```
// Example of a vector for an image of a cat
[0.1, 0.2, 0.3, 0.4, 0.5];
// Example of a vector for an image of a dog
[(0.2, 0.3, 0.4, 0.5, 0.6)];
```

## [Use cases](#use-cases)

You can use the Vercel and Pinecone integration to power a variety of AI applications, including:

*   Personalized search: Use Pinecone's vector database to provide personalized search results. By analyzing user behavior and preferences as vectors, search engines can suggest results that are likely to interest the user
*   Image and video retrieval: Use Pinecone's vector database in image and video retrieval systems. They can quickly find images or videos similar to a given input by comparing embeddings that represent visual content
*   Recommendation systems: Use Pinecone's vector database in e-commerce apps and streaming services to help power recommendation systems. By analyzing user behavior, preferences, and item characteristics as vectors, these systems can suggest products, movies, or articles that are likely to interest the user

## [Getting started](#getting-started)

The Vercel Pinecone integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select Pinecone from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @pinecone-database/pinecone
    ```
    
10.  Connect your project using the code below:
    
    index.ts
    
    ```
    1// index.ts2import { Pinecone } from '@pinecone-database/pinecone';3
    4const pc = new Pinecone();5
    ```
    

## [Deploy a template](#deploy-a-template)

You can deploy a template to Vercel that includes a pre-trained model and a sample application that uses the model:

## [More resources](#more-resources)

[

### Pinecone Website

Learn more about Pinecone by visiting their website.

](https://pinecone.io/)[

### Pinecone Pricing

Learn more about Pinecone pricing.

](https://pinecone.io/pricing)[

### Pinecone Documentation

Visit the Pinecone documentation.

](https://docs.pinecone.io)

--------------------------------------------------------------------------------
title: "Vercel Replicate IntegrationConnectable Account"
description: "Learn how to add Replicate connectable account integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/replicate"
--------------------------------------------------------------------------------

# Vercel Replicate Integration

Connectable Account

Copy page

Ask AI about this page

Last updated June 26, 2025

[Replicate](https://replicate.com) provides a platform for accessing and deploying a wide range of open-source artificial intelligence models. These models span various AI applications such as image and video processing, natural language processing, and audio synthesis. With the Vercel Replicate integration, you can incorporate these AI capabilities into your applications, enabling advanced functionalities and enhancing user experiences.

## [Use cases](#use-cases)

You can use the Vercel and Replicate integration to power a variety of AI applications, including:

*   Content generation: Use Replicate for generating text, images, and audio content in creative and marketing applications
*   Image and video processing: Use Replicate in applications for image enhancement, style transfer, or object detection
*   NLP and chat-bots: Use Replicate's language processing models in chat-bots and natural language interfaces

### [Available models](#available-models)

Replicate models cover a broad spectrum of AI applications ranging from image and video processing to natural language processing and audio synthesis.

### Some available models on Replicate

Blip

**Type:** Image

Generate image captions

Flux 1.1 Pro

**Type:** Image

Faster, better FLUX Pro. Text-to-image model with excellent image quality, prompt adherence, and output diversity.

Flux.1 Dev

**Type:** Image

A 12 billion parameter rectified flow transformer capable of generating images from text descriptions

Flux.1 Pro

**Type:** Image

State-of-the-art image generation with top of the line prompt following, visual quality, image detail and output diversity.

Flux.1 Schnell

**Type:** Image

The fastest image generation model tailored for local development and personal use

Ideogram v2

**Type:** Image

An excellent image model with state of the art inpainting, prompt comprehension and text rendering

Ideogram v2 Turbo

**Type:** Image

A fast image model with state of the art inpainting, prompt comprehension and text rendering.

Incredibly Fast Whisper

**Type:** Audio

whisper-large-v3, incredibly fast, powered by Hugging Face Transformers.

Llama 3 70B Instruct

**Type:** Chat

A 70 billion parameter language model from Meta, fine tuned for chat completions

Llama 3 8B Instruct

**Type:** Image

An 8 billion parameter language model from Meta, fine tuned for chat completions

Llama 3.1 405B Instruct

**Type:** Chat

Meta's flagship 405 billion parameter language model, fine-tuned for chat completions

LLaVA 13B

**Type:** Image

Visual instruction tuning towards large language and vision models with GPT-4 level capabilities

Moondream2

**Type:** Image

Moondream2 is a small vision language model designed to run efficiently on edge devices

Recraft V3

**Type:** Image

Recraft V3 (code-named red\_panda) is a text-to-image model with the ability to generate long texts, and images in a wide list of styles. As of today, it is SOTA in image generation, proven by the Text-to-Image Benchmark by Artificial Analysis

Recraft V3 SVG

**Type:** Image

Recraft V3 SVG (code-named red\_panda) is a text-to-image model with the ability to generate high quality SVG images including logotypes, and icons. The model supports a wide list of styles.

Sana

**Type:** Image

A fast image model with wide artistic range and resolutions up to 4096x4096

Stable Diffusion 3.5 Large

**Type:** Image

A text-to-image model that generates high-resolution images with fine details. It supports various artistic styles and produces diverse outputs from the same prompt, thanks to Query-Key Normalization.

Stable Diffusion 3.5 Large Turbo

**Type:** Image

A text-to-image model that generates high-resolution images with fine details. It supports various artistic styles and produces diverse outputs from the same prompt, with a focus on fewer inference steps

Stable Diffusion 3.5 Medium

**Type:** Image

2.5 billion parameter image model with improved MMDiT-X architecture

## [Getting started](#getting-started)

The Vercel Replicate integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select Replicate from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i replicate
    ```
    
10.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/predictions/route.ts
    
    ```
    1// app/api/predictions/route.ts2
    3import { NextResponse } from 'next/server';4import Replicate from 'replicate';5
    6const replicate = new Replicate({7  auth: process.env.REPLICATE_API_TOKEN,8});9
    10// In production and preview deployments (on Vercel), the VERCEL_URL environment variable is set.11// In development (on your local machine), the NGROK_HOST environment variable is set.12const WEBHOOK_HOST = process.env.VERCEL_URL13  ? `https://${process.env.VERCEL_URL}`14  : process.env.NGROK_HOST;15
    16export async function POST(request) {17  if (!process.env.REPLICATE_API_TOKEN) {18    throw new Error(19      'The REPLICATE_API_TOKEN environment variable is not set. See README.md for instructions on how to set it.',20    );21  }22
    23  const { prompt } = await request.json();24
    25  const options = {26    version: '8beff3369e81422112d93b89ca01426147de542cd4684c244b673b105188fe5f',27    input: { prompt },28  };29
    30  if (WEBHOOK_HOST) {31    options.webhook = `${WEBHOOK_HOST}/api/webhooks`;32    options.webhook_events_filter = ['start', 'completed'];33  }34
    35  // A prediction is the result you get when you run a model, including the input, output, and other details36  const prediction = await replicate.predictions.create(options);37
    38  if (prediction?.error) {39    return NextResponse.json({ detail: prediction.error }, { status: 500 });40  }41
    42  return NextResponse.json(prediction, { status: 201 });43}44
    45// app/api/predictions/[id]/route.ts46
    47import { NextResponse } from 'next/server';48import Replicate from 'replicate';49
    50const replicate = new Replicate({51  auth: process.env.REPLICATE_API_TOKEN,52});53
    54// Poll for the prediction's status55export async function GET(request, { params }) {56  const { id } = params;57  const prediction = await replicate.predictions.get(id);58
    59  if (prediction?.error) {60    return NextResponse.json({ detail: prediction.error }, { status: 500 });61  }62
    63  return NextResponse.json(prediction);64}65
    ```
    

## [Deploy a template](#deploy-a-template)

You can deploy a template to Vercel that uses a pre-trained model from Replicate:

## [More resources](#more-resources)

[

### Replicate Website

Learn more about Replicate by visiting their website.

](https://replicate.com)[

### Replicate Pricing

Learn more about Replicate pricing.

](https://replicate.com/pricing)[

### Replicate Documentation

Visit the Replicate documentation.

](https://replicate.com/docs)

--------------------------------------------------------------------------------
title: "Vercel Together AI IntegrationConnectable Account"
description: "Learn how to add Together AI connectable account integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/togetherai"
--------------------------------------------------------------------------------

# Vercel Together AI Integration

Connectable Account

Copy page

Ask AI about this page

Last updated June 26, 2025

[Together AI](https://www.together.ai/) offers models for interactive AI experiences, focusing on collaborative and real-time engagement. Integrating Together AI with Vercel empowers your applications with enhanced user interaction and co-creative functionalities.

## [Use cases](#use-cases)

You can use the Vercel and Together AI integration to power a variety of AI applications, including:

*   Co-creative platforms: Use Together AI in platforms that enable collaborative creative processes, such as design or writing
*   Interactive learning environments: Use Together AI in educational tools for interactive and adaptive learning experiences
*   Real-time interaction tools: Use Together AI for developing applications that require real-time user interaction and engagement

### [Available models](#available-models)

Together AI offers models that specialize in collaborative and interactive AI experiences. These models are adept at facilitating real-time interaction, enhancing user engagement, and supporting co-creative processes.

### Some available models on Together AI

Nous Hermes 2 - Mixtral 8x7B-DPO

**Type:** Chat

Nous Hermes 2 Mixtral 8x7B DPO is the new flagship Nous Research model trained over the Mixtral 8x7B MoE LLM.

Llama 3.1 70B Instruct Turbo

**Type:** Chat

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.1 8B Instruct Turbo

**Type:** Chat

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.1 405B Instruct Turbo

**Type:** Chat

Llama 3.1 is an auto-regressive language model that uses an optimized transformer architecture.

Llama 3.2 3B Instruct Turbo

**Type:** Chat

Llama 3.2 is an auto-regressive language model that uses an optimized transformer architecture.

Llama-3.3-70b-Instruct-Turbo

**Type:** Chat

The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out).

Mistral 7B Instruct v0.3

**Type:** Chat

The Mistral 7B Instruct v0.3 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral 7B v0.3.

Mythomax L2 (13B)

**Type:** Chat

A variant of Mythomix proficient at both roleplaying and storywriting.

## [Getting started](#getting-started)

The Vercel Together AI integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select Together AI from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/togetherai ai
    ```
    
10.  Connect your project using the code below:
    
    index.ts
    
    ```
    1// index.ts2
    3import { togetherai } from '@ai-sdk/togetherai';4import { generateText } from 'ai';5
    6const { text } = await generateText({7  model: togetherai('meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo'),8  prompt: 'Write a vegetarian lasagna recipe for 4 people.',9});10
    ```
    

## [More resources](#more-resources)

[

### Together AI Website

Learn more about Together AI by visiting their website.

](https://www.together.ai/)[

### Together AI Pricing

Learn more about Together AI pricing.

](https://www.together.ai/pricing)[

### Together AI Documentation

Visit the Together AI documentation.

](https://docs.together.ai/)

--------------------------------------------------------------------------------
title: "Vercel xAI IntegrationNative Integration"
description: "Learn how to add the xAI native integration with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/ai/xai"
--------------------------------------------------------------------------------

# Vercel xAI Integration

Native Integration

Copy page

Ask AI about this page

Last updated March 19, 2025

[xAI](https://x.ai/) provides language, chat and vision AI capabilities with integrated billing through Vercel.

## [Use cases](#use-cases)

You can use the [Vercel and xAI integration](https://vercel.com/marketplace/xai) to:

*   Perform text generation, translation and question answering in your Vercel projects.
*   Use the language with vision model for advanced language understanding and visual processing.

### [Available models](#available-models)

xAI provides language and language with vision AI models.

### Some available models on xAI

Grok-2

**Type:** Chat

Grok-2 is a large language model that can be used for a variety of tasks, including text generation, translation, and question answering.

Grok-2 Vision

**Type:** Image

Grok-2 Vision is a multimodal AI model that combines advanced language understanding with powerful visual processing capabilities.

Grok 2 Image

**Type:** Image

A text-to-image model that can generate high-quality images across several domains where other image generation models often struggle. It can render precise visual details of real-world entities, text, logos, and can create realistic portraits of humans.

Grok-3 Beta

**Type:** Chat

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science.

Grok-3 Fast Beta

**Type:** Chat

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science. Fast mode delivers reduced latency and a quicker time-to-first-token.

Grok-3 Mini Beta

**Type:** Chat

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science. Fast mode delivers reduced latency and a quicker time-to-first-token. Mini is a lightweight model that thinks before responding. Great for simple or logic-based tasks that do not require deep domain knowledge. The raw thinking traces are accessible.

Grok-3 Mini Fast Beta

**Type:** Chat

xAI's flagship model that excels at enterprise use cases like data extraction, coding, and text summarization. Possesses deep domain knowledge in finance, healthcare, law, and science. Fast mode delivers reduced latency and a quicker time-to-first-token. Mini is a lightweight model that thinks before responding. Fast mode delivers reduced latency and a quicker time-to-first-token.

## [Getting started](#getting-started)

The Vercel xAI integration can be accessed through the AI tab on your [Vercel dashboard](/dashboard).

### [Prerequisites](#prerequisites)

To follow this guide, you'll need the following:

*   An existing [Vercel project](/docs/projects/overview#creating-a-project)
*   The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    

### [Add the provider to your project](#add-the-provider-to-your-project)

#### [Using the dashboard](#using-the-dashboard)

1.  Navigate to the AI tab in your [Vercel dashboard](/dashboard)
2.  Select xAI from the list of providers, and press Add
3.  Review the provider information, and press Add Provider
4.  You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
    *   If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
    *   Multiple projects can be selected during this step
5.  Select the Connect to Project button
6.  You'll be redirected to the provider's website to complete the connection process
7.  Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8.  Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
    
    terminal
    
    ```
    vercel env pull
    ```
    
9.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/xai ai
    ```
    
10.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2
    3import { xai } from '@ai-sdk/xai';4import { streamText } from 'ai';5
    6// Allow streaming responses up to 30 seconds7export const maxDuration = 30;8
    9export async function POST(req: Request) {10  // Extract the `messages` from the body of the request11  const { messages } = await req.json();12
    13  // Call the language model14  const result = streamText({15    model: xai('grok-2-1212'),16    messages,17  });18
    19  // Respond with the stream20  return result.toDataStreamResponse();21}22
    ```
    

#### [Using the CLI](#using-the-cli)

1.  Add the provider to your project using the [Vercel CLI `install`](/docs/cli/install) command
    
    terminal
    
    ```
    vercel install xai
    ```
    
    During this process, you will be asked to open the dashboard to accept the marketplace terms if you have not installed this integration before. You can also choose which project(s) the provider will have access to.
2.  Install the providers package
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @ai-sdk/xai ai
    ```
    
3.  Connect your project using the code below:
    
    Next.js (/app)Next.js (/pages)SvelteKitOther frameworks
    
    app/api/chat/route.ts
    
    ```
    1// app/api/chat/route.ts2
    3import { xai } from '@ai-sdk/xai';4import { streamText } from 'ai';5
    6// Allow streaming responses up to 30 seconds7export const maxDuration = 30;8
    9export async function POST(req: Request) {10  // Extract the `messages` from the body of the request11  const { messages } = await req.json();12
    13  // Call the language model14  const result = streamText({15    model: xai('grok-2-1212'),16    messages,17  });18
    19  // Respond with the stream20  return result.toDataStreamResponse();21}22
    ```
    

## [More resources](#more-resources)

[

### xAI Website

Learn more about xAI by visiting their website.

](https://x.ai/)[

### xAI Pricing

Learn more about xAI pricing.

](https://docs.x.ai/docs/models)[

### xAI Documentation

Visit the xAI documentation.

](https://docs.x.ai/docs/overview)[

### xAI AI SDK page

Visit the xAI AI SDK reference page.

](https://sdk.vercel.ai/providers/ai-sdk-providers/xai)

--------------------------------------------------------------------------------
title: "Alerts"
description: "Get notified when something's wrong with your Vercel projects. Set up alerts through Slack, webhooks, or email so you can fix issues quickly."
last_updated: "null"
source: "https://vercel.com/docs/alerts"
--------------------------------------------------------------------------------

# Alerts

Copy page

Ask AI about this page

Last updated October 23, 2025

Alerts are available in [Beta](/docs/release-phases#beta) on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans with [Observability Plus](/docs/observability/observability-plus)

Alerts let you know when something's wrong with your Vercel projects, like a spike in failed function invocations or unusual usage patterns. You can get these alerts by email, through Slack, or set up a webhook so you can jump on issues quickly.

By default, you'll be notified about:

*   Usage anomaly: When your project's usage exceeds abnormal levels.
*   Error anomaly: When your project's error rate of function invocations (those with a status code of 5xx) exceeds abnormal levels.

## [Alert types](#alert-types)

| Alert Type | Triggered when | Webhook Event | Slack Event |
| --- | --- | --- | --- |
| Error Anomaly | Fires when your 5-minute error rate (5xx) is more than 4 standard deviations above your 24-hour average and exceeds the minimum threshold. | [observability.error-anomaly](/docs/webhooks/webhooks-api#observability.error-anomaly) | observability\_anomaly\_error |
| Usage Anomaly | Fires when your 5-minute usage is more than 4 standard deviations above your 24-hour average and exceeds the minimum threshold. | [observability.usage-anomaly](/docs/webhooks/webhooks-api#observability.usage-anomaly) | observability\_anomaly |

## [Configure alerts](#configure-alerts)

Here's how to configure alerts for your projects:

1.  First, head to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability%2Falerts).
2.  Go to the Observability tab, find the Alerts tab, and click Subscribe to Alerts.
3.  Then, pick how you'd like to be notified: [Email](#vercel-notifications), [Slack](#slack-integration), or [Webhook](#webhook).

### [Vercel Notifications](#vercel-notifications)

You can subscribe to alerts about anomalies through the standard [Vercel notifications](/docs/notifications), which will notify you through either email or the Vercel dashboard.

By default, users with team owner roles will receive notifications.

To enable notifications:

1.  Go to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability%2Falerts), head to Observability, then Alerts.
2.  Click Subscribe to Alerts.
3.  Click Manage next to Vercel Notifications.
4.  Select which alert you'd like to receive to each of the notification channels.

You can configure your own notification preferences in your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fnotifications&title=Manage+Notifications). You cannot configure notification preferences for other users.

### [Slack integration](#slack-integration)

You'll need the correct permissions in your Slack workspace to install the Slack integration.

1.  Install the Vercel [Slack integration](https://vercel.com/integrations/slack) if you haven't already.
    
2.  Go to the Slack channel where you want alerts and run this command for alerts about usage and error anomalies:
    
    ```
    /vercel subscribe [team/project] observability_anomaly observability_error_anomaly
    ```
    
    The dashboard will show you the exact command for your team or project.
    

### [Webhook](#webhook)

With webhooks, you can send alerts to any destination.

1.  Go to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability%2Falerts), head to Observability, then Alerts.
2.  Click Subscribe to Alerts.
3.  Choose Subscribe to webhook.
4.  Fill out the webhook details:
    *   Pick which [observability events](#alert-types) to listen to
    *   Choose which projects to monitor
    *   Add your endpoint URL

You can also set this up through [account webhooks](/docs/webhooks#account-webhooks), just pick the events you want under Observability Events.

#### [Webhooks payload](#webhooks-payload)

To learn more about the webhook payload, see the [Webhooks API Reference](/docs/webhooks/webhooks-api) for each event type:

*   [Usage anomaly](/docs/webhooks/webhooks-api#observability.usage-anomaly)
*   [Error anomaly](/docs/webhooks/webhooks-api#observability.error-anomaly)

## [Investigate alerts with AI](#investigate-alerts-with-ai)

When you get an error alert, [Agent Investigation](/docs/agent/investigation) can run automatically to help you debug faster. Instead of manually digging through logs and metrics, AI analyzes what's happening and displays highlights of the anomaly directly in your dashboard.

When you view an alert in the dashboard, you can click the Enable Auto Run button to run an investigation automatically. You'll then be brought to the Agents tab to allow you set up Investigations automatically on new alerts. In addition, you can click the Rerun button to run an investigation manually.

Learn more in the [Agent Investigation docs](/docs/agent/investigation).

--------------------------------------------------------------------------------
title: "Vercel Web Analytics"
description: "With Web Analytics, you can get detailed insights into your website's visitors with new metrics like top pages, top referrers, and demographics."
last_updated: "null"
source: "https://vercel.com/docs/analytics"
--------------------------------------------------------------------------------

# Vercel Web Analytics

Copy page

Ask AI about this page

Last updated September 24, 2025

Web Analytics are available on [all plans](/docs/plans)

![Visitors tab data.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fanalytics%2Fvisitor-chart-light.png&w=3840&q=75)![Visitors tab data.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fanalytics%2Fvisitor-chart-dark.png&w=3840&q=75)

Visitors tab data.

Web Analytics provides comprehensive insights into your website's visitors, allowing you to track the top visited pages, referrers for a specific page, and demographics like location, operating systems, and browser information. Vercel's Web Analytics offers:

*   Privacy: Web Analytics only stores anonymized data and [does not use cookies](#how-visitors-are-determined), providing data for you while respecting your visitors' privacy and web experience.
*   Integrated Infrastructure: Web Analytics is built into the Vercel platform and accessible from your project's dashboard so there's no need for third-party services for detailed visitor insights.
*   Customizable: You can configure Web Analytics to track custom events and feature flag usage to get a better understanding of how your visitors are using your website.

To set up Web Analytics for your project, see the [Quickstart](/docs/analytics/quickstart).

If you're interested in learning more about how your site is performing, use [Speed Insights](/docs/speed-insights).

## [Visitors](#visitors)

The Visitors tab displays all your website's unique visitors within a selected timeframe. You can adjust the timeframe by selecting a value from the dropdown in the top right hand corner.

You can use the [panels](#panels) section to view a breakdown of specific information, organized by the total number of visitors.

### [How visitors are determined](#how-visitors-are-determined)

Instead of relying on cookies like many analytics products, visitors are identified by a hash created from the incoming request. Using a generated hash provides a privacy-friendly experience for your visitors and means visitors can't be tracked between different days or different websites.

The generated hash is valid for a single day, at which point it is automatically reset.

If a visitor loads your website for the first time, we immediately track this visit as a page view. Subsequent page views are tracked through the native browser API.

## [Page views](#page-views)

The Page Views tab, like the Visitors tab, shows a breakdown of every page loaded on your website during a certain time period. Page views are counted by the total number of views on a page. For page views, the same visitor can view the same page multiple times resulting in multiple events.

You can use the [panels](#panels) section to view a breakdown of specific information, organized by the total number of page views.

## [Bounce rate](#bounce-rate)

The Bounce rate is the percentage of visitors who land on a page and leave without taking any further action.

The higher the bounce rate, the less engaging the page is.

### [How bounce rate is calculated](#how-bounce-rate-is-calculated)

Bounce Rate (%) = (Single-Page Sessions / Total Sessions) × 100

Web Analytics defines a session as a group or page views by the same visitor. Custom event do not count towards the bounce rate.

For that reason, when filtering the dashboard for a given custom event, the bounce rate will always be 0%.

## [Panels](#panels)

Panels provide a way to view detailed analytics for Visitors and Page Views, such as top pages and referrers. They'll also show additional information such as the country, OS, and device or browser of your visitors, and configured options such as [custom events](/docs/analytics/custom-events) and [feature flag](/docs/feature-flags) usage.

By default, panels provide you with a list of top entries, categorized by the number of visitors. Depending on the panel, the information is displayed either as a number or percentage of the total visitors. You can click View All to see all the data:

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fpanels-light-mode.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fpanels-dark-mode.png&w=3840&q=75)

Panels showing a breakdown of page view data.

You can export the up to 250 entries from the panel as a CSV file. See [Exporting data as CSV](/docs/analytics/using-web-analytics#exporting-data-as-csv) for more information.

## [Bots](#bots)

Web Analytics does not count traffic that comes from automated processes or accounts. This is determined by inspecting the [User Agent](https://developer.mozilla.org/docs/Web/HTTP/Headers/User-Agent) header for incoming requests.

--------------------------------------------------------------------------------
title: "Tracking custom events"
description: "Learn how to send custom analytics events from your application."
last_updated: "null"
source: "https://vercel.com/docs/analytics/custom-events"
--------------------------------------------------------------------------------

# Tracking custom events

Copy page

Ask AI about this page

Last updated September 24, 2025

Custom Events are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Vercel Web Analytics allows you to track custom events in your application using the `track()` function. This is useful for tracking user interactions, such as button clicks, form submissions, or purchases.

Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).

## [Tracking a client-side event](#tracking-a-client-side-event)

To track an event:

1.  Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).
    
2.  Import `{ track }` from `@vercel/analytics`.
    
3.  In most cases you will want to track an event when a user performs an action, such as clicking a button or submitting a form, so you should use this on the button handler.
    
4.  Call `track` and pass in a string representing the event name as the first argument. You can also pass [custom data](#tracking-an-event-with-custom-data) as the second argument:
    
    component.ts
    
    ```
    import { track } from '@vercel/analytics';
     
    // Call this function when a user clicks a button or performs an action you want to track
    track('Signup');
    ```
    

This will track an event named **Signup**.

For example, if you have a button that says Sign Up, you can track an event when the user clicks the button:

components/button.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { track } from '@vercel/analytics';
 
function SignupButton() {
  return (
    <button
      onClick={() => {
        track('Signup');
        // ... other logic
      }}
    >
      Sign Up
    </button>
  );
}
```

## [Tracking an event with custom data](#tracking-an-event-with-custom-data)

You can also pass custom data along with an event. To do so, pass an object with key-value pairs as the second argument to `track()`:

component.ts

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
track('Signup', { location: 'footer' });
track('Purchase', { productName: 'Shoes', price: 49.99 });
```

This tracks a "Signup" event that occurred in the "footer" location. The second event tracks a "Purchase" event with product name and a price.

## [Tracking a server-side event](#tracking-a-server-side-event)

In scenarios such as when a user signs up or makes a purchase, it's more useful to track an event on the server-side. For this, you can use the `track` function on API routes or server actions.

To set up server-side events:

1.  Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).
2.  Import `{ track }` from `@vercel/analytics/server`.
3.  Use the `track` function in your API routes or server actions.
4.  Pass in a string representing the event name as the first argument to the `track` function. You can also pass [custom data](#tracking-an-event-with-custom-data) as the second argument.

For example, if you want to track a purchase event:

app/actions.ts

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
'use server';
import { track } from '@vercel/analytics/server';
 
export async function purchase() {
  await track('Item purchased', {
    quantity: 1,
  });
}
```

## [Limitations](#limitations)

The following limitations apply to custom data:

*   The number of custom data properties you can pass is limited based on your [plan](/docs/analytics/limits-and-pricing).
*   Nested objects are not supported.
*   Allowed values are `strings`, `numbers`, `booleans`, and `null`.
*   You cannot set event name, key, or values to longer than 255 characters each.

## [Tracking custom events in the dashboard](#tracking-custom-events-in-the-dashboard)

Once you have tracked an event, you can view and filter for it in the dashboard. To view your events:

1.  Go to your [dashboard](/dashboard), select your project, and click the Analytics tab.
2.  From the Web Analytics page, scroll to the Events panel.
3.  The events panel displays a list of all the event names that you have created in your project. Select the event name to drill down into the event data.
4.  The event details page displays a list, organized by custom data properties, of all the events that have been tracked.

--------------------------------------------------------------------------------
title: "Filtering Analytics"
description: "Learn how filters allow you to explore insights about your website's visitors."
last_updated: "null"
source: "https://vercel.com/docs/analytics/filtering"
--------------------------------------------------------------------------------

# Filtering Analytics

Copy page

Ask AI about this page

Last updated September 15, 2025

Web Analytics provides you with a way to filter your data in order to gain a deeper understanding of your website traffic. This guide will show you how to use the filtering feature and provide examples of how to use it to answer specific questions.

## [Using filters](#using-filters)

To filter the Web Analytics view:

1.  Select a project from the dashboard and then click the Analytics tab.
2.  Click on any row within a data panel you want to filter by. You can use multiple filters simultaneously. The following filters are available:

*   Routes (if your application is based on a [supported framework](/docs/analytics/quickstart#add-the-analytics-component-to-your-app))
*   Pages
*   Hostname
*   Referrers
*   UTM Parameters (available with [Web Analytics Plus](/docs/analytics/limits-and-pricing) and Enterprise)
*   Country
*   Browsers
*   Devices
*   Operating System
*   If configured: [Custom Events](/docs/analytics/custom-events) and [Feature Flags](/docs/feature-flags)

1.  All panels on the Web Analytics page will then update to show data filtered to your selection.

For example, if you want to see data for visitors from the United States:

1.  Search for "United States" within the Country panel.
2.  Click on the row:

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fweb-analytics%2Ffilter-us-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fweb-analytics%2Ffilter-us-dark.png&w=3840&q=75)

## [Examples of using filters](#examples-of-using-filters)

By using the filtering feature in Web Analytics, you can gain a deeper understanding of your website traffic and make data-driven decisions.

### [Find where visitors of a specific page came from](#find-where-visitors-of-a-specific-page-came-from)

Let's say you want to find out where people came from that viewed your "About Us" page. To do this:

1.  First, apply a filter in the Pages panel and click on the `/about-us` page. This will show you all of the data for visitors who viewed that page.
2.  In the Referrer panel you can view all external pages that link directly to the filtered page.

### [Understand content popularity in a specific country](#understand-content-popularity-in-a-specific-country)

You can use the Web Analytics dashboard to find out what content people from a specific country viewed. For example, to see what pages visitors from Canada viewed:

1.  Go to the Countries panel, select View All to bring up the filter box.
2.  Search for "Canada" and click on the row labeled "Canada". This will show you all of the data for visitors from Canada.
3.  Go to the Pages panel to see what specific pages they viewed.

### [Discover route popularity from a specific referrer](#discover-route-popularity-from-a-specific-referrer)

To find out viewed pages from a specific referrer, such as Google:

1.  From the Analytics tab, go to the Referrers panel.
2.  Locate the row for "google.com" and click on it. This will show you all of the data for visitors who came from google.com.
3.  Go to the Routes panel to see what specific pages they viewed.

## [Drill-downs](#drill-downs)

You can user certain panels to drill down into more specific information:

*   The Referrers panel lets you drill-down into your referral data to identify the sources of referral traffic, and find out which specific pages on a website are driving traffic to your site. By default, the Referrers panel only shows top level domains, but by clicking on one of the domains, you can start a drill-down and reveal all sub-pages that refer to your website.
*   The Flags panel lets you drill down into your feature flag data to find out which flag options are causing certain events to occur and how many times each option is being used.
*   The Custom Events panel lets you drill down into your custom event data to find out which events are occurring and how many times they are occurring. The options available will depend on the [custom data you have configured](/docs/analytics/custom-events#tracking-an-event-with-custom-data).

## [Find Tweets from t.co referrer](#find-tweets-from-t.co-referrer)

Web Analytics allows you to track the origin of traffic from Twitter by using the Twitter Resolver feature. This feature can be especially useful for understanding the performance of Twitter campaigns, identifying the sources of referral traffic and finding out the origin of a specific link.

To use it:

1.  From the Referrers panel, click View All and search for `t.co`
2.  Click on the `t.co` row to filter for it. This performs a drill-down, which reveals all `t.co` links that refer to your page.
3.  Clicking on any of these links a new tab will open and and redirect you to the Twitter search page with the URL as the search parameter. From there, you can find the original post of the link and gain insights into the traffic coming from Twitter.

Twitter search might not always be able to resolve to the original post of that link, and it may appear multiple times.

--------------------------------------------------------------------------------
title: "Pricing for Web Analytics"
description: "Learn about pricing for Vercel Web Analytics."
last_updated: "null"
source: "https://vercel.com/docs/analytics/limits-and-pricing"
--------------------------------------------------------------------------------

# Pricing for Web Analytics

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Pricing](#pricing)

The Web Analytics pricing model is based on the number of [collected events](#what-is-an-event-in-vercel-web-analytics) across all projects of your team. Once you've enabled Vercel Web Analytics, you will have access to various features depending on your plan.

|  | Hobby | Pro | [Pro with Web Analytics Plus](#pro-with-web-analytics-plus) | Enterprise |
| --- | --- | --- | --- | --- |
| Included Events | 50,000 Events | N/A | N/A | None |
| Additional Events | \- | $3 / 100,000 Events (prorated) | $3 / 100,000 Events (prorated) | Custom |
| Included Projects | Unlimited | Unlimited | Unlimited | Unlimited |
| Reporting Window | 1 Month | 12 Months | 24 Months | 24 Months |
| [Custom Events](/docs/analytics/custom-events) | \- | Included | Included | Included |
| Properties on Custom Events | \- | 2 | 8 | 8 |
| [UTM Parameters](/docs/analytics/filtering#using-filters) | \- | \- | Included | Included |

On every billing cycle (every month for Hobby teams), you will be granted a certain number of events based on your plan.

Once you exceed your included limit, you will be charged for additional events. If your team is on the Hobby plan, we will [pause](#hobby) the collection, as you cannot be charged for extra events.

Pro teams can also purchase the [Web Analytics Plus add-on](#pro-with-web-analytics-plus) for an additional $10/month per team, which grants access to more features and an extended reporting window.

## [Usage](#usage)

The table below shows the metrics for the [Observability](/docs/pricing/observability) section of the Usage dashboard where you can view your Web Analytics usage.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Events](/docs/pricing/observability#managing-web-analytics-events) | The number of page views and custom events tracked | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](/docs/manage-and-optimize-observability#optimizing-web-analytics-events) |

See the [manage and optimize Observability usage](/docs/pricing/observability) section for more information on how to optimize your usage.

Speed Insights and Web Analytics require scripts to do collection of [data points](/docs/speed-insights/metrics#understanding-data-points). These scripts are loaded on the client-side and therefore may incur additional usage and costs for [Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) and [Edge Requests](/docs/manage-cdn-usage#edge-requests).

## [Billing information](#billing-information)

### [Hobby](#hobby)

Web Analytics are free for Hobby users within the usage limits detailed above.

Vercel will [send you notifications](/docs/notifications#on-demand-usage-notifications) as you are nearing your usage limits. You will not pay for any additional usage. However, once you exceed the limits, a three day grace period will start before Vercel will stop capturing events. In this scenario, you have two options to move forward:

*   Wait 7 days before Vercel will start collecting events again
*   Upgrade to Pro to capture more events, send custom events, and access an extended reporting window.

You can sign up for Pro and start a trial using the button below.

### Experience Vercel Pro for free

Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.

[Start your free Pro trial](/upgrade/docs-trial-button)

If you're expecting large number of page views, make sure to deploy your project to a Vercel [Team](/docs/accounts/create-a-team) on the [Pro](/docs/plans/pro) plan.

### [Pro](#pro)

For Teams on a Pro trial, the [trial will end](/docs/plans/pro-plan/trials#post-trial-decision) after 14 days.

Note that while you will not be charged during the time of the trial, once the trial ends, you will be charged for the events collected during the trial

You will be charged $0.00003 per event. These numbers are based on a per-billing cycle basis. Vercel will [send you notifications](/docs/notifications#on-demand-usage-notifications) when you get closer to spending your included credit.

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

Analytics data is not collected while your project is paused, but becomes accessible again once you upgrade to Pro.

### [Pro with Web Analytics Plus](#pro-with-web-analytics-plus)

Teams on the Pro plan can optionally extend usage and capabilities through the Web Analytics Plus [add-on](/docs/pricing#pro-plan-add-ons) for an additional $10/month per team.

When enabled, all projects within the team have access to additional features.

To upgrade to Web Analytics Plus:

1.  Visit the Vercel [dashboard](/dashboard) and select the Settings tab
2.  From the left-nav, go to Billing and scroll to the Add-ons section
3.  Under Web Analytics Plus, toggle to Enable the switch

## [FAQ](#faq)

### [What is an event in Vercel Web Analytics?](#what-is-an-event-in-vercel-web-analytics)

An event in Vercel Web Analytics is either an automatically tracked page view or a [custom event](/docs/analytics/custom-events). A page view is a default event that is automatically tracked by our script when a user visits a page on your website. A custom event is any other action that you want to track on your website, such as a button click or form submission.

### [What happens when you reach the maximum number of events?](#what-happens-when-you-reach-the-maximum-number-of-events)

*   Hobby teams won't be billed beyond their allocation. Instead, collection will be paused after the 3 days grace period.
*   Pro and Enterprise teams will be billed per collected event.

### [Is usage shared across projects?](#is-usage-shared-across-projects)

Yes, events are shared across all projects under the same Vercel account in Web Analytics. This means that the events collected by each project count towards the total event limit for your account. Keep in mind that if you have high-traffic websites or multiple projects with heavy event usage, you may need to upgrade to a higher-tier plan to accommodate your needs.

### [What is the reporting window?](#what-is-the-reporting-window)

The reporting window in Vercel Web Analytics is the length of time that your analytics data is guaranteed to be stored and viewable for analysis. While only the reporting window is guaranteed to be stored, Vercel may store your data for longer periods to give you the option to upgrade to a bigger plan without losing any data.

--------------------------------------------------------------------------------
title: "Advanced Web Analytics Config with @vercel/analytics"
description: "With the @vercel/analytics npm package, you are able to configure your application to send analytics data to Vercel."
last_updated: "null"
source: "https://vercel.com/docs/analytics/package"
--------------------------------------------------------------------------------

# Advanced Web Analytics Config with @vercel/analytics

Copy page

Ask AI about this page

Last updated March 4, 2025

## [Getting started](#getting-started)

To get started with analytics, follow our [Quickstart](/docs/analytics/quickstart) guide which will walk you through the process of setting up analytics for your project.

## [`mode`](#mode)

Override the automatic environment detection.

This option allows you to force a specific environment for the package. If not defined, it will use `auto` which tries to set the `development` or `production` mode based on available environment variables such as `NODE_ENV`.

If your used framework does not expose these environment variables, the automatic detection won't work correctly. In this case, you're able to provide the correct `mode` manually or by other helpers that your framework exposes.

If you're using the `<Analytics />` component, you can pass the `mode` prop to force a specific environment:

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics mode="production" />;
      </body>
    </html>
  );
}
```

## [`debug`](#debug)

You'll see all analytics events in the browser's console with the debug mode. This option is automatically enabled if the `NODE_ENV` environment variable is available and either `development` or `test`.

You can manually disable it to prevent debug messages in your browsers console.

To disable the debug mode for server-side events, you need to set the `VERCEL_WEB_ANALYTICS_DISABLE_LOGS` environment variable to `true`.

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics debug />
      </body>
    </html>
  );
}
```

## [`beforeSend`](#beforesend)

With the `beforeSend` option, you can modify the event data before it's sent to Vercel. Below, you will see an example that ignores all events that have a `/private` inside the URL.

Returning `null` will ignore the event and no data will be sent. You can also modify the URL and check our docs about [redacting sensitive data](/docs/analytics/redacting-sensitive-data).

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics, type BeforeSendEvent } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics
          beforeSend={(event: BeforeSendEvent) => {
            if (event.url.includes('/private')) {
              return null;
            }
            return event;
          }}
        />
      </body>
    </html>
  );
}
```

## [`endpoint`](#endpoint)

The `endpoint` option allows you to report the collected analytics to a different url than the default: `https://yourdomain.com/_vercel/insights`.

This is useful when deploying several projects under the same domain, as it allows you to keep each application isolated.

For example, when `yourdomain.com` is managed outside of Vercel:

1.  "alice-app" is deployed under `yourdomain.com/alice/*`, vercel alias is `alice-app.vercel.sh`
2.  "bob-app" is deployed under `yourdomain.com/bob/*`, vercel alias is `bob-app.vercel.sh`
3.  `yourdomain.com/_vercel/*` is routed to `alice-app.vercel.sh`

Both applications are sending their analytics to `alice-app.vercel.sh`. To restore the isolation, "bob-app" should use:

```
<Analytics endpoint="https://bob-app.vercel.sh/_vercel/insights" />
```

## [`scriptSrc`](#scriptsrc)

The `scriptSrc` option allows you to load the Web Analytics script from a different URL than the default one.

```
<Analytics scriptSrc="https://bob-app.vercel.sh/_vercel/insights/script.js" />
```

--------------------------------------------------------------------------------
title: "Privacy and Compliance"
description: "Learn how Vercel supports privacy and data compliance standards with Vercel Web Analytics."
last_updated: "null"
source: "https://vercel.com/docs/analytics/privacy-policy"
--------------------------------------------------------------------------------

# Privacy and Compliance

Copy page

Ask AI about this page

Last updated March 4, 2025

Vercel takes a privacy-focused approach to our products and strive to enable our customers to use Vercel with confidence. The company aim to be as transparent as possible so our customers have the relevant information that they need about Vercel Web Analytics to meet their compliance obligations.

## [Data collected](#data-collected)

Vercel Web Analytics can be used globally and Vercel have designed it to align with leading data protection authority guidance. When using Vercel Web Analytics, no personal identifiers that track and cross-check end users' data across different applications or websites, are collected. By default, Vercel Web Analytics allows you to use only aggregated data that can not identify or re-identify customers' end users. For more information, see [Configuring Vercel Web Analytics](#configuring-vercel-web-analytics)

The recording of data points (for example, page views or custom events) is anonymous, so you have insight into your data without it being tied to or associated with any individual, customer, or IP address.

Vercel Web Analytics does not collect or store any information that would enable you to reconstruct an end user’s browsing session across different applications or websites and/or personally identify an end user. A minimal amount of data is collected and it is used for aggregated statistics only. For information on the type of data, see the [Data Point Information](#data-point-information) section.

## [Visitor identification and data storage](#visitor-identification-and-data-storage)

Vercel Web Analytics allows you to track your website traffic and gather valuable insights without using any third-party cookies, instead end users are identified by a hash created from the incoming request.

The lifespan of a visitor session is not stored permanently, it is automatically discarded after 24 hours.

After following the dashboard instructions to enable Vercel Web Analytics, see our [Quickstart](/docs/analytics/quickstart) for a step-by-step tutorial on integrating the Vercel Web Analytics script into your application. After successfully completing the quickstart and deploying your application, the script will begin transmitting page view data to Vercel's servers.

All page views will automatically be tracked by Vercel Web Analytics, including both fresh page loads and client-side page transitions.

### [Data point information](#data-point-information)

The following information may be stored with every data point:

| Collected Value | Example Value |
| --- | --- |
| Event Timestamp | 2020-10-29 09:06:30 |
| URL | `/blog/nextjs-10` |
| Dynamic Path | `/blog/[slug]` |
| Referrer | [https://news.ycombinator.com/](https://news.ycombinator.com/) |
| Query Params (Filtered) | `?ref=hackernews` |
| Geolocation | US, California, San Francisco |
| Device OS & Version | Android 10 |
| Browser & Version | Chrome 86 (Blink) |
| Device Type | Mobile (or Desktop/Tablet) |
| Web Analytics Script Version | 1.0.0 |

## [Configuring Vercel Web Analytics](#configuring-vercel-web-analytics)

Some URLs and query parameters can include sensitive data and personal information (i.e. user ID, token, order ID or any other information that can individually identify a person). You have the ability to configure Vercel Web Analytics in a manner that suits your security and privacy needs to ensure that no personal information is collected in your custom events or page views, if desired.

For example, automatic page view tracking may track personal information `https://acme.com/[name of individual]/invoice/[12345]`. You can modify the URL by passing in the `beforeSend` function. For more information see our documentation on [redacting sensitive data](/docs/analytics/redacting-sensitive-data).

For [custom events](/docs/analytics/custom-events), you may want to prevent sending sensitive or personal information, such as email addresses, to Vercel.

--------------------------------------------------------------------------------
title: "Getting started with Vercel Web Analytics"
description: "Vercel Web Analytics provides you detailed insights into your website's visitors. This quickstart guide will help you get started with using Analytics on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/analytics/quickstart"
--------------------------------------------------------------------------------

# Getting started with Vercel Web Analytics

Copy page

Ask AI about this page

Last updated September 24, 2025

This guide will help you get started with using Vercel Web Analytics on your project, showing you how to enable it, add the package to your project, deploy your app to Vercel, and view your data in the dashboard.

Select your framework to view instructions on using the Vercel Web Analytics in your project.

## [Prerequisites](#prerequisites)

*   A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
*   A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
*   The Vercel CLI installed. If you don't have it, you can install it using the following command:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel
    ```
    

1.  ### [Enable Web Analytics in Vercel](#enable-web-analytics-in-vercel)
    
    On the [Vercel dashboard](/dashboard), select your Project and then click the Analytics tab and click Enable from the dialog.
    
    [Go to Web Analytics](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fanalytics&title=Open+Web+Analytics)
    
    Enabling Web Analytics will add new routes (scoped at `/_vercel/insights/*`) after your next deployment.
    
*   ### [Add `@vercel/analytics` to your project](#add-@vercel/analytics-to-your-project)
    
    Using the package manager of your choice, add the `@vercel/analytics` package to your project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/analytics
    ```
    3.  ### [Add the `Analytics` component to your app](#add-the-analytics-component-to-your-app)
    
    The `Analytics` component is a wrapper around the tracking script, offering more seamless integration with Next.js, including route support.
    
    Add the following code to the root layout:
    
    app/layout.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { Analytics } from '@vercel/analytics/next';
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode;
    }) {
      return (
        <html lang="en">
          <head>
            <title>Next.js</title>
          </head>
          <body>
            {children}
            <Analytics />
          </body>
        </html>
      );
    }
    ```
    
4.  ### [Deploy your app to Vercel](#deploy-your-app-to-vercel)
    
    Deploy your app using the following command:
    
    terminal
    
    ```
    vercel deploy
    ```
    
    If you haven't already, we also recommend [connecting your project's Git repository](/docs/git#deploying-a-git-repository), which will enable Vercel to deploy your latest commits to main without terminal commands.
    
    Once your app is deployed, it will start tracking visitors and page views.
    
    If everything is set up properly, you should be able to see a Fetch/XHR request in your browser's Network tab from `/_vercel/insights/view` when you visit any page.
    
5.  ### [View your data in the dashboard](#view-your-data-in-the-dashboard)
    
    Once your app is deployed, and users have visited your site, you can view your data in the dashboard.
    
    To do so, go to your [dashboard](/dashboard), select your project, and click the Analytics tab.
    
    After a few days of visitors, you'll be able to start exploring your data by viewing and [filtering](/docs/analytics/filtering) the panels.
    
    Users on Pro and Enterprise plans can also add [custom events](/docs/analytics/custom-events) to their data to track user interactions such as button clicks, form submissions, or purchases.
    

Learn more about how Vercel supports [privacy and data compliance standards](/docs/analytics/privacy-policy) with Vercel Web Analytics.

## [Next steps](#next-steps)

Now that you have Vercel Web Analytics set up, you can explore the following topics to learn more:

*   [Learn how to use the `@vercel/analytics` package](/docs/analytics/package)
*   [Learn how to set update custom events](/docs/analytics/custom-events)
*   [Learn about filtering data](/docs/analytics/filtering)
*   [Read about privacy and compliance](/docs/analytics/privacy-policy)
*   [Explore pricing](/docs/analytics/limits-and-pricing)
*   [Troubleshooting](/docs/analytics/troubleshooting)

--------------------------------------------------------------------------------
title: "Redacting Sensitive Data from Web Analytics Events"
description: "Learn how to redact sensitive data from your Web Analytics events."
last_updated: "null"
source: "https://vercel.com/docs/analytics/redacting-sensitive-data"
--------------------------------------------------------------------------------

# Redacting Sensitive Data from Web Analytics Events

Copy page

Ask AI about this page

Last updated March 4, 2025

Sometimes, URLs and query parameters may contain sensitive data. This could be a user ID, a token, an order ID, or any other data that you don't want to be sent to Vercel. In this case, you may not want them to be tracked automatically.

To prevent sensitive data from being sent to Vercel, you can pass in the `beforeSend` function that modifies the event before it is sent. To learn more about the `beforeSend` function and how it can be used with other frameworks, see the [@vercel/analytics](/docs/analytics/package) package documentation.

## [Ignoring events or routes](#ignoring-events-or-routes)

To ignore an event or route, you can return `null` from the `beforeSend` function. Returning the event or a modified version of it will track it normally.

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
import { Analytics, type BeforeSendEvent } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics
          beforeSend={(event: BeforeSendEvent) => {
            if (event.url.includes('/private')) {
              return null;
            }
            return event;
          }}
        />
      </body>
    </html>
  );
}
```

## [Removing query parameters](#removing-query-parameters)

To apply changes to the event, you can parse the URL and adjust it to your needs before you return the modified event.

In this example the query parameter `secret` is removed on all events.

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
'use client';
import { Analytics } from '@vercel/analytics/react';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics
          beforeSend={(event) => {
            const url = new URL(event.url);
            url.searchParams.delete('secret');
            return {
              ...event,
              url: url.toString(),
            };
          }}
        />
      </body>
    </html>
  );
}
```

## [Allowing users to opt-out of tracking](#allowing-users-to-opt-out-of-tracking)

You can also use `beforeSend` to allow users to opt-out of all tracking by setting a `localStorage` value (for example `va-disable`).

app/layout.tsx

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitCreate React AppNuxtVueRemixAstroHTMLOther frameworks

TypeScript

TypeScriptJavaScript

```
'use client';
import { Analytics } from '@vercel/analytics/react';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics
          beforeSend={(event) => {
            if (localStorage.getItem('va-disable')) {
              return null;
            }
            return event;
          }}
        />
      </body>
    </html>
  );
}
```

--------------------------------------------------------------------------------
title: "Vercel Web Analytics Troubleshooting"
description: "Learn how to troubleshoot common issues with Vercel Web Analytics."
last_updated: "null"
source: "https://vercel.com/docs/analytics/troubleshooting"
--------------------------------------------------------------------------------

# Vercel Web Analytics Troubleshooting

Copy page

Ask AI about this page

Last updated July 29, 2025

## [No data visible in Web Analytics dashboard](#no-data-visible-in-web-analytics-dashboard)

Issue: If you are experiencing a situation where data is not visible in the analytics dashboard or a 404 error occurs while loading `script.js`, it could be due to deploying the tracking code before enabling Web Analytics.

How to fix:

1.  Make sure that you have [enabled Analytics](/docs/analytics/quickstart#enable-web-analytics-in-vercel) in the dashboard.
2.  Re-deploy your app to Vercel.
3.  Promote your latest deployment to production. To do so, visit the project in your dashboard, and select the Deployments tab. From there, select the three dots to the right of the most recent deployment and select Promote to Production.

## [Web Analytics is not working with a proxy (e.g., Cloudflare)](#web-analytics-is-not-working-with-a-proxy-e.g.-cloudflare)

Issue: Web Analytics may not function when using a proxy, such as Cloudflare.

How to fix:

1.  Check your proxy configuration to make sure that all desired pages are correctly proxied to the deployment.
2.  Additionally, forward all requests to `/_vercel/insights/*` to the deployments to ensure proper functioning of Web Analytics through the proxy.

## [Routes are not visible in Web Analytics dashboard](#routes-are-not-visible-in-web-analytics-dashboard)

Issue: Not all data is visible in the Web Analytics dashboard

How to fix:

1.  Verify that you are using the latest version of the `@vercel/analytics` package.
2.  Make sure you are using the correct import statement.

```
import { Analytics } from '@vercel/analytics/next'; // Next.js import
```

```
import { Analytics } from '@vercel/analytics/react'; // Generic React import
```

--------------------------------------------------------------------------------
title: "Using Web Analytics"
description: "Learn how to use Vercel's Web Analytics to understand how visitors are using your website."
last_updated: "null"
source: "https://vercel.com/docs/analytics/using-web-analytics"
--------------------------------------------------------------------------------

# Using Web Analytics

Copy page

Ask AI about this page

Last updated September 30, 2025

## [Accessing Web Analytics](#accessing-web-analytics)

To access Web Analytics:

1.  Select a project from your dashboard and navigate to the Analytics tab.
2.  Select the [timeframe](/docs/analytics/using-web-analytics#specifying-a-timeframe) and [environment](/docs/analytics/using-web-analytics#viewing-environment-specific-data) you want to view data for.
3.  Use the panels to [filter](/docs/analytics/filtering) the page or event data you want to view.

## [Viewing data for a specific dimension](#viewing-data-for-a-specific-dimension)

1.  Select a project from your dashboard and navigate to the Analytics tab.
2.  Using panels you can choose whether to view data by:
    *   Pages: The page url (without query parameters) that the visitor viewed.
    *   Route: The route, as defined by your application's framework.
    *   Hostname: Use this to analyze traffic by specific domains. This is beneficial for per-country domains, or for building multi-tenant applications.
    *   Referrers: The URL of the page that referred the visitor to your site. Referrer data is tracked for custom events and for initial pageviews according to the [Referrer-Policy HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy), and only if the referring link doesn't have the `rel="noreferrer"` attribute. Subsequent soft navigation within your application doesn't include referrer data.
    *   UTM Parameters (available with [Web Analytics Plus](/docs/analytics/limits-and-pricing) and Enterprise): the forwarded UTM parameters, if any.
    *   Country: Your visitors location.
    *   Browsers: Your visitors browsers.
    *   Devices: Distinction between mobile, tablet, and desktop devices.
    *   Operating System: Your visitors operating systems.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fpage-panel-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fobservability%2Fpage-panel-dark.png&w=1920&q=75)

## [Specifying a timeframe](#specifying-a-timeframe)

1.  Select a project from your dashboard and navigate to the Analytics tab.
2.  Select the timeframe dropdown in the top-right of the page to choose a predefined timeframe. Alternatively, select the Calendar icon to specify a custom timeframe.

## [Viewing environment-specific data](#viewing-environment-specific-data)

1.  Select a project from your dashboard and navigate to the Analytics tab.
2.  Select the environments dropdown in the top-right of the page to choose Production, Preview, or All Environments. Production is selected by default.

## [Exporting data as CSV](#exporting-data-as-csv)

To export the data from a panel as a CSV file:

1.  Select the Analytics tab from your project's [dashboard](/dashboard)
2.  From the bottom of the panel you want to export data from, click the three-dot menu
3.  Select the Export as CSV button

The export will include up to 250 entries from the panel, not just the top entries.

## [Disabling Web Analytics](#disabling-web-analytics)

1.  Select a project from your dashboard and navigate to the Analytics tab.
2.  Remove the `@vercel/analytics` package from your codebase and dependencies in order to prevent your app from sending analytics events to Vercel.
3.  If events have been collected, click on the ellipsis on the top-right of the Web Analytics page and select Disable Web Analytics. If no data has been collected yet then you will see an Awaiting Data popup. From here you can click the Disable Web Analytics button:

![Awaiting Web Analytics data popup.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fweb-analytics%2Fgetting-started-light.png&w=1080&q=75)![Awaiting Web Analytics data popup.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fweb-analytics%2Fgetting-started-dark.png&w=1080&q=75)

Awaiting Web Analytics data popup.

--------------------------------------------------------------------------------
title: "Audit Logs"
description: "Learn how to track and analyze your team members' activities."
last_updated: "null"
source: "https://vercel.com/docs/audit-log"
--------------------------------------------------------------------------------

# Audit Logs

Copy page

Ask AI about this page

Last updated October 23, 2025

Audit Logs are available on [Enterprise plans](/docs/plans/enterprise)

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

Audit logs help you track and analyze your [team members'](/docs/rbac/managing-team-members) activity. They can be accessed by team members with the [owner](/docs/rbac/access-roles#owner-role) role, and are available to customers on [enterprise](/docs/plans/enterprise) plans.

![Select a timeframe to export audit logs for your team.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Faudit-logs-section-light.png&w=1920&q=75)![Select a timeframe to export audit logs for your team.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Faudit-logs-section-dark.png&w=1920&q=75)

Select a timeframe to export audit logs for your team.

## [Export audit logs](#export-audit-logs)

To export and download audit logs:

*   Go to Team Settings > Security > Audit Log
*   Select a timeframe to export a Comma Separated Value ([CSV](#audit-logs-csv-file-structure)) file containing all events occurred during that time period
*   Click the Export CSV button to download the file

The team owner requesting an export will then receive an email with a link containing the report. This link is used to access the report and is valid for 24 hours.

Reports generated for the last 90 days (three months) will not impact your billing.

## [Custom SIEM Log Streaming](#custom-siem-log-streaming)

Custom SIEM Log Streaming is available for purchase on [Enterprise plans](/docs/plans/enterprise)

In addition to the standard audit log functionalities, Vercel supports custom log streaming to your Security Information and Event Management (SIEM) system of choice. This allows you to integrate Vercel audit logs with your existing observability and security infrastructure.

We support the following SIEM options out of the box:

*   AWS S3
*   Splunk
*   Datadog
*   Google Cloud Storage

We also support streaming logs to any HTTP endpoint, secured with a custom header.

### [Allowlisting IP Addresses](#allowlisting-ip-addresses)

If your SIEM requires IP allowlisting, please use the following IP addresses:

```
23.21.184.92
34.204.154.149
44.213.245.178
44.215.236.82
50.16.203.9
52.1.251.34
52.21.49.187
174.129.36.47
```

### [Setup Process](#setup-process)

To set up custom log streaming to your SIEM:

*   From your [dashboard](/dashboard) go to Team Settings, select the Security & Privacy tab, and scroll to Audit Log
*   Click the Configure button
*   Select one of the supported SIEM providers and follow the step-by-step guide

![Select one of the supported SIEM providers](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Faudit-log-streams-light.png&w=3840&q=75)![Select one of the supported SIEM providers](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Faudit-log-streams-dark.png&w=3840&q=75)

Select one of the supported SIEM providers

The HTTP POST provider is generic solution to stream audit logs to any configured endpoint. To set this up, you need to provide:

*   URL: The endpoint that will accept HTTP POST requests
*   HTTP Header Name: The name of the header, such as `Authorization`
*   HTTP Header Value: The corresponding value, e.g. `Bearer <token>`

For the request body format, you can choose between:

*   JSON: Sends a JSON array containing event objects
*   NDJSON: Sends events as newline-delimited JSON objects, enabling individual processing

### [Audit Logs CSV file structure](#audit-logs-csv-file-structure)

The CSV file can be opened using any spreadsheet-compatible software, and includes the following fields:

| Property | Description |
| --- | --- |
| timestamp | Time and date at which the event occurred |
| action | Name for the specific event. E.g, `project.created`, `team.member.left`, `project.transfer_out.completed`, `auditlog.export.downloaded`, `auditlog.export.requested`, etc. [Learn more about it here](#actions). |
| actor\_vercel\_id | User ID of the team member responsible for an event |
| actor\_name | Account responsible for the action. For example, username of the team member |
| actor\_email | Email address of the team member responsible for a specific event |
| location | IP address from where the action was performed |
| user\_agent | Details about the application, operating system, vendor, and/or browser version used by the team member |
| previous | Custom metadata (JSON object) showing the object's previous state |
| next | Custom metadata (JSON object) showing the object's updated state |

## [`actions`](#actions)

Vercel logs the following list of `actions` performed by team members.

### [`alias`](#alias)

Maps a custom domain or subdomain to a specific deployment or URL of a project. To learn more, see the `vercel alias` [docs](/docs/cli/alias).

| Action Name | Description |
| --- | --- |
| `alias.created` | Indicates that a new alias was created |
| `alias.deleted` | Indicates that an alias was deleted |
| `alias.protection-user-access-request-requested` | An external user requested access to a protected deployment alias URL |

### [`auditlog`](#auditlog)

Refers to the audit logs of your Vercel team account.

| Action Name | Description |
| --- | --- |
| `auditlog.export.downloaded` | Indicates that an export of the audit logs was downloaded |
| `auditlog.export.requested` | Indicates that an export of the audit logs was requested |

### [`cert`](#cert)

A digital certificate to manage SSL/TLS certificates for your custom domains through the [vercel certs](/docs/cli/certs) command. It is used to authenticate the identity of a server and establish a secure connection.

| Action Name | Description |
| --- | --- |
| `cert.created` | Indicates that a new certificate was created |
| `cert.deleted` | Indicates that a new certificate was deleted |
| `cert.renewed` | Indicates that a new certificate was renewed |

### [`deploy_hook`](#deploy_hook)

Create URLs that accept HTTP POST requests to trigger deployments and rerun the build step. To learn more, see the [Deploy Hooks](/docs/deploy-hooks) docs.

| Action Name | Description |
| --- | --- |
| `deploy_hook.deduped` | A deploy hook is de-duplicated which means that multiple instances of the same hook have been combined into one |

### [`deployment`](#deployment)

Refers to a successful build of your application. To learn more, see the [deployment](/docs/deployments) docs.

| Action Name | Description |
| --- | --- |
| `deployment.deleted` | Indicates that a deployment was deleted |
| `deployment.job.errored` | Indicates that a job in a deployment has failed with an error |

### [`domain`](#domain)

A unique name that identifies your website. To learn more, see the [domains](/docs/domains) docs.

| Action Name | Description |
| --- | --- |
| `domain.auto_renew.changed` | Indicates that the auto-renew setting for a domain was changed |
| `domain.buy` | Indicates that a domain was purchased |
| `domain.created` | Indicates that a new domain was created |
| `domain.delegated` | Indicates that a domain was delegated to another account |
| `domain.deleted` | Indicates that a domain was deleted |
| `domain.move_out.requested` | Indicates that a request was made to move a domain out of the current account |
| `domain.moved_in` | Indicates that a domain was moved into the current account |
| `domain.moved_out` | Indicates that a domain was moved out of the current account |
| `domain.record.created` | Indicates that a new domain record was created |
| `domain.record.deleted` | Indicates that a new domain record was deleted |
| `domain.record.updated` | Indicates that a new domain record was updated |
| `domain.transfer_in` | Indicates that a request was made to transfer a domain into the current account |
| `domain.transfer_in.canceled` | Indicates that a request to transfer a domain into the current account was canceled |
| `domain.transfer_in.completed` | Indicates that a domain was transferred into the current account |

### [`edge_config`](#edge_config)

A key-value data store associated with your Vercel account that enables you to read data at the edge without querying an external database. To learn more, see the [Edge Config docs](/docs/edge-config).

| Action Name | Description |
| --- | --- |
| `edge_config.created` | Indicates that a new edge configuration was created |
| `edge_config.deleted` | Indicates that a new edge configuration was deleted |
| `edge_config.updated` | Indicates that a new edge configuration was updated |

### [`integration`](#integration)

Helps you pair Vercel's functionality with a third-party service to streamline installation, reduce configuration, and increase productivity. To learn more, see the [integrations docs](/docs/integrations).

| Action Name | Description |
| --- | --- |
| `integration.deleted` | Indicates that an integration was deleted |
| `integration.installed` | Indicates that an integration was installed |
| `integration.updated` | Indicates that an integration was updated |

### [`password_protection`](#password_protection)

[Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) allows visitors to access preview deployments with a password to manage team-wide access.

| Action Name | Description |
| --- | --- |
| `password_protection.disabled` | Indicates that password protection was disabled |
| `password_protection.enabled` | Indicates that password protection was enabled |

### [`preview_deployment_suffix`](#preview_deployment_suffix)

Customize the appearance of your preview deployment URLs by adding a valid suffix. To learn more, see the [preview deployment suffix](/docs/deployments/generated-urls#preview-deployment-suffix) docs.

| Action Name | Description |
| --- | --- |
| `preview_deployment_suffix.disabled` | Indicates that the preview deployment suffix was disabled |
| `preview_deployment_suffix.enabled` | Indicates that the preview deployment suffix was enabled |
| `preview_deployment_suffix.updated` | Indicates that the preview deployment suffix was updated |

### [`project`](#project)

Refers to actions performed on your Vercel [projects](/docs/projects/overview).

| Action Name | Description |
| --- | --- |
| `project.analytics.disabled` | Indicates that analytics were disabled for the project |
| `project.analytics.enabled` | Indicates that analytics were enabled for the project |
| `project.deleted` | Indicates that a project was deleted |
| `project.env_variable` | This field refers to an environment variable within a project |
| `project.env_variable.created` | Indicates that a new environment variable was created for the project |
| `project.env_variable.deleted` | Indicates that a new environment variable was deleted for the project |
| `project.env_variable.updated` | Indicates that a new environment variable was updated for the project |

### [`project.password_protection`](#project.password_protection)

Refers to the password protection settings for a project.

| Action Name | Description |
| --- | --- |
| `project.password_protection.disabled` | Indicates that password protection was disabled for the project |
| `project.password_protection.enabled` | Indicates that password protection was enabled for the project |
| `project.password_protection.updated` | Indicates that password protection was updated for the project |

### [`project.sso_protection`](#project.sso_protection)

Refers to the [Single Sign-On (SSO)](/docs/saml) protection settings for a project.

| Action Name | Description |
| --- | --- |
| `project.sso_protection.disabled` | Indicates that SSO protection was disabled for the project |
| `project.sso_protection.enabled` | Indicates that SSO protection was enabled for the project |
| `project.sso_protection.updated` | Indicates that SSO protection was updated for the project |

### [`project.rolling_release`](#project.rolling_release)

Refers to [Rolling Releases](/docs/rolling-releases) for a project, which allow you to gradually roll out deployments to production.

| Action Name | Description |
| --- | --- |
| `project.rolling_release.aborted` | Indicates that a rolling release was aborted |
| `project.rolling_release.approved` | Indicates that a rolling release was approved to advance to the next stage |
| `project.rolling_release.completed` | Indicates that a rolling release was completed successfully |
| `project.rolling_release.configured` | Indicates that the rolling release configuration was updated for the project |
| `project.rolling_release.deleted` | Indicates that a rolling release was deleted |
| `project.rolling_release.started` | Indicates that a rolling release was started |

### [`project.transfer`](#project.transfer)

Refers to the transfer of a project between Vercel accounts.

| Action Name | Description |
| --- | --- |
| `project.transfer_in.completed` | Indicates that a project transfer into the current account was completed successfully |
| `project.transfer_in.failed` | Indicates that a project transfer into the current account was failed |
| `project.transfer_out.completed` | Indicates that a project transfer out of the current account was completed successfully |
| `project.transfer_out.failed` | Indicates that a project transfer out of the current account was |
| `project.transfer.started` | Indicates that a project transfer was initiated |

### [`project.web-analytics`](#project.web-analytics)

Refers to the generation of web [analytics](/docs/analytics) for a Vercel project.

| Action Name | Description |
| --- | --- |
| `project.web-analytics.disabled` | Indicates that web analytics were disabled for the project |
| `project.web-analytics.enabled` | Indicates that web analytics were enabled for the project |

### [`shared_env_variable`](#shared_env_variable)

Refers to environment variables defined at the team level. To learn more, see the [shared environment variables](/docs/environment-variables/shared-environment-variables) docs.

| Action Name | Description |
| --- | --- |
| `shared_env_variable.created` | Indicates that a new shared environment variable was created |
| `shared_env_variable.decrypted` | Indicates that a new shared environment variable was decrypted |
| `shared_env_variable.deleted` | Indicates that a new shared environment variable was deleted |
| `shared_env_variable.updated` | Indicates that a new shared environment variable was updated |

### [`team`](#team)

Refers to actions performed by members of a Vercel [team](/docs/accounts/create-a-team).

| Action Name | Description |
| --- | --- |
| `team.avatar.updated` | Indicates that the avatar (profile picture) associated with the team was updated |
| `team.created` | Indicates that a new team was created |
| `team.deleted` | Indicates that a new team was deleted |
| `team.name.updated` | Indicates that the name of the team was updated |
| `team.slug.updated` | Indicates that the team's unique identifier, or "slug," was updated |

### [`team.member`](#team.member)

Refers to actions performed by any [team member](/docs/accounts/team-members-and-roles).

| Action Name | Description |
| --- | --- |
| `team.member.access_request.confirmed` | Indicates that an access request by a team member was confirmed |
| `team.member.access_request.declined` | Indicates that an access request by a team member was declined |
| `team.member.access_request.requested` | Indicates that a team member has requested access to the team |
| `team.member.added` | Indicates that a new member was added to the team |
| `team.member.deleted` | Indicates that a member was removed from the team |
| `team.member.joined` | Indicates that a member has joined the team |
| `team.member.left` | Indicates that a new member has left the team |
| `team.member.role.updated` | Indicates that the role of a team member was updated |

--------------------------------------------------------------------------------
title: "Bot Management"
description: "Learn how to manage bot traffic to your site."
last_updated: "null"
source: "https://vercel.com/docs/bot-management"
--------------------------------------------------------------------------------

# Bot Management

Copy page

Ask AI about this page

Last updated September 24, 2025

Bots generate nearly half of all internet traffic. While many bots serve legitimate purposes like search engine crawling and content aggregation, others originate from malicious sources. Bot management encompasses both observing and controlling all bot traffic. A key component of this is bot protection, which focuses specifically on mitigating risks from automated threats that scrape content, attempt unauthorized logins, or overload servers.

## [How bot management works](#how-bot-management-works)

Bot management systems analyze incoming traffic to identify and classify requests based on their source and intent. This includes:

*   Verifying and allowing legitimate bots that correctly identify themselves
*   Monitoring bot traffic patterns and resource consumption
*   Detecting and challenging suspicious traffic that behaves abnormally
*   Enforcing browser-like behavior by verifying navigation patterns and cache usage

### [Methods of bot management and protection](#methods-of-bot-management-and-protection)

To effectively manage bot traffic and protect against harmful bots, various techniques are used, including:

*   Signature-based detection: Inspecting HTTP requests for known bot signatures
*   Rate limiting: Restricting how often certain actions can be performed to prevent abuse
*   Challenges: [Using JavaScript checks to verify human presence](/docs/vercel-firewall/firewall-concepts#challenge)
*   Behavioral analysis: Detecting unusual patterns in user activity that suggest automation

With Vercel, you can use:

*   [Managed rulesets](/docs/vercel-waf/managed-rulesets#configure-bot-protection-managed-ruleset) to challenge specific bot traffic
*   Rate limiting and challenge actions with [WAF custom rules](/docs/vercel-waf/custom-rules) to prevent bot activity from reaching your application
*   [DDoS protection](/docs/security/ddos-mitigation) to defend your application against bot driven attacks
*   [Observability](/docs/observability) and [Firewall](/docs/vercel-firewall/firewall-observability) to monitor bot patterns, traffic sources, and the effectiveness of your bot management strategies

## [Bot protection managed ruleset](#bot-protection-managed-ruleset)

Bot protection managed ruleset is available on [all plans](/docs/plans)

With Vercel, you can use the bot protection managed ruleset to [challenge](/docs/vercel-firewall/firewall-concepts#challenge) non-browser traffic from accessing your applications. It filters out automated threats while allowing legitimate traffic.

*   It identifies clients that violate browser-like behavior and serves a javascript challenge to them.
*   It prevents requests that falsely claim to be from a browser such as a `curl` request identifying as Chrome.
*   It automatically excludes [verified bots](#verified-bots), such as Google's crawler, from evaluation.

To learn more about how the ruleset works, review the [Challenge](/docs/vercel-firewall/firewall-concepts#challenge) section of [Firewall actions](/docs/vercel-firewall/firewall-concepts#firewall-actions). To understand the details of what get logged and how to monitor your traffic, review [Firewall Observability](/docs/vercel-firewall/firewall-observability).

For trusted automated traffic, you can create [custom WAF rules](/docs/vercel-waf/custom-rules) with [bypass actions](/docs/vercel-firewall/firewall-concepts#bypass) that will allow this traffic to skip the bot protection ruleset.

### [Enable the ruleset](#enable-the-ruleset)

You can apply the ruleset to your project in [log](/docs/vercel-firewall/firewall-concepts#log) or [challenge](/docs/vercel-firewall/firewall-concepts#challenge) mode. Learn how to [configure the bot protection managed ruleset](/docs/vercel-waf/managed-rulesets#configure-bot-protection-managed-ruleset).

### [Bot protection ruleset with reverse proxies](#bot-protection-ruleset-with-reverse-proxies)

Bot Protection does not work when a reverse proxy (e.g. Cloudflare, Azure, or other CDNs) is placed in front of your Vercel deployment. This setup significantly degrades detection accuracy and performance, leading to a suboptimal end-user experience.

[Reverse proxies](/docs/security/reverse-proxy) interfere with Vercel's ability to reliably identify bots:

*   Obscured detection signals: Legitimate users may be incorrectly challenged because the proxy masks signals that Bot Protection relies on.
*   Frequent re-challenges: Some proxies rotate their exit node IPs frequently, forcing Vercel to re-initiate the challenge on every IP change.

## [AI bots managed ruleset](#ai-bots-managed-ruleset)

AI bots managed ruleset is available on [all plans](/docs/plans)

Vercel's AI bots managed ruleset allows you to control traffic from AI bots that crawl your site for training data, search purposes, or user-generated fetches.

*   It identifies and filters requests from known AI crawlers and bots.
*   It provides options to log or deny these requests based on your preferences.
*   The list of known AI bots is automatically maintained and updated by Vercel.

When new AI bots emerge, they are automatically added to Vercel's managed list and will be handled according to your existing configured action without requiring any changes on your part.

### [Enable the ruleset](#enable-the-ruleset)

You can apply the ruleset to your project in [log](/docs/vercel-firewall/firewall-concepts#log) or [deny](/docs/vercel-firewall/firewall-concepts#deny) mode. Learn how to [configure the AI bots managed ruleset](/docs/vercel-waf/managed-rulesets#configure-ai-bots-managed-ruleset).

## [Verified bots](#verified-bots)

Vercel maintains and continuously updates a comprehensive directory of known legitimate bots from across the internet. This directory is regularly updated to include new legitimate services as they emerge. [Attack Challenge Mode](/docs/vercel-firewall/attack-challenge-mode#known-bots-support) and bot protection automatically recognize and allow these bots to pass through without being challenged. You can block access to some or all of these bots by writing [WAF custom rules](/docs/vercel-firewall/vercel-waf/custom-rules) with the User Agent match condition or Signature-Agent header. To learn how to do this, review [WAF Examples](/docs/vercel-firewall/vercel-waf/examples).

### [Bot verification methods](#bot-verification-methods)

To prove that bots are legitimate and verify their claimed identity, several methods are used:

*   IP Address Verification: Checking if requests originate from known IP ranges owned by legitimate bot operators (e.g., Google's Googlebot, Bing's crawler).
*   Reverse DNS Lookup: Performing reverse DNS queries to verify that an IP address resolves back to the expected domain (e.g., an IP claiming to be Googlebot should resolve to `*.googlebot.com` or `*.google.com`).
*   Cryptographic Verification: Using digital signatures to authenticate bot requests through protocols like [Web Bot Authentication](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture), which employs HTTP Message Signatures (RFC 9421) to cryptographically verify automated requests.

### [Verified bots directory](#verified-bots-directory)

[Submit a bot request](https://bots.fyi/new-bot) if you are a SaaS provider and would like to be added to this list.

| Bot name | Category | Description | Documentation |
| --- | --- | --- | --- |
| adagiobot | advertising | Adagiobot is a web crawler that analyzes websites for advertising demand optimization, helping publishers maximize revenue through real-time bidding analysis and performance insights. AdagioBot fetches /ads.txt, /app-ads.txt and /sellers.json files to comply with IAB Supply Chain Validation. | [View](https://adagio-io.gitbook.io/adagio-documentation/general-configuration/update-your-app-ads.txt-file) |
| adidxbot | advertising | AdIdxBot is the crawler used by Bing Ads for quality control of ads and their destination websites. It has multiple user agent variants including desktop, iPhone, and Windows Phone versions. | [View](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0) |
| adsbot-google | advertising | AdsBot-Google is Google's web crawler used for quality control of Google Ads. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| adsense | advertising | The AdSense crawler visits participating sites in order to provide them with relevant ads. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| adyen-webhook | webhook | Adyen’s webhooks (Notification API) send encrypted, real-time HTTP callbacks for key payment and account events—automating order fulfillment, settlement reconciliation, and risk-management workflows. | [View](https://docs.adyen.com/development-resources/webhooks/domain-and-ip-addresses/) |
| ahrefsbot | search\_engine\_optimization | Powers the database for both Ahrefs, a marketing intelligence platform, and Yep, an independent, privacy-focused search engine. | [View](https://help.ahrefs.com/en/articles/78658-what-is-the-list-of-your-ip-ranges) |
| ahrefssiteaudit | search\_engine\_optimization | Powers Ahrefs’ Site Audit tool. Ahrefs users can use Site Audit to analyze websites and find both technical SEO and on-page SEO issues. | [View](https://help.ahrefs.com/en/articles/78658-what-is-the-list-of-your-ip-ranges) |
| algolia | search\_engine\_crawler | The Algolia Crawler extracts content from your site and makes it searchable. | [View](https://www.algolia.com/doc/tools/crawler/getting-started/overview/) |
| amazon-kendra | ai\_assistant | Amazon Kendra is a managed information retrieval and intelligent search service that uses natural language processing and advanced deep learning model. | [View](https://docs.aws.amazon.com/kendra/latest/dg/data-source-web-crawler.html) |
| amazon-q | ai\_assistant | Amazon Q Business is a generative artificial intelligence (generative AI)-powered assistant that you can tailor to your business needs. | [View](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/webcrawler-overview.html) |
| amazonbot | ai\_crawler | Amazonbot is Amazon's web crawler used to improve our services, such as enabling Alexa to more accurately answer questions for customers. | [View](https://developer.amazon.com/amazonbot) |
| apis-google | search\_engine\_crawler | Crawling preferences addressed to the APIs-Google user agent affect the delivery of push notification messages by Google APIs. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| apple-podcasts | feed\_fetcher | Apple Podcasts crawler that only accesses URLs associated with registered content on Apple Podcasts. Does not follow robots.txt. | [View](https://support.apple.com/en-us/119829) |
| applebot | ai\_crawler | Applebot powers search features in Apple's ecosystem (Spotlight, Siri, Safari) and may be used to train Apple's foundation models for generative AI features. | [View](https://support.apple.com/en-us/119829) |
| artemis-web-crawler | aggregator | Artemis is a calm web reader with which you can follow websites and blogs. | [View](https://artemis.jamesg.blog/bot) |
| baiduspider | search\_engine\_crawler | Baiduspider is Baidu’s web crawler that indexes websites for inclusion in its Chinese-market search results. | [View](https://www.baidu.jp/) |
| barkrowler | search\_engine\_optimization | Barkrowler is Babbar's web crawler that fuels and updates their graph representation of the web, providing SEO tools for the marketing community. | [View](https://www.babbar.tech/crawler) |
| better-stack | monitor | Better Stack is a platform for monitoring and alerting on your applications. | [View](https://betterstack.com/docs/uptime/frequently-asked-questions/) |
| bingbot | search\_engine\_crawler | Bingbot is Microsoft's web crawler used for indexing websites for Bing Search. | [View](https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26) |
| blexbot | search\_engine\_optimization | BLEXBot is SE Ranking's web crawler that helps analyze websites for SEO purposes, including backlink analysis, rank tracking, and website auditing. The bot is part of SE Ranking's all-in-one SEO platform used by marketing professionals and agencies. | [View](https://help.seranking.com/en/blex-crawler) |
| brightbot | monitor | Brightbot is Bright Data's crawler layer that monitors the health of websites and enforces ethical web data collection. It prevents access to non-public information and blocks interactive endpoints that could be abused, acting as a guardian for ethical data collection. | [View](https://brightdata.com/trustcenter/brightbot-ethical-web-data-guardian) |
| buffer-link-preview-bot | preview | Helps Buffer users create better social media posts by generating rich previews when they share links | [View](https://scraper.buffer.com/about/bots/link-preview-bot) |
| ccbot | ai\_crawler | CCBot is operated by the Common Crawl Foundation to crawl web content for AI training and research. Common Crawl is a non-profit organization that maintains an open repository of web crawl data that is universally accessible for research and analysis. | [View](https://commoncrawl.org/faq/) |
| chatgpt-operator | ai\_assistant | Handles user-initiated requests from ChatGPT operator accessing external content; not used for automated crawling or AI training. | [View](https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting) |
| chatgpt-user | ai\_assistant | Handles user-initiated requests in ChatGPT, accessing external content to provide real-time information; not used for automated crawling or AI training. | [View](https://platform.openai.com/docs/bots) |
| checkly | monitor | Checkly is a platform for monitoring and alerting on your applications. | [View](https://www.checklyhq.com/docs/monitoring/allowlisting/) |
| chrome-lighthouse | analytics | PageSpeed Insights (PSI) reports on the user experience of a page on both mobile and desktop devices, and provides suggestions on how that page may be improved. | [View](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers) |
| chrome-privacy-preserving-prefetch-proxy | page\_preview | Chrome's Privacy Preserving Prefetch Proxy service that fetches /.well-known/traffic-advice to enable privacy-preserving prefetch hints. | [View](https://developer.chrome.com/blog/private-prefetch-proxy) |
| claude-searchbot | ai\_assistant | Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. | [View](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| claude-user | ai\_assistant | Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. | [View](https://docs.anthropic.com/en/api/ip-addresses) |
| claudebot | ai\_crawler | ClaudeBot helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training. | [View](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| cookiebot | monitor | Cookiebot automates compliance with cookie laws and helps you manage your cookie consent preferences. | [View](https://support.cookiebot.com/hc/en-us/articles/360003824153-Whitelisting-the-Cookiebot-scanner) |
| criteobot | advertising | CriteoBot is a crawler operated by Criteo that analyzes web content to serve relevant contextual ads. The bot respects robots.txt directives and crawl delays, and only accesses publicly available content. | [View](https://www.criteo.com/criteo-crawler/) |
| customerio-webhooks | webhook | Customer.io's webhook service for event-driven marketing automation and customer data platform. | [View](https://docs.customer.io/integrations/data-out/connections/webhook/) |
| cybaa-agent | verification | Performs user-initiated security checks on behalf of Cybaa customers, validating security headers, TLS/SSL configuration, and other domain-specific security controls to ensure website compliance and protection. | [View](https://cybaa.io/bot-policy) |
| dash0-synthetic | monitor | Dash0's Synthetic Monitoring provides proactive, automated insights into the availability and performance of your websites and APIs. | [View](https://www.dash0.com/documentation/) |
| datadog-synthetic-monitoring-robot | monitor | Datadog's automated monitoring service that performs synthetic tests to verify website availability and performance. | [View](https://docs.datadoghq.com/synthetics/guide/identify_synthetics_bots/) |
| dataforseobot | search\_engine\_optimization | DataForSeoBot is a backlink checker bot operated by DataForSEO that crawls websites to build and maintain their backlink database. The bot respects robots.txt directives and crawl delays, and is used to provide SEO data and analytics services. | [View](https://dataforseo.com/dataforseo-bot) |
| detectify | monitor | Detectify is a web security scanner that performs automated security tests on web applications and attack surface monitoring. | [View](https://support.detectify.com/support/solutions/articles/48001049001-how-do-i-allow-detectify-to-scan-my-assets-) |
| duckassistbot | ai\_assistant | DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models. | [View](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) |
| duckduckbot | search\_engine\_crawler | DuckDuckBot is a web crawler for DuckDuckGo. DuckDuckBot’s job is to constantly improve search results and offer users the best and most secure search experience possible. | [View](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot) |
| facebook-webhooks | webhook | Facebook's webhook service that delivers real-time event notifications for Meta platform events and changes. | [View](https://developers.facebook.com/docs/graph-api/webhooks/) |
| facebookexternalhit | preview | Fetches content for shared links on Meta platforms to generate rich previews. | [View](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/) |
| falbot | webhook | fal.ai's webhook service that delivers asynchronous notifications for AI model processing and generation tasks. | [View](https://docs.fal.ai/model-apis/model-endpoints/webhooks/#_top) |
| feedfetcher | feed\_fetcher | Feedfetcher is used for crawling RSS or Atom feeds for Google News and PubSubHubbub. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| geedoproductsearchbot | ecommerce | GeedoProductSearch is a web crawler operated by Geedo SIA that indexes product information from e-commerce websites. The crawler respects robots.txt directives and can be configured for crawl speed and behavior through standard crawl-delay settings. | [View](https://geedo.com/product-search.html) |
| gemini-deep-research | ai\_assistant | Gemini Deep Research is Google's AI-powered research tool that performs comprehensive multi-step research on complex topics, analyzing web content to provide detailed insights and answers. | [View](https://gemini.google/overview/deep-research/) |
| github-camo | preview | GitHub's image proxy service | [View](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls) |
| github-hookshot | webhook | GitHub's webhooks for events like push, pull request, etc. | [View](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses) |
| google-cloudvertexbot | ai\_assistant | Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents. It has no effect on Google Search or other products. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-extended | ai\_crawler | Google-Extended is a standalone product token that web publishers can use to manage whether their sites help improve Gemini Apps and Vertex AI generative APIs, including future generations of models that power those products. Grounding with Google Search on Vertex AI does not use web pages for grounding that have disallowed Google-Extended. Google-Extended does not impact a site's inclusion or ranking in Google Search. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-image-proxy | preview | Google's image caching proxy service used by Gmail and other Google services to cache and serve images. | [View](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers) |
| google-inspectiontool | monitor | Crawling preferences addressed to the Google-InspectionTool user agent affect Search testing tools such as the Rich Result Test and URL inspection in Search Console. It has no effect on Google Search or other products. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-pagerenderer | page\_preview | Upon user request, Google Page Renderer fetches and renders web pages. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-publisher-center | feed\_fetcher | Google Publisher Center fetches and processes feeds that publishers explicitly supplied for use in Google News landing pages. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-read-aloud | accessibility | Upon user request, Google Read Aloud fetches and reads out web pages using text-to-speech (TTS). | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-safety | monitor | The Google-Safety user agent handles abuse-specific crawling, such as malware discovery for publicly posted links on Google properties. As such it's unaffected by crawling preferences. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-site-verifier | verification | Google Site Verifier fetches Search Console verification tokens. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| google-storebot | ecommerce | Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping (for example, the Shopping tab in Google Search and Google Shopping). | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| googlebot | search\_engine\_crawler | Crawling preferences addressed to the Googlebot user agent affect Google Search (including Discover and all Google Search features), as well as other products such as Google Images, Google Video, Google News, and Discover. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| googleother | search\_engine\_crawler | Crawling preferences addressed to the GoogleOther user agent don't affect any specific product. GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development. It has no effect on Google Search or other products. | [View](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) |
| gpt-actions | ai\_assistant | Enables ChatGPT to interact with external APIs and retrieve real-time information from the web in response to user-initiated requests; allows access to up-to-date content without being used for automated crawling or AI training. | [View](https://platform.openai.com/docs/actions/introduction) |
| gptbot | ai\_crawler | Crawls web content to improve OpenAI's generative AI models and ChatGPT; respects 'robots.txt' directives to exclude sites from training data. | [View](https://platform.openai.com/docs/bots) |
| gtmetrix | monitor | GTmetrix provides metrics and insights for your site's loading speed and performance. | [View](https://gtmetrix.com/features.html) |
| hetrixtools-uptime-monitoring-bot | monitor | HetrixTools Uptime Monitoring Bot is used by HetrixTools's monitoring services to perform various checks on websites, including uptime and performance monitoring. | [View](https://docs.hetrixtools.com/avoid-getting-our-ips-blocked/) |
| hookdeck | webhook | A reliable Event Gateway for event-driven applications | [View](https://hookdeck.com/docs) |
| hydrozen | monitor | Hydrozen is a tool for monitoring availability of your websites, Cronjobs, APIs, Domains, SSL etc. | [View](https://docs.hydrozen.io/overview/misc/user-agent-and-ip-list) |
| iframely | page\_preview | Fetches your page metadata to generate rich link previews when users share your links across apps, blogs, and news sites, enhancing content visibility and engagement. | [View](https://iframely.com/docs/about) |
| imagesiftbot | ai\_crawler | ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support Hive's suite of web intelligence products. | [View](https://imagesift.com/about) |
| inngest | webhook | Inngest is a platform for building event-driven applications. | [View](https://www.inngest.com/docs/platform/webhooks) |
| jobswithgpt | search\_engine\_crawler | Crawls job-related pages to power jobswithgpt.com, a platform for discovering AI-enhanced career opportunities. | [View](https://jobswithgpt.com/bot.html) |
| linkedinbot | preview | LinkedInBot is a bot that renders links shared on LinkedIn. | [View](https://www.linkedin.com/robots.txt) |
| logicmonitor | monitor | LogicMonitor SiteMonitor monitors your website's uptime, performance, and availability from multiple global regions. | [View](https://www.logicmonitor.com/support/data-monitored-for-websites) |
| lumar | search\_engine\_optimization | The Lumar website intelligence platform is used by SEO, engineering, marketing and digital operations teams to monitor the performance of their site’s technical health, and ensure a high-performing, revenue-driving website. | [View](https://www.lumar.io/spdr/) |
| marfeel-audits | monitor | Marfeel's audit crawlers that periodically re-crawl traffic-receiving URLs to detect structured data, meta tags, and HTML issues. | [View](https://community.marfeel.com/t/marfeel-crawlers/5966) |
| marfeel-flowcards | page\_preview | Marfeel's crawler that fetches content for Flowcards that load directly from specific URLs. | [View](https://community.marfeel.com/t/marfeel-crawlers/5966) |
| marfeel-preview | preview | Marfeel's previewer crawler used to render preview experiences for both mobile and desktop views. | [View](https://community.marfeel.com/t/marfeel-crawlers/5966) |
| marfeel-social | social\_media | Marfeel's crawler used for social experiences (Facebook, X/Twitter, Telegram, Reddit, LinkedIn). | [View](https://community.marfeel.com/t/marfeel-crawlers/5966) |
| meta-externalads | advertising | Crawls the web to improve advertising and business-related products and services. | [View](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/) |
| meta-externalagent | ai\_crawler | The Meta-ExternalAgent crawler crawls the web for use cases such as training AI models or improving products by indexing content directly. | [View](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/) |
| meta-externalfetcher | user\_initiated | The Meta-ExternalFetcher crawler performs user-initiated fetches of individual links to support specific product functions. Because the fetch was initiated by a user, this crawler may bypass robots.txt rules. | [View](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/) |
| microsoftpreview | preview | MicrosoftPreview generates page snapshots for Microsoft products. It has desktop and mobile variants, with Chrome version dynamically updated to match the latest Microsoft Edge version. | [View](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0) |
| momenticbot | user\_initiated | Momentic is a AI-powered platform for software testing. It allows you to write reliable end-to-end tests for web apps in a simple and intuitive way using natural language. | [View](https://momentic.ai/docs/quickstart/cloud) |
| adsnaver | search\_engine\_crawler | Naver's ad crawler that periodically visits registered ad landing pages to collect on-page content for effective ad matching and ranking. It ignores robots.txt for URLs registered in the ad system. | [View](https://ads.naver.com/help/faq/652) |
| naver-blueno | preview | Naver's preview-snippet crawler that fetches summary information (titles, descriptions, images) when users insert links in Naver services such as blogs or cafés. It operates on demand and respects robots.txt. | [View](https://help.naver.com/service/5626/contents/19008?lang=ko) |
| naverbot | search\_engine\_crawler | Naver's web crawler (also known as Yeti) is used by Naver, South Korea's largest search engine, to crawl and index web content. | [View](https://searchadvisor.naver.com/guide) |
| newrelic-minions | monitor | New Relic Synthetic monitoring infrastructure that performs API checks and virtual browser instances to monitor websites and applications from global locations | [View](https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/administration/synthetic-public-minion-ips) |
| oai-searchbot | ai\_assistant | Indexes websites for inclusion in ChatGPT's search results; does not crawl content for AI model training. | [View](https://platform.openai.com/docs/bots) |
| paypal | webhook | PayPal delivers real-time event notifications for payments, subscriptions, and account updates. | [View](https://developer.paypal.com/api/rest/webhooks/) |
| perplexity-user | ai\_assistant | Handles user-initiated requests in Perplexity, accessing external content to provide real-time information; not used for automated crawling or AI training. | [View](https://docs.perplexity.ai/guides/bots) |
| perplexitybot | ai\_assistant | Indexes websites for inclusion in Perplexity's search results; does not crawl content for AI model training. | [View](https://docs.perplexity.ai/guides/bots) |
| petalbot | search\_engine\_crawler | PetalBot is a web crawler operated by Huawei's Petal Search engine. It crawls both PC and mobile websites to build an index database for Petal search engine and to provide content recommendations for Huawei Assistant and AI Search services. | [View](https://webmaster.petalsearch.com/site/petalbot) |
| pingdom-bot | monitor | Pingdom Bot is used by Pingdom's monitoring services to perform various checks on websites, including uptime and performance monitoring. | [View](https://documentation.solarwinds.com/en/success_center/pingdom/content/topics/pingdom-probe-servers-ip-addresses.htm) |
| pinterest-bot | aggregator | Pinterest's web crawler that indexes content for their platform. It crawls websites to collect metadata for Pins, including images, titles, descriptions, and prices. The crawler also helps maintain Pin data accuracy and detect broken links. | [View](https://help.pinterest.com/en/business/article/pinterestbot) |
| polar-webhooks | webhook | Polar's webhook service delivers real-time event notifications for payment processing, including purchases, subscriptions, cancellations, and refunds. | [View](https://polar.sh/docs/integrate/webhooks/endpoints) |
| pulsepoint-crawler | advertising | A web crawler used by PulsePoint, a digital advertising technology company, for content indexing and ads.txt verification. | [View](https://www.pulsepoint.com/) |
| qatech | monitor | The QA.tech web agent browses the website and identifies potential test cases, and executes tests against a web application | [View](https://docs.qa.tech) |
| qstash | webhook | QStash is a platform for building event-driven applications. | [View](https://upstash.com/docs/qstash/howto/signature) |
| quantcastbot | advertising | Quantcast Bot is a web crawler used for advertisement quality assurance and to understand page content for Interest-Based Audiences. | [View](https://www.quantcast.com/bot) |
| razorpay-webhook | webhook | Razorpay’s webhooks enable merchants to receive secure, real-time HTTP callbacks for key payment events—automating reconciliation, notifications, and downstream workflows. | [View](https://razorpay.com/docs/webhooks/) |
| redirect-pizza | monitor | redirect.pizza's destination monitor ensures that the redirect destination URLs are reachable. | [View](https://redirect.pizza/support/broken-destination-monitoring) |
| amazon-route-53-health-check-service | monitor | Amazon Route 53 Health Check Service | [View](https://repost.aws/knowledge-center/route-53-fix-unwanted-health-checks) |
| ryebot | ecommerce | Powers automated checkout on behalf of shoppers with explicit consent. | [View](https://docs.rye.com/api-v2-experimental/ryebot) |
| sanity-webhooks | webhook | Sanity's webhook service that delivers real-time event notifications for content changes and other events. | [View](https://www.sanity.io/docs/webhooks) |
| sansec-security-monitor | monitor | Sansec Security Monitor is a web crawler that monitors online stores for malicious code, data breaches, and digital skimming attacks. | [View](https://sansec.io/monitor) |
| seekportbot | search\_engine\_crawler | SeekportBot is the web crawler for Seekport, a German search engine operated by SISTRIX. The bot crawls and indexes web content while respecting robots.txt directives and crawl delays. | [View](https://bot.seekport.com/) |
| semrush-site-audit | search\_engine\_optimization | Semrush Site Audit is a powerful website crawler that analyzes the health of a website by checking for on-page and technical SEO issues, including duplicate content, broken links, HTTPS implementation, hreflang attributes, and more. | [View](https://www.semrush.com/bot/) |
| semrush | search\_engine\_optimization | Semrush is a platform for SEO, content marketing, competitor research, PPC and social media marketing. | [View](https://www.semrush.com/bot/) |
| sentry-uptime-monitoring-bot | monitor | Sentry's Uptime Monitoring Bot performs health checks on configured URLs to monitor the availability and reliability of web services. | [View](https://docs.sentry.io/product/alerts/uptime-monitoring/troubleshooting/) |
| seobility | search\_engine\_crawler | Seobility is a browser-based online SEO software that helps you improve your website’s search engine rankings. | [View](https://www.seobility.net/en/faq/?category=website-crawling#aboutourbot) |
| seznambot | search\_engine\_crawler | SeznamBot is the web crawler operated by Seznam.cz, the leading Czech search engine. The bot crawls and indexes web content for Seznam's search results, respecting robots.txt directives and crawl delays. | [View](https://o-seznam.cz/napoveda/vyhledavani/en/seznambot-crawler/) |
| site24x7 | monitor | Site24x7 Bot is used by Site24x7's monitoring services to perform various checks on websites, including uptime and performance monitoring. | [View](https://www.site24x7.com/multi-location-web-site-monitoring.html) |
| statuscake-pagespeed | monitor | StatusCake Page Speed monitors your page load and render speeds. | [View](https://www.statuscake.com/kb/knowledge-base/page-speed-f-a-q/) |
| statuscake-ssl | monitor | StatusCake SSL monitors your website certificates for common issues | [View](https://www.statuscake.com/kb/article-categories/ssl-monitoring/) |
| statuscake-uptime | monitor | StatusCake monitors the uptime of your website. | [View](https://www.statuscake.com/kb/article-categories/testing/) |
| stripe-webhooks | webhook | Stripe's webhook service that delivers real-time event notifications for payment processing and account updates. | [View](https://docs.stripe.com/ips) |
| svix | webhook | svix is a webhook service for sending events to webhooks. | [View](https://docs.svix.com/receiving/source-ips) |
| termlybot | monitor | Crawls websites to detect and categorize cookies set by first and third parties. | [View](https://termly.io/bot/) |
| twitterbot | preview | Fetches content for shared links on X/Twitter to generate rich previews. | [View](https://developer.x.com/en/docs/x-for-websites/cards/guides/troubleshooting-cards) |
| uptime-robot | monitor | Uptime Robot is a platform for monitoring and alerting on your applications. | [View](https://uptimerobot.com/help/locations/) |
| v0bot | ai\_crawler | Bot for v0 services. |  |
| vercel-build-container | preview | System-initiated requests made from Vercel's build container during a build | [View](https://vercel.com/docs/builds) |
| vercel-favicon-bot | preview | Vercel Favicon Bot | [View](https://vercel.com/docs) |
| vercelflags | monitor | vercel flags | [View](https://vercel.com/docs/feature-flags/flags-explorer) |
| vercel-screenshot-bot | preview | Vercel Screenshot Bot | [View](https://vercel.com/docs) |
| verceltracing | monitor | vercel tracing | [View](https://github.com/vercel/front/pull/45573) |
| whatkilledthedog | monitor | WhatKilledTheDog monitors your website's uptime, and performance. | [View](https://www.whatkilledthedog.com/faq) |
| yahoo-ad-monitoring | advertising | Yahoo Ad Monitoring crawls landing pages of URLs listed with Yahoo advertising services to analyze content quality, ensure ad relevance, and improve user experience by maintaining accurate ad listings. | [View](https://help.yahoo.com/kb/yahoo-ad-monitoring-SLN24857.html) |
| yahoo-slurp | search\_engine\_crawler | Yahoo! Slurp is the web crawler (robot) used by Yahoo! Search to discover and index web pages for its search engine. | [View](https://help.yahoo.com/kb/SLN22600.html) |
| yandexbot | search\_engine\_crawler | YandexBot is a web crawler operated by Yandex, a major Russian search engine. | [View](https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.html) |

--------------------------------------------------------------------------------
title: "BotID"
description: "Protect your applications from automated attacks with intelligent bot detection and verification, powered by Kasada."
last_updated: "null"
source: "https://vercel.com/docs/botid"
--------------------------------------------------------------------------------

# BotID

Copy page

Ask AI about this page

Last updated September 25, 2025

BotID is available on [all plans](/docs/plans)

[Vercel BotID](/botid) is an invisible CAPTCHA that protects against sophisticated bots without showing visible challenges or requiring manual intervention. It adds a protection layer for public, high-value routes, such as checkouts, signups, and APIs, that are common targets for bots imitating real users.

## [Sophisticated bot behavior](#sophisticated-bot-behavior)

Sophisticated bots are designed to mimic real user behavior. They can run JavaScript, solve CAPTCHAs, and navigate interfaces in ways that closely resemble human interactions. Tools like Playwright and Puppeteer automate these sessions, simulating actions from page load to form submission.

These bots do not rely on spoofed headers or patterns that typically trigger rate limits. Instead, they blend in with normal traffic, making detection difficult and mitigation costly.

## [Using BotID](#using-botid)

*   [Getting Started](/docs/botid/get-started) - Setup guide with complete code examples
*   [Verified Bots](/docs/botid/verified-bots) - Information about verified bots and their handling
*   [Bypass BotID](#bypass-botid) - Configure bypass rules for BotID detection

BotID includes a [Deep Analysis mode](#how-botid-deep-analysis-works), powered by [Kasada](https://www.kasada.io/). Kasada is a leading bot protection provider trusted by Fortune 500 companies and global enterprises. It delivers advanced bot detection and anti-fraud capabilities.

BotID provides real-time protection against:

*   Automated attacks: Shield your application from credential stuffing, brute force attacks, and other automated threats
*   Data scraping: Prevent unauthorized data extraction and content theft
*   API abuse: Protect your endpoints from excessive automated requests
*   Spam and fraud: Block malicious bots while allowing legitimate traffic through
*   Expensive resources: Prevent bots from consuming expensive infrastructure, bandwidth, compute, or inventory

## [Key features](#key-features)

*   Seamless integration: Works with existing Vercel projects with minimal configuration
*   Customizable protection: Define which paths and endpoints require bot protection
*   Privacy-focused: Respects user privacy while providing robust protection
*   Deep Analysis (Kasada-powered): For the highest level of protection, enable Deep Analyis in your [Vercel Dashboard](/dashboard). This leverages Kasada's advanced detection technology to block even the most sophisticated bots.

## [BotID modes](#botid-modes)

BotID has two modes:

*   Basic - Ensures valid browser sessions are accessing your sites
*   Deep Analysis - Connects thousands of additional client side signals to further distinguish humans from bots

### [How BotID deep analysis works](#how-botid-deep-analysis-works)

With a few lines of code, you can run BotID on any endpoint. It operates by:

*   Giving you a clear yes or no response to each request
*   Deploying dynamic detection models based on a deep understanding of bots that validates requests on your server actions and route handlers to ensure only verified traffic reaches your protected endpoints
*   Quickly assessing users without disrupting user sessions

BotID counters the most advanced bots by:

1.  Silently collecting thousands of signals that distinguish human users from bots
2.  Changing detection methods on every page load to prevent reverse engineering and sophisticated bypasses
3.  Streaming attack data to a global machine learning system that improves protection for all customers

## [Pricing](#pricing)

| Mode | Plans Available | Price |
| --- | --- | --- |
| Basic | All Plans | Free |
| Deep Analysis | Pro and Enterprise | $1/1000 `checkBotId()` Deep Analysis calls |

Calling the `checkBotId()` function in your code triggers BotID Deep Analysis charges. Passive page views or requests that don't invoke the `checkBotId()` function are not charged.

## [Bypass BotID](#bypass-botid)

You can add a bypass rule to the [Vercel WAF](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass) to let through traffic that would have otherwise been detected as a bot by BotID.

### [Checking BotID traffic](#checking-botid-traffic)

You can view BotID checks by selecting BotID on the firewall traffic dropdown filter of the [Firewall tab](/docs/vercel-firewall/firewall-observability#traffic-monitoring) of a project.

Metrics are also available in [Observability Plus](/docs/observability/observability-plus).

## [More resources](#more-resources)

*   [Advanced configuration](/docs/botid/advanced-configuration) - Fine-grained control over detection levels and backend domains
*   [Form submissions](/docs/botid/form-submissions) - Handling form submissions with BotID protection
*   [Local Development Behavior](/docs/botid/local-development-behavior) - Testing BotID in development environments

--------------------------------------------------------------------------------
title: "Advanced BotID Configuration"
description: "Fine-grained control over BotID detection levels and backend domain configuration"
last_updated: "null"
source: "https://vercel.com/docs/botid/advanced-configuration"
--------------------------------------------------------------------------------

# Advanced BotID Configuration

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Route-by-Route configuration](#route-by-route-configuration)

When you need fine-grained control over BotID's detection levels, you can specify `advancedOptions` to choose between basic and deep analysis modes on a per-route basis. This configuration takes precedence over the project-level BotID settings in your Vercel dashboard.

Important: The `checkLevel` in both client and server configurations must be identical for each protected route. A mismatch between client and server configurations will cause BotID verification to fail, potentially blocking legitimate traffic or allowing bots through. This feature is available in `botid@1.4.5` and above

### [Client-side configuration](#client-side-configuration)

In your client-side protection setup, you can specify the check level for each protected path:

```
initBotId({
  protect: [
    {
      path: '/api/checkout',
      method: 'POST',
      advancedOptions: {
        checkLevel: 'deepAnalysis', // or 'basic'
      },
    },
    {
      path: '/api/contact',
      method: 'POST',
      advancedOptions: {
        checkLevel: 'basic',
      },
    },
  ],
});
```

### [Server-side configuration](#server-side-configuration)

In your server-side endpoint that uses `checkBotId()`, ensure it matches the client-side configuration.

```
export async function POST(request: NextRequest) {
  const verification = await checkBotId({
    advancedOptions: {
      checkLevel: 'deepAnalysis', // Must match client-side config
    },
  });
 
  if (verification.isBot) {
    return NextResponse.json({ error: 'Access denied' }, { status: 403 });
  }
 
  // Your protected logic here
}
```

## [Separate backend domains](#separate-backend-domains)

By default, BotID validates that requests come from the same host that serves the BotID challenge. However, if your application architecture separates your frontend and backend domains (e.g., your app is served from `vercel.com` but your API is on `api.vercel.com` or `vercel-api.com`), you'll need to configure `extraAllowedHosts`.

The `extraAllowedHosts` parameter in `checkBotId()` allows you to specify a list of frontend domains that are permitted to send requests to your backend:

app/api/backend/route.ts

```
export async function POST(request: NextRequest) {
  const verification = await checkBotId({
    advancedOptions: {
      extraAllowedHosts: ['vercel.com', 'app.vercel.com'],
    },
  });
 
  if (verification.isBot) {
    return NextResponse.json({ error: 'Access denied' }, { status: 403 });
  }
 
  // Your protected logic here
}
```

Only add trusted domains to `extraAllowedHosts`. Each domain in this list can send requests that will be validated by BotID, so ensure these are domains you control.

### [When to use `extraAllowedHosts`](#when-to-use-extraallowedhosts)

Use this configuration when:

*   Your frontend is hosted on a different domain than your API (e.g., `myapp.com` → `api.myapp.com`)
*   You have multiple frontend applications that need to access the same protected backend
*   Your architecture uses a separate subdomain for API endpoints

### [Example with advanced options](#example-with-advanced-options)

You can combine `extraAllowedHosts` with other advanced options:

app/api/backend-advanced/route.ts

```
const verification = await checkBotId({
  advancedOptions: {
    checkLevel: 'deepAnalysis',
    extraAllowedHosts: ['app.example.com', 'dashboard.example.com'],
  },
});
```

## [Next.js Pages Router configuration](#next.js-pages-router-configuration)

When using [Pages Router API handlers](/docs/pages/building-your-application/routing/api-routes) in development, pass request headers to `checkBotId()`:

pages/api/endpoint.ts

```
import type { NextApiRequest, NextApiResponse } from 'next';
import { checkBotId } from 'botid/server';
 
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse,
) {
  const result = await checkBotId({
    advancedOptions: {
      headers: req.headers,
    },
  });
 
  if (result.isBot) {
    return res.status(403).json({ error: 'Access denied' });
  }
 
  // Your protected logic here
  res.status(200).json({ success: true });
}
```

Pages Router requires explicit headers in development. In production, headers are extracted automatically.

--------------------------------------------------------------------------------
title: "Form Submissions"
description: "How to properly handle form submissions with BotID protection"
last_updated: "null"
source: "https://vercel.com/docs/botid/form-submissions"
--------------------------------------------------------------------------------

# Form Submissions

Copy page

Ask AI about this page

Last updated August 12, 2025

BotID does not support traditional HTML forms that use the `action` and `method` attributes, such as:

```
<form id="contact-form" method="POST" action="/api/contact">
  <!-- form fields -->
  <button type="submit">Send</button>
</form>
```

Native form submissions don't work with BotID due to how they are handled by the browser.

To ensure the necessary headers are attached, handle the form submission in JavaScript and send the request using `fetch` or `XMLHttpRequest`, allowing BotID to properly verify the request.

## [Enable form submissions to work with BotID](#enable-form-submissions-to-work-with-botid)

Here's how you can refactor your form to work with BotID:

```
async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
  e.preventDefault();
  const formData = new FormData(e.currentTarget);
  const response = await fetch('/api/contact', {
    method: 'POST',
    body: formData,
  });
  const data = await response.json();
  // handle response
}
 
return (
  <form onSubmit={handleSubmit}>
    {/* form fields */}
    <button type="submit">Send</button>
  </form>
);
```

### [Form submissions with Next.js](#form-submissions-with-next.js)

If you're using Next.js, you can [use a server action](https://nextjs.org/docs/app/guides/forms#how-it-works) in your form and use the `checkBotId` function to verify the request:

```
'use server';
import { checkBotId } from 'botid/server';
 
export async function submitContact(formData: FormData) {
  const verification = await checkBotId();
  if (verification.isBot) {
    throw new Error('Access denied');
  }
  // process formData
  return { success: true };
}
```

And in your form component:

```
'use client';
import { submitContact } from '../actions/contact';
 
export default function ContactForm() {
  async function handleAction(formData: FormData) {
    return submitContact(formData);
  }
 
  return (
    <form action={handleAction}>
      {/* form fields */}
      <button type="submit">Send</button>
    </form>
  );
}
```

--------------------------------------------------------------------------------
title: "Get Started with BotID"
description: "Step-by-step guide to setting up BotID protection in your Vercel project"
last_updated: "null"
source: "https://vercel.com/docs/botid/get-started"
--------------------------------------------------------------------------------

# Get Started with BotID

Copy page

Ask AI about this page

Last updated September 24, 2025

This guide shows you how to add BotID protection to your Vercel project. BotID blocks automated bots while allowing real users through, protecting your APIs, forms, and sensitive endpoints from abuse.

The setup involves three main components:

*   Client-side component to run challenges.
*   Server-side verification to classify sessions.
*   Route configuration to ensure requests are routed through BotID.

## [Step by step guide](#step-by-step-guide)

Before setting up BotID, ensure you have a JavaScript [project deployed](/docs/projects/managing-projects#creating-a-project) on Vercel.

1.  ### [Install the package](#install-the-package)
    
    Add BotID to your project:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i botid
    ```
    
2.  ### [Configure redirects](#configure-redirects)
    
    Use the appropriate configuration method for your framework to set up proxy rewrites. This ensures that ad-blockers, third party scripts, and more won't make BotID any less effective.
    
    Next.js (/app)SvelteKitNuxtOther frameworks
    
    next.config.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { withBotId } from 'botid/next/config';
     
    const nextConfig = {
      // Your existing Next.js config
    };
     
    export default withBotId(nextConfig);
    ```
    
3.  ### [Add client-side protection](#add-client-side-protection)
    
    Choose the appropriate method for your framework:
    
    *   Next.js 15.3+: Use `initBotId()` in `instrumentation-client.ts` for optimal performance
    *   Other Next.js: Mount the `<BotIdClient/>` component in your layout `head`
    *   Other frameworks: Call `initBotId()` during application initialization
    
    Next.js 15.3+ (Recommended)
    
    We recommend using `initBotId()` in [`instrumentation-client.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client) for better performance in Next.js 15.3+. For earlier versions, use the React component approach.
    
    Next.js (/app)SvelteKitNuxtOther frameworks
    
    instrumentation-client.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { initBotId } from 'botid/client/core';
     
    // Define the paths that need bot protection.
    // These are paths that are routed to by your app.
    // These can be:
    // - API endpoints (e.g., '/api/checkout')
    // - Server actions invoked from a page (e.g., '/dashboard')
    // - Dynamic routes (e.g., '/api/create/*')
     
    initBotId({
      protect: [
        {
          path: '/api/checkout',
          method: 'POST',
        },
        {
          // Wildcards can be used to expand multiple segments
          // /team/*/activate will match
          // /team/a/activate
          // /team/a/b/activate
          // /team/a/b/c/activate
          // ...
          path: '/team/*/activate',
          method: 'POST',
        },
        {
          // Wildcards can also be used at the end for dynamic routes
          path: '/api/user/*',
          method: 'POST',
        },
      ],
    });
    ```
    
    Next.js < 15.3
    
    Next.js (/app)SvelteKitNuxtOther frameworks
    
    app/layout.tsx
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { BotIdClient } from 'botid/client';
    import { ReactNode } from 'react';
     
    const protectedRoutes = [
      {
        path: '/api/checkout',
        method: 'POST',
      },
    ];
     
    type RootLayoutProps = {
      children: ReactNode;
    };
     
    export default function RootLayout({ children }: RootLayoutProps) {
      return (
        <html lang="en">
          <head>
            <BotIdClient protect={protectedRoutes} />
          </head>
          <body>{children}</body>
        </html>
      );
    }
    ```
    
4.  ### [Perform BotID checks on the server](#perform-botid-checks-on-the-server)
    
    Use `checkBotId()` on the routes configured in the `<BotIdClient/>` component.
    
    Important configuration requirements: - Not adding the protected route to `<BotIdClient />` will result in `checkBotId()` failing. The client side component dictates which requests to attach special headers to for classification purposes. - Local development always returns `isBot: false` unless you configure the `developmentOptions` option on `checkBotId()`. [Learn more about local development behavior](/docs/botid/local-development-behavior).
    
    Using API routes
    
    Next.js (/app)SvelteKitNuxtOther frameworks
    
    app/api/sensitive/route.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { checkBotId } from 'botid/server';
    import { NextRequest, NextResponse } from 'next/server';
     
    export async function POST(request: NextRequest) {
      const verification = await checkBotId();
     
      if (verification.isBot) {
        return NextResponse.json({ error: 'Access denied' }, { status: 403 });
      }
     
      const data = await processUserRequest(request);
     
      return NextResponse.json({ data });
    }
     
    async function processUserRequest(request: NextRequest) {
      // Your business logic here
      const body = await request.json();
      // Process the request...
      return { success: true };
    }
    ```
    
    Using Server Actions
    
    Next.js (/app)SvelteKitNuxtOther frameworks
    
    app/actions/create-user.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    'use server';
     
    import { checkBotId } from 'botid/server';
     
    export async function createUser(formData: FormData) {
      const verification = await checkBotId();
     
      if (verification.isBot) {
        throw new Error('Access denied');
      }
     
      const userData = {
        name: formData.get('name') as string,
        email: formData.get('email') as string,
      };
     
      const user = await saveUser(userData);
      return { success: true, user };
    }
     
    async function saveUser(userData: { name: string; email: string }) {
      // Your database logic here
      console.log('Saving user:', userData);
      return { id: '123', ...userData };
    }
    ```
    
    BotID actively runs JavaScript on page sessions and sends headers to the server. If you test with `curl` or visit a protected route directly, BotID will block you in production. To effectively test, make a `fetch` request from a page in your application to the protected route.
    
5.  ### [Enable BotID deep analysis in Vercel (Recommended)](#enable-botid-deep-analysis-in-vercel-recommended)
    
    BotID Deep Analysis are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans
    
    From the [Vercel dashboard](/dashboard)
    
    *   Select your Project
    *   Click the Firewall tab
    *   Click Configure
    *   Enable Vercel BotID Deep Analysis
    
    [Go to Firewall Configuration](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Fconfigure&title=Open+Firewall+Configuration)

## [Complete examples](#complete-examples)

### [Next.js App Router example](#next.js-app-router-example)

Client-side code for the BotID Next.js implementation:

app/checkout/page.tsx

```
'use client';
 
import { useState } from 'react';
 
export default function CheckoutPage() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
 
  async function handleCheckout(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);
 
    try {
      const formData = new FormData(e.currentTarget);
      const response = await fetch('/api/checkout', {
        method: 'POST',
        body: JSON.stringify({
          product: formData.get('product'),
          quantity: formData.get('quantity'),
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      });
 
      if (!response.ok) {
        throw new Error('Checkout failed');
      }
 
      const data = await response.json();
      setMessage('Checkout successful!');
    } catch (error) {
      setMessage('Checkout failed. Please try again.');
    } finally {
      setLoading(false);
    }
  }
 
  return (
    <form onSubmit={handleCheckout}>
      <input name="product" placeholder="Product ID" required />
      <input name="quantity" type="number" placeholder="Quantity" required />
      <button type="submit" disabled={loading}>
        {loading ? 'Processing...' : 'Checkout'}
      </button>
      {message && <p>{message}</p>}
    </form>
  );
}
```

Server-side code for the BotID Next.js implementation:

app/api/checkout/route.ts

```
import { checkBotId } from 'botid/server';
import { NextRequest, NextResponse } from 'next/server';
 
export async function POST(request: NextRequest) {
  // Check if the request is from a bot
  const verification = await checkBotId();
 
  if (verification.isBot) {
    return NextResponse.json(
      { error: 'Bot detected. Access denied.' },
      { status: 403 },
    );
  }
 
  // Process the legitimate checkout request
  const body = await request.json();
 
  // Your checkout logic here
  const order = await processCheckout(body);
 
  return NextResponse.json({
    success: true,
    orderId: order.id,
  });
}
 
async function processCheckout(data: any) {
  // Implement your checkout logic
  return { id: 'order-123' };
}
```

--------------------------------------------------------------------------------
title: "Local Development Behavior"
description: "How BotID behaves in local development environments and testing options"
last_updated: "null"
source: "https://vercel.com/docs/botid/local-development-behavior"
--------------------------------------------------------------------------------

# Local Development Behavior

Copy page

Ask AI about this page

Last updated September 24, 2025

During local development, BotID behaves differently than in production to facilitate testing and development workflows. In development mode, `checkBotId()` always returns `{ isBot: false }`, allowing all requests to pass through. This ensures your development workflow isn't interrupted by bot protection while building and testing features.

### [Using developmentOptions](#using-developmentoptions)

If you need to test BotID's different return values in local development, you can use the `developmentBypass` option:

app/api/sensitive/route.ts

```
import { checkBotId } from 'botid/server';
import { NextRequest, NextResponse } from 'next/server';
 
export async function POST(request: NextRequest) {
  const verification = await checkBotId({
    developmentOptions: {
      bypass: 'BAD-BOT', // default: 'HUMAN'
    },
  });
 
  if (verification.isBot) {
    return NextResponse.json({ error: 'Access denied' }, { status: 403 });
  }
 
  // Your protected logic here
}
```

The `developmentOptions` option only works in development mode and is ignored in production. In production, BotID always performs real bot detection.

This allows you to:

*   Test your bot handling logic without deploying to production
*   Verify error messages and fallback behaviors
*   Ensure your application correctly handles both human and bot traffic

--------------------------------------------------------------------------------
title: "Handling Verified Bots"
description: "Information about verified bots and their handling in BotID"
last_updated: "null"
source: "https://vercel.com/docs/botid/verified-bots"
--------------------------------------------------------------------------------

# Handling Verified Bots

Copy page

Ask AI about this page

Last updated September 24, 2025

Handling verified bots is available in botid@1.5.0 and above.

BotID allows you to identify and handle [verified bots](/docs/bot-management#verified-bots) differently from regular bots. This feature enables you to permit certain trusted bots (like AI assistants) to access your application while blocking others.

Vercel maintains a directory of known and verified bots across the web at [bots.fyi](https://bots.fyi)

### [Checking for Verified Bots](#checking-for-verified-bots)

When using `checkBotId()`, the response includes fields that help you identify verified bots:

```
import { checkBotId } from "botid/server";
import { NextResponse } from "next/server";
 
export async function POST(request: Request) {
  const botResult = await checkBotId();
 
  const { isBot, verifiedBotName, isVerifiedBot, verifiedBotCategory } = botResult;
 
  // Check if it's ChatGPT Operator
  const isOperator = isVerifiedBot && verifiedBotName === "chatgpt-operator";
 
  if (isBot && !isOperator) {
    return Response.json({ error: "Access denied" }, { status: 403 });
  }
 
  // ... rest of your handler
  return Response.json(botResult);
}
```

### [Verified Bot response fields](#verified-bot-response-fields)

View our directory of verified bot names and categories [here](/docs/bot-management#verified-bots-directory).

The `checkBotId()` function returns the following fields for verified bots:

*   `isVerifiedBot`: Boolean indicating whether the bot is verified
*   `verifiedBotName`: String identifying the specific verified bot
*   `verifiedBotCategory`: String categorizing the type of verified bot

### [Example use cases](#example-use-cases)

Verified bots are useful when you want to:

*   Allow AI assistants to interact with your API while blocking other bots
*   Provide different responses or functionality for verified bots
*   Track usage by specific verified bot services
*   Enable AI-powered features while maintaining security

--------------------------------------------------------------------------------
title: "Build Output API"
description: "The Build Output API is a file-system-based specification for a directory structure that can produce a Vercel deployment."
last_updated: "null"
source: "https://vercel.com/docs/build-output-api"
--------------------------------------------------------------------------------

# Build Output API

Copy page

Ask AI about this page

Last updated July 2, 2025

The Build Output API is a file-system-based specification for a directory structure that can produce a Vercel deployment.

Framework authors can take advantage of [framework-defined infrastructure](/blog/framework-defined-infrastructure) by implementing this directory structure as the output of their build command. This allows the framework to define and use all of the Vercel platform features.

## [Overview](#overview)

The Build Output API closely maps to the Vercel product features in a logical and understandable format.

It is primarily targeted toward authors of web frameworks who would like to utilize all of the Vercel platform features, such as Vercel Functions, Routing, Caching, etc.

If you are a framework author looking to integrate with Vercel, you can use this reference as a way to understand which files the framework should emit to the `.vercel/output` directory.

If you are not using a framework and would like to still take advantage of any of the features that those frameworks provide, you can create the `.vercel/output` directory and populate it according to this specification yourself.

You can find complete examples of Build Output API directories in [vercel/examples](https://github.com/vercel/examples/tree/main/build-output-api).

Check out our blog post on using the [Build Output API to build your own framework](/blog/build-your-own-web-framework) with Vercel.

## [Known limitations](#known-limitations)

Native Dependencies: Please keep in mind that when building locally, your build tools will compile native dependencies targeting your machine’s architecture. This will not necessarily match what runs in production on Vercel.

For projects that depend on native binaries, you should build on a host machine running Linux with a `x64` CPU architecture, ideally the same as the platform [Build Image](/docs/deployments/build-image).

## [More resources](#more-resources)

*   [Configuration](/docs/build-output-api/v3/configuration)
*   [Vercel Primitives](/docs/build-output-api/v3/primitives)
*   [Features](/docs/build-output-api/v3/features)

--------------------------------------------------------------------------------
title: "Build Output Configuration"
description: "Learn about the Build Output Configuration file, which is used to configure the behavior of a Deployment."
last_updated: "null"
source: "https://vercel.com/docs/build-output-api/configuration"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./01-vercel-documentation.md) | [Index](./index.md) | [Next →](./03-build-output-configuration.md)
