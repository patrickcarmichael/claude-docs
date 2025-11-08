---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing and Billing

### How can I estimate my fine-tuning job cost?

To estimate the cost of your fine-tuning job:

1. Calculate approximate training tokens: `context_length × batch_size × steps × epochs`
2. Add validation tokens: `validation_dataset_size × evaluation_frequency`
3. Multiply the total tokens by the per-token rate for your chosen model size, fine-tuning type, and implementation method

### Fine-Tuning Pricing

Fine-tuning pricing is based on the total number of tokens processed during your job, including training and validation. Cost varies by model size, fine-tuning type (Supervised Fine-tuning or DPO), and implementation method (LoRA or Full Fine-tuning).

The total cost is calculated as: `total_tokens_processed × per_token_rate`

Where `total_tokens_processed = (n_epochs × n_tokens_per_training_dataset) + (n_evals × n_tokens_per_validation_dataset)`

For current rates, refer to our [fine-tuning pricing page](https://together.ai/pricing).

The exact token count and final price are available after tokenization completes, shown in your [jobs dashboard](https://api.together.xyz/jobs) or via `together fine-tuning retrieve $JOB_ID`.

### Dedicated Endpoint Charges for Fine-Tuned Models

After fine-tuning, hosting charges apply for dedicated endpoints (per minute, even when not in use). These are separate from job costs and continue until you stop the endpoint.

To avoid unexpected charges:

* Monitor active endpoints in the [models dashboard](https://api.together.xyz/models)
* Stop unused endpoints
* Review hosting rates on the [pricing page](https://together.ai/pricing)

### Understanding Refunds When Canceling Fine-Tuning Jobs

When you cancel a running fine-tuning job, you're charged only for completed steps (hardware resources used). Refunds apply only for uncompleted steps.

To check progress: Use `client.fine_tuning.retrieve("your-job-id").total_steps` (replace with your job ID).

For billing questions, contact support with your job ID.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
