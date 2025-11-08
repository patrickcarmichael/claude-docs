---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1M token context window

Claude Sonnet 4 and 4.5 support a 1-million token context window. This extended context window allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases.

>   **📝 Note**
>
> The 1M token context window is currently in beta for organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4 and Sonnet 4.5.

To use the 1M token context window, include the `context-1m-2025-08-07` [beta header](/en/api/beta-headers) in your API requests:
```python
  from anthropic import Anthropic

  client = Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Process this large document..."}
      ],
      betas=["context-1m-2025-08-07"]
  )
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const msg = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      { role: 'user', content: 'Process this large document...' }
    ],
    betas: ['context-1m-2025-08-07']
  });
```
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: context-1m-2025-08-07" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Process this large document..."}
      ]
    }'
```

**Important considerations:**

* **Beta status**: This is a beta feature subject to change. Features and pricing may be modified or removed in future releases.
* **Usage tier requirement**: The 1M token context window is available to organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. Lower tier organizations must advance to usage tier 4 to access this feature.
* **Availability**: The 1M token context window is currently available on the Claude API, [Amazon Bedrock](/en/docs/build-with-claude/claude-on-amazon-bedrock), and [Google Cloud's Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai).
* **Pricing**: Requests exceeding 200K tokens are automatically charged at premium rates (2x input, 1.5x output pricing). See the [pricing documentation](/en/docs/about-claude/pricing#long-context-pricing) for details.
* **Rate limits**: Long context requests have dedicated rate limits. See the [rate limits documentation](/en/api/rate-limits#long-context-rate-limits) for details.
* **Multimodal considerations**: When processing large numbers of images or pdfs, be aware that the files can vary in token usage. When pairing a large prompt with a large number of images, you may hit [request size limits](/en/api/overview#request-size-limits).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
