---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Classification

Classification allows the model to categorize images into predefined classes or labels. This is useful for organizing visual content, filtering images, or extracting structured information from visual data.
```python PYTHON
image_path1 = "image6.jpg"
image_path2 = "image7.jpg"
render_image(image_path1)
render_image(image_path2)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image6.jpg" />

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image7.jpg" />
```python PYTHON
message = "Please classify this image as one of these dish types: japanese, malaysian, turkish, or other.Respond in the following format: dish_type: <the_dish_type>."

images = [
    image_path1, # turkish

    image_path2, # japanese

]

for item in images:
    generate_text(item, message)
    print("-" * 30)
```
```mdx wordWrap
dish_type: turkish
------------------------------
dish_type: japanese
------------------------------
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
