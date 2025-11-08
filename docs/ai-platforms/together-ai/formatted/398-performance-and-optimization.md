---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Performance and Optimization

### What kind of latency can I expect for inference requests?

Latency depends on the model and prompt length. Smaller models like Mistral may respond in less than 1 second, while larger MoE models like Mixtral may take several seconds. Prompt caching and streaming can help reduce perceived latency.

### Is Together suitable for high-throughput workloads?

Yes. Together supports production-scale inference. For high-throughput applications (e.g., over 100 RPS), [contact](https://www.together.ai/contact) the Together team for dedicated support and infrastructure.

### Does Together support streaming responses?

Yes. You can receive streamed tokens by setting `"stream": true` in your request. This allows you to begin processing output as soon as it is generated.

### Can I use quantized models for faster inference?

Yes. Together hosts some models with quantized weights (e.g., FP8, FP16, INT4) for faster and more memory-efficient inference. Support varies by model.

### Can I cache prompts or use speculative decoding?

Yes. Together supports optimizations like prompt caching and speculative decoding for models that allow it, reducing latency and improving throughput.

### Can I run batched or parallel inference requests?

Yes. Together supports batching and high-concurrency usage. You can send parallel requests from your client and take advantage of backend batching. See [Batch Inference](https://docs.together.ai/docs/batch-inference#batch-inference) for more details.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
