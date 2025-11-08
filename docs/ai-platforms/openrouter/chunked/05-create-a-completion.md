**Navigation:** [← Previous](./04-list-all-models-and-their-properties.md) | [Index](./index.md) | [Next →](./06-crypto-api.md)

---

# Create a completion

POST https://openrouter.ai/api/v1/completions
Content-Type: application/json

Creates a completion for the provided prompt and parameters. Supports both streaming and non-streaming modes.

Reference: https://openrouter.ai/docs/api-reference/completions/create-completions

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a completion
  version: endpoint_completions.createCompletions
paths:
  /completions:
    post:
      operationId: create-completions
      summary: Create a completion
      description: >-
        Creates a completion for the provided prompt and parameters. Supports
        both streaming and non-streaming modes.
      tags:
        - - subpackage_completions
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful completion response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompletionResponse'
        '400':
          description: Bad request - invalid parameters
          content: {}
        '401':
          description: Unauthorized - invalid API key
          content: {}
        '429':
          description: Too many requests - rate limit exceeded
          content: {}
        '500':
          description: Internal server error
          content: {}
      requestBody:
        description: Completion request parameters
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompletionCreateParams'
components:
  schemas:
    ModelName:
      type: string
    CompletionCreateParamsPrompt:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
        - type: array
          items:
            type: number
            format: double
        - type: array
          items:
            type: array
            items:
              type: number
              format: double
    CompletionCreateParamsStop:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
    CompletionCreateParamsStreamOptions:
      type: object
      properties:
        include_usage:
          type:
            - boolean
            - 'null'
    CompletionCreateParamsResponseFormat0:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: text
      required:
        - type
    CompletionCreateParamsResponseFormat1:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_object
      required:
        - type
    JSONSchemaConfig:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        schema:
          type: object
          additionalProperties:
            description: Any type
        strict:
          type:
            - boolean
            - 'null'
      required:
        - name
    ResponseFormatJSONSchema:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_schema
        json_schema:
          $ref: '#/components/schemas/JSONSchemaConfig'
      required:
        - type
        - json_schema
    ResponseFormatTextGrammar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: grammar
        grammar:
          type: string
      required:
        - type
        - grammar
    CompletionCreateParamsResponseFormat4:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: python
      required:
        - type
    CompletionCreateParamsResponseFormat:
      oneOf:
        - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat0'
        - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat1'
        - $ref: '#/components/schemas/ResponseFormatJSONSchema'
        - $ref: '#/components/schemas/ResponseFormatTextGrammar'
        - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat4'
    CompletionCreateParams:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/ModelName'
        models:
          type: array
          items:
            $ref: '#/components/schemas/ModelName'
        prompt:
          $ref: '#/components/schemas/CompletionCreateParamsPrompt'
        best_of:
          type:
            - integer
            - 'null'
        echo:
          type:
            - boolean
            - 'null'
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
        logit_bias:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
        logprobs:
          type:
            - integer
            - 'null'
        max_tokens:
          type:
            - integer
            - 'null'
        'n':
          type:
            - integer
            - 'null'
        presence_penalty:
          type:
            - number
            - 'null'
          format: double
        seed:
          type:
            - integer
            - 'null'
        stop:
          oneOf:
            - $ref: '#/components/schemas/CompletionCreateParamsStop'
            - type: 'null'
        stream:
          type: boolean
        stream_options:
          oneOf:
            - $ref: '#/components/schemas/CompletionCreateParamsStreamOptions'
            - type: 'null'
        suffix:
          type:
            - string
            - 'null'
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        user:
          type: string
        metadata:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        response_format:
          oneOf:
            - $ref: '#/components/schemas/CompletionCreateParamsResponseFormat'
            - type: 'null'
      required:
        - prompt
    CompletionLogprobs:
      type: object
      properties:
        tokens:
          type: array
          items:
            type: string
        token_logprobs:
          type: array
          items:
            type: number
            format: double
        top_logprobs:
          type:
            - array
            - 'null'
          items:
            type: object
            additionalProperties:
              type: number
              format: double
        text_offset:
          type: array
          items:
            type: number
            format: double
      required:
        - tokens
        - token_logprobs
        - top_logprobs
        - text_offset
    CompletionFinishReason:
      type: string
      enum:
        - value: stop
        - value: length
        - value: content_filter
    CompletionChoice:
      type: object
      properties:
        text:
          type: string
        index:
          type: number
          format: double
        logprobs:
          oneOf:
            - $ref: '#/components/schemas/CompletionLogprobs'
            - type: 'null'
        finish_reason:
          $ref: '#/components/schemas/CompletionFinishReason'
      required:
        - text
        - index
        - logprobs
        - finish_reason
    CompletionUsage:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
    CompletionResponse:
      type: object
      properties:
        id:
          type: string
        object:
          type: string
          enum:
            - type: stringLiteral
              value: text_completion
        created:
          type: number
          format: double
        model:
          type: string
        system_fingerprint:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/CompletionChoice'
        usage:
          $ref: '#/components/schemas/CompletionUsage'
      required:
        - id
        - object
        - created
        - model
        - choices

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/completions"

