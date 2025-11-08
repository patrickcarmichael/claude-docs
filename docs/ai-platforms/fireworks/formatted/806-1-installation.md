---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Installation

1. **Clone the quickstart repo**: [https://github.com/eval-protocol/quickstart](https://github.com/eval-protocol/quickstart)
```bash
git clone git@github.com:eval-protocol/quickstart.git
cd quickstart
```
2. **Install Eval Protocol**:
```bash
pip install "eval-protocol[svgbench]"
```
3. **Environment Setup**:

Make a copy of `env.example`, name it `.env`, and fill in the keys:
```
FIREWORKS_API_KEY=your-fireworks-key-here
OPENAI_API_KEY=your-openai-key-here
```
Place this file in your evaluator directory (e.g., `evaluator/.env`). The create process below automatically reads and uploads these secrets to Fireworks.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
