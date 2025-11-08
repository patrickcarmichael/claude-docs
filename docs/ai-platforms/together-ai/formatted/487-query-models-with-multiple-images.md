---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Query models with multiple images

Currently this model supports **5 images** as input.
```python
  # Multi-modal message with multiple images

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Compare these two images."},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                      },
                  },
              ],
          }
      ],
  )
  print(response.choices[0].message.content)
```

### Output

```typescript
The first image is a collage of multiple identical landscape photos showing a natural scene with rocks, trees, and a stream under a blue sky. The second image is a screenshot of a mobile app interface, specifically the navigation menu of the Canva app, which includes icons for Home, DMs (Direct Messages), Activity, Later, Canvases, and More.

### Comparison:

1. **Content**:
   - The first image focuses on a natural landscape.
   - The second image shows a digital interface from an app.

2. **Purpose**:
   - The first image could be used for showcasing nature, design elements in graphic work, or as a background.
   - The second image represents the functionality and layout of the Canva app's navigation system.

3. **Visual Style**:
   - The first image has vibrant colors and realistic textures typical of outdoor photography.
   - The second image uses flat design icons with a simple color palette suited for user interface design.

4. **Context**:
   - The first image is likely intended for artistic or environmental contexts.
   - The second image is relevant to digital design and app usability discussions.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
