---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

The Together Fine-Tuning Platform now supports training custom models beyond our official model catalog. If you've found a promising model on Hugging Face Hub, whether it's a community model, a specialized variant, or your own previous experiment, you can now fine-tune it using our service.

**Why Use This Feature?**

* **Leverage specialized models**: Use domain-specific or task-optimized models as your starting point
* **Continue previous work**: Resume training from your own checkpoints or experiments
* **Access community innovations**: Fine-tune cutting-edge models not yet in our official catalog

**Key Concept: Base Model + Custom Model**

Understanding BYOM requires grasping our **dual-model approach**:

* **Base Model** (`model` parameter): A model from Together's official catalog that provides the infrastructure configuration, training settings, and inference setup
* **Custom Model** (`from_hf_model` parameter): Your actual HuggingFace model that gets fine-tuned

**Think of it this way**: The base model acts as a "template" that tells our system how to optimally train and serve your custom model. Your custom model should have a similar architecture, size, and sequence length to the base model for best results.

**Example**:
```python
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model (training template)

    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Your custom model

    training_file="file-id-from-upload",
)
```

In this example, we use Llama-2-7B as the base model template because SmolLM2 has Llama architecture and similar characteristics.

**How It Works**

Simply provide a Hugging Face repository URL, and our API will:

1. Load your model checkpoint
2. Apply your fine-tuning data
3. Make the trained model available through our inference endpoints

### Prerequisites

Before you begin, ensure your model meets these requirements:

**Model Architecture**

* **Supported type**: CausalLM models only (models designed for text generation tasks)
* **Size limit**: A maximum of 100 billion parameters
* **Framework version**: Compatible with Transformers library v4.55 or earlier

**Technical Requirements**

* Model weights must be in the `.safetensors` format for security and efficiency
* The model configuration must not require custom code execution (no `trust_remote_code`)
* The repository must be publicly accessible, or you must provide an API token that has access to the private repository

**What You'll Need**

* The Hugging Face repository URL containing your model
* (Optional) The Hugging Face API token for accessing private repositories
* Your training data prepared according to [one of our standard formats](./fine-tuning-data-preparation.mdx)
* Your training hyperparameters for the fine-tuning job

### Compatibility Check

Before starting your fine-tuning job, validate that your model meets our requirements:

1. **Architecture Check**: Visit your model's HuggingFace page and verify it's a "text-generation" or "causal-lm" model
2. **Size Check**: Look for parameter count in model card (should be ≤100B)
3. **Format Check**: Verify model files include `.safetensors` format
4. **Code Check**: Ensure the model doesn't require `trust_remote_code=True`

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
