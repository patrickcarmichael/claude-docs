---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Download the evaluator and dataset

Run this Python script to download two files from the Eval Protocol repository into a folder on your machine called `gsm8k_artifacts/`.

* **Test script** (`test_pytest_math_example.py`): Defines how to evaluate math answers
* **Sample dataset** (`gsm8k_sample.jsonl`): Contains example math problems to test on
```python tutorial/download_gsm8k_assets.py theme={null}
from pathlib import Path
import requests

ARTIFACT_ROOT = Path("gsm8k_artifacts")
TEST_PATH = ARTIFACT_ROOT / "tests" / "pytest" / "gsm8k" / "test_pytest_math_example.py"
DATASET_PATH = ARTIFACT_ROOT / "development" / "gsm8k_sample.jsonl"

files_to_download = {
    TEST_PATH: "https://raw.githubusercontent.com/eval-protocol/python-sdk/main/tests/pytest/gsm8k/test_pytest_math_example.py",
    DATASET_PATH: "https://raw.githubusercontent.com/eval-protocol/python-sdk/main/development/gsm8k_sample.jsonl",
}

for local_path, url in files_to_download.items():
    local_path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    local_path.write_bytes(response.content)
    print(f"Saved {url} -> {local_path}")
```
Expected output:
```
Saved https://raw.githubusercontent.com/.../test_pytest_math_example.py -> gsm8k_artifacts/tests/pytest/gsm8k/test_pytest_math_example.py
Saved https://raw.githubusercontent.com/.../gsm8k_sample.jsonl -> gsm8k_artifacts/development/gsm8k_sample.jsonl
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
