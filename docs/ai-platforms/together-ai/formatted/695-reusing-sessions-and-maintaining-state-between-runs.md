---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reusing sessions and maintaining state between runs

The `session_id` can be used to access a previously initialized session. All packages, variables, and memory will be retained.
```python
  from together import Together

  client = Together()

  ## set a variable x to 42

  response1 = client.code_interpreter.run(code="x = 42", language="python")

  session_id = response1.data.session_id

  ## print the value of x

  response2 = client.code_interpreter.run(
      code='print(f"The value of x is {x}")',
      language="python",
      session_id=session_id,
  )

  for output in response2.data.outputs:
      print(f"{output.type}: {output.data}")
```
```typescript
  import Together from 'together-ai';

  const client = new Together();

   // Run the first session
  const response1 = await client.codeInterpreter.execute({
    code: 'x = 42',
    language: 'python',
  });

  if (response1.errors) {
    console.log(`Response 1 errors: ${response1.errors}`);
    return;
  }

  // Save the session_id
  const sessionId = response1.data.session_id;

  // Resuse the first session
  const response2 = await client.codeInterpreter.execute({
    code: 'print(f"The value of x is {x}")',
    language: 'python',
    session_id: sessionId,
  });

  if (response2.errors) {
    console.log(`Response 2 errors: ${response2.errors}`);
    return;
  }

  for (const output of response2.data.outputs) {
    console.log(`${output.type}: ${output.data}`);
  }
```
```bash
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "x = 42"
    }'

    curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "print(f\"The value of x is {x}\")",
      "session_id": "YOUR_SESSION_ID_FROM_FIRST_RESPONSE"
    }'
```

Output
```text
stdout: The value of x is 42
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
