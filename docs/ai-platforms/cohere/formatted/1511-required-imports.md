---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## required imports

from getpass import getpass
import os
import re
import numpy as np
from llama_index.core import SimpleDirectoryReader
from llama_index.core.llama_dataset import download_llama_dataset, LabelledRagDataset
from openai import Client
from mistralai.client import MistralClient
```
For Response evaluation, we will use an LLM as a judge.
Any LLM can be used for this goal, but because evaluation is a very challenging task, we recommend using powerful LLMs, possibly as an ensemble of models. In [previous work](https://arxiv.org/pdf/2303.16634.pdf), it has been shown that models tend to assign higher scores to their own output. Since we generated the answers in this notebook using `command-r`, we will not use it for evaluation. We will provide two alternatives, `gpt-4` and `mistral`. We set `gpt-4` as the default model because, as mentioned above, evaluation is challenging, and `gpt-4` is powerful enough to efficiently perform the task.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
