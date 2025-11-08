---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using the TCI for Data analysis

Together Code Interpreter is a very powerful tool and gives you access to a fully functional coding environment. You can install Python libraries and conduct fully fledged data analysis experiments.
```python
  from together import Together

  client = Together()

  ## Create a code interpreter instance

  code_interpreter = client.code_interpreter

  code = """
  !pip install numpy
  import numpy as np

  ## Create a random matrix

  matrix = np.random.rand(3, 3)
  print("Random matrix:")
  print(matrix)

  ## Calculate eigenvalues

  eigenvalues = np.linalg.eigvals(matrix)
  print("\\nEigenvalues:")
  print(eigenvalues)
  """

  response = code_interpreter.run(code=code, language="python")

  for output in response.data.outputs:
      print(f"{output.type}: {output.data}")
  if response.data.errors:
      print(f"Errors: {response.data.errors}")
```
```typescript
  import Together from 'together-ai';

  const client = new Together();

  // Data analysis
  const code = `
    !pip install numpy
    import numpy as np

    # Create a random matrix

    matrix = np.random.rand(3, 3)
    print("Random matrix:")
    print(matrix)

    # Calculate eigenvalues

    eigenvalues = np.linalg.eigvals(matrix)
    print("\\nEigenvalues:")
    print(eigenvalues)
  `;

  const response = await client.codeInterpreter.execute({
    code,
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
```bash
  curl -X POST "https://api.together.ai/tci/execute" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "language": "python",
      "code": "!pip install numpy\nimport numpy as np\n# Create a random matrix\nmatrix = np.random.rand(3, 3)\nprint(\"Random matrix:\")\nprint(matrix)\n# Calculate eigenvalues\neigenvalues = np.linalg.eigvals(matrix)\nprint(\"\\nEigenvalues:\")\nprint(eigenvalues)"

    }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
