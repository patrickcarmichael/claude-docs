---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create Batch Request

Source: https://docs.fireworks.ai/api-reference/create-batch-request

post /{path}?endpoint_id={endpoint_id}

<CardGroup cols={1}>
  <Card title="Try notebook" icon="rocket" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/batch-api/batch_api.ipynb">
    Create a batch request for our audio transcription service
  </Card>
</CardGroup>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=FIREWORKS_API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Path Parameters

<ParamField query="path" type="string" required>
  The relative route of the target API operation (e.g. `"v1/audio/transcriptions"`, `"v1/audio/translations"`). This should correspond to a valid route supported by the backend service.
</ParamField>

### Query Parameters

<ParamField query="endpoint_id" type="string" required>
  Identifies the target backend service or model to handle the request. Currently supported:

  * `audio-prod`: [https://audio-prod.api.fireworks.ai](https://audio-prod.api.fireworks.ai)
  * `audio-turbo`: [https://audio-turbo.api.fireworks.ai](https://audio-turbo.api.fireworks.ai)
</ParamField>

### Body

Request body fields vary depending on the selected `endpoint_id` and `path`.

The request body must conform to the schema defined by the corresponding synchronous API.\
For example, transcription requests typically accept fields such as `model`, `diarize`, and `response_format`.\
Refer to the relevant synchronous API for required fields:

* [Transcribe audio](https://docs.fireworks.ai/api-reference/audio-transcriptions)
* [Translate audio](https://docs.fireworks.ai/api-reference/audio-translations)

### Response

<Tabs>
  <Tab title="json">
    <ResponseField name="status" type="string" required>
      The status of the batch request submission.\
      A value of `"submitted"` indicates the batch request was accepted and queued for processing.
    </ResponseField>

    <ResponseField name="batch_id" type="string" required>
      A unique identifier assigned to the batch job.
      This ID can be used to check job status or retrieve results later.
    </ResponseField>

    <ResponseField name="account_id" type="string" required>
      The unique identifier of the account associated with the batch job.
    </ResponseField>

    <ResponseField name="endpoint_id" type="string" required>
      The backend service selected to process the request.\
      This typically matches the `endpoint_id` used during submission.
    </ResponseField>

    <ResponseField name="message" type="string" optional>
      A human-readable message describing the result of the submission.\
      Typically `"Request submitted successfully"` if accepted.
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
```bash

  # Download audio file

  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request

  curl -X POST "https://audio-batch.api.fireworks.ai/v1/audio/transcriptions?endpoint_id=audio-prod" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
```
```python
  !pip install requests

  import os
  import requests

  # input API key and download audio

  api_key = "<FIREWORKS_API_KEY>"
  audio = requests.get("https://tinyurl.com/4cb74vas").content

  # Prepare request data

  url = "https://audio-batch.api.fireworks.ai/v1/audio/transcriptions?endpoint_id=audio-prod"
  headers = {"Authorization": api_key}
  payload = {
      "model": "whisper-v3",
      "response_format": "json"
  }
  files = {"file": ("audio.flac", audio, "audio/flac")}

  # Send request

  response = requests.post(url, headers=headers, data=payload, files=files)
  print(response.text)
```
</RequestExample>

To check the status of your batch request, use the [Check Batch Status](https://docs.fireworks.ai/api-reference/get-batch-status) endpoint with the returned `batch_id`.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
