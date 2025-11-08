---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

First, install the Cohere Python SDK and create a client.
```python PYTHON
%pip install cohere -q
```
```python PYTHON
import cohere
import base64

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key here: https://dashboard.cohere.com/api-keys

```
Next, let's set up a function to generate text responses, given an image and a message. It uses the Cohere API via the Chat endpoint to call the Aya Vision model.

To pass an image to the API, pass a Base64-encoded image as the `image_url` argument in the `messages` parameter. To convert and image into a Base64-encoded version, we can use the `base64` library as in this example.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
