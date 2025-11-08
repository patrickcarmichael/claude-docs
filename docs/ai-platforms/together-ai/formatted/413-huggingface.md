---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## HuggingFace

*You can use Together AI models with Hugging Face Inference.*

Install the `huggingface_hub` library:
```bash
  pip install huggingface_hub>=0.29.0
```
```bash
  npm install @huggingface/inference
```

Chat Completion with Hugging Face Hub library
```python
  from huggingface_hub import InferenceClient

  ## Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key (HF or custom)

  )

  ## Define the chat messages

  messages = [{"role": "user", "content": "What is the capital of France?"}]

  ## Generate a chat completion

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=messages,
      max_tokens=500,
  )

  ## Print the response

  print(completion.choices[0].message)
```
```typescript
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

Learn more in our [Together AI - HuggingFace Guide](https://docs.together.ai/docs/quickstart-using-hugging-face-inference).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
