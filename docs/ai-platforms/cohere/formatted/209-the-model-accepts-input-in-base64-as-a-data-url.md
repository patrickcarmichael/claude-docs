---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The model accepts input in base64 as a Data URL


def image_to_base64_data_url(image_path):
    # Open the image file

    with Image.open(image_path) as img:
        image_format = img.format.lower()
        buffered = BytesIO()
        img.save(buffered, format=img.format)
        # Encode the image data in base64

        img_base64 = base64.b64encode(buffered.getvalue()).decode(
            "utf-8"
        )

    # Create the Data URL with the inferred image type

    data_url = f"data:image/{image_format};base64,{img_base64}"
    return data_url


base64_url = image_to_base64_data_url("<PATH_TO_IMAGE>")

input = {
    "content": [
        {"type": "image_url", "image_url": {"url": base64_url}}
    ]
}

res = co.embed(
    model="embed-v4.0",
    embedding_types=["float"],
    input_type="search_document",
    inputs=[input],
    output_dimension=1024,
)

res.embeddings.float
```
Here's a code sample using the `images` parameter:
```python PYTHON
import cohere
from PIL import Image
from io import BytesIO
import base64

co = cohere.ClientV2(api_key="YOUR_API_KEY")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
