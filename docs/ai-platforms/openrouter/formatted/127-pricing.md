---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing

### Exa Search Pricing

When using Exa search (either explicitly via `"engine": "exa"` or as fallback), the web plugin uses your OpenRouter credits and charges *\$4 per 1000 results*. By default, `max_results` set to 5, this comes out to a maximum of \$0.02 per request, in addition to the LLM usage for the search result prompt tokens.

### Native Search Pricing (Provider Passthrough)

Some models have built-in web search. These models charge a fee based on the search context size, which determines how much search data is retrieved and processed for a query.

### Search Context Size Thresholds

Search context can be 'low', 'medium', or 'high' and determines how much search context is retrieved for a query:

* **Low**: Minimal search context, suitable for basic queries
* **Medium**: Moderate search context, good for general queries
* **High**: Extensive search context, ideal for detailed research

### Specifying Search Context Size

You can specify the search context size in your API request using the `web_search_options` parameter:
```json
{
  "model": "openai/gpt-4.1",
  "messages": [
    {
      "role": "user",
      "content": "What are the latest developments in quantum computing?"
    }
  ],
  "web_search_options": {
    "search_context_size": "high"
  }
}
```

### OpenAI Model Pricing

For GPT-4.1, GPT-4o, and GPT-4o search preview Models:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$30.00                 |
| Medium              | \$35.00                 |
| High                | \$50.00                 |

For GPT-4.1-Mini, GPT-4o-Mini, and GPT-4o-Mini-Search-Preview Models:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$25.00                 |
| Medium              | \$27.50                 |
| High                | \$30.00                 |

### Perplexity Model Pricing

For Sonar and SonarReasoning:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$5.00                  |
| Medium              | \$8.00                  |
| High                | \$12.00                 |

For SonarPro and SonarReasoningPro:

| Search Context Size | Price per 1000 Requests |
| ------------------- | ----------------------- |
| Low                 | \$6.00                  |
| Medium              | \$10.00                 |
| High                | \$14.00                 |

<Note title="Engine Parameter">
  The pricing above applies when using `"engine": "native"` or when native search is used by default for supported models. When using `"engine": "exa"`, the Exa search pricing (\$4 per 1000 results) applies instead.
</Note>

<Note title="Pricing Documentation">
  For more detailed information about pricing models, refer to the official documentation:

  * [OpenAI Pricing](https://platform.openai.com/docs/pricing#web-search)
  * [Anthropic Pricing](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool#usage-and-pricing)
  * [Perplexity Pricing](https://docs.perplexity.ai/guides/pricing)
</Note>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
