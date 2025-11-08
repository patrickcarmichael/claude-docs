---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Frequently Asked Questions

**Question: How to choose the base model?**

There are three variables to consider:

* Model Architecture
* Model Size
* Maximum Sequence Length

You want to use the model with the same architecture, the closest number of parameters as possible to the base model and the max seq length for the base model should not exceed the maximum length for the external model.

For example, `HuggingFaceTB/SmolLM2-135M-Instruct`. It has Llama architecture, the model size is 135M parameters and the max sequence length is 8k. Looking into the Llama models, Fine-tuning API supports llama2, llama3, llama3.1 and llama3.2 families. The closest model by number of parameters is `meta-llama/Llama-3.2-1B-Instruct`, but the max seq length is 131k, which is much higher than the model can support. It's better to use `togethercomputer/llama-2-7b-chat`, which is larger than the provided model, but the max seq length is not exceeding the model's limits.

**Issue**: "No exact architecture match available"

* **Solution**: Choose the closest architecture family (e.g., treat CodeLlama as Llama)

**Issue**: "All base models are much larger than my custom model"

* **Solution**: Use the smallest available base model; the system will adjust automatically

**Issue**: "Unsure about sequence length limits"

* **Solution**: Check your model's `config.json` for `max_position_embeddings` or use our compatibility checker

***

**Question: Which models are supported?**

Any CausalLM model under 100B parameters that has a corresponding base model in [our official catalog](./fine-tuning-models.mdx). The base model determines the inference configuration. If your checkpoint significantly differs from the base model architecture, you'll receive warnings, but training will proceed.

***

**Question: Can I fine-tune an adapter/LoRA model?**

Yes, you can continue training from an existing adapter model. However, the Fine-tuning API will merge the adapter with the base model during training, resulting in a full checkpoint rather than a separate adapter.

***

**Question: Will my model work with inference?**

Your model will work with inference if:

* The base model you specified is officially supported
* The architecture matches the base model configuration
* Training completed successfully without errors

Models based on unsupported architectures may not function correctly during inference. If you want to run a trained model with unsupported architecture, please submit a support ticket on [the support page](https://support.together.ai/).

***

**Question: Can I load a custom model for dedicated endpoint and train it?**

No, you cannot use uploaded models for training in Fine-tuning API. Models uploaded for inference will not appear in the fine-tunable models. To learn more about what you can do with the uploaded models for dedicated endpoint, see this [page](./custom-models.mdx).

However, you can upload your model to the Hugging Face Hub and use the repo id to train it. The trained model will be available for the inference after the training.

***

**Question: How do I handle private repositories?**

Include your Hugging Face API token with read permissions for those repositories when creating the fine-tuning job:
```python
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="private-org/private-model",
    hf_api_token="hf_xxxxxxxxxxxx",
    training_file="your-file-id",
)
```

***

**Question: What if my model requires custom code?**

Models requiring `trust_remote_code=True` are not currently supported for security reasons. Consider these alternatives:

* Use a similar model that doesn't require custom code
* Contact our support team and request adding the model to our official catalog
* Wait for the architecture to be supported officially

***

**Question: How do I specify a particular model version?**

If you need to use a specific commit hash instead of the latest version, use the `hf_model_revision` parameter:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
