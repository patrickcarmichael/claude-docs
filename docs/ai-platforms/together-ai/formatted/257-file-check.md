---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## File Check

To confirm that your dataset has the right format, run the following command. This step is optional, but we highly recommend to run this step before uploading the file and using it for fine-tuning.
```text
together files check PATH_TO_DATA_FILE
```

Here's the output:
```bash
together files check joke_explanations.jsonl
{
    "is_check_passed": true,
    "message": "Checks passed",
    "found": true,
    "file_size": 781041,
    "utf8": true,
    "line_type": true,
    "text_field": true,
    "key_value": true,
    "min_samples": true,
    "num_samples": 238,
    "load_json": true,
    "filetype": "jsonl"
}
```

After your data is prepared, upload your file using either [CLI](/reference/finetune) or [Python SDK](https://github.com/togethercomputer/together-python).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
