---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Captioning

Instead of asking about specific questions, we can also get the model to provide a description of an image as a whole, be it detailed descriptions or simple captions.

This can be particularly useful for creating alt text for accessibility, generating descriptions for image databases, social media content creation, and others.
```python PYTHON
image_path = "image4.jpg"
render_image(image_path)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image4.jpg" />
```python PYTHON
message = "Describe this image in detail."

generate_text(image_path, message)
```
```mdx wordWrap
In the heart of a vibrant amusement park, a magnificent and whimsical dragon sculpture emerges from the water, its scales shimmering in hues of red, green, and gold. The dragon's head, adorned with sharp teeth and piercing yellow eyes, rises above the surface, while its body coils gracefully beneath the waves. Surrounding the dragon are colorful LEGO-like structures, including a bridge with intricate blue and purple patterns and a tower that reaches towards the sky. The water, a striking shade of turquoise, is contained by a wooden fence, and beyond the fence, lush green trees provide a natural backdrop. The scene is set against a cloudy sky, adding a touch of drama to this fantastical display.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
