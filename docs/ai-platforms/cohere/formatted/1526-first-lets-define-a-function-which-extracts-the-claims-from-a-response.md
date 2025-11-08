---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## first, let's define a function which extracts the claims from a response

def extract_claims(query, response, model, client):

  # define the instructions on how to extract the claims

  preamble = "You are shown a prompt and a completion. You have to identify the main claims stated in the completion. A claim is any sentence or part of a sentence that expresses a verifiable fact. Please return a bullet list, in which every line includes one of the claims you identified. Do not add any further explanation to the bullet points."

  # build the prompt

  prompt = f"{preamble}\n\nPROMPT: {query}\n\nCOMPLETION: {response}"

  # get the claims

  claims = get_response(model, client, prompt)

  return claims
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
