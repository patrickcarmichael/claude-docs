---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl unload-lora

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/unload-lora

Unloads a LoRA model from a deployment.

### Usage

Unloads a LoRA model from a deployment. If a deployment is not specified, the model will be unloaded from the Fireworks serverless platform. If a deployment is specified, it will be unloaded to the given dedicated deployment.
```
firectl unload-lora [flags]
```

### Examples

```
firectl unload-lora my-lora  # To unload it from serverless

firectl unload-lora my-lora --deployment abcd1234  # To unload it from a dedicated deployment

```

### Flags

```
      --deployment string       The resource name of the deployment where the model is to be undeployed.
  -h, --help                    help for unload-lora
      --wait                    Wait until the model is deployed.
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
