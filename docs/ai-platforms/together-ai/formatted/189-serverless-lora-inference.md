---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Serverless LoRA Inference

If you fine-tuned the model using parameter efficient LoRA fine-tuning you can select the model in the models dashbaord and can click `OPEN IN PLAYGROUND` to quickly test the fine-tuned model.

You can also call the model directly just like any other model on the Together AI platform, by providing the unique fine-tuned model `output_name` that you can find for the specific model on the dashboard. See the list of models that [support LoRA Inference](/docs/lora-inference#supported-base-models).
```bash
  MODEL_NAME_FOR_INFERENCE="[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17" #from Model page or Fine-tuning page

  curl -X POST https://api.together.xyz/v1/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "messages": [
        {
          "role": "user",
          "content": "What are some fun things to do in New York?",
        },
      ],
      "max_tokens": 128
    }'
```
```python
  import os
  from together import Together

  client = Together()

  user_prompt = "debate the pros and cons of AI"

  response = client.chat.completions.create(
      model="[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17",
      messages=[
          {
              "role": "user",
              "content": user_prompt,
          }
      ],
      max_tokens=512,
      temperature=0.7,
  )

  print(response.choices[0].message.content)
```
```typescript
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: '[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17',
    messages: [
      { role: 'user', content: '"ebate the pros and cons of AI' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
```

You can even upload LoRA adapters from HuggingFace or an s3 bucket. Read more about Serverless LoRA Inference [here](/docs/lora-inference) .

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
