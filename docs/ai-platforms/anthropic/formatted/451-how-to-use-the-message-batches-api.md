---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use the Message Batches API

### Prepare and create your batch

A Message Batch is composed of a list of requests to create a Message. The shape of an individual request is comprised of:

* A unique `custom_id` for identifying the Messages request
* A `params` object with the standard [Messages API](/en/api/messages) parameters

You can [create a batch](/en/api/creating-message-batches) by passing this list into the `requests` parameter:
```bash
  curl https://api.anthropic.com/v1/messages/batches \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "requests": [
          {
              "custom_id": "my-first-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "messages": [
                      {"role": "user", "content": "Hello, world"}
                  ]
              }
          },
          {
              "custom_id": "my-second-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "messages": [
                      {"role": "user", "content": "Hi again, friend"}
                  ]
              }
          }
      ]
  }'
```
```python
  import anthropic
  from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
  from anthropic.types.messages.batch_create_params import Request

  client = anthropic.Anthropic()

  message_batch = client.messages.batches.create(
      requests=[
          Request(
              custom_id="my-first-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  messages=[{
                      "role": "user",
                      "content": "Hello, world",
                  }]
              )
          ),
          Request(
              custom_id="my-second-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  messages=[{
                      "role": "user",
                      "content": "Hi again, friend",
                  }]
              )
          )
      ]
  )

  print(message_batch)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const messageBatch = await anthropic.messages.batches.create({
    requests: [{
      custom_id: "my-first-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        messages: [
          {"role": "user", "content": "Hello, world"}
        ]
      }
    }, {
      custom_id: "my-second-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        messages: [
          {"role": "user", "content": "Hi again, friend"}
        ]
      }
    }]
  });

  console.log(messageBatch)
```
```java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.batches.*;

  public class BatchExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          BatchCreateParams params = BatchCreateParams.builder()
              .addRequest(BatchCreateParams.Request.builder()
                  .customId("my-first-request")
                  .params(BatchCreateParams.Request.Params.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addUserMessage("Hello, world")
                      .build())
                  .build())
              .addRequest(BatchCreateParams.Request.builder()
                  .customId("my-second-request")
                  .params(BatchCreateParams.Request.Params.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addUserMessage("Hi again, friend")
                      .build())
                  .build())
              .build();

          MessageBatch messageBatch = client.messages().batches().create(params);

          System.out.println(messageBatch);
      }
  }
```

In this example, two separate requests are batched together for asynchronous processing. Each request has a unique `custom_id` and contains the standard parameters you'd use for a Messages API call.

<Tip>
  **Test your batch requests with the Messages API**

  Validation of the `params` object for each message request is performed asynchronously, and validation errors are returned when processing of the entire batch has ended. You can ensure that you are building your input correctly by verifying your request shape with the [Messages API](/en/api/messages) first.
</Tip>

When a batch is first created, the response will have a processing status of `in_progress`.
```JSON
{
  "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

### Tracking your batch

The Message Batch's `processing_status` field indicates the stage of processing the batch is in. It starts as `in_progress`, then updates to `ended` once all the requests in the batch have finished processing, and results are ready. You can monitor the state of your batch by visiting the [Console](https://console.anthropic.com/settings/workspaces/default/batches), or using the [retrieval endpoint](/en/api/retrieving-message-batches).

#### Polling for Message Batch completion

To poll a Message Batch, you'll need its `id`, which is provided in the response when creating a batch or by listing batches. You can implement a polling loop that checks the batch status periodically until processing has ended:
```python
  import anthropic
  import time

  client = anthropic.Anthropic()

  message_batch = None
  while True:
      message_batch = client.messages.batches.retrieve(
          MESSAGE_BATCH_ID
      )
      if message_batch.processing_status == "ended":
          break

      print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
      time.sleep(60)
  print(message_batch)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  let messageBatch;
  while (true) {
    messageBatch = await anthropic.messages.batches.retrieve(
      MESSAGE_BATCH_ID
    );
    if (messageBatch.processing_status === 'ended') {
      break;
    }

    console.log(`Batch ${messageBatch} is still processing... waiting`);
    await new Promise(resolve => setTimeout(resolve, 60_000));
  }
  console.log(messageBatch);
```
```bash
  #!/bin/sh

  until [[ $(curl -s "https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID" \
            --header "x-api-key: $ANTHROPIC_API_KEY" \
            --header "anthropic-version: 2023-06-01" \
            | grep -o '"processing_status":[[:space:]]*"[^"]*"' \
            | cut -d'"' -f4) == "ended" ]]; do
      echo "Batch $MESSAGE_BATCH_ID is still processing..."
      sleep 60
  done

  echo "Batch $MESSAGE_BATCH_ID has finished processing"
