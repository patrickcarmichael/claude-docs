---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## A quick example

To call the Chat API with RAG, pass the following parameters as a minimum:

* `model` for the model ID
* `messages` for the user's query.
* `documents` for defining the documents to be used as the context for the response.

The code snippet below, for example, will produce a grounded answer to `"Where do the tallest penguins live?"`, along with inline citations based on the provided documents.

<Tabs>
  <Tab title="Cohere platform">
```python PYTHON
    # ! pip install -U cohere

    import cohere

    co = cohere.ClientV2(
        "COHERE_API_KEY"
    )  # Get your free API key here: https://dashboard.cohere.com/api-keys

```
  </Tab>

  <Tab title="Private deployment">
```python PYTHON
    # ! pip install -U cohere

    import cohere

    co = cohere.ClientV2(
        api_key="",  # Leave this blank

        base_url="<YOUR_DEPLOYMENT_URL>",
    )
```
  </Tab>
</Tabs>
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
