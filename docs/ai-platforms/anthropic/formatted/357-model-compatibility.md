---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Model compatibility

The code execution tool is available on the following models:

| Model                                                                                                     | Tool Version              |
| --------------------------------------------------------------------------------------------------------- | ------------------------- |
| Claude Opus 4.1 (`claude-opus-4-1-20250805`)                                                              | `code_execution_20250825` |
| Claude Opus 4 (`claude-opus-4-20250514`)                                                                  | `code_execution_20250825` |
| Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)                                                          | `code_execution_20250825` |
| Claude Sonnet 4 (`claude-sonnet-4-20250514`)                                                              | `code_execution_20250825` |
| Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`) ([deprecated](/en/docs/about-claude/model-deprecations)) | `code_execution_20250825` |
| Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)                                                            | `code_execution_20250825` |
| Claude Haiku 3.5 (`claude-3-5-haiku-latest`)                                                              | `code_execution_20250825` |

>   **📝 Note**
>
> The current version `code_execution_20250825` supports Bash commands and file operations. A legacy version `code_execution_20250522` (Python only) is also available. See [Upgrade to latest tool version](#upgrade-to-latest-tool-version) for migration details.

>   **⚠️ Warning**
>
> Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
