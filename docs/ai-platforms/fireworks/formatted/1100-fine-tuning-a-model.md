---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fine-tuning a model

You can fine-tune a model by creating a `Dataset` object and then calling the `.create_supervised_fine_tuning_job()` method on the `LLM` object.
```python main.py theme={null}
from fireworks import Dataset, LLM

dataset = Dataset.from_file("my-dataset.jsonl")

base_model = LLM(model="qwen2p5-7b-instruct", id="my-base-deployment-id", deployment_type="on-demand")

job = base_model.create_supervised_fine_tuning_job(
    "my-fine-tuning-job",
    dataset,
)
job.wait_for_completion()
fine_tuned_model=job.output_llm
```
Datasets are files in JSONL format, where each line represents a complete JSON-formatted training example following the Chat Completions API format. See [fine-tuning a model](../../fine-tuning/fine-tuning-models#step-2%3A-prepare-the-dataset) for an example. Once you have training examples prepared, you can create a `Dataset` object and upload the dataset to Fireworks by using `from_file()`, `from_string()`, or `from_list()`, and pass it to the `.create_supervised_fine_tuning_job()` method on the `LLM` object as we did above.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
