---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting started

**Note:** Make sure your `together` version number is **>1.5.13**. Run `pip install together --upgrade` to upgrade if needed.

### 1. Prepare your batch file

Batches start with a `.jsonl` file where each line contains the details of an individual request to the API. The available endpoint is `/v1/chat/completions` (Chat Completions API). Each request must include a unique `custom_id` value, which you can use to reference results after completion. Here's an example of an input file with 2 requests:
```json batch_input.jsonl theme={null}
{"custom_id": "request-1", "body": {"model": "deepseek-ai/DeepSeek-V3", "messages": [{"role": "user", "content": "Hello, world!"}], "max_tokens": 200}}
{"custom_id": "request-2", "body": {"model": "deepseek-ai/DeepSeek-V3", "messages": [{"role": "user", "content": "Explain quantum computing"}], "max_tokens": 200}}
```
Each line in your batch file must follow this schema:

| Field       | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `custom_id` | string | Yes      | Unique identifier for tracking (max 64 chars)   |
| `body`      | object | Yes      | The request body matching the endpoint's schema |

### 2. Upload your batch input file

You must first upload your input file so that you can reference it correctly when creating batches. Upload your `.jsonl` file using the Files API with `purpose=batch-api`.
```python
  from together import Together

  client = Together()

  ## Uploads batch job file

  file_resp = client.files.upload(file="batch_input.jsonl", purpose="batch-api")
```
```shell
  together files upload batch_input.jsonl --purpose "batch-api"
```

This will return a file object with `id` and other details:
```text
FileResponse(
  id='file-fa37fdce-89cb-414b-923c-2add62250155',
  object=<ObjectType.File: 'file'>,
  ...
  filename='batch_input.jsonl',
  bytes=1268723,
  line_count=0,
  processed=True,
  FileType='jsonl')
```

### 3. Create the batch

Once you've successfully uploaded your input file, you can use the input File object's ID to create a batch. The completion window can be set to `24h`. For now, the completion window defaults to `24h` and cannot be changed. You can also provide custom metadata.
```python
  file_id = file_resp.id

  batch = client.batches.create_batch(file_id, endpoint="/v1/chat/completions")

  print(batch.id)
```
```ts
  import Together from "together-ai";

  const client = new Together();

  // The file id from the previous step
  const fileId = file_resp.id;

  const batch = await client.batches.create({
    endpoint: "/v1/chat/completions",
    input_file_id: fileId,
  });

  console.log(batch);
```

This request will return a Batch object with metadata about your batch:
```json
{
  "id": "batch-xyz789",
  "status": "VALIDATING",
  "endpoint": "/v1/chat/completions",
  "input_file_id": "file-abc123",
  "created_at": "2024-01-15T10:00:00Z",
  "request_count": 0,
  "model_id": null
}
```

### 4. Check the status of a batch

You can check the status of a batch at any time, which will return updated batch information.
```python
  batch_stat = client.batches.get_batch(batch.id)

  print(batch_stat.status)
```
```ts
  import Together from "together-ai";

  const client = new Together();

  // The batch id from the previous step
  const batchId = batch.job?.id;

  let batchInfo = await client.batches.retrieve(batchId);

  console.log(batchInfo.status);
```

The status of a given Batch object can be any of the following:

| Status        | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `VALIDATING`  | The input file is being validated before the batch can begin |
| `IN_PROGRESS` | Batch is in progress                                         |
| `COMPLETED`   | Batch processing completed successfully                      |
| `FAILED`      | Batch processing failed                                      |
| `EXPIRED`     | Batch exceeded deadline                                      |
| `CANCELLED`   | Batch was cancelled                                          |

### 5. Retrieve the results

Once the batch is complete, you can download the output by making a request to retrieve the output file using the `output_file_id` field from the Batch object.
```python
  from together import Together

  client = Together()

  ## Get the batch status to find output_file_id

  batch = client.batches.get_batch("batch-xyz789")

  if batch.status == "COMPLETED":
      # Download the output file

      client.files.retrieve_content(
          id=batch_stat.output_file_id,
          output="batch_output.jsonl",
      )
```
```ts
  import Together from "together-ai";

  const client = new Together();

  // The batch id from the previous step
  const batchInfo = await client.batches.retrieve(batchId);

  if (batchInfo.status === "COMPLETED" && batchInfo.output_file_id) {
    const resp = await client.files.content(batchInfo.output_file_id);
    const result = await resp.text();
    console.log(result);
  }
```

The output `.jsonl` file will have one response line for every successful request line in the input file. Any failed requests will have their error information in a separate error file accessible via `error_file_id`.

Note that the output line order may not match the input line order. Use the `custom_id` field to map requests to results.

### 6. Cancel a batch

You can cancel a batch job as follows:
```python
from together import Together

client = Together()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
