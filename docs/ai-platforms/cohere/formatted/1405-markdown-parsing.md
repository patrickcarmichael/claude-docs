---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Markdown parsing

filename = "llamaparse-markdown-parsed-fda-approved-drug.txt"
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

### Solution 5: pdf2image + pytesseract [\[Back to Solutions\]](#top) \[#pdf2image]

The final parsing method we examine does not rely on cloud services, but rather relies on two libraries: `pdf2image`, and `pytesseract`. `pytesseract` lets you perform OCR locally on images, but not PDF files. So, we first convert our PDF into a set of images via `pdf2image`.

#### Parsing the document

```python PYTHON
from matplotlib import pyplot as plt
from pdf2image import convert_from_path
import pytesseract
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
