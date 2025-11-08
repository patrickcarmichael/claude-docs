---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rate Limits

Source: https://docs.together.ai/docs/rate-limits

Rate limits restrict how often a user or client can access our API within a set timeframe.

Rate limiting refers to the constraints our API enforces on how frequently a user or client can access our services within a given timeframe. Rate limits are denoted as HTTP status code 429. Read more about our rate limit tiers below, and find out how you can increase them here:

* If you have a high volume of steady traffic and good payment history for this traffic, you can request a higher limit by emailing [support@together.ai](mailto:support@together.ai).
* If you are interested in our Enterprise package, with custom requests per minute (RPM) and unlimited tokens per minute (TPM), please reach out to sales [here](https://www.together.ai/contact-sales).

### What is the purpose of rate limits?

Rate limits in APIs are a standard approach, and they serve to safeguard against abuse or misuse of the API, helping to ensure equitable access to the API with consistent performance.

### How are our rate limits implemented?

Our rate limits are currently measured in requests per second (RPS) and tokens per second (TPS) for each model type. If you exceed any of the rate limits you will get a 429 error. We show you the values per minute below, as it's the industry standard.

Important: when we launch support for a brand new model, we may temporarily disable automatic increases for that given model. This ensures our service levels remain stable, as rate limits represent the maximum "up to" capacity a user is entitled to, which is ultimately driven by our available serverless capacity. We strive to enable automatic increases as soon as possible once capacity stabilizes.

### Rate limit tiers

You can view your rate limit by navigating to Settings > Billing. As your usage of the Together API and your spend on our API increases, we will automatically increase your rate limits.

**Chat, language & code models**

| Tier   | Qualification criteria      | RPM   | TPM       |
| :----- | :-------------------------- | :---- | :-------- |
| Tier 1 | Credit card added, \$5 paid | 600   | 180,000   |
| Tier 2 | \$50 paid                   | 1,800 | 250,000   |
| Tier 3 | \$100 paid                  | 3,000 | 500,000   |
| Tier 4 | \$250 paid                  | 4,500 | 1,000,000 |
| Tier 5 | \$1,000 paid                | 6,000 | 2,000,000 |

**DeepSeek R1 model-specific rate limits**

> Due to high demand on the platform, DeepSeek R1 has these special rate limits. We are actively increasing them.

| Tier   | RPM     |
| :----- | :------ |
| Tier 1 | 3       |
| Tier 2 | 60      |
| Tier 3 | \~400+  |
| Tier 4 | \~400+  |
| Tier 5 | \~1200+ |

**Embedding models**

| Tier   | Qualification criteria      | RPM    | TPM        |
| :----- | :-------------------------- | :----- | :--------- |
| Tier 1 | Credit card added, \$5 paid | 3,000  | 2,000,000  |
| Tier 2 | \$50 paid                   | 5,000  | 2,000,000  |
| Tier 3 | \$100 paid                  | 5,000  | 10,000,000 |
| Tier 4 | \$250 paid                  | 10,000 | 10,000,000 |
| Tier 5 | \$1,000 paid                | 10,000 | 20,000,000 |

**Re-rank models**

| Tier   | Qualification criteria      | RPM   | TPM       |
| :----- | :-------------------------- | :---- | :-------- |
| Tier 1 | Credit card added, \$5 paid | 2,500 | 500,000   |
| Tier 2 | \$50 paid                   | 3,500 | 1,500,000 |
| Tier 3 | \$100 paid                  | 4,000 | 2,000,000 |
| Tier 4 | \$250 paid                  | 7,500 | 3,000,000 |
| Tier 5 | \$1,000 paid                | 9,000 | 5,000,000 |

**Image models**

| Tier   | Qualification criteria      | Img/min |
| :----- | :-------------------------- | :------ |
| Tier 1 | Credit card added, \$5 paid | 240     |
| Tier 2 | \$50 paid                   | 480     |
| Tier 3 | \$100 paid                  | 600     |
| Tier 4 | \$250 paid                  | 960     |
| Tier 5 | \$1,000 paid                | 1,200   |

Note: Due to high demand:

* FLUX.1 \[schnell] Free has a model specific rate limit of 6 img/min.
* FLUX.1 Kontext \[pro] has a model specific rate limit of 57 img/min.

You may experience congestion based on traffic from other users, and may be throttled to a lower level because of that. If you want committed capacity, [contact](https://together.ai/forms/scale-ent) our sales team to inquire about our Scale and Enterprise plans, which include custom RPM and unlimited TPM.

**Rate limits in headers**

The API response includes headers that display the rate limit enforcement, current usage, and when the limit will reset. We enforce limits per second and minute for token usage and per second for request rates, but the headers display per second limits only.

| Field                  | Description                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| x-ratelimit-limit      | The maximum number of requests per sec that are permitted before exhausting the rate limit.   |
| x-ratelimit-remaining  | The remaining number of requests per sec that are permitted before exhausting the rate limit. |
| x-ratelimit-reset      | The time until the rate limit (based on requests per sec) resets to its initial state.        |
| x-tokenlimit-limit     | The maximum number of tokens per sec that are permitted before exhausting the rate limit.     |
| x-tokenlimit-remaining | The remaining number of tokens per sec that are permitted before exhausting the rate limit.   |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
