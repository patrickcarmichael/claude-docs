---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Technical Architecture

#### **Model Architecture:**

* **MoE Design:** Token-choice Mixture-of-Experts with SwiGLU activations for improved performance
* **Expert Selection:** Softmax-after-topk approach for calculating MoE weights, ensuring optimal expert utilization
* **Attention Mechanism:** RoPE (Rotary Position Embedding) with 128k context length
* **Attention Patterns:** Alternating between full context and sliding 128-token window for efficiency
* **Attention Sink:** Learned attention sink per-head with additional additive value in the softmax denominator

#### **Tokenization:**

* **Standard Compatibility:** Uses the same tokenizer as GPT-4o
* **Broad Support:** Ensures seamless integration with existing applications and tools

#### **Context Handling:**

* **128k Context Window:** Large context capacity for processing extensive documents
* **Efficient Patterns:** Optimized attention patterns for long-context scenarios
* **Memory Optimization:** GPT-OSS Large designed to fit efficiently within 80GB GPU memory


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
