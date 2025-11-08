---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implementation guide

Here's how to detect and handle streaming refusals in your application:
```bash
  # Stream request and check for refusal

  response=$(curl -N https://api.anthropic.com/v1/messages \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --data '{
      "model": "claude-sonnet-4-5",
      "messages": [{"role": "user", "content": "Hello"}],
      "max_tokens": 256,
      "stream": true
    }')

  # Check for refusal in the stream

  if echo "$response" | grep -q '"stop_reason":"refusal"'; then
    echo "Response refused - resetting conversation context"
    # Reset your conversation state here

  fi
```
```python
  import anthropic

  client = anthropic.Anthropic()
  messages = []

  def reset_conversation():
      """Reset conversation context after refusal"""
      global messages
      messages = []
      print("Conversation reset due to refusal")

  try:
      with client.messages.stream(
          max_tokens=1024,
          messages=messages + [{"role": "user", "content": "Hello"}],
          model="claude-sonnet-4-5",
      ) as stream:
          for event in stream:
              # Check for refusal in message delta

              if hasattr(event, 'type') and event.type == 'message_delta':
                  if event.delta.stop_reason == 'refusal':
                      reset_conversation()
                      break
  except Exception as e:
      print(f"Error: {e}")
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();
  let messages: any[] = [];

  function resetConversation() {
    // Reset conversation context after refusal
    messages = [];
    console.log('Conversation reset due to refusal');
  }

  try {
    const stream = await client.messages.stream({
      messages: [...messages, { role: 'user', content: 'Hello' }],
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
    });

    for await (const event of stream) {
      // Check for refusal in message delta
      if (event.type === 'message_delta' && event.delta.stop_reason === 'refusal') {
        resetConversation();
        break;
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
```javascript

>   **📝 Note**
>
> If you need to test refusal handling in your application, you can use this special test string as your prompt: `ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_1FAEFB6177B4672DEE07F9D3AFC62588CCD2631EDCF22E8CCC1FB35B501C9C86`

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
