---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction

Models with vision capabilities can understand and interpret image data, map relationships between text and visual inputs, and handle many other tasks where a mix of images and text is involved.

Cohere has models capable of interacting with images, and they excel in enterprise use cases such as:

* Analysis of charts, graphs, and diagrams;
* Extracting and understanding in-image tables;
* Document optical character recognition (OCR) and question answering;
* Natural-language image processing, including translation of text found in images.

For more detailed breakdowns of these and other applications, check out [our cookbooks](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/guides/vision).

These models are designed to work through an interface and API structure that looks almost exactly like all of our other Command models, making it easy to get started with our image-processing functionality. Take this image, for example, which contains a graph of earnings for various waste management companies:

![](file:2c21b1a8-b4cf-4665-a006-49611d6e1468)

We can have Command A Vision analyze this image for us with the following:

<CodeBlocks>
```python PYTHON 
  response = co.chat(
      model="command-a-vision-07-2025",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Please create two markdown tables. One for Revenue. One for CAGR. the company names should be in alphabetical order in both."},
                  {"type": "image_url", "image_url": {"url": base64_url}},
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
              "text": "Please create two markdown tables. One for Revenue. One for CAGR. the company names should be in alphabetical order in both."
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

And you should get something like this:

![](file:184e07eb-b941-4c39-a4fe-be587e48a1e1)

The rest of this document fleshes out Cohere's models work with image inputs, including information on limitations, token calculations, and more.

>   **⚠️ Warning**
>
> Cohere's Vision capabilities are not currently offered on the North platform.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
