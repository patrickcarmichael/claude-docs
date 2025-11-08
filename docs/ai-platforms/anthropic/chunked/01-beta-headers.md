**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-hosting-the-agent-sdk.md)

---

# Beta headers
Source: https://docs.claude.com/en/api/beta-headers

Documentation for using beta headers with the Claude API

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

These features are subject to change and may be modified or removed in future releases.

<Info>
  Beta headers are often used in conjunction with the [beta namespace in the client SDKs](/en/api/client-sdks#beta-namespace-in-client-sdks)
</Info>

## How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

```http  theme={null}
POST /v1/messages
Content-Type: application/json
X-API-Key: YOUR_API_KEY
anthropic-beta: BETA_FEATURE_NAME
```

When using the SDK, you can specify beta headers in the request options:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import Anthropic

  client = Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Hello, Claude"}
      ],
      betas=["beta-feature-name"]
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const msg = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      { role: 'user', content: 'Hello, Claude' }
    ],
    betas: ['beta-feature-name']
  });
  ```

  ```curl cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: beta-feature-name" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Hello, Claude"}
      ]
    }'
  ```
</CodeGroup>

<Warning>
  Beta features are experimental and may:

  * Have breaking changes without notice
  * Be deprecated or removed
  * Have different rate limits or pricing
  * Not be available in all regions
</Warning>

### Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

```http  theme={null}
anthropic-beta: feature1,feature2,feature3
```

### Version naming conventions

Beta feature names typically follow the pattern: `feature-name-YYYY-MM-DD`, where the date indicates when the beta version was released. Always use the exact beta feature name as documented.

## Error handling

If you use an invalid or unavailable beta header, you'll receive an error response:

```json  theme={null}
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unsupported beta header: invalid-beta-name"
  }
}
```

## Getting help

For questions about beta features:

1. Check the documentation for the specific feature
2. Review the [API changelog](/en/api/versioning) for updates
3. Contact support for assistance with production usage

Remember that beta features are provided "as-is" and may not have the same SLA guarantees as stable API features.


# Client SDKs
Source: https://docs.claude.com/en/api/client-sdks

We provide client libraries in a number of popular languages that make it easier to work with the Claude API.

This page includes brief installation instructions and links to the open-source GitHub repositories for Anthropic's Client SDKs. For basic usage instructions, see the [API reference](/en/api/overview) For detailed usage instructions, refer to each SDK's GitHub repository.

<Note>
  Additional configuration is needed to use Anthropic's Client SDKs through a partner platform. If you are using Amazon Bedrock, see [this guide](/en/docs/build-with-claude/claude-on-amazon-bedrock); if you are using Google Cloud Vertex AI, see [this guide](/en/docs/build-with-claude/claude-on-vertex-ai).
</Note>

## Python

[Python library GitHub repo](https://github.com/anthropics/anthropic-sdk-python)

**Requirements:** Python 3.8+

**Installation:**

```bash  theme={null}
pip install anthropic
```

***

## TypeScript

[TypeScript library GitHub repo](https://github.com/anthropics/anthropic-sdk-typescript)

<Info>
  While this library is in TypeScript, it can also be used in JavaScript libraries.
</Info>

**Installation:**

```bash  theme={null}
npm install @anthropic-ai/sdk
```

***

## Java

[Java library GitHub repo](https://github.com/anthropics/anthropic-sdk-java)

**Requirements:** Java 8 or later

**Installation:**

Gradle:

```gradle  theme={null}
implementation("com.anthropic:anthropic-java:2.10.0")
```

Maven:

```xml  theme={null}
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java</artifactId>
    <version>2.10.0</version>
</dependency>
```

***

## Go

[Go library GitHub repo](https://github.com/anthropics/anthropic-sdk-go)

**Requirements:** Go 1.22+

**Installation:**

```bash  theme={null}
go get -u 'github.com/anthropics/anthropic-sdk-go@v1.17.0'
```

***

## C\#

[C# library GitHub repo](https://github.com/anthropics/anthropic-sdk-csharp)

<Info>
  The C# SDK is currently in beta.
</Info>

**Requirements:** .NET 8 or later

**Installation:**

```bash  theme={null}
git clone git@github.com:anthropics/anthropic-sdk-csharp.git
dotnet add reference anthropic-sdk-csharp/src/Anthropic.Client
```

***

## Ruby

[Ruby library GitHub repo](https://github.com/anthropics/anthropic-sdk-ruby)

**Requirements:** Ruby 3.2.0 or later

**Installation:**

Add to your Gemfile:

```ruby  theme={null}
gem "anthropic", "~> 1.13.0"
```

Then run:

```bash  theme={null}
bundle install
```

***

## PHP

[PHP library GitHub repo](https://github.com/anthropics/anthropic-sdk-php)

<Info>
  The PHP SDK is currently in beta.
</Info>

**Requirements:** PHP 8.1.0 or higher

**Installation:**

```bash  theme={null}
composer require "anthropic-ai/sdk 0.3.0"
```

***

## Beta namespace in client SDKs

Every SDK has a `beta` namespace that is available for accessing new features that Anthropic releases in beta versions. Use this in conjunction with [beta headers](/en/api/beta-headers) to access these features. Refer to each SDK's GitHub repository for specific usage examples.


# Create a Message Batch
Source: https://docs.claude.com/en/api/creating-message-batches

post /v1/messages/batches
Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)

## Feature Support

The Message Batches API supports all active models. All features available in the Messages API, including beta features, are available through the Message Batches API.

Batches may contain up to 100,000 requests and be up to 256 MB in total size.


# Errors
Source: https://docs.claude.com/en/api/errors



## HTTP errors

Our API follows a predictable HTTP error code format:

* 400 - `invalid_request_error`: There was an issue with the format or content of your request. We may also use this error type for other 4XX status codes not listed below.
* 401 - `authentication_error`: There's an issue with your API key.
* 403 - `permission_error`: Your API key does not have permission to use the specified resource.
* 404 - `not_found_error`: The requested resource was not found.
* 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. The maximum request size is 32 MB for standard API endpoints.
* 429 - `rate_limit_error`: Your account has hit a rate limit.
* 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems.
* 529 - `overloaded_error`: The API is temporarily overloaded.

  <Warning>
    529 errors can occur when APIs experience high traffic across all users.

    In rare cases, if your organization has a sharp increase in usage, you might see 429 errors due to acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.
  </Warning>

When receiving a [streaming](/en/docs/build-with-claude/streaming) response via SSE, it's possible that an error can occur after returning a 200 response, in which case error handling wouldn't follow these standard mechanisms.

## Request size limits

The API enforces request size limits to ensure optimal performance:

| Endpoint Type                                            | Maximum Request Size |
| :------------------------------------------------------- | :------------------- |
| Messages API                                             | 32 MB                |
| Token Counting API                                       | 32 MB                |
| [Batch API](/en/docs/build-with-claude/batch-processing) | 256 MB               |
| [Files API](/en/docs/build-with-claude/files)            | 500 MB               |

If you exceed these limits, you'll receive a 413 `request_too_large` error. The error is returned from Cloudflare before the request reaches our API servers.

## Error shapes

Errors are always returned as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:

```JSON JSON theme={null}
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

In accordance with our [versioning](/en/api/versioning) policy, we may expand the values within these objects, and it is possible that the `type` values will grow over time.

## Request id

Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. When contacting support about a specific request, please include this ID to help us quickly resolve your issue.

Our official SDKs provide this value as a property on top-level response objects, containing the value of the `request-id` header:

