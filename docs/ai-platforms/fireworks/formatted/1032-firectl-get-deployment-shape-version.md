---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl get deployment-shape-version

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment-shape-version

Prints information about a deployment shape version.
```
firectl get deployment-shape-version [flags]
```

### Examples

```
firectl get deployment-shape-version accounts/my-account/deploymentShapes/my-deployment-shape/versions/my-version
		firectl get deployment-shape-version accounts/my-account/deploymentShapes/my-deployment-shape/versions/latest
```

### Flags

```
  -h, --help   help for deployment-shape-version
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
