---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common Error Codes During Fine-Tuning

| Code | Cause                                                                   | Solution                                                                                                          |
| ---- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 401  | Missing or Invalid API Key                                              | Ensure you are using the correct [API Key](https://api.together.xyz/settings/api-keys) and supplying it correctly |
| 403  | Input token count + `max_tokens` parameter exceeds model context length | Set `max_tokens` to a lower number. For chat models, you may set `max_tokens` to `null`                           |
| 404  | Invalid Endpoint URL or model name                                      | Check your request is made to the correct endpoint and the model is available                                     |
| 429  | Rate limit exceeded                                                     | Throttle request rate (see [rate limits](https://docs.together.ai/docs/rate-limits))                              |
| 500  | Invalid Request                                                         | Ensure valid JSON, correct API key, and proper prompt format for the model type                                   |
| 503  | Engine Overloaded                                                       | Try again after a brief wait. Contact support if persistent                                                       |
| 504  | Timeout                                                                 | Try again after a brief wait. Contact support if persistent                                                       |
| 524  | Cloudflare Timeout                                                      | Try again after a brief wait. Contact support if persistent                                                       |
| 529  | Server Error                                                            | Try again after a wait. Contact support if persistent                                                             |

If you encounter other errors or these solutions don't work, [contact support](https://www.together.ai/contact).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
