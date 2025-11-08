---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fireworks Benchmark Tool

Use our open-source benchmarking tool to measure and optimize your deployment's performance:

**[Fireworks Benchmark Tool](https://github.com/fw-ai/benchmark)**

This tool allows you to:

* Test throughput and latency under various load conditions
* Simulate production traffic patterns
* Identify performance bottlenecks
* Compare different deployment configurations

### Installation

```bash
git clone https://github.com/fw-ai/benchmark.git
cd benchmark
pip install -r requirements.txt
```

### Basic usage

Run a basic benchmark test:
```bash
python benchmark.py \
  --model "accounts/fireworks/models/llama-v3p1-8b-instruct" \
  --deployment "your-deployment-id" \
  --num-requests 1000 \
  --concurrency 10
```

### Key metrics to monitor

When benchmarking your deployment, focus on these key metrics:

* **Throughput**: Requests per second (RPS) your deployment can handle
* **Latency**: Time to first token (TTFT) and end-to-end response time
* **Token generation rate**: Tokens per second during generation
* **Error rate**: Failed requests under load

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
