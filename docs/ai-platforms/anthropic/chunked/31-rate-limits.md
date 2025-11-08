**Navigation:** [← Previous](./30-rate-limits.md) | [Index](./index.md) | Next →

---

# Rate limits
Source: https://docs.claude.com/en/api/rate-limits

To mitigate misuse and manage capacity on our API, we have implemented limits on how much an organization can use the Claude API.

We have two types of limits:

1. **Spend limits** set a maximum monthly cost an organization can incur for API usage.
2. **Rate limits** set the maximum number of API requests an organization can make over a defined period of time.

We enforce service-configured limits at the organization level, but you may also set user-configurable limits for your organization's workspaces.

These limits apply to both Standard and Priority Tier usage. For more information about Priority Tier, which offers enhanced service levels in exchange for committed spend, see [Service Tiers](/en/api/service-tiers).

## About our limits

* Limits are designed to prevent API abuse, while minimizing impact on common customer usage patterns.
* Limits are defined by **usage tier**, where each tier is associated with a different set of spend and rate limits.
* Your organization will increase tiers automatically as you reach certain thresholds while using the API.
  Limits are set at the organization level. You can see your organization's limits in the [Limits page](https://console.anthropic.com/settings/limits) in the [Claude Console](https://console.anthropic.com/).
* You may hit rate limits over shorter time intervals. For instance, a rate of 60 requests per minute (RPM) may be enforced as 1 request per second. Short bursts of requests at a high volume can surpass the rate limit and result in rate limit errors.
* The limits outlined below are our standard tier limits. If you're seeking higher, custom limits or Priority Tier for enhanced service levels, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
* We use the [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket) to do rate limiting. This means that your capacity is continuously replenished up to your maximum limit, rather than being reset at fixed intervals.
* All limits described here represent maximum allowed usage, not guaranteed minimums. These limits are intended to reduce unintentional overspend and ensure fair distribution of resources among users.

## Spend limits

Each usage tier has a limit on how much you can spend on the API each calendar month. Once you reach the spend limit of your tier, until you qualify for the next tier, you will have to wait until the next month to be able to use the API again.

To qualify for the next tier, you must meet a deposit requirement. To minimize the risk of overfunding your account, you cannot deposit more than your monthly spend limit.

### Requirements to advance tier

<table>
  <thead>
    <tr>
      <th>Usage Tier</th>
      <th>Credit Purchase</th>
      <th>Max Credit Purchase</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Tier 1</td>
      <td>\$5</td>
      <td>\$100</td>
    </tr>

    <tr>
      <td>Tier 2</td>
      <td>\$40</td>
      <td>\$500</td>
    </tr>

    <tr>
      <td>Tier 3</td>
      <td>\$200</td>
      <td>\$1,000</td>
    </tr>

    <tr>
      <td>Tier 4</td>
      <td>\$400</td>
      <td>\$5,000</td>
    </tr>

    <tr>
      <td>Monthly Invoicing</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>

<Note>
  **Credit Purchase** shows the cumulative credit purchases (excluding tax) required to advance to that tier. You advance immediately upon reaching the threshold.

  **Max Credit Purchase** limits the maximum amount you can add to your account in a single transaction to prevent account overfunding.
</Note>

## Rate limits

Our rate limits for the Messages API are measured in requests per minute (RPM), input tokens per minute (ITPM), and output tokens per minute (OTPM) for each model class.
If you exceed any of the rate limits you will get a [429 error](/en/api/errors) describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

<Note>
  You might also encounter 429 errors due to acceleration limits on the API if your organization has a sharp increase in usage. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.
</Note>

### Cache-aware ITPM

Many API providers use a combined "tokens per minute" (TPM) limit that may include all tokens, both cached and uncached, input and output. **For most Claude models, only uncached input tokens count towards your ITPM rate limits.** This is a key advantage that makes our rate limits effectively higher than they might initially appear.

ITPM rate limits are estimated at the beginning of each request, and the estimate is adjusted during the request to reflect the actual number of input tokens used.

Here's what counts towards ITPM:

* `input_tokens` (tokens after the last cache breakpoint) ✓ **Count towards ITPM**
* `cache_creation_input_tokens` (tokens being written to cache) ✓ **Count towards ITPM**
* `cache_read_input_tokens` (tokens read from cache) ✗ **Do NOT count towards ITPM** for most models

<Note>
  The `input_tokens` field only represents tokens that appear **after your last cache breakpoint**, not all input tokens in your request. To calculate total input tokens:

  ```
  total_input_tokens = cache_read_input_tokens + cache_creation_input_tokens + input_tokens
  ```

  This means when you have cached content, `input_tokens` will typically be much smaller than your total input. For example, with a 200K token cached document and a 50 token user question, you'd see `input_tokens: 50` even though the total input is 200,050 tokens.

  For rate limit purposes on most models, only `input_tokens` + `cache_creation_input_tokens` count toward your ITPM limit, making [prompt caching](/en/docs/build-with-claude/prompt-caching) an effective way to increase your effective throughput.
</Note>

**Example**: With a 2,000,000 ITPM limit and an 80% cache hit rate, you could effectively process 10,000,000 total input tokens per minute (2M uncached + 8M cached), since cached tokens don't count towards your rate limit.

<Note>
  Some older models (marked with † in the rate limit tables below) also count `cache_read_input_tokens` towards ITPM rate limits.

  For all models without the † marker, cached input tokens do not count towards rate limits and are billed at a reduced rate (10% of base input token price). This means you can achieve significantly higher effective throughput by using [prompt caching](/en/docs/build-with-claude/prompt-caching).
</Note>

