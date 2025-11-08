---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming Web Search

Monitor web search progress with streaming:
```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the latest news about AI?',
            },
          ],
        },
      ],
      plugins: [{ id: 'web', max_results: 2 }],
      stream: true,
      max_output_tokens: 9000,
    }),
  });

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
        if (data === '[DONE]') return;

        try {
          const parsed = JSON.parse(data);
          if (parsed.type === 'response.output_item.added' &&
              parsed.item?.type === 'message') {
            console.log('Message added');
          }
          if (parsed.type === 'response.completed') {
            const annotations = parsed.response?.output
              ?.find(o => o.type === 'message')
              ?.content?.find(c => c.type === 'output_text')
              ?.annotations || [];
            console.log('Citations:', annotations.length);
          }
        } catch (e) {
          // Skip invalid JSON
        }
      }
    }
  }
```
```python title="Python"
  import requests
  import json

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the latest news about AI?',
                      },
                  ],
              },
          ],
          'plugins': [{'id': 'web', 'max_results': 2}],
          'stream': True,
          'max_output_tokens': 9000,
      },
      stream=True
  )

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
              if data == '[DONE]':
                  break
              try:
                  parsed = json.loads(data)
                  if (parsed.get('type') == 'response.output_item.added' and
                      parsed.get('item', {}).get('type') == 'message'):
                      print('Message added')
                  if parsed.get('type') == 'response.completed':
                      output = parsed.get('response', {}).get('output', [])
                      message = next((o for o in output if o.get('type') == 'message'), {})
                      content = message.get('content', [])
                      text_content = next((c for c in content if c.get('type') == 'output_text'), {})
                      annotations = text_content.get('annotations', [])
                      print(f'Citations: {len(annotations)}')
              except json.JSONDecodeError:
                  continue
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
