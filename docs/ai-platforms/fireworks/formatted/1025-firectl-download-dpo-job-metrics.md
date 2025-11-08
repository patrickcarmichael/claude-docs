---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl download dpo-job-metrics

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-dpo-job-metrics

Retrieves metrics for a dpo job.
```
firectl download dpo-job-metrics [flags]
```

### Examples

```
firectl download dpoj-metrics my-dpo-job
firectl download dpoj-metrics accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
      --filename string   The file name to export to. (default "metrics.jsonl")
  -h, --help              help for dpo-job-metrics
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
