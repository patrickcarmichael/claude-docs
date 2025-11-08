---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Model compatibility

| Model                                                                      | Tool Version           |
| -------------------------------------------------------------------------- | ---------------------- |
| Claude 4.x models                                                          | `text_editor_20250728` |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `text_editor_20250124` |

>   **⚠️ Warning**
>
> The `text_editor_20250728` tool for Claude 4 models does not include the `undo_edit` command. If you require this functionality, you'll need to use Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)).

>   **⚠️ Warning**
>
> Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
