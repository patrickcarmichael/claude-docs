---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Option 1: Fine-tune your LoRA model and run inference on it on Together

The Together API supports both LoRA and full fine-tuning. For serverless LoRA inference, follow these steps:

**Step 1: Fine-Tune with LoRA on Together API:** To start a Fine-tuning job with LoRA, follow the detailed instructions in the [Fine-Tuning Overview,](/docs/fine-tuning-overview) or follow the below snippets as a quick start:
```bash
  together files upload "your-datafile.jsonl"
```
```python
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  resp = client.files.upload(file="your-datafile.jsonl")

  print(resp.model_dump())
```
```bash
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --lora
```
```python
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.fine_tuning.create(
      training_file=file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      lora=True,
  )

  print(response)
```

If you plan to use a validation set, make sure to set the `--validation-file` and `--n-evals` (the number of evaluations over the entire job) parameters. `--n-evals` needs to be set as a number above 0 in order for your validation set to be used.

**Step 2: Run LoRA Inference**:

Once you submit the fine-tuning job you should be able to see the model name in the response:
```json
  {
    "id": "ft-44129430-ac08-4136-9774-aed81e0164a4",
    "training_file": "file-629e58b4-ff73-438c-b2cc-f69542b27980",
    "validation_file": "",
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    "output_name": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    ...
  }
```

You can also see the status of the job and get the model name if you navigate to your fine-tuned model in the 'Model' or 'Jobs' tab in the Together dashboard. You'll see a model string – use it through the Together API.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7e332c714e184d6d4d9554b761a6e350" alt="" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cc3d85962dac161d2842617ce37f0b45 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2081ba31e7cb4fa4d9cacb96d4a08976 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=db9915d04970709baaa0ee97c53d3235 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a051712d1d8408ba70701d81dc41aef3 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6677dee05d46a3641aa28021bb3ddcf5 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7a83d855bf5a9d4dd8f4fc26497cdb19 2500w" />
</Frame>
```bash
  MODEL_NAME_FOR_INFERENCE="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a"

  curl -X POST https://api.together.xyz/v1/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "messages": [
        {
          "role": "user",
          "content": "debate the pros and cons of AI",
        },
      ],
      "max_tokens": 128
    }'
```
```python
  import os
  from together import Together

  client = Together(api_key=TOGETHERAI_API_KEY)

  user_prompt = "debate the pros and cons of AI"

  response = client.chat.completions.create(
      model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
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
    model: 'zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a',
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

Expected Response:
```json
  {
    "id": "8f2cb236c80ea20e-YYZ",
    "object": "text.completion",
    "created": 1734331375,
    "model": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    "prompt": [],
    "choices": [
      {
        "text": "Here's a debate on the pros and cons of AI:\n\n**Moderator:** Welcome to today's debate on the pros and cons of AI. We have two debaters, Alex and Ben, who will present their arguments on the topic. Alex will argue in favor of AI, while Ben will argue against it. Let's begin with opening statements.\n\n**Alex (In Favor of AI):** Thank you, Moderator. AI has revolutionized the way we live and work. It has improved efficiency, productivity, and accuracy in various industries, such as healthcare, finance, and transportation. AI-powered systems can analyze vast amounts of data, identify",
        "finish_reason": "length",
        "seed": 5626645655383684000,
        "logprobs": null,
        "index": 0
      }
    ],
    "usage": {
      "prompt_tokens": 18,
      "completion_tokens": 128,
      "total_tokens": 146,
      "cache_hit_rate": 0
    }
  }
```

Your first couple queries may have slow TTFT (up to 10 seconds) but subsequent queries should be fast!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
