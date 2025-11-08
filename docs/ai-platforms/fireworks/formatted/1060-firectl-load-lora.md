---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl load-lora

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/load-lora

Loads a LoRA model to a deployment.

### Usage

Loads a LoRA model to a deployment. If a deployment is not specified, the model will be loaded to Fireworks' serverless platform (if supported). If a deployment is specified, it will be loaded to the given dedicated deployment. If successful, a DeployedModel resource will be created.
```
firectl load-lora [flags]
```

### Examples

```
firectl load-lora my-lora  # To load it to serverless

firectl load-lora my-lora --deployment abcd1234  # To load it to a dedicated deployment

```

### Flags

```
      --deployment string       The resource ID of the deployment where the LoRA model is to be loaded.
  -h, --help                    help for load-lora
      --public                  If true, the LoRA model will be publicly available for inference.
      --replace-merged-addon    Required when loading an addon to a hot reload deployment. If there is already an existing addon, it will be replaced.
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
