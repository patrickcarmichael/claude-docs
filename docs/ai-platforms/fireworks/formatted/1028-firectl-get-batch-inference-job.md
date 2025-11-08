---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl get batch-inference-job

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-batch-inference-job

Retrieves information about a batch inference job.
```
firectl get batch-inference-job [flags]
```

### Examples

```
firectl get batch-inference-job my-batch-job
firectl get batch-inference-job accounts/my-account/batch-inference-jobs/my-batch-job
```

### Flags

```
  -h, --help   help for batch-inference-job
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
