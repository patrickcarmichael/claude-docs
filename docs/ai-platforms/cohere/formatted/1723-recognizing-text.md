---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Recognizing text

The model can recognize and extract text from images, which is useful for reading signs, documents, or other text-based content in photographs. This capability enables applications that can answer questions about text content.
```python PYTHON
image_path = "image5.jpg"
render_image(image_path)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image5.jpg" />
```python PYTHON
message = "How many bread rolls do I get?"

generate_text(image_path, message)
```
```mdx wordWrap
You get 6 bread rolls in the pack.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
