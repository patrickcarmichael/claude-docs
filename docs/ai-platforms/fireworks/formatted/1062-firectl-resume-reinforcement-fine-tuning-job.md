---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl resume reinforcement-fine-tuning-job

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/resume-reinforcement-fine-tuning-job

Resumes a failed reinforcement fine-tuning job.
```
firectl resume reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl resume reinforcement-fine-tuning-job my-rftj
firectl resume reinforcement-fine-tuning-job accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for reinforcement-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
