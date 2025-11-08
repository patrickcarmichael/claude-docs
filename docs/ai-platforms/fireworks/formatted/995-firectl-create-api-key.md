---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl create api-key

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-api-key

Creates an API key for the signed in user or a specified service account user.
```
firectl create api-key [flags]
```

### Examples

```
firectl create api-key
firectl create api-key --service-account=my-service-account
firectl create api-key --key-name="Production Key" --service-account=ci-bot
firectl create api-key --key-name="Temporary Key" --expire-time="2025-12-31 23:59:59"
```

### Flags

```
      --expire-time string       If specified, the time at which the API key will automatically expire. Specified in YYYY-MM-DD[ HH:MM:SS] format.
  -h, --help                     help for api-key
      --key-name string          The name of the key to be created. Defaults to "default"
      --service-account string   Admin only: Create API key for the specified service account user
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
