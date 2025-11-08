---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Image Detail

The Chat API allows users to control the level of image `“detail”` sent to the model, which can be one of `“low”`, `“high”`, or `“auto”` (the default).

Lower detail helps reduce the overall token count (and therefore price and latency), but may result in poorer performance. We recommend trying both levels of detail to identify whether the performance is sufficient at `"low"`.

The `detail` property is specified for each image, here's what that look like:

<CodeBlocks>
```python PYTHON 
  co.chat(
    model="command-a-vision-07-2025",
    messages=[
  	{ "role": "user", "content": [
              {"type": "text",
                "text": "what's in this image?"
                },
              {"type": "image_url",
              "image_url": {
                "url": "https://cohere.com/favicon-32x32.png",
                "detail": "high" # Here's where we're setting the detail.

            }
          },
        ]
      }
    ]
  )
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-vision-07-2025",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "what'\''s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://cohere.com/favicon-32x32.png",
                "detail": "high"
              }
            }
          ]
        }
      ]
    }'
```
</CodeBlocks>

When detail is set to “low”:

* If the image area is larger than 512px \* 512px, it will be resized to fit into these dimensions while attempting to maintain the aspect ratio.
* Each “low” detail image takes up 256 tokens that count towards the model’s context length.

When detail is set to “high”:

* If the image area is larger than 1536px \* 2048px it will be resized to fit into these dimensions while attempting to maintain the aspect ratio, so that it can be cached.
* Under the hood, the API will divide the image into one or more tiles of 512x512 pixels, plus one additional 512x512 pixel *preview* tile; each of these tiles takes up 256 tokens that count towards the model’s context length.

When detail is unspecified or is set to “auto”:

* If any of the image sides are larger than 768px then `high` detail will be used, otherwise detail will be set to `low`.

Here's an example calculation of how an image is processed into tokens:

* Suppose a user provides a 10,000px \* 20,000px image.
* This image would be resized down to 1024px \* 2048px (since the longest side has to be at most 2048 pixels long), which fits into eight tiles of 512x512.
* What ultimately gets sent to the model is one 512px \* 512px preview thumbnail in addition to eight tiles of 512px \* 512px. Since the thumbnail is 256 tokens, and each of the eight tiles is 256 tokens, that means the image will take up 9 x 256 = 2304 tokens.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