payload = { "prompt": "string" }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/completions';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"prompt":"string"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/completions"

	payload := strings.NewReader("{\n  \"prompt\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/completions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/completions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"prompt\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/completions', [
  'body' => '{
  "prompt": "string"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/completions");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["prompt": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/completions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# TypeScript SDK

> Complete guide to using the OpenRouter TypeScript SDK. Learn how to integrate AI models into your TypeScript applications.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

The OpenRouter TypeScript SDK is a type-safe toolkit for building AI applications with access to 300+ language models through a unified API.

## Why use the OpenRouter SDK?

Integrating AI models into applications involves handling different provider APIs, managing model-specific requirements, and avoiding common implementation mistakes. The OpenRouter SDK standardizes these integrations and protects you from footguns.

```typescript
import OpenRouter from '@openrouter/sdk';

const client = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY
});

const response = await client.chat.completions.create({
  model: "minimax/minimax-m2",
  messages: [
    { role: "user", content: "Explain quantum computing" }
  ]
});
```

The SDK provides three core benefits:

### Auto-generated from API specifications

The SDK is automatically generated from OpenRouter's OpenAPI specs and updated with every API change. New models, parameters, and features appear in your IDE autocomplete immediately. No manual updates. No version drift.

```typescript
// When new models launch, they're available instantly
const response = await client.chat.completions.create({
  model: "minimax/minimax-m2",
});
```

### Type-safe by default

Every parameter, response field, and configuration option is fully typed. Invalid configurations are caught at compile time, not in production.

```typescript
const response = await client.chat.completions.create({
  model: "minimax/minimax-m2",
  messages: [
    { role: "user", content: "Hello" }
    // ← Your IDE validates message structure
  ],
  temperature: 0.7, // ← Type-checked
  stream: true      // ← Response type changes based on this
});
```

**Actionable error messages:**

```typescript
// Instead of generic errors, get specific guidance:
// "Model 'openai/o1-preview' requires at least 2 messages.
//  You provided 1 message. Add a system or user message."
```

**Type-safe streaming:**

```typescript
const stream = await client.chat.completions.create({
  model: "minimax/minimax-m2",
  messages: [{ role: "user", content: "Write a story" }],
  stream: true
});

for await (const chunk of stream) {
  // Full type information for streaming responses
  const content = chunk.choices[0]?.delta?.content;
}
```

## Installation

```bash
npm install @openrouter/sdk
```

Get your API key from [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).

## Quick start

```typescript
import OpenRouter from '@openrouter/sdk';

const client = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY
});

const response = await client.chat.completions.create({
  model: "minimax/minimax-m2",
  messages: [
    { role: "user", content: "Hello!" }
  ]
});

console.log(response.choices[0].message.content);
```


# Analytics - TypeScript SDK

> Analytics method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*analytics*)

## Overview

Analytics and usage endpoints

### Available Operations

