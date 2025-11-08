---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## depending on the metric we want to compute.

def assess_claims(query, claims, context, model, client):

  # define the instructions on how to perform the assessment.

  # the model has to append to each row a binary SUPPORTED tag

  preamble = "You are shown a prompt, a context and a list of claims. You have to check which of the claims in the list are supported by the context. Please return the list of claims exactly as is it, just append to each row “SUPPORTED=1” if the claim is supported by the context, or “SUPPORTED=0” if the claim is not supported by the context. Do not add any further explanation to the bullet points."

  # turn list into string

  context = '\n'.join(context)

  # build the prompt

  prompt = f"{preamble}\n\nPROMPT: {query}\n\nCONTEXT:\n{context}\n\nCLAIMS:\n{claims}"

  # get the response

  assessment = get_response(model, client, prompt)

  return assessment
```

### Faithfulness

```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
