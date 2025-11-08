---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implementation Details

### Mode-Specific Requirements

* **Local Mode**: Requires either `func` or `func_path`.
* **Remote Mode**: Requires either `endpoint` or `name`.
* **Fireworks Hosted Mode**: Requires `model_id`.

### Function Loading

When providing a `func_path`, the path can be specified in two formats:

* `module.path:function_name` - Module with colon separator (preferred)
* `module.path.function_name` - Module with function as last component

### Authentication

For remote and Fireworks-hosted modes, the authentication token is retrieved from the `FIREWORKS_API_KEY` environment variable.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
