---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get Started \[#start]

You'll need a Cohere API key to run this notebook. If you don't have a key, head to [https://cohere.com/](https://cohere.com/) to generate your key.
```python PYTHON
!pip install cohere datasets --quiet
```
```python PYTHON
import json
import random
import re
from typing import List, Optional

import cohere
from getpass import getpass
from datasets import load_dataset
import pandas as pd

co_api_key = getpass("Enter your Cohere API key: ")
co_model = "command-r"
co = cohere.Client(api_key=co_api_key)
```
As test data, we'll use transcripts from the [QMSum dataset](https://github.com/Yale-LILY/QMSum). Note that in addition to the transcripts, this dataset also contains reference summaries -- we will use only the transcripts as our approach is reference-free.
```python PYTHON
qmsum = load_dataset("MocktaiLEngineer/qmsum-processed", split="validation")
transcripts = [x for x in qmsum["meeting_transcript"] if x is not None]
```
```txt title="Output"
Generating train split:   0%|          | 0/1095 [00:00<?, ? examples/s]


Generating validation split:   0%|          | 0/237 [00:00<?, ? examples/s]


Generating test split:   0%|          | 0/244 [00:00<?, ? examples/s]
```javascript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
