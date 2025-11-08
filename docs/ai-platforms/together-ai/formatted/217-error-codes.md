---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error Codes

Source: https://docs.together.ai/docs/error-codes

An overview on error status codes, causes, and quick fix solutions

| Code                       | Cause                                                                                                                                 | Solution                                                                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400 - Invalid Request      | Misconfigured request                                                                                                                 | Ensure your request is a [Valid JSON](/docs/inference-rest#create-your-json-formatted-object) and your [API Key](https://api.together.xyz/settings/api-keys) is correct. Also ensure you're using the right prompt format - which is different for Mistral and LLaMA models. |
| 401 - Authentication Error | Missing or Invalid API Key                                                                                                            | Ensure you are using the correct [API Key](https://api.together.xyz/settings/api-keys) and [supplying it correctly](/reference/inference)                                                                                                                                    |
| 402 - Payment Required     | The account associated with the API key has reached its maximum allowed monthly spending limit.                                       | Adjust your [billing settings](https://api.together.xyz/settings/billing) or make a payment to resume service.                                                                                                                                                               |
| 403 - Bad Request          | Input token count + `max_tokens` parameter must be less than the [context](/docs/inference-models) length of the model being queried. | Set `max_tokens` to a lower number. If querying a chat model, you may set `max_tokens` to `null` and let the model decide when to stop generation.                                                                                                                           |
| 404 - Not Found            | Invalid Endpoint URL or model name                                                                                                    | Check your request is being made to the correct endpoint (see the [API reference](/reference/inference) page for details) and that the [model being queried is available](/docs/inference-models)                                                                            |
| 429 - Rate limit           | Too many requests sent in a short period of time                                                                                      | Throttle the rate at which requests are sent to our servers (see our [rate limits](/docs/rate-limits))                                                                                                                                                                       |
| 500 - Server Error         | Unknown server error                                                                                                                  | This error is caused by an issue on our servers. Please try again after a brief wait. If the issue persists, please [contact support](https://www.together.ai/contact)                                                                                                       |
| 503 - Engine Overloaded    | Our servers are seeing high amounts of traffic                                                                                        | Please try again after a brief wait. If the issue persists, please [contact support](https://www.together.ai/contact)                                                                                                                                                        |

If you are seeing other error codes or the solutions do not work, please [contact support](https://www.together.ai/contact) for help.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
