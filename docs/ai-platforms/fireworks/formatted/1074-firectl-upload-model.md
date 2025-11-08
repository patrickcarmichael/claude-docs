---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl upload model

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/upload-model

Resumes or completes a model upload.

### Usage

Resumes or completes a model upload for an existing model. This command should be used when a previous upload was interrupted.
```
firectl upload model [flags]
```

### Examples

```
firectl upload model my-model /path/to/checkpoint/
```

### Flags

```
  -h, --help    help for model
      --quiet   If true, does not print the upload progress bar.
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
