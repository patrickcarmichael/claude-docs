---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl delete dataset

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-dataset

Deletes a dataset.
```
firectl delete dataset [flags]
```

### Examples

```
firectl delete dataset my-dataset
firectl delete dataset accounts/my-account/datasets/my-dataset
```

### Flags

```
  -h, --help                    help for dataset
      --wait                    Wait until the dataset is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
