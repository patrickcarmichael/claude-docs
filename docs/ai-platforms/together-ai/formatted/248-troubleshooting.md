---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

**Understanding Training Stages**

Your fine-tuning job progresses through several stages. Understanding these helps you identify where issues might occur:

1. **Data Download**: The system downloads your model weights from Hugging Face and your training data from Together
2. **Initialization**: Model is loaded onto GPUs and the data pipeline is prepared for training
3. **Training**: The actual fine-tuning occurs based on your specified hyperparameters
4. **Saving**: The trained model is saved to temporary storage
5. **Upload**: The final model is moved to permanent storage for inference availability

**Common Errors and Solutions**

Due to the number of diverse model families hosted on the Hugging Face Hub, understanding these error types helps you quickly resolve issues:

* **Internal Errors**: Training failed due to an internal problem with the Fine-tuning API. Our team gets automatically notified and usually starts investigating the issue shortly after it occurs. If this persists for long periods of time, please contact support with your job ID.
* **CUDA OOM (Out of Memory) Errors**: Training failed because it exceeded available GPU memory. To resolve this, reduce the `batch_size` parameter or consider using a smaller model variant.
* **Value Errors and Assertions**: Training failed due to a checkpoint validation error. These typically occur when model hyperparameters are incompatible or when the model architecture doesn't match expectations. Check that your model is actually CausalLM and that all parameters are within valid ranges.
* **Runtime Errors**: Training failed due to computational exceptions raised by PyTorch. These often indicate issues with model weights or tensor operations. Verify that your model checkpoint is complete and uncorrupted.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
