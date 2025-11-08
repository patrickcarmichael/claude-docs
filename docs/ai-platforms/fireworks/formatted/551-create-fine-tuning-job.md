---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create fine-tuning job

job = base_llm.create_supervised_fine_tuning_job(
    display_name="kd-sft-job",
    dataset_or_id=dataset.id,
    epochs=3,
    learning_rate=1e-5
)

job.wait_for_completion()
```

### Deploying the Fine-Tuned Model

```python
sft_llm = LLM(
    model=job.output_model,
    deployment_type="on-demand",
    id="kd-sft-model",
    min_replica_count=0,
    max_replica_count=1
)
sft_llm.apply()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
