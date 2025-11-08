---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Real-World Knowledge Distillation Use Cases

### Common Scenarios Where You Need Teacher Models

**1. Legal Document Analysis**

* **Challenge**: No ground truth for contract clause interpretation
* **Teacher Solution**: Use teacher models to generate expert-level legal analyses

**2. Code Review Automation**

* **Challenge**: No perfect code review comments for your codebase
* **Teacher Solution**: Use teacher models to generate code review insights

**4. Customer Support Chatbot**

* **Challenge**: No ideal responses for company-specific questions
* **Teacher Solution**: Use teacher models for customer service responses

**6. Content Moderation**

* **Challenge**: No labeled decisions for edge-case content
* **Teacher Solution**: Use teacher models to generate moderation reasoning and decisions

### Popular Open Source Teacher Models

* **[Kimi K2](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct)**: Great general purpose model, especially for agentic use cases.
* **[Qwen3 Coder 480B](https://app.fireworks.ai/models/fireworks/qwen3-coder-480b-a35b-instruct)**: Strong coding model, especially for one-off coding tasks.
* **[Qwen3 235B (instruct)](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-instruct-2507)**: Good general purpose model. Has strong world knowledge for tasks like classification.
* **[Qwen3 235B (thinking)](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-thinking-2507)**: Good reasoning model for agentic tasks and tasks that require multi-step planning.
* **[Open AI GPT OSS 120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b)**: OpenAI's open-weight model, with strong reasoning and tool use capabilities. Runs efficiently on single 80GB GPU and achieves near-parity with o4-mini on core reasoning benchmarks.
* **[DeepSeek V3](https://app.fireworks.ai/models/fireworks/deepseek-v3-0324)**: Powerful MoE model with 671B parameters (37B active) that rivals GPT-4o and Claude 3.5 Sonnet. Strong performance in math, coding, and reasoning tasks.
* **[DeepSeek R1](https://app.fireworks.ai/models/fireworks/deepseek-r1-0528)**: Open-source reasoning model that rivals OpenAI o1. Trained using pure reinforcement learning. Shows explicit chain-of-thought reasoning process and excels at complex mathematical and logical problems.

### Uploading Training Data to Fireworks

```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
