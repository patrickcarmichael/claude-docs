---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Text-to-Image Generation

```py
  from huggingface_hub import InferenceClient

  # Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",  # Replace with together's provider name

      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key

  )

  # Generate an image from text

  image = client.text_to_image(
      "Bob Marley in the style of a painting by Johannes Vermeer",
      model="black-forest-labs/FLUX.1-schnell",  # Replace with your desired model

  )

  # `image` is a PIL.Image object

  image.show()
```
```js
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const generatedImage = await client.textToImage({
      model: "black-forest-labs/FLUX.1-schnell",  // Replace with your desired model
      inputs: "Bob Marley in the style of a painting by Johannes Vermeer",
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });
```

Similar to LLMs, you can use any compatible Text to Image model from the [list here](https://huggingface.co/models?inference_provider=together\&pipeline_tag=text-to-image\&sort=trending).

You can search for all [Together AI models](https://huggingface.co/models?inference_provider=together\&sort=trending) on the hub and directly try out the available models via the Model Page widget too.

We’ll continue to increase the number of models and ways to try it out!


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
