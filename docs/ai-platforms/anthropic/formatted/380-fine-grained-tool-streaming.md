---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fine-grained tool streaming

Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming


Tool use now supports fine-grained [streaming](/en/docs/build-with-claude/streaming) for parameter values. This allows developers to stream tool use parameters without buffering / JSON validation, reducing the latency to begin receiving large parameters.

>   **📝 Note**
>
> Fine-grained tool streaming is a beta feature. Please make sure to evaluate your responses before using it in production.

  Please use [this form](https://forms.gle/D4Fjr7GvQRzfTZT96) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation—we cannot wait to hear from you!

>   **⚠️ Warning**
>
> When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Please make sure to account for these edge cases in your code.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
