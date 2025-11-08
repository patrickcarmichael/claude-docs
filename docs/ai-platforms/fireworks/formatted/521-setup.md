---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

1. **Environment**: Ensure your Python environment has `reward-kit` and its development dependencies installed:
```bash
   # From the root of the repository

   pip install -e ".[dev]"
```
2. **TRL Extras (for `trl_grpo_integration.py`)**:
```bash
   pip install "reward-kit[trl]"
```
3. **API Keys**: If using models that require API keys (e.g., Fireworks AI models for `local_eval.py` if not using a local model, or for downloading a base model for TRL), ensure necessary keys like `FIREWORKS_API_KEY` are set.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
