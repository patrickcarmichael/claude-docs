---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompt caching

Web search works with [prompt caching](/en/docs/build-with-claude/prompt-caching). To enable prompt caching, add at least one `cache_control` breakpoint in your request. The system will automatically cache up until the last `web_search_tool_result` block when executing the tool.

For multi-turn conversations, set a `cache_control` breakpoint on or after the last `web_search_tool_result` block to reuse cached content.

For example, to use prompt caching with web search for a multi-turn conversation:
```python
  import anthropic

  client = anthropic.Anthropic()

  # First request with web search and cache breakpoint

  messages = [
      {
          "role": "user",
          "content": "What's the current weather in San Francisco today?"
      }
  ]

  response1 = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=messages,
      tools=[{
          "type": "web_search_20250305",
          "name": "web_search",
          "user_location": {
              "type": "approximate",
              "city": "San Francisco",
              "region": "California",
              "country": "US",
              "timezone": "America/Los_Angeles"
          }
      }]
  )

  # Add Claude's response to the conversation

  messages.append({
      "role": "assistant",
      "content": response1.content
  })

  # Second request with cache breakpoint after the search results

  messages.append({
      "role": "user",
      "content": "Should I expect rain later this week?",
      "cache_control": {"type": "ephemeral"}  # Cache up to this point

  })

  response2 = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=messages,
      tools=[{
          "type": "web_search_20250305",
          "name": "web_search",
          "user_location": {
              "type": "approximate",
              "city": "San Francisco",
              "region": "California",
              "country": "US",
              "timezone": "America/Los_Angeles"
          }
      }]
  )
  # The second response will benefit from cached search results

  # while still being able to perform new searches if needed

  print(f"Cache read tokens: {response2.usage.get('cache_read_input_tokens', 0)}")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
