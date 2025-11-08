---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Question answering

One of the more common use cases is question answering. Here, the model is used to answer questions based on the content of an image.

By providing an image and a relevant question, the model can analyze the visual content and generate a text response. This is particularly useful in scenarios where visual context is important, such as identifying objects, understanding scenes, or providing descriptions.
```python PYTHON
image_path = "image1.jpg"
render_image(image_path)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image1.jpg" />
```python PYTHON
message = "Where is this art style from and what is this dish typically used for?"
generate_text(image_path, message)
```
```mdx wordWrap
The art style on this dish is typical of traditional Moroccan or North African pottery. It's characterized by intricate geometric patterns, bold colors, and a mix of stylized floral and abstract designs.

This type of dish is often used as a spice container or for serving small portions of food. In Moroccan cuisine, similar dishes are commonly used to hold spices like cumin, cinnamon, or paprika, or to serve condiments and appetizers.

The design and craftsmanship suggest this piece is likely handmade, which is a common practice in Moroccan pottery. The vibrant colors and detailed patterns make it not just a functional item but also a decorative piece that adds to the aesthetic of a dining table or kitchen.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
