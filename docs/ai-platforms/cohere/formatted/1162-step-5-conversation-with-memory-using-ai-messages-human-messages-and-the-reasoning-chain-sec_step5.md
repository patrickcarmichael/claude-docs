---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 5: Conversation with Memory using AI Messages, Human Messages and the Reasoning Chain \[#sec\_step5]

Reasoning chains can be very long, especially in the cases that contain errors and the agent needs several attempts to get to the final output. Hence, by concatenating all the reasoning chains, we might have two issues: (i) noisy information; (ii) we would quickly hit max input length.

To avoid this issue, we need a way to extract the relevant info from the previous turns. Below, we propose a simple approach to info extraction. We format the extracted info in such a way to enhance human interpretability. We call the objects passed in the chat history *augmented memory objects*.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
