---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use Llama 4 Models

```python
  from together import Together

  client = Together()  # API key via api_key param or TOGETHER_API_KEY env var

  # Query image with Llama 4 Maverick model

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What can you see in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  import Together from "together-ai";

  const together = new Together();  // API key via apiKey param or TOGETHER_API_KEY env var

  async function main() {
   const response = await together.chat.completions.create({
     model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
     messages: [{
       role: "user",
       content: [
         { type: "text", text: "What can you see in this image?" },
         { type: "image_url", image_url: { url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png" }}
       ]
     }]
   });

   console.log(response.choices[0].message.content);
  }

  main();
```

### Output

```
The image depicts a serene landscape of Yosemite National Park, featuring a river flowing through a valley surrounded by towering cliffs and lush greenery.

*   **River:**
    *   The river is calm and peaceful, with clear water that reflects the surrounding scenery.
    *   It flows gently from the bottom-left corner to the center-right of the image.
    *   The riverbank is lined with rocks and grasses, adding to the natural beauty of the scene.
*   **Cliffs:**
    *   The cliffs are massive and imposing, rising steeply from the valley floor.
    *   They are composed of light-colored rock, possibly granite, and feature vertical striations.
    *   The cliffs are covered in trees and shrubs, which adds to their rugged charm.
*   **Trees and Vegetation:**
    *   The valley is densely forested, with tall trees growing along the riverbanks and on the cliffsides.
    *   The trees are a mix of evergreen and deciduous species, with some displaying vibrant green foliage.
    *   Grasses and shrubs grow in the foreground, adding texture and color to the scene.
*   **Sky:**
    *   The sky is a brilliant blue, with only a few white clouds scattered across it.
    *   The sun appears to be shining from the right side of the image, casting a warm glow over the scene.

In summary, the image presents a breathtaking view of Yosemite National Park, showcasing the natural beauty of the valley and its surroundings. The calm river, towering cliffs, and lush vegetation all contribute to a sense of serenity and wonder.
```

>   **ℹ️ Info**
>
> ### Llama4 Notebook

  If you'd like to see common use-cases in code see our [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Getting_started_with_Llama4.ipynb) .

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
