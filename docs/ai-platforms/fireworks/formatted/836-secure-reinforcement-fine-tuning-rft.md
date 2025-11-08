---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Secure reinforcement fine-tuning (RFT)

Use reinforcement fine-tuning while keeping sensitive components and data under your control. Follow these steps to run secure RFT end to end using your own storage and reward pipeline.

<Steps>
  <Step title="Configure storage (BYOB)">
    Point Fireworks to your storage so you retain governance and apply your own compliance controls.

    * Datasets: [GCS Bucket Integration](#gcs-bucket-integration) (AWS S3 coming soon)
    * Models (optional): [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model)

    <Tip>
      Grant least-privilege IAM to only the bucket/path prefixes needed for training. Use server-side encryption and your KMS policies where required.
    </Tip>
  </Step>

  <Step title="Prepare your reward pipeline and rollouts">
    Keep your reward functions, rollout servers, and training metrics under your control. Generate rewards from your environment and write them to examples in your dataset (or export a dataset that contains per-example rewards).

    * Reward functions and reward models remain proprietary and never need to be shared
    * Rollouts and evaluation infrastructure run in your environment
    * Model checkpoints can be registered to your storage registry if desired
  </Step>

  <Step title="Create a dataset that includes rewards">
    Create or point a `Dataset` at your BYOB storage. Ensure each example contains the information required by your reward pipeline (for example, prompts, outputs/trajectories, and numeric rewards).

    >   **ℹ️ Info**
>
> You can reuse existing supervised data by attaching reward signals produced by your pipeline, or export a fresh dataset into your bucket for consumption by RFT.
  </Step>

  <Step title="Run reinforcement step from Python">
    Use the Python SDK to run reinforcement steps that read from your BYOB dataset and produce a new checkpoint.
```python
    # Assumes you have an authenticated `llm` client and a `dataset` that

    # references your BYOB bucket with per-example rewards.

    import time

    job = llm.reinforcement_step(
        dataset=dataset,                 # Dataset with rewards in your bucket

        output_model="my-improved-model-v1",  # New checkpoint name (must not exist)

        epochs=1,
        learning_rate=1e-5,
        accelerator_count=2,
        accelerator_type="NVIDIA_H100_80GB",
    )

    # Wait for completion

    while not job.is_completed:
        job.raise_if_bad_state()
        time.sleep(1)
        job = job.get()
        if job is None:
            raise RuntimeError("Job was deleted while waiting for completion")

    # The new model is now available at job.output_model

```
    See [`LLM.reinforcement_step()`](/tools-sdks/python-client/sdk-reference#reinforcement-step) and [`ReinforcementStep`](/tools-sdks/python-client/sdk-reference#reinforcementstep) for full parameters and return types.

    >   **📝 Note**
>
> When continuing from a LoRA checkpoint, training parameters such as `lora_rank`, `learning_rate`, `max_context_length`, `epochs`, and `batch_size` must match the original LoRA training.
  </Step>

  <Step title="Verify outputs and enforce controls">
    * Validate the new checkpoint functions as expected in your environment
    * If exporting models to your storage, apply your registry policies and access reviews
    * Review audit logs and rotate any temporary credentials used for the run
  </Step>
</Steps>

>   **⚠️ Warning**
>
> Do not store long-lived credentials in code. Use short-lived tokens, workload identity, or scoped service accounts when granting Fireworks access to your buckets.

<Check>
  You now have an end-to-end secure RFT workflow with BYOB datasets, proprietary reward pipelines, and isolated training jobs that generate new checkpoints.
</Check>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
