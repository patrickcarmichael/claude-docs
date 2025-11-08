---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Claude 4 models

tools=[
    {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
    }
]
```

For more information, see the [Text editor tool documentation](/en/docs/agents-and-tools/tool-use/text-editor-tool).

### Updated code execution tool

If you're using the code execution tool, ensure you're using the latest version `code_execution_20250825`, which adds Bash commands and file manipulation capabilities.

The legacy version `code_execution_20250522` (Python only) is still available but not recommended for new implementations.

For migration instructions, see the [Code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
