---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Training Parameters

Core parameters that control how your model learns during the training process.

<AccordionGroup>
  <Accordion title="Learning Rate">
    **What it does**: Controls how aggressively the model updates its weights during each training step. Think of it as the "step size" when descending the loss landscape.

    **Default**: `1e-4` (0.0001)\
    **Valid range**: `1e-5` to `5e-4`

    **How it affects outcome**:

    * **Too high** → Unstable training where reward spikes briefly then collapses as the model overshoots optimal weights.
    * **Too low** → Painfully slow convergence. The reward curve plateaus too early before reaching optimal performance.
    * **Just right** → Steady, consistent reward improvement throughout training.

    **When to adjust**:

    * **Decrease** when you see reward spikes followed by crashes in your training metrics
    * **Increase** when the reward curve plateaus too early and stops improving
    * Keep changes within 2× of the default value
  </Accordion>

  <Accordion title="Epochs">
    **What it does**: The number of complete passes through your training dataset. Each epoch processes every example once.

    **Default**: `1`\
    **Valid range**: `1` to `10` (whole numbers only)

    **How it affects outcome**:

    * **Too few** → The model hasn't had enough exposure to learn patterns from your data
    * **Too many** → Overfitting risk where the model memorizes the training set instead of generalizing
    * **Just right** → Reward curve shows steady improvement and plateaus near the end of training

    **When to adjust**:

    * **Add 1-2 more epochs** if the reward is still climbing steadily at the end of training
    * **Keep at 1** for most tasks—the default works well
    * Watch your reward curves to detect when adding more epochs stops helping
  </Accordion>

  <Accordion title="LoRA Rank">
    **What it does**: Controls the number of trainable parameters in your LoRA adapter. LoRA (Low-Rank Adaptation) adds small adapter layers to the base model rather than training all weights. Higher rank means more capacity to learn new behaviors.

    **Default**: `8`\
    **Valid range**: `4` to `128` (must be powers of 2: 4, 8, 16, 32, 64, 128)

    **How it affects outcome**:

    * **Lower rank (4-8)** → Faster training, less GPU usage, but may lack capacity for complex tasks
    * **Higher rank (32-128)** → More learning capacity, but requires significantly more GPUs and risks overfitting
    * **Just right (8-16)** → Balances capacity and efficiency for most tasks

    **When to adjust**:

    * **Increase** for complex reasoning tasks or when the model struggles to learn desired behaviors
    * **Keep ≤64** unless you have high-end GPUs
    * Consider task complexity: simple style changes need lower rank, complex reasoning needs higher
  </Accordion>

  <Accordion title="Batch Size">
    **What it does**: The amount of data (measured in tokens) processed in each training step before updating model weights.

    >   **📝 Note**
>
> Unlike traditional batch sizes that count sequences (e.g., 32 or 64 sequences), Fireworks RFT uses **token-based batch sizing**. For example, with an 8k max sequence length, a 64k batch size allows up to 8 sequences per batch (64k tokens ÷ 8k tokens/sequence = 8 sequences).

    **Default**: `32k tokens`\
    **Valid range**: Hardware-dependent

    **How it affects outcome**:

    * **Smaller batches** → Noisier gradient updates that may help exploration, but slower training
    * **Larger batches** → Smoother, more stable updates and faster training throughput, but requires more GPU memory
    * **Just right** → Maximizes GPU utilization without running out of memory

    **When to adjust**:

    * **Decrease** when you hit out-of-memory (OOM) errors
    * **Increase** only when GPUs show >30% memory headroom and you want faster training
    * Most users should stick with the default
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
