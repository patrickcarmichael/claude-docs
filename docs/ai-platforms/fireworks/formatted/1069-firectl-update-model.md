---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## firectl update model

Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-model

Updates a model.
```
firectl update model [flags]
```

### Examples

```
firectl update model my-model --display-name="New Name"
firectl update model accounts/my-account/models/my-model --display-name="New Name"
```

### Flags

```
      --default-draft-model string        The default speculative draft model to use when creating a deployment.
      --default-draft-token-count int32   The default speculative draft token count when creating a deployment.
      --description string                The description of the model.
      --display-name string               The display name of the model.
      --github-url string                 The GitHub URL of the model.
  -h, --help                              help for model
      --hugging-face-url string           The Hugging Face URL of the model.
      --public                            Whether the model is publicly accessible.
      --supports-image-input              Whether the model supports image inputs.
      --supports-tools                    Whether the model supports function calling.
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
