---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Steps

1. extract\_pdf() function extracts text data from the PDF using [unstructured](https://unstructured.io/) package. You can use other packages like PyPDF2 as well.
2. This extracted text is added to the prompt so the model can "see" the document.
3. The agent summarizes the document and passes that information to convert\_to\_json() function. This function makes another call to command model to convert the summary to json output. This separation of tasks is useful when the text document is complicated and long. Therefore, we first distill the information and ask another model to convert the text into json object. This is useful so each model or agent focuses on its own task without suffering from long context.
4. Then the json object goes through a check to make sure all keys are present and gets saved as a csv file. When the document is too long or the task is too complex, the model may fail to extract all information. These checks are then very useful because they give feedback to the model so it can adjust it's parameters to retry.
```python PYTHON
import os

import cohere
import pandas as pd
import json
from unstructured.partition.pdf import partition_pdf
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
