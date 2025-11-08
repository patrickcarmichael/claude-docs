---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Choose Your Model

Select from Together AI's powerful model selection:

### Recommended Models for Coding

**For General Development:**

* `deepseek-ai/DeepSeek-V3` - Excellent balance of performance and cost (\$1.25/M tokens)
* `meta-llama/Llama-3.3-70B-Instruct-Turbo` - Fast and cost-effective (\$0.88/M tokens)

**For Advanced Coding Tasks:**

* `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` - Specialized for complex coding (\$2.00/M tokens)
* `deepseek-ai/DeepSeek-R1` - Advanced reasoning capabilities ($3.00-$7.00/M tokens)

### Example Configuration

```bash
export OPENAI_API_KEY="your_together_api_key"
export OPENAI_BASE_URL="https://api.together.xyz/v1"
export OPENAI_MODEL="deepseek-ai/DeepSeek-V3"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
