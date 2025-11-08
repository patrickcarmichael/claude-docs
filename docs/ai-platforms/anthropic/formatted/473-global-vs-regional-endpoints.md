---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Amazon Bedrock offers two endpoint types:

* **Global endpoints**: Dynamic routing for maximum availability
* **Regional endpoints**: Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.

>   **📝 Note**
>
> This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4, Opus 4, and earlier) maintain their existing pricing structures.

### When to use each option

**Global endpoints (recommended):**

* Provide maximum availability and uptime
* Dynamically route requests to regions with available capacity
* No pricing premium
* Best for applications where data residency is flexible

**Regional endpoints (CRIS):**

* Route traffic through specific geographic regions
* Required for data residency and compliance requirements
* Available for US, EU, Japan, and Australia
* 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints (default for Sonnet 4.5 and 4):**

The model IDs for Claude Sonnet 4.5 and 4 already include the `global.` prefix:
```python
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(aws_region="us-west-2")

  message = client.messages.create(
      model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}]
  )
```
```typescript
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  const client = new AnthropicBedrock({
    awsRegion: 'us-west-2',
  });

  const message = await client.messages.create({
    model: 'global.anthropic.claude-sonnet-4-5-20250929-v1:0',
    max_tokens: 256,
    messages: [{role: "user", content: "Hello, world"}]
  });
```

**Using regional endpoints (CRIS):**

To use regional endpoints, remove the `global.` prefix from the model ID:
```python
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(aws_region="us-west-2")

  # Using US regional endpoint (CRIS)

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",  # No global. prefix

      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}]
  )
```
```typescript
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  const client = new AnthropicBedrock({
    awsRegion: 'us-west-2',
  });

  // Using US regional endpoint (CRIS)
  const message = await client.messages.create({
    model: 'anthropic.claude-sonnet-4-5-20250929-v1:0',  // No global. prefix
    max_tokens: 256,
    messages: [{role: "user", content: "Hello, world"}]
  });
```python

### Additional resources

* **AWS Bedrock pricing:** [aws.amazon.com/bedrock/pricing](https://aws.amazon.com/bedrock/pricing/)
* **AWS pricing documentation:** [Bedrock pricing guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html)
* **AWS blog post:** [Introducing Claude Sonnet 4.5 in Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)
* **Anthropic pricing details:** [Pricing documentation](/en/docs/about-claude/pricing#third-party-platform-pricing)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
