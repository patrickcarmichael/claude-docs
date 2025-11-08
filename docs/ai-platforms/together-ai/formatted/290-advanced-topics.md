---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced Topics

**Continuing a Fine-tuning Job**

You can continue training from a previous fine-tuning job:
```python
  response = client.fine_tuning.create(
      training_file="your-new-training-file-id",
      from_checkpoint="previous-finetune-job-id",
      wandb_api_key="your-wandb-api-key",
  )
```
```bash
  together fine-tuning create \
    --training-file "your-new-training-file-id" \
    --from-checkpoint "previous-finetune-job-id" \
    --wandb-api-key $WANDB_API_KEY
```

You can specify a checkpoint by using:

* The output model name from the previous job
* Fine-tuning job ID
* A specific checkpoint step with the format `ft-...:{STEP_NUM}`

To check all available checkpoints for a job, use:
```bash
together fine-tuning list-checkpoints {FT_JOB_ID}
```

### Continued Fine-tuning jobs and LoRA Serverless Inference

Continued Fine-tuning supports various training method combinations: you can train an adapter module on top of a fully trained model or continue training an existing adapter from a previous job. Therefore, LoRA Serverless can be enabled or disabled after training is completed.
If you continue a LoRA fine-tuning job with the same LoRA hyperparameters (rank, alpha, selected modules), the trained model will be available for LoRA Serverless. However, if you change any of these parameters or continue with Full training, LoRA Serverless will be disabled. Additionally, if you continue a Full fine-tuning job, LoRA Serverless will remain disabled.
\*Note: The feature is disabled when parameters change because the Fine-tuning API merges the parent fine-tuning adapter to the base model when it detects different adapter hyperparameters, ensuring optimal training quality.

**Training and Validation Split**

To split your dataset into training and validation sets:
```bash
split_ratio=0.9  # Specify the split ratio for your training set

total_lines=$(wc -l < "your-datafile.jsonl")
split_lines=$((total_lines * split_ratio))

head -n $split_lines "your-datafile.jsonl" > "your-datafile-train.jsonl"
tail -n +$((split_lines + 1)) "your-datafile.jsonl" > "your-datafile-validation.jsonl"
```

**Using a Validation Set During Training**

A validation set is a held-out dataset to evaluate your model performance during training on unseen data. Using a validation set provides multiple benefits such as monitoring for overfitting and helping with hyperparameter tuning.

To use a validation set, provide `validation_file` and set `n_evals` to a number above 0:
```python
response = client.fine_tuning.create(
    training_file="your-training-file-id",
    validation_file="your-validation-file-id",
    n_evals=10,  # Number of evaluations over the entire job

    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
)
```

At set intervals during training, the model will be evaluated on your validation set, and the evaluation loss will be recorded in your job event log. If you provide a W\&B API key, you'll also be able to see these losses in the W\&B dashboard.

**Recap**

Fine-tuning LLMs with Together AI allows you to create specialized models tailored to your specific requirements. By following this guide, you've learned how to:

1. Prepare and format your data for fine-tuning
2. Launch a fine-tuning job with appropriate parameters
3. Monitor the progress of your fine-tuning job
4. Use your fine-tuned model via API or dedicated endpoints
5. Evaluate your model's performance improvements
6. Work with advanced features like continued training and validation sets


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
