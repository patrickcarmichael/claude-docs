---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How `math_reward` Works

The `math_reward` function:

1. Extracts potential answer values from the last assistant message
2. Extracts expected answer value from the provided string
3. Compares them with tolerance for floating-point values
4. Returns a score of 1.0 for correct answers and 0.0 for incorrect answers
5. Provides detailed metrics about the extraction and comparison process

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
