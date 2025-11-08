---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

Safety is a critical factor in building confidence in any technology, especially an emerging one with as much power and flexibility as large language models. Cohere recognizes that appropriate model outputs are dependent on the context of a customer’s use case and business needs, and **Safety Modes** provide a way to consistently and reliably set guardrails that are safe while still being suitable for a specific set of needs.

<Warning title="Built-in Protections">
  Command A, Command A Vision, Command R7B, Command R+, and Command R have built-in protections against core harms, such as content that endangers child safety, which are **always** operative and cannot be adjusted.
</Warning>

<Warning title="Reasoning Models">
  Be aware that Safety Modes is not optimized for [Command A Reasoning](/docs/command-a-reasoning) when reasoning is enabled, so monitor it closely when using it in sensitive contexts.
</Warning>

<Warning title="Safety versus Security">
  We know customers often think of security as interlinked with safety; this is true, but the two are nevertheless distinct. This page details the guardrails we provide to prevent models from generating unsafe outputs. For information on our data security and cybersecurity practices, please consult the [security page](https://cohere.com/security).
</Warning>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
