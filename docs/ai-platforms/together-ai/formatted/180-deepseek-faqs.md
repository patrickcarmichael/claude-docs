---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## DeepSeek FAQs

Source: https://docs.together.ai/docs/deepseek-faqs


### How can I access DeepSeek R1 and V3?

Together AI hosts DeepSeek R1 and V3 models on Serverless. Find them in our playground: [DeepSeek R1](https://api.together.xyz/models/deepseek-ai/DeepSeek-R1) / [DeepSeek V3](https://api.together.xyz/models/deepseek-ai/DeepSeek-V3).

### Why is R1 more expensive than V3 if they share the same architecture and are the same size?

R1 produces more tokens in the form of long reasoning chains, which significantly increase memory and compute requirements per query. Each user request locks more of the GPU for a longer period, limiting the number of simultaneous requests the hardware can handle and leading to higher per-query costs compared to V3.

### Have you changed the DeepSeek model in any way? Is it quantized, distilled or modified?

* No quantization – Full-precision versions are hosted.
* No distillation — we do offer distilled models but as separate endpoints (e.g. `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`)
* No modifications — no forced system prompt or censorship.

### Do you send data to China or DeepSeek?

No. We host DeepSeek models on secure, private (North America-based) data centers. DeepSeek does not have access to user's requests or API calls. We provide full opt-out privacy controls for our users. Learn more about our privacy policy [here](https://www.together.ai/privacy).

### Can I deploy DeepSeek in Dedicated Endpoints? What speed and costs can I expect?

We recently launched [Together Reasoning Clusters](https://www.together.ai/blog/deploy-deepseek-r1-at-scale-fast-secure-serverless-apis-and-large-scale-together-reasoning-clusters), which allows users to get dedicated, high-performance compute built for large-scale, low-latency inference.

Together Reasoning Clusters include:

✅ Speeds up to 110 tokens/sec with no rate limits or resource sharing\
✅ Custom optimizations fine-tuned for your traffic profile\
✅ Predictable pricing for cost-effective scaling\
✅ Enterprise SLAs with 99.9% uptime\
✅ Secure deployments with full control over your data

Looking to deploy DeepSeek-R1 in production? [Contact us](https://www.together.ai/deploy-deepseek-r1-production?utm_source=website\&utm_medium=blog-post\&utm_campaign=deepseek-r1-reasoning-clusters)!

### What are the rate limits for DeepSeek R1?

Due to high demand, DeepSeek R1 has model specific rate limits that are based on load. For Free and Tier 1 users the rate limits can range from 0.3 RPM to 4 RPM at this time. Billing tiers 2-5 have a rate limit ranging from 240 RPM to 480 RPM. [Contact sales](https://www.together.ai/deploy-deepseek-r1-production?utm_source=website\&utm_medium=blog-post\&utm_campaign=deepseek-r1-reasoning-clusters) if you need higher limits for BT 5/Enterprise/Scale.

### How do I enable thinking mode for DeepSeek V3.1?

DeepSeek V3.1 is a "Hybrid" model. To enable reasoning response generations, you need to pass `reasoning={"enabled": True}` in your request.

Example:
```python
from together import Together

client = Together()

stream = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.1",
    messages=[
        {"role": "user", "content": "What is the most expensive sandwich?"}
    ],
    reasoning={"enabled": True},
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta

    # Show reasoning tokens if present

    if hasattr(delta, "reasoning") and delta.reasoning:
        print(delta.reasoning, end="", flush=True)

    # Show content tokens if present

    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)
```

Note: For this model, function calling only works in non-reasoning mode (`reasoning={"enabled": False}`).

***


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
