---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl delete model

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-model

Deletes a model.
```
firectl delete model [flags]
```

### Examples

```
firectl delete model my-model
firectl delete model accounts/my-account/models/my-model
```

### Flags

```
  -h, --help   help for model
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
