---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Monitor progress

print(f"Job ID: {job.id}")
print(f"Status: {job.status}")
```

The custom model should be as close (have similar architecture, similar model sizes and max sequence length) to the base model family as possible. In the example above, `HuggingFaceTB/SmolLM2-1.7B-Instruct` has Llama architecture, and the closest model size and max sequence length.

### Parameter Explanation

| Parameter           | Purpose                                                                              | Example                                                      |
| ------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| `model`             | Specifies the base model family for optimal configuration and inference setup        | `"togethercomputer/llama-2-7b-chat"`, `"meta-llama/Llama-3"` |
| `from_hf_model`     | The Hugging Face repository containing your custom model weights                     | `"username/model-name"`                                      |
| `hf_model_revision` | (Optional) Use only if you need a specific commit hash instead of the latest version | `"abc123def456"`                                             |
| `hf_api_token`      | (Optional) API token for accessing private repositories                              | `"hf_xxxxxxxxxxxx"`                                          |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
