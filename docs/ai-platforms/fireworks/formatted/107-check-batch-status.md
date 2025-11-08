---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Check Batch Status

Source: https://docs.fireworks.ai/api-reference/get-batch-status

get /v1/accounts/{account_id}/batch_job/{batch_id}

This endpoint allows you to check the current status of a previously submitted batch request, and retrieve the final result if available.

<CardGroup cols={1}>
  <Card title="Try notebook" icon="rocket" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/batch-api/batch_api.ipynb">
    Check status of your batch request
  </Card>
</CardGroup>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key. e.g. `Authorization=FIREWORKS_API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Path Parameters

<ParamField query="account_id" type="string" required>
  The identifier of your Fireworks account. Must match the account used when the batch request was submitted.
</ParamField>

<ParamField query="batch_id" type="string" required>
  The unique identifier of the batch job to check.\
  This should match the `batch_id` returned when the batch request was originally submitted.
</ParamField>

### Response

The response includes the status of the batch job and, if completed, the final result.

<Tabs>
  <Tab title="json">
    <ResponseField name="status" type="string" required>
      The status of the batch job at the time of the request.\
      Possible values include `"completed"` and `"processing"`.
    </ResponseField>

    <ResponseField name="batch_id" type="string" required>
      The unique identifier of the batch job whose status is being retrieved.\
      This ID matches the one provided in the original request.
    </ResponseField>

    <ResponseField name="message" type="string" optional>
      A human-readable message describing the current state of the batch job.\
      This field is typically `null` when the job has completed successfully.
    </ResponseField>

    <ResponseField name="content_type" type="string" optional>
      The original content type of the response body.\
      This value can be used to determine how to parse the string in the `body` field.
    </ResponseField>

    <ResponseField name="body" type="string" optional>
      The serialized result of the batch job, this field is only present when `status` is `"completed"`.\
      The format of this string depends on the `content_type` field and may vary across endpoints.\
      Clients should use `content_type` to determine how to parse or interpret the value.
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
```bash
  # Make request

  curl -X GET "https://audio-batch.api.fireworks.ai/v1/accounts/{account_id}/batch_job/{batch_id}" \
  -H "Authorization: <FIREWORKS_API_KEY>"
```
```python
  !pip install requests

  import os
  import requests

  # Input api key and path parameters

  api_key = "<FIREWORKS_API_KEY>"
  account_id = "<ACCOUNT_ID>"
  batch_id = "<BATCH_ID>"

  # Send request

  url = f"https://audio-batch.api.fireworks.ai/v1/accounts/{account_id}/batch_job/{batch_id}"
  headers = {"Authorization": api_key}

  response = requests.get(url, headers=headers)
  print(response.text)
```
</RequestExample>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
