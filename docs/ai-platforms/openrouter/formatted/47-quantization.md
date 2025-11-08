---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quantization

Quantization reduces model size and computational requirements while aiming to preserve performance. Most LLMs today use FP16 or BF16 for training and inference, cutting memory requirements in half compared to FP32. Some optimizations use FP8 or quantization to reduce size further (e.g., INT8, INT4).

| Field           | Type      | Default | Description                                                                                     |
| --------------- | --------- | ------- | ----------------------------------------------------------------------------------------------- |
| `quantizations` | string\[] | -       | List of quantization levels to filter by (e.g. `["int4", "int8"]`). [Learn more](#quantization) |

>   **⚠️ Warning**
>
> Quantized models may exhibit degraded performance for certain prompts,
  depending on the method used.

Providers can support various quantization levels for open-weight models.

### Quantization Levels

By default, requests are load-balanced across all available providers, ordered by price. To filter providers by quantization level, specify the `quantizations` field in the `provider` parameter with the following values:

* `int4`: Integer (4 bit)
* `int8`: Integer (8 bit)
* `fp4`: Floating point (4 bit)
* `fp6`: Floating point (6 bit)
* `fp8`: Floating point (8 bit)
* `fp16`: Floating point (16 bit)
* `bf16`: Brain floating point (16 bit)
* `fp32`: Floating point (32 bit)
* `unknown`: Unknown

### Example: Requesting FP8 Quantization

Here's an example that will only use providers that support FP8 quantization:
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const completion = await openRouter.chat.send({
    model: 'meta-llama/llama-3.1-8b-instruct',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      quantizations: ['fp8'],
    },
    stream: false,
  });
```
```typescript title="TypeScript (fetch)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer <OPENROUTER_API_KEY>',
      'HTTP-Referer': '<YOUR_SITE_URL>',
      'X-Title': '<YOUR_SITE_NAME>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'meta-llama/llama-3.1-8b-instruct',
      messages: [{ role: 'user', content: 'Hello' }],
      provider: {
        quantizations: ['fp8'],
      },
    }),
  });
```
```python title="Python"
  import requests

  headers = {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>',
    'Content-Type': 'application/json',
  }

  response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
    'model': 'meta-llama/llama-3.1-8b-instruct',
    'messages': [{ 'role': 'user', 'content': 'Hello' }],
    'provider': {
      'quantizations': ['fp8'],
    },
  })
```

### Max Price

To filter providers by price, specify the `max_price` field in the `provider` parameter with a JSON object specifying the highest provider pricing you will accept.

For example, the value `{"prompt": 1, "completion": 2}` will route to any provider with a price of `<= $1/m` prompt tokens, and `<= $2/m` completion tokens or less.

Some providers support per request pricing, in which case you can use the `request` attribute of max\_price. Lastly, `image` is also available, which specifies the max price per image you will accept.

Practically, this field is often combined with a provider `sort` to express, for example, "Use the provider with the highest throughput, as long as it doesn't cost more than `$x/m` tokens."

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
