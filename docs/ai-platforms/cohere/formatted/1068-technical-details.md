---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Technical Details

### API Changes:

The Embed API has two major changes:

* Introduced a new `input_type` called `image`
* Introduced a new parameter called `images`

Example request on how to process
```Text cURL
POST https://api.cohere.ai/v1/embed
{
    "model": "embed-multilingual-v3.0",
    "input_type": "image",
    "embedding_types": ["float"],
    "images": [enc_img]
}
```

### Restrictions:

* The API only accepts images in the base format of the following: `png`, `jpeg`,`Webp`, and `gif`
* Image embeddings currently does not support batching so the max images sent per request is 1
* The maximum image sizez is `5mb`
* The `images` parameter only accepts a base64 encoded image formatted as a Data Url


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
