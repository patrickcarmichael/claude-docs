---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Passing in an Image

### Image URL Formats

Cohere supports images in two formats, base64 *data* URLs and HTTP *image* URLs.

A base64 data URL (e.g., `"data:image/png;base64,..."`) has the advantage of being usable in deployments that don't have access to the internet. Here's what that looks like:

<CodeBlocks>
```python PYTHON
  co.chat(
      model="command-a-vision-07-2025",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "what's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {"url": "data:image..."},
                  },
              ],
          }
      ],
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
                "url": "data:image/png;base64,..."
              }
            }
          ]
        }
      ]
    }'
```
</CodeBlocks>

An HTTP image URL (e.g., "[https://cohere.com/favicon-32x32.png](https://cohere.com/favicon-32x32.png)") is faster, but requires you to upload your image somewhere and is not available in outside platforms (Azure, Bedrock, etc.) HTTP image URLs make the API easy to try out, as data URLs are long and difficult to deal with. Moreover, including long data URLs in the request increases the request size and the corresponding network latency.

Here's what that looks like:

<CodeBlocks>
```python PYTHON
  co.chat(
      model="command-a-vision-07-2025",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "what's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://cohere.com/favicon-32x32.png"
                      },
                  },
              ],
          }
      ],
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
                "url": "https://cohere.com/favicon-32x32.png"
              }
            }
          ]
        }
      ]
    }'
```typescript
</CodeBlocks>

For use cases like chatbots, where the images accumulate in the chat history, we recommend you use HTTP/HTTPs image URLs, since the request size will be smaller, and, with server-side caching, will result in faster response times.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
