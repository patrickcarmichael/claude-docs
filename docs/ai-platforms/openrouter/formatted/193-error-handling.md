---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error Handling

Handle common errors gracefully:
```typescript title="TypeScript"
  try {
    const response = await fetch('https://openrouter.ai/api/v1/responses', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'openai/o4-mini',
        input: 'Hello, world!',
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      console.error('API Error:', error.error.message);
      return;
    }

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error('Network Error:', error);
  }
```
```python title="Python"
  import requests

  try:
      response = requests.post(
          'https://openrouter.ai/api/v1/responses',
          headers={
              'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
              'Content-Type': 'application/json',
          },
          json={
              'model': 'openai/o4-mini',
              'input': 'Hello, world!',
          }
      )

      if response.status_code != 200:
          error = response.json()
          print(f"API Error: {error['error']['message']}")
      else:
          result = response.json()
          print(result)

  except requests.RequestException as e:
      print(f"Network Error: {e}")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
