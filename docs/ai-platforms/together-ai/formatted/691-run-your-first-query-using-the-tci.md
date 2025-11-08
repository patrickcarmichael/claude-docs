---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run your first query using the TCI

```python
  from together import Together

  client = Together()

  ## Run a simple print statement in the code interpreter

  response = client.code_interpreter.run(
      code='print("Welcome to Together Code Interpreter!")',
      language="python",
  )


  print(f"Status: {response.data.status}")


  for output in response.data.outputs:
      print(f"{output.type}: {output.data}")
```
```typescript
  import Together from 'together-ai';

  const client = new Together();

  const response = await client.codeInterpreter.execute({
    code: 'print("Welcome to Together Code Interpreter!")',
    language: 'python',
  });

  if (response.errors) {
    console.log(`Errors: ${response.errors}`);
  } else {
    for (const output of response.data.outputs) {
      console.log(`${output.type}: ${output.data}`);
    }
  }
```
```powershell
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "print(\"Welcome to Together Code Interpreter!\")"
    }'
```

Output
```text
Status: completed
stdout: Welcome to Together Code Interpreter!
```
> ℹ️ Pricing information
>
> TCI usage is billed at **\$0.03/session**. As detailed below, sessions have a lifespan of 60 minutes and can be used multiple times.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