```

### Listing all Message Batches

You can list all Message Batches in your Workspace using the [list endpoint](/en/api/listing-message-batches). The API supports pagination, automatically fetching additional pages as needed:
```python
  import anthropic

  client = anthropic.Anthropic()

  # Automatically fetches more pages as needed.

  for message_batch in client.messages.batches.list(
      limit=20
  ):
      print(message_batch)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Automatically fetches more pages as needed.
  for await (const messageBatch of anthropic.messages.batches.list({
    limit: 20
  })) {
    console.log(messageBatch);
  }
```
```bash
  #!/bin/sh

  if ! command -v jq &> /dev/null; then
      echo "Error: This script requires jq. Please install it first."
      exit 1
  fi

  BASE_URL="https://api.anthropic.com/v1/messages/batches"

  has_more=true
  after_id=""

  while [ "$has_more" = true ]; do
      # Construct URL with after_id if it exists

      if [ -n "$after_id" ]; then
          url="${BASE_URL}?limit=20&after_id=${after_id}"
      else
          url="$BASE_URL?limit=20"
      fi

      response=$(curl -s "$url" \
                --header "x-api-key: $ANTHROPIC_API_KEY" \
                --header "anthropic-version: 2023-06-01")

      # Extract values using jq

      has_more=$(echo "$response" | jq -r '.has_more')
      after_id=$(echo "$response" | jq -r '.last_id')

      # Process and print each entry in the data array

      echo "$response" | jq -c '.data[]' | while read -r entry; do
          echo "$entry" | jq '.'
      done
  done
```
```java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.batches.*;

  public class BatchListExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Automatically fetches more pages as needed
          for (MessageBatch messageBatch : client.messages().batches().list(
                  BatchListParams.builder()
                          .limit(20)
                          .build()
          )) {
              System.out.println(messageBatch);
          }
      }
  }
```

### Retrieving batch results

Once batch processing has ended, each Messages request in the batch will have a result. There are 4 result types:

| Result Type | Description                                                                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded` | Request was successful. Includes the message result.                                                                                                                        |
| `errored`   | Request encountered an error and a message was not created. Possible errors include invalid requests and internal server errors. You will not be billed for these requests. |
| `canceled`  | User canceled the batch before this request could be sent to the model. You will not be billed for these requests.                                                          |
| `expired`   | Batch reached its 24 hour expiration before this request could be sent to the model. You will not be billed for these requests.                                             |

You will see an overview of your results with the batch's `request_counts`, which shows how many requests reached each of these four states.

