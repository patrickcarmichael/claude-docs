---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How Are Costs Calculated for Different Cohere Models?

Our generative models, such as [Command A](/docs/command-a), [Command R7B](/docs/command-r7b), [Command R](/docs/command-r) and [Command R+](/docs/command-r-plus), are priced on a per-token basis. Be aware that input tokens (i.e. tokens generated from text sent *to* the model) and output tokens (i.e. text generated *by* the model) are priced differently.

Our Rerank models are priced based on the quantity of searches, and our Embedding models are priced based on the number of tokens embedded.

### What's the Difference Between "billed" Tokens and Generic Tokens?

When using the [Chat API endpoint](https://docs.cohere.com/reference/chat), the response will contain the total count of input and output tokens, as well as the count of *billed* tokens. Here's an example:
```json JSON
{
  "billed_units": {
    "input_tokens": 6772,
    "output_tokens": 248
  },
  "tokens": {
    "input_tokens": 7596,
    "output_tokens": 645
  }
}
```typescript
The rerank and embed models have their own, slightly different versions, and it may not be obvious why there are separate input and output values under `billed_units`. To clarify, the *billed* input and output tokens are the tokens that you're actually *billed* for. The reason these values can be different from the overall `"tokens"` value is that there are situations in which Cohere adds tokens under the hood, and there are others in which a particular model has been trained to do so (i.e. when outputting special tokens). Since these are tokens *you don't have control over, you are not charged for them.*

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
