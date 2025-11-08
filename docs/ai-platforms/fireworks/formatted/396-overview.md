---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

These examples show how to use the `cosine_scaled_accuracy_length_reward` function to evaluate model responses based on both:

1. Accuracy (correctness of the answer)
2. Length efficiency (brevity of the response)

This combined approach rewards responses that are both accurate and concise, penalizing verbosity in correct answers and providing a clear separation between correct and incorrect responses.

**Note**: The accuracy detection depends on specific text-extraction mechanisms that may need customization for different types of content using the `extract_fn` and `compare_fn` parameters.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
