---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Installation

You can install the Fireworks Build SDK using pip:
```bash
pip install --upgrade fireworks-ai
```
Make sure to set the `FIREWORKS_API_KEY` environment variable to your Fireworks API key:
```bash
export FIREWORKS_API_KEY=<API_KEY>
```
You can create an API key in the [Fireworks AI web UI](https://app.fireworks.ai/settings/users/api-keys) or by installing the [firectl](/tools-sdks/firectl/firectl) CLI tool and running:
```bash
firectl signin
firectl create api-key --key-name <Your-Key-Name>
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
