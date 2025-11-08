---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Limitations

### Image Counts

The Cohere API has the following limitations with respect to image counts:

* You can pass in a maximum of 20 images per request, or 20 megabytes (mb) in total data, whichever comes first.

### File types

These are the supported file types:

* PNG (`.png`)
* JPEG (`.jpeg` and `.jpg`)
* WEBP (`.webp`)
* Non-animated GIF (`.gif`)

### Non-Latin Alphabets

Performance may vary when processing images containing text in non-Latin scripts, like Japanese or Korean characters.

### Text Size

To enhance accuracy, consider enlarging small text in images while ensuring no crucial visual information is lost. If you're expecting small text in images, set `detail='high'`.

A good rule of thumb is: 'if you have trouble reading image in a text, then the model will too.'

### Rate Limits

Image inputs don't change rate limit considerations; for more detail, check out our dedicated [rate limit documentation](https://docs.cohere.com/docs/rate-limits).

### Understanding Costs

To understand how to calculate costs for a model, consult the breakdown above about how *tokens* are determined by the model, then consult our dedicated [pricing page](https://cohere.com/pricing?_gl=1*9o1g49*_gcl_au*MTE3MTc3OTk1OC4xNzUwMjQ1NzE0*_ga*MTAxNTg1NTM1MS4xNjk1MjMwODQw*_ga_CRGS116RZS*czE3NTEyOTcxMDQkbzMyMyRnMSR0MTc1MTI5NzExMiRqNTIkbDAkaDA.) to figure out what your ultimate spend will be.

### Acceptable Use

Please refer to our [usage policy](https://docs.cohere.com/docs/usage-policy).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