<CodeGroup>
  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Hello, Claude"}
      ]
  )
  print(f"Request ID: {message._request_id}")
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const message = await client.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      {"role": "user", "content": "Hello, Claude"}
    ]
  });
  console.log('Request ID:', message._request_id);
  ```
</CodeGroup>

## Long requests

<Warning>
  We highly encourage using the [streaming Messages API](/en/docs/build-with-claude/streaming) or [Message Batches API](/en/api/creating-message-batches) for long running requests, especially those over 10 minutes.
</Warning>

We do not recommend setting a large `max_tokens` values without using our [streaming Messages API](/en/docs/build-with-claude/streaming)
or [Message Batches API](/en/api/creating-message-batches):

* Some networks may drop idle connections after a variable period of time, which
  can cause the request to fail or timeout without receiving a response from Anthropic.
* Networks differ in reliability; our [Message Batches API](/en/api/creating-message-batches) can help you
  manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, you should be aware that setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

Our [SDKs](/en/api/client-sdks) will validate that your non-streaming Messages API requests are not expected to exceed a 10 minute timeout and
also will set a socket option for TCP keep-alive.


# List Message Batches
Source: https://docs.claude.com/en/api/listing-message-batches

get /v1/messages/batches
List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)



# Messages
Source: https://docs.claude.com/en/api/messages

post /v1/messages
Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](/en/docs/initial-setup)



# Count Message tokens
Source: https://docs.claude.com/en/api/messages-count-tokens

post /v1/messages/count_tokens
Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](/en/docs/build-with-claude/token-counting)



# Get a Model
Source: https://docs.claude.com/en/api/models

get /v1/models/{model_id}
Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.



# List Models
Source: https://docs.claude.com/en/api/models-list

get /v1/models
List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.



# Features overview
Source: https://docs.claude.com/en/api/overview

Explore Claude's advanced features and capabilities.

export const PlatformAvailability = ({claudeApi = false, claudeApiBeta = false, bedrock = false, bedrockBeta = false, vertexAi = false, vertexAiBeta = false}) => {
  const platforms = [];
  if (claudeApi || claudeApiBeta) {
    platforms.push(claudeApiBeta ? 'Claude API (Beta)' : 'Claude API');
  }
  if (bedrock || bedrockBeta) {
    platforms.push(bedrockBeta ? 'Amazon Bedrock (Beta)' : 'Amazon Bedrock');
  }
  if (vertexAi || vertexAiBeta) {
    platforms.push(vertexAiBeta ? "Google Cloud's Vertex AI (Beta)" : "Google Cloud's Vertex AI");
  }
  return <>
      {platforms.map((platform, index) => <span key={index}>
          {platform}
          {index < platforms.length - 1 && <><br /><br /></>}
        </span>)}
    </>;
};

## Core capabilities

These features enhance Claude's fundamental abilities for processing, analyzing, and generating content across various formats and use cases.

| Feature                                                                                       | Description                                                                                                                                                                                                               | Availability                                                    |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) | An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases.                                                                       | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta /> |
| [Agent Skills](/en/docs/agents-and-tools/agent-skills/overview)                               | Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context.     | <PlatformAvailability claudeApiBeta />                          |
| [Batch processing](/en/docs/build-with-claude/batch-processing)                               | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls costs 50% less than standard API calls.                                         | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Citations](/en/docs/build-with-claude/citations)                                             | Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Context editing](/en/docs/build-with-claude/context-editing)                                 | Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations.                     | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta /> |
| [Extended thinking](/en/docs/build-with-claude/extended-thinking)                             | Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer.                                                                  | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Files API](/en/docs/build-with-claude/files)                                                 | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files.                                                                                         | <PlatformAvailability claudeApiBeta />                          |
| [PDF support](/en/docs/build-with-claude/pdf-support)                                         | Process and analyze text and visual content from PDF documents.                                                                                                                                                           | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Prompt caching (5m)](/en/docs/build-with-claude/prompt-caching)                              | Provide Claude with more background knowledge and example outputs to reduce costs and latency.                                                                                                                            | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Prompt caching (1hr)](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration)       | Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache.                                                                                             | <PlatformAvailability claudeApi />                              |
| [Search results](/en/docs/build-with-claude/search-results)                                   | Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools.                                      | <PlatformAvailability claudeApi vertexAi />                     |
| [Token counting](/en/api/messages-count-tokens)                                               | Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage.                                                  | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Tool use](/en/docs/agents-and-tools/tool-use/overview)                                       | Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. For a list of supported tools, see [the Tools table](#tools).                                                                 | <PlatformAvailability claudeApi bedrock vertexAi />             |

## Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces.

| Feature                                                                                       | Description                                                                                                                                                        | Availability                                                    |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| [Bash](/en/docs/agents-and-tools/tool-use/bash-tool)                                          | Execute bash commands and scripts to interact with the system shell and perform command-line operations.                                                           | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Code execution](/en/docs/agents-and-tools/tool-use/code-execution-tool)                      | Run Python code in a sandboxed environment for advanced data analysis.                                                                                             | <PlatformAvailability claudeApiBeta />                          |
| [Computer use](/en/docs/agents-and-tools/tool-use/computer-use-tool)                          | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands.                                                                         | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta /> |
| [Fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters.                                                     | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [MCP connector](/en/docs/agents-and-tools/mcp-connector)                                      | Connect to remote [MCP](/en/docs/mcp) servers directly from the Messages API without a separate MCP client.                                                        | <PlatformAvailability claudeApiBeta />                          |
| [Memory](/en/docs/agents-and-tools/tool-use/memory-tool)                                      | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta /> |
| [Text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool)                            | Create and edit text files with a built-in text editor interface for file manipulation tasks.                                                                      | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool)                                | Retrieve full content from specified web pages and PDF documents for in-depth analysis.                                                                            | <PlatformAvailability claudeApiBeta />                          |
| [Web search](/en/docs/agents-and-tools/tool-use/web-search-tool)                              | Augment Claude's comprehensive knowledge with current, real-world data from across the web.                                                                        | <PlatformAvailability claudeApi vertexAi />                     |


# Retrieve Message Batch Results
Source: https://docs.claude.com/en/api/retrieving-message-batch-results

get /v1/messages/batches/{message_batch_id}/results
Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)

<Warning>The path for retrieving Message Batch results should be pulled from the batch's `results_url`. This path should not be assumed and may change.</Warning>

<ResponseExample>
  ```JSON 200 theme={null}
  {"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
  {"custom_id":"my-first-request","result":{"type":"succeeded","message":{"id":"msg_01FqfsLoHwgeFbguDgpz48m7","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[{"type":"text","text":"Hello! How can I assist you today? Feel free to ask me any questions or let me know if there's anything you'd like to chat about."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"output_tokens":34}}}}
  ```

  ```JSON 4XX theme={null}
  {
    "type": "error",
    "error": {
      "type": "invalid_request_error",
      "message": "<string>"
    }
  }
  ```
</ResponseExample>


# Retrieve a Message Batch
Source: https://docs.claude.com/en/api/retrieving-message-batches

get /v1/messages/batches/{message_batch_id}
This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)



# Model deprecations
Source: https://docs.claude.com/en/docs/about-claude/model-deprecations



As we launch safer and more capable models, we regularly retire older models. Applications relying on Anthropic models may need occasional updates to keep working. Impacted customers will always be notified by email and in our documentation.

This page lists all API deprecations, along with recommended replacements.

## Overview

Anthropic uses the following terms to describe the lifecycle of our models:

* **Active**: The model is fully supported and recommended for use.
* **Legacy**: The model will no longer receive updates and may be deprecated in the future.
* **Deprecated**: The model is no longer available for new customers but continues to be available for existing users until retirement. We assign a retirement date at this point.
* **Retired**: The model is no longer available for use. Requests to retired models will fail.

<Warning>
  Please note that deprecated models are likely to be less reliable than active models. We urge you to move workloads to active models to maintain the highest level of support and reliability.
</Warning>

## Migrating to replacements

Once a model is deprecated, please migrate all usage to a suitable replacement before the retirement date. Requests to models past the retirement date will fail.

To help measure the performance of replacement models on your tasks, we recommend thorough testing of your applications with the new models well before the retirement date.

For specific instructions on migrating from Claude 3.7 to Claude 4.5 models, see [Migrating to Claude 4.5](/en/docs/about-claude/models/migrating-to-claude-4).

## Notifications

Anthropic notifies customers with active deployments for models with upcoming retirements. We provide at least 60 days notice before model retirement for publicly released models.

## Auditing model usage

To help identify usage of deprecated models, customers can access an audit of their API usage. Follow these steps:

1. Go to [https://console.anthropic.com/settings/usage](https://console.anthropic.com/settings/usage)
2. Click the "Export" button
3. Review the downloaded CSV to see usage broken down by API key and model

This audit will help you locate any instances where your application is still using deprecated models, allowing you to prioritize updates to newer models before the retirement date.

## Best practices

1. Regularly check our documentation for updates on model deprecations.
2. Test your applications with newer models well before the retirement date of your current model.
3. Update your code to use the recommended replacement model as soon as possible.
4. Contact our support team if you need assistance with migration or have any questions.

## Deprecation downsides and mitigations

We currently deprecate and retire models to ensure capacity for new model releases. We recognize that this comes with downsides:

* Users who value specific models must migrate to new versions
* Researchers lose access to models for ongoing and comparative studies
* Model retirement introduces safety- and model welfare-related risks

At some point, we hope to make past models publicly available again. In the meantime, we've committed to long-term preservation of model weights and other measures to help mitigate these impacts. For more details, see [Commitments on Model Deprecation and Preservation](https://www.anthropic.com/research/deprecation-commitments).

## Model status

All publicly released models are listed below with their status:

| API Model Name               | Current State | Deprecated       | Tentative Retirement Date          |
| :--------------------------- | :------------ | :--------------- | :--------------------------------- |
| `claude-3-opus-20240229`     | Deprecated    | June 30, 2025    | January 5, 2026                    |
| `claude-3-haiku-20240307`    | Active        | N/A              | Not sooner than March 7, 2025      |
| `claude-3-5-haiku-20241022`  | Active        | N/A              | Not sooner than October 22, 2025   |
| `claude-3-7-sonnet-20250219` | Deprecated    | October 28, 2025 | February 19, 2026                  |
| `claude-sonnet-4-20250514`   | Active        | N/A              | Not sooner than May 14, 2026       |
| `claude-opus-4-20250514`     | Active        | N/A              | Not sooner than May 14, 2026       |
| `claude-opus-4-1-20250805`   | Active        | N/A              | Not sooner than August 5, 2026     |
| `claude-sonnet-4-5-20250929` | Active        | N/A              | Not sooner than September 29, 2026 |
| `claude-haiku-4-5-20251001`  | Active        | N/A              | Not sooner than October 15, 2026   |

## Deprecation history

All deprecations are listed below, with the most recent announcements at the top.

### 2025-10-28: Claude Sonnet 3.7 model

On October 28, 2025, we notified developers using Claude Sonnet 3.7 model of its upcoming retirement on the Claude API.

| Retirement Date   | Deprecated Model             | Recommended Replacement      |
| :---------------- | :--------------------------- | :--------------------------- |
| February 19, 2026 | `claude-3-7-sonnet-20250219` | `claude-sonnet-4-5-20250929` |

### 2025-08-13: Claude Sonnet 3.5 models

<Note>
  These models were retired October 28, 2025.
</Note>

On August 13, 2025, we notified developers using Claude Sonnet 3.5 models of their upcoming retirement.

| Retirement Date  | Deprecated Model             | Recommended Replacement      |
| :--------------- | :--------------------------- | :--------------------------- |
| October 28, 2025 | `claude-3-5-sonnet-20240620` | `claude-sonnet-4-5-20250929` |
| October 28, 2025 | `claude-3-5-sonnet-20241022` | `claude-sonnet-4-5-20250929` |

### 2025-06-30: Claude Opus 3 model

On June 30, 2025, we notified developers using Claude Opus 3 model of its upcoming retirement.

| Retirement Date | Deprecated Model         | Recommended Replacement    |
| :-------------- | :----------------------- | :------------------------- |
| January 5, 2026 | `claude-3-opus-20240229` | `claude-opus-4-1-20250805` |

### 2025-01-21: Claude 2, Claude 2.1, and Claude Sonnet 3 models

<Note>
  These models were retired July 21, 2025.
</Note>

On January 21, 2025, we notified developers using Claude 2, Claude 2.1, and Claude Sonnet 3 models of their upcoming retirements.

| Retirement Date | Deprecated Model           | Recommended Replacement      |
| :-------------- | :------------------------- | :--------------------------- |
| July 21, 2025   | `claude-2.0`               | `claude-sonnet-4-5-20250929` |
| July 21, 2025   | `claude-2.1`               | `claude-sonnet-4-5-20250929` |
| July 21, 2025   | `claude-3-sonnet-20240229` | `claude-sonnet-4-5-20250929` |

### 2024-09-04: Claude 1 and Instant models

<Note>
  These models were retired November 6, 2024.
</Note>

On September 4, 2024, we notified developers using Claude 1 and Instant models of their upcoming retirements.

| Retirement Date  | Deprecated Model     | Recommended Replacement     |
| :--------------- | :------------------- | :-------------------------- |
| November 6, 2024 | `claude-1.0`         | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-1.1`         | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-1.2`         | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-1.3`         | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-instant-1.0` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-instant-1.1` | `claude-3-5-haiku-20241022` |
| November 6, 2024 | `claude-instant-1.2` | `claude-3-5-haiku-20241022` |


# Choosing the right model
Source: https://docs.claude.com/en/docs/about-claude/models/choosing-a-model

Selecting the optimal Claude model for your application involves balancing three key considerations: capabilities, speed, and cost. This guide helps you make an informed decision based on your specific requirements.

## Establish key criteria

When choosing a Claude model, we recommend first evaluating these factors:

* **Capabilities:** What specific features or capabilities will you need the model to have in order to meet your needs?
* **Speed:** How quickly does the model need to respond in your application?
* **Cost:** What's your budget for both development and production usage?

Knowing these answers in advance will make narrowing down and deciding which model to use much easier.

***

## Choose the best model to start with

There are two general approaches you can use to start testing which Claude model best works for your needs.

### Option 1: Start with a fast, cost-effective model

For many applications, starting with a faster, more cost-effective model like Claude Haiku 4.5 can be the optimal approach:

1. Begin implementation with Claude Haiku 4.5
2. Test your use case thoroughly
3. Evaluate if performance meets your requirements
4. Upgrade only if necessary for specific capability gaps

This approach allows for quick iteration, lower development costs, and is often sufficient for many common applications. This approach is best for:

* Initial prototyping and development
* Applications with tight latency requirements
* Cost-sensitive implementations
* High-volume, straightforward tasks

### Option 2: Start with the most capable model

For complex tasks where intelligence and advanced capabilities are paramount, you may want to start with the most capable model and then consider optimizing to more efficient models down the line:

1. Implement with Claude Sonnet 4.5
2. Optimize your prompts for these models
3. Evaluate if performance meets your requirements
4. Consider increasing efficiency by downgrading intelligence over time with greater workflow optimization

This approach is best for:

* Complex reasoning tasks
* Scientific or mathematical applications
* Tasks requiring nuanced understanding
* Applications where accuracy outweighs cost considerations
* Advanced coding

## Model selection matrix

| When you need...                                                                                                                                            | We recommend starting with... | Example use cases                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Best model for complex agents and coding, highest intelligence across most tasks, superior tool orchestration for long-running autonomous tasks             | Claude Sonnet 4.5             | Autonomous coding agents, cybersecurity automation, complex financial analysis, multi-hour research tasks, multi agent frameworks |
| Exceptional intelligence and reasoning for specialized complex tasks                                                                                        | Claude Opus 4.1               | Highly complex codebase refactoring, nuanced creative writing, specialized scientific analysis                                    |
| Near-frontier performance with lightning-fast speed and extended thinking - our fastest and most intelligent Haiku model at the most economical price point | Claude Haiku 4.5              | Real-time applications, high-volume intelligent processing, cost-sensitive deployments needing strong reasoning, sub-agent tasks  |

***

## Decide whether to upgrade or change models

To determine if you need to upgrade or change models, you should:

1. [Create benchmark tests](/en/docs/test-and-evaluate/develop-tests) specific to your use case - having a good evaluation set is the most important step in the process
2. Test with your actual prompts and data
3. Compare performance across models for:
   * Accuracy of responses
   * Response quality
   * Handling of edge cases
4. Weigh performance and cost tradeoffs

## Next steps

<CardGroup cols={3}>
  <Card title="Model comparison chart" icon="head-side-gear" href="/en/docs/about-claude/models/overview">
    See detailed specifications and pricing for the latest Claude models
  </Card>

  <Card title="What's new in Claude 4.5" icon="sparkles" href="/en/docs/about-claude/models/whats-new-claude-4-5">
    Explore the latest improvements in Claude 4.5 models
  </Card>

  <Card title="Start building" icon="code" href="/en/docs/get-started">
    Get started with your first API call
  </Card>
</CardGroup>


# Migrating to Claude 4.5
Source: https://docs.claude.com/en/docs/about-claude/models/migrating-to-claude-4



This guide covers two key migration paths to Claude 4.5 models:

* **Claude Sonnet 3.7 → Claude Sonnet 4.5**: Our most intelligent model with best-in-class reasoning, coding, and long-running agent capabilities
* **Claude Haiku 3.5 → Claude Haiku 4.5**: Our fastest and most intelligent Haiku model with near-frontier performance for real-time applications and high-volume intelligent processing

Both migrations involve breaking changes that require updates to your implementation. This guide will walk you through each migration path with step-by-step instructions and clearly marked breaking changes.

Before starting your migration, we recommend reviewing [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5) to understand the new features and capabilities available in these models, including extended thinking, context awareness, and behavioral improvements.

## Migrating from Claude Sonnet 3.7 to Claude Sonnet 4.5

Claude Sonnet 4.5 is our most intelligent model, offering best-in-class performance for reasoning, coding, and long-running autonomous agents. This migration includes several breaking changes that require updates to your implementation.

### Migration steps

1. **Update your model name:**
   ```python  theme={null}
   # Before (Claude Sonnet 3.7)
   model="claude-3-7-sonnet-20250219"

   # After (Claude Sonnet 4.5)
   model="claude-sonnet-4-5-20250929"
   ```

2. **Update sampling parameters**

   <Warning>
     This is a breaking change from the Claude Sonnet 3.7.
   </Warning>

   Use only `temperature` OR `top_p`, not both:

   ```python  theme={null}
   # Before (Claude Sonnet 3.7) - This will error in Sonnet 4.5
   response = client.messages.create(
       model="claude-3-7-sonnet-20250219",
       temperature=0.7,
       top_p=0.9,  # Cannot use both
       ...
   )

   # After (Claude Sonnet 4.5)
   response = client.messages.create(
       model="claude-sonnet-4-5-20250929",
       temperature=0.7,  # Use temperature OR top_p, not both
       ...
   )
   ```

3. **Handle the new `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals):

   ```python  theme={null}
   response = client.messages.create(...)

   if response.stop_reason == "refusal":
       # Handle refusal appropriately
       pass
   ```

4. **Update text editor tool (if applicable)**

   <Warning>
     This is a breaking change from the Claude Sonnet 3.7.
   </Warning>

   Update to `text_editor_20250728` (type) and `str_replace_based_edit_tool` (name). Remove any code using the `undo_edit` command.

   ```python  theme={null}
   # Before (Claude Sonnet 3.7)
   tools=[{"type": "text_editor_20250124", "name": "str_replace_editor"}]

   # After (Claude Sonnet 4.5)
   tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
   ```

   See [Text editor tool documentation](/en/docs/agents-and-tools/tool-use/text-editor-tool) for details.

5. **Update code execution tool (if applicable)**

   Upgrade to `code_execution_20250825`. The legacy version `code_execution_20250522` still works but is not recommended. See [Code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version) for migration instructions.

6. **Remove token-efficient tool use beta header**

   [Token-efficient tool use](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use) is a beta feature that only works with Claude 3.7 Sonnet. All Claude 4 models have built-in token-efficient tool use, so you should no longer include the beta header.

   Remove the `token-efficient-tools-2025-02-19` [beta header](/en/api/beta-headers) from your requests:

   ```python  theme={null}
   # Before (Claude Sonnet 3.7)
   client.messages.create(
       model="claude-3-7-sonnet-20250219",
       betas=["token-efficient-tools-2025-02-19"],  # Remove this
       ...
   )

   # After (Claude Sonnet 4.5)
   client.messages.create(
       model="claude-sonnet-4-5-20250929",
       # No token-efficient-tools beta header
       ...
   )
   ```

7. **Remove extended output beta header**

   The `output-128k-2025-02-19` [beta header](/en/api/beta-headers) for extended output is only available in Claude Sonnet 3.7.

   Remove this header from your requests:

   ```python  theme={null}
   # Before (Claude Sonnet 3.7)
   client.messages.create(
       model="claude-3-7-sonnet-20250219",
       betas=["output-128k-2025-02-19"],  # Remove this
       ...
   )

   # After (Claude Sonnet 4.5)
   client.messages.create(
       model="claude-sonnet-4-5-20250929",
       # No output-128k beta header
       ...
   )
   ```

8. **Update your prompts for behavioral changes**

   Claude Sonnet 4.5 has a more concise, direct communication style and requires explicit direction. Review [Claude 4 prompt engineering best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices) for optimization guidance.

9. **Consider enabling extended thinking for complex tasks**

   Enable [extended thinking](/en/docs/build-with-claude/extended-thinking) for significant performance improvements on coding and reasoning tasks (disabled by default):

   ```python  theme={null}
   response = client.messages.create(
       model="claude-sonnet-4-5-20250929",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 10000},
       messages=[...]
   )
   ```

   <Note>
     Extended thinking impacts [prompt caching](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency.
   </Note>

10. **Test your implementation**

Test in a development environment before deploying to production to ensure all breaking changes are properly handled.

### Sonnet 3.7 → 4.5 migration checklist

* [ ] Update model ID to `claude-sonnet-4-5-20250929`
* [ ] **BREAKING**: Update sampling parameters to use only `temperature` OR `top_p`, not both
* [ ] Handle new `refusal` stop reason in your application
* [ ] **BREAKING**: Update text editor tool to `text_editor_20250728` and `str_replace_based_edit_tool` (if applicable)
* [ ] **BREAKING**: Remove any code using the `undo_edit` command (if applicable)
* [ ] Update code execution tool to `code_execution_20250825` (if applicable)
* [ ] Remove `token-efficient-tools-2025-02-19` beta header (if applicable)
* [ ] Remove `output-128k-2025-02-19` beta header (if applicable)
* [ ] Review and update prompts following [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
* [ ] Consider enabling extended thinking for complex reasoning tasks
* [ ] Handle `model_context_window_exceeded` stop reason (Sonnet 4.5 specific)
* [ ] Consider enabling memory tool for long-running agents (beta)
* [ ] Consider using automatic tool call clearing for context editing (beta)
* [ ] Test in development environment before production deployment

### Features removed from Claude Sonnet 3.7

* **Token-efficient tool use**: The `token-efficient-tools-2025-02-19` beta header only works with Claude 3.7 Sonnet and is not supported in Claude 4 models (see step 6)
* **Extended output**: The `output-128k-2025-02-19` beta header is not supported (see step 7)

Both headers can be included in Claude 4 requests but will have no effect.

## Migrating from Claude Haiku 3.5 to Claude Haiku 4.5

Claude Haiku 4.5 is our fastest and most intelligent Haiku model with near-frontier performance, delivering premium model quality with real-time performance for interactive applications and high-volume intelligent processing. This migration includes several breaking changes that require updates to your implementation.

For a complete overview of new capabilities, see [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5#key-improvements-in-haiku-4-5-over-haiku-3-5).

<Note>
  Haiku 4.5 pricing $1 per million input tokens, $5 per million output tokens. See [Claude pricing](/en/docs/about-claude/pricing) for details.
</Note>

### Migration steps

1. **Update your model name:**
   ```python  theme={null}
   # Before (Haiku 3.5)
   model="claude-3-5-haiku-20241022"

   # After (Haiku 4.5)
   model="claude-haiku-4-5-20251001"
   ```

2. **Update tool versions (if applicable)**

   <Warning>
     This is a breaking change from the Claude Haiku 3.5.
   </Warning>

   Haiku 4.5 only supports the latest tool versions:

   ```python  theme={null}
   # Before (Haiku 3.5)
   tools=[{"type": "text_editor_20250124", "name": "str_replace_editor"}]

   # After (Haiku 4.5)
   tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
   ```

   * **Text editor**: Use `text_editor_20250728` and `str_replace_based_edit_tool`
   * **Code execution**: Use `code_execution_20250825`
   * Remove any code using the `undo_edit` command

3. **Update sampling parameters**

   <Warning>
     This is a breaking change from the Claude Haiku 3.5.
   </Warning>

   Use only `temperature` OR `top_p`, not both:

   ```python  theme={null}
   # Before (Haiku 3.5) - This will error in Haiku 4.5
   response = client.messages.create(
       model="claude-3-5-haiku-20241022",
       temperature=0.7,
       top_p=0.9,  # Cannot use both
       ...
   )

   # After (Haiku 4.5)
   response = client.messages.create(
       model="claude-haiku-4-5-20251001",
       temperature=0.7,  # Use temperature OR top_p, not both
       ...
   )
   ```

4. **Review new rate limits**

   Haiku 4.5 has separate rate limits from Haiku 3.5. See [Rate limits documentation](/en/api/rate-limits) for details.

5. **Handle the new `refusal` stop reason**

   Update your application to [handle refusal stop reasons](/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).

6. **Consider enabling extended thinking for complex tasks**

   Enable [extended thinking](/en/docs/build-with-claude/extended-thinking) for significant performance improvements on coding and reasoning tasks (disabled by default):

   ```python  theme={null}
   response = client.messages.create(
       model="claude-haiku-4-5-20251001",
       max_tokens=16000,
       thinking={"type": "enabled", "budget_tokens": 5000},
       messages=[...]
   )
   ```

   <Note>
     Extended thinking impacts [prompt caching](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency.
   </Note>

7. **Explore new capabilities**

   See [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5#key-improvements-in-haiku-4-5-over-haiku-3-5) for details on context awareness, increased output capacity (64K tokens), higher intelligence, and improved speed.

8. **Test your implementation**

   Test in a development environment before deploying to production to ensure all breaking changes are properly handled.

### Haiku 3.5 → 4.5 migration checklist

* [ ] Update model ID to `claude-haiku-4-5-20251001`
* [ ] **BREAKING**: Update tool versions to latest (e.g., `text_editor_20250728`, `code_execution_20250825`) - legacy versions not supported
* [ ] **BREAKING**: Remove any code using the `undo_edit` command (if applicable)
* [ ] **BREAKING**: Update sampling parameters to use only `temperature` OR `top_p`, not both
* [ ] Review and adjust for new rate limits (separate from Haiku 3.5)
* [ ] Handle new `refusal` stop reason in your application
* [ ] Consider enabling extended thinking for complex reasoning tasks (new capability)
* [ ] Leverage context awareness for better token management in long sessions
* [ ] Prepare for larger responses (max output increased from 8K to 64K tokens)
* [ ] Review and update prompts following [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
* [ ] Test in development environment before production deployment

## Choosing between Sonnet 4.5 and Haiku 4.5

Both Claude Sonnet 4.5 and Claude Haiku 4.5 are powerful Claude 4 models with different strengths:

### Choose Claude Sonnet 4.5 (most intelligent) for:

* **Complex reasoning and analysis**: Best-in-class intelligence for sophisticated tasks
* **Long-running autonomous agents**: Superior performance for agents working independently for extended periods
* **Advanced coding tasks**: Our strongest coding model with advanced planning and security engineering
* **Large context workflows**: Enhanced context management with memory tool and context editing capabilities
* **Tasks requiring maximum capability**: When intelligence and accuracy are the top priorities

### Choose Claude Haiku 4.5 (fastest and most intelligent Haiku) for:

* **Real-time applications**: Fast response times for interactive user experiences with near-frontier performance
* **High-volume intelligent processing**: Cost-effective intelligence at scale with improved speed
* **Cost-sensitive deployments**: Near-frontier performance at lower price points
* **Sub-agent architectures**: Fast, intelligent agents for multi-agent systems
* **Computer use at scale**: Cost-effective autonomous desktop and browser automation
* **Tasks requiring speed**: When low latency is critical while maintaining near-frontier intelligence

### Extended thinking recommendations

Claude 4 models, particularly Sonnet and Haiku 4.5, show significant performance improvements when using [extended thinking](/en/docs/build-with-claude/extended-thinking) for coding and complex reasoning tasks. Extended thinking is **disabled by default** but we recommend enabling it for demanding work.

**Important**: Extended thinking impacts [prompt caching](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency. When non-tool-result content is added to a conversation, thinking blocks are stripped from cache, which can increase costs in multi-turn conversations. We recommend enabling thinking when the performance benefits outweigh the caching trade-off.

## Other migration scenarios

The primary migration paths covered above (Sonnet 3.7 → 4.5 and Haiku 3.5 → 4.5) represent the most common upgrades. However, you may be migrating from other Claude models to Claude 4.5. This section covers those scenarios.

### Migrating from Claude Sonnet 4 → Sonnet 4.5

**Breaking change**: Cannot specify both `temperature` and `top_p` in the same request.

All other API calls will work without modification. Update your model ID and adjust sampling parameters if needed:

```python  theme={null}
# Before (Claude Sonnet 4)
model="claude-sonnet-4-20250514"

# After (Claude Sonnet 4.5)
model="claude-sonnet-4-5-20250929"
```

### Migrating from Claude Opus 4.1 → Sonnet 4.5

**No breaking changes.** All API calls will work without modification.

Simply update your model ID:

```python  theme={null}
# Before (Claude Opus 4.1)
model="claude-opus-4-1-20250805"

# After (Claude Sonnet 4.5)
model="claude-sonnet-4-5-20250929"
```

Claude Sonnet 4.5 is our most intelligent model with best-in-class reasoning, coding, and long-running agent capabilities. It offers superior performance compared to Opus 4.1 for most use cases.

## Need help?

* Check our [API documentation](/en/api/overview) for detailed specifications
* Review [model capabilities](/en/docs/about-claude/models/overview) for performance comparisons
* Review [API release notes](/en/release-notes/api) for API updates
* Contact support if you encounter any issues during migration


# Models overview
Source: https://docs.claude.com/en/docs/about-claude/models/overview

Claude is a family of state-of-the-art large language models developed by Anthropic. This guide introduces our models and compares their performance.

export const ModelId = ({children, style = {}}) => {
  const copiedNotice = 'Copied!';
  const handleClick = e => {
    const element = e.currentTarget;
    const textSpan = element.querySelector('.model-id-text');
    const copiedSpan = element.querySelector('.model-id-copied');
    navigator.clipboard.writeText(children).then(() => {
      textSpan.style.opacity = '0';
      copiedSpan.style.opacity = '1';
      element.style.backgroundColor = '#d4edda';
      element.style.borderColor = '#c3e6cb';
      setTimeout(() => {
        textSpan.style.opacity = '1';
        copiedSpan.style.opacity = '0';
        element.style.backgroundColor = '#f5f5f5';
        element.style.borderColor = 'transparent';
      }, 2000);
    }).catch(error => {
      console.error('Failed to copy:', error);
    });
  };
  const handleMouseEnter = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip && copiedSpan.style.opacity !== '1') {
      tooltip.style.opacity = '1';
    }
    element.style.backgroundColor = '#e8e8e8';
    element.style.borderColor = '#d0d0d0';
  };
  const handleMouseLeave = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip) {
      tooltip.style.opacity = '0';
    }
    if (copiedSpan.style.opacity !== '1') {
      element.style.backgroundColor = '#f5f5f5';
      element.style.borderColor = 'transparent';
    }
  };
  const defaultStyle = {
    cursor: 'pointer',
    position: 'relative',
    transition: 'all 0.2s ease',
    display: 'inline-block',
    userSelect: 'none',
    backgroundColor: '#f5f5f5',
    padding: '2px 4px',
    borderRadius: '4px',
    fontFamily: 'Monaco, Consolas, "Courier New", monospace',
    fontSize: '0.75em',
    border: '1px solid transparent',
    ...style
  };
  return <span onClick={handleClick} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} style={defaultStyle}>
      <span className="model-id-text" style={{
    transition: 'opacity 0.1s ease'
  }}>
        {children}
      </span>
      <span className="model-id-copied" style={{
    position: 'absolute',
    top: '2px',
    left: '4px',
    right: '4px',
    opacity: '0',
    transition: 'opacity 0.1s ease',
    color: '#155724'
  }}>
        {copiedNotice}
      </span>
    </span>;
};

## Choosing a model

If you're unsure which model to use, we recommend starting with **Claude Sonnet 4.5**. It offers the best balance of intelligence, speed, and cost for most use cases, with exceptional performance in coding and agentic tasks.

All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Anthropic API, AWS Bedrock, and Google Vertex AI.

Once you've picked a model, [learn how to make your first API call](/en/docs/get-started).

### Latest models comparison

| Feature                                                               | Claude Sonnet 4.5                                                                                                                                                                 | Claude Haiku 4.5                                                            | Claude Opus 4.1                                                             |
| :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Description**                                                       | Our smartest model for complex agents and coding                                                                                                                                  | Our fastest model with near-frontier intelligence                           | Exceptional model for specialized reasoning tasks                           |
| **Claude API ID**                                                     | <ModelId>claude-sonnet-4-5-20250929</ModelId>                                                                                                                                     | <ModelId>claude-haiku-4-5-20251001</ModelId>                                | <ModelId>claude-opus-4-1-20250805</ModelId>                                 |
| **Claude API alias**<sup>1</sup>                                      | <ModelId>claude-sonnet-4-5</ModelId>                                                                                                                                              | <ModelId>claude-haiku-4-5</ModelId>                                         | <ModelId>claude-opus-4-1</ModelId>                                          |
| **AWS Bedrock ID**                                                    | <ModelId>anthropic.claude-sonnet-4-5-20250929-v1:0</ModelId>                                                                                                                      | <ModelId>anthropic.claude-haiku-4-5-20251001-v1:0</ModelId>                 | <ModelId>anthropic.claude-opus-4-1-20250805-v1:0</ModelId>                  |
| **GCP Vertex AI ID**                                                  | <ModelId>claude-sonnet-4-5\@20250929</ModelId>                                                                                                                                    | <ModelId>claude-haiku-4-5\@20251001</ModelId>                               | <ModelId>claude-opus-4-1\@20250805</ModelId>                                |
| **Pricing**<sup>2</sup>                                               | \$3 / input MTok<br />\$15 / output MTok                                                                                                                                          | \$1 / input MTok<br />\$5 / output MTok                                     | \$15 / input MTok<br />\$75 / output MTok                                   |
| **[Extended thinking](/en/docs/build-with-claude/extended-thinking)** | Yes                                                                                                                                                                               | Yes                                                                         | Yes                                                                         |
| **[Priority Tier](/en/api/service-tiers)**                            | Yes                                                                                                                                                                               | Yes                                                                         | Yes                                                                         |
| **Comparative latency**                                               | Fast                                                                                                                                                                              | Fastest                                                                     | Moderate                                                                    |
| **Context window**                                                    | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> / <br /> <Tooltip tip="~750K words \ ~3.4M unicode characters">1M tokens</Tooltip> (beta)<sup>3</sup> | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> |
| **Max output**                                                        | 64K tokens                                                                                                                                                                        | 64K tokens                                                                  | 32K tokens                                                                  |
| **Reliable knowledge cutoff**                                         | Jan 2025<sup>4</sup>                                                                                                                                                              | Feb 2025                                                                    | Jan 2025<sup>4</sup>                                                        |
| **Training data cutoff**                                              | Jul 2025                                                                                                                                                                          | Jul 2025                                                                    | Mar 2025                                                                    |

*<sup>1 - Aliases automatically point to the most recent model snapshot. When we release new model snapshots, we migrate aliases to point to the newest version of a model, typically within a week of the new release. While aliases are useful for experimentation, we recommend using specific model versions (e.g., `claude-sonnet-4-5-20250929`) in production applications to ensure consistent behavior.</sup>*

*<sup>2 - See our [pricing page](/en/docs/about-claude/pricing) for complete pricing information including batch API discounts, prompt caching rates, extended thinking costs, and vision processing fees.</sup>*

*<sup>3 - Claude Sonnet 4.5 supports a [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) when using the `context-1m-2025-08-07` beta header. [Long context pricing](/en/docs/about-claude/pricing#long-context-pricing) applies to requests exceeding 200K tokens.</sup>*

*<sup>4 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used. For example, Claude Sonnet 4.5 was trained on publicly available information through July 2025, but its knowledge is most extensive and reliable through January 2025. For more information, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).</sup>*

<Note>Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.</Note>

<Note>Starting with **Claude Sonnet 4.5 and all future models**, AWS Bedrock and Google Vertex AI offer two endpoint types: **global endpoints** (dynamic routing for maximum availability) and **regional endpoints** (guaranteed data routing through specific geographic regions). For more information, see the [third-party platform pricing section](/en/docs/about-claude/pricing#third-party-platform-pricing).</Note>

<AccordionGroup>
  <Accordion title="Legacy models">
    The following models are still available but we recommend migrating to current models for improved performance:

    | Feature                                                               | Claude Sonnet 4                                                                                                                                                                   | Claude Sonnet 3.7                                                           | Claude Opus 4                                                               | Claude Haiku 3.5                                                            | Claude Haiku 3                                                              |
    | :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
    | **Claude API ID**                                                     | <ModelId>claude-sonnet-4-20250514</ModelId>                                                                                                                                       | <ModelId>claude-3-7-sonnet-20250219</ModelId>                               | <ModelId>claude-opus-4-20250514</ModelId>                                   | <ModelId>claude-3-5-haiku-20241022</ModelId>                                | <ModelId>claude-3-haiku-20240307</ModelId>                                  |
    | **Claude API alias**                                                  | <ModelId>claude-sonnet-4-0</ModelId>                                                                                                                                              | <ModelId>claude-3-7-sonnet-latest</ModelId>                                 | <ModelId>claude-opus-4-0</ModelId>                                          | <ModelId>claude-3-5-haiku-latest</ModelId>                                  | —                                                                           |
    | **AWS Bedrock ID**                                                    | <ModelId>anthropic.claude-sonnet-4-20250514-v1:0</ModelId>                                                                                                                        | <ModelId>anthropic.claude-3-7-sonnet-20250219-v1:0</ModelId>                | <ModelId>anthropic.claude-opus-4-20250514-v1:0</ModelId>                    | <ModelId>anthropic.claude-3-5-haiku-20241022-v1:0</ModelId>                 | <ModelId>anthropic.claude-3-haiku-20240307-v1:0</ModelId>                   |
    | **GCP Vertex AI ID**                                                  | <ModelId>claude-sonnet-4\@20250514</ModelId>                                                                                                                                      | <ModelId>claude-3-7-sonnet\@20250219</ModelId>                              | <ModelId>claude-opus-4\@20250514</ModelId>                                  | <ModelId>claude-3-5-haiku\@20241022</ModelId>                               | <ModelId>claude-3-haiku\@20240307</ModelId>                                 |
    | **Pricing**                                                           | \$3 / input MTok<br />\$15 / output MTok                                                                                                                                          | \$3 / input MTok<br />\$15 / output MTok                                    | \$15 / input MTok<br />\$75 / output MTok                                   | \$0.80 / input MTok<br />\$4 / output MTok                                  | \$0.25 / input MTok<br />\$1.25 / output MTok                               |
    | **[Extended thinking](/en/docs/build-with-claude/extended-thinking)** | Yes                                                                                                                                                                               | Yes                                                                         | Yes                                                                         | No                                                                          | No                                                                          |
    | **[Priority Tier](/en/api/service-tiers)**                            | Yes                                                                                                                                                                               | Yes                                                                         | Yes                                                                         | Yes                                                                         | No                                                                          |
    | **Comparative latency**                                               | Fast                                                                                                                                                                              | Fast                                                                        | Moderate                                                                    | Fastest                                                                     | Fast                                                                        |
    | **Context window**                                                    | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> / <br /> <Tooltip tip="~750K words \ ~3.4M unicode characters">1M tokens</Tooltip> (beta)<sup>1</sup> | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> | <Tooltip tip="~150K words \ ~215K unicode characters">200K tokens</Tooltip> | <Tooltip tip="~150K words \ ~680K unicode characters">200K tokens</Tooltip> |
    | **Max output**                                                        | 64K tokens                                                                                                                                                                        | 64K tokens / 128K tokens (beta)<sup>4</sup>                                 | 32K tokens                                                                  | 8K tokens                                                                   | 4K tokens                                                                   |
    | **Reliable knowledge cutoff**                                         | Jan 2025<sup>2</sup>                                                                                                                                                              | Oct 2024<sup>2</sup>                                                        | Jan 2025<sup>2</sup>                                                        | <sup>3</sup>                                                                | <sup>3</sup>                                                                |
    | **Training data cutoff**                                              | Mar 2025                                                                                                                                                                          | Nov 2024                                                                    | Mar 2025                                                                    | Jul 2024                                                                    | Aug 2023                                                                    |

    *<sup>1 - Claude Sonnet 4 supports a [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) when using the `context-1m-2025-08-07` beta header. [Long context pricing](/en/docs/about-claude/pricing#long-context-pricing) applies to requests exceeding 200K tokens.</sup>*

    *<sup>2 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used.</sup>*

    *<sup>3 - Some Haiku models have a single training data cutoff date.</sup>*

    *<sup>4 - Include the beta header `output-128k-2025-02-19` in your API request to increase the maximum output token length to 128K tokens for Claude Sonnet 3.7. We strongly suggest using our [streaming Messages API](/en/docs/build-with-claude/streaming) to avoid timeouts when generating longer outputs. See our guidance on [long requests](/en/api/errors#long-requests) for more details.</sup>*
  </Accordion>
</AccordionGroup>

## Prompt and output performance

Claude 4 models excel in:

* **Performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 4 blog post](http://www.anthropic.com/news/claude-4) for more information.
* **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.

  * If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our [prompt engineering guides](/en/docs/build-with-claude/prompt-engineering) for details.
  * For specific Claude 4 prompting best practices, see our [Claude 4 best practices guide](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices).
* **Output quality**: When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.

## Migrating to Claude 4.5

If you're currently using Claude 3 models, we recommend migrating to Claude 4.5 to take advantage of improved intelligence and enhanced capabilities. For detailed migration instructions, see [Migrating to Claude 4.5](/en/docs/about-claude/models/migrating-to-claude-4).

## Get started with Claude

If you're ready to start exploring what Claude can do for you, let's dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we've got you covered.

<Note>Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!</Note>

<CardGroup cols={3}>
  <Card title="Intro to Claude" icon="check" href="/en/docs/intro">
    Explore Claude's capabilities and development flow.
  </Card>

  <Card title="Quickstart" icon="bolt-lightning" href="/en/docs/get-started">
    Learn how to make your first API call in minutes.
  </Card>

  <Card title="Claude Console" icon="code" href="https://console.anthropic.com">
    Craft and test powerful prompts directly in your browser.
  </Card>
</CardGroup>

If you have any questions or need assistance, don't hesitate to reach out to our [support team](https://support.claude.com/) or consult the [Discord community](https://www.anthropic.com/discord).


# What's new in Claude 4.5
Source: https://docs.claude.com/en/docs/about-claude/models/whats-new-claude-4-5



Claude 4.5 introduces two models designed for different use cases:

* **Claude Sonnet 4.5**: Our best model for complex agents and coding, with the highest intelligence across most tasks
* **Claude Haiku 4.5**: Our fastest and most intelligent Haiku model with near-frontier performance. The first Haiku model with extended thinking

## Key improvements in Sonnet 4.5 over Sonnet 4

### Coding excellence

Claude Sonnet 4.5 is our best coding model to date, with significant improvements across the entire development lifecycle:

* **SWE-bench Verified performance**: Advanced state-of-the-art on coding benchmarks
* **Enhanced planning and system design**: Better architectural decisions and code organization
* **Improved security engineering**: More robust security practices and vulnerability detection
* **Better instruction following**: More precise adherence to coding specifications and requirements

<Note>
  Claude Sonnet 4.5 performs significantly better on coding tasks when [extended thinking](/en/docs/build-with-claude/extended-thinking) is enabled. Extended thinking is disabled by default, but we recommend enabling it for complex coding work. Be aware that extended thinking impacts [prompt caching efficiency](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks). See the [migration guide](/en/docs/about-claude/models/migrating-to-claude-4#extended-thinking-recommendations) for configuration details.
</Note>

### Agent capabilities

Claude Sonnet 4.5 introduces major advances in agent capabilities:

* **Extended autonomous operation**: Sonnet 4.5 can work independently for hours while maintaining clarity and focus on incremental progress. The model makes steady advances on a few tasks at a time rather than attempting everything at once. It provides fact-based progress updates that accurately reflect what has been accomplished.
* **Context awareness**: Claude now tracks its token usage throughout conversations, receiving updates after each tool call. This awareness helps prevent premature task abandonment and enables more effective execution on long-running tasks. See [Context awareness](/en/docs/build-with-claude/context-windows#context-awareness-in-claude-sonnet-4-5) for technical details and [prompting guidance](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#context-awareness-and-multi-window-workflows).
* **Enhanced tool usage**: The model more effectively uses parallel tool calls, firing off multiple speculative searches simultaneously during research and reading several files at once to build context faster. Improved coordination across multiple tools and information sources enables the model to effectively leverage a wide range of capabilities in agentic search and coding workflows.
* **Advanced context management**: Sonnet 4.5 maintains exceptional state tracking in external files, preserving goal-orientation across sessions. Combined with more effective context window usage and our new context management API features, the model optimally handles information across extended sessions to maintain coherence over time.

<Note>Context awareness is available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1.</Note>

### Communication and interaction style

Claude Sonnet 4.5 has a refined communication approach that is concise, direct, and natural. It provides fact-based progress updates and may skip verbose summaries after tool calls to maintain workflow momentum (though this can be adjusted with prompting).

For detailed guidance on working with this communication style, see [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices).

### Creative content generation

Claude Sonnet 4.5 excels at creative content tasks:

* **Presentations and animations**: Matches or exceeds Claude Opus 4.1 for creating slides and visual content
* **Creative flair**: Produces polished, professional output with strong instruction following
* **First-try quality**: Generates usable, well-designed content in initial attempts

## Key improvements in Haiku 4.5 over Haiku 3.5

Claude Haiku 4.5 represents a transformative leap for the Haiku model family, bringing frontier capabilities to our fastest model class:

### Near-frontier intelligence with blazing speed

Claude Haiku 4.5 delivers near-frontier performance matching Sonnet 4 at significantly lower cost and faster speed:

* **Near-frontier intelligence**: Matches Sonnet 4 performance across reasoning, coding, and complex tasks
* **Enhanced speed**: More than twice the speed of Sonnet 4, with optimizations for output tokens per second (OTPS)
* **Optimal cost-performance**: Near-frontier intelligence at one-third the cost, ideal for high-volume deployments

### Extended thinking capabilities

Claude Haiku 4.5 is the **first Haiku model** to support extended thinking, bringing advanced reasoning capabilities to the Haiku family:

* **Reasoning at speed**: Access to Claude's internal reasoning process for complex problem-solving
* **Thinking Summarization**: Summarized thinking output for production-ready deployments
* **Interleaved thinking**: Think between tool calls for more sophisticated multi-step workflows
* **Budget control**: Configure thinking token budgets to balance reasoning depth with speed

Extended thinking must be enabled explicitly by adding a `thinking` parameter to your API requests. See the [Extended thinking documentation](/en/docs/build-with-claude/extended-thinking) for implementation details.

<Note>
  Claude Haiku 4.5 performs significantly better on coding and reasoning tasks when [extended thinking](/en/docs/build-with-claude/extended-thinking) is enabled. Extended thinking is disabled by default, but we recommend enabling it for complex problem-solving, coding work, and multi-step reasoning. Be aware that extended thinking impacts [prompt caching efficiency](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks). See the [migration guide](/en/docs/about-claude/models/migrating-to-claude-4#extended-thinking-recommendations) for configuration details.
</Note>

<Note>Available in Claude Sonnet 3.7, Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1.</Note>

### Context awareness

Claude Haiku 4.5 features **context awareness**, enabling the model to track its remaining context window throughout a conversation:

* **Token budget tracking**: Claude receives real-time updates on remaining context capacity after each tool call
* **Better task persistence**: The model can execute tasks more effectively by understanding available working space
* **Multi-context-window workflows**: Improved handling of state transitions across extended sessions

This is the first Haiku model with native context awareness capabilities. For prompting guidance, see [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#context-awareness-and-multi-window-workflows).

<Note>Available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1.</Note>

### Strong coding and tool use

Claude Haiku 4.5 delivers robust coding capabilities expected from modern Claude models:

* **Coding proficiency**: Strong performance across code generation, debugging, and refactoring tasks
* **Full tool support**: Compatible with all Claude 4 tools including bash, code execution, text editor, web search, and computer use
* **Enhanced computer use**: Optimized for autonomous desktop interaction and browser automation workflows
* **Parallel tool execution**: Efficient coordination across multiple tools for complex workflows

Haiku 4.5 is designed for use cases that demand both intelligence and efficiency:

* **Real-time applications**: Fast response times for interactive user experiences
* **High-volume processing**: Cost-effective intelligence for large-scale deployments
* **Free tier implementations**: Premium model quality at accessible pricing
* **Sub-agent architectures**: Fast, intelligent agents for multi-agent systems
* **Computer use at scale**: Cost-effective autonomous desktop and browser automation

## New API features

### Memory tool (Beta)

The new [memory tool](/en/docs/agents-and-tools/tool-use/memory-tool) enables Claude to store and retrieve information outside the context window:

```python  theme={null}
tools=[
    {
        "type": "memory_20250818",
        "name": "memory"
    }
]
```

This allows for:

* Building knowledge bases over time
* Maintaining project state across sessions
* Preserving effectively unlimited context through file-based storage

<Note>Available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1. Requires [beta header](/en/api/beta-headers): `context-management-2025-06-27`</Note>

### Context editing

Use [context editing](/en/docs/build-with-claude/context-editing) for intelligent context management through automatic tool call clearing:

```python  theme={null}
response = client.beta.messages.create(
    betas=["context-management-2025-06-27"],
    model="claude-sonnet-4-5",  # or claude-haiku-4-5
    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    context_management={
        "edits": [
            {
                "type": "clear_tool_uses_20250919",
                "trigger": {"type": "input_tokens", "value": 500},
                "keep": {"type": "tool_uses", "value": 2},
                "clear_at_least": {"type": "input_tokens", "value": 100}
            }
        ]
    },
    tools=[...]
)
```

This feature automatically removes older tool calls and results when approaching token limits, helping manage context in long-running agent sessions.

<Note>Available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1. Requires [beta header](/en/api/beta-headers): `context-management-2025-06-27`</Note>

### Enhanced stop reasons

Claude 4.5 models introduce a new `model_context_window_exceeded` stop reason that explicitly indicates when generation stopped due to hitting the context window limit, rather than the requested `max_tokens` limit. This makes it easier to handle context window limits in your application logic.

```json  theme={null}
{
  "stop_reason": "model_context_window_exceeded",
  "usage": {
    "input_tokens": 150000,
    "output_tokens": 49950
  }
}
```

### Improved tool parameter handling

Claude 4.5 models include a bug fix that preserves intentional formatting in tool call string parameters. Previously, trailing newlines in string parameters were sometimes incorrectly stripped. This fix ensures that tools requiring precise formatting (like text editors) receive parameters exactly as intended.

<Note>
  This is a behind-the-scenes improvement with no API changes required. However, tools with string parameters may now receive values with trailing newlines that were previously stripped.
</Note>

**Example:**

```json  theme={null}
// Before: Final newline accidentally stripped
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "edit_todo",
  "input": {
    "file": "todo.txt",
    "contents": "1. Chop onions.\n2. ???\n3. Profit"
  }
}

// After: Trailing newline preserved as intended
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "edit_todo",
  "input": {
    "file": "todo.txt",
    "contents": "1. Chop onions.\n2. ???\n3. Profit\n"
  }
}
```

### Token count optimizations

Claude 4.5 models include automatic optimizations to improve model performance. These optimizations may add small amounts of tokens to requests, but **you are not billed for these system-added tokens**.

## Features introduced in Claude 4

The following features were introduced in Claude 4 and are available across Claude 4 models, including Claude Sonnet 4.5 and Claude Haiku 4.5.

### New refusal stop reason

Claude 4 models introduce a new `refusal` stop reason for content that the model declines to generate for safety reasons:

```json  theme={null}
{"id":"msg_014XEDjypDjFzgKVWdFUXxZP",
"type":"message",
"role":"assistant",
"model":"claude-sonnet-4-5",
"content":[{"type":"text","text":"I would be happy to assist you. You can "}],
"stop_reason":"refusal",
"stop_sequence":null,
"usage":{"input_tokens":564,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":22}
}
```

When using Claude 4 models, you should update your application to [handle `refusal` stop reasons](/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).

### Summarized thinking

With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude's full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse.

While the API is consistent across Claude 3.7 and 4 models, streaming responses for extended thinking might return in a "chunky" delivery pattern, with possible delays between streaming events.

<Note>
  Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.
</Note>

For more information, see the [Extended thinking documentation](/en/docs/build-with-claude/extended-thinking#summarized-thinking).

### Interleaved thinking

Claude 4 models support interleaving tool use with extended thinking, allowing for more natural conversations where tool uses and responses can be mixed with regular messages.

<Note>
  Interleaved thinking is in beta. To enable interleaved thinking, add [the beta header](/en/api/beta-headers) `interleaved-thinking-2025-05-14` to your API request.
</Note>

For more information, see the [Extended thinking documentation](/en/docs/build-with-claude/extended-thinking#interleaved-thinking).

### Behavioral differences

Claude 4 models have notable behavioral changes that may affect how you structure prompts:

#### Communication style changes

* **More concise and direct**: Claude 4 models communicate more efficiently, with less verbose explanations
* **More natural tone**: Responses are slightly more conversational and less machine-like
* **Efficiency-focused**: May skip detailed summaries after completing actions to maintain workflow momentum (you can prompt for more detail if needed)

#### Instruction following

Claude 4 models are trained for precise instruction following and require more explicit direction:

* **Be explicit about actions**: Use direct language like "Make these changes" or "Implement this feature" rather than "Can you suggest changes" if you want Claude to take action
* **State desired behaviors clearly**: Claude will follow instructions precisely, so being specific about what you want helps achieve better results

For comprehensive guidance on working with these models, see [Claude 4 prompt engineering best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices).

### Updated text editor tool

The text editor tool has been updated for Claude 4 models with the following changes:

* **Tool type**: `text_editor_20250728`
* **Tool name**: `str_replace_based_edit_tool`
* The `undo_edit` command is no longer supported

<Note>
  The `str_replace_editor` text editor tool remains the same for Claude Sonnet 3.7.
</Note>

If you're migrating from Claude Sonnet 3.7 and using the text editor tool:

```python  theme={null}
# Claude Sonnet 3.7
tools=[
    {
        "type": "text_editor_20250124",
        "name": "str_replace_editor"
    }
]

# Claude 4 models
tools=[
    {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
    }
]
```

For more information, see the [Text editor tool documentation](/en/docs/agents-and-tools/tool-use/text-editor-tool).

### Updated code execution tool

If you're using the code execution tool, ensure you're using the latest version `code_execution_20250825`, which adds Bash commands and file manipulation capabilities.

The legacy version `code_execution_20250522` (Python only) is still available but not recommended for new implementations.

For migration instructions, see the [Code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version).

## Pricing and availability

### Pricing

Claude 4.5 models maintain competitive pricing:

| Model             | Input                  | Output                  |
| ----------------- | ---------------------- | ----------------------- |
| Claude Sonnet 4.5 | \$3 per million tokens | \$15 per million tokens |
| Claude Haiku 4.5  | \$1 per million tokens | \$5 per million tokens  |

For more details, see the [pricing documentation](/en/docs/about-claude/pricing).

### Third-party platform pricing

Starting with Claude 4.5 models (Sonnet 4.5 and Haiku 4.5), AWS Bedrock and Google Vertex AI offer two endpoint types:

* **Global endpoints**: Dynamic routing for maximum availability
* **Regional endpoints**: Guaranteed data routing through specific geographic regions with a **10% pricing premium**

**This regional pricing applies to both Claude Sonnet 4.5 and Claude Haiku 4.5.**

**The Claude API (1P) is global by default and unaffected by this change.** The Claude API is global-only (equivalent to the global endpoint offering and pricing from other providers).

For implementation details and migration guidance:

* [AWS Bedrock global vs regional endpoints](/en/docs/build-with-claude/claude-on-amazon-bedrock#global-vs-regional-endpoints)
* [Google Vertex AI global vs regional endpoints](/en/docs/build-with-claude/claude-on-vertex-ai#global-vs-regional-endpoints)

### Availability

Claude 4.5 models are available on:

| Model             | Claude API                   | Amazon Bedrock                              | Google Cloud Vertex AI       |
| ----------------- | ---------------------------- | ------------------------------------------- | ---------------------------- |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` | `anthropic.claude-sonnet-4-5-20250929-v1:0` | `claude-sonnet-4-5@20250929` |
| Claude Haiku 4.5  | `claude-haiku-4-5-20251001`  | `anthropic.claude-haiku-4-5-20251001-v1:0`  | `claude-haiku-4-5@20251001`  |

Also available through Claude.ai and Claude Code platforms.

## Migration guide

Breaking changes and migration requirements vary depending on which model you're upgrading from. For detailed migration instructions, including step-by-step guides, breaking changes, and migration checklists, see [Migrating to Claude 4.5](/en/docs/about-claude/models/migrating-to-claude-4).

The migration guide covers the following scenarios:

* **Claude Sonnet 3.7 → Sonnet 4.5**: Complete migration path with breaking changes
* **Claude Haiku 3.5 → Haiku 4.5**: Complete migration path with breaking changes
* **Claude Sonnet 4 → Sonnet 4.5**: Quick upgrade with minimal changes
* **Claude Opus 4.1 → Sonnet 4.5**: Seamless upgrade with no breaking changes

## Next steps

<CardGroup cols={3}>
  <Card title="Best practices" icon="lightbulb" href="/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices">
    Learn prompt engineering techniques for Claude 4.5 models
  </Card>

  <Card title="Model overview" icon="table" href="/en/docs/about-claude/models/overview">
    Compare Claude 4.5 models with other Claude models
  </Card>

  <Card title="Migration guide" icon="arrow-right-arrow-left" href="/en/docs/about-claude/models/migrating-to-claude-4">
    Upgrade from previous models
  </Card>
</CardGroup>


# Pricing
Source: https://docs.claude.com/en/docs/about-claude/pricing

Learn about Anthropic's pricing structure for models and features

This page provides detailed pricing information for Anthropic's models and features. All prices are in USD.

For the most current pricing information, please visit [claude.com/pricing](https://claude.com/pricing).

## Model pricing

The following table shows pricing for all Claude models across different usage tiers:

| Model                                                                      | Base Input Tokens | 5m Cache Writes | 1h Cache Writes | Cache Hits & Refreshes | Output Tokens |
| -------------------------------------------------------------------------- | ----------------- | --------------- | --------------- | ---------------------- | ------------- |
| Claude Opus 4.1                                                            | \$15 / MTok       | \$18.75 / MTok  | \$30 / MTok     | \$1.50 / MTok          | \$75 / MTok   |
| Claude Opus 4                                                              | \$15 / MTok       | \$18.75 / MTok  | \$30 / MTok     | \$1.50 / MTok          | \$75 / MTok   |
| Claude Sonnet 4.5                                                          | \$3 / MTok        | \$3.75 / MTok   | \$6 / MTok      | \$0.30 / MTok          | \$15 / MTok   |
| Claude Sonnet 4                                                            | \$3 / MTok        | \$3.75 / MTok   | \$6 / MTok      | \$0.30 / MTok          | \$15 / MTok   |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | \$3 / MTok        | \$3.75 / MTok   | \$6 / MTok      | \$0.30 / MTok          | \$15 / MTok   |
| Claude Haiku 4.5                                                           | \$1 / MTok        | \$1.25 / MTok   | \$2 / MTok      | \$0.10 / MTok          | \$5 / MTok    |
| Claude Haiku 3.5                                                           | \$0.80 / MTok     | \$1 / MTok      | \$1.6 / MTok    | \$0.08 / MTok          | \$4 / MTok    |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | \$15 / MTok       | \$18.75 / MTok  | \$30 / MTok     | \$1.50 / MTok          | \$75 / MTok   |
| Claude Haiku 3                                                             | \$0.25 / MTok     | \$0.30 / MTok   | \$0.50 / MTok   | \$0.03 / MTok          | \$1.25 / MTok |

<Note>
  MTok = Million tokens. The "Base Input Tokens" column shows standard input pricing, "Cache Writes" and "Cache Hits" are specific to [prompt caching](/en/docs/build-with-claude/prompt-caching), and "Output Tokens" shows output pricing. Prompt caching offers both 5-minute (default) and 1-hour cache durations to optimize costs for different use cases.

  The table above reflects the following pricing multipliers for prompt caching:

  * 5-minute cache write tokens are 1.25 times the base input tokens price
  * 1-hour cache write tokens are 2 times the base input tokens price
  * Cache read tokens are 0.1 times the base input tokens price
</Note>

## Third-party platform pricing

Claude models are available on [AWS Bedrock](/en/docs/build-with-claude/claude-on-amazon-bedrock) and [Google Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai). For official pricing, visit:

* [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
* [Google Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)

<Note>
  **Regional endpoint pricing for Claude 4.5 models and beyond**

  Starting with Claude Sonnet 4.5 and Haiku 4.5, AWS Bedrock and Google Vertex AI offer two endpoint types:

  * **Global endpoints**: Dynamic routing across regions for maximum availability
  * **Regional endpoints**: Data routing guaranteed within specific geographic regions

  Regional endpoints include a 10% premium over global endpoints. **The Claude API (1P) is global by default and unaffected by this change.** The Claude API is global-only (equivalent to the global endpoint offering and pricing from other providers).

  **Scope**: This pricing structure applies to Claude Sonnet 4.5, Haiku 4.5, and all future models. Earlier models (Claude Sonnet 4, Opus 4, and prior releases) retain their existing pricing.

  For implementation details and code examples:

  * [AWS Bedrock global vs regional endpoints](/en/docs/build-with-claude/claude-on-amazon-bedrock#global-vs-regional-endpoints)
  * [Google Vertex AI global vs regional endpoints](/en/docs/build-with-claude/claude-on-vertex-ai#global-vs-regional-endpoints)
</Note>

## Feature-specific pricing

### Batch processing

The Batch API allows asynchronous processing of large volumes of requests with a 50% discount on both input and output tokens.

| Model                                                                      | Batch input    | Batch output   |
| -------------------------------------------------------------------------- | -------------- | -------------- |
| Claude Opus 4.1                                                            | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Opus 4                                                              | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Sonnet 4.5                                                          | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Sonnet 4                                                            | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Haiku 4.5                                                           | \$0.50 / MTok  | \$2.50 / MTok  |
| Claude Haiku 3.5                                                           | \$0.40 / MTok  | \$2 / MTok     |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Haiku 3                                                             | \$0.125 / MTok | \$0.625 / MTok |

For more information about batch processing, see our [batch processing documentation](/en/docs/build-with-claude/batch-processing).

### Long context pricing

When using Claude Sonnet 4 or Sonnet 4.5 with the [1M token context window enabled](/en/docs/build-with-claude/context-windows#1m-token-context-window), requests that exceed 200K input tokens are automatically charged at premium long context rates:

<Note>
  The 1M token context window is currently in beta for organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4 and Sonnet 4.5.
</Note>

| ≤ 200K input tokens | > 200K input tokens    |
| ------------------- | ---------------------- |
| Input: \$3 / MTok   | Input: \$6 / MTok      |
| Output: \$15 / MTok | Output: \$22.50 / MTok |

Long context pricing stacks with other pricing modifiers:

* The [Batch API 50% discount](#batch-processing) applies to long context pricing
* [Prompt caching multipliers](#model-pricing) apply on top of long context pricing

<Note>
  Even with the beta flag enabled, requests with fewer than 200K input tokens are charged at standard rates. If your request exceeds 200K input tokens, all tokens incur premium pricing.

  The 200K threshold is based solely on input tokens (including cache reads/writes). Output token count does not affect pricing tier selection, though output tokens are charged at the higher rate when the input threshold is exceeded.
</Note>

To check if your API request was charged at the 1M context window rates, examine the `usage` object in the API response:

```json  theme={null}
{
  "usage": {
    "input_tokens": 250000,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 500
  }
}
```

Calculate the total input tokens by summing:

* `input_tokens`
* `cache_creation_input_tokens` (if using prompt caching)
* `cache_read_input_tokens` (if using prompt caching)

If the total exceeds 200,000 tokens, the entire request was billed at 1M context rates.

For more information about the `usage` object, see the [API response documentation](/en/api/messages#response-usage).

### Tool use pricing

Tool use requests are priced based on:

1. The total number of input tokens sent to the model (including in the `tools` parameter)
2. The number of output tokens generated
3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.

The additional tokens from tool use come from:

* The `tools` parameter in API requests (tool names, descriptions, and schemas)
* `tool_use` content blocks in API requests and responses
* `tool_result` content blocks in API requests

When you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.

| Model                                                                      | Tool choice                                        | Tool use system prompt token count          |
| -------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------- |
| Claude Opus 4.1                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Opus 4                                                              | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 4.5                                                          | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 4                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Haiku 4.5                                                           | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Haiku 3.5                                                           | `auto`, `none`<hr className="my-2" />`any`, `tool` | 264 tokens<hr className="my-2" />340 tokens |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | `auto`, `none`<hr className="my-2" />`any`, `tool` | 530 tokens<hr className="my-2" />281 tokens |
| Claude Sonnet 3                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 159 tokens<hr className="my-2" />235 tokens |
| Claude Haiku 3                                                             | `auto`, `none`<hr className="my-2" />`any`, `tool` | 264 tokens<hr className="my-2" />340 tokens |

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

For current per-model prices, refer to our [model pricing](#model-pricing) section above.

For more information about tool use implementation and best practices, see our [tool use documentation](/en/docs/agents-and-tools/tool-use/overview).

### Specific tool pricing

#### Bash tool

The bash tool adds **245 input tokens** to your API calls.

Additional tokens are consumed by:

* Command outputs (stdout/stderr)
* Error messages
* Large file contents

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Code execution tool

Code execution tool usage is tracked separately from token usage. Execution time has a minimum of 5 minutes.
If files are included in the request, execution time is billed even if the tool is not used due to files being preloaded onto the container.

Each organization receives 50 free hours of usage with the code execution tool per day. Additional usage beyond the first 50 hours is billed at \$0.05 per hour, per container.

#### Text editor tool

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool                                                                                                | Additional input tokens |
| --------------------------------------------------------------------------------------------------- | ----------------------- |
| `text_editor_20250429` (Claude 4.x)                                                                 | 700 tokens              |
| `text_editor_20250124` (Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations))) | 700 tokens              |

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Web search tool

Web search usage is charged in addition to token usage:

```json  theme={null}
"usage": {
  "input_tokens": 105,
  "output_tokens": 6039,
  "cache_read_input_tokens": 7123,
  "cache_creation_input_tokens": 7345,
  "server_tool_use": {
    "web_search_requests": 1
  }
}
```

Web search is available on the Claude API for **\$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.

#### Web fetch tool

Web fetch usage has **no additional charges** beyond standard token costs:

```json  theme={null}
"usage": {
  "input_tokens": 25039,
  "output_tokens": 931,
  "cache_read_input_tokens": 0,
  "cache_creation_input_tokens": 0,
  "server_tool_use": {
    "web_fetch_requests": 1
  }
}
```

The web fetch tool is available on the Claude API at **no additional cost**. You only pay standard token costs for the fetched content that becomes part of your conversation context.

To protect against inadvertently fetching large content that would consume excessive tokens, use the `max_content_tokens` parameter to set appropriate limits based on your use case and budget considerations.

Example token usage for typical content:

* Average web page (10KB): \~2,500 tokens
* Large documentation page (100KB): \~25,000 tokens
* Research paper PDF (500KB): \~125,000 tokens

#### Computer use tool

Computer use follows the standard [tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**System prompt overhead**: The computer use beta adds 466-499 tokens to the system prompt

**Computer use tool token usage**:

| Model                                                                      | Input tokens per tool definition |
| -------------------------------------------------------------------------- | -------------------------------- |
| Claude 4.x models                                                          | 735 tokens                       |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 735 tokens                       |

**Additional token consumption**:

* Screenshot images (see [Vision pricing](/en/docs/build-with-claude/vision))
* Tool execution results returned to Claude

<Note>
  If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.
</Note>

## Agent use case pricing examples

Understanding pricing for agent applications is crucial when building with Claude. These real-world examples can help you estimate costs for different agent patterns.

### Customer support agent example

When building a customer support agent, here's how costs might break down:

<Note>
  Example calculation for processing 10,000 support tickets:

  * Average \~3,700 tokens per conversation
  * Using Claude Sonnet 4.5 at $3/MTok input, $15/MTok output
  * Total cost: \~\$22.20 per 10,000 tickets
</Note>

For a detailed walkthrough of this calculation, see our [customer support agent guide](/en/docs/about-claude/use-case-guides/customer-support-chat).

### General agent workflow pricing

For more complex agent architectures with multiple steps:

1. **Initial request processing**
   * Typical input: 500-1,000 tokens
   * Processing cost: \~\$0.003 per request

2. **Memory and context retrieval**
   * Retrieved context: 2,000-5,000 tokens
   * Cost per retrieval: \~\$0.015 per operation

3. **Action planning and execution**
   * Planning tokens: 1,000-2,000
   * Execution feedback: 500-1,000
   * Combined cost: \~\$0.045 per action

For a comprehensive guide on agent pricing patterns, see our [agent use cases guide](/en/docs/about-claude/use-case-guides).

### Cost optimization strategies

When building agents with Claude:

1. **Use appropriate models**: Choose Haiku for simple tasks, Sonnet for complex reasoning
2. **Implement prompt caching**: Reduce costs for repeated context
3. **Batch operations**: Use the Batch API for non-time-sensitive tasks
4. **Monitor usage patterns**: Track token consumption to identify optimization opportunities

<Tip>
  For high-volume agent applications, consider contacting our [enterprise sales team](https://claude.com/contact-sales) for custom pricing arrangements.
</Tip>

## Additional pricing considerations

### Rate limits

Rate limits vary by usage tier and affect how many requests you can make:

* **Tier 1**: Entry-level usage with basic limits
* **Tier 2**: Increased limits for growing applications
* **Tier 3**: Higher limits for established applications
* **Tier 4**: Maximum standard limits
* **Enterprise**: Custom limits available

For detailed rate limit information, see our [rate limits documentation](/en/api/rate-limits).

For higher rate limits or custom pricing arrangements, [contact our sales team](https://claude.com/contact-sales).

### Volume discounts

Volume discounts may be available for high-volume users. These are negotiated on a case-by-case basis.

* Standard tiers use the pricing shown above
* Enterprise customers can [contact sales](mailto:sales@anthropic.com) for custom pricing
* Academic and research discounts may be available

### Enterprise pricing

For enterprise customers with specific needs:

* Custom rate limits
* Volume discounts
* Dedicated support
* Custom terms

Contact our sales team at [sales@anthropic.com](mailto:sales@anthropic.com) or through the [Claude Console](https://console.anthropic.com/settings/limits) to discuss enterprise pricing options.

## Billing and payment

* Billing is calculated monthly based on actual usage
* Payments are processed in USD
* Credit card and invoicing options available
* Usage tracking available in the [Claude Console](https://console.anthropic.com)

## Frequently asked questions

**How is token usage calculated?**

Tokens are pieces of text that models process. As a rough estimate, 1 token is approximately 4 characters or 0.75 words in English. The exact count varies by language and content type.

**Are there free tiers or trials?**

New users receive a small amount of free credits to test the API. [Contact sales](mailto:sales@anthropic.com) for information about extended trials for enterprise evaluation.

**How do discounts stack?**

Batch API and prompt caching discounts can be combined. For example, using both features together provides significant cost savings compared to standard API calls.

**What payment methods are accepted?**

We accept major credit cards for standard accounts. Enterprise customers can arrange invoicing and other payment methods.

For additional questions about pricing, contact [support@anthropic.com](mailto:support@anthropic.com).


# Tracking Costs and Usage
Source: https://docs.claude.com/en/docs/agent-sdk/cost-tracking

Understand and track token usage for billing in the Claude Agent SDK

# SDK Cost Tracking

The Claude Agent SDK provides detailed token usage information for each interaction with Claude. This guide explains how to properly track costs and understand usage reporting, especially when dealing with parallel tool uses and multi-step conversations.

For complete API documentation, see the [TypeScript SDK reference](https://code.claude.com/docs/typescript).

## Understanding Token Usage

When Claude processes requests, it reports token usage at the message level. This usage data is essential for tracking costs and billing users appropriately.

### Key Concepts

1. **Steps**: A step is a single request/response pair between your application and Claude
2. **Messages**: Individual messages within a step (text, tool uses, tool results)
3. **Usage**: Token consumption data attached to assistant messages

## Usage Reporting Structure

### Single vs Parallel Tool Use

When Claude executes tools, the usage reporting differs based on whether tools are executed sequentially or in parallel:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Example: Tracking usage in a conversation
  const result = await query({
    prompt: "Analyze this codebase and run tests",
    options: {
      onMessage: (message) => {
        if (message.type === 'assistant' && message.usage) {
          console.log(`Message ID: ${message.id}`);
          console.log(`Usage:`, message.usage);
        }
      }
    }
  });
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage
  import asyncio

  # Example: Tracking usage in a conversation
  async def track_usage():
      # Process messages as they arrive
      async for message in query(
          prompt="Analyze this codebase and run tests"
      ):
          if isinstance(message, AssistantMessage) and hasattr(message, 'usage'):
              print(f"Message ID: {message.id}")
              print(f"Usage: {message.usage}")

  asyncio.run(track_usage())
  ```
</CodeGroup>

### Message Flow Example

Here's how messages and usage are reported in a typical multi-step conversation:

```
<!-- Step 1: Initial request with parallel tool uses -->
assistant (text)      { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
user (tool_result)
user (tool_result)
user (tool_result)

<!-- Step 2: Follow-up response -->
assistant (text)      { id: "msg_2", usage: { output_tokens: 98, ... } }
```

## Important Usage Rules

### 1. Same ID = Same Usage

**All messages with the same `id` field report identical usage**. When Claude sends multiple messages in the same turn (e.g., text + tool uses), they share the same message ID and usage data.

```typescript  theme={null}
// All these messages have the same ID and usage
const messages = [
  { type: 'assistant', id: 'msg_123', usage: { output_tokens: 100 } },
  { type: 'assistant', id: 'msg_123', usage: { output_tokens: 100 } },
  { type: 'assistant', id: 'msg_123', usage: { output_tokens: 100 } }
];

// Charge only once per unique message ID
const uniqueUsage = messages[0].usage; // Same for all messages with this ID
```

### 2. Charge Once Per Step

**You should only charge users once per step**, not for each individual message. When you see multiple assistant messages with the same ID, use the usage from any one of them.

### 3. Result Message Contains Cumulative Usage

The final `result` message contains the total cumulative usage from all steps in the conversation:

```typescript  theme={null}
// Final result includes total usage
const result = await query({
  prompt: "Multi-step task",
  options: { /* ... */ }
});

console.log("Total usage:", result.usage);
console.log("Total cost:", result.usage.total_cost_usd);
```

## Implementation: Cost Tracking System

Here's a complete example of implementing a cost tracking system:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  class CostTracker {
    private processedMessageIds = new Set<string>();
    private stepUsages: Array<any> = [];
    
    async trackConversation(prompt: string) {
      const result = await query({
        prompt,
        options: {
          onMessage: (message) => {
            this.processMessage(message);
          }
        }
      });
      
      return {
        result,
        stepUsages: this.stepUsages,
        totalCost: result.usage?.total_cost_usd || 0
      };
    }
    
    private processMessage(message: any) {
      // Only process assistant messages with usage
      if (message.type !== 'assistant' || !message.usage) {
        return;
      }
      
      // Skip if we've already processed this message ID
      if (this.processedMessageIds.has(message.id)) {
        return;
      }
      
      // Mark as processed and record usage
      this.processedMessageIds.add(message.id);
      this.stepUsages.push({
        messageId: message.id,
        timestamp: new Date().toISOString(),
        usage: message.usage,
        costUSD: this.calculateCost(message.usage)
      });
    }
    
    private calculateCost(usage: any): number {
      // Implement your pricing calculation here
      // This is a simplified example
      const inputCost = usage.input_tokens * 0.00003;
      const outputCost = usage.output_tokens * 0.00015;
      const cacheReadCost = (usage.cache_read_input_tokens || 0) * 0.0000075;
      
      return inputCost + outputCost + cacheReadCost;
    }
  }

  // Usage
  const tracker = new CostTracker();
  const { result, stepUsages, totalCost } = await tracker.trackConversation(
    "Analyze and refactor this code"
  );

  console.log(`Steps processed: ${stepUsages.length}`);
  console.log(`Total cost: $${totalCost.toFixed(4)}`);
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, AssistantMessage, ResultMessage
  from datetime import datetime
  import asyncio

  class CostTracker:
      def __init__(self):
          self.processed_message_ids = set()
          self.step_usages = []

      async def track_conversation(self, prompt):
          result = None

          # Process messages as they arrive
          async for message in query(prompt=prompt):
              self.process_message(message)

              # Capture the final result message
              if isinstance(message, ResultMessage):
                  result = message

          return {
              "result": result,
              "step_usages": self.step_usages,
              "total_cost": result.total_cost_usd if result else 0
          }

      def process_message(self, message):
          # Only process assistant messages with usage
          if not isinstance(message, AssistantMessage) or not hasattr(message, 'usage'):
              return

          # Skip if already processed this message ID
          message_id = getattr(message, 'id', None)
          if not message_id or message_id in self.processed_message_ids:
              return

          # Mark as processed and record usage
          self.processed_message_ids.add(message_id)
          self.step_usages.append({
              "message_id": message_id,
              "timestamp": datetime.now().isoformat(),
              "usage": message.usage,
              "cost_usd": self.calculate_cost(message.usage)
          })

      def calculate_cost(self, usage):
          # Implement your pricing calculation
          input_cost = usage.get("input_tokens", 0) * 0.00003
          output_cost = usage.get("output_tokens", 0) * 0.00015
          cache_read_cost = usage.get("cache_read_input_tokens", 0) * 0.0000075

          return input_cost + output_cost + cache_read_cost

  # Usage
  async def main():
      tracker = CostTracker()
      result = await tracker.track_conversation("Analyze and refactor this code")

      print(f"Steps processed: {len(result['step_usages'])}")
      print(f"Total cost: ${result['total_cost']:.4f}")

  asyncio.run(main())
  ```
</CodeGroup>

## Handling Edge Cases

### Output Token Discrepancies

In rare cases, you might observe different `output_tokens` values for messages with the same ID. When this occurs:

1. **Use the highest value** - The final message in a group typically contains the accurate total
2. **Verify against total cost** - The `total_cost_usd` in the result message is authoritative
3. **Report inconsistencies** - File issues at the [Claude Code GitHub repository](https://github.com/anthropics/claude-code/issues)

### Cache Token Tracking

When using prompt caching, track these token types separately:

```typescript  theme={null}
interface CacheUsage {
  cache_creation_input_tokens: number;
  cache_read_input_tokens: number;
  cache_creation: {
    ephemeral_5m_input_tokens: number;
    ephemeral_1h_input_tokens: number;
  };
}
```

## Best Practices

1. **Use Message IDs for Deduplication**: Always track processed message IDs to avoid double-charging
2. **Monitor the Result Message**: The final result contains authoritative cumulative usage
3. **Implement Logging**: Log all usage data for auditing and debugging
4. **Handle Failures Gracefully**: Track partial usage even if a conversation fails
5. **Consider Streaming**: For streaming responses, accumulate usage as messages arrive

## Usage Fields Reference

Each usage object contains:

* `input_tokens`: Base input tokens processed
* `output_tokens`: Tokens generated in the response
* `cache_creation_input_tokens`: Tokens used to create cache entries
* `cache_read_input_tokens`: Tokens read from cache
* `service_tier`: The service tier used (e.g., "standard")
* `total_cost_usd`: Total cost in USD (only in result message)

## Example: Building a Billing Dashboard

Here's how to aggregate usage data for a billing dashboard:

```typescript  theme={null}
class BillingAggregator {
  private userUsage = new Map<string, {
    totalTokens: number;
    totalCost: number;
    conversations: number;
  }>();
  
  async processUserRequest(userId: string, prompt: string) {
    const tracker = new CostTracker();
    const { result, stepUsages, totalCost } = await tracker.trackConversation(prompt);
    
    // Update user totals
    const current = this.userUsage.get(userId) || {
      totalTokens: 0,
      totalCost: 0,
      conversations: 0
    };
    
    const totalTokens = stepUsages.reduce((sum, step) => 
      sum + step.usage.input_tokens + step.usage.output_tokens, 0
    );
    
    this.userUsage.set(userId, {
      totalTokens: current.totalTokens + totalTokens,
      totalCost: current.totalCost + totalCost,
      conversations: current.conversations + 1
    });
    
    return result;
  }
  
  getUserBilling(userId: string) {
    return this.userUsage.get(userId) || {
      totalTokens: 0,
      totalCost: 0,
      conversations: 0
    };
  }
}
```

## Related Documentation

* [TypeScript SDK Reference](https://code.claude.com/docs/typescript) - Complete API documentation
* [SDK Overview](/en/docs/agent-sdk/overview) - Getting started with the SDK
* [SDK Permissions](/en/docs/agent-sdk/permissions) - Managing tool permissions


# Custom Tools
Source: https://docs.claude.com/en/docs/agent-sdk/custom-tools

Build and integrate custom tools to extend Claude Agent SDK functionality

Custom tools allow you to extend Claude Code's capabilities with your own functionality through in-process MCP servers, enabling Claude to interact with external services, APIs, or perform specialized operations.

## Creating Custom Tools

Use the `createSdkMcpServer` and `tool` helper functions to define type-safe custom tools:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
  import { z } from "zod";

  // Create an SDK MCP server with custom tools
  const customServer = createSdkMcpServer({
    name: "my-custom-tools",
    version: "1.0.0",
    tools: [
      tool(
        "get_weather",
        "Get current temperature for a location using coordinates",
        {
          latitude: z.number().describe("Latitude coordinate"),
          longitude: z.number().describe("Longitude coordinate")
        },
        async (args) => {
          const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&current=temperature_2m&temperature_unit=fahrenheit`);
          const data = await response.json();

          return {
            content: [{
              type: "text",
              text: `Temperature: ${data.current.temperature_2m}°F`
            }]
          };
        }
      )
    ]
  });
  ```

  ```python Python theme={null}
  from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeSDKClient, ClaudeAgentOptions
  from typing import Any
  import aiohttp

  # Define a custom tool using the @tool decorator
  @tool("get_weather", "Get current temperature for a location using coordinates", {"latitude": float, "longitude": float})
  async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
      # Call weather API
      async with aiohttp.ClientSession() as session:
          async with session.get(
              f"https://api.open-meteo.com/v1/forecast?latitude={args['latitude']}&longitude={args['longitude']}&current=temperature_2m&temperature_unit=fahrenheit"
          ) as response:
              data = await response.json()

      return {
          "content": [{
              "type": "text",
              "text": f"Temperature: {data['current']['temperature_2m']}°F"
          }]
      }

  # Create an SDK MCP server with the custom tool
  custom_server = create_sdk_mcp_server(
      name="my-custom-tools",
      version="1.0.0",
      tools=[get_weather]  # Pass the decorated function
  )
  ```
</CodeGroup>

## Using Custom Tools

Pass the custom server to the `query` function via the `mcpServers` option as a dictionary/object.

<Note>
  **Important:** Custom MCP tools require streaming input mode. You must use an async generator/iterable for the `prompt` parameter - a simple string will not work with MCP servers.
</Note>

### Tool Name Format

When MCP tools are exposed to Claude, their names follow a specific format:

* Pattern: `mcp__{server_name}__{tool_name}`
* Example: A tool named `get_weather` in server `my-custom-tools` becomes `mcp__my-custom-tools__get_weather`

### Configuring Allowed Tools

You can control which tools Claude can use via the `allowedTools` option:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Use the custom tools in your query with streaming input
  async function* generateMessages() {
    yield {
      type: "user" as const,
      message: {
        role: "user" as const,
        content: "What's the weather in San Francisco?"
      }
    };
  }

  for await (const message of query({
    prompt: generateMessages(),  // Use async generator for streaming input
    options: {
      mcpServers: {
        "my-custom-tools": customServer  // Pass as object/dictionary, not array
      },
      // Optionally specify which tools Claude can use
      allowedTools: [
        "mcp__my-custom-tools__get_weather",  // Allow the weather tool
        // Add other tools as needed
      ],
      maxTurns: 3
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
  import asyncio

  # Use the custom tools with Claude
  options = ClaudeAgentOptions(
      mcp_servers={"my-custom-tools": custom_server},
      allowed_tools=[
          "mcp__my-custom-tools__get_weather",  # Allow the weather tool
          # Add other tools as needed
      ]
  )

  async def main():
      async with ClaudeSDKClient(options=options) as client:
          await client.query("What's the weather in San Francisco?")

          # Extract and print response
          async for msg in client.receive_response():
              print(msg)

  asyncio.run(main())
  ```
</CodeGroup>

### Multiple Tools Example

When your MCP server has multiple tools, you can selectively allow them:

<CodeGroup>
  ```typescript TypeScript theme={null}
  const multiToolServer = createSdkMcpServer({
    name: "utilities",
    version: "1.0.0",
    tools: [
      tool("calculate", "Perform calculations", { /* ... */ }, async (args) => { /* ... */ }),
      tool("translate", "Translate text", { /* ... */ }, async (args) => { /* ... */ }),
      tool("search_web", "Search the web", { /* ... */ }, async (args) => { /* ... */ })
    ]
  });

  // Allow only specific tools with streaming input
  async function* generateMessages() {
    yield {
      type: "user" as const,
      message: {
        role: "user" as const,
        content: "Calculate 5 + 3 and translate 'hello' to Spanish"
      }
    };
  }

  for await (const message of query({
    prompt: generateMessages(),  // Use async generator for streaming input
    options: {
      mcpServers: {
        utilities: multiToolServer
      },
      allowedTools: [
        "mcp__utilities__calculate",   // Allow calculator
        "mcp__utilities__translate",   // Allow translator
        // "mcp__utilities__search_web" is NOT allowed
      ]
    }
  })) {
    // Process messages
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, tool, create_sdk_mcp_server
  from typing import Any
  import asyncio

  # Define multiple tools using the @tool decorator
  @tool("calculate", "Perform calculations", {"expression": str})
  async def calculate(args: dict[str, Any]) -> dict[str, Any]:
      result = eval(args["expression"])  # Use safe eval in production
      return {"content": [{"type": "text", "text": f"Result: {result}"}]}

  @tool("translate", "Translate text", {"text": str, "target_lang": str})
  async def translate(args: dict[str, Any]) -> dict[str, Any]:
      # Translation logic here
      return {"content": [{"type": "text", "text": f"Translated: {args['text']}"}]}

  @tool("search_web", "Search the web", {"query": str})
  async def search_web(args: dict[str, Any]) -> dict[str, Any]:
      # Search logic here
      return {"content": [{"type": "text", "text": f"Search results for: {args['query']}"}]}

  multi_tool_server = create_sdk_mcp_server(
      name="utilities",
      version="1.0.0",
      tools=[calculate, translate, search_web]  # Pass decorated functions
  )

  # Allow only specific tools with streaming input
  async def message_generator():
      yield {
          "type": "user",
          "message": {
              "role": "user",
              "content": "Calculate 5 + 3 and translate 'hello' to Spanish"
          }
      }

  async for message in query(
      prompt=message_generator(),  # Use async generator for streaming input
      options=ClaudeAgentOptions(
          mcp_servers={"utilities": multi_tool_server},
          allowed_tools=[
              "mcp__utilities__calculate",   # Allow calculator
              "mcp__utilities__translate",   # Allow translator
              # "mcp__utilities__search_web" is NOT allowed
          ]
      )
  ):
      if hasattr(message, 'result'):
          print(message.result)
  ```
</CodeGroup>

## Type Safety with Python

The `@tool` decorator supports various schema definition approaches for type safety:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { z } from "zod";

  tool(
    "process_data",
    "Process structured data with type safety",
    {
      // Zod schema defines both runtime validation and TypeScript types
      data: z.object({
        name: z.string(),
        age: z.number().min(0).max(150),
        email: z.string().email(),
        preferences: z.array(z.string()).optional()
      }),
      format: z.enum(["json", "csv", "xml"]).default("json")
    },
    async (args) => {
      // args is fully typed based on the schema
      // TypeScript knows: args.data.name is string, args.data.age is number, etc.
      console.log(`Processing ${args.data.name}'s data as ${args.format}`);
      
      // Your processing logic here
      return {
        content: [{
          type: "text",
          text: `Processed data for ${args.data.name}`
        }]
      };
    }
  )
  ```

  ```python Python theme={null}
  from typing import Any

  # Simple type mapping - recommended for most cases
  @tool(
      "process_data",
      "Process structured data with type safety",
      {
          "name": str,
          "age": int,
          "email": str,
          "preferences": list  # Optional parameters can be handled in the function
      }
  )
  async def process_data(args: dict[str, Any]) -> dict[str, Any]:
      # Access arguments with type hints for IDE support
      name = args["name"]
      age = args["age"]
      email = args["email"]
      preferences = args.get("preferences", [])
      
      print(f"Processing {name}'s data (age: {age})")
      
      return {
          "content": [{
              "type": "text",
              "text": f"Processed data for {name}"
          }]
      }

  # For more complex schemas, you can use JSON Schema format
  @tool(
      "advanced_process",
      "Process data with advanced validation",
      {
          "type": "object",
          "properties": {
              "name": {"type": "string"},
              "age": {"type": "integer", "minimum": 0, "maximum": 150},
              "email": {"type": "string", "format": "email"},
              "format": {"type": "string", "enum": ["json", "csv", "xml"], "default": "json"}
          },
          "required": ["name", "age", "email"]
      }
  )
  async def advanced_process(args: dict[str, Any]) -> dict[str, Any]:
      # Process with advanced schema validation
      return {
          "content": [{
              "type": "text",
              "text": f"Advanced processing for {args['name']}"
          }]
      }
  ```
</CodeGroup>

## Error Handling

Handle errors gracefully to provide meaningful feedback:

<CodeGroup>
  ```typescript TypeScript theme={null}
  tool(
    "fetch_data",
    "Fetch data from an API",
    {
      endpoint: z.string().url().describe("API endpoint URL")
    },
    async (args) => {
      try {
        const response = await fetch(args.endpoint);
        
        if (!response.ok) {
          return {
            content: [{
              type: "text",
              text: `API error: ${response.status} ${response.statusText}`
            }]
          };
        }
        
        const data = await response.json();
        return {
          content: [{
            type: "text",
            text: JSON.stringify(data, null, 2)
          }]
        };
      } catch (error) {
        return {
          content: [{
            type: "text",
            text: `Failed to fetch data: ${error.message}`
          }]
        };
      }
    }
  )
  ```

  ```python Python theme={null}
  import json
  import aiohttp
  from typing import Any

  @tool(
      "fetch_data",
      "Fetch data from an API",
      {"endpoint": str}  # Simple schema
  )
  async def fetch_data(args: dict[str, Any]) -> dict[str, Any]:
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(args["endpoint"]) as response:
                  if response.status != 200:
                      return {
                          "content": [{
                              "type": "text",
                              "text": f"API error: {response.status} {response.reason}"
                          }]
                      }
                  
                  data = await response.json()
                  return {
                      "content": [{
                          "type": "text",
                          "text": json.dumps(data, indent=2)
                      }]
                  }
      except Exception as e:
          return {
              "content": [{
                  "type": "text",
                  "text": f"Failed to fetch data: {str(e)}"
              }]
          }
  ```
</CodeGroup>

## Example Tools

### Database Query Tool

<CodeGroup>
  ```typescript TypeScript theme={null}
  const databaseServer = createSdkMcpServer({
    name: "database-tools",
    version: "1.0.0",
    tools: [
      tool(
        "query_database",
        "Execute a database query",
        {
          query: z.string().describe("SQL query to execute"),
          params: z.array(z.any()).optional().describe("Query parameters")
        },
        async (args) => {
          const results = await db.query(args.query, args.params || []);
          return {
            content: [{
              type: "text",
              text: `Found ${results.length} rows:\n${JSON.stringify(results, null, 2)}`
            }]
          };
        }
      )
    ]
  });
  ```

  ```python Python theme={null}
  from typing import Any
  import json

  @tool(
      "query_database",
      "Execute a database query",
      {"query": str, "params": list}  # Simple schema with list type
  )
  async def query_database(args: dict[str, Any]) -> dict[str, Any]:
      results = await db.query(args["query"], args.get("params", []))
      return {
          "content": [{
              "type": "text",
              "text": f"Found {len(results)} rows:\n{json.dumps(results, indent=2)}"
          }]
      }

  database_server = create_sdk_mcp_server(
      name="database-tools",
      version="1.0.0",
      tools=[query_database]  # Pass the decorated function
  )
  ```
</CodeGroup>

### API Gateway Tool

<CodeGroup>
  ```typescript TypeScript theme={null}
  const apiGatewayServer = createSdkMcpServer({
    name: "api-gateway",
    version: "1.0.0",
    tools: [
      tool(
        "api_request",
        "Make authenticated API requests to external services",
        {
          service: z.enum(["stripe", "github", "openai", "slack"]).describe("Service to call"),
          endpoint: z.string().describe("API endpoint path"),
          method: z.enum(["GET", "POST", "PUT", "DELETE"]).describe("HTTP method"),
          body: z.record(z.any()).optional().describe("Request body"),
          query: z.record(z.string()).optional().describe("Query parameters")
        },
        async (args) => {
          const config = {
            stripe: { baseUrl: "https://api.stripe.com/v1", key: process.env.STRIPE_KEY },
            github: { baseUrl: "https://api.github.com", key: process.env.GITHUB_TOKEN },
            openai: { baseUrl: "https://api.openai.com/v1", key: process.env.OPENAI_KEY },
            slack: { baseUrl: "https://slack.com/api", key: process.env.SLACK_TOKEN }
          };
          
          const { baseUrl, key } = config[args.service];
          const url = new URL(`${baseUrl}${args.endpoint}`);
          
          if (args.query) {
            Object.entries(args.query).forEach(([k, v]) => url.searchParams.set(k, v));
          }
          
          const response = await fetch(url, {
            method: args.method,
            headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
            body: args.body ? JSON.stringify(args.body) : undefined
          });
          
          const data = await response.json();
          return {
            content: [{
              type: "text",
              text: JSON.stringify(data, null, 2)
            }]
          };
        }
      )
    ]
  });
  ```

  ```python Python theme={null}
  import os
  import json
  import aiohttp
  from typing import Any

  # For complex schemas with enums, use JSON Schema format
  @tool(
      "api_request",
      "Make authenticated API requests to external services",
      {
          "type": "object",
          "properties": {
              "service": {"type": "string", "enum": ["stripe", "github", "openai", "slack"]},
              "endpoint": {"type": "string"},
              "method": {"type": "string", "enum": ["GET", "POST", "PUT", "DELETE"]},
              "body": {"type": "object"},
              "query": {"type": "object"}
          },
          "required": ["service", "endpoint", "method"]
      }
  )
  async def api_request(args: dict[str, Any]) -> dict[str, Any]:
      config = {
          "stripe": {"base_url": "https://api.stripe.com/v1", "key": os.environ["STRIPE_KEY"]},
          "github": {"base_url": "https://api.github.com", "key": os.environ["GITHUB_TOKEN"]},
          "openai": {"base_url": "https://api.openai.com/v1", "key": os.environ["OPENAI_KEY"]},
          "slack": {"base_url": "https://slack.com/api", "key": os.environ["SLACK_TOKEN"]}
      }
      
      service_config = config[args["service"]]
      url = f"{service_config['base_url']}{args['endpoint']}"
      
      if args.get("query"):
          params = "&".join([f"{k}={v}" for k, v in args["query"].items()])
          url += f"?{params}"
      
      headers = {"Authorization": f"Bearer {service_config['key']}", "Content-Type": "application/json"}
      
      async with aiohttp.ClientSession() as session:
          async with session.request(
              args["method"], url, headers=headers, json=args.get("body")
          ) as response:
              data = await response.json()
              return {
                  "content": [{
                      "type": "text",
                      "text": json.dumps(data, indent=2)
                  }]
              }

  api_gateway_server = create_sdk_mcp_server(
      name="api-gateway",
      version="1.0.0",
      tools=[api_request]  # Pass the decorated function
  )
  ```
</CodeGroup>

### Calculator Tool

<CodeGroup>
  ```typescript TypeScript theme={null}
  const calculatorServer = createSdkMcpServer({
    name: "calculator",
    version: "1.0.0",
    tools: [
      tool(
        "calculate",
        "Perform mathematical calculations",
        {
          expression: z.string().describe("Mathematical expression to evaluate"),
          precision: z.number().optional().default(2).describe("Decimal precision")
        },
        async (args) => {
          try {
            // Use a safe math evaluation library in production
            const result = eval(args.expression); // Example only!
            const formatted = Number(result).toFixed(args.precision);
            
            return {
              content: [{
                type: "text",
                text: `${args.expression} = ${formatted}`
              }]
            };
          } catch (error) {
            return {
              content: [{
                type: "text",
                text: `Error: Invalid expression - ${error.message}`
              }]
            };
          }
        }
      ),
      tool(
        "compound_interest",
        "Calculate compound interest for an investment",
        {
          principal: z.number().positive().describe("Initial investment amount"),
          rate: z.number().describe("Annual interest rate (as decimal, e.g., 0.05 for 5%)"),
          time: z.number().positive().describe("Investment period in years"),
          n: z.number().positive().default(12).describe("Compounding frequency per year")
        },
        async (args) => {
          const amount = args.principal * Math.pow(1 + args.rate / args.n, args.n * args.time);
          const interest = amount - args.principal;
          
          return {
            content: [{
              type: "text",
              text: `Investment Analysis:\n` +
                    `Principal: $${args.principal.toFixed(2)}\n` +
                    `Rate: ${(args.rate * 100).toFixed(2)}%\n` +
                    `Time: ${args.time} years\n` +
                    `Compounding: ${args.n} times per year\n\n` +
                    `Final Amount: $${amount.toFixed(2)}\n` +
                    `Interest Earned: $${interest.toFixed(2)}\n` +
                    `Return: ${((interest / args.principal) * 100).toFixed(2)}%`
            }]
          };
        }
      )
    ]
  });
  ```

  ```python Python theme={null}
  import math
  from typing import Any

  @tool(
      "calculate",
      "Perform mathematical calculations",
      {"expression": str, "precision": int}  # Simple schema
  )
  async def calculate(args: dict[str, Any]) -> dict[str, Any]:
      try:
          # Use a safe math evaluation library in production
          result = eval(args["expression"], {"__builtins__": {}})
          precision = args.get("precision", 2)
          formatted = round(result, precision)
          
          return {
              "content": [{
                  "type": "text",
                  "text": f"{args['expression']} = {formatted}"
              }]
          }
      except Exception as e:
          return {
              "content": [{
                  "type": "text",
                  "text": f"Error: Invalid expression - {str(e)}"
              }]
          }

  @tool(
      "compound_interest",
      "Calculate compound interest for an investment",
      {"principal": float, "rate": float, "time": float, "n": int}
  )
  async def compound_interest(args: dict[str, Any]) -> dict[str, Any]:
      principal = args["principal"]
      rate = args["rate"]
      time = args["time"]
      n = args.get("n", 12)
      
      amount = principal * (1 + rate / n) ** (n * time)
      interest = amount - principal
      
      return {
          "content": [{
              "type": "text",
              "text": f"""Investment Analysis:
  Principal: ${principal:.2f}
  Rate: {rate * 100:.2f}%
  Time: {time} years
  Compounding: {n} times per year

  Final Amount: ${amount:.2f}
  Interest Earned: ${interest:.2f}
  Return: {(interest / principal) * 100:.2f}%"""
          }]
      }

  calculator_server = create_sdk_mcp_server(
      name="calculator",
      version="1.0.0",
      tools=[calculate, compound_interest]  # Pass decorated functions
  )
  ```
</CodeGroup>

## Related Documentation

* [TypeScript SDK Reference](/en/docs/agent-sdk/typescript)
* [Python SDK Reference](/en/docs/agent-sdk/python)
* [MCP Documentation](https://modelcontextprotocol.io)
* [SDK Overview](/en/docs/agent-sdk/overview)



---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-hosting-the-agent-sdk.md)
