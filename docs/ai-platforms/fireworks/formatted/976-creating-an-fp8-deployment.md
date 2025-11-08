---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating an FP8 deployment

By default, creating a deployment uses the FP16 checkpoint. To use a quantized FP8 checkpoint, first ensure the model has been prepared for FP8 (see [Checking available precisions](#checking-available-precisions) above), then pass the `--precision` flag when creating your deployment:

<Tabs>
  <Tab title="firectl">
```bash
    firectl create deployment <MODEL> --accelerator-type NVIDIA_H100_80GB --precision FP8
```
  </Tab>

  <Tab title="Python (REST API)">
```python
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    # The ID of the model you want to deploy.

    # The model must be prepared for FP8 precision.

    MODEL_ID = "<YOUR_MODEL_ID>"
    DEPLOYMENT_NAME = "My FP8 Deployment"

    response = requests.post(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/deployments",
      headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
      },
      json={
        "displayName": DEPLOYMENT_NAME,
        "baseModel": MODEL_ID,
        "acceleratorType": "NVIDIA_H100_80GB",
        "precision": "FP8",
      }
    )

    print(response.json())
```
  </Tab>
</Tabs>

>   **📝 Note**
>
> Quantized deployments can only be served using H100 GPUs.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
