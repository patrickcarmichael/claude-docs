---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create

Create a new dedicated inference endpoint.

### Usage

```sh
together endpoints create [MODEL] [GPU] [OPTIONS]
```

### Example

```sh
together endpoints create \
--model mistralai/Mixtral-8x7B-Instruct-v0.1 \
--gpu h100 \
--gpu-count 2 \
--display-name "My Endpoint" \
--wait
```

### Options

| Options                                             | Description                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------- |
| `--model`- TEXT                                     | (required) The model to deploy                                   |
| `--gpu` \[ h100 \| a100 \| l40 \| l40s \| rtx-6000] | (required) GPU type to use for inference                         |
| `--min-replicas`- INTEGER                           | Minimum number of replicas to deploy                             |
| `--max-replicas`- INTEGER                           | Maximum number of replicas to deploy                             |
| `--gpu-count` - INTEGER                             | Number of GPUs to use per replica                                |
| `--display-name`- TEXT                              | A human-readable name for the endpoint                           |
| `--no-prompt-cache`                                 | Disable the prompt cache for this endpoint                       |
| `--no-speculative-decoding`                         | Disable speculative decoding for this endpoint                   |
| `--no-auto-start`                                   | Create the endpoint in STOPPED state instead of auto-starting it |
| `--wait`                                            | Wait for the endpoint to be ready after creation                 |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
