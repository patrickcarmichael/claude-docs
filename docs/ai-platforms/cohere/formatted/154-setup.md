---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

First, import the Cohere library and create a client.

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