Results of the batch are available for download at the `results_url` property on the Message Batch, and if the organization permission allows, in the Console. Because of the potentially large size of the results, it's recommended to [stream results](/en/api/retrieving-message-batch-results) back rather than download them all at once.
```bash
  #!/bin/sh
  curl "https://api.anthropic.com/v1/messages/batches/msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    | grep -o '"results_url":[[:space:]]*"[^"]*"' \
    | cut -d'"' -f4 \
    | while read -r url; do
      curl -s "$url" \
        --header "anthropic-version: 2023-06-01" \
        --header "x-api-key: $ANTHROPIC_API_KEY" \
        | sed 's/}{/}\n{/g' \
        | while IFS= read -r line
      do
        result_type=$(echo "$line" | sed -n 's/.*"result":[[:space:]]*{[[:space:]]*"type":[[:space:]]*"\([^"]*\)".*/\1/p')
        custom_id=$(echo "$line" | sed -n 's/.*"custom_id":[[:space:]]*"\([^"]*\)".*/\1/p')
        error_type=$(echo "$line" | sed -n 's/.*"error":[[:space:]]*{[[:space:]]*"type":[[:space:]]*"\([^"]*\)".*/\1/p')

        case "$result_type" in
          "succeeded")
            echo "Success! $custom_id"
            ;;
          "errored")
            if [ "$error_type" = "invalid_request" ]; then
              # Request body must be fixed before re-sending request

              echo "Validation error: $custom_id"
            else
              # Request can be retried directly

              echo "Server error: $custom_id"
            fi
            ;;
          "expired")
            echo "Expired: $line"
            ;;
        esac
      done
    done
```
```python
  import anthropic

  client = anthropic.Anthropic()

  # Stream results file in memory-efficient chunks, processing one at a time

  for result in client.messages.batches.results(
      "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  ):
      match result.result.type:
          case "succeeded":
              print(f"Success! {result.custom_id}")
          case "errored":
              if result.result.error.type == "invalid_request":
                  # Request body must be fixed before re-sending request

                  print(f"Validation error {result.custom_id}")
              else:
                  # Request can be retried directly

                  print(f"Server error {result.custom_id}")
          case "expired":
              print(f"Request expired {result.custom_id}")
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Stream results file in memory-efficient chunks, processing one at a time
  for await (const result of await anthropic.messages.batches.results(
      "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"
  )) {
    switch (result.result.type) {
      case 'succeeded':
        console.log(`Success! ${result.custom_id}`);
        break;
      case 'errored':
        if (result.result.error.type == "invalid_request") {
          // Request body must be fixed before re-sending request
          console.log(`Validation error: ${result.custom_id}`);
        } else {
          // Request can be retried directly
          console.log(`Server error: ${result.custom_id}`);
        }
        break;
      case 'expired':
        console.log(`Request expired: ${result.custom_id}`);
        break;
    }
  }
```
```java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.http.StreamResponse;
  import com.anthropic.models.messages.batches.MessageBatchIndividualResponse;
  import com.anthropic.models.messages.batches.BatchResultsParams;

  public class BatchResultsExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Stream results file in memory-efficient chunks, processing one at a time
          try (StreamResponse<MessageBatchIndividualResponse> streamResponse = client.messages()
                  .batches()
                  .resultsStreaming(
                          BatchResultsParams.builder()
                                  .messageBatchId("msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d")
                                  .build())) {

              streamResponse.stream().forEach(result -> {
                  if (result.result().isSucceeded()) {
                      System.out.println("Success! " + result.customId());
                  } else if (result.result().isErrored()) {
                      if (result.result().asErrored().error().error().isInvalidRequestError()) {
                          // Request body must be fixed before re-sending request
                          System.out.println("Validation error: " + result.customId());
                      } else {
                          // Request can be retried directly
                          System.out.println("Server error: " + result.customId());
                      }
                  } else if (result.result().isExpired()) {
                      System.out.println("Request expired: " + result.customId());
                  }
              });
          }
      }
  }
```

