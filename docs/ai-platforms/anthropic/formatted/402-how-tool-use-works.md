---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How tool use works

Claude supports two types of tools:

1. **Client tools**: Tools that execute on your systems, which include:
   * User-defined custom tools that you create and implement
   * Anthropic-defined tools like [computer use](/en/docs/agents-and-tools/tool-use/computer-use-tool) and [text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool) that require client implementation

2. **Server tools**: Tools that execute on Anthropic's servers, like the [web search](/en/docs/agents-and-tools/tool-use/web-search-tool) and [web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool) tools. These tools must be specified in the API request but don't require implementation on your part.

>   **📝 Note**
>
> Anthropic-defined tools use versioned types (e.g., `web_search_20250305`, `text_editor_20250124`) to ensure compatibility across model versions.

### Client tools

Integrate client tools with Claude in these steps:

<Steps>
  <Step title="Provide Claude with tools and a user prompt">
    * Define client tools with names, descriptions, and input schemas in your API request.
    * Include a user prompt that might require these tools, e.g., "What's the weather in San Francisco?"
  </Step>

  <Step title="Claude decides to use a tool">
    * Claude assesses if any tools can help with the user's query.
    * If yes, Claude constructs a properly formatted tool use request.
    * For client tools, the API response has a `stop_reason` of `tool_use`, signaling Claude's intent.
  </Step>

  <Step title="Execute the tool and return results">
    * Extract the tool name and input from Claude's request
    * Execute the tool code on your system
    * Return the results in a new `user` message containing a `tool_result` content block
  </Step>

  <Step title="Claude uses tool result to formulate a response">
    * Claude analyzes the tool results to craft its final response to the original user prompt.
  </Step>
</Steps>

Note: Steps 3 and 4 are optional. For some workflows, Claude's tool use request (step 2) might be all you need, without sending results back to Claude.

### Server tools

Server tools follow a different workflow:

<Steps>
  <Step title="Provide Claude with tools and a user prompt">
    * Server tools, like [web search](/en/docs/agents-and-tools/tool-use/web-search-tool) and [web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool), have their own parameters.
    * Include a user prompt that might require these tools, e.g., "Search for the latest news about AI" or "Analyze the content at this URL."
  </Step>

  <Step title="Claude executes the server tool">
    * Claude assesses if a server tool can help with the user's query.
    * If yes, Claude executes the tool, and the results are automatically incorporated into Claude's response.
  </Step>

  <Step title="Claude uses the server tool result to formulate a response">
    * Claude analyzes the server tool results to craft its final response to the original user prompt.
    * No additional user interaction is needed for server tool execution.
  </Step>
</Steps>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
