---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl delete batch-inference-job

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-batch-inference-job

Deletes a batch inference job.
```
firectl delete batch-inference-job [flags]
```

### Examples

```
firectl delete batch-inference-job my-batch-job
firectl delete batch-inference-job accounts/my-account/batch-inference-jobs/my-batch-job
```

### Flags

```
  -h, --help                    help for batch-inference-job
      --wait                    Wait until the batch inference job is deleted.
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
