---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Update

Update an existing endpoint by listing the changes followed by the endpoint ID.

You can find the endpoint ID by listing your dedicated endpoints.

### Usage

```sh
together endpoints update [OPTIONS] ENDPOINT_ID
```

### Example

```sh
together endpoints update --min-replicas 2 --max-replicas 4 endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

Note: Both `--min-replicas` and `--max-replicas` must be specified together

| Options                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| `--display-name` - TEXT    | A new human-readable name for the endpoint    |
| `--min-replicas` - INTEGER | New minimum number of replicas to maintain    |
| `--max-replicas` - INTEGER | New maximum number of replicas to scale up to |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
