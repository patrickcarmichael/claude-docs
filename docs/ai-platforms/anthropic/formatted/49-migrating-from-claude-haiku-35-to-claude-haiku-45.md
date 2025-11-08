---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Migrating from Claude Haiku 3.5 to Claude Haiku 4.5

Claude Haiku 4.5 is our fastest and most intelligent Haiku model with near-frontier performance, delivering premium model quality with real-time performance for interactive applications and high-volume intelligent processing. This migration includes several breaking changes that require updates to your implementation.

For a complete overview of new capabilities, see [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5#key-improvements-in-haiku-4-5-over-haiku-3-5).

>   **📝 Note**
>
> Haiku 4.5 pricing $1 per million input tokens, $5 per million output tokens. See [Claude pricing](/en/docs/about-claude/pricing) for details.

### Migration steps

1. **Update your model name:**
```python
   # Before (Haiku 3.5)

   model="claude-3-5-haiku-20241022"

   # After (Haiku 4.5)

   model="claude-haiku-4-5-20251001"
```

2. **Update tool versions (if applicable)**

   >   **⚠️ Warning**
>
> This is a breaking change from the Claude Haiku 3.5.

   Haiku 4.5 only supports the latest tool versions:
```python
   # Before (Haiku 3.5)

   tools=[{"type": "text_editor_20250124", "name": "str_replace_editor"}]

   # After (Haiku 4.5)

   tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
```

   * **Text editor**: Use `text_editor_20250728` and `str_replace_based_edit_tool`
   * **Code execution**: Use `code_execution_20250825`
   * Remove any code using the `undo_edit` command

3. **Update sampling parameters**

   >   **⚠️ Warning**
>
> This is a breaking change from the Claude Haiku 3.5.

   Use only `temperature` OR `top_p`, not both:
```python
   # Before (Haiku 3.5) - This will error in Haiku 4.5

   response = client.messages.create(
       model="claude-3-5-haiku-20241022",
       temperature=0.7,
       top_p=0.9,  # Cannot use both

       ...
   )

   # After (Haiku 4.5)

   response = client.messages.create(
       model="claude-haiku-4-5-20251001",
       temperature=0.7,  # Use temperature OR top_p, not both

       ...
   )
```

4. **Review new rate limits**

   Haiku 4.5 has separate rate limits from Haiku 3.5. See [Rate limits documentation](/en/api/rate-limits) for details.

5. **Handle the new `refusal` stop reason**

   Update your application to [handle refusal stop reasons](/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).

6. **Consider enabling extended thinking for complex tasks**

   Enable [extended thinking](/en/docs/build-with-claude/extended-thinking) for significant performance improvements on coding and reasoning tasks (disabled by default):
```python
   response = client.messages.create(
       model="claude-haiku-4-5-20251001",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 5000},
       messages=[...]
   )
```

   >   **📝 Note**
>
> Extended thinking impacts [prompt caching](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency.

7. **Explore new capabilities**

   See [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5#key-improvements-in-haiku-4-5-over-haiku-3-5) for details on context awareness, increased output capacity (64K tokens), higher intelligence, and improved speed.

8. **Test your implementation**

   Test in a development environment before deploying to production to ensure all breaking changes are properly handled.

### Haiku 3.5 → 4.5 migration checklist

* [ ] Update model ID to `claude-haiku-4-5-20251001`
* [ ] **BREAKING**: Update tool versions to latest (e.g., `text_editor_20250728`, `code_execution_20250825`) - legacy versions not supported
* [ ] **BREAKING**: Remove any code using the `undo_edit` command (if applicable)
* [ ] **BREAKING**: Update sampling parameters to use only `temperature` OR `top_p`, not both
* [ ] Review and adjust for new rate limits (separate from Haiku 3.5)
* [ ] Handle new `refusal` stop reason in your application
* [ ] Consider enabling extended thinking for complex reasoning tasks (new capability)
* [ ] Leverage context awareness for better token management in long sessions
* [ ] Prepare for larger responses (max output increased from 8K to 64K tokens)
* [ ] Review and update prompts following [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
* [ ] Test in development environment before production deployment

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
