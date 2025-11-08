---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quantizing a model

A model can be quantized to 8-bit floating-point (FP8) precision.

<Tabs>
  <Tab title="firectl">
```bash
    firectl prepare-model <MODEL_ID>
```
  </Tab>

  <Tab title="Python (REST API)">
```python
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to prepare

    response = requests.post(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}:prepare",
      headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
      },
      json={
        "precision": "FP8"
      }
    )

    print(response.json())
```
  </Tab>
</Tabs>

>   **📝 Note**
>
> This is an additive process that enables creating deployments with additional precisions. The original FP16 checkpoint is still available for use.

You can check on the status of preparation by running:

<Tabs>
  <Tab title="firectl">
```bash
    firectl get model <MODEL_ID>
```
  </Tab>

  <Tab title="Python (REST API)">
```python
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to get

    response = requests.get(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}",
      headers={
        "Authorization": f"Bearer {API_KEY}"
      }
    )

    print(response.json())
```
  </Tab>
</Tabs>

and checking if the state is still in `PREPARING`. A successfully prepared model will have the desired precision added
to the `Precisions` list.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
