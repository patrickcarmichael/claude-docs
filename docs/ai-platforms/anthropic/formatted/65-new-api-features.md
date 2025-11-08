---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## New API features

### Memory tool (Beta)

The new [memory tool](/en/docs/agents-and-tools/tool-use/memory-tool) enables Claude to store and retrieve information outside the context window:
```python
tools=[
    {
        "type": "memory_20250818",
        "name": "memory"
    }
]
```

This allows for:

* Building knowledge bases over time
* Maintaining project state across sessions
* Preserving effectively unlimited context through file-based storage

>   **📝 Note**
>
> Available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1. Requires [beta header](/en/api/beta-headers): `context-management-2025-06-27`

### Context editing

Use [context editing](/en/docs/build-with-claude/context-editing) for intelligent context management through automatic tool call clearing:
```python
response = client.beta.messages.create(
    betas=["context-management-2025-06-27"],
    model="claude-sonnet-4-5",  # or claude-haiku-4-5

    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    context_management={
        "edits": [
            {
                "type": "clear_tool_uses_20250919",
                "trigger": {"type": "input_tokens", "value": 500},
                "keep": {"type": "tool_uses", "value": 2},
                "clear_at_least": {"type": "input_tokens", "value": 100}
            }
        ]
    },
    tools=[...]
)
```

This feature automatically removes older tool calls and results when approaching token limits, helping manage context in long-running agent sessions.

>   **📝 Note**
>
> Available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1. Requires [beta header](/en/api/beta-headers): `context-management-2025-06-27`

### Enhanced stop reasons

Claude 4.5 models introduce a new `model_context_window_exceeded` stop reason that explicitly indicates when generation stopped due to hitting the context window limit, rather than the requested `max_tokens` limit. This makes it easier to handle context window limits in your application logic.
```json
{
  "stop_reason": "model_context_window_exceeded",
  "usage": {
    "input_tokens": 150000,
    "output_tokens": 49950
  }
}
```

### Improved tool parameter handling

Claude 4.5 models include a bug fix that preserves intentional formatting in tool call string parameters. Previously, trailing newlines in string parameters were sometimes incorrectly stripped. This fix ensures that tools requiring precise formatting (like text editors) receive parameters exactly as intended.

>   **📝 Note**
>
> This is a behind-the-scenes improvement with no API changes required. However, tools with string parameters may now receive values with trailing newlines that were previously stripped.

**Example:**
```json
// Before: Final newline accidentally stripped
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "edit_todo",
  "input": {
    "file": "todo.txt",
    "contents": "1. Chop onions.\n2. ???\n3. Profit"
  }
}

// After: Trailing newline preserved as intended
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "edit_todo",
  "input": {
    "file": "todo.txt",
    "contents": "1. Chop onions.\n2. ???\n3. Profit\n"
  }
}
```

### Token count optimizations

Claude 4.5 models include automatic optimizations to improve model performance. These optimizations may add small amounts of tokens to requests, but **you are not billed for these system-added tokens**.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
