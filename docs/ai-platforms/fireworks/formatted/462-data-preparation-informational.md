---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data Preparation (Informational)

The example typically uses a pre-generated sample of prompts from the `codeparrot/apps` dataset. The default run configuration (`run_eval.yaml`) references `apps_full_prompts`, which points to `development/CODING_DATASET.jsonl`.

If you wished to regenerate this sample or create a different one (this is for informational purposes, not required to run the example with defaults):

1. The script `scripts/convert_apps_to_prompts.py` can convert the raw Hugging Face `codeparrot/apps` dataset into the JSONL format expected by the pipeline.
2. The source dataset configuration for raw APPS data is defined in `conf/dataset/apps_source.yaml`.
3. An example command to generate 5 samples from the 'test' split:
```bash
   python scripts/convert_apps_to_prompts.py \
       --dataset_name codeparrot/apps \
       --split test \
       --output_file development/apps_sample_prompts.jsonl \
       --max_samples 5 \
       --id_column problem_id \
       --query_column question \
       --ground_truth_column input_output
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
