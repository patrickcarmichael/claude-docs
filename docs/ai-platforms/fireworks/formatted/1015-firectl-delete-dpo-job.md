---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl delete dpo-job

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-dpo-job

Deletes a dpo job.
```
firectl delete dpo-job [flags]
```

### Examples

```
firectl delete dpo-job my-dpo-job
firectl delete dpo-job accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
  -h, --help                    help for dpo-job
      --wait                    Wait until the dpo job is deleted.
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
