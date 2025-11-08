---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Comparing multiple images

This section demonstrates how to analyze and compare multiple images simultaneously. The API allows passing more than one image in a single call, enabling the model to perform comparative analysis between different visual inputs.
```python PYTHON
image_path1 = "image6.jpg"
image_path2 = "image7.jpg"
render_image(image_path1)
render_image(image_path2)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image6.jpg" />

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image7.jpg" />
```python PYTHON
message = "Compare these two dishes."

with open(image_path1, "rb") as img_file1:
    base64_image_url1 = f"data:image/jpeg;base64,{base64.b64encode(img_file1.read()).decode('utf-8')}"

with open(image_path2, "rb") as img_file2:
    base64_image_url2 = f"data:image/jpeg;base64,{base64.b64encode(img_file2.read()).decode('utf-8')}"

response = co.chat(
    model=model,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": message},
                {"type": "image_url", "image_url": {"url": base64_image_url1}},
                {"type": "image_url", "image_url": {"url":base64_image_url2}}
            ],
        }
    ],
)

print(response.message.content[0].text)
```
```mdx wordWrap
The first dish is a Japanese-style bento box containing a variety of items such as sushi rolls, tempura shrimp, grilled salmon, rice, and vegetables. It is served in a clear plastic container with individual compartments for each food item. The second dish is a Turkish-style meal featuring baklava, a sweet pastry made with layers of phyllo dough, nuts, and honey. It is accompanied by a small bowl of cream and a red flag with a gold emblem. The baklava is presented on a black plate, while the bento box is placed on a tray with a red and gold napkin. Both dishes offer a unique culinary experience, with the Japanese bento box providing a balanced meal with a mix of proteins, carbohydrates, and vegetables, and the Turkish baklava offering a rich, sweet dessert.
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
