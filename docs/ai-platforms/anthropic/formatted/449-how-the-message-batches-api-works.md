---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How the Message Batches API works

When you send a request to the Message Batches API:

1. The system creates a new Message Batch with the provided Messages requests.
2. The batch is then processed asynchronously, with each request handled independently.
3. You can poll for the status of the batch and retrieve results when processing has ended for all requests.

This is especially useful for bulk operations that don't require immediate results, such as:

* Large-scale evaluations: Process thousands of test cases efficiently.
* Content moderation: Analyze large volumes of user-generated content asynchronously.
* Data analysis: Generate insights or summaries for large datasets.
* Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries).

### Batch limitations

* A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first.
* We process each batch as fast as possible, with most batches completing within 1 hour. You will be able to access batch results when all messages have completed or after 24 hours, whichever comes first. Batches will expire if processing does not complete within 24 hours.
* Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download.
* Batches are scoped to a [Workspace](https://console.anthropic.com/settings/workspaces). You may view all batches—and their results—that were created within the Workspace that your API key belongs to.
* Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See [Message Batches API rate limits](/en/api/rate-limits#message-batches-api). Additionally, we may slow down processing based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours.
* Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured [spend limit](https://console.anthropic.com/settings/limits).

### Supported models

All [active models](/en/docs/about-claude/models/overview) support the Message Batches API.

### What can be batched

Any request that you can make to the Messages API can be included in a batch. This includes:

* Vision
* Tool use
* System messages
* Multi-turn conversations
* Any beta features

Since each request in the batch is processed independently, you can mix different types of requests within a single batch.

<Tip>
  Since batches can take longer than 5 minutes to process, consider using the [1-hour cache duration](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration) with prompt caching for better cache hit rates when processing batches with shared context.
</Tip>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
