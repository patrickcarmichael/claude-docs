---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting errors

>   **📝 Note**
>
>   **Built-in Error Handling**: [Tool runner](#tool-runner-beta) provide automatic error handling for most common scenarios. This section covers manual error handling for advanced use cases.

There are a few different types of errors that can occur when using tools with Claude:

<AccordionGroup>
  <Accordion title="Tool execution error">
    If the tool itself throws an error during execution (e.g. a network error when fetching weather data), you can return the error message in the `content` along with `"is_error": true`:
```JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "ConnectionError: the weather service API is not available (HTTP 500)",
          "is_error": true
        }
      ]
    }
```
    Claude will then incorporate this error into its response to the user, e.g. "I'm sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later."
  </Accordion>

  <Accordion title="Invalid tool name">
    If Claude's attempted use of a tool is invalid (e.g. missing required parameters), it usually means that the there wasn't enough information for Claude to use the tool correctly. Your best bet during development is to try the request again with more-detailed `description` values in your tool definitions.

    However, you can also continue the conversation forward with a `tool_result` that indicates the error, and Claude will try to use the tool again with the missing information filled in:
```JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Missing required 'location' parameter",
          "is_error": true
        }
      ]
    }
```
    If a tool request is invalid or missing parameters, Claude will retry 2-3 times with corrections before apologizing to the user.
  </Accordion>

  <Accordion title="<search_quality_reflection> tags">
    To prevent Claude from reflecting on search quality with \<search\_quality\_reflection> tags, add "Do not reflect on the quality of the returned search results in your response" to your prompt.
  </Accordion>

  <Accordion title="Server tool errors">
    When server tools encounter errors (e.g., network issues with Web Search), Claude will transparently handle these errors and attempt to provide an alternative response or explanation to the user. Unlike client tools, you do not need to handle `is_error` results for server tools.

    For web search specifically, possible error codes include:

    * `too_many_requests`: Rate limit exceeded
    * `invalid_input`: Invalid search query parameter
    * `max_uses_exceeded`: Maximum web search tool uses exceeded
    * `query_too_long`: Query exceeds maximum length
    * `unavailable`: An internal error occurred
  </Accordion>

  <Accordion title="Parallel tool calls not working">
    If Claude isn't making parallel tool calls when expected, check these common issues:

    **1. Incorrect tool result formatting**

    The most common issue is formatting tool results incorrectly in the conversation history. This "teaches" Claude to avoid parallel calls.

    Specifically for parallel tool use:

    * ❌ **Wrong**: Sending separate user messages for each tool result
    * ✅ **Correct**: All tool results must be in a single user message
```json
    // ❌ This reduces parallel tool use
    [
      {"role": "assistant", "content": [tool_use_1, tool_use_2]},
      {"role": "user", "content": [tool_result_1]},
      {"role": "user", "content": [tool_result_2]}  // Separate message
    ]

    // ✅ This maintains parallel tool use
    [
      {"role": "assistant", "content": [tool_use_1, tool_use_2]},
      {"role": "user", "content": [tool_result_1, tool_result_2]}  // Single message
    ]
```
    See the [general formatting requirements above](#handling-tool-use-and-tool-result-content-blocks) for other formatting rules.

    **2. Weak prompting**

    Default prompting may not be sufficient. Use stronger language:
```text
    <use_parallel_tool_calls>
    For maximum efficiency, whenever you perform multiple independent operations,
    invoke all relevant tools simultaneously rather than sequentially.
    Prioritize calling tools in parallel whenever possible.
    </use_parallel_tool_calls>
```
    **3. Measuring parallel tool usage**

    To verify parallel tool calls are working:
```python
    # Calculate average tools per tool-calling message

    tool_call_messages = [msg for msg in messages if any(
        block.type == "tool_use" for block in msg.content
    )]
    total_tool_calls = sum(
        len([b for b in msg.content if b.type == "tool_use"])
        for msg in tool_call_messages
    )
    avg_tools_per_message = total_tool_calls / len(tool_call_messages)
    print(f"Average tools per message: {avg_tools_per_message}")
    # Should be > 1.0 if parallel calls are working

```
    **4. Model-specific behavior**

    * Claude Opus 4.1, Opus 4, and Sonnet 4: Excel at parallel tool use with minimal prompting
    * Claude Sonnet 3.7: May need stronger prompting or [token-efficient tool use](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use)
    * Claude Haiku: Less likely to use parallel tools without explicit prompting
  </Accordion>
</AccordionGroup>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
