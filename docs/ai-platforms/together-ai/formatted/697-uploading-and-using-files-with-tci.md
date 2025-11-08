---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Uploading and using files with TCI

```python
  from together import Together

  client = Together()

  ## Create a code interpreter instance

  code_interpreter = client.code_interpreter

  script_content = "import sys\nprint(f'Hello from inside {sys.argv[0]}!')"

  ## Define the script file as a dictionary

  script_file = {
      "name": "myscript.py",
      "encoding": "string",
      "content": script_content,
  }

  code_to_run_script = "!python myscript.py"

  response = code_interpreter.run(
      code=code_to_run_script,
      language="python",
      files=[script_file],  # Pass the script dictionary in a list

  )

  ## Print results

  print(f"Status: {response.data.status}")
  for output in response.data.outputs:
      print(f"{output.type}: {output.data}")
  if response.data.errors:
      print(f"Errors: {response.data.errors}")
```
```typescript
  import Together from 'together-ai';

  // Initialize the Together client
  const client = new Together();

  // Create a code interpreter instance
  const codeInterpreter = client.codeInterpreter;

  // Define the script content
  const scriptContent = "import sys\nprint(f'Hello from inside {sys.argv[0]}!')";

  // Define the script file as an object
  const scriptFile = {
    name: "myscript.py",
    encoding: "string",
    content: scriptContent,
  };

  // Define the code to run the script
  const codeToRunScript = "!python myscript.py";

  // Run the code interpreter
  async function runScript() {
    const response = await codeInterpreter.run({
      code: codeToRunScript,
```
```bash
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "files": [
        {
          "name": "myscript.py",
          "encoding": "string",
          "content": "import sys\nprint(f'\''Hello from inside {sys.argv[0]}!'\'')"
        }
      ],
      "code": "!python myscript.py"
    }'
```

Output
```text
Status: completed
stdout: Hello from inside myscript.py!
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
