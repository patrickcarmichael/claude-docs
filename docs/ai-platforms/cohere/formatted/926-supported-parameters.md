---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supported parameters

The following is the list supported parameters in the Compatibility API, including those that are not explicitly demonstrated in the examples above:

### Chat completions

* `model`
* `messages`
* `stream`
* `reasoning_effort` (Only "none" and "high" are currently supported.)
* `response_format`
* `tools`
* `temperature`
* `max_tokens`
* `stop`
* `seed`
* `top_p`
* `frequency_penalty`
* `presence_penalty`

<Warning title="Note">
  Currently, only **`none`** and **`high`** are supported for `reasoning_effort`.\
  These correspond to enabling or disabling `thinking` in the Cohere Chat API.\
  Passing **`medium`** or **`low`** is **not supported** at this time.
</Warning>

### Embeddings

* `input`
* `model`
* `encoding_format`

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