The results will be in `.jsonl` format, where each line is a valid JSON object representing the result of a single request in the Message Batch. For each streamed result, you can do something different depending on its `custom_id` and result type. Here is an example set of results:
```JSON .jsonl file theme={null}
{"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
{"custom_id":"my-first-request","result":{"type":"succeeded","message":{"id":"msg_01FqfsLoHwgeFbguDgpz48m7","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[{"type":"text","text":"Hello! How can I assist you today? Feel free to ask me any questions or let me know if there's anything you'd like to chat about."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"output_tokens":34}}}}
```
If your result has an error, its `result.error` will be set to our standard [error shape](/en/api/errors#error-shapes).

<Tip>
  **Batch results may not match input order**

  Batch results can be returned in any order, and may not match the ordering of requests when the batch was created. In the above example, the result for the second batch request is returned before the first. To correctly match results with their corresponding requests, always use the `custom_id` field.
</Tip>

### Canceling a Message Batch

You can cancel a Message Batch that is currently processing using the [cancel endpoint](/en/api/canceling-message-batches). Immediately after cancellation, a batch's `processing_status` will be `canceling`. You can use the same polling technique described above to wait until cancellation is finalized. Canceled batches end up with a status of `ended` and may contain partial results for requests that were processed before cancellation.
```python
  import anthropic

  client = anthropic.Anthropic()

  message_batch = client.messages.batches.cancel(
      MESSAGE_BATCH_ID,
  )
  print(message_batch)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const messageBatch = await anthropic.messages.batches.cancel(
      MESSAGE_BATCH_ID
  );
  console.log(messageBatch);
```
```bash
  #!/bin/sh
  curl --request POST https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/cancel \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01"
```
```java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.batches.*;

  public class BatchCancelExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          MessageBatch messageBatch = client.messages().batches().cancel(
                  BatchCancelParams.builder()
                          .messageBatchId(MESSAGE_BATCH_ID)
                          .build()
          );
          System.out.println(messageBatch);
      }
  }
```

The response will show the batch in a `canceling` state:
```JSON
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch",
  "processing_status": "canceling",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": "2024-09-24T18:39:03.114875Z",
  "results_url": null
}
```

### Using prompt caching with Message Batches

The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns.

To maximize the likelihood of cache hits in your batch requests:

1. Include identical `cache_control` blocks in every Message request within your batch
2. Maintain a steady stream of requests to prevent cache entries from expiring after their 5-minute lifetime
3. Structure your requests to share as much cached content as possible

Example of implementing prompt caching in a batch:
```bash
  curl https://api.anthropic.com/v1/messages/batches \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "requests": [
          {
              "custom_id": "my-first-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "system": [
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  "messages": [
                      {"role": "user", "content": "Analyze the major themes in Pride and Prejudice."}
                  ]
              }
          },
          {
              "custom_id": "my-second-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "system": [
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  "messages": [
                      {"role": "user", "content": "Write a summary of Pride and Prejudice."}
                  ]
              }
          }
      ]
  }'
```
```python
  import anthropic
  from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
  from anthropic.types.messages.batch_create_params import Request

  client = anthropic.Anthropic()

  message_batch = client.messages.batches.create(
      requests=[
          Request(
              custom_id="my-first-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  system=[
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  messages=[{
                      "role": "user",
                      "content": "Analyze the major themes in Pride and Prejudice."
                  }]
              )
          ),
          Request(
              custom_id="my-second-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  system=[
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  messages=[{
                      "role": "user",
                      "content": "Write a summary of Pride and Prejudice."
                  }]
              )
          )
      ]
  )
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const messageBatch = await anthropic.messages.batches.create({
    requests: [{
      custom_id: "my-first-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: {type: "ephemeral"}
          }
        ],
        messages: [
          {"role": "user", "content": "Analyze the major themes in Pride and Prejudice."}
        ]
      }
    }, {
      custom_id: "my-second-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: {type: "ephemeral"}
          }
        ],
        messages: [
          {"role": "user", "content": "Write a summary of Pride and Prejudice."}
        ]
      }
    }]
  });
```
```java
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.CacheControlEphemeral;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;
  import com.anthropic.models.messages.batches.*;

  public class BatchExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          BatchCreateParams createParams = BatchCreateParams.builder()
                  .addRequest(BatchCreateParams.Request.builder()
                          .customId("my-first-request")
                          .params(BatchCreateParams.Request.Params.builder()
                                  .model(Model.CLAUDE_OPUS_4_0)
                                  .maxTokens(1024)
                                  .systemOfTextBlockParams(List.of(
                                          TextBlockParam.builder()
                                                  .text("You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n")
                                                  .build(),
                                          TextBlockParam.builder()
                                                  .text("<the entire contents of Pride and Prejudice>")
                                                  .cacheControl(CacheControlEphemeral.builder().build())
                                                  .build()
                                  ))
                                  .addUserMessage("Analyze the major themes in Pride and Prejudice.")
                                  .build())
                          .build())
                  .addRequest(BatchCreateParams.Request.builder()
                          .customId("my-second-request")
                          .params(BatchCreateParams.Request.Params.builder()
                                  .model(Model.CLAUDE_OPUS_4_0)
                                  .maxTokens(1024)
                                  .systemOfTextBlockParams(List.of(
                                          TextBlockParam.builder()
                                                  .text("You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n")
                                                  .build(),
                                          TextBlockParam.builder()
                                                  .text("<the entire contents of Pride and Prejudice>")
                                                  .cacheControl(CacheControlEphemeral.builder().build())
                                                  .build()
                                  ))
                                  .addUserMessage("Write a summary of Pride and Prejudice.")
                                  .build())
                          .build())
                  .build();

          MessageBatch messageBatch = client.messages().batches().create(createParams);
      }
  }
```

In this example, both requests in the batch include identical system messages and the full text of Pride and Prejudice marked with `cache_control` to increase the likelihood of cache hits.

### Best practices for effective batching

To get the most out of the Batches API:

* Monitor batch processing status regularly and implement appropriate retry logic for failed requests.
* Use meaningful `custom_id` values to easily match results with requests, since order is not guaranteed.
* Consider breaking very large datasets into multiple batches for better manageability.
* Dry run a single request shape with the Messages API to avoid validation errors.

### Troubleshooting common issues

If experiencing unexpected behavior:

* Verify that the total batch request size doesn't exceed 256 MB. If the request size is too large, you may get a 413 `request_too_large` error.
* Check that you're using [supported models](#supported-models) for all requests in the batch.
* Ensure each request in the batch has a unique `custom_id`.
* Ensure that it has been less than 29 days since batch `created_at` (not processing `ended_at`) time. If over 29 days have passed, results will no longer be viewable.
* Confirm that the batch has not been canceled.

Note that the failure of one request in a batch does not affect the processing of other requests.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
