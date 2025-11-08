---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## New Feature: Safety Modes

The primary new feature available in both `command-r-08-2024` and `command-r-plus-08-2024` is Safety Modes (in beta). For our enterprise customers building with our models, what is considered safe depends on their use case and the context the model is deployed in. To support diverse enterprise applications, we have developed safety modes, acknowledging that safety and appropriateness are context-dependent, and that predictability and control are critical in building confidence in Cohere models.

Safety guardrails have traditionally been reactive and binary, and we’ve observed that users often have difficulty defining what safe usage means to them for their use case. Safety Modes introduce a nuanced approach that is context sensitive.

(Note: Command R/R+ have built-in protections against core harms, such as content that endangers child safety. These types of harm are always blocked and cannot be adjusted.)

Safety modes are activated through a `safety_mode` parameter, which can (currently) be in one of two modes:

* `"STRICT"`: Encourages avoidance of all sensitive topics. Strict content guardrails provide an extra safe experience by prohibiting inappropriate responses or recommendations. Ideal for general and enterprise use.
* `"CONTEXTUAL"`: (enabled by default): For wide-ranging interactions with fewer constraints on output while maintaining core protections. The model responds as instructed while still rejecting harmful or illegal suggestions. Well-suited for entertainment, creative, educational use.

You can also opt out of the safety modes beta by setting `safety_mode="NONE"`. For more information, check out our dedicated guide to [Safety Modes](https://docs.cohere.com/docs/safety-modes).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
