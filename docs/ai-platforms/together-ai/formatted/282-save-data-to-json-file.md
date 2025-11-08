---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Save data to JSON file

train_messages.to_json("coqa_prepared_train.jsonl")
```

**Loss Masking**

In some cases, you may want to fine-tune a model to focus on predicting only a specific part of the prompt:

1. When using Conversational or Instruction Data Formats, you can specify `train_on_inputs` (bool or 'auto') - whether to mask the user messages in conversational data or prompts in instruction data.
2. For Conversational format, you can mask specific messages by assigning weights.
3. With pre-tokenized datasets (Parquet), you can provide custom `labels` to mask specific tokens by setting their label to `-100`.

**Checking and Uploading Your Data**

Once your data is prepared, verify it's correctly formatted and upload it to Together AI:
```python
  ## Using Python

  from together import Together
  import os
  import json

  TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
  WANDB_API_KEY = os.getenv(
      "WANDB_API_KEY"
  )  # Optional, for logging fine-tuning to wandb

  ## Check the file format

  from together.utils import check_file

  client = Together(api_key=TOGETHER_API_KEY)

  sft_report = check_file("coqa_prepared_train.jsonl")
  print(json.dumps(sft_report, indent=2))

  assert sft_report["is_check_passed"] == True

  ## Upload the data to Together

  train_file_resp = client.files.upload("coqa_prepared_train.jsonl", check=True)
  print(train_file_resp.id)  # Save this ID for starting your fine-tuning job

```
```bash
  ## Using CLI

  together files check "coqa_prepared_train.jsonl"
  together files upload "coqa_prepared_train.jsonl"
```

The output from checking the file should look similar to:
```json
{
  "is_check_passed": true,
  "message": "Checks passed",
  "found": true,
  "file_size": 23777505,
  "utf8": true,
  "line_type": true,
  "text_field": true,
  "key_value": true,
  "has_min_samples": true,
  "num_samples": 7199,
  "load_json": true,
  "filetype": "jsonl"
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
