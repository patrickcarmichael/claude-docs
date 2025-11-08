---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How Can I Get Access to the Aya Models?

If you want to test Aya, you have three options. First (and simplest), you can use the [Cohere playground](https://dashboard.cohere.com/playground/chat) or [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/aya_expanse) to play around with them and see what they’re capable of.

Second, you can use the [Cohere Chat API](https://docs.cohere.com/v2/docs/chat-api) to work with Aya programmatically. Here’s a very lightweight example of using the Cohere SDK to get Aya Vision to describe the contents of an image; if you haven’t installed the Cohere SDK, you can do that with `pip install cohere`.
```python PYTHON
import cohere
import base64
import os


def generate_text(image_path, message):

    model = "c4ai-aya-vision-8b"

    co = cohere.ClientV2("<YOUR_API_KEY>")

    with open(image_path, "rb") as img_file:
        base64_image_url = f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

    response = co.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": message},
                    {
                        "type": "image_url",
                        "image_url": {"url": base64_image_url},
                    },
                ],
            }
        ],
        temperature=0.3,
    )

    print(response.message.content[0].text)
```
Here's an image we might feed to Aya Vision:
![A guitar-focused room](file:dd6335bc-6df3-4e61-bac4-8de24be66d8a)

And here’s an example output we might get when we run `generate_text(image_path, "What items are in the wall of this room?")`

(remember: these models are stochastic, and what you see might look quite different).
```
The wall in this room showcases a collection of musical instruments and related items, creating a unique and personalized atmosphere. Here's a breakdown of the items featured:

1. **Guitar Wall Mount**: The centerpiece of the wall is a collection of guitars mounted on a wall. There are three main guitars visible:
   - A blue electric guitar with a distinctive design.
   - An acoustic guitar with a turquoise color and a unique shape.
   - A red electric guitar with a sleek design.

2. **Ukulele Display**: Above the guitars, there is a display featuring a ukulele and its case. The ukulele has a traditional wooden body and a colorful design.

3. **Artwork and Posters**:
   - A framed poster or artwork depicting a scene from *The Matrix*, featuring the iconic green pill and red pill.
   - A framed picture or album artwork of *Fleetwood Mac McDonald*, including *Rumours*, *Tusk*, and *Dreams*.
   - A framed image of the *Dark Side of the Moon* album cover by Pink Floyd.
   - A framed poster or artwork of *Star Wars* featuring *R2-D2* (Robotic Man).

4. **Album Collection**: Along the floor, there is a collection of vinyl records or album artwork displayed on a carpeted area. Some notable albums include:
   - *Dark Side of the Moon* by Pink Floyd.
   - *The Beatles* (White Album).
   - *Abbey Road* by The Beatles.
   - *Nevermind* by Nirvana.

5. **Lighting and Accessories**:
   - A blue lamp with a distinctive design, possibly serving as a floor lamp.
   - A small table lamp with a warm-toned shade.
```
Finally, you can directly download the raw models for research purposes because Cohere Labs has released Aya Vision as open-weight models, through HuggingFace. We also released a new valuable evaluation set -- [Aya Vision Benchmark](https://huggingface.co/datasets/CohereForAI/AyaVisionBench) -- to measure progress on multilingual models here.

### Aya Expanse Integration with WhatsApp.

On our [Aya Expanse](https://docs.cohere.com/docs/aya) page, you can find more information about Aya models in general, including a detailed FAQ section on how to use it with WhatsApp. There, we walk through using Aya Vision with WhatsApp.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
