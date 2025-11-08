---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Migrating from Claude Sonnet 3.7 to Claude Sonnet 4.5

Claude Sonnet 4.5 is our most intelligent model, offering best-in-class performance for reasoning, coding, and long-running autonomous agents. This migration includes several breaking changes that require updates to your implementation.

### Migration steps

1. **Update your model name:**
```python
   # Before (Claude Sonnet 3.7)

   model="claude-3-7-sonnet-20250219"

   # After (Claude Sonnet 4.5)

   model="claude-sonnet-4-5-20250929"
```

2. **Update sampling parameters**

   >   **⚠️ Warning**
>
> This is a breaking change from the Claude Sonnet 3.7.

   Use only `temperature` OR `top_p`, not both:
```python
   # Before (Claude Sonnet 3.7) - This will error in Sonnet 4.5

   response = client.messages.create(
       model="claude-3-7-sonnet-20250219",
       temperature=0.7,
       top_p=0.9,  # Cannot use both

       ...
   )

   # After (Claude Sonnet 4.5)

   response = client.messages.create(
       model="claude-sonnet-4-5-20250929",
       temperature=0.7,  # Use temperature OR top_p, not both

       ...
   )
```

3. **Handle the new `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals):
```python
   response = client.messages.create(...)

   if response.stop_reason == "refusal":
       # Handle refusal appropriately

       pass
```

4. **Update text editor tool (if applicable)**

   >   **⚠️ Warning**
>
> This is a breaking change from the Claude Sonnet 3.7.

   Update to `text_editor_20250728` (type) and `str_replace_based_edit_tool` (name). Remove any code using the `undo_edit` command.
```python
   # Before (Claude Sonnet 3.7)

   tools=[{"type": "text_editor_20250124", "name": "str_replace_editor"}]

   # After (Claude Sonnet 4.5)

   tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
```

   See [Text editor tool documentation](/en/docs/agents-and-tools/tool-use/text-editor-tool) for details.

5. **Update code execution tool (if applicable)**

   Upgrade to `code_execution_20250825`. The legacy version `code_execution_20250522` still works but is not recommended. See [Code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version) for migration instructions.

6. **Remove token-efficient tool use beta header**

   [Token-efficient tool use](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use) is a beta feature that only works with Claude 3.7 Sonnet. All Claude 4 models have built-in token-efficient tool use, so you should no longer include the beta header.

   Remove the `token-efficient-tools-2025-02-19` [beta header](/en/api/beta-headers) from your requests:
```python
   # Before (Claude Sonnet 3.7)

   client.messages.create(
       model="claude-3-7-sonnet-20250219",
       betas=["token-efficient-tools-2025-02-19"],  # Remove this

       ...
   )

   # After (Claude Sonnet 4.5)

   client.messages.create(
       model="claude-sonnet-4-5-20250929",
       # No token-efficient-tools beta header

       ...
   )
```

7. **Remove extended output beta header**

   The `output-128k-2025-02-19` [beta header](/en/api/beta-headers) for extended output is only available in Claude Sonnet 3.7.

   Remove this header from your requests:
```python
   # Before (Claude Sonnet 3.7)

   client.messages.create(
       model="claude-3-7-sonnet-20250219",
       betas=["output-128k-2025-02-19"],  # Remove this

       ...
   )

   # After (Claude Sonnet 4.5)

   client.messages.create(
       model="claude-sonnet-4-5-20250929",
       # No output-128k beta header

       ...
   )
```

8. **Update your prompts for behavioral changes**

   Claude Sonnet 4.5 has a more concise, direct communication style and requires explicit direction. Review [Claude 4 prompt engineering best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices) for optimization guidance.

9. **Consider enabling extended thinking for complex tasks**

   Enable [extended thinking](/en/docs/build-with-claude/extended-thinking) for significant performance improvements on coding and reasoning tasks (disabled by default):
```python
   response = client.messages.create(
       model="claude-sonnet-4-5-20250929",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 10000},
       messages=[...]
   )
```

   >   **📝 Note**
>
> Extended thinking impacts [prompt caching](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency.

10. **Test your implementation**

Test in a development environment before deploying to production to ensure all breaking changes are properly handled.

### Sonnet 3.7 → 4.5 migration checklist

* [ ] Update model ID to `claude-sonnet-4-5-20250929`
* [ ] **BREAKING**: Update sampling parameters to use only `temperature` OR `top_p`, not both
* [ ] Handle new `refusal` stop reason in your application
* [ ] **BREAKING**: Update text editor tool to `text_editor_20250728` and `str_replace_based_edit_tool` (if applicable)
* [ ] **BREAKING**: Remove any code using the `undo_edit` command (if applicable)
* [ ] Update code execution tool to `code_execution_20250825` (if applicable)
* [ ] Remove `token-efficient-tools-2025-02-19` beta header (if applicable)
* [ ] Remove `output-128k-2025-02-19` beta header (if applicable)
* [ ] Review and update prompts following [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
* [ ] Consider enabling extended thinking for complex reasoning tasks
* [ ] Handle `model_context_window_exceeded` stop reason (Sonnet 4.5 specific)
* [ ] Consider enabling memory tool for long-running agents (beta)
* [ ] Consider using automatic tool call clearing for context editing (beta)
* [ ] Test in development environment before production deployment

### Features removed from Claude Sonnet 3.7

* **Token-efficient tool use**: The `token-efficient-tools-2025-02-19` beta header only works with Claude 3.7 Sonnet and is not supported in Claude 4 models (see step 6)
* **Extended output**: The `output-128k-2025-02-19` beta header is not supported (see step 7)

Both headers can be included in Claude 4 requests but will have no effect.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
