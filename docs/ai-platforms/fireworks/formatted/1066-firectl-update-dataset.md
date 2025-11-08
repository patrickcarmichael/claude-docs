---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl update dataset

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-dataset

Updates a dataset.
```
firectl update dataset [flags]
```

### Examples

```
firectl update dataset my-dataset
firectl update dataset accounts/my-account/datasets/my-dataset
```

### Flags

```
      --display-name string   The display name of the dataset.
  -h, --help                  help for dataset
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
