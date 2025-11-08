---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Image Generation

> This feature is still marked as experimental with Vercel SDK

To generate images with Together AI models using the Vercel AI SDK, use the `.image()` factory method. For more on image generation with the AI SDK see [generateImage()](/docs/reference/ai-sdk-core/generate-image).
```js
import { createTogetherAI } from '@ai-sdk/togetherai';
import { experimental_generateImage as generateImage } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { images } = await generateImage({
  model: togetherai.image('black-forest-labs/FLUX.1-dev'),
  prompt: 'A delighted resplendent quetzal mid flight amidst raindrops',
});

// The images array contains base64-encoded image data by default
```
You can pass optional provider-specific request parameters using the `providerOptions` argument.
```js
import { createTogetherAI } from '@ai-sdk/togetherai';
import { experimental_generateImage as generateImage } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { images } = await generateImage({
  model: togetherai.image('black-forest-labs/FLUX.1-dev'),
  prompt: 'A delighted resplendent quetzal mid flight amidst raindrops',
  size: '512x512',
  // Optional additional provider-specific request parameters
  providerOptions: {
    togetherai: {
      steps: 40,
    },
  },
});
```
Together.ai image models support various image dimensions that vary by model. Common sizes include 512x512, 768x768, and 1024x1024, with some models supporting up to 1792x1792. The default size is 1024x1024.

Available Models:

* `black-forest-labs/FLUX.1-schnell-Free` (free)
* `black-forest-labs/FLUX.1-schnell` (Turbo)
* `black-forest-labs/FLUX.1-dev`
* `black-forest-labs/FLUX.1.1-pro`
* `black-forest-labs/FLUX.1-kontext-pro`
* `black-forest-labs/FLUX.1-kontext-max`
* `black-forest-labs/FLUX.1-kontext-dev`
* `black-forest-labs/FLUX.1-krea-dev`

Please see the [Together.ai models page](https://docs.together.ai/docs/serverless-models#image-models) for a full list of available image models and their capabilities.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
