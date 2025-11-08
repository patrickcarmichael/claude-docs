---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl prepare-model

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/prepare-model

Prepare models for different precisions
```
firectl prepare-model [flags]
```

### Examples

```
firectl prepare-model my-model
firectl prepare-model accounts/my-account/models/my-model
```

### Flags

```
  -h, --help                    help for prepare-model
      --wait                    Wait until the model preparation is complete.
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
