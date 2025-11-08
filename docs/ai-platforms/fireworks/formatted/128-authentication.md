---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Authentication

All requests made to the Fireworks AI REST API must include an `Authorization` header with a valid `Bearer` token using your API key, along with the `Content-Type: application/json` header.

### Getting your API key

You can obtain an API key by:

* Using the [`firectl create api-key`](/tools-sdks/firectl/commands/create-api-key) command
* Generating one through the [Fireworks AI dashboard](https://app.fireworks.ai/settings/users/api-keys)

### Request headers

Include the following headers in your REST API requests:
```json
authorization: Bearer <API_KEY>
content-type: application/json
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
