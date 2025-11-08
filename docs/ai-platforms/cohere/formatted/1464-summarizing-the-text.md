---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Summarizing the text

```python PYTHON
def generate_response(message, max_tokens=300, temperature=0.2, k=0):
  """
  A wrapper around the Cohere API to generate a response based on a given prompt.

  Args:
    messsage (str): The input message for generating the response.
    max_tokens (int, optional): The maximum number of tokens in the generated response. Defaults to 300.
    temperature (float, optional): Controls the randomness of the generated response. Higher values (e.g., 1.0) make the output more random, while lower values (e.g., 0.2) make it more deterministic. Defaults to 0.2.
    k (int, optional): Controls the diversity of the generated response. Higher values (e.g., 5) make the output more diverse, while lower values (e.g., 0) make it more focused. Defaults to 0.

  Returns:
    str: The generated response.

  """
  response = co.chat(
    model = co_model,
    message=message,
    max_tokens=max_tokens,
    temperature=temperature,
    return_prompt=True
    )
  return response.text
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
