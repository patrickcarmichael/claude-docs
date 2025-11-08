---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hardware

List all the hardware options, optionally filtered by model.

### Usage

```sh
together endpoints hardware [OPTIONS]
```

### Example

```sh
together endpoints hardware --model mistralai/Mixtral-8x7B-Instruct-v0.1
```

### Options

| Options         | Description                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| `--model`- TEXT | Filter hardware options by model                                               |
| `--json`        | Print output in JSON format                                                    |
| `--available`   | Print only available hardware options (can only be used if model is passed in) |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
