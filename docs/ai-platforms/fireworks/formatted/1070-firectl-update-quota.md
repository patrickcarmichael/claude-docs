---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl update quota

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-quota

Updates a quota.
```
firectl update quota [flags]
```

### Examples

```
firectl update quota serverless-inference-rpm --value 300
```

### Flags

```
  -h, --help        help for quota
      --value int   The quota allowed to be used by this account. Must be less than max_value.
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
