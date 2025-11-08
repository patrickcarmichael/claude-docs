---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## PDF to Text using OCR and `pdf2image`

This method will be required for any PDFs you have that need to be converted to text.

**WARNING**: this process can take a long time without the proper optimizations. We have provided a snippet for your use below, but use at your own risk.

To go from PDF to text with PyTesseract, there is an intermediary step of converting the PDF to an image first, then passing that image into the OCR package, as OCR is usually only available for images.

To do this, we use `pdf2image`, which uses `poppler` behind the scenes to convert the PDF into a PNG. From there, we can pass the image (which is a PIL Image object) directly into the OCR tool.
```python PYTHON
import pytesseract
from pdf2image import convert_from_path

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
