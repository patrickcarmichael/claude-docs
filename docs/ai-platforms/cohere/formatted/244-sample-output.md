---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample Output

Below is a sample of what the output would look like if you passed in a `jpeg` with original dimensions of `1080x1350` with a standard bit-depth of 24.
```json JSON
{
    "id": "d8f2b461-79a4-44ee-82e4-be601bbb07be",
    "embeddings": {
        "float_": [[-0.025604248, 0.0154418945, ...]],
        "int8": null,
        "uint8": null,
        "binary": null,
        "ubinary": null,
    },
    "texts": [],
    "meta": {
        "api_version": {"version": "2", "is_deprecated": null, "is_experimental": null},
        "billed_units": {
            "input_tokens": null,
            "output_tokens": null,
            "search_units": null,
            "classifications": null,
            "images": 1,
        },
        "tokens": null,
        "warnings": null,
    },
    "images": [{"width": 1080, "height": 1080, "format": "jpeg", "bit_depth": 24}],
    "response_type": "embeddings_by_type",
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
