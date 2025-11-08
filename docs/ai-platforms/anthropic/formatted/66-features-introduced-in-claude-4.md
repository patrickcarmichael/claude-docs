---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Features introduced in Claude 4

The following features were introduced in Claude 4 and are available across Claude 4 models, including Claude Sonnet 4.5 and Claude Haiku 4.5.

### New refusal stop reason

Claude 4 models introduce a new `refusal` stop reason for content that the model declines to generate for safety reasons:
```json
{"id":"msg_014XEDjypDjFzgKVWdFUXxZP",
"type":"message",
"role":"assistant",
"model":"claude-sonnet-4-5",
"content":[{"type":"text","text":"I would be happy to assist you. You can "}],
"stop_reason":"refusal",
"stop_sequence":null,
"usage":{"input_tokens":564,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":22}
}
```

When using Claude 4 models, you should update your application to [handle `refusal` stop reasons](/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).

### Summarized thinking

With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude's full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse.

While the API is consistent across Claude 3.7 and 4 models, streaming responses for extended thinking might return in a "chunky" delivery pattern, with possible delays between streaming events.

>   **📝 Note**
>
> Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.

For more information, see the [Extended thinking documentation](/en/docs/build-with-claude/extended-thinking#summarized-thinking).

### Interleaved thinking

Claude 4 models support interleaving tool use with extended thinking, allowing for more natural conversations where tool uses and responses can be mixed with regular messages.

>   **📝 Note**
>
> Interleaved thinking is in beta. To enable interleaved thinking, add [the beta header](/en/api/beta-headers) `interleaved-thinking-2025-05-14` to your API request.

For more information, see the [Extended thinking documentation](/en/docs/build-with-claude/extended-thinking#interleaved-thinking).

### Behavioral differences

Claude 4 models have notable behavioral changes that may affect how you structure prompts:

#### Communication style changes

* **More concise and direct**: Claude 4 models communicate more efficiently, with less verbose explanations
* **More natural tone**: Responses are slightly more conversational and less machine-like
* **Efficiency-focused**: May skip detailed summaries after completing actions to maintain workflow momentum (you can prompt for more detail if needed)

#### Instruction following

Claude 4 models are trained for precise instruction following and require more explicit direction:

* **Be explicit about actions**: Use direct language like "Make these changes" or "Implement this feature" rather than "Can you suggest changes" if you want Claude to take action
* **State desired behaviors clearly**: Claude will follow instructions precisely, so being specific about what you want helps achieve better results

For comprehensive guidance on working with these models, see [Claude 4 prompt engineering best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices).

### Updated text editor tool

The text editor tool has been updated for Claude 4 models with the following changes:

* **Tool type**: `text_editor_20250728`
* **Tool name**: `str_replace_based_edit_tool`
* The `undo_edit` command is no longer supported

>   **📝 Note**
>
> The `str_replace_editor` text editor tool remains the same for Claude Sonnet 3.7.

If you're migrating from Claude Sonnet 3.7 and using the text editor tool:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
