---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multimodal PDF search

Handling PDF files, which often contain a mix of text, images, and layout information, presents a challenge for traditional embedding methods. This usually requires a multimodal generative model to pre-process the documents into a format that is suitable for the embedding model. This intermediate text representations can lose critical information; for example, the structure and precise content of tables or complex layouts might not be accurately rendered

Embed v4 solves this problem as it is designed to natively understand mixed-modality inputs. Embed v4 can directly process the PDF content, including text and images, in a single step. It generates a unified embedding that captures the semantic meaning derived from both the textual and visual elements.

Here's an example of how to use the Embed endpoint to perform multimodal PDF search.

First, import the required libraries.
```python PYTHON
from pdf2image import convert_from_path
from io import BytesIO
import base64
import chromadb
import cohere
```
Next, turn a PDF file into a list of images, with one image per page. Then format these images into the content structure expected by the Embed endpoint.
```python PYTHON
pdf_path = "PDF_FILE_PATH"  # https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/guide/embed-v4-pdf-search/data/Samsung_Home_Theatre_HW-N950_ZA_FullManual_02_ENG_180809_2.pdf

pages = convert_from_path(pdf_path, dpi=200)

input_array = []
for page in pages:
    buffer = BytesIO()
    page.save(buffer, format="PNG")
    base64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    base64_image = f"data:image/png;base64,{base64_str}"
    page_entry = {
        "content": [
            {"type": "text", "text": f"{pdf_path}"},
            {"type": "image_url", "image_url": {"url": base64_image}},
        ]
    }
    input_array.append(page_entry)
```
Next, generate the embeddings for these pages and store them in a vector database (in this example, we use Chroma).
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
