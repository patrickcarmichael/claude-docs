---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Upgrade to latest tool version

By upgrading to `code-execution-2025-08-25`, you get access to file manipulation and Bash capabilities, including code in multiple languages. There is no price difference.

### What's changed

| Component      | Legacy                      | Current                                                           |
| -------------- | --------------------------- | ----------------------------------------------------------------- |
| Beta header    | `code-execution-2025-05-22` | `code-execution-2025-08-25`                                       |
| Tool type      | `code_execution_20250522`   | `code_execution_20250825`                                         |
| Capabilities   | Python only                 | Bash commands, file operations                                    |
| Response types | `code_execution_result`     | `bash_code_execution_result`, `text_editor_code_execution_result` |

### Backward compatibility

* All existing Python code execution continues to work exactly as before
* No changes required to existing Python-only workflows

### Upgrade steps

To upgrade, you need to make the following changes in your API requests:

1. **Update the beta header**:
```diff
   - "anthropic-beta": "code-execution-2025-05-22"
   + "anthropic-beta": "code-execution-2025-08-25"
```
2. **Update the tool type**:
```diff
   - "type": "code_execution_20250522"
   + "type": "code_execution_20250825"
```
3. **Review response handling** (if parsing responses programmatically):
   * The previous blocks for Python execution responses will no longer be sent
   * Instead, new response types for Bash and file operations will be sent (see Response Format section)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