<Tip>
  **Maximize your rate limits with prompt caching**

  To get the most out of your rate limits, use [prompt caching](/en/docs/build-with-claude/prompt-caching) for repeated content like:

  * System instructions and prompts
  * Large context documents
  * Tool definitions
  * Conversation history

  With effective caching, you can dramatically increase your actual throughput without increasing your rate limits. Monitor your cache hit rate on the [Usage page](https://console.anthropic.com/settings/usage) to optimize your caching strategy.
</Tip>

OTPM rate limits are estimated based on `max_tokens` at the beginning of each request, and the estimate is adjusted at the end of the request to reflect the actual number of output tokens used.
If you're hitting OTPM limits earlier than expected, try reducing `max_tokens` to better approximate the size of your completions.

Rate limits are applied separately for each model; therefore you can use different models up to their respective limits simultaneously.
You can check your current rate limits and behavior in the [Claude Console](https://console.anthropic.com/settings/limits).

<Note>
  For long context requests (>200K tokens) when using the `context-1m-2025-08-07` beta header with Claude Sonnet 4.x, separate rate limits apply. See [Long context rate limits](#long-context-rate-limits) below.
</Note>

<Tabs>
  <Tab title="Tier 1">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 50                                | 30,000                                 | 8,000                                   |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 50                                | 20,000                                 | 8,000                                   |
    | Claude Haiku 4.5                                                           | 50                                | 50,000                                 | 10,000                                  |
    | Claude Haiku 3.5                                                           | 50                                | 50,000<sup>†</sup>                     | 10,000                                  |
    | Claude Haiku 3                                                             | 50                                | 50,000<sup>†</sup>                     | 10,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 50                                | 30,000                                 | 8,000                                   |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 50                                | 20,000<sup>†</sup>                     | 4,000                                   |
  </Tab>

  <Tab title="Tier 2">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 1,000                             | 450,000                                | 90,000                                  |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 1,000                             | 40,000                                 | 16,000                                  |
    | Claude Haiku 4.5                                                           | 1,000                             | 450,000                                | 90,000                                  |
    | Claude Haiku 3.5                                                           | 1,000                             | 100,000<sup>†</sup>                    | 20,000                                  |
    | Claude Haiku 3                                                             | 1,000                             | 100,000<sup>†</sup>                    | 20,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 1,000                             | 450,000                                | 90,000                                  |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 1,000                             | 40,000<sup>†</sup>                     | 8,000                                   |
  </Tab>

  <Tab title="Tier 3">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 2,000                             | 800,000                                | 160,000                                 |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 2,000                             | 80,000                                 | 32,000                                  |
    | Claude Haiku 4.5                                                           | 2,000                             | 1,000,000                              | 200,000                                 |
    | Claude Haiku 3.5                                                           | 2,000                             | 200,000<sup>†</sup>                    | 40,000                                  |
    | Claude Haiku 3                                                             | 2,000                             | 200,000<sup>†</sup>                    | 40,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 2,000                             | 800,000                                | 160,000                                 |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 2,000                             | 80,000<sup>†</sup>                     | 16,000                                  |
  </Tab>

  <Tab title="Tier 4">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 4,000                             | 2,000,000                              | 400,000                                 |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 4,000                             | 200,000                                | 80,000                                  |
    | Claude Haiku 4.5                                                           | 4,000                             | 4,000,000                              | 800,000                                 |
    | Claude Haiku 3.5                                                           | 4,000                             | 400,000<sup>†</sup>                    | 80,000                                  |
    | Claude Haiku 3                                                             | 4,000                             | 400,000<sup>†</sup>                    | 80,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 4,000                             | 2,000,000                              | 400,000                                 |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 4,000                             | 400,000<sup>†</sup>                    | 80,000                                  |
  </Tab>

  <Tab title="Custom">
    If you're seeking higher limits for an Enterprise use case, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
  </Tab>
</Tabs>

*<sup>\* - Opus 4.x rate limit is a total limit that applies to combined traffic across both Opus 4 and Opus 4.1.</sup>*

*<sup>\*\* - Sonnet 4.x rate limit is a total limit that applies to combined traffic across both Sonnet 4 and Sonnet 4.5.</sup>*

*<sup>† - Limit counts `cache_read_input_tokens` towards ITPM usage.</sup>*

### Message Batches API

The Message Batches API has its own set of rate limits which are shared across all models. These include a requests per minute (RPM) limit to all API endpoints and a limit on the number of batch requests that can be in the processing queue at the same time. A "batch request" here refers to part of a Message Batch. You may create a Message Batch containing thousands of batch requests, each of which count towards this limit. A batch request is considered part of the processing queue when it has yet to be successfully processed by the model.

<Tabs>
  <Tab title="Tier 1">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 50                                | 100,000                                    | 100,000                          |
  </Tab>

  <Tab title="Tier 2">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 1,000                             | 200,000                                    | 100,000                          |
  </Tab>

  <Tab title="Tier 3">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 2,000                             | 300,000                                    | 100,000                          |
  </Tab>

  <Tab title="Tier 4">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 4,000                             | 500,000                                    | 100,000                          |
  </Tab>

  <Tab title="Custom">
    If you're seeking higher limits for an Enterprise use case, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
  </Tab>
</Tabs>

### Long context rate limits

When using Claude Sonnet 4 and Sonnet 4.5 with the [1M token context window enabled](/en/docs/build-with-claude/context-windows#1m-token-context-window), the following dedicated rate limits apply to requests exceeding 200K tokens.

<Note>
  The 1M token context window is currently in beta for organizations in usage tier 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4 and Sonnet 4.5.
</Note>

<Tabs>
  <Tab title="Tier 4">
    | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------- | --------------------------------------- |
    | 1,000,000                              | 200,000                                 |
  </Tab>

  <Tab title="Custom">
    For custom long context rate limits for enterprise use cases, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
  </Tab>
</Tabs>

<Tip>
  To get the most out of the 1M token context window with rate limits, use [prompt caching](/en/docs/build-with-claude/prompt-caching).
</Tip>

### Monitoring your rate limits in the Console

You can monitor your rate limit usage on the [Usage](https://console.anthropic.com/settings/usage) page of the [Claude Console](https://console.anthropic.com/).

In addition to providing token and request charts, the Usage page provides two separate rate limit charts. Use these charts to see what headroom you have to grow, when you may be hitting peak use, better undersand what rate limits to request, or how you can improve your caching rates. The charts visualize a number of metrics for a given rate limit (e.g. per model):

* The **Rate Limit - Input Tokens** chart includes:
  * Hourly maximum uncached input tokens per minute
  * Your current input tokens per minute rate limit
  * The cache rate for your input tokens (i.e. the percentage of input tokens read from the cache)
* The **Rate Limit - Output Tokens** chart includes:
  * Hourly maximum output tokens per minute
  * Your current output tokens per minute rate limit

## Setting lower limits for Workspaces

In order to protect Workspaces in your Organization from potential overuse, you can set custom spend and rate limits per Workspace.

Example: If your Organization's limit is 40,000 input tokens per minute and 8,000 output tokens per minute, you might limit one Workspace to 30,000 total tokens per minute. This protects other Workspaces from potential overuse and ensures a more equitable distribution of resources across your Organization. The remaining unused tokens per minute (or more, if that Workspace doesn't use the limit) are then available for other Workspaces to use.

Note:

* You can't set limits on the default Workspace.
* If not set, Workspace limits match the Organization's limit.
* Organization-wide limits always apply, even if Workspace limits add up to more.
* Support for input and output token limits will be added to Workspaces in the future.

## Response headers

The API response includes headers that show you the rate limit enforced, current usage, and when the limit will be reset.

The following headers are returned:

| Header                                        | Description                                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `retry-after`                                 | The number of seconds to wait until you can retry the request. Earlier retries will fail.                                             |
| `anthropic-ratelimit-requests-limit`          | The maximum number of requests allowed within any rate limit period.                                                                  |
| `anthropic-ratelimit-requests-remaining`      | The number of requests remaining before being rate limited.                                                                           |
| `anthropic-ratelimit-requests-reset`          | The time when the request rate limit will be fully replenished, provided in RFC 3339 format.                                          |
| `anthropic-ratelimit-tokens-limit`            | The maximum number of tokens allowed within any rate limit period.                                                                    |
| `anthropic-ratelimit-tokens-remaining`        | The number of tokens remaining (rounded to the nearest thousand) before being rate limited.                                           |
| `anthropic-ratelimit-tokens-reset`            | The time when the token rate limit will be fully replenished, provided in RFC 3339 format.                                            |
| `anthropic-ratelimit-input-tokens-limit`      | The maximum number of input tokens allowed within any rate limit period.                                                              |
| `anthropic-ratelimit-input-tokens-remaining`  | The number of input tokens remaining (rounded to the nearest thousand) before being rate limited.                                     |
| `anthropic-ratelimit-input-tokens-reset`      | The time when the input token rate limit will be fully replenished, provided in RFC 3339 format.                                      |
| `anthropic-ratelimit-output-tokens-limit`     | The maximum number of output tokens allowed within any rate limit period.                                                             |
| `anthropic-ratelimit-output-tokens-remaining` | The number of output tokens remaining (rounded to the nearest thousand) before being rate limited.                                    |
| `anthropic-ratelimit-output-tokens-reset`     | The time when the output token rate limit will be fully replenished, provided in RFC 3339 format.                                     |
| `anthropic-priority-input-tokens-limit`       | The maximum number of Priority Tier input tokens allowed within any rate limit period. (Priority Tier only)                           |
| `anthropic-priority-input-tokens-remaining`   | The number of Priority Tier input tokens remaining (rounded to the nearest thousand) before being rate limited. (Priority Tier only)  |
| `anthropic-priority-input-tokens-reset`       | The time when the Priority Tier input token rate limit will be fully replenished, provided in RFC 3339 format. (Priority Tier only)   |
| `anthropic-priority-output-tokens-limit`      | The maximum number of Priority Tier output tokens allowed within any rate limit period. (Priority Tier only)                          |
| `anthropic-priority-output-tokens-remaining`  | The number of Priority Tier output tokens remaining (rounded to the nearest thousand) before being rate limited. (Priority Tier only) |
| `anthropic-priority-output-tokens-reset`      | The time when the Priority Tier output token rate limit will be fully replenished, provided in RFC 3339 format. (Priority Tier only)  |

The `anthropic-ratelimit-tokens-*` headers display the values for the most restrictive limit currently in effect. For instance, if you have exceeded the Workspace per-minute token limit, the headers will contain the Workspace per-minute token rate limit values. If Workspace limits do not apply, the headers will return the total tokens remaining, where total is the sum of input and output tokens. This approach ensures that you have visibility into the most relevant constraint on your current API usage.


# Service tiers
Source: https://docs.claude.com/en/api/service-tiers

Different tiers of service allow you to balance availability, performance, and predictable costs based on your application's needs.

We offer three service tiers:

* **Priority Tier:** Best for workflows deployed in production where time, availability, and predictable pricing are important
* **Standard:** Default tier for both piloting and scaling everyday use cases
* **Batch:** Best for asynchronous workflows which can wait or benefit from being outside your normal capacity

## Standard Tier

The standard tier is the default service tier for all API requests. Requests in this tier are prioritized alongside all other requests and observe best-effort availability.

## Priority Tier

Requests in this tier are prioritized over all other requests to Anthropic. This prioritization helps minimize ["server overloaded" errors](/en/api/errors#http-errors), even during peak times.

For more information, see [Get started with Priority Tier](#get-started-with-priority-tier)

## How requests get assigned tiers

When handling a request, Anthropic decides to assign a request to Priority Tier in the following scenarios:

* Your organization has sufficient priority tier capacity **input** tokens per minute
* Your organization has sufficient priority tier capacity **output** tokens per minute

Anthropic counts usage against Priority Tier capacity as follows:

**Input Tokens**

* Cache reads as 0.1 tokens per token read from the cache
* Cache writes as 1.25 tokens per token written to the cache with a 5 minute TTL
* Cache writes as 2.00 tokens per token written to the cache with a 1 hour TTL
* For [long-context](/en/docs/build-with-claude/context-windows) (>200k input tokens) requests, input tokens are 2 tokens per token
* All other input tokens are 1 token per token

**Output Tokens**

* For [long-context](/en/docs/build-with-claude/context-windows) (>200k input tokens) requests, output tokens are 1.5 tokens per token
* All other output tokens are 1 token per token

Otherwise, requests proceed at standard tier.

<Note>
  Requests assigned Priority Tier pull from both the Priority Tier capacity and the regular rate limits.
  If servicing the request would exceed the rate limits, the request is declined.
</Note>

## Using service tiers

You can control which service tiers can be used for a request by setting the `service_tier` parameter:

```python  theme={null}
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}],
    service_tier="auto"  # Automatically use Priority Tier when available, fallback to standard
)
```

The `service_tier` parameter accepts the following values:

* `"auto"` (default) - Uses the Priority Tier capacity if available, falling back to your other capacity if not
* `"standard_only"` - Only use standard tier capacity, useful if you don't want to use your Priority Tier capacity

The response `usage` object also includes the service tier assigned to the request:

```json  theme={null}
{
  "usage": {
    "input_tokens": 410,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 585,
    "service_tier": "priority"
  }
}
```

This allows you to determine which service tier was assigned to the request.

When requesting `service_tier="auto"` with a model with a Priority Tier commitment, these response headers provide insights:

```
anthropic-priority-input-tokens-limit: 10000
anthropic-priority-input-tokens-remaining: 9618
anthropic-priority-input-tokens-reset: 2025-01-12T23:11:59Z
anthropic-priority-output-tokens-limit: 10000
anthropic-priority-output-tokens-remaining: 6000
anthropic-priority-output-tokens-reset: 2025-01-12T23:12:21Z
```

You can use the presence of these headers to detect if your request was eligible for Priority Tier, even if it was over the limit.

## Get started with Priority Tier

You may want to commit to Priority Tier capacity if you are interested in:

* **Higher availability**: Target 99.5% uptime with prioritized computational resources
* **Cost Control**: Predictable spend and discounts for longer commitments
* **Flexible overflow**: Automatically falls back to standard tier when you exceed your committed capacity

Committing to Priority Tier will involve deciding:

* A number of input tokens per minute
* A number of output tokens per minute
* A commitment duration (1, 3, 6, or 12 months)
* A specific model version

<Note>
  The ratio of input to output tokens you purchase matters. Sizing your Priority Tier capacity to align with your actual traffic patterns helps you maximize utilization of your purchased tokens.
</Note>

### Supported models

Priority Tier is supported by:

* Claude Opus 4.1
* Claude Opus 4
* Claude Sonnet 4
* Claude Sonnet 3.7
* Claude Haiku 3.5

Check the [model overview page](/en/docs/about-claude/models/overview) for more details on our models.

### How to access Priority Tier

To begin using Priority Tier:

1. [Contact sales](https://claude.com/contact-sales/priority-tier) to complete provisioning
2. (Optional) Update your API requests to optionally set the `service_tier` parameter to `auto`
3. Monitor your usage through response headers and the Claude Console


# Supported regions
Source: https://docs.claude.com/en/api/supported-regions

Here are the countries, regions, and territories we can currently support access from:

* Albania
* Algeria
* Andorra
* Angola
* Antigua and Barbuda
* Argentina
* Armenia
* Australia
* Austria
* Azerbaijan
* Bahamas
* Bahrain
* Bangladesh
* Barbados
* Belgium
* Belize
* Benin
* Bhutan
* Bolivia
* Bosnia and Herzegovina
* Botswana
* Brazil
* Brunei
* Bulgaria
* Burkina Faso
* Burundi
* Cabo Verde
* Cambodia
* Cameroon
* Canada
* Chad
* Chile
* Colombia
* Comoros
* Congo, Republic of the
* Costa Rica
* Côte d'Ivoire
* Croatia
* Cyprus
* Czechia (Czech Republic)
* Denmark
* Djibouti
* Dominica
* Dominican Republic
* Ecuador
* Egypt
* El Salvador
* Equatorial Guinea
* Estonia
* Eswatini
* Fiji
* Finland
* France
* Gabon
* Gambia
* Georgia
* Germany
* Ghana
* Greece
* Grenada
* Guatemala
* Guinea
* Guinea-Bissau
* Guyana
* Haiti
* Holy See (Vatican City)
* Honduras
* Hungary
* Iceland
* India
* Indonesia
* Iraq
* Ireland
* Israel
* Italy
* Jamaica
* Japan
* Jordan
* Kazakhstan
* Kenya
* Kiribati
* Kuwait
* Kyrgyzstan
* Laos
* Latvia
* Lebanon
* Lesotho
* Liberia
* Liechtenstein
* Lithuania
* Luxembourg
* Madagascar
* Malawi
* Malaysia
* Maldives
* Malta
* Marshall Islands
* Mauritania
* Mauritius
* Mexico
* Micronesia
* Moldova
* Monaco
* Mongolia
* Montenegro
* Morocco
* Mozambique
* Namibia
* Nauru
* Nepal
* Netherlands
* New Zealand
* Niger
* Nigeria
* North Macedonia
* Norway
* Oman
* Pakistan
* Palau
* Palestine
* Panama
* Papua New Guinea
* Paraguay
* Peru
* Philippines
* Poland
* Portugal
* Qatar
* Romania
* Rwanda
* Saint Kitts and Nevis
* Saint Lucia
* Saint Vincent and the Grenadines
* Samoa
* San Marino
* Sao Tome and Principe
* Saudi Arabia
* Senegal
* Serbia
* Seychelles
* Sierra Leone
* Singapore
* Slovakia
* Slovenia
* Solomon Islands
* South Africa
* South Korea
* Spain
* Sri Lanka
* Suriname
* Sweden
* Switzerland
* Taiwan
* Tajikistan
* Tanzania
* Thailand
* Timor-Leste, Democratic Republic of
* Togo
* Tonga
* Trinidad and Tobago
* Tunisia
* Turkey
* Turkmenistan
* Tuvalu
* Uganda
* Ukraine (except Crimea, Donetsk, and Luhansk regions)
* United Arab Emirates
* United Kingdom
* United States of America
* Uruguay
* Uzbekistan
* Vanuatu
* Vietnam
* Zambia
* Zimbabwe


# Versions
Source: https://docs.claude.com/en/api/versioning

When making API requests, you must send an `anthropic-version` request header. For example, `anthropic-version: 2023-06-01`. If you are using our [client SDKs](/en/api/client-sdks), this is handled for you automatically.

For any given API version, we will preserve:

* Existing input parameters
* Existing output parameters

However, we may do the following:

* Add additional optional inputs
* Add additional values to the output
* Change conditions for specific error types
* Add new variants to enum-like output values (for example, streaming event types)

Generally, if you are using the API as documented in this reference, we will not break your usage.

## Version history

We always recommend using the latest API version whenever possible. Previous versions are considered deprecated and may be unavailable for new users.

* `2023-06-01`
  * New format for [streaming](/en/docs/build-with-claude/streaming) server-sent events (SSE):
    * Completions are incremental. For example, `" Hello"`, `" my"`, `" name"`, `" is"`, `" Claude." ` instead of `" Hello"`, `" Hello my"`, `" Hello my name"`, `" Hello my name is"`, `" Hello my name is Claude."`.
    * All events are [named events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#named%5Fevents), rather than [data-only events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents#data-only%5Fmessages).
    * Removed unnecessary `data: [DONE]` event.
  * Removed legacy `exception` and `truncated` values in responses.
* `2023-01-01`: Initial release.


# Model Context Protocol (MCP)
Source: https://docs.claude.com/en/docs/mcp



MCP is an open protocol that standardizes how applications provide context to LLMs.

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

## Build your own MCP products

<Card title="MCP Documentation" icon="book" href="https://modelcontextprotocol.io">
  Learn more about the protocol, how to build servers and clients, and discover those made by others.
</Card>

## MCP in Anthropic products

<CardGroup>
  <Card title="MCP in the Messages API" icon="cloud" href="/en/docs/agents-and-tools/mcp-connector">
    Use the MCP connector in the Messages API to connect to MCP servers.
  </Card>

  <Card title="MCP in Claude Code" icon="head-side-gear" href="https://code.claude.com/docs/mcp">
    Add your MCP servers to Claude Code, or use Claude Code as a server.
  </Card>

  <Card title="MCP in Claude.ai" icon="comments" href="https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp">
    Enable MCP connectors for your team in Claude.ai.
  </Card>

  <Card title="MCP in Claude Desktop" icon="desktop" href="https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop">
    Add MCP servers to Claude Desktop.
  </Card>
</CardGroup>


# Claude Developer Platform
Source: https://docs.claude.com/en/release-notes/overview

Updates to the Claude Developer Platform, including the Claude API, client SDKs, and the Claude Console.

<Tip>
  For release notes on Claude Apps, see the [Release notes for Claude Apps in the Claude Help Center](https://support.claude.com/en/articles/12138966-release-notes).

  For updates to Claude Code, see the [complete CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) in the `claude-code` repository.
</Tip>

#### October 28, 2025

* We announced the deprecation of the Claude Sonnet 3.7 model. Read more in [our documentation](/en/docs/about-claude/model-deprecations).
* We've retired the Claude Sonnet 3.5 models. All requests to these models will now return an error.
* We've expanded context editing with thinking block clearing (`clear_thinking_20251015`), enabling automatic management of thinking blocks. Learn more in our [context editing documentation](/en/docs/build-with-claude/context-editing).

#### October 16, 2025

* We've launched [Agent Skills](https://https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills-skills) (`skills-2025-10-02` beta), a new way to extend Claude's capabilities. Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically to perform specialized tasks. The initial release includes:
  * **Anthropic-managed Skills**: Pre-built Skills for working with PowerPoint (.pptx), Excel (.xlsx), Word (.docx), and PDF files
  * **Custom Skills**: Upload your own Skills via the Skills API (`/v1/skills` endpoints) to package domain expertise and organizational workflows
  * Skills require the [code execution tool](/en/docs/agents-and-tools/tool-use/code-execution-tool) to be enabled
  * Learn more in our [Agent Skills documentation](/en/docs/agents-and-tools/agent-skills/overview) and [API reference](/en/api/skills/create-skill)

#### October 15, 2025

* We've launched [Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5), our fastest and most intelligent Haiku model with near-frontier performance. Ideal for real-time applications, high-volume processing, and cost-sensitive deployments requiring strong reasoning. Learn more in our [Models & Pricing documentation](/en/docs/about-claude/models).

#### September 29, 2025

* We've launched [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5), our best model for complex agents and coding, with the highest intelligence across most tasks. Learn more in [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5).
* We've introduced [global endpoint pricing](/en/docs/about-claude/pricing#third-party-platform-pricing) for AWS Bedrock and Google Vertex AI. The Claude API (1P) pricing is unaffected.
* We've introduced a new stop reason `model_context_window_exceeded` that allows you to request the maximum possible tokens without calculating input size. Learn more in our [handling stop reasons documentation](/en/docs/build-with-claude/handling-stop-reasons).
* We've launched the memory tool in beta, enabling Claude to store and consult information across conversations. Learn more in our [memory tool documentation](/en/docs/agents-and-tools/tool-use/memory-tool).
* We've launched context editing in beta, providing strategies to automatically manage conversation context. The initial release supports clearing older tool results and calls when approaching token limits. Learn more in our [context editing documentation](/en/docs/build-with-claude/context-editing).

#### September 17, 2025

* We've launched tool helpers in beta for the Python and TypeScript SDKs, simplifying tool creation and execution with type-safe input validation and a tool runner for automated tool handling in conversations. For details, see the documentation for [the Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md) and [the TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers).

#### September 16, 2025

* We've unified our developer offerings under the Claude brand. You should see updated naming and URLs across our platform and documentation, but **our developer interfaces will remain the same**. Here are some notable changes:
  * Anthropic Console ([console.anthropic.com](https://console.anthropic.com)) → Claude Console ([platform.claude.com](https://platform.claude.com)). The console will be available at both URLs until December 16, 2025. After that date, [console.anthropic.com](https://console.anthropic.com) will automatically redirect to [platform.claude.com](https://platform.claude.com).
  * Anthropic Docs ([docs.claude.com](https://docs.claude.com)) → Claude Docs ([docs.claude.com](https://docs.claude.com))
  * Anthropic Help Center ([support.claude.com](https://support.claude.com)) → Claude Help Center ([support.claude.com](https://support.claude.com))
  * API endpoints, headers, environment variables, and SDKs remain the same. Your existing integrations will continue working without any changes.

#### September 10, 2025

* We've launched the web fetch tool in beta, allowing Claude to retrieve full content from specified web pages and PDF documents. Learn more in our [web fetch tool documentation](/en/docs/agents-and-tools/tool-use/web-fetch-tool).
* We've launched the [Claude Code Analytics API](/en/docs/build-with-claude/claude-code-analytics-api), enabling organizations to programmatically access daily aggregated usage metrics for Claude Code, including productivity metrics, tool usage statistics, and cost data.

#### September 8, 2025

* We launched a beta version of the [C# SDK](https://github.com/anthropics/anthropic-sdk-csharp).

#### September 5, 2025

* We've launched [rate limit charts](/en/api/rate-limits#monitoring-your-rate-limits-in-the-console) in the Console [Usage](https://console.anthropic.com/settings/usage) page, allowing you to monitor your API rate limit usage and caching rates over time.

#### September 3, 2025

* We've launched support for citable documents in client-side tool results. Learn more in our [tool use documentation](en/docs/agents-and-tools/tool-use/implement-tool-use.mdx).

#### September 2, 2025

* We've launched v2 of the [Code Execution Tool](/en/docs/agents-and-tools/tool-use/code-execution-tool) in public beta, replacing the original Python-only tool with Bash command execution and direct file manipulation capabilities, including writing code in other languages.

#### August 27, 2025

* We launched a beta version of the [PHP SDK](https://github.com/anthropics/anthropic-sdk-php).

#### August 26, 2025

* We've increased rate limits on the [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) for Claude Sonnet 4 on the Claude API. For more information, see [Long context rate limits](/en/api/rate-limits#long-context-rate-limits).
* The 1m token context window is now available on Google Cloud's Vertex AI. For more information, see [Claude on Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai).

#### August 19, 2025

* Request IDs are now included directly in error response bodies alongside the existing `request-id` header. Learn more in our [error documentation](/en/api/errors#error-shapes).

#### August 18, 2025

* We've released the [Usage & Cost API](/en/docs/build-with-claude/usage-cost-api), allowing administrators to programmatically monitor their organization's usage and cost data.
* We've added a new endpoint to the Admin API for retrieving organization information. For details, see the [Organization Info Admin API reference](/en/api/admin-api/organization/get-me).

#### August 13, 2025

* We announced the deprecation of the Claude Sonnet 3.5 models (`claude-3-5-sonnet-20240620` and `claude-3-5-sonnet-20241022`). These models will be retired on October 28, 2025. We recommend migrating to Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) for improved performance and capabilities. Read more in the [Model deprecations documentation](/en/docs/about-claude/model-deprecations).
* The 1-hour cache duration for prompt caching is now generally available. You can now use the extended cache TTL without a beta header. Learn more in our [prompt caching documentation](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration).

#### August 12, 2025

* We've launched beta support for a [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) in Claude Sonnet 4 on the Claude API and Amazon Bedrock.

#### August 11, 2025

* Some customers might encounter 429 (`rate_limit_error`) [errors](/en/api/errors) following a sharp increase in API usage due to acceleration limits on the API. Previously, 529 (`overloaded_error`) errors would occur in similar scenarios.

#### August 8, 2025

* Search result content blocks are now generally available on the Claude API and Google Cloud's Vertex AI. This feature enables natural citations for RAG applications with proper source attribution. The beta header `search-results-2025-06-09` is no longer required. Learn more in our [search results documentation](/en/docs/build-with-claude/search-results).

#### August 5, 2025

* We've launched [Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4-1), an incremental update to Claude Opus 4 with enhanced capabilities and performance improvements.<sup>\*</sup> Learn more in our [Models & Pricing documentation](/en/docs/about-claude/models).

*<sup>\* - Opus 4.1 does not allow both `temperature` and `top_p` parameters to be specified. Please use only one. </sup>*

#### July 28, 2025

* We've released `text_editor_20250728`, an updated text editor tool that fixes some issues from the previous versions and adds an optional `max_characters` parameter that allows you to control the truncation length when viewing large files.

#### July 24, 2025

* We've increased [rate limits](/en/api/rate-limits) for Claude Opus 4 on the Claude API to give you more capacity to build and scale with Claude. For customers with [usage tier 1-4 rate limits](/en/api/rate-limits#rate-limits), these changes apply immediately to your account - no action needed.

#### July 21, 2025

* We've retired the Claude 2.0, Claude 2.1, and Claude Sonnet 3 models. All requests to these models will now return an error. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### July 17, 2025

* We've increased [rate limits](/en/api/rate-limits) for Claude Sonnet 4 on the Claude API to give you more capacity to build and scale with Claude. For customers with [usage tier 1-4 rate limits](/en/api/rate-limits#rate-limits), these changes apply immediately to your account - no action needed.

#### July 3, 2025

* We've launched search result content blocks in beta, enabling natural citations for RAG applications. Tools can now return search results with proper source attribution, and Claude will automatically cite these sources in its responses - matching the citation quality of web search. This eliminates the need for document workarounds in custom knowledge base applications. Learn more in our [search results documentation](/en/docs/build-with-claude/search-results). To enable this feature, use the beta header `search-results-2025-06-09`.

#### June 30, 2025

* We announced the deprecation of the Claude Opus 3 model. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### June 23, 2025

* Console users with the Developer role can now access the [Cost](https://console.anthropic.com/settings/cost) page. Previously, the Developer role allowed access to the [Usage](https://console.anthropic.com/settings/usage) page, but not the Cost page.

#### June 11, 2025

* We've launched [fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming) in public beta, a feature that enables Claude to stream tool use parameters without buffering / JSON validation. To enable fine-grained tool streaming, use the [beta header](/en/api/beta-headers) `fine-grained-tool-streaming-2025-05-14`.

#### May 22, 2025

* We've launched [Claude Opus 4 and Claude Sonnet 4](http://www.anthropic.com/news/claude-4), our latest models with extended thinking capabilities. Learn more in our [Models & Pricing documentation](/en/docs/about-claude/models).
* The default behavior of [extended thinking](/en/docs/build-with-claude/extended-thinking) in Claude 4 models returns a summary of Claude's full thinking process, with the full thinking encrypted and returned in the `signature` field of `thinking` block output.
* We've launched [interleaved thinking](/en/docs/build-with-claude/extended-thinking#interleaved-thinking) in public beta, a feature that enables Claude to think in between tool calls. To enable interleaved thinking, use the [beta header](/en/api/beta-headers) `interleaved-thinking-2025-05-14`.
* We've launched the [Files API](/en/docs/build-with-claude/files) in public beta, enabling you to upload files and reference them in the Messages API and code execution tool.
* We've launched the [Code execution tool](/en/docs/agents-and-tools/tool-use/code-execution-tool) in public beta, a tool that enables Claude to execute Python code in a secure, sandboxed environment.
* We've launched the [MCP connector](/en/docs/agents-and-tools/mcp-connector) in public beta, a feature that allows you to connect to remote MCP servers directly from the Messages API.
* To increase answer quality and decrease tool errors, we've changed the default value for the `top_p` [nucleus sampling](https://en.wikipedia.org/wiki/Top-p_sampling) parameter in the Messages API from 0.999 to 0.99 for all models. To revert this change, set `top_p` to 0.999.
  Additionally, when extended thinking is enabled, you can now set `top_p` to values between 0.95 and 1.
* We've moved our [Go SDK](https://github.com/anthropics/anthropic-sdk-go) from beta to GA.
* We've included minute and hour level granularity to the [Usage](https://console.anthropic.com/settings/usage) page of Console alongside 429 error rates on the Usage page.

#### May 21, 2025

* We've moved our [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby) from beta to GA.

#### May 7, 2025

* We've launched a web search tool in the API, allowing Claude to access up-to-date information from the web. Learn more in our [web search tool documentation](/en/docs/agents-and-tools/tool-use/web-search-tool).

#### May 1, 2025

* Cache control must now be specified directly in the parent `content` block of `tool_result` and `document.source`. For backwards compatibility, if cache control is detected on the last block in `tool_result.content` or `document.source.content`, it will be automatically applied to the parent block instead. Cache control on any other blocks within `tool_result.content` and `document.source.content` will result in a validation error.

#### April 9th, 2025

* We launched a beta version of the [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby)

#### March 31st, 2025

* We've moved our [Java SDK](https://github.com/anthropics/anthropic-sdk-java) from beta to GA.
* We've moved our [Go SDK](https://github.com/anthropics/anthropic-sdk-go) from alpha to beta.

#### February 27th, 2025

* We've added URL source blocks for images and PDFs in the Messages API. You can now reference images and PDFs directly via URL instead of having to base64-encode them. Learn more in our [vision documentation](/en/docs/build-with-claude/vision) and [PDF support documentation](/en/docs/build-with-claude/pdf-support).
* We've added support for a `none` option to the `tool_choice` parameter in the Messages API that prevents Claude from calling any tools. Additionally, you're no longer required to provide any `tools` when including `tool_use` and `tool_result` blocks.
* We've launched an OpenAI-compatible API endpoint, allowing you to test Claude models by changing just your API key, base URL, and model name in existing OpenAI integrations. This compatibility layer supports core chat completions functionality. Learn more in our [OpenAI SDK compatibility documentation](/en/api/openai-sdk).

#### February 24th, 2025

* We've launched [Claude Sonnet 3.7](http://www.anthropic.com/news/claude-3-7-sonnet), our most intelligent model yet. Claude Sonnet 3.7 can produce near-instant responses or show its extended thinking step-by-step. One model, two ways to think. Learn more about all Claude models in our [Models & Pricing documentation](/en/docs/about-claude/models).
* We've added vision support to Claude Haiku 3.5, enabling the model to analyze and understand images.
* We've released a token-efficient tool use implementation, improving overall performance when using tools with Claude. Learn more in our [tool use documentation](/en/docs/agents-and-tools/tool-use/overview).
* We've changed the default temperature in the [Console](https://console.anthropic.com/workbench) for new prompts from 0 to 1 for consistency with the default temperature in the API. Existing saved prompts are unchanged.
* We've released updated versions of our tools that decouple the text edit and bash tools from the computer use system prompt:
  * `bash_20250124`: Same functionality as previous version but is independent from computer use. Does not require a beta header.
  * `text_editor_20250124`: Same functionality as previous version but is independent from computer use. Does not require a beta header.
  * `computer_20250124`: Updated computer use tool with new command options including "hold\_key", "left\_mouse\_down", "left\_mouse\_up", "scroll", "triple\_click", and "wait". This tool requires the "computer-use-2025-01-24" anthropic-beta header.
    Learn more in our [tool use documentation](/en/docs/agents-and-tools/tool-use/overview).

#### February 10th, 2025

* We've added the `anthropic-organization-id` response header to all API responses. This header provides the organization ID associated with the API key used in the request.

#### January 31st, 2025

* We've moved our [Java SDK](https://github.com/anthropics/anthropic-sdk-java) from alpha to beta.

#### January 23rd, 2025

* We've launched citations capability in the API, allowing Claude to provide source attribution for information. Learn more in our [citations documentation](/en/docs/build-with-claude/citations).
* We've added support for plain text documents and custom content documents in the Messages API.

#### January 21st, 2025

* We announced the deprecation of the Claude 2, Claude 2.1, and Claude Sonnet 3 models. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### January 15th, 2025

* We've updated [prompt caching](/en/docs/build-with-claude/prompt-caching) to be easier to use. Now, when you set a cache breakpoint, we'll automatically read from your longest previously cached prefix.
* You can now put words in Claude's mouth when using tools.

#### January 10th, 2025

* We've optimized support for [prompt caching in the Message Batches API](/en/docs/build-with-claude/batch-processing#using-prompt-caching-with-message-batches) to improve cache hit rate.

#### December 19th, 2024

* We've added support for a [delete endpoint](/en/api/deleting-message-batches) in the Message Batches API

#### December 17th, 2024

The following features are now generally available in the Claude API:

* [Models API](/en/api/models-list): Query available models, validate model IDs, and resolve [model aliases](/en/docs/about-claude/models#model-names) to their canonical model IDs.
* [Message Batches API](/en/docs/build-with-claude/batch-processing): Process large batches of messages asynchronously at 50% of the standard API cost.
* [Token counting API](/en/docs/build-with-claude/token-counting): Calculate token counts for Messages before sending them to Claude.
* [Prompt Caching](/en/docs/build-with-claude/prompt-caching): Reduce costs by up to 90% and latency by up to 80% by caching and reusing prompt content.
* [PDF support](/en/docs/build-with-claude/pdf-support): Process PDFs to analyze both text and visual content within documents.

We also released new official SDKs:

* [Java SDK](https://github.com/anthropics/anthropic-sdk-java) (alpha)
* [Go SDK](https://github.com/anthropics/anthropic-sdk-go) (alpha)

#### December 4th, 2024

* We've added the ability to group by API key to the [Usage](https://console.anthropic.com/settings/usage) and [Cost](https://console.anthropic.com/settings/cost) pages of the [Developer Console](https://console.anthropic.com)
* We've added two new **Last used at** and **Cost** columns and the ability to sort by any column in the [API keys](https://console.anthropic.com/settings/keys) page of the [Developer Console](https://console.anthropic.com)

#### November 21st, 2024

* We've released the [Admin API](/en/docs/build-with-claude/administration-api), allowing users to programmatically manage their organization's resources.

### November 20th, 2024

* We've updated our rate limits for the Messages API. We've replaced the tokens per minute rate limit with new input and output tokens per minute rate limits. Read more in our [documentation](/en/api/rate-limits).
* We've added support for [tool use](/en/docs/agents-and-tools/tool-use/overview) in the [Workbench](https://console.anthropic.com/workbench).

### November 13th, 2024

* We've added PDF support for all Claude Sonnet 3.5 models. Read more in our [documentation](/en/docs/build-with-claude/pdf-support).

### November 6th, 2024

* We've retired the Claude 1 and Instant models. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### November 4th, 2024

* [Claude Haiku 3.5](https://www.anthropic.com/claude/haiku) is now available on the Claude API as a text-only model.

#### November 1st, 2024

* We've added PDF support for use with the new Claude Sonnet 3.5. Read more in our [documentation](/en/docs/build-with-claude/pdf-support).
* We've also added token counting, which allows you to determine the total number of tokens in a Message, prior to sending it to Claude. Read more in our [documentation](/en/docs/build-with-claude/token-counting).

#### October 22nd, 2024

* We've added Anthropic-defined computer use tools to our API for use with the new Claude Sonnet 3.5. Read more in our [documentation](/en/docs/agents-and-tools/tool-use/computer-use-tool).
* Claude Sonnet 3.5, our most intelligent model yet, just got an upgrade and is now available on the Claude API. Read more [here](https://www.anthropic.com/claude/sonnet).

#### October 8th, 2024

* The Message Batches API is now available in beta. Process large batches of queries asynchronously in the Claude API for 50% less cost. Read more in our [documentation](/en/docs/build-with-claude/batch-processing).
* We've loosened restrictions on the ordering of `user`/`assistant` turns in our Messages API. Consecutive `user`/`assistant` messages will be combined into a single message instead of erroring, and we no longer require the first input message to be a `user` message.
* We've deprecated the Build and Scale plans in favor of a standard feature suite (formerly referred to as Build), along with additional features that are available through sales. Read more [here](https://claude.com/platform/api).

#### October 3rd, 2024

* We've added the ability to disable parallel tool use in the API. Set `disable_parallel_tool_use: true` in the `tool_choice` field to ensure that Claude uses at most one tool. Read more in our [documentation](/en/docs/agents-and-tools/tool-use/implement-tool-use#parallel-tool-use).

#### September 10th, 2024

* We've added Workspaces to the [Developer Console](https://console.anthropic.com). Workspaces allow you to set custom spend or rate limits, group API keys, track usage by project, and control access with user roles. Read more in our [blog post](https://www.anthropic.com/news/workspaces).

#### September 4th, 2024

* We announced the deprecation of the Claude 1 models. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### August 22nd, 2024

* We've added support for usage of the SDK in browsers by returning CORS headers in the API responses. Set `dangerouslyAllowBrowser: true` in the SDK instantiation to enable this feature.

#### August 19th, 2024

* We've moved 8,192 token outputs from beta to general availability for Claude Sonnet 3.5.

#### August 14th, 2024

* [Prompt caching](/en/docs/build-with-claude/prompt-caching) is now available as a beta feature in the Claude API. Cache and re-use prompts to reduce latency by up to 80% and costs by up to 90%.

#### July 15th, 2024

* Generate outputs up to 8,192 tokens in length from Claude Sonnet 3.5 with the new `anthropic-beta: max-tokens-3-5-sonnet-2024-07-15` header.

#### July 9th, 2024

* Automatically generate test cases for your prompts using Claude in the [Developer Console](https://console.anthropic.com).
* Compare the outputs from different prompts side by side in the new output comparison mode in the [Developer Console](https://console.anthropic.com).

#### June 27th, 2024

* View API usage and billing broken down by dollar amount, token count, and API keys in the new [Usage](https://console.anthropic.com/settings/usage) and [Cost](https://console.anthropic.com/settings/cost) tabs in the [Developer Console](https://console.anthropic.com).
* View your current API rate limits in the new [Rate Limits](https://console.anthropic.com/settings/limits) tab in the [Developer Console](https://console.anthropic.com).

#### June 20th, 2024

* [Claude Sonnet 3.5](http://anthropic.com/news/claude-3-5-sonnet), our most intelligent model yet, is now generally available across the Claude API, Amazon Bedrock, and Google Vertex AI.

#### May 30th, 2024

* [Tool use](/en/docs/agents-and-tools/tool-use/overview) is now generally available across the Claude API, Amazon Bedrock, and Google Vertex AI.

#### May 10th, 2024

* Our prompt generator tool is now available in the [Developer Console](https://console.anthropic.com). Prompt Generator makes it easy to guide Claude to generate a high-quality prompts tailored to your specific tasks. Read more in our [blog post](https://www.anthropic.com/news/prompt-generator).



---

**Navigation:** [← Previous](./30-rate-limits.md) | [Index](./index.md) | Next →
