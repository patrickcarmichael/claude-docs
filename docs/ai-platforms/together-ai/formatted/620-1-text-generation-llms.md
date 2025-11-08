---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Text Generation - LLMs

### a. Chat Completion with Hugging Face Hub library

```py
  from huggingface_hub import InferenceClient

  # Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key (HF or custom)

  )

  # Define the chat messages

  messages = [{"role": "user", "content": "What is the capital of France?"}]

  # Generate a chat completion

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=messages,
      max_tokens=500,
  )

  # Print the response

  print(completion.choices[0].message)
```
```js
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const chatCompletion = await client.chatCompletion({
      model: "deepseek-ai/DeepSeek-R1",  // Replace with your desired model
      messages: [
          {
              role: "user",
              content: "What is the capital of France?"
          }
      ],
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });

  // Log the response
  console.log(chatCompletion.choices[0].message);
```

You can swap this for any compatible LLM from Together AI, here’s a handy [URL](https://huggingface.co/models?inference_provider=together\&other=text-generation-inference\&sort=trending) to find the list.

### b. OpenAI client library

You can also call inference providers via the [OpenAI python client](https://github.com/openai/openai-python). You will need to specify the `base_url` and `model` parameters in the client and call respectively.

The easiest way is to go to [a model’s page](https://huggingface.co/deepseek-ai/DeepSeek-R1?inference_api=true\&inference_provider=together\&language=python) on the hub and copy the snippet.
```py
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/together",
    api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxx",  # together or Hugging Face api key

)

messages = [{"role": "user", "content": "What is the capital of France?"}]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=messages,
    max_tokens=500,
)

print(completion.choices[0].message)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
