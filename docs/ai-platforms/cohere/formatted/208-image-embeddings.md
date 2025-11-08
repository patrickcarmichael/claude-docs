---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Image Embeddings

The Cohere Embedding platform supports image embeddings for `embed-v4.0` and the `embed-v3.0` family. There are two ways to access this functionality:

* Pass `image` to the `input_type` parameter. Here are the steps:
  * Pass image to the `input_type` parameter
  * Pass your image URL to the images parameter
* Pass your image URL to the new `images` parameter. Here are the steps:
  * Pass in a input list of `dicts` with the key content
  * content contains a list of `dicts` with the keys `type` and `image`

When using the `images` parameter the following restrictions exist:

* Pass `image` to the `input_type` parameter (as discussed above).
* Pass your image URL to the new `images` parameter.

Be aware that image embedding has the following restrictions:

* If `input_type='image'`, the `texts` field must be empty.
* The original image file type must be in a `png`, `jpeg`, `webp`, or `gif` format and can be up to 5 MB in size.
* The image must be base64 encoded and sent as a Data URL to the `images` parameter.
* Our API currently does not support batch image embeddings for `embed-v3.0` models. For `embed-v4.0`, however, you can submit up to 96 images.

When using the `inputs` parameter the following restrictions exist (note these restrictions apply to `embed-v4.0`):

* The maximum size of payload is 20mb
* All images larger than 2,458,624 pixels will be downsampled to 2,458,624 pixels
* All images smaller than 3,136 (56x56) pixels will be upsampled to 3,136 pixels
* `input_type` must be set to one of the following
  * `search_query`
  * `search_document`
  * `classification`
  * `clustering`

Here's a code sample using the `inputs` parameter:
```python PYTHON
import cohere
from PIL import Image
from io import BytesIO
import base64

co = cohere.ClientV2(api_key="YOUR_API_KEY")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
