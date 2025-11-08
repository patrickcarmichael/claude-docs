---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Option A: CLI with Eval Protocol

Placeholder: Complete guide to launching via command line

### Step 1: Install Eval Protocol CLI

Placeholder: Installation instructions
```bash
pip install eval-protocol
```

### Step 2: Authenticate

Placeholder: How to set up API credentials

### Step 3: Upload Evaluator

Placeholder: Command to upload your evaluator
```bash
eval-protocol upload --entry "module::function"
```
**Example**: Placeholder: Concrete example with real module name

### Step 4: Create RFT Job

Placeholder: Full command with all options explained
```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --dataset-id DATASET_ID \
  --evaluator-id EVALUATOR_ID \
  --output-model my-finetuned-model \
  --epochs 1 \
  --learning-rate 1e-4 \
  --inference-temperature 0.7 \
  --inference-n 4
```

### Step 5: Verify Job Created

Placeholder: How to check job status
```bash
eval-protocol list rft
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
