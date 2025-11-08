---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces.

| Feature                                                                                       | Description                                                                                                                                                        | Availability                                                    |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| [Bash](/en/docs/agents-and-tools/tool-use/bash-tool)                                          | Execute bash commands and scripts to interact with the system shell and perform command-line operations.                                                           | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Code execution](/en/docs/agents-and-tools/tool-use/code-execution-tool)                      | Run Python code in a sandboxed environment for advanced data analysis.                                                                                             | <PlatformAvailability claudeApiBeta />                          |
| [Computer use](/en/docs/agents-and-tools/tool-use/computer-use-tool)                          | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands.                                                                         | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta /> |
| [Fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters.                                                     | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [MCP connector](/en/docs/agents-and-tools/mcp-connector)                                      | Connect to remote [MCP](/en/docs/mcp) servers directly from the Messages API without a separate MCP client.                                                        | <PlatformAvailability claudeApiBeta />                          |
| [Memory](/en/docs/agents-and-tools/tool-use/memory-tool)                                      | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta /> |
| [Text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool)                            | Create and edit text files with a built-in text editor interface for file manipulation tasks.                                                                      | <PlatformAvailability claudeApi bedrock vertexAi />             |
| [Web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool)                                | Retrieve full content from specified web pages and PDF documents for in-depth analysis.                                                                            | <PlatformAvailability claudeApiBeta />                          |
| [Web search](/en/docs/agents-and-tools/tool-use/web-search-tool)                              | Augment Claude's comprehensive knowledge with current, real-world data from across the web.                                                                        | <PlatformAvailability claudeApi vertexAi />                     |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