* [getUserActivity](#getuseractivity) - Get user activity grouped by endpoint

## getUserActivity

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days

### Example Usage

{/* UsageSnippet language="typescript" operationID="getUserActivity" method="get" path="/activity" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.analytics.getUserActivity();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { analyticsGetUserActivity } from "@openrouter/sdk/funcs/analyticsGetUserActivity.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await analyticsGetUserActivity(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("analyticsGetUserActivity failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useAnalyticsGetUserActivity,
  useAnalyticsGetUserActivitySuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchAnalyticsGetUserActivity,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAnalyticsGetUserActivity,
  invalidateAllAnalyticsGetUserActivity,
} from "@openrouter/sdk/react-query/analyticsGetUserActivity.js";
```

### Parameters

| Parameter              | Type                                                                                         | Required             | Description                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.GetUserActivityRequest](/docs/sdks/typescript/operations/getuseractivityrequest) | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                               | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)      | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                         | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetUserActivityResponse](/docs/sdks/typescript/operations/getuseractivityresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError     | 400         | application/json |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.ForbiddenResponseError      | 403         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# APIKeys - TypeScript SDK

> APIKeys method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*apiKeys*)

## Overview

API key management endpoints

### Available Operations

* [list](#list) - List API keys
* [create](#create) - Create a new API key
* [update](#update) - Update an API key
* [delete](#delete) - Delete an API key
* [get](#get) - Get a single API key
* [getCurrentKeyMetadata](#getcurrentkeymetadata) - Get current API key

## list

List API keys

### Example Usage

{/* UsageSnippet language="typescript" operationID="list" method="get" path="/keys" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.list();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysList } from "@openrouter/sdk/funcs/apiKeysList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysList failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useApiKeysList,
  useApiKeysListSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchApiKeysList,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateApiKeysList,
  invalidateAllApiKeysList,
} from "@openrouter/sdk/react-query/apiKeysList.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.ListRequest](/docs/sdks/typescript/operations/listrequest)                  | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ListResponse](/docs/sdks/typescript/operations/listresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |

## create

Create a new API key

### Example Usage

{/* UsageSnippet language="typescript" operationID="createKeys" method="post" path="/keys" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.create({
    name: "My New API Key",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysCreate } from "@openrouter/sdk/funcs/apiKeysCreate.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysCreate(openRouter, {
    name: "My New API Key",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysCreate failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useApiKeysCreateMutation
} from "@openrouter/sdk/react-query/apiKeysCreate.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.CreateKeysRequest](/docs/sdks/typescript/operations/createkeysrequest)      | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CreateKeysResponse](/docs/sdks/typescript/operations/createkeysresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError      | 400         | application/json |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |

## update

Update an API key

### Example Usage

{/* UsageSnippet language="typescript" operationID="updateKeys" method="patch" path="/keys/{hash}" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.update({
    hash: "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",
    requestBody: {},
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysUpdate } from "@openrouter/sdk/funcs/apiKeysUpdate.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysUpdate(openRouter, {
    hash: "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",
    requestBody: {},
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysUpdate failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useApiKeysUpdateMutation
} from "@openrouter/sdk/react-query/apiKeysUpdate.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.UpdateKeysRequest](/docs/sdks/typescript/operations/updatekeysrequest)      | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.UpdateKeysResponse](/docs/sdks/typescript/operations/updatekeysresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError      | 400         | application/json |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.NotFoundResponseError        | 404         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |

## delete

Delete an API key

### Example Usage

{/* UsageSnippet language="typescript" operationID="deleteKeys" method="delete" path="/keys/{hash}" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.delete({
    hash: "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",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysDelete } from "@openrouter/sdk/funcs/apiKeysDelete.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysDelete(openRouter, {
    hash: "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",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysDelete failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useApiKeysDeleteMutation
} from "@openrouter/sdk/react-query/apiKeysDelete.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.DeleteKeysRequest](/docs/sdks/typescript/operations/deletekeysrequest)      | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.DeleteKeysResponse](/docs/sdks/typescript/operations/deletekeysresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.NotFoundResponseError        | 404         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |

## get

Get a single API key

### Example Usage

{/* UsageSnippet language="typescript" operationID="getKey" method="get" path="/keys/{hash}" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.get({
    hash: "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",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysGet } from "@openrouter/sdk/funcs/apiKeysGet.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysGet(openRouter, {
    hash: "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",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysGet failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useApiKeysGet,
  useApiKeysGetSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchApiKeysGet,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateApiKeysGet,
  invalidateAllApiKeysGet,
} from "@openrouter/sdk/react-query/apiKeysGet.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.GetKeyRequest](/docs/sdks/typescript/operations/getkeyrequest)              | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetKeyResponse](/docs/sdks/typescript/operations/getkeyresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.NotFoundResponseError        | 404         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |

## getCurrentKeyMetadata

Get information on the API key associated with the current authentication session

### Example Usage

{/* UsageSnippet language="typescript" operationID="getCurrentKey" method="get" path="/key" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.getCurrentKeyMetadata();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysGetCurrentKeyMetadata } from "@openrouter/sdk/funcs/apiKeysGetCurrentKeyMetadata.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysGetCurrentKeyMetadata(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysGetCurrentKeyMetadata failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useApiKeysGetCurrentKeyMetadata,
  useApiKeysGetCurrentKeyMetadataSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchApiKeysGetCurrentKeyMetadata,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllApiKeysGetCurrentKeyMetadata,
} from "@openrouter/sdk/react-query/apiKeysGetCurrentKeyMetadata.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetCurrentKeyResponse](/docs/sdks/typescript/operations/getcurrentkeyresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# Chat - TypeScript SDK

> Chat method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*chat*)

## Overview

### Available Operations

* [send](#send) - Create a chat completion

## send

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

### Example Usage

{/* UsageSnippet language="typescript" operationID="sendChatCompletionRequest" method="post" path="/chat/completions" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.chat.send({
    messages: [],
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { chatSend } from "@openrouter/sdk/funcs/chatSend.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await chatSend(openRouter, {
    messages: [],
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("chatSend failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useChatSendMutation
} from "@openrouter/sdk/react-query/chatSend.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [models.ChatGenerationParams](/docs/sdks/typescript/models/chatgenerationparams)        | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SendChatCompletionRequestResponse](/docs/sdks/typescript/operations/sendchatcompletionrequestresponse)>**

### Errors

| Error Type                    | Status Code   | Content Type     |
| ----------------------------- | ------------- | ---------------- |
| errors.ChatError              | 400, 401, 429 | application/json |
| errors.ChatError              | 500           | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX      | \*/\*            |


# Completions - TypeScript SDK

> Completions method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*completions*)

## Overview

### Available Operations

* [generate](#generate) - Create a completion

## generate

Creates a completion for the provided prompt and parameters. Supports both streaming and non-streaming modes.

### Example Usage

{/* UsageSnippet language="typescript" operationID="createCompletions" method="post" path="/completions" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.completions.generate({
    prompt: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { completionsGenerate } from "@openrouter/sdk/funcs/completionsGenerate.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await completionsGenerate(openRouter, {
    prompt: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("completionsGenerate failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useCompletionsGenerateMutation
} from "@openrouter/sdk/react-query/completionsGenerate.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [models.CompletionCreateParams](/docs/sdks/typescript/models/completioncreateparams)    | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[models.CompletionResponse](/docs/sdks/typescript/models/completionresponse)>**

### Errors

| Error Type                    | Status Code   | Content Type     |
| ----------------------------- | ------------- | ---------------- |
| errors.ChatError              | 400, 401, 429 | application/json |
| errors.ChatError              | 500           | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX      | \*/\*            |


# Credits - TypeScript SDK

> Credits method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*credits*)

## Overview

Credit management endpoints

### Available Operations

* [getCredits](#getcredits) - Get remaining credits
* [createCoinbaseCharge](#createcoinbasecharge) - Create a Coinbase charge for crypto payment

## getCredits

Get total credits purchased and used for the authenticated user

### Example Usage

{/* UsageSnippet language="typescript" operationID="getCredits" method="get" path="/credits" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.credits.getCredits();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { creditsGetCredits } from "@openrouter/sdk/funcs/creditsGetCredits.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await creditsGetCredits(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("creditsGetCredits failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useCreditsGetCredits,
  useCreditsGetCreditsSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchCreditsGetCredits,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllCreditsGetCredits,
} from "@openrouter/sdk/react-query/creditsGetCredits.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetCreditsResponse](/docs/sdks/typescript/operations/getcreditsresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.ForbiddenResponseError      | 403         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## createCoinbaseCharge

Create a Coinbase charge for crypto payment

### Example Usage

{/* UsageSnippet language="typescript" operationID="createCoinbaseCharge" method="post" path="/credits/coinbase" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter();

async function run() {
  const result = await openRouter.credits.createCoinbaseCharge({
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  }, {
    amount: 100,
    sender: "0x1234567890123456789012345678901234567890",
    chainId: 1,
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { creditsCreateCoinbaseCharge } from "@openrouter/sdk/funcs/creditsCreateCoinbaseCharge.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore();

async function run() {
  const res = await creditsCreateCoinbaseCharge(openRouter, {
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  }, {
    amount: 100,
    sender: "0x1234567890123456789012345678901234567890",
    chainId: 1,
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("creditsCreateCoinbaseCharge failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useCreditsCreateCoinbaseChargeMutation
} from "@openrouter/sdk/react-query/creditsCreateCoinbaseCharge.js";
```

### Parameters

| Parameter              | Type                                                                                                     | Required             | Description                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [models.CreateChargeRequest](/docs/sdks/typescript/models/createchargerequest)                           | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `security`             | [operations.CreateCoinbaseChargeSecurity](/docs/sdks/typescript/operations/createcoinbasechargesecurity) | :heavy\_check\_mark: | The security requirements to use for the request.                                                                                                                              |
| `options`              | RequestOptions                                                                                           | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                  | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                                     | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CreateCoinbaseChargeResponse](/docs/sdks/typescript/operations/createcoinbasechargeresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError      | 400         | application/json |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |


# Embeddings - TypeScript SDK

> Embeddings method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*embeddings*)

## Overview

Text embedding endpoints

### Available Operations

* [generate](#generate) - Submit an embedding request

## generate

Submits an embedding request to the embeddings router

### Example Usage

{/* UsageSnippet language="typescript" operationID="createEmbeddings" method="post" path="/embeddings" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.embeddings.generate({
    input: "<value>",
    model: "Taurus",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { embeddingsGenerate } from "@openrouter/sdk/funcs/embeddingsGenerate.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await embeddingsGenerate(openRouter, {
    input: "<value>",
    model: "Taurus",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("embeddingsGenerate failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useEmbeddingsGenerateMutation
} from "@openrouter/sdk/react-query/embeddingsGenerate.js";
```

### Parameters

| Parameter              | Type                                                                                           | Required             | Description                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.CreateEmbeddingsRequest](/docs/sdks/typescript/operations/createembeddingsrequest) | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                                 | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)        | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                           | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CreateEmbeddingsResponse](/docs/sdks/typescript/operations/createembeddingsresponse)>**

### Errors

| Error Type                             | Status Code | Content Type     |
| -------------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError         | 400         | application/json |
| errors.UnauthorizedResponseError       | 401         | application/json |
| errors.PaymentRequiredResponseError    | 402         | application/json |
| errors.NotFoundResponseError           | 404         | application/json |
| errors.TooManyRequestsResponseError    | 429         | application/json |
| errors.InternalServerResponseError     | 500         | application/json |
| errors.BadGatewayResponseError         | 502         | application/json |
| errors.ServiceUnavailableResponseError | 503         | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524         | application/json |
| errors.ProviderOverloadedResponseError | 529         | application/json |
| errors.OpenRouterDefaultError          | 4XX, 5XX    | \*/\*            |


# Endpoints - TypeScript SDK

> Endpoints method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*endpoints*)

## Overview

Endpoint information

### Available Operations

* [list](#list) - List all endpoints for a model
* [listZdrEndpoints](#listzdrendpoints) - Preview the impact of ZDR on the available endpoints

## list

List all endpoints for a model

### Example Usage

{/* UsageSnippet language="typescript" operationID="listEndpoints" method="get" path="/models/{author}/{slug}/endpoints" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.endpoints.list({
    author: "<value>",
    slug: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { endpointsList } from "@openrouter/sdk/funcs/endpointsList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await endpointsList(openRouter, {
    author: "<value>",
    slug: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("endpointsList failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useEndpointsList,
  useEndpointsListSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchEndpointsList,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateEndpointsList,
  invalidateAllEndpointsList,
} from "@openrouter/sdk/react-query/endpointsList.js";
```

### Parameters

| Parameter              | Type                                                                                     | Required             | Description                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.ListEndpointsRequest](/docs/sdks/typescript/operations/listendpointsrequest) | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                           | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)  | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                     | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ListEndpointsResponse](/docs/sdks/typescript/operations/listendpointsresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.NotFoundResponseError       | 404         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## listZdrEndpoints

Preview the impact of ZDR on the available endpoints

### Example Usage

{/* UsageSnippet language="typescript" operationID="listEndpointsZdr" method="get" path="/endpoints/zdr" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.endpoints.listZdrEndpoints();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { endpointsListZdrEndpoints } from "@openrouter/sdk/funcs/endpointsListZdrEndpoints.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await endpointsListZdrEndpoints(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("endpointsListZdrEndpoints failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useEndpointsListZdrEndpoints,
  useEndpointsListZdrEndpointsSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchEndpointsListZdrEndpoints,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllEndpointsListZdrEndpoints,
} from "@openrouter/sdk/react-query/endpointsListZdrEndpoints.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ListEndpointsZdrResponse](/docs/sdks/typescript/operations/listendpointszdrresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# Generations - TypeScript SDK

> Generations method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*generations*)

## Overview

Generation history endpoints

### Available Operations

* [getGeneration](#getgeneration) - Get request & usage metadata for a generation

## getGeneration

Get request & usage metadata for a generation

### Example Usage

{/* UsageSnippet language="typescript" operationID="getGeneration" method="get" path="/generation" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.generations.getGeneration({
    id: "<id>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { generationsGetGeneration } from "@openrouter/sdk/funcs/generationsGetGeneration.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await generationsGetGeneration(openRouter, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("generationsGetGeneration failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useGenerationsGetGeneration,
  useGenerationsGetGenerationSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchGenerationsGetGeneration,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateGenerationsGetGeneration,
  invalidateAllGenerationsGetGeneration,
} from "@openrouter/sdk/react-query/generationsGetGeneration.js";
```

### Parameters

| Parameter              | Type                                                                                     | Required             | Description                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.GetGenerationRequest](/docs/sdks/typescript/operations/getgenerationrequest) | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                           | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)  | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                     | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetGenerationResponse](/docs/sdks/typescript/operations/getgenerationresponse)>**

### Errors

| Error Type                             | Status Code | Content Type     |
| -------------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError       | 401         | application/json |
| errors.PaymentRequiredResponseError    | 402         | application/json |
| errors.NotFoundResponseError           | 404         | application/json |
| errors.TooManyRequestsResponseError    | 429         | application/json |
| errors.InternalServerResponseError     | 500         | application/json |
| errors.BadGatewayResponseError         | 502         | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524         | application/json |
| errors.ProviderOverloadedResponseError | 529         | application/json |
| errors.OpenRouterDefaultError          | 4XX, 5XX    | \*/\*            |


# Models - TypeScript SDK

> Models method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*models*)

## Overview

Model information endpoints

### Available Operations

* [count](#count) - Get total count of available models
* [list](#list) - List all models and their properties
* [listEmbeddings](#listembeddings) - List all embeddings models
* [listForUser](#listforuser) - List models filtered by user provider preferences

## count

Get total count of available models

### Example Usage

{/* UsageSnippet language="typescript" operationID="listModelsCount" method="get" path="/models/count" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.models.count();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { modelsCount } from "@openrouter/sdk/funcs/modelsCount.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await modelsCount(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("modelsCount failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useModelsCount,
  useModelsCountSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchModelsCount,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllModelsCount,
} from "@openrouter/sdk/react-query/modelsCount.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[models.ModelsCountResponse](/docs/sdks/typescript/models/modelscountresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## list

List all models and their properties

### Example Usage

{/* UsageSnippet language="typescript" operationID="getModels" method="get" path="/models" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.models.list();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { modelsList } from "@openrouter/sdk/funcs/modelsList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await modelsList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("modelsList failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useModelsList,
  useModelsListSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchModelsList,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateModelsList,
  invalidateAllModelsList,
} from "@openrouter/sdk/react-query/modelsList.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.GetModelsRequest](/docs/sdks/typescript/operations/getmodelsrequest)        | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[models.ModelsListResponse](/docs/sdks/typescript/models/modelslistresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError     | 400         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## listEmbeddings

Returns a list of all available embeddings models and their properties

### Example Usage

{/* UsageSnippet language="typescript" operationID="listModelsEmbeddings" method="get" path="/models/embeddings" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.models.listEmbeddings();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { modelsListEmbeddings } from "@openrouter/sdk/funcs/modelsListEmbeddings.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await modelsListEmbeddings(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("modelsListEmbeddings failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useModelsListEmbeddings,
  useModelsListEmbeddingsSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchModelsListEmbeddings,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllModelsListEmbeddings,
} from "@openrouter/sdk/react-query/modelsListEmbeddings.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[models.ModelsListResponse](/docs/sdks/typescript/models/modelslistresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError     | 400         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## listForUser

List models filtered by user provider preferences

### Example Usage

{/* UsageSnippet language="typescript" operationID="listModelsUser" method="get" path="/models/user" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter();

async function run() {
  const result = await openRouter.models.listForUser({
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { modelsListForUser } from "@openrouter/sdk/funcs/modelsListForUser.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore();

async function run() {
  const res = await modelsListForUser(openRouter, {
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("modelsListForUser failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useModelsListForUser,
  useModelsListForUserSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchModelsListForUser,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllModelsListForUser,
} from "@openrouter/sdk/react-query/modelsListForUser.js";
```

### Parameters

| Parameter              | Type                                                                                         | Required             | Description                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`             | [operations.ListModelsUserSecurity](/docs/sdks/typescript/operations/listmodelsusersecurity) | :heavy\_check\_mark: | The security requirements to use for the request.                                                                                                                              |
| `options`              | RequestOptions                                                                               | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)      | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                         | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[models.ModelsListResponse](/docs/sdks/typescript/models/modelslistresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# OAuth - TypeScript SDK

> OAuth method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*oAuth*)

## Overview

OAuth authentication endpoints

### Available Operations

* [exchangeAuthCodeForAPIKey](#exchangeauthcodeforapikey) - Exchange authorization code for API key
* [createAuthCode](#createauthcode) - Create authorization code

## exchangeAuthCodeForAPIKey

Exchange an authorization code from the PKCE flow for a user-controlled API key

### Example Usage

{/* UsageSnippet language="typescript" operationID="exchangeAuthCodeForAPIKey" method="post" path="/auth/keys" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.oAuth.exchangeAuthCodeForAPIKey({
    code: "auth_code_abc123def456",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { oAuthExchangeAuthCodeForAPIKey } from "@openrouter/sdk/funcs/oAuthExchangeAuthCodeForAPIKey.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await oAuthExchangeAuthCodeForAPIKey(openRouter, {
    code: "auth_code_abc123def456",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("oAuthExchangeAuthCodeForAPIKey failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useOAuthExchangeAuthCodeForAPIKeyMutation
} from "@openrouter/sdk/react-query/oAuthExchangeAuthCodeForAPIKey.js";
```

### Parameters

| Parameter              | Type                                                                                                             | Required             | Description                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.ExchangeAuthCodeForAPIKeyRequest](/docs/sdks/typescript/operations/exchangeauthcodeforapikeyrequest) | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                                                   | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                          | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                                             | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ExchangeAuthCodeForAPIKeyResponse](/docs/sdks/typescript/operations/exchangeauthcodeforapikeyresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError     | 400         | application/json |
| errors.ForbiddenResponseError      | 403         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## createAuthCode

Create an authorization code for the PKCE flow to generate a user-controlled API key

### Example Usage

{/* UsageSnippet language="typescript" operationID="createAuthKeysCode" method="post" path="/auth/keys/code" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.oAuth.createAuthCode({
    callbackUrl: "https://myapp.com/auth/callback",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { oAuthCreateAuthCode } from "@openrouter/sdk/funcs/oAuthCreateAuthCode.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await oAuthCreateAuthCode(openRouter, {
    callbackUrl: "https://myapp.com/auth/callback",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("oAuthCreateAuthCode failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useOAuthCreateAuthCodeMutation
} from "@openrouter/sdk/react-query/oAuthCreateAuthCode.js";
```

### Parameters

| Parameter              | Type                                                                                               | Required             | Description                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.CreateAuthKeysCodeRequest](/docs/sdks/typescript/operations/createauthkeyscoderequest) | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                                     | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)            | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                               | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CreateAuthKeysCodeResponse](/docs/sdks/typescript/operations/createauthkeyscoderesponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError     | 400         | application/json |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# ParametersT - TypeScript SDK

> ParametersT method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*parameters*)

## Overview

Parameters endpoints

### Available Operations

* [getParameters](#getparameters) - Get a model's supported parameters and data about which are most popular

## getParameters

Get a model's supported parameters and data about which are most popular

### Example Usage

{/* UsageSnippet language="typescript" operationID="getParameters" method="get" path="/parameters/{author}/{slug}" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter();

async function run() {
  const result = await openRouter.parameters.getParameters({
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  }, {
    author: "<value>",
    slug: "<value>",
    provider: "Google AI Studio",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { parametersGetParameters } from "@openrouter/sdk/funcs/parametersGetParameters.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore();

async function run() {
  const res = await parametersGetParameters(openRouter, {
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  }, {
    author: "<value>",
    slug: "<value>",
    provider: "Google AI Studio",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("parametersGetParameters failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useParametersGetParameters,
  useParametersGetParametersSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchParametersGetParameters,
  
  // Utilities to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateParametersGetParameters,
  invalidateAllParametersGetParameters,
} from "@openrouter/sdk/react-query/parametersGetParameters.js";
```

### Parameters

| Parameter              | Type                                                                                       | Required             | Description                                                                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [operations.GetParametersRequest](/docs/sdks/typescript/operations/getparametersrequest)   | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `security`             | [operations.GetParametersSecurity](/docs/sdks/typescript/operations/getparameterssecurity) | :heavy\_check\_mark: | The security requirements to use for the request.                                                                                                                              |
| `options`              | RequestOptions                                                                             | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)    | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                       | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetParametersResponse](/docs/sdks/typescript/operations/getparametersresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.NotFoundResponseError       | 404         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# Providers - TypeScript SDK

> Providers method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*providers*)

## Overview

Provider information endpoints

### Available Operations

* [list](#list) - List all providers

## list

List all providers

### Example Usage

{/* UsageSnippet language="typescript" operationID="listProviders" method="get" path="/providers" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.providers.list();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { providersList } from "@openrouter/sdk/funcs/providersList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await providersList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("providersList failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Query hooks for fetching data.
  useProvidersList,
  useProvidersListSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchProvidersList,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllProvidersList,
} from "@openrouter/sdk/react-query/providersList.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ListProvidersResponse](/docs/sdks/typescript/operations/listprovidersresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


# Responses - TypeScript SDK

> Responses method documentation for the OpenRouter TypeScript SDK. Learn how to use this API endpoint with code examples.

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

(*beta.responses*)

## Overview

beta.responses endpoints

### Available Operations

* [send](#send) - Create a response

## send

Creates a streaming or non-streaming response using OpenResponses API format

### Example Usage

{/* UsageSnippet language="typescript" operationID="createResponses" method="post" path="/responses" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.beta.responses.send({});

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { betaResponsesSend } from "@openrouter/sdk/funcs/betaResponsesSend.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await betaResponsesSend(openRouter, {});
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("betaResponsesSend failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md

```tsx
import {
  // Mutation hook for triggering the API call.
  useBetaResponsesSendMutation
} from "@openrouter/sdk/react-query/betaResponsesSend.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [models.OpenResponsesRequest](/docs/sdks/typescript/models/openresponsesrequest)        | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CreateResponsesResponse](/docs/sdks/typescript/operations/createresponsesresponse)>**

### Errors

| Error Type                              | Status Code | Content Type     |
| --------------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError          | 400         | application/json |
| errors.UnauthorizedResponseError        | 401         | application/json |
| errors.PaymentRequiredResponseError     | 402         | application/json |
| errors.NotFoundResponseError            | 404         | application/json |
| errors.RequestTimeoutResponseError      | 408         | application/json |
| errors.PayloadTooLargeResponseError     | 413         | application/json |
| errors.UnprocessableEntityResponseError | 422         | application/json |
| errors.TooManyRequestsResponseError     | 429         | application/json |
| errors.InternalServerResponseError      | 500         | application/json |
| errors.BadGatewayResponseError          | 502         | application/json |
| errors.ServiceUnavailableResponseError  | 503         | application/json |
| errors.EdgeNetworkTimeoutResponseError  | 524         | application/json |
| errors.ProviderOverloadedResponseError  | 529         | application/json |
| errors.OpenRouterDefaultError           | 4XX, 5XX    | \*/\*            |


# BYOK

> Learn how to use your existing AI provider keys with OpenRouter. Integrate your own API keys while leveraging OpenRouter's unified interface and features.

## Bring your own API Keys

OpenRouter supports both OpenRouter credits and the option to bring your own provider keys (BYOK).

When you use OpenRouter credits, your rate limits for each provider are managed by OpenRouter.

Using provider keys enables direct control over rate limits and costs via your provider account.

Your provider keys are securely encrypted and used for all requests routed through the specified provider.

Manage keys in your [account settings](/settings/integrations).

The cost of using custom provider keys on OpenRouter is **{bn(openRouterBYOKFee.fraction).times(100).toString()}% of what the same model/provider would cost normally on OpenRouter** and will be deducted from your OpenRouter credits.
This fee is waived for the first {toHumanNumber(BYOK_FEE_MONTHLY_REQUEST_THRESHOLD)} BYOK requests per-month.

### Key Priority and Fallback

OpenRouter always prioritizes using your provider keys when available. By default, if your key encounters a rate limit or failure, OpenRouter will fall back to using shared OpenRouter credits.

You can configure individual keys with "Always use this key" to prevent any fallback to OpenRouter credits. When this option is enabled, OpenRouter will only use your key for requests to that provider, which may result in rate limit errors if your key is exhausted, but ensures all requests go through your account.

### Azure API Keys

To use Azure AI Services with OpenRouter, you'll need to provide your Azure API key configuration in JSON format. Each key configuration requires the following fields:

```json
{
  "model_slug": "the-openrouter-model-slug",
  "endpoint_url": "https://<resource>.services.ai.azure.com/deployments/<model-id>/chat/completions?api-version=<api-version>",
  "api_key": "your-azure-api-key",
  "model_id": "the-azure-model-id"
}
```

You can find these values in your Azure AI Services resource:

1. **endpoint\_url**: Navigate to your Azure AI Services resource in the Azure portal. In the "Overview" section, you'll find your endpoint URL. Make sure to append `/chat/completions` to the base URL. You can read more in the [Azure Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/concepts/endpoints?tabs=python).

2. **api\_key**: In the same "Overview" section of your Azure AI Services resource, you can find your API key under "Keys and Endpoint".

3. **model\_id**: This is the name of your model deployment in Azure AI Services.

4. **model\_slug**: This is the OpenRouter model identifier you want to use this key for.

Since Azure supports multiple model deployments, you can provide an array of configurations for different models:

```json
[
  {
    "model_slug": "mistralai/mistral-large",
    "endpoint_url": "https://example-project.openai.azure.com/openai/deployments/mistral-large/chat/completions?api-version=2024-08-01-preview",
    "api_key": "your-azure-api-key",
    "model_id": "mistral-large"
  },
  {
    "model_slug": "openai/gpt-4o",
    "endpoint_url": "https://example-project.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview",
    "api_key": "your-azure-api-key",
    "model_id": "gpt-4o"
  }
]
```

Make sure to replace the url with your own project url. Also the url should end with /chat/completions with the api version that you would like to use.

### AWS Bedrock API Keys

To use Amazon Bedrock with OpenRouter, you can authenticate using either Bedrock API keys or traditional AWS credentials.

#### Option 1: Bedrock API Keys (Recommended)

Amazon Bedrock API keys provide a simpler authentication method. Simply provide your Bedrock API key as a string:

```
your-bedrock-api-key-here
```

**Note:** Bedrock API keys are tied to a specific AWS region and cannot be used to change regions. If you need to use models in different regions, use the AWS credentials option below.

You can generate Bedrock API keys in the AWS Management Console. Learn more in the [Amazon Bedrock API keys documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html).

#### Option 2: AWS Credentials

Alternatively, you can use traditional AWS credentials in JSON format. This option allows you to specify the region and provides more flexibility:

```json
{
  "accessKeyId": "your-aws-access-key-id",
  "secretAccessKey": "your-aws-secret-access-key",
  "region": "your-aws-region"
}
```

You can find these values in your AWS account:

1. **accessKeyId**: This is your AWS Access Key ID. You can create or find your access keys in the AWS Management Console under "Security Credentials" in your AWS account.

2. **secretAccessKey**: This is your AWS Secret Access Key, which is provided when you create an access key.

3. **region**: The AWS region where your Amazon Bedrock models are deployed (e.g., "us-east-1", "us-west-2").

Make sure your AWS IAM user or role has the necessary permissions to access Amazon Bedrock services. At minimum, you'll need permissions for:

* `bedrock:InvokeModel`
* `bedrock:InvokeModelWithResponseStream` (for streaming responses)

Example IAM policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*"
    }
  ]
}
```

For enhanced security, we recommend creating dedicated IAM users with limited permissions specifically for use with OpenRouter.

Learn more in the [AWS Bedrock Getting Started with the API](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api.html) documentation, [IAM Permissions Setup](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) guide, or the [AWS Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html).

### Google Vertex API Keys

To use Google Vertex AI with OpenRouter, you'll need to provide your Google Cloud service account key in JSON format. The service account key should include all standard Google Cloud service account fields, with an optional `region` field for specifying the deployment region.

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account@your-project.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account@your-project.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com",
  "region": "global"
}
```

You can find these values in your Google Cloud Console:

1. **Service Account Key**: Navigate to the Google Cloud Console, go to "IAM & Admin" > "Service Accounts", select your service account, and create/download a JSON key.

2. **region** (optional): Specify the region for your Vertex AI deployment. Use `"global"` to allow requests to run in any available region, or specify a specific region like `"us-central1"` or `"europe-west1"`.

Make sure your service account has the necessary permissions to access Vertex AI services:

* `aiplatform.endpoints.predict`
* `aiplatform.endpoints.streamingPredict` (for streaming responses)

Example IAM policy:

```json
{
  "bindings": [
    {
      "role": "roles/aiplatform.user",
      "members": [
        "serviceAccount:your-service-account@your-project.iam.gserviceaccount.com"
      ]
    }
  ]
}
```

Learn more in the [Google Cloud Vertex AI documentation](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) and [Service Account setup guide](https://cloud.google.com/iam/docs/service-accounts-create).



---

**Navigation:** [← Previous](./04-list-all-models-and-their-properties.md) | [Index](./index.md) | [Next →](./06-crypto-api.md)
