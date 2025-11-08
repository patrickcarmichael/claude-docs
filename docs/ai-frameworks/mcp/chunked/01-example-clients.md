# Example Clients

**Navigation:** [Index](./index.md) | [Next →](./02-build-an-mcp-server.md)

---

# Example Clients
Source: https://modelcontextprotocol.io/clients

A list of applications that support MCP integrations

This page provides an overview of applications that support the Model Context Protocol (MCP). Each client may support different MCP features, allowing for varying levels of integration with MCP servers.


## Feature support matrix

<div id="feature-support-matrix-wrapper">
  | Client                                                     | [Resources] | [Prompts] | [Tools] | [Discovery] | [Sampling] | [Roots] | [Elicitation] | [Instructions] |
  | ---------------------------------------------------------- | ----------- | --------- | ------- | ----------- | ---------- | ------- | ------------- | -------------- |
  | [5ire][5ire]                                               | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [AgentAI][AgentAI]                                         | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [AgenticFlow][AgenticFlow]                                 | ✅           | ✅         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [AIQL TUUI][AIQL TUUI]                                     | ✅           | ✅         | ✅       | ✅           | ✅          | ❌       | ✅             | ❓              |
  | [Amazon Q CLI][Amazon Q CLI]                               | ❌           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Amazon Q IDE][Amazon Q IDE]                               | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Amp][Amp]                                                 | ✅           | ✅         | ✅       | ❌           | ✅          | ❌       | ❓             | ❓              |
  | [Apify MCP Tester][Apify MCP Tester]                       | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [Augment Code][AugmentCode]                                | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Avatar Shell][Avatar Shell]                               | ✅           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [BeeAI Framework][BeeAI Framework]                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [BoltAI][BoltAI]                                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Call Chirp][Call Chirp]                                   | ❌           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Chatbox][Chatbox]                                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             | ❓              |
  | [ChatFrame][ChatFrame]                                     | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             | ❓              |
  | [ChatGPT][ChatGPT]                                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [ChatWise][ChatWise]                                       | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Claude.ai][Claude.ai]                                     | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Claude Code][Claude Code]                                 | ✅           | ✅         | ✅       | ❌           | ❌          | ✅       | ❓             | ✅              |
  | [Claude Desktop App][Claude Desktop]                       | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Chorus][Chorus]                                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Cline][Cline]                                             | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [CodeGPT][CodeGPT]                                         | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Continue][Continue]                                       | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Copilot-MCP][CopilotMCP]                                  | ✅           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Cursor][Cursor]                                           | ✅           | ✅         | ✅       | ❌           | ❌          | ✅       | ✅             | ❓              |
  | [Daydreams Agents][Daydreams]                              | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [ECA][ECA]                                                 | ✅           | ✅         | ✅       | ❌           | ❌          | ✅       | ❓             | ❓              |
  | [Emacs Mcp][Mcp.el]                                        | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [fast-agent][fast-agent]                                   | ✅           | ✅         | ✅       | ✅           | ✅          | ✅       | ✅             | ✅              |
  | [FlowDown][FlowDown]                                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❌             | ❓              |
  | [FLUJO][FLUJO]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Genkit][Genkit]                                           | ⚠️          | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Glama][Glama]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Gemini CLI][Gemini CLI]                                   | ❌           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [GenAIScript][GenAIScript]                                 | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [GitHub Copilot coding agent][GitHubCopilotCodingAgent]    | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             | ❓              |
  | [Goose][Goose]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ✅              |
  | [gptme][gptme]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [HyperAgent][HyperAgent]                                   | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Jenova][Jenova]                                           | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [JetBrains AI Assistant][JetBrains AI Assistant]           | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [JetBrains Junie][JetBrains Junie]                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             | ❓              |
  | [Kilo Code][Kilo Code]                                     | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [Klavis AI Slack/Discord/Web][Klavis AI]                   | ✅           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Langflow][Langflow]                                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [LibreChat][LibreChat]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ✅              |
  | [LM-Kit.NET][LM-Kit.NET]                                   | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             | ❓              |
  | [LM Studio][LM Studio]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Lutra][Lutra]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [MCP Bundler for MacOS][mcp-bundler]                       | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❌             | ❓              |
  | [mcp-agent][mcp-agent]                                     | ✅           | ✅         | ✅       | ❓           | ⚠️         | ✅       | ✅             | ❓              |
  | [mcp-client-chatbot][mcp-client-chatbot]                   | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [MCPJam][MCPJam]                                           | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ✅             | ❓              |
  | [mcp-use][mcp-use]                                         | ✅           | ✅         | ✅       | ✅           | ✅          | ❌       | ✅             | ❓              |
  | [modelcontextchat.com][modelcontextchat.com]               | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [MCPHub][MCPHub]                                           | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [MCPOmni-Connect][MCPOmni-Connect]                         | ✅           | ✅         | ✅       | ❓           | ✅          | ❌       | ❓             | ❓              |
  | [Memex][Memex]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Microsoft Copilot Studio]                                 | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [MindPal][MindPal]                                         | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Mistral AI: Le Chat][Mistral AI: Le Chat]                 | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [MooPoint][MooPoint]                                       | ❌           | ❌         | ✅       | ❓           | ✅          | ❌       | ❓             | ❓              |
  | [Msty Studio][Msty Studio]                                 | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Needle][Needle]                                           | ✅           | ✅         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [NVIDIA Agent Intelligence toolkit][AIQ toolkit]           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [OpenSumi][OpenSumi]                                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [oterm][oterm]                                             | ❌           | ✅         | ✅       | ❓           | ✅          | ❌       | ❓             | ❓              |
  | [Postman][postman]                                         | ✅           | ✅         | ✅       | ✅           | ✅          | ❌       | ✅             | ❓              |
  | [RecurseChat][RecurseChat]                                 | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Roo Code][Roo Code]                                       | ✅           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Shortwave][Shortwave]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Simtheory][Simtheory]                                     | ✅           | ✅         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [Slack MCP Client][Slack MCP Client]                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Smithery Playground][Smithery Playground]                 | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [SpinAI][SpinAI]                                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Superinterface][Superinterface]                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Superjoin][Superjoin]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Swarms][Swarms]                                           | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [systemprompt][systemprompt]                               | ✅           | ✅         | ✅       | ❓           | ✅          | ❌       | ❓             | ❓              |
  | [Tambo][Tambo]                                             | ❌           | ✅         | ✅       | ✅           | ✅          | ❌       | ✅             | ❓              |
  | [Tencent CloudBase AI DevKit][Tencent CloudBase AI DevKit] | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [TheiaAI/TheiaIDE][TheiaAI/TheiaIDE]                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Tome][Tome]                                               | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [TypingMind App][TypingMind App]                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [VS Code GitHub Copilot][VS Code]                          | ✅           | ✅         | ✅       | ✅           | ✅          | ✅       | ✅             | ✅              |
  | [VT Code][VT Code]                                         | ✅           | ✅         | ✅       | ✅           | ⚠️         | ✅       | ✅             | ❓              |
  | [Warp][Warp]                                               | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [WhatsMCP][WhatsMCP]                                       | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Windsurf Editor][Windsurf]                                | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             | ❓              |
  | [Witsy][Witsy]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             | ❓              |
  | [Zed][Zed]                                                 | ❌           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |
  | [Zencoder][Zencoder]                                       | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             | ❓              |

  [Resources]: /docs/concepts/resources

  [Prompts]: /docs/concepts/prompts

  [Tools]: /docs/concepts/tools

  [Discovery]: /docs/concepts/tools#tool-discovery-and-updates

  [Sampling]: /docs/concepts/sampling

  [Roots]: /docs/concepts/roots

  [Elicitation]: /docs/concepts/elicitation

  [Instructions]: https://modelcontextprotocol.io/specification/2025-06-18/schema#initializeresult

  [5ire]: https://github.com/nanbingxyz/5ire

  [AgentAI]: https://github.com/AdamStrojek/rust-agentai

  [AgenticFlow]: https://agenticflow.ai/mcp

  [AIQ toolkit]: https://github.com/NVIDIA/AIQToolkit

  [AIQL TUUI]: https://github.com/AI-QL/tuui

  [Amazon Q CLI]: https://github.com/aws/amazon-q-developer-cli

  [Amazon Q IDE]: https://aws.amazon.com/q/developer

  [Amp]: https://ampcode.com

  [Apify MCP Tester]: https://apify.com/jiri.spilka/tester-mcp-client

  [AugmentCode]: https://augmentcode.com

  [Avatar Shell]: https://github.com/mfukushim/avatar-shell

  [BeeAI Framework]: https://framework.beeai.dev

  [BoltAI]: https://boltai.com

  [Call Chirp]: https://www.call-chirp.com

  [Chatbox]: https://chatboxai.app

  [ChatFrame]: https://chatframe.co

  [ChatGPT]: https://chatgpt.com

  [ChatWise]: https://chatwise.app

  [Claude.ai]: https://claude.ai

  [Claude Code]: https://claude.com/product/claude-code

  [Claude Desktop]: https://claude.ai/download

  [Chorus]: https://chorus.sh

  [Cline]: https://github.com/cline/cline

  [CodeGPT]: https://codegpt.co

  [Continue]: https://github.com/continuedev/continue

  [CopilotMCP]: https://github.com/VikashLoomba/copilot-mcp

  [Cursor]: https://cursor.com

  [Daydreams]: https://github.com/daydreamsai/daydreams

  [ECA]: https://eca.dev

  [Klavis AI]: https://www.klavis.ai/

  [Mcp.el]: https://github.com/lizqwerscott/mcp.el

  [fast-agent]: https://github.com/evalstate/fast-agent

  [FlowDown]: https://github.com/Lakr233/FlowDown

  [FLUJO]: https://github.com/mario-andreschak/flujo

  [Glama]: https://glama.ai/chat

  [Gemini CLI]: https://goo.gle/gemini-cli

  [Genkit]: https://github.com/firebase/genkit

  [GenAIScript]: https://microsoft.github.io/genaiscript/reference/scripts/mcp-tools/

  [GitHubCopilotCodingAgent]: https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/about-copilot-coding-agent

  [Goose]: https://block.github.io/goose/docs/goose-architecture/#interoperability-with-extensions

  [Jenova]: https://www.jenova.ai

  [JetBrains AI Assistant]: https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant

  [JetBrains Junie]: https://www.jetbrains.com/junie

  [Kilo Code]: https://github.com/Kilo-Org/kilocode

  [Langflow]: https://github.com/langflow-ai/langflow

  [LibreChat]: https://github.com/danny-avila/LibreChat

  [LM-Kit.NET]: https://lm-kit.com/products/lm-kit-net/

  [LM Studio]: https://lmstudio.ai

  [Lutra]: https://lutra.ai

  [mcp-bundler]: https://mcp-bundler.maketry.xyz

  [mcp-agent]: https://github.com/lastmile-ai/mcp-agent

  [mcp-client-chatbot]: https://github.com/cgoinglove/mcp-client-chatbot

  [MCPJam]: https://github.com/MCPJam/inspector

  [mcp-use]: https://github.com/pietrozullo/mcp-use

  [modelcontextchat.com]: https://modelcontextchat.com

  [MCPHub]: https://github.com/ravitemer/mcphub.nvim

  [MCPOmni-Connect]: https://github.com/Abiorh001/mcp_omni_connect

  [Memex]: https://memex.tech/

  [Microsoft Copilot Studio]: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp

  [MindPal]: https://mindpal.io

  [Mistral AI: Le Chat]: https://chat.mistral.ai

  [MooPoint]: https://moopoint.io

  [Msty Studio]: https://msty.ai

  [Needle]: https://needle.app

  [OpenSumi]: https://github.com/opensumi/core

  [oterm]: https://github.com/ggozad/oterm

  [Postman]: https://postman.com/downloads

  [RecurseChat]: https://recurse.chat/

  [Roo Code]: https://roocode.com

  [Shortwave]: https://www.shortwave.com

  [Simtheory]: https://simtheory.ai

  [Slack MCP Client]: https://github.com/tuannvm/slack-mcp-client

  [Smithery Playground]: https://smithery.ai/playground

  [SpinAI]: https://docs.spinai.dev

  [Superinterface]: https://superinterface.ai

  [Superjoin]: https://superjoin.ai

  [Swarms]: https://github.com/kyegomez/swarms

  [systemprompt]: https://systemprompt.io

  [Tambo]: https://tambo.co

  [Tencent CloudBase AI DevKit]: https://docs.cloudbase.net/ai/agent/mcp

  [TheiaAI/TheiaIDE]: https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/

  [Tome]: https://github.com/runebookai/tome

  [TypingMind App]: https://www.typingmind.com

  [VS Code]: https://code.visualstudio.com/

  [VT Code]: https://github.com/vinhnx/vtcode

  [Windsurf]: https://codeium.com/windsurf

  [gptme]: https://github.com/gptme/gptme

  [Warp]: https://www.warp.dev/

  [WhatsMCP]: https://wassist.app/mcp/

  [Witsy]: https://github.com/nbonamy/witsy

  [Zed]: https://zed.dev

  [Zencoder]: https://zencoder.ai

  [HyperAgent]: https://github.com/hyperbrowserai/HyperAgent
</div>


## Client details

### 5ire

[5ire](https://github.com/nanbingxyz/5ire) is an open source cross-platform desktop AI assistant that supports tools through MCP servers.

**Key features:**

* Built-in MCP servers can be quickly enabled and disabled.
* Users can add more servers by modifying the configuration file.
* It is open-source and user-friendly, suitable for beginners.
* Future support for MCP will be continuously improved.

### AgentAI

[AgentAI](https://github.com/AdamStrojek/rust-agentai) is a Rust library designed to simplify the creation of AI agents. The library includes seamless integration with MCP Servers.

[Example of MCP Server integration](https://github.com/AdamStrojek/rust-agentai/blob/master/examples/tools_mcp.rs)

**Key features:**

* Multi-LLM – We support most LLM APIs (OpenAI, Anthropic, Gemini, Ollama, and all OpenAI API Compatible).
* Built-in support for MCP Servers.
* Create agentic flows in a type- and memory-safe language like Rust.

### AgenticFlow

[AgenticFlow](https://agenticflow.ai/) is a no-code AI platform that helps you build agents that handle sales, marketing, and creative tasks around the clock. Connect 2,500+ APIs and 10,000+ tools securely via MCP.

**Key features:**

* No-code AI agent creation and workflow building.
* Access a vast library of 10,000+ tools and 2,500+ APIs through MCP.
* Simple 3-step process to connect MCP servers.
* Securely manage connections and revoke access anytime.

**Learn more:**

* [AgenticFlow MCP Integration](https://agenticflow.ai/mcp)

### AIQL TUUI

[AIQL TUUI] is a native, cross-platform desktop AI chat application with MCP support. It supports multiple AI providers (e.g., Anthropic, Cloudflare, Deepseek, OpenAI, Qwen), local AI models (via vLLM, Ray, etc.), and aggregated API platforms (such as Deepinfra, Openrouter, and more).

**Key features:**

* **Dynamic LLM API & Agent Switching**: Seamlessly toggle between different LLM APIs and agents on the fly.
* **Comprehensive Capabilities Support**: Built-in support for tools, prompts, resources, and sampling methods.
* **Configurable Agents**: Enhanced flexibility with selectable and customizable tools via agent settings.
* **Advanced Sampling Control**: Modify sampling parameters and leverage multi-round sampling for optimal results.
* **Cross-Platform Compatibility**: Fully compatible with macOS, Windows, and Linux.
* **Free & Open-Source (FOSS)**: Permissive licensing allows modifications and custom app bundling.

**Learn more:**

* [TUUI document](https://www.tuui.com/)
* [AIQL GitHub repository](https://github.com/AI-QL)

### Amazon Q CLI

[Amazon Q CLI](https://github.com/aws/amazon-q-developer-cli) is an open-source, agentic coding assistant for terminals.

**Key features:**

* Full support for MCP servers.
* Edit prompts using your preferred text editor.
* Access saved prompts instantly with `@`.
* Control and organize AWS resources directly from your terminal.
* Tools, profiles, context management, auto-compact, and so much more!

**Get Started**

```bash  theme={null}
brew install amazon-q
```

### Amazon Q IDE

[Amazon Q IDE](https://aws.amazon.com/q/developer) is an open-source, agentic coding assistant for IDEs.

**Key features:**

* Support for the VSCode, JetBrains, Visual Studio, and Eclipse IDEs.
* Control and organize AWS resources directly from your IDE.
* Manage permissions for each MCP tool via the IDE user interface.

### Apify MCP Tester

[Apify MCP Tester](https://github.com/apify/tester-mcp-client) is an open-source client that connects to any MCP server using Server-Sent Events (SSE).
It is a standalone Apify Actor designed for testing MCP servers over SSE, with support for Authorization headers.
It uses plain JavaScript (old-school style) and is hosted on Apify, allowing you to run it without any setup.

**Key features:**

* Connects to any MCP server via SSE.
* Works with the [Apify MCP Server](https://apify.com/apify/actors-mcp-server) to interact with one or more Apify [Actors](https://apify.com/store).
* Dynamically utilizes tools based on context and user queries (if supported by the server).

### Amp

[Amp](https://ampcode.com) is an agentic coding tool built by Sourcegraph. It runs in VS Code (and compatible forks like Cursor, Windsurf, and VSCodium), JetBrains IDEs, Neovim, and as a command-line tool. It’s also multiplayer — you can share threads and collaborate with your team.

**Key features:**

* Granular control over enabled tools and permissions
* Support for MCP servers defined in VS Code `mcp.json`

### Augment Code

[Augment Code](https://augmentcode.com) is an AI-powered coding platform for VS Code and JetBrains with autonomous agents, chat, and completions. Both local and remote agents are backed by full codebase awareness and native support for MCP, enabling enhanced context through external sources and tools.

**Key features:**

* Full MCP support in local and remote agents.
* Add additional context through MCP servers.
* Automate your development workflows with MCP tools.
* Works in VS Code and JetBrains IDEs.

### Avatar Shell

[Avatar-Shell](https://github.com/mfukushim/avatar-shell) is an electron-based MCP client application that prioritizes avatar conversations and media output such as images.

**Key features:**

* MCP tools and resources can be used
* Supports avatar-to-avatar communication via socket.io.
* Supports the mixed use of multiple LLM APIs.
* The daemon mechanism allows for flexible scheduling.

### BeeAI Framework

[BeeAI Framework](https://framework.beeai.dev) is an open-source framework for building, deploying, and serving powerful agentic workflows at scale. The framework includes the **MCP Tool**, a native feature that simplifies the integration of MCP servers into agentic workflows.

**Key features:**

* Seamlessly incorporate MCP tools into agentic workflows.
* Quickly instantiate framework-native tools from connected MCP client(s).
* Planned future support for agentic MCP capabilities.

**Learn more:**

* [Example of using MCP tools in agentic workflow](https://i-am-bee.github.io/beeai-framework/#/typescript/tools?id=using-the-mcptool-class)

### BoltAI

[BoltAI](https://boltai.com) is a native, all-in-one AI chat client with MCP support. BoltAI supports multiple AI providers (OpenAI, Anthropic, Google AI...), including local AI models (via Ollama, LM Studio or LMX)

**Key features:**

* MCP Tool integrations: once configured, user can enable individual MCP server in each chat
* MCP quick setup: import configuration from Claude Desktop app or Cursor editor
* Invoke MCP tools inside any app with AI Command feature
* Integrate with remote MCP servers in the mobile app

**Learn more:**

* [BoltAI docs](https://boltai.com/docs/plugins/mcp-servers)
* [BoltAI website](https://boltai.com)

### Call Chirp

[Call Chirp] [https://www.call-chirp.com](https://www.call-chirp.com) uses AI to capture every critical detail from your business conversations, automatically syncing insights to your CRM and project tools so you never miss another deal-closing moment.

**Key features:**

* Save transcriptions from Zoom, Google Meet, and more
* MCP Tools for voice AI agents
* Remote MCP servers support

### Chatbox

Chatbox is a better UI and desktop app for ChatGPT, Claude, and other LLMs, available on Windows, Mac, Linux, and the web. It's open-source and has garnered 37K stars⭐ on GitHub.

**Key features:**

* Tools support for MCP servers
* Support both local and remote MCP servers
* Built-in MCP servers marketplace

### ChatFrame

A cross-platform desktop chatbot that unifies access to multiple AI language models, supports custom tool integration via MCP servers, and enables RAG conversations with your local files—all in a single, polished app for macOS and Windows.

**Key features:**

* Unified access to top LLM providers (OpenAI, Anthropic, DeepSeek, xAI, and more) in one interface
* Built-in retrieval-augmented generation (RAG) for instant, private search across your PDFs, text, and code files
* Plug-in system for custom tools via Model Context Protocol (MCP) servers
* Multimodal chat: supports images, text, and live interactive artifacts

### ChatGPT

ChatGPT is OpenAI's AI assistant that provides MCP support for remote servers to conduct deep research.

**Key features:**

* Support for MCP via connections UI in settings
* Access to search tools from configured MCP servers for deep research
* Enterprise-grade security and compliance features

### ChatWise

ChatWise is a desktop-optimized, high-performance chat application that lets you bring your own API keys. It supports a wide range of LLMs and integrates with MCP to enable tool workflows.

**Key features:**

* Tools support for MCP servers
* Offer built-in tools like web search, artifacts and image generation.

### Claude Code

Claude Code is an interactive agentic coding tool from Anthropic that helps you code faster through natural language commands. It supports MCP integration for resources, prompts, tools, and roots, and also functions as an MCP server to integrate with other clients.

**Key features:**

* Full support for resources, prompts, tools, and roots from MCP servers
* Offers its own tools through an MCP server for integrating with other MCP clients

### Claude.ai

[Claude.ai](https://claude.ai) is Anthropic's web-based AI assistant that provides MCP support for remote servers.

**Key features:**

* Support for remote MCP servers via integrations UI in settings
* Access to tools, prompts, and resources from configured MCP servers
* Seamless integration with Claude's conversational interface
* Enterprise-grade security and compliance features

### Claude Desktop App

The Claude desktop application provides comprehensive support for MCP, enabling deep integration with local tools and data sources.

**Key features:**

* Full support for resources, allowing attachment of local files and data
* Support for prompt templates
* Tool integration for executing commands and scripts
* Local server connections for enhanced privacy and security

### Chorus

[Chorus](https://chorus.sh) is a native Mac app for chatting with AIs. Chat with multiple models at once, run tools and MCPs, create projects, quick chat, bring your own key, all in a blazing fast, keyboard shortcut friendly app.

**Key features:**

* MCP support with one-click install
* Built in tools, like web search, terminal, and image generation
* Chat with multiple models at once (cloud or local)
* Create projects with scoped memory
* Quick chat with an AI that can see your screen

### Cline

[Cline](https://github.com/cline/cline) is an autonomous coding agent in VS Code that edits files, runs commands, uses a browser, and more–with your permission at each step.

**Key features:**

* Create and add tools through natural language (e.g. "add a tool that searches the web")
* Share custom MCP servers Cline creates with others via the `~/Documents/Cline/MCP` directory
* Displays configured MCP servers along with their tools, resources, and any error logs

### CodeGPT

[CodeGPT](https://codegpt.co) is a popular VS Code and Jetbrains extension that brings AI-powered coding assistance to your editor. It supports integration with MCP servers for tools, allowing users to leverage external AI capabilities directly within their development workflow.

**Key features:**

* Use MCP tools from any configured MCP server
* Seamless integration with VS Code and Jetbrains UI
* Supports multiple LLM providers and custom endpoints

**Learn more:**

* [CodeGPT Documentation](https://docs.codegpt.co/)

### Continue

[Continue](https://github.com/continuedev/continue) is an open-source AI code assistant, with built-in support for all MCP features.

**Key features:**

* Type "@" to mention MCP resources
* Prompt templates surface as slash commands
* Use both built-in and MCP tools directly in chat
* Supports VS Code and JetBrains IDEs, with any LLM

### Copilot-MCP

[Copilot-MCP](https://github.com/VikashLoomba/copilot-mcp) enables AI coding assistance via MCP.

**Key features:**

* Support for MCP tools and resources
* Integration with development workflows
* Extensible AI capabilities

### Cursor

[Cursor](https://docs.cursor.com/context/mcp#protocol-support) is an AI code editor.

**Key features:**

* Support for MCP tools in Cursor Composer
* Support for roots
* Support for prompts
* Support for elicitation
* Support for both STDIO and SSE

### Daydreams

[Daydreams](https://github.com/daydreamsai/daydreams) is a generative agent framework for executing anything onchain

**Key features:**

* Supports MCP Servers in config
* Exposes MCP Client

### ECA - Editor Code Assistant

[ECA](https://eca.dev) is a Free and open-source editor-agnostic tool that aims to easily link LLMs and Editors, giving the best UX possible for AI pair programming using a well-defined protocol

**Key features:**

* **Editor-agnostic**: protocol for any editor to integrate.
* **Single configuration**: Configure eca making it work the same in any editor via global or local configs.
* **Chat** interface: ask questions, review code, work together to code.
* **Agentic**: let LLM work as an agent with its native tools and MCPs you can configure.
* **Context**: support: giving more details about your code to the LLM, including MCP resources and prompts.
* **Multi models**: Login to OpenAI, Anthropic, Copilot, Ollama local models and many more.
* **OpenTelemetry**: Export metrics of tools, prompts, server usage.

**Learn more:**

* [ECA website](https://eca.dev)
* [ECA source code](https://github.com/editor-code-assistant/eca)

### Emacs Mcp

[Emacs Mcp](https://github.com/lizqwerscott/mcp.el) is an Emacs client designed to interface with MCP servers, enabling seamless connections and interactions. It provides MCP tool invocation support for AI plugins like [gptel](https://github.com/karthink/gptel) and [llm](https://github.com/ahyatt/llm), adhering to Emacs' standard tool invocation format. This integration enhances the functionality of AI tools within the Emacs ecosystem.

**Key features:**

* Provides MCP tool support for Emacs.

### fast-agent

[fast-agent](https://github.com/evalstate/fast-agent) is a Python Agent framework, with simple declarative support for creating Agents and Workflows, with full multi-modal support for Anthropic and OpenAI models.

**Key features:**

* PDF and Image support, based on MCP Native types
* Interactive front-end to develop and diagnose Agent applications, including passthrough and playback simulators
* Built in support for "Building Effective Agents" workflows.
* Deploy Agents as MCP Servers

### FlowDown

[FlowDown](https://github.com/Lakr233/FlowDown) is a blazing fast and smooth client app for using AI/LLM, with a strong emphasis on privacy and user experience. It supports MCP servers to extend its capabilities with external tools, allowing users to build powerful, customized workflows.

**Key features:**

* **Seamless MCP Integration**: Easily connect to MCP servers to utilize a wide range of external tools.
* **Privacy-First Design**: Your data stays on your device. We don't collect any user data, ensuring complete privacy.
* **Lightweight & Efficient**: A compact and optimized design ensures a smooth and responsive experience with any AI model.
* **Broad Compatibility**: Works with all OpenAI-compatible service providers and supports local offline models through MLX.
* **Rich User Experience**: Features beautifully formatted Markdown, blazing-fast text rendering, and intelligent, automated chat titling.

**Learn more:**

* [FlowDown website](https://flowdown.ai/)
* [FlowDown documentation](https://apps.qaq.wiki/docs/flowdown/)

### FLUJO

Think n8n + ChatGPT. FLUJO is an desktop application that integrates with MCP to provide a workflow-builder interface for AI interactions. Built with Next.js and React, it supports both online and offline (ollama) models, it manages API Keys and environment variables centrally and can install MCP Servers from GitHub. FLUJO has an ChatCompletions endpoint and flows can be executed from other AI applications like Cline, Roo or Claude.

**Key features:**

* Environment & API Key Management
* Model Management
* MCP Server Integration
* Workflow Orchestration
* Chat Interface

### Genkit

[Genkit](https://github.com/firebase/genkit) is a cross-language SDK for building and integrating GenAI features into applications. The [genkitx-mcp](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) plugin enables consuming MCP servers as a client or creating MCP servers from Genkit tools and prompts.

**Key features:**

* Client support for tools and prompts (resources partially supported)
* Rich discovery with support in Genkit's Dev UI playground
* Seamless interoperability with Genkit's existing tools and prompts
* Works across a wide variety of GenAI models from top providers

### Glama

[Glama](https://glama.ai/chat) is a comprehensive AI workspace and integration platform that offers a unified interface to leading LLM providers, including OpenAI, Anthropic, and others. It supports the Model Context Protocol (MCP) ecosystem, enabling developers and enterprises to easily discover, build, and manage MCP servers.

**Key features:**

* Integrated [MCP Server Directory](https://glama.ai/mcp/servers)
* Integrated [MCP Tool Directory](https://glama.ai/mcp/tools)
* Host MCP servers and access them via the Chat or SSE endpoints
  – Ability to chat with multiple LLMs and MCP servers at once
* Upload and analyze local files and data
* Full-text search across all your chats and data

### GenAIScript

Programmatically assemble prompts for LLMs using [GenAIScript](https://microsoft.github.io/genaiscript/) (in JavaScript). Orchestrate LLMs, tools, and data in JavaScript.

**Key features:**

* JavaScript toolbox to work with prompts
* Abstraction to make it easy and productive
* Seamless Visual Studio Code integration

### Goose

[Goose](https://github.com/block/goose) is an open source AI agent that supercharges your software development by automating coding tasks.

**Key features:**

* Expose MCP functionality to Goose through tools.
* MCPs can be installed directly via the [extensions directory](https://block.github.io/goose/v1/extensions/), CLI, or UI.
* Goose allows you to extend its functionality by [building your own MCP servers](https://block.github.io/goose/docs/tutorials/custom-extensions).
* Includes built-in tools for development, web scraping, automation, memory, and integrations with JetBrains and Google Drive.

### GitHub Copilot coding agent

Delegate tasks to [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent) and let it work in the background while you stay focused on the highest-impact and most interesting work

**Key features:**

* Delegate tasks to Copilot from GitHub Issues, Visual Studio Code, GitHub Copilot Chat or from your favorite MCP host using the GitHub MCP Server
* Tailor Copilot to your project by [customizing the agent's development environment](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/customizing-the-development-environment-for-copilot-coding-agent#preinstalling-tools-or-dependencies-in-copilots-environment) or [writing custom instructions](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository)
* [Augment Copilot's context and capabilities with MCP tools](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp), with support for both local and remote MCP servers

### gptme

[gptme](https://github.com/gptme/gptme) is a open-source terminal-based personal AI assistant/agent, designed to assist with programming tasks and general knowledge work.

**Key features:**

* CLI-first design with a focus on simplicity and ease of use
* Rich set of built-in tools for shell commands, Python execution, file operations, and web browsing
* Local-first approach with support for multiple LLM providers
* Open-source, built to be extensible and easy to modify

### HyperAgent

[HyperAgent](https://github.com/hyperbrowserai/HyperAgent) is Playwright supercharged with AI. With HyperAgent, you no longer need brittle scripts, just powerful natural language commands. Using MCP servers, you can extend the capability of HyperAgent, without having to write any code.

**Key features:**

* AI Commands: Simple APIs like page.ai(), page.extract() and executeTask() for any AI automation
* Fallback to Regular Playwright: Use regular Playwright when AI isn't needed
* Stealth Mode – Avoid detection with built-in anti-bot patches
* Cloud Ready – Instantly scale to hundreds of sessions via [Hyperbrowser](https://www.hyperbrowser.ai/)
* MCP Client – Connect to tools like Composio for full workflows (e.g. writing web data to Google Sheets)

### Jenova

[Jenova](https://jenova.ai) is the best MCP client for non-technical users, especially on mobile.

**Key features:**

* 30+ pre-integrated MCP servers with one-click integration of custom servers
* MCP recommendation capability that suggests the best servers for specific tasks
* Multi-agent architecture with leading tool use reliability and scalability, supporting unlimited concurrent MCP server connections through RAG-powered server metadata
* Model agnostic platform supporting any leading LLMs (OpenAI, Anthropic, Google, etc.)
* Unlimited chat history and global persistent memory powered by RAG
* Easy creation of custom agents with custom models, instructions, knowledge bases, and MCP servers
* Local MCP server (STDIO) support coming soon with desktop apps

### JetBrains AI Assistant

[JetBrains AI Assistant](https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant) plugin provides AI-powered features for software development available in all JetBrains IDEs.

**Key features:**

* Unlimited code completion powered by Mellum, JetBrains’ proprietary AI model.
* Context-aware AI chat that understands your code and helps you in real time.
* Access to top-tier models from OpenAI, Anthropic, and Google.
* Offline mode with connected local LLMs via Ollama or LM Studio.
* Deep integration into IDE workflows, including code suggestions in the editor, VCS assistance, runtime error explanation, and more.

### JetBrains Junie

[Junie](https://www.jetbrains.com/junie) is JetBrains’ AI coding agent for JetBrains IDEs and Android Studio.

**Key features:**

* Connects to MCP servers over **stdio** to use external tools and data sources.
* Per-command approval with an optional allowlist.
* Config via `mcp.json` (global `~/.junie/mcp.json` or project `.junie/mcp/`).

### Kilo Code

[Kilo Code](https://github.com/Kilo-Org/kilocode) is an autonomous coding AI dev team in VS Code that edits files, runs commands, uses a browser, and more.

**Key features:**

* Create and add tools through natural language (e.g. "add a tool that searches the web")
* Discover MCP servers via the MCP Marketplace
* One click MCP server installs via MCP Marketplace
* Displays configured MCP servers along with their tools, resources, and any error logs

### Klavis AI Slack/Discord/Web

[Klavis AI](https://www.klavis.ai/) is an Open-Source Infra to Use, Build & Scale MCPs with ease.

**Key features:**

* Slack/Discord/Web MCP clients for using MCPs directly
* Simple web UI dashboard for easy MCP configuration
* Direct OAuth integration with Slack & Discord Clients and MCP Servers for secure user authentication
* SSE transport support
* Open-source infrastructure ([GitHub repository](https://github.com/Klavis-AI/klavis))

**Learn more:**

* [Demo video showing MCP usage in Slack/Discord](https://youtu.be/9-QQAhrQWw8)

### Langflow

Langflow is an open-source visual builder that lets developers rapidly prototype and build AI applications, it integrates with the Model Context Protocol (MCP) as both an MCP server and an MCP client.

**Key features:**

* Full support for using MCP server tools to build agents and flows.
* Export agents and flows as MCP server
* Local & remote server connections for enhanced privacy and security

**Learn more:**

* [Demo video showing how to use Langflow as both an MCP client & server](https://www.youtube.com/watch?v=pEjsaVVPjdI)

### LibreChat

[LibreChat](https://github.com/danny-avila/LibreChat) is an open-source, customizable AI chat UI that supports multiple AI providers, now including MCP integration.

**Key features:**

* Extend current tool ecosystem, including [Code Interpreter](https://www.librechat.ai/docs/features/code_interpreter) and Image generation tools, through MCP servers
* Add tools to customizable [Agents](https://www.librechat.ai/docs/features/agents), using a variety of LLMs from top providers
* Open-source and self-hostable, with secure multi-user support
* Future roadmap includes expanded MCP feature support

### LM-Kit.NET

[LM-Kit.NET] is a local-first Generative AI SDK for .NET (C# / VB.NET) that can act as an **MCP client**. Current MCP support: **Tools only**.

**Key features:**

* Consume MCP server tools over HTTP/JSON-RPC 2.0 (initialize, list tools, call tools).
* Programmatic tool discovery and invocation via `McpClient`.
* Easy integration in .NET agents and applications.

**Learn more:**

* [Docs: Using MCP in LM-Kit.NET](https://docs.lm-kit.com/lm-kit-net/api/LMKit.Mcp.Client.McpClient.html)
* [Creating AI agents](https://lm-kit.com/solutions/ai-agents)
* Product page: [LM-Kit.NET]

### LM Studio

[LM Studio](https://lmstudio.ai) is a cross-platform desktop app for discovering, downloading, and running open-source LLMs locally. You can now connect local models to tools via Model Context Protocol (MCP).

**Key features:**

* Use MCP servers with local models on your computer. Add entries to `mcp.json` and save to get started.
* Tool confirmation UI: when a model calls a tool, you can confirm the call in the LM Studio app.
* Cross-platform: runs on macOS, Windows, and Linux, one-click installer with no need to fiddle in the command line
* Supports GGUF (llama.cpp) or MLX models with GPU acceleration
* GUI & terminal mode: use the LM Studio app or CLI (lms) for scripting and automation

**Learn more:**

* [Docs: Using MCP in LM Studio](https://lmstudio.ai/docs/app/plugins/mcp)
* [Create a 'Add to LM Studio' button for your server](https://lmstudio.ai/docs/app/plugins/mcp/deeplink)
* [Announcement blog: LM Studio + MCP](https://lmstudio.ai/blog/mcp)

### Lutra

[Lutra](https://lutra.ai) is an AI agent that transforms conversations into actionable, automated workflows.

**Key features:**

* Easy MCP Integration: Connecting Lutra to MCP servers is as simple as providing the server URL; Lutra handles the rest behind the scenes.
* Chat to Take Action: Lutra understands your conversational context and goals, automatically integrating with your existing apps to perform tasks.
* Reusable Playbooks: After completing a task, save the steps as reusable, automated workflows—simplifying repeatable processes and reducing manual effort.
* Shareable Automations: Easily share your saved playbooks with teammates to standardize best practices and accelerate collaborative workflows.

**Learn more:**

* [Lutra AI agent explained](https://www.youtube.com/watch?v=W5ZpN0cMY70)

### MCP Bundler for MacOS

[MCP Bundler](https://mcp-bundler.maketry.xyz) is perfect local proxy for your MCP workflow. The app centralizes all your MCP servers — toggle, group, turn off capabilities instantly. Switch bundles on the fly inside the MCP Bundler.

**Key features:**

* Unified Control Panel: Manage all your MCP servers — both Local STDIO and Remote HTTP/SSE — from one clear macOS window. Start, stop, or edit them instantly without touching configs.
* One Click, All Connected: Launch or disable entire MCP setups with one toggle. Switch bundles per project or workspace and keep your AI tools synced automatically.
* Per-Tool Control: Enable or hide individual tools inside each server. Keep your bundles clean, lightweight, and tailored for every AI workflow.
* Instant Health & Logs: Real-time health indicators and request logs show exactly what’s running. Diagnose and fix connection issues without leaving the app.
* Auto-Generate MCP Config: Copy a ready-made JSON snippet for any client in seconds. No manual wiring — connect your Bundler as a single MCP endpoint.

**Learn more:**

* [MCP Bundler in action](https://www.youtube.com/watch?v=CEHVSShw_NU)

### mcp-agent

[mcp-agent] is a simple, composable framework to build agents using Model Context Protocol.

**Key features:**

* Automatic connection management of MCP servers.
* Expose tools from multiple servers to an LLM.
* Implements every pattern defined in [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents).
* Supports workflow pause/resume signals, such as waiting for human feedback.

### mcp-client-chatbot

[mcp-client-chatbot](https://github.com/cgoinglove/mcp-client-chatbot) is a local-first chatbot built with Vercel's Next.js, AI SDK, and Shadcn UI.

**Key features:**

* It supports standard MCP tool calling and includes both a custom MCP server and a standalone UI for testing MCP tools outside the chat flow.
* All MCP tools are provided to the LLM by default, but the project also includes an optional `@toolname` mention feature to make tool invocation more explicit—particularly useful when connecting to multiple MCP servers with many tools.
* Visual workflow builder that lets you create custom tools by chaining LLM nodes and MCP tools together. Published workflows become callable as `@workflow_name` tools in chat, enabling complex multi-step automation sequences.

### MCPJam

[MCPJam] is an open source testing and debugging tool for MCP servers - Postman for MCP servers.

**Key features:**

* Test your MCP server's tools, resources, prompts, and OAuth. MCP spec compliant.
* LLM playground to test your server against different LLMs.
* Tracing and logging error messages.
* Connect and test multiple MCP servers simultaneously.
* Supports all transports - STDIO, SSE, and Streamable HTTP.

### mcp-use

[mcp-use] is an open source python library to very easily connect any LLM to any MCP server both locally and remotely.

**Key features:**

* Very simple interface to connect any LLM to any MCP.
* Support the creation of custom agents, workflows.
* Supports connection to multiple MCP servers simultaneously.
* Supports all langchain supported models, also locally.
* Offers efficient tool orchestration and search functionalities.

### modelcontextchat.com

[modelcontextchat.com](https://modelcontextchat.com) is a web-based MCP client designed for working with remote MCP servers, featuring comprehensive authentication support and integration with OpenRouter.

**Key features:**

* Web-based interface for remote MCP server connections
* Header-based Authorization support for secure server access
* OAuth authentication integration
* OpenRouter API Key support for accessing various LLM providers
* No installation required - accessible from any web browser

### MCPHub

[MCPHub] is a powerful Neovim plugin that integrates MCP (Model Context Protocol) servers into your workflow.

**Key features:**

* Install, configure and manage MCP servers with an intuitive UI.
* Built-in Neovim MCP server with support for file operations (read, write, search, replace), command execution, terminal integration, LSP integration, buffers, and diagnostics.
* Create Lua-based MCP servers directly in Neovim.
* Inegrates with popular Neovim chat plugins Avante.nvim and CodeCompanion.nvim

### MCPOmni-Connect

[MCPOmni-Connect](https://github.com/Abiorh001/mcp_omni_connect) is a versatile command-line interface (CLI) client designed to connect to various Model Context Protocol (MCP) servers using both stdio and SSE transport.

**Key features:**

* Support for resources, prompts, tools, and sampling
* Agentic mode with ReAct and orchestrator capabilities
* Seamless integration with OpenAI models and other LLMs
* Dynamic tool and resource management across multiple servers
* Support for both stdio and SSE transport protocols
* Comprehensive tool orchestration and resource analysis capabilities

### Memex

[Memex](https://memex.tech/) is the first MCP client and MCP server builder - all-in-one desktop app. Unlike traditional MCP clients that only consume existing servers, Memex can create custom MCP servers from natural language prompts, immediately integrate them into its toolkit, and use them to solve problems—all within a single conversation.

**Key features:**

* **Prompt-to-MCP Server**: Generate fully functional MCP servers from natural language descriptions
* **Self-Testing & Debugging**: Autonomously test, debug, and improve created MCP servers
* **Universal MCP Client**: Works with any MCP server through intuitive, natural language integration
* **Curated MCP Directory**: Access to tested, one-click installable MCP servers (Neon, Netlify, GitHub, Context7, and more)
* **Multi-Server Orchestration**: Leverage multiple MCP servers simultaneously for complex workflows

**Learn more:**

* [Memex Launch 2: MCP Teams and Agent API](https://memex.tech/blog/memex-launch-2-mcp-teams-and-agent-api-private-preview-125f)

### Microsoft Copilot Studio

[Microsoft Copilot Studio] is a robust SaaS platform designed for building custom AI-driven applications and intelligent agents, empowering developers to create, deploy, and manage sophisticated AI solutions.

**Key features:**

* Support for MCP tools
* Extend Copilot Studio agents with MCP servers
* Leveraging Microsoft unified, governed, and secure API management solutions

### MindPal

[MindPal](https://mindpal.io) is a no-code platform for building and running AI agents and multi-agent workflows for business processes.

**Key features:**

* Build custom AI agents with no-code
* Connect any SSE MCP server to extend agent tools
* Create multi-agent workflows for complex business processes
* User-friendly for both technical and non-technical professionals
* Ongoing development with continuous improvement of MCP support

**Learn more:**

* [MindPal MCP Documentation](https://docs.mindpal.io/agent/mcp)

### MooPoint

[MooPoint](https://moopoint.io)

MooPoint is a web-based AI chat platform built for developers and advanced users, letting you interact with multiple large language models (LLMs) through a single, unified interface. Connect your own API keys (OpenAI, Anthropic, and more) and securely manage custom MCP server integrations.

**Key features:**

* Accessible from any PC or smartphone—no installation required
* Choose your preferred LLM provider
* Supports `SSE`, `Streamable HTTP`, `npx`, and `uvx` MCP servers
* OAuth and sampling support
* New features added daily

### Mistral AI: Le Chat

[Mistral AI: Le Chat](https://mistral.ai) is Mistral AI assistant with MCP support for remote servers and enterprise workflows.

**Key features:**

* Remote MCP server integration
* Enterprise-grade security
* Low-latency, high-throughput interactions with structured data

**Learn more:**

* [Mistral MCP Documentation](https://help.mistral.ai/en/collections/911943-connectors)

### Msty Studio

[Msty Studio](https://msty.ai) is a privacy-first AI productivity platform that seamlessly integrates local and online language models (LLMs) into customizable workflows. Designed for both technical and non-technical users, Msty Studio offers a suite of tools to enhance AI interactions, automate tasks, and maintain full control over data and model behavior.

**Key features:**

* **Toolbox & Toolsets**: Connect AI models to local tools and scripts using MCP-compliant configurations. Group tools into Toolsets to enable dynamic, multi-step workflows within conversations.
* **Turnstiles**: Create automated, multi-step AI interactions, allowing for complex data processing and decision-making flows.
* **Real-Time Data Integration**: Enhance AI responses with up-to-date information by integrating real-time web search capabilities.
* **Split Chats & Branching**: Engage in parallel conversations with multiple models simultaneously, enabling comparative analysis and diverse perspectives.

**Learn more:**

* [Msty Studio Documentation](https://docs.msty.studio/features/toolbox/tools)

### Needle

[Needle](https://needle.app) is a RAG workflow platform that also works as an MCP client, letting you connect and use MCP servers in seconds.

**Key features:**

* **Instant MCP integration:** Connect any remote MCP server to your collection in seconds
* **Built-in RAG:** Automatically get retrieval-augmented generation out of the box
* **Secure OAuth:** Safe, token-based authorization when connecting to servers
* **Smart previews:** See what each MCP server can do and selectively enable the tools you need

**Learn more:**

* [Getting Started](https://docs.needle.app/docs/guides/hello-needle/getting-started/)
* [Needle MCP Client](https://docs.needle.app/docs/guides/mcp/getting-started/)

### NVIDIA Agent Intelligence (AIQ) toolkit

[NVIDIA Agent Intelligence (AIQ) toolkit](https://github.com/NVIDIA/AIQToolkit) is a flexible, lightweight, and unifying library that allows you to easily connect existing enterprise agents to data sources and tools across any framework.

**Key features:**

* Acts as an MCP **client** to consume remote tools
* Acts as an MCP **server** to expose tools
* Framework agnostic and compatible with LangChain, CrewAI, Semantic Kernel, and custom agents
* Includes built-in observability and evaluation tools

**Learn more:**

* [AIQ toolkit GitHub repository](https://github.com/NVIDIA/AIQToolkit)
* [AIQ toolkit MCP documentation](https://docs.nvidia.com/aiqtoolkit/latest/workflows/mcp/index.html)

### OpenSumi

[OpenSumi](https://github.com/opensumi/core) is a framework helps you quickly build AI Native IDE products.

**Key features:**

* Supports MCP tools in OpenSumi
* Supports built-in IDE MCP servers and custom MCP servers

### oterm

[oterm] is a terminal client for Ollama allowing users to create chats/agents.

**Key features:**

* Support for multiple fully customizable chat sessions with Ollama connected with tools.
* Support for MCP tools.

### Roo Code

[Roo Code](https://roocode.com) enables AI coding assistance via MCP.

**Key features:**

* Support for MCP tools and resources
* Integration with development workflows
* Extensible AI capabilities

### Postman

[Postman](https://postman.com/downloads) is the most popular API client and now supports MCP server testing and debugging.

**Key features:**

* Full support of all major MCP features (tools, prompts, resources, and subscriptions)
* Fast, seamless UI for debugging MCP capabilities
* MCP config integration (Claude, VSCode, etc.) for fast first-time experience in testing MCPs
* Integration with history, variables, and collections for reuse and collaboration

### RecurseChat

[RecurseChat](https://recurse.chat) is a powerful, fast, local-first chat client with MCP support. RecurseChat supports multiple AI providers including LLaMA.cpp, Ollama, and OpenAI, Anthropic.

**Key features:**

* Local AI: Support MCP with Ollama models.
* MCP Tools: Individual MCP server management. Easily visualize the connection states of MCP servers.
* MCP Import: Import configuration from Claude Desktop app or JSON

**Learn more:**

* [RecurseChat docs](https://recurse.chat/docs/features/mcp/)

### Shortwave

[Shortwave](https://www.shortwave.com) is an AI-powered email client that supports MCP tools to enhance email productivity and workflow automation.

**Key features:**

* MCP tool integration for enhanced email workflows
* Rich UI for adding, managing and interacting with a wide range of MCP servers
* Support for both remote (Streamable HTTP and SSE) and local (Stdio) MCP servers
* AI assistance for managing your emails, calendar, tasks and other third-party services

### Simtheory

Simtheory is an agentic AI workspace that unifies multiple AI models, tools, and capabilities under a single subscription. It provides comprehensive MCP support through its MCP Store, allowing users to extend their workspace with productivity tools and integrations.

**Key features:**

* **MCP Store**: Marketplace for productivity tools and MCP server integrations
* **Parallel Tasking**: Run multiple AI tasks simultaneously with MCP tool support
* **Model Catalogue**: Access to frontier models with MCP tool integration
* **Hosted MCP Servers**: Plug-and-play MCP integrations with no technical setup
* **Advanced MCPs**: Specialized tools like Tripo3D (3D creation), Podcast Maker, and Video Maker
* **Enterprise Ready**: Flexible workspaces with granular access control for MCP tools

**Learn more:**

* [Simtheory website](https://simtheory.ai)

### Slack MCP Client

[Slack MCP Client](https://github.com/tuannvm/slack-mcp-client) acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

**Key features:**

* **Supports Popular LLM Providers:** Integrates seamlessly with leading large language model providers such as OpenAI, Anthropic, and Ollama, allowing users to leverage advanced conversational AI and orchestration capabilities within Slack.
* **Dynamic and Secure Integration:** Supports dynamic registration of MCP tools, works in both channels and direct messages and manages credentials securely via environment variables or Kubernetes secrets.
* **Easy Deployment and Extensibility:** Offers official Docker images, a Helm chart for Kubernetes, and Docker Compose for local development, making it simple to deploy, configure, and extend with additional MCP servers or tools.

### Smithery Playground

Smithery Playground is a developer-first MCP client for exploring, testing and debugging MCP servers against LLMs. It provides detailed traces of MCP RPCs to help troubleshoot implementation issues.

**Key features:**

* One-click connect to MCP servers via URL or from Smithery's registry
* Develop MCP servers that are running on localhost
* Inspect tools, prompts, resources, and sampling configurations with live previews
* Run conversational or raw tool calls to verify MCP behavior before shipping
* Full OAuth MCP-spec support

### SpinAI

[SpinAI](https://docs.spinai.dev) is an open-source TypeScript framework for building observable AI agents. The framework provides native MCP compatibility, allowing agents to seamlessly integrate with MCP servers and tools.

**Key features:**

* Built-in MCP compatibility for AI agents
* Open-source TypeScript framework
* Observable agent architecture
* Native support for MCP tools integration

### Superinterface

[Superinterface](https://superinterface.ai) is AI infrastructure and a developer platform to build in-app AI assistants with support for MCP, interactive components, client-side function calling and more.

**Key features:**

* Use tools from MCP servers in assistants embedded via React components or script tags
* SSE transport support
* Use any AI model from any AI provider (OpenAI, Anthropic, Ollama, others)

### Superjoin

[Superjoin](https://superjoin.ai) brings the power of MCP directly into Google Sheets extension. With Superjoin, users can access and invoke MCP tools and agents without leaving their spreadsheets, enabling powerful AI workflows and automation right where their data lives.

**Key features:**

* Native Google Sheets add-on providing effortless access to MCP capabilities
* Supports OAuth 2.1 and header-based authentication for secure and flexible connections
* Compatible with both SSE and Streamable HTTP transport for efficient, real-time streaming communication
* Fully web-based, cross-platform client requiring no additional software installation

### Swarms

[Swarms](https://github.com/kyegomez/swarms) is a production-grade multi-agent orchestration framework that supports MCP integration for dynamic tool discovery and execution.

**Key features:**

* Connects to MCP servers via SSE transport for real-time tool integration
* Automatic tool discovery and loading from MCP servers
* Support for distributed tool functionality across multiple agents
* Enterprise-ready with high availability and observability features
* Modular architecture supporting multiple AI model providers

**Learn more:**

* [Swarms MCP Integration Documentation](https://docs.swarms.world/en/latest/swarms/tools/tools_examples/)
* [GitHub Repository](https://github.com/kyegomez/swarms)

### systemprompt

[systemprompt](https://systemprompt.io) is a voice-controlled mobile app that manages your MCP servers. Securely leverage MCP agents from your pocket. Available on iOS and Android.

**Key features:**

* **Native Mobile Experience**: Access and manage your MCP servers anytime, anywhere on both Android and iOS devices
* **Advanced AI-Powered Voice Recognition**: Sophisticated voice recognition engine enhanced with cutting-edge AI and Natural Language Processing (NLP), specifically tuned to understand complex developer terminology and command structures
* **Unified Multi-MCP Server Management**: Effortlessly manage and interact with multiple Model Context Protocol (MCP) servers from a single, centralized mobile application

### Tambo

[Tambo](https://tambo.co) is a platform for building custom chat experiences in React, with integrated custom user interface components.

**Key features:**

* Hosted platform with React SDK for integrating chat or other LLM-based experiences into your own app.
* Support for selection of arbitrary React components in the chat experience, with state management and tool calling.
* Support for MCP servers, from Tambo's servers or directly from the browser.
* Supports OAuth 2.1 and custom header-based authentication.
* Support for MCP tools and sampling, with additional MCP features coming soon.

### Tencent CloudBase AI DevKit

[Tencent CloudBase AI DevKit](https://docs.cloudbase.net/ai/agent/mcp) is a tool for building AI agents in minutes, featuring zero-code tools, secure data integration, and extensible plugins via MCP.

**Key features:**

* Support for MCP tools
* Extend agents with MCP servers
* MCP servers hosting: serverless hosting and authentication support

### TheiaAI/TheiaIDE

[Theia AI](https://eclipsesource.com/blogs/2024/10/07/introducing-theia-ai/) is a framework for building AI-enhanced tools and IDEs. The [AI-powered Theia IDE](https://eclipsesource.com/blogs/2024/10/08/introducting-ai-theia-ide/) is an open and flexible development environment built on Theia AI.

**Key features:**

* **Tool Integration**: Theia AI enables AI agents, including those in the Theia IDE, to utilize MCP servers for seamless tool interaction.
* **Customizable Prompts**: The Theia IDE allows users to define and adapt prompts, dynamically integrating MCP servers for tailored workflows.
* **Custom agents**: The Theia IDE supports creating custom agents that leverage MCP capabilities, enabling users to design dedicated workflows on the fly.

Theia AI and Theia IDE's MCP integration provide users with flexibility, making them powerful platforms for exploring and adapting MCP.

**Learn more:**

* [Theia IDE and Theia AI MCP Announcement](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/)
* [Download the AI-powered Theia IDE](https://theia-ide.org/)

### Tome

[Tome](https://github.com/runebookai/tome) is an open source cross-platform desktop app designed for working with local LLMs and MCP servers. It is designed to be beginner friendly and abstract away the nitty gritty of configuration for people getting started with MCP.

**Key features:**

* MCP servers are managed by Tome so there is no need to install uv or npm or configure JSON
* Users can quickly add or remove MCP servers via UI
* Any tool-supported local model on Ollama is compatible

### TypingMind App

[TypingMind](https://www.typingmind.com) is an advanced frontend for LLMs with MCP support. TypingMind supports all popular LLM providers like OpenAI, Gemini, Claude, and users can use with their own API keys.

**Key features:**

* **MCP Tool Integration**: Once MCP is configured, MCP tools will show up as plugins that can be enabled/disabled easily via the main app interface.
* **Assign MCP Tools to Agents**: TypingMind allows users to create AI agents that have a set of MCP servers assigned.
* **Remote MCP servers**: Allows users to customize where to run the MCP servers via its MCP Connector configuration, allowing the use of MCP tools across multiple devices (laptop, mobile devices, etc.) or control MCP servers from a remote private server.

**Learn more:**

* [TypingMind MCP Document](https://www.typingmind.com/mcp)
* [Download TypingMind (PWA)](https://www.typingmind.com/)

### VS Code GitHub Copilot

[VS Code](https://code.visualstudio.com/) integrates MCP with GitHub Copilot through [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode), allowing direct interaction with MCP-provided tools within your agentic coding workflow. Configure servers in Claude Desktop, workspace or user settings, with guided MCP installation and secure handling of keys in input variables to avoid leaking hard-coded keys.

**Key features:**

* Support for stdio and server-sent events (SSE) transport
* Per-session selection of tools per agent session for optimal performance
* Easy server debugging with restart commands and output logging
* Tool calls with editable inputs and always-allow toggle
* Integration with existing VS Code extension system to register MCP servers from extensions

### VT Code

[VT Code](https://github.com/vinhnx/vtcode) is a terminal coding agent that integrates with Model Context Protocol (MCP) servers, focusing on predictable tool permissions and robust transport controls.

**Key features:**

* Connect to MCP servers over stdio; optional experimental RMCP/streamable HTTP support
* Configurable per-provider concurrency, startup/tool timeouts, and retries via `vtcode.toml`
* Pattern-based allowlists for tools, resources, and prompts with provider-level overrides

**Learn more:**

* [MCP Integration Guide](https://github.com/vinhnx/vtcode/blob/main/docs/guides/mcp-integration.md)

### Warp

[Warp](https://www.warp.dev/) is the intelligent terminal with AI and your dev team's knowledge built-in. With natural language capabilities integrated directly into an agentic command line, Warp enables developers to code, automate, and collaborate more efficiently -- all within a terminal that features a modern UX.

**Key features:**

* **Agent Mode with MCP support**: invoke tools and access data from MCP servers using natural language prompts
* **Flexible server management**: add and manage CLI or SSE-based MCP servers via Warp's built-in UI
* **Live tool/resource discovery**: view tools and resources from each running MCP server
* **Configurable startup**: set MCP servers to start automatically with Warp or launch them manually as needed

### WhatsMCP

[WhatsMCP](https://wassist.app/mcp/) is an MCP client for WhatsApp. WhatsMCP lets you interact with your AI stack from the comfort of a WhatsApp chat.

**Key features:**

* Supports MCP tools
* SSE transport, full OAuth2 support
* Chat flow management for WhatsApp messages
* One click setup for connecting to your MCP servers
* In chat management of MCP servers
* Oauth flow natively supported in WhatsApp

### Windsurf Editor

[Windsurf Editor](https://codeium.com/windsurf) is an agentic IDE that combines AI assistance with developer workflows. It features an innovative AI Flow system that enables both collaborative and independent AI interactions while maintaining developer control.

**Key features:**

* Revolutionary AI Flow paradigm for human-AI collaboration
* Intelligent code generation and understanding
* Rich development tools with multi-model support

### Witsy

[Witsy](https://github.com/nbonamy/witsy) is an AI desktop assistant, supporting Anthropic models and MCP servers as LLM tools.

**Key features:**

* Multiple MCP servers support
* Tool integration for executing commands and scripts
* Local server connections for enhanced privacy and security
* Easy-install from Smithery.ai
* Open-source, available for macOS, Windows and Linux

### Zed

[Zed](https://zed.dev/docs/assistant/model-context-protocol) is a high-performance code editor with built-in MCP support, focusing on prompt templates and tool integration.

**Key features:**

* Prompt templates surface as slash commands in the editor
* Tool integration for enhanced coding workflows
* Tight integration with editor features and workspace context
* Does not support MCP resources

### Zencoder

[Zencoder](https://zecoder.ai) is a coding agent that's available as an extension for VS Code and JetBrains family of IDEs, meeting developers where they already work. It comes with RepoGrokking (deep contextual codebase understanding), agentic pipeline, and the ability to create and share custom agents.

**Key features:**

* RepoGrokking - deep contextual understanding of codebases
* Agentic pipeline - runs, tests, and executes code before outputting it
* Zen Agents platform - ability to build and create custom agents and share with the team
* Integrated MCP tool library with one-click installations
* Specialized agents for Unit and E2E Testing

**Learn more:**

* [Zencoder Documentation](https://docs.zencoder.ai)


## Adding MCP support to your application

If you've added MCP support to your application, we encourage you to submit a pull request to add it to this list. MCP integration can provide your users with powerful contextual AI capabilities and make your application part of the growing MCP ecosystem.

Benefits of adding MCP support:

* Enable users to bring their own context and tools
* Join a growing ecosystem of interoperable AI applications
* Provide users with flexible integration options
* Support local-first AI workflows

To get started with implementing MCP in your application, check out our [Python](https://github.com/modelcontextprotocol/python-sdk) or [TypeScript SDK Documentation](https://github.com/modelcontextprotocol/typescript-sdk)


## Updates and corrections

This list is maintained by the community. If you notice any inaccuracies or would like to update information about MCP support in your application, please submit a pull request or [open an issue in our documentation repository](https://github.com/modelcontextprotocol/modelcontextprotocol/issues).



# Antitrust Policy
Source: https://modelcontextprotocol.io/community/antitrust

MCP Project Antitrust Policy for participants and contributors

**Effective: September 29, 2025**


## Introduction

The goal of the Model Context Protocol open source project (the "Project") is to develop a universal standard for model-to-world interactions, including enabling LLMs and agents to seamlessly connect with and utilize external data sources and tools. The purpose of this Antitrust Policy (the "Policy") is to avoid antitrust risks in carrying out this pro-competitive mission.

Participants in and contributors to the Project (collectively, "participants") will use their best reasonable efforts to comply in all respects with all applicable state and federal antitrust and trade regulation laws, and applicable antitrust/competition laws of other countries (collectively, the "Antitrust Laws").

The goal of Antitrust Laws is to encourage vigorous competition. Nothing in this Policy prohibits or limits the ability of participants to make, sell or use any product, or otherwise to compete in the marketplace. This Policy provides general guidance on compliance with Antitrust Law. Participants should contact their respective legal counsel to address specific questions.

This Policy is conservative and is intended to promote compliance with the Antitrust Laws, not to create duties or obligations beyond what the Antitrust Laws actually require. In the event of any inconsistency between this Policy and the Antitrust Laws, the Antitrust Laws preempt and control.


## Participation

Technical participation in the Project shall be open to all, subject only to compliance with the provisions of the Project's charter and other governance documents.


## Conduct of Meetings

At meetings among actual or potential competitors, there is a risk that participants in those meetings may improperly disclose or discuss information in violation of the Antitrust Laws or otherwise act in an anti-competitive manner. To avoid this risk, participants must adhere to the following policies when participating in Project-related or sponsored meetings, conference calls, or other forums (collectively, "Project Meetings").

Participants must not, in fact or appearance, discuss or exchange information regarding:

* An individual company's current or projected prices, price changes, price differentials, markups, discounts, allowances, terms and conditions of sale, including credit terms, etc., or data that bear on prices, including profits, margins or cost.
* Industry-wide pricing policies, price levels, price changes, differentials, or the like.
* Actual or projected changes in industry production, capacity or inventories.
* Matters relating to bids or intentions to bid for particular products, procedures for responding to bid invitations or specific contractual arrangements.
* Plans of individual companies concerning the design, characteristics, production, distribution, marketing or introduction dates of particular products, including proposed territories or customers.
* Matters relating to actual or potential individual suppliers that might have the effect of excluding them from any market or of influencing the business conduct of firms toward such suppliers.
* Matters relating to actual or potential customers that might have the effect of influencing the business conduct of firms toward such customers.
* Individual company current or projected cost of procurement, development or manufacture of any product.
* Individual company market shares for any product or for all products.
* Confidential or otherwise sensitive business plans or strategy.

In connection with all Project Meetings, participants must do the following:

* Adhere to prepared agendas.
* Insist that meeting minutes be prepared and distributed to all participants, and that meeting minutes accurately reflect the matters that transpired.
* Consult with their respective counsel on all antitrust questions related to Project Meetings.
* Protest against any discussions that appear to violate these policies or the Antitrust Laws, leave any meeting in which such discussions continue, and either insist that such protest be noted in the minutes.


## Requirements/Standard Setting

The Project may establish standards, technical requirements and/or specifications for use (collectively, "requirements"). Participants shall not enter into agreements that prohibit or restrict any participant from establishing or adopting any other requirements. Participants shall not undertake any efforts, directly or indirectly, to prevent any firm from manufacturing, selling, or supplying any product not conforming to a requirement.

The Project shall not promote standardization of commercial terms, such as terms for license and sale.


## Contact Information

To contact the Project regarding matters addressed by this Antitrust Policy, please send an email to [antitrust@modelcontextprotocol.io](mailto:antitrust@modelcontextprotocol.io), and reference "Antitrust Policy" in the subject line.



# Contributor Communication
Source: https://modelcontextprotocol.io/community/communication

Communication strategy and framework for the Model Context Protocol community

This document explains how to communicate and collaborate within the Model Context Protocol (MCP) project.


## Communication Channels

In short:

* **[Discord][discord-join]**: For real-time or ad-hoc discussions.
* **[GitHub Discussions](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions)**: For structured, longer-form discussions.
* **[GitHub Issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues)**: For actionable tasks, bug reports, and feature requests.
* **For security-sensitive issues**: Follow the process in [SECURITY.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md).

All communication is governed by our [Code of Conduct](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CODE_OF_CONDUCT.md). We expect all participants to maintain respectful, professional, and inclusive interactions across all channels.

### Discord

For real-time contributor discussion and collaboration. The server is designed around **MCP contributors** and is not intended
to be a place for general MCP support.

The Discord server will have both public and private channels.

[Join the Discord server here][discord-join].

#### Public Channels (Default)

* **Purpose**: Open community engagement, collaborative development, and transparent project coordination.
* Primary use cases:
  * **Public SDK and tooling development**: All development, from ideation to release planning, happens in public channels (e.g., `#typescript-sdk-dev`, `#inspector-dev`).
  * **[Working and Interest Group](/community/working-interest-groups) discussions**
  * **Community onboarding** and contribution guidance.
  * **Community feedback** and collaborative brainstorming.
  * Public **office hours** and **maintainer availability**.
* Avoid:
  * MCP user support: participants are expected to read official documentation and start new GitHub Discussions for questions or support.
  * Service or product marketing: interactions on this Discord are expected to be vendor-neutral and not used for brand-building or sales. Mentions of brands or products are discouraged outside of being used as examples or responses to conversations that start off focused on the specification.

#### Private channels (Exceptions)

* **Purpose**: Confidential coordination and sensitive matters that cannot be discussed publicly. Access will be restricted to designated maintainers.
* **Strict criteria for private use**:
  * **Security incidents** (CVEs, protocol vulnerabilities).
  * **People matters** (maintainer-related discussions, code of conduct policies).
  * Select channels will be configured to be **read-only**. This can be good for example for maintainer decision making.
  * Coordination requiring **immediate** or otherwise **focused response** with a limited audience.
* **Transparency**:
  * **All technical and governance decisions** affecting the community **must be documented** in GitHub Discussions and/or Issues, and will be labeled with `notes`.
  * **Some matters related to individual contributors** may remain private when appropriate (e.g., personal circumstances, disciplinary actions, or other sensitive individual matters).
  * Private channels are to be used as **temporary "incident rooms,"** not for routine development.

Any significant discussion on Discord that leads to a potential decision or proposal must be moved to a GitHub Discussion or GitHub Issue to create a persistent, searchable record. Proposals will then be promoted to full-fledged PRs with associated work items (GitHub Issues) as needed.

### GitHub Discussions

For structured, long-form discussion and debate on project direction, features, improvements, and community topics.

When to use:

* Project roadmap planning and milestone discussions
* Announcements and release communications
* Community polls and consensus-building processes
* Feature requests with context and rationale
  * If a particular repository does not have GitHub Discussions enabled, feel free to open a GitHub Issue instead.

### GitHub Issues

For bug reports, feature tracking, and actionable development tasks.

When to use:

* Submit SEP proposals (following the [SEP guidelines](./sep-guidelines))
* Bug reports with reproducible steps
* Documentation improvements with specific scope
* CI/CD problems and infrastructure issues
* Release tasks and milestone tracking

### Security Issues

**Do not post security issues publicly.** Instead:

1. Use the private security reporting process. For protocol-level security issues, follow the process in [SECURITY.md in the modelcontextprotocol GitHub repository](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md).
2. Contact lead and/or [core maintainers](./governance#current-core-maintainers) directly.
3. Follow responsible disclosure guidelines.


## Decision Records

All MCP decisions are documented and captured in public channels.

* **Technical decisions**: [GitHub Issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues) and SEPs.
* **Specification changes**: [On the Model Context Protocol website](https://modelcontextprotocol.io/specification/draft/changelog).
* **Process changes**: [Community documentation](https://modelcontextprotocol.io/community/governance).
* **Governance decisions and updates**: [GitHub Issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues) and SEPs.

When documenting decisions, we will retain as much context as possible:

* Decision makers
* Background context and motivation
* Options that were considered
* Rationale for the chosen approach
* Implementation steps

[discord-join]: https://discord.gg/6CSzBmMkjX



# Governance and Stewardship
Source: https://modelcontextprotocol.io/community/governance

Learn about the Model Context Protocol's governance structure and how to participate in the community

The Model Context Protocol (MCP) follows a formal governance model to ensure transparent decision-making and community participation. This document outlines how the project is organized and how decisions are made.


## Technical Governance

The MCP project adopts a hierarchical structure, similar to Python, PyTorch and other open source projects:

* A community of **contributors** who file issues, make pull requests, and contribute to the project.
* A small set of **maintainers** drive components within the MCP project, such as SDKs, documentation, and others.
* Contributors and maintainers are overseen by **core maintainers**, who drive the overall project direction.
* The core maintainers have two **lead core maintainers** who are the catch-all decision makers.
* Maintainers, core maintainers, and lead core maintainers form the **MCP steering group**.

All maintainers are expected to have a strong bias towards MCP's design philosophy. Membership in the technical governance process is for individuals, not companies. That is, there are no seats reserved for specific companies, and membership is associated with the person rather than the company employing that person. This ensures that maintainers act in the best interests of the protocol itself and the open source community.

### Channels

Technical Governance is facilitated through a shared [Discord server](/community/communication#discord) of all **maintainers, core maintainers** and **lead maintainers**. Each maintainer group can choose additional communication channels, but all decisions and their supporting discussions must be recorded and made transparently available on the Discord server.

### Maintainers

Maintainers are responsible for [Working or Interest Groups](/community/working-interest-groups) within the MCP project. These generally are independent repositories such as language-specific SDKs, but can also extend to subdirectories of a repository, such as the MCP documentation. Maintainers may adopt their own rules and procedures for making decisions. Maintainers are expected to make decisions for their respective projects independently, but can defer or escalate to the core maintainers when needed.

Maintainers are responsible for the:

* Thoughtful and productive engagement with community contributors,
* Maintaining and improving their respective area of the MCP project,
* Supporting documentation, roadmaps and other adjacent parts of the MCP project,
* Present ideas from community to core.

Maintainers are encouraged to propose additional maintainers when needed. Maintainers can only be appointed and removed by core maintainers or lead core maintainers at any time and without reason.

Maintainers have write and/or admin access to their respective repositories.

### Core Maintainers

The core maintainers are expected to have a deep understanding of the Model Context Protocol and its specification. Their responsibilities include:

* Designing, reviewing and steering the evolution of the MCP specification, as well as all other parts of the MCP project, such as documentation,
* Articulating a cohesive long-term vision for the project,
* Mediating and resolving contentious issues with fairness and transparency, seeking consensus where possible while making decisive choices when necessary,
* Appoint or remove maintainers,
* Stewardship of the MCP project in the best interest of MCP.

The core maintainers as a group have the power to veto any decisions made by maintainers by majority vote. The core maintainers have power to resolve disputes as they see fit. The core maintainers should publicly articulate their decision-making. The core group is responsible for adopting their own procedures for making decisions.

Core maintainers generally have write and admin access to all MCP repositories, but should use the same contribution (usually pull-requests) mechanism as outside contributors. Exceptions can be made based on security considerations.

### Lead Maintainers (BDFL)

MCP has two lead maintainers: Justin Spahr-Summers and David Soria Parra. Lead Maintainers can veto any decision by core maintainers or maintainers. This model is also commonly known as Benevolent Dictator for Life (BDFL) in the open source community. The Lead Maintainers should publicly articulate their decision-making and give clear reasoning for their decisions. Lead maintainers are part of the core maintainer group.

The Lead Maintainers are responsible for confirming or removing core maintainers.

Lead Maintainers are administrators on all infrastructure for the MCP project where possible. This includes but is not restricted to all communication channels, GitHub organizations and repositories.

### Decision Process

The core maintainer group meets every two weeks to discuss and vote on proposals, as well as discuss any topics needed. The shared Discord server can be used to discuss and vote on smaller proposals if needed.

The lead maintainer, core maintainer, and maintainer group should attempt to meet in person every three to six months.


## Processes

Core and lead maintainers are responsible for all aspects of Model Context Protocol, including documentation, issues, suggestions for content, and all other parts under the [MCP project](https://github.com/modelcontextprotocol). Maintainers are responsible for documentation, issues, and suggestions of content for their area of the MCP project, but are encouraged to partake in general maintenance of the MCP projects. Maintainers, core maintainers, and lead maintainers should use the same contribution process as external contributors, rather than making direct changes to repos. This provides insight into intent and opportunity for discussion.

### Working and Interest Groups

MCP collaboration and contributions are organized around two structures: [Working Groups and Interest Groups](/community/working-interest-groups).

Interest Groups are responsible for identifying and articulating problems that MCP should address, primarily by facilitating open discussions within the community. In contrast, Working Groups focus on developing concrete solutions by collaboratively producing deliverables, such as SEPs or community-owned implementations of the specification. While input from Interest Groups can help justify the formation of a Working Group, it is not a strict requirement. Similarly, contributions from either Interest Groups or Working Groups are encouraged, but not mandatory, when submitting SEPs or other community proposals.

We strongly encourage all contributors interested in working on a specific SEP to first collaborate within an Interest Group. This collaborative process helps ensure that the proposed SEP aligns with protocol needs and is the right direction for its adopters.

#### Governance Principles

All groups are self-governed while adhering to these core principles:

1. Clear contribution and decision-making processes
2. Open communication and transparent decisions

Both must:

* Document their contribution process
* Maintain transparent communication
* Make decisions publicly (groups must publish meeting notes and proposals)

Projects and working groups without specified processes default to:

* GitHub pull requests and issues for contributions
* A public channel in the official [MCP Contributor Discord](/community/communication#discord)

#### Maintenance Responsibilities

Components without dedicated maintainers (such as documentation) fall under core maintainer responsibility. These follow standard contribution guidelines through pull requests, with maintainers handling reviews and escalating to core maintainer review for any significant changes.

Core maintainers and maintainers are encouraged to improve any part of the MCP project, regardless of formal maintenance assignments.

### Specification Project

#### Specification Enhancement Proposal (SEP)

Proposed changes to the specification must come in the form of a written version, starting with a summary of the proposal, outlining the **problem** it tries to solve, propose **solution**, **alternatives**, **considerations, outcomes** and **risks**. The [SEP Guidelines](/community/sep-guidelines) outline information on the expected structure of SEPs. SEP's should be created as issues in the [specification repository](https://github.com/modelcontextprotocol/specification) and tagged with the labels `proposal, sep`.

All proposals must have a **sponsor** from the MCP steering group (maintainer, core maintainer or lead core maintainer). The sponsor is responsible for ensuring that the proposal is actively developed, meets the quality standard for proposals and is responsible for presenting and discussing it in meetings of core maintainers. Maintainer and Core Maintainer groups should review open proposals without sponsors in regular intervals. Proposals that do not find a sponsor within six months are automatically rejected.

Once proposals have a sponsor, they are assigned to the sponsor and are tagged `draft`.


## Communication

### Core Maintainer Meetings

The core maintainer group meets on a bi-weekly basis to discuss proposals and the project. Notes on proposals should be made public. The core maintainer group will strive to meet in person every 3-6 months.

### Public Chat

The MCP project maintains a [public Discord server](/community/communication#discord) with open chats for interest groups. The MCP project may have private channels for certain communications.


## Nominating, Confirming and Removing Maintainers

### The Principles

* Membership in module maintainer groups is given to **individuals** on merit basis after they demonstrated strong expertise of their area of work through contributions, reviews, and discussions and are aligned with the overall MCP direction.
* For membership in the **maintainer** group the individual has to demonstrate strong and continued alignment with the overall MCP principles.
* No term limits for module maintainers or core maintainers
* Light criteria of moving working-group or sub-project maintenance to 'emeritus' status if they don't actively participate over long periods of time. Each maintainer group may define the inactive period that's appropriate for their area.
* The membership is for an individual, not a company.

### Nomination and Removal

* Core Maintainers are responsible for adding and removing maintainers. They will take the consideration of existing maintainers into account.
* The lead maintainers are responsible for adding and removing core maintainers.

#### Nomination Process

If a Maintainer (or Core / Lead Maintainer) wishes to propose a nomination for the Core / Lead Maintainers’ consideration, they should follow the following process:

1. Collect evidence for the nomination. This will generally come in the form of a history of merged PRs on the repositories for which maintainership is being considered.
2. Discuss among maintainers of the relevant group(s) as to whether they would be supportive of approving the nomination.
3. DM a Community Moderator or Core Maintainer to create a private channel in Discord, in the format `nomination-{name}-{group}`. Add all core maintainers, lead maintainers, and co-maintainers on the relevant group.
4. Provide context for the individual under nomination. See below for suggestions on what to include here.
5. Create a Discord Poll and ask Core / Lead Maintainers to vote Yes / No on the nomination. Reaching consensus is encouraged though not required.
6. After Core / Lead Maintainers discuss and/or vote, if the nomination is favorable, relevant members with permissions to update GitHub an Discord roles will add the nominee to the appropriate groups. The nominator should announce the new maintainership in the relevant Discord channel.
7. The temporary Discord channel will be deleted a week later.

Suggestions for the kind of information to share with core maintainers when nominating someone:

* GitHub profile link, LinkedIn profile link, Discord username
* For what group(s) are you nominating the individual for maintainership
* Whether the group(s) agree that this person should be elevated to maintainership
* Description of their contributions to date (including links to most substantial contributions)
* Description of expected contributions moving forward (e.g. Are they eager to be a maintainer? Will they have capacity to do so?)
* Other context about the individual (e.g. current employer, motivations behind MCP involvement)
* Anything else you think may be relevant to consider for the nomination


## Current Core Maintainers

* Inna Harper
* Basil Hosmer
* Paul Carleton
* Nick Cooper
* Nick Aldridge
* Che Liu
* Den Delimarsky


## Current Maintainers and Working Groups

Refer to [the maintainer list](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md).



# SEP Guidelines
Source: https://modelcontextprotocol.io/community/sep-guidelines

Specification Enhancement Proposal (SEP) guidelines for proposing changes to the Model Context Protocol


## What is a SEP?

SEP stands for Specification Enhancement Proposal. A SEP is a design document providing information to the MCP community, or describing a new feature for the Model Context Protocol or its processes or environment. The SEP should provide a concise technical specification of the feature and a rationale for the feature.

We intend SEPs to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into MCP. The SEP author is responsible for building consensus within the community and documenting dissenting opinions.

Because the SEPs are maintained as text files in a versioned repository (GitHub Issues), their revision history is the historical record of the feature proposal.


## What qualifies a SEP?

The goal is to reserve the SEP process for changes that are substantial enough to require broad community discussion, a formal design document, and a historical record of the decision-making process. A regular GitHub issue or pull request is often more appropriate for smaller, more direct changes.

Consider proposing a SEP if your change involves any of the following:

* **A New Feature or Protocol Change**: Any change that adds, modifies, or removes features in the Model Context Protocol. This includes:
  * Adding new API endpoints or methods.
  * Changing the syntax or semantics of existing data structures or messages.
  * Introducing a new standard for interoperability between different MCP-compatible tools.
  * Significant changes to how the specification itself is defined, presented, or validated.
* **A Breaking Change**: Any change that is not backwards-compatible.
* **A Change to Governance or Process**: Any proposal that alters the project's decision-making, contribution guidelines (like this document itself).
* **A Complex or Controversial Topic**: If a change is likely to have multiple valid solutions or generate significant debate, the SEP process provides the necessary framework to explore alternatives, document the rationale, and build community consensus before implementation begins.


## SEP Types

There are three kinds of SEP:

1. **Standards Track** SEP describes a new feature or implementation for the Model Context Protocol. It may also describe an interoperability standard that will be supported outside the core protocol specification.
2. **Informational** SEP describes a Model Context Protocol design issue, or provides general guidelines or information to the MCP community, but does not propose a new feature. Informational SEPs do not necessarily represent an MCP community consensus or recommendation.
3. **Process** SEP describes a process surrounding MCP, or proposes a change to (or an event in) a process. Process SEPs are like Standards Track SEPs but apply to areas other than the MCP protocol itself.


## Submitting a SEP

The SEP process begins with a new idea for the Model Context Protocol. It is highly recommended that a single SEP contain a single key proposal or new idea. Small enhancements or patches often don't need a SEP and can be injected into the MCP development workflow with a pull request to the MCP repo. The more focused the SEP, the more successful it tends to be.

Each SEP must have an **SEP author** -- someone who writes the SEP using the style and format described below, shepherds the discussions in the appropriate forums, and attempts to build community consensus around the idea. The SEP author should first attempt to ascertain whether the idea is SEP-able. Posting to the MCP community forums (Discord, GitHub Discussions) is the best way to go about this.

### SEP Workflow

SEPs should be submitted as a GitHub Issue in the [specification repository](https://github.com/modelcontextprotocol/modelcontextprotocol). The standard SEP workflow is:

1. You, the SEP author, create a [well-formatted](#sep-format) GitHub Issue with the `SEP` and `proposal` tags. The SEP number is the same as the GitHub Issue number, the two can be used interchangeably.
2. Find a Core Maintainer or Maintainer to sponsor your proposal. Core Maintainers and Maintainers will regularly go over the list of open proposals to determine which proposals to sponsor. You can tag relevant maintainers from [the maintainer list](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md) in your proposal.
3. Once a sponsor is found, the GitHub Issue is assigned to the sponsor. The sponsor will add the `draft` tag, ensure the SEP number is in the title, and assign a milestone.
4. The sponsor will informally review the proposal and may request changes based on community feedback. When ready for formal review, the sponsor will add the `in-review` tag.
5. After the `in-review` tag is added, the SEP enters formal review by the Core Maintainers team. The SEP may be accepted, rejected, or returned for revision.
6. If the SEP has not found a sponsor within three months, Core Maintainers may close the SEP as `dormant`.

### SEP Format

Each SEP should have the following parts:

1. **Preamble** -- A short descriptive title, the names and contact info for each author, the current status.
2. **Abstract** -- A short (\~200 word) description of the technical issue being addressed.
3. **Motivation** -- The motivation should clearly explain why the existing protocol specification is inadequate to address the problem that the SEP solves. The motivation is critical for SEPs that want to change the Model Context Protocol. SEP submissions without sufficient motivation may be rejected outright.
4. **Specification** -- The technical specification should describe the syntax and semantics of any new protocol feature. The specification should be detailed enough to allow competing, interoperable implementations. A PR with the changes to the specification should be provided.
5. **Rationale** -- The rationale explains why particular design decisions were made. It should describe alternate designs that were considered and related work. The rationale should provide evidence of consensus within the community and discuss important objections or concerns raised during discussion.
6. **Backward Compatibility** -- All SEPs that introduce backward incompatibilities must include a section describing these incompatibilities and their severity. The SEP must explain how the author proposes to deal with these incompatibilities.
7. **Reference Implementation** -- The reference implementation must be completed before any SEP is given status "Final", but it need not be completed before the SEP is accepted. While there is merit to the approach of reaching consensus on the specification and rationale before writing code, the principle of "rough consensus and running code" is still useful when it comes to resolving many discussions of protocol details.
8. **Security Implications** -- If there are security concerns in relation to the SEP, those concerns should be explicitly written out to make sure reviewers of the SEP are aware of them.

### SEP States

SEPs can be one one of the following states

* `proposal`: SEP proposal without a sponsor.
* `draft`: SEP proposal with a sponsor.
* `in-review`: SEP proposal ready for review.
* `accepted`: SEP accepted by Core Maintainers, but still requires final wording and reference implementation.
* `rejected`: SEP rejected by Core Maintainers.
* `withdrawn`: SEP withdrawn.
* `final`: SEP finalized.
* `superseded`: SEP has been replaced by a newer SEP.
* `dormant`: SEP that has not found sponsors and was subsequently closed.

### SEP Review & Resolution

SEPs are reviewed by the MCP Core Maintainers team on a bi-weekly basis.

For a SEP to be accepted it must meet certain minimum criteria:

* A prototype implementation demonstrating the proposal
* Clear benefit to the MCP ecosystem
* Community support and consensus

Once a SEP has been accepted, the reference implementation must be completed. When the reference implementation is complete and incorporated into the main source code repository, the status will be changed to "Final".

A SEP can also be "Rejected" or "Withdrawn". A SEP that is "Withdrawn" may be re-submitted at a later date.


## Reporting SEP Bugs, or Submitting SEP Updates

How you report a bug, or submit a SEP update depends on several factors, such as the maturity of the SEP, the preferences of the SEP author, and the nature of your comments. For SEPs not yet reaching `final` state, it's probably best to send your comments and changes directly to the SEP author. Once SEP is finalized, you may want to submit corrections as a GitHub comment on the issue or pull request to the reference implementation.


## Transferring SEP Ownership

It occasionally becomes necessary to transfer ownership of SEPs to a new SEP author. In general, we'd like to retain the original author as a co-author of the transferred SEP, but that's really up to the original author. A good reason to transfer ownership is because the original author no longer has the time or interest in updating it or following through with the SEP process, or has fallen off the face of the 'net (i.e. is unreachable or not responding to email). A bad reason to transfer ownership is because you don't agree with the direction of the SEP. We try to build consensus around a SEP, but if that's not possible, you can always submit a competing SEP.


## Copyright

This document is placed in the public domain or under the CC0-1.0-Universal license, whichever is more permissive.



# Working and Interest Groups
Source: https://modelcontextprotocol.io/community/working-interest-groups

Learn about the two forms of collaborative groups within the Model Context Protocol's governance structure - Working Groups and Interest Groups.

Within the MCP contributor community we maintain two types of collaboration formats - **Interest** and **Working** groups.

**Interest Groups** are responsible for identifying and articulating problems that MCP should address, primarily by facilitating open discussions within the community. In contrast, **Working Groups** focus on developing concrete solutions by collaboratively producing deliverables, such as SEPs or community-owned implementations of the specification.

While input from Interest Groups can help justify the formation of a Working Group, it is not a strict requirement. Similarly, contributions from either Interest Groups or Working Groups are encouraged, but not mandatory, when submitting SEPs or other community proposals.

We strongly encourage all contributors interested in working on a specific SEP to first collaborate within an Interest Group. This collaborative process helps ensure that the proposed SEP aligns with community needs and is the right direction for the protocol.

Long-term projects in the MCP ecosystem, such as SDKs, Inspector, or Registry are maintained by dedicated Working Groups.


## Purpose

These groups exist to:

* **Facilitate high-signal spaces for focused discussions** - contributors who opt into notifications, expertise sharing, and regular meetings can engage with topics that are highly relevant to them, enabling meaningful contributions and opportunities to learn from others.
* **Establish clear expectations and leadership roles** - guide collaborative efforts and ensure steady progress toward concrete deliverables that advance MCP evolution and adoption.


## Mechanisms


## Meeting Calendar

All Interest Group and Working Group meetings are published on the public MCP community calendar at [meet.modelcontextprotocol.io](https://meet.modelcontextprotocol.io/).

Facilitators are responsible for posting their meeting schedules to this calendar in advance to ensure discoverability and enable broader community participation.

### Interest Groups (IGs)

**Goal:** Facilitate discussion and knowledge-sharing among MCP contributors who share interests in a specific MCP sub-topic or context. The primary focus is on identifying and gathering problems that may be worth addressing through SEPs or other community artifacts, while encouraging open exploration of protocol issues and opportunities.

**Expectations**:

* Regular conversations in the Interest Group Discord channel
* **AND/OR** a recurring live meeting regularly attended by Interest Group members
* Meeting dates and times published in advance on the [MCP community calendar](https://meet.modelcontextprotocol.io/) when applicable, and tagged with their primary topic and interest group Discord channel name (e.g. `auth-ig`)
* Notes publicly shared after meetings, as a GitHub issue ([example](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1629)) and/or public Google Doc

**Examples**:

* Security in MCP
* Auth in MCP
* Using MCP in enterprise settings
* Tooling and practices surrounding hosting MCP servers
* Tooling and practices surrounding implementing MCP clients

**Lifecycle**:

* Creation begins by filling out a template in the #wg-ig-group-creation [Discord](/community/communication#discord) channel
* A community moderator will review and call for a vote in the (private) #community-moderators Discord channel. Majority positive vote by members over a 72h period approves creation of the group.
  * The creation of the group can be reversed at any time (e.g., after new information surfaces). Core and lead maintainers can veto.
* Facilitator(s) and Maintainer(s) responsible for organizing IG into meeting expectations
  * Facilitator is an informal role responsible for shepherding or speaking for a group
  * Maintainer is an official representative from the MCP steering group. A maintainer is not required for every group, but can help advocate for specific changes or initiatives.
* IG is retired only when community moderators or Core or Lead Maintainers determine it's no longer active and/or needed
  * Successful IGs do not have a time limit or expiration date - as long as they are active and maintained, they will remain available

**Creation Template**:

* Facilitator(s)
* Maintainer(s) (optional)
* IGs with potentially similar goals/discussions
* How this IG differentiates itself from the related IGs
* First topic you to discuss within the IG

Participation in an Interest Group (IG) is not required to start a Working Group (WG) or to create a SEP. However, building consensus within IGs can be valuable when justifying the formation of a WG. Likewise, referencing support from IGs or WGs can strengthen a SEP and its chances of success.

### Working Groups (WG)

**Goal:** Facilitate collaboration within the MCP community on a SEP, a themed series of SEPs, or an otherwise officially endorsed project.

**Expectations**:

* Meaningful progress towards at least one SEP or spec-related implementation **OR** hold maintenance responsibilities for a project (e.g., Inspector, Registry, SDKs)
* Facilitators are responsible for keeping track of progress and communicating status when appropriate
* Meeting dates and times published in advance on the [MCP community calendar](https://meet.modelcontextprotocol.io/) when applicable, and tagged with their primary topic and working group Discord channel name (e.g. `agents-wg`)
* Notes publicly shared after meetings, as a GitHub issue ([example](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1629)) and/or public Google Doc

**Examples**:

* Registry
* Inspector
* Tool Filtering
* Server Identity

**Lifecycle**:

* Creation begins by filling out a template in #wg-ig-group-creation Discord channel
* A community moderator will review and call for a vote in the (private) #community-moderators Discord channel. Majority positive vote by members over a 72h period approves creation of the group.
  * The creation of the group can be reversed at any time (e.g., after new information surfaces). Core and lead maintainers can veto.
* Facilitator(s) and Maintainer(s) responsible for organizing WG into meeting expectations
  * Facilitator is an informal role responsible for shepherding or speaking for a group
  * Maintainer is an official representative from the MCP steering group. A maintainer is not required for every group, but can help advocate for specific changes or initiatives
* WG is retired when either:
  * Community moderators or Core and Lead Maintainers decide it is no longer active and/or needed
  * The WG no longer has an active Issue/PR for a month or more, or has completed all Issues/PRs it intended to pursue.

**Creation Template**:

* Facilitator(s)
* Maintainer(s) (optional)
* Explanation of interest/use cases, ideally originating from an IG discussion; however that is not a requirement
* First Issue/PR/SEP that the WG will work on


## WG/IG Facilitators

A **Facilitator** role in a WG or IG does *not* result in a [maintainership role](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md) across the MCP organization. It is an informal role into which anyone can self-nominate.

A Facilitator is responsible for helping shepherd discussions and collaboration within an Interest or Working Group.

Lead and Core Maintainers reserve the right to modify the list of Facilitators and Maintainers for any WG/IG at any time.


## FAQ

### How do I get involved contributing to MCP?

These IG and WG abstractions help provide an elegant on-ramp:

1. [Join the Discord](/community/communication#discord) and follow conversations in IGs relevant to you. Attend [live calls](https://meet.modelcontextprotocol.io/). Participate.
2. Offer to facilitate calls. Contribute your use cases in SEP proposals and other work.
3. When you're comfortable contributing to deliverables, jump in to contribute to WG work.
4. Active and valuable contributors will be nominated by WG maintainers as new maintainers.

### Where can I find a list of all current WGs and IGs?

On the [MCP Contributor Discord](/community/communication#discord) there is a section of channels for each Working and Interest Group.



# Roadmap
Source: https://modelcontextprotocol.io/development/roadmap

Our plans for evolving Model Context Protocol

<Info>Last updated: **2025-10-31**</Info>

The Model Context Protocol is rapidly evolving. This page outlines our priorities for **the next release on November 25th, 2025**, with a release candidate available on November 11th, 2025. To see what's changing in the upcoming release, check out the **[specification changelog](/specification/draft/changelog/)**.

For more context on our release timeline and governance process, read our [blog post on the next version update](https://blog.modelcontextprotocol.io/posts/2025-09-26-mcp-next-version-update/).

<Note>
  The ideas presented here are not commitments—we may solve these challenges differently than described, or some may not materialize at all. This is also not an *exhaustive* list; we may incorporate work that isn't mentioned here.
</Note>

We value community participation! Each section links to relevant discussions where you can learn more and contribute your thoughts.

For a technical view of our standardization process, visit the [Standards Track](https://github.com/orgs/modelcontextprotocol/projects/2/views/2) on GitHub, which tracks how proposals progress toward inclusion in the official [MCP specification](https://spec.modelcontextprotocol.io).


## Priority Areas for the Next Release

### Asynchronous Operations

Currently, MCP is built around mostly synchronous operations. We're adding async support to allow servers to kick off long-running tasks while clients can check back later for results. This will enable operations that take minutes or hours without blocking.

Follow the progress in [SEP-1686](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1686).

### Statelessness and Scalability

As organizations deploy MCP servers at enterprise scale, we're addressing challenges around horizontal scaling. While [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) provides some stateless support, we're smoothing out rough edges around server startup and session handling to make it easier to run MCP servers in production.

The current focus point for this effort is [SEP-1442](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442).

### Server Identity

We're enabling servers to advertise themselves through [`.well-known` URLs](https://en.wikipedia.org/wiki/Well-known_URI)—an established standard for providing metadata. This will allow clients to discover what a server can do without having to connect to it first, making discovery much more intuitive and enabling systems like our registry to automatically catalog capabilities. We are working closely across multiple projects in the industry to rely on a common standard on agent cards.

### Official Extensions

As MCP has grown, valuable patterns have emerged for specific industries and use cases. Rather than leaving everyone to reinvent the wheel, we're officially recognizing and documenting the most popular protocol extensions. This curated collection will give developers building for specialized domains like healthcare, finance, or education a solid starting point.

### SDK Support Standardization

We're introducing a clear tiering system for SDKs based on factors like specification compliance speed, maintenance responsiveness, and feature completeness. This will help developers understand exactly what level of support they're getting before committing to a dependency.

### MCP Registry General Availability

The [MCP Registry](https://github.com/modelcontextprotocol/registry) launched in preview in September 2025 and is progressing toward general availability. We're stabilizing the v0.1 API through real-world integrations and community feedback, with plans to transition from preview to a production-ready service. This will provide developers with a reliable, community-driven platform for discovering and sharing MCP servers.


## Validation

To foster a robust developer ecosystem, we plan to invest in:

* **Reference Client Implementations**: demonstrating protocol features with high-quality AI applications
* **Reference Server Implementation**: showcasing authentication patterns and remote deployment best practices
* **Compliance Test Suites**: automated verification that clients, servers, and SDKs properly implement the specification

These tools will help developers confidently implement MCP while ensuring consistent behavior across the ecosystem.


## Get Involved

We welcome your contributions to MCP's future! Join our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to share ideas, provide feedback, or participate in the development process.



# Build an MCP client
Source: https://modelcontextprotocol.io/docs/develop/build-client

Get started building your own client that can integrate with all MCP servers.

In this tutorial, you'll learn how to build an LLM-powered chatbot client that connects to MCP servers.

Before you begin, it helps to have gone through our [Build an MCP Server](/docs/develop/build-server) tutorial so you can understand how clients and servers communicate.

<Tabs>
  <Tab title="Python">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-python)

    ## System Requirements

    Before starting, ensure your system meets these requirements:

    * Mac or Windows computer
    * Latest Python version installed
    * Latest version of `uv` installed

    ## Setting Up Your Environment

    First, create a new Python project with `uv`:

    <CodeGroup>
      ```bash macOS/Linux theme={null}
      # Create project directory
      uv init mcp-client
      cd mcp-client

      # Create virtual environment
      uv venv

      # Activate virtual environment
      source .venv/bin/activate

      # Install required packages
      uv add mcp anthropic python-dotenv

      # Remove boilerplate files
      rm main.py

      # Create our main file
      touch client.py
      ```

      ```powershell Windows theme={null}
      # Create project directory
      uv init mcp-client
      cd mcp-client

      # Create virtual environment
      uv venv

      # Activate virtual environment
      .venv\Scripts\activate

      # Install required packages
      uv add mcp anthropic python-dotenv

      # Remove boilerplate files
      del main.py

      # Create our main file
      new-item client.py
      ```
    </CodeGroup>

    ## Setting Up Your API Key

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).

    Create a `.env` file to store it:

    ```bash  theme={null}
    echo "ANTHROPIC_API_KEY=your-api-key-goes-here" > .env
    ```

    Add `.env` to your `.gitignore`:

    ```bash  theme={null}
    echo ".env" >> .gitignore
    ```

    <Warning>
      Make sure you keep your `ANTHROPIC_API_KEY` secure!
    </Warning>

    ## Creating the Client

    ### Basic Client Structure

    First, let's set up our imports and create the basic client class:

    ```python  theme={null}
    import asyncio
    from typing import Optional
    from contextlib import AsyncExitStack

    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    from anthropic import Anthropic
    from dotenv import load_dotenv

    load_dotenv()  # load environment variables from .env

    class MCPClient:
        def __init__(self):
            # Initialize session and client objects
            self.session: Optional[ClientSession] = None
            self.exit_stack = AsyncExitStack()
            self.anthropic = Anthropic()
        # methods will go here
    ```

    ### Server Connection Management

    Next, we'll implement the method to connect to an MCP server:

    ```python  theme={null}
    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])
    ```

    ### Query Processing Logic

    Now let's add the core functionality for processing queries and handling tool calls:

    ```python  theme={null}
    async def process_query(self, query: str) -> str:
        """Process a query using Claude and available tools"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        # Initial Claude API call
        response = self.anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=messages,
            tools=available_tools
        )

        # Process response and handle tool calls
        final_text = []

        assistant_message_content = []
        for content in response.content:
            if content.type == 'text':
                final_text.append(content.text)
                assistant_message_content.append(content)
            elif content.type == 'tool_use':
                tool_name = content.name
                tool_args = content.input

                # Execute tool call
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")

                assistant_message_content.append(content)
                messages.append({
                    "role": "assistant",
                    "content": assistant_message_content
                })
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": result.content
                        }
                    ]
                })

                # Get next response from Claude
                response = self.anthropic.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    messages=messages,
                    tools=available_tools
                )

                final_text.append(response.content[0].text)

        return "\n".join(final_text)
    ```

    ### Interactive Chat Interface

    Now we'll add the chat loop and cleanup functionality:

    ```python  theme={null}
    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()
    ```

    ### Main Entry Point

    Finally, we'll add the main execution logic:

    ```python  theme={null}
    async def main():
        if len(sys.argv) < 2:
            print("Usage: python client.py <path_to_server_script>")
            sys.exit(1)

        client = MCPClient()
        try:
            await client.connect_to_server(sys.argv[1])
            await client.chat_loop()
        finally:
            await client.cleanup()

    if __name__ == "__main__":
        import sys
        asyncio.run(main())
    ```

    You can find the complete `client.py` file [here](https://github.com/modelcontextprotocol/quickstart-resources/blob/main/mcp-client-python/client.py).

    ## Key Components Explained

    ### 1. Client Initialization

    * The `MCPClient` class initializes with session management and API clients
    * Uses `AsyncExitStack` for proper resource management
    * Configures the Anthropic client for Claude interactions

    ### 2. Server Connection

    * Supports both Python and Node.js servers
    * Validates server script type
    * Sets up proper communication channels
    * Initializes the session and lists available tools

    ### 3. Query Processing

    * Maintains conversation context
    * Handles Claude's responses and tool calls
    * Manages the message flow between Claude and tools
    * Combines results into a coherent response

    ### 4. Interactive Interface

    * Provides a simple command-line interface
    * Handles user input and displays responses
    * Includes basic error handling
    * Allows graceful exit

    ### 5. Resource Management

    * Proper cleanup of resources
    * Error handling for connection issues
    * Graceful shutdown procedures

    ## Common Customization Points

    1. **Tool Handling**
       * Modify `process_query()` to handle specific tool types
       * Add custom error handling for tool calls
       * Implement tool-specific response formatting

    2. **Response Processing**
       * Customize how tool results are formatted
       * Add response filtering or transformation
       * Implement custom logging

    3. **User Interface**
       * Add a GUI or web interface
       * Implement rich console output
       * Add command history or auto-completion

    ## Running the Client

    To run your client with any MCP server:

    ```bash  theme={null}
    uv run client.py path/to/server.py # python server
    uv run client.py path/to/build/index.js # node server
    ```

    <Note>
      If you're continuing [the weather tutorial from the server quickstart](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python), your command might look something like this: `python client.py .../quickstart-resources/weather-server-python/weather.py`
    </Note>

    The client will:

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude

    Here's an example of what it should look like if connected to the weather server from the server quickstart:

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=686d6e0ae7c54f807827db111eaed7d4" data-og-width="1932" width="1932" data-og-height="1739" height="1739" data-path="images/client-claude-cli-python.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?w=280&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=48ff45c4ca51501589d9f20f060daa56 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?w=560&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=b35ca5d8a67c2f08efec9c6519efcfe2 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?w=840&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=51b8f5c7fa48db6ccd30aa9988a8c917 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?w=1100&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=9e1b01bc4c324a7e5100674f63f36b13 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?w=1650&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=e3e961bd5b5506fed6c860f70df9bf9d 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/client-claude-cli-python.png?w=2500&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=da01c2527db68cb0c99d29d20751a868 2500w" />
    </Frame>

    ## How It Works

    When you submit a query:

    1. The client gets the list of available tools from the server
    2. Your query is sent to Claude along with tool descriptions
    3. Claude decides which tools (if any) to use
    4. The client executes any requested tool calls through the server
    5. Results are sent back to Claude
    6. Claude provides a natural language response
    7. The response is displayed to you

    ## Best practices

    1. **Error Handling**
       * Always wrap tool calls in try-catch blocks
       * Provide meaningful error messages
       * Gracefully handle connection issues

    2. **Resource Management**
       * Use `AsyncExitStack` for proper cleanup
       * Close connections when done
       * Handle server disconnections

    3. **Security**
       * Store API keys securely in `.env`
       * Validate server responses
       * Be cautious with tool permissions

    4. **Tool Names**
       * Tool names can be validated according to the format specified [here](/specification/draft/server/tools#tool-names)
       * If a tool name conforms to the specified format, it should not fail validation by an MCP client

    ## Troubleshooting

    ### Server Path Issues

    * Double-check the path to your server script is correct
    * Use the absolute path if the relative path isn't working
    * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
    * Verify the server file has the correct extension (.py for Python or .js for Node.js)

    Example of correct path usage:

    ```bash  theme={null}
    # Relative path
    uv run client.py ./server/weather.py

    # Absolute path
    uv run client.py /Users/username/projects/mcp-server/weather.py

    # Windows path (either format works)
    uv run client.py C:/projects/mcp-server/weather.py
    uv run client.py C:\\projects\\mcp-server\\weather.py
    ```

    ### Response Timing

    * The first response might take up to 30 seconds to return
    * This is normal and happens while:
      * The server initializes
      * Claude processes the query
      * Tools are being executed
    * Subsequent responses are typically faster
    * Don't interrupt the process during this initial waiting period

    ### Common Error Messages

    If you see:

    * `FileNotFoundError`: Check your server path
    * `Connection refused`: Ensure the server is running and the path is correct
    * `Tool execution failed`: Verify the tool's required environment variables are set
    * `Timeout error`: Consider increasing the timeout in your client configuration
  </Tab>

  <Tab title="Node">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-typescript)

    ## System Requirements

    Before starting, ensure your system meets these requirements:

    * Mac or Windows computer
    * Node.js 17 or higher installed
    * Latest version of `npm` installed
    * Anthropic API key (Claude)

    ## Setting Up Your Environment

    First, let's create and set up our project:

    <CodeGroup>
      ```bash macOS/Linux theme={null}
      # Create project directory
      mkdir mcp-client-typescript
      cd mcp-client-typescript

      # Initialize npm project
      npm init -y

      # Install dependencies
      npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv

      # Install dev dependencies
      npm install -D @types/node typescript

      # Create source file
      touch index.ts
      ```

      ```powershell Windows theme={null}
      # Create project directory
      md mcp-client-typescript
      cd mcp-client-typescript

      # Initialize npm project
      npm init -y

      # Install dependencies
      npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv

      # Install dev dependencies
      npm install -D @types/node typescript

      # Create source file
      new-item index.ts
      ```
    </CodeGroup>

    Update your `package.json` to set `type: "module"` and a build script:

    ```json package.json theme={null}
    {
      "type": "module",
      "scripts": {
        "build": "tsc && chmod 755 build/index.js"
      }
    }
    ```

    Create a `tsconfig.json` in the root of your project:

    ```json tsconfig.json theme={null}
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "./build",
        "rootDir": "./",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": ["index.ts"],
      "exclude": ["node_modules"]
    }
    ```

    ## Setting Up Your API Key

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).

    Create a `.env` file to store it:

    ```bash  theme={null}
    echo "ANTHROPIC_API_KEY=<your key here>" > .env
    ```

    Add `.env` to your `.gitignore`:

    ```bash  theme={null}
    echo ".env" >> .gitignore
    ```

    <Warning>
      Make sure you keep your `ANTHROPIC_API_KEY` secure!
    </Warning>

    ## Creating the Client

    ### Basic Client Structure

    First, let's set up our imports and create the basic client class in `index.ts`:

    ```typescript  theme={null}
    import { Anthropic } from "@anthropic-ai/sdk";
    import {
      MessageParam,
      Tool,
    } from "@anthropic-ai/sdk/resources/messages/messages.mjs";
    import { Client } from "@modelcontextprotocol/sdk/client/index.js";
    import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
    import readline from "readline/promises";
    import dotenv from "dotenv";

    dotenv.config();

    const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
    if (!ANTHROPIC_API_KEY) {
      throw new Error("ANTHROPIC_API_KEY is not set");
    }

    class MCPClient {
      private mcp: Client;
      private anthropic: Anthropic;
      private transport: StdioClientTransport | null = null;
      private tools: Tool[] = [];

      constructor() {
        this.anthropic = new Anthropic({
          apiKey: ANTHROPIC_API_KEY,
        });
        this.mcp = new Client({ name: "mcp-client-cli", version: "1.0.0" });
      }
      // methods will go here
    }
    ```

    ### Server Connection Management

    Next, we'll implement the method to connect to an MCP server:

    ```typescript  theme={null}
    async connectToServer(serverScriptPath: string) {
      try {
        const isJs = serverScriptPath.endsWith(".js");
        const isPy = serverScriptPath.endsWith(".py");
        if (!isJs && !isPy) {
          throw new Error("Server script must be a .js or .py file");
        }
        const command = isPy
          ? process.platform === "win32"
            ? "python"
            : "python3"
          : process.execPath;

        this.transport = new StdioClientTransport({
          command,
          args: [serverScriptPath],
        });
        await this.mcp.connect(this.transport);

        const toolsResult = await this.mcp.listTools();
        this.tools = toolsResult.tools.map((tool) => {
          return {
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
          };
        });
        console.log(
          "Connected to server with tools:",
          this.tools.map(({ name }) => name)
        );
      } catch (e) {
        console.log("Failed to connect to MCP server: ", e);
        throw e;
      }
    }
    ```

    ### Query Processing Logic

    Now let's add the core functionality for processing queries and handling tool calls:

    ```typescript  theme={null}
    async processQuery(query: string) {
      const messages: MessageParam[] = [
        {
          role: "user",
          content: query,
        },
      ];

      const response = await this.anthropic.messages.create({
        model: "claude-sonnet-4-20250514",
        max_tokens: 1000,
        messages,
        tools: this.tools,
      });

      const finalText = [];

      for (const content of response.content) {
        if (content.type === "text") {
          finalText.push(content.text);
        } else if (content.type === "tool_use") {
          const toolName = content.name;
          const toolArgs = content.input as { [x: string]: unknown } | undefined;

          const result = await this.mcp.callTool({
            name: toolName,
            arguments: toolArgs,
          });
          finalText.push(
            `[Calling tool ${toolName} with args ${JSON.stringify(toolArgs)}]`
          );

          messages.push({
            role: "user",
            content: result.content as string,
          });

          const response = await this.anthropic.messages.create({
            model: "claude-sonnet-4-20250514",
            max_tokens: 1000,
            messages,
          });

          finalText.push(
            response.content[0].type === "text" ? response.content[0].text : ""
          );
        }
      }

      return finalText.join("\n");
    }
    ```

    ### Interactive Chat Interface

    Now we'll add the chat loop and cleanup functionality:

    ```typescript  theme={null}
    async chatLoop() {
      const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
      });

      try {
        console.log("\nMCP Client Started!");
        console.log("Type your queries or 'quit' to exit.");

        while (true) {
          const message = await rl.question("\nQuery: ");
          if (message.toLowerCase() === "quit") {
            break;
          }
          const response = await this.processQuery(message);
          console.log("\n" + response);
        }
      } finally {
        rl.close();
      }
    }

    async cleanup() {
      await this.mcp.close();
    }
    ```

    ### Main Entry Point

    Finally, we'll add the main execution logic:

    ```typescript  theme={null}
    async function main() {
      if (process.argv.length < 3) {
        console.log("Usage: node index.ts <path_to_server_script>");
        return;
      }
      const mcpClient = new MCPClient();
      try {
        await mcpClient.connectToServer(process.argv[2]);
        await mcpClient.chatLoop();
      } finally {
        await mcpClient.cleanup();
        process.exit(0);
      }
    }

    main();
    ```

    ## Running the Client

    To run your client with any MCP server:

    ```bash  theme={null}
    # Build TypeScript
    npm run build

    # Run the client
    node build/index.js path/to/server.py # python server
    node build/index.js path/to/build/index.js # node server
    ```

    <Note>
      If you're continuing [the weather tutorial from the server quickstart](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript), your command might look something like this: `node build/index.js .../quickstart-resources/weather-server-typescript/build/index.js`
    </Note>

    **The client will:**

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude

    ## How It Works

    When you submit a query:

    1. The client gets the list of available tools from the server
    2. Your query is sent to Claude along with tool descriptions
    3. Claude decides which tools (if any) to use
    4. The client executes any requested tool calls through the server
    5. Results are sent back to Claude
    6. Claude provides a natural language response
    7. The response is displayed to you

    ## Best practices

    1. **Error Handling**
       * Use TypeScript's type system for better error detection
       * Wrap tool calls in try-catch blocks
       * Provide meaningful error messages
       * Gracefully handle connection issues

    2. **Security**
       * Store API keys securely in `.env`
       * Validate server responses
       * Be cautious with tool permissions

    ## Troubleshooting

    ### Server Path Issues

    * Double-check the path to your server script is correct
    * Use the absolute path if the relative path isn't working
    * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
    * Verify the server file has the correct extension (.js for Node.js or .py for Python)

    Example of correct path usage:

    ```bash  theme={null}
    # Relative path
    node build/index.js ./server/build/index.js

    # Absolute path
    node build/index.js /Users/username/projects/mcp-server/build/index.js

    # Windows path (either format works)
    node build/index.js C:/projects/mcp-server/build/index.js
    node build/index.js C:\\projects\\mcp-server\\build\\index.js
    ```

    ### Response Timing

    * The first response might take up to 30 seconds to return
    * This is normal and happens while:
      * The server initializes
      * Claude processes the query
      * Tools are being executed
    * Subsequent responses are typically faster
    * Don't interrupt the process during this initial waiting period

    ### Common Error Messages

    If you see:

    * `Error: Cannot find module`: Check your build folder and ensure TypeScript compilation succeeded
    * `Connection refused`: Ensure the server is running and the path is correct
    * `Tool execution failed`: Verify the tool's required environment variables are set
    * `ANTHROPIC_API_KEY is not set`: Check your .env file and environment variables
    * `TypeError`: Ensure you're using the correct types for tool arguments
  </Tab>

  <Tab title="Java">
    <Note>
      This is a quickstart demo based on Spring AI MCP auto-configuration and boot starters.
      To learn how to create sync and async MCP Clients manually, consult the [Java SDK Client](/sdk/java/mcp-client) documentation
    </Note>

    This example demonstrates how to build an interactive chatbot that combines Spring AI's Model Context Protocol (MCP) with the [Brave Search MCP Server](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search). The application creates a conversational interface powered by Anthropic's Claude AI model that can perform internet searches through Brave Search, enabling natural language interactions with real-time web data.
    [You can find the complete code for this tutorial here.](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/web-search/brave-chatbot)

    ## System Requirements

    Before starting, ensure your system meets these requirements:

    * Java 17 or higher
    * Maven 3.6+
    * npx package manager
    * Anthropic API key (Claude)
    * Brave Search API key

    ## Setting Up Your Environment

    1. Install npx (Node Package eXecute):
       First, make sure to install [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
       and then run:

       ```bash  theme={null}
       npm install -g npx
       ```

    2. Clone the repository:

       ```bash  theme={null}
       git clone https://github.com/spring-projects/spring-ai-examples.git
       cd model-context-protocol/brave-chatbot
       ```

    3. Set up your API keys:

       ```bash  theme={null}
       export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
       export BRAVE_API_KEY='your-brave-api-key-here'
       ```

    4. Build the application:

       ```bash  theme={null}
       ./mvnw clean install
       ```

    5. Run the application using Maven:
       ```bash  theme={null}
       ./mvnw spring-boot:run
       ```

    <Warning>
      Make sure you keep your `ANTHROPIC_API_KEY` and `BRAVE_API_KEY` keys secure!
    </Warning>

    ## How it Works

    The application integrates Spring AI with the Brave Search MCP server through several components:

    ### MCP Client Configuration

    1. Required dependencies in pom.xml:

    ```xml  theme={null}
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-mcp-client</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-model-anthropic</artifactId>
    </dependency>
    ```

    2. Application properties (application.yml):

    ```yml  theme={null}
    spring:
      ai:
        mcp:
          client:
            enabled: true
            name: brave-search-client
            version: 1.0.0
            type: SYNC
            request-timeout: 20s
            stdio:
              root-change-notification: true
              servers-configuration: classpath:/mcp-servers-config.json
            toolcallback:
              enabled: true
        anthropic:
          api-key: ${ANTHROPIC_API_KEY}
    ```

    This activates the `spring-ai-starter-mcp-client` to create one or more `McpClient`s based on the provided server configuration.
    The `spring.ai.mcp.client.toolcallback.enabled=true` property enables the tool callback mechanism, that automatically registers all MCP tool as spring ai tools.
    It is disabled by default.

    3. MCP Server Configuration (`mcp-servers-config.json`):

    ```json  theme={null}
    {
      "mcpServers": {
        "brave-search": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-brave-search"],
          "env": {
            "BRAVE_API_KEY": "<PUT YOUR BRAVE API KEY>"
          }
        }
      }
    }
    ```

    ### Chat Implementation

    The chatbot is implemented using Spring AI's ChatClient with MCP tool integration:

    ```java  theme={null}
    var chatClient = chatClientBuilder
        .defaultSystem("You are useful assistant, expert in AI and Java.")
        .defaultToolCallbacks((Object[]) mcpToolAdapter.toolCallbacks())
        .defaultAdvisors(new MessageChatMemoryAdvisor(new InMemoryChatMemory()))
        .build();
    ```

    Key features:

    * Uses Claude AI model for natural language understanding
    * Integrates Brave Search through MCP for real-time web search capabilities
    * Maintains conversation memory using InMemoryChatMemory
    * Runs as an interactive command-line application

    ### Build and run

    ```bash  theme={null}
    ./mvnw clean install
    java -jar ./target/ai-mcp-brave-chatbot-0.0.1-SNAPSHOT.jar
    ```

    or

    ```bash  theme={null}
    ./mvnw spring-boot:run
    ```

    The application will start an interactive chat session where you can ask questions. The chatbot will use Brave Search when it needs to find information from the internet to answer your queries.

    The chatbot can:

    * Answer questions using its built-in knowledge
    * Perform web searches when needed using Brave Search
    * Remember context from previous messages in the conversation
    * Combine information from multiple sources to provide comprehensive answers

    ### Advanced Configuration

    The MCP client supports additional configuration options:

    * Client customization through `McpSyncClientCustomizer` or `McpAsyncClientCustomizer`
    * Multiple clients with multiple transport types: `STDIO` and `SSE` (Server-Sent Events)
    * Integration with Spring AI's tool execution framework
    * Automatic client initialization and lifecycle management

    For WebFlux-based applications, you can use the WebFlux starter instead:

    ```xml  theme={null}
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-mcp-client-webflux-spring-boot-starter</artifactId>
    </dependency>
    ```

    This provides similar functionality but uses a WebFlux-based SSE transport implementation, recommended for production deployments.
  </Tab>

  <Tab title="Kotlin">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-client)

    ## System Requirements

    Before starting, ensure your system meets these requirements:

    * Java 17 or higher
    * Anthropic API key (Claude)

    ## Setting up your environment

    First, let's install `java` and `gradle` if you haven't already.
    You can download `java` from [official Oracle JDK website](https://www.oracle.com/java/technologies/downloads/).
    Verify your `java` installation:

    ```bash  theme={null}
    java --version
    ```

    Now, let's create and set up your project:

    <CodeGroup>
      ```bash macOS/Linux theme={null}
      # Create a new directory for our project
      mkdir kotlin-mcp-client
      cd kotlin-mcp-client

      # Initialize a new kotlin project
      gradle init
      ```

      ```powershell Windows theme={null}
      # Create a new directory for our project
      md kotlin-mcp-client
      cd kotlin-mcp-client
      # Initialize a new kotlin project
      gradle init
      ```
    </CodeGroup>

    After running `gradle init`, you will be presented with options for creating your project.
    Select **Application** as the project type, **Kotlin** as the programming language, and **Java 17** as the Java version.

    Alternatively, you can create a Kotlin application using the [IntelliJ IDEA project wizard](https://kotlinlang.org/docs/jvm-get-started.html).

    After creating the project, add the following dependencies:

    <CodeGroup>
      ```kotlin build.gradle.kts theme={null}
      val mcpVersion = "0.4.0"
      val slf4jVersion = "2.0.9"
      val anthropicVersion = "0.8.0"

      dependencies {
          implementation("io.modelcontextprotocol:kotlin-sdk:$mcpVersion")
          implementation("org.slf4j:slf4j-nop:$slf4jVersion")
          implementation("com.anthropic:anthropic-java:$anthropicVersion")
      }
      ```

      ```groovy build.gradle theme={null}
      def mcpVersion = '0.3.0'
      def slf4jVersion = '2.0.9'
      def anthropicVersion = '0.8.0'
      dependencies {
          implementation "io.modelcontextprotocol:kotlin-sdk:$mcpVersion"
          implementation "org.slf4j:slf4j-nop:$slf4jVersion"
          implementation "com.anthropic:anthropic-java:$anthropicVersion"
      }
      ```
    </CodeGroup>

    Also, add the following plugins to your build script:

    <CodeGroup>
      ```kotlin build.gradle.kts theme={null}
      plugins {
          id("com.github.johnrengelman.shadow") version "8.1.1"
      }
      ```

      ```groovy build.gradle theme={null}
      plugins {
          id 'com.github.johnrengelman.shadow' version '8.1.1'
      }
      ```
    </CodeGroup>

    ## Setting up your API key

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).

    Set up your API key:

    ```bash  theme={null}
    export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
    ```

    <Warning>
      Make sure your keep your `ANTHROPIC_API_KEY` secure!
    </Warning>

    ## Creating the Client

    ### Basic Client Structure

    First, let's create the basic client class:

    ```kotlin  theme={null}
    class MCPClient : AutoCloseable {
        private val anthropic = AnthropicOkHttpClient.fromEnv()
        private val mcp: Client = Client(clientInfo = Implementation(name = "mcp-client-cli", version = "1.0.0"))
        private lateinit var tools: List<ToolUnion>

        // methods will go here

        override fun close() {
            runBlocking {
                mcp.close()
                anthropic.close()
            }
        }
    ```

    ### Server connection management

    Next, we'll implement the method to connect to an MCP server:

    ```kotlin  theme={null}
    suspend fun connectToServer(serverScriptPath: String) {
        try {
            val command = buildList {
                when (serverScriptPath.substringAfterLast(".")) {
                    "js" -> add("node")
                    "py" -> add(if (System.getProperty("os.name").lowercase().contains("win")) "python" else "python3")
                    "jar" -> addAll(listOf("java", "-jar"))
                    else -> throw IllegalArgumentException("Server script must be a .js, .py or .jar file")
                }
                add(serverScriptPath)
            }

            val process = ProcessBuilder(command).start()
            val transport = StdioClientTransport(
                input = process.inputStream.asSource().buffered(),
                output = process.outputStream.asSink().buffered()
            )

            mcp.connect(transport)

            val toolsResult = mcp.listTools()
            tools = toolsResult?.tools?.map { tool ->
                ToolUnion.ofTool(
                    Tool.builder()
                        .name(tool.name)
                        .description(tool.description ?: "")
                        .inputSchema(
                            Tool.InputSchema.builder()
                                .type(JsonValue.from(tool.inputSchema.type))
                                .properties(tool.inputSchema.properties.toJsonValue())
                                .putAdditionalProperty("required", JsonValue.from(tool.inputSchema.required))
                                .build()
                        )
                        .build()
                )
            } ?: emptyList()
            println("Connected to server with tools: ${tools.joinToString(", ") { it.tool().get().name() }}")
        } catch (e: Exception) {
            println("Failed to connect to MCP server: $e")
            throw e
        }
    }
    ```

    Also create a helper function to convert from `JsonObject` to `JsonValue` for Anthropic:

    ```kotlin  theme={null}
    private fun JsonObject.toJsonValue(): JsonValue {
        val mapper = ObjectMapper()
        val node = mapper.readTree(this.toString())
        return JsonValue.fromJsonNode(node)
    }
    ```

    ### Query processing logic

    Now let's add the core functionality for processing queries and handling tool calls:

    ```kotlin  theme={null}
    private val messageParamsBuilder: MessageCreateParams.Builder = MessageCreateParams.builder()
        .model(Model.CLAUDE_SONNET_4_20250514)
        .maxTokens(1024)

    suspend fun processQuery(query: String): String {
        val messages = mutableListOf(
            MessageParam.builder()
                .role(MessageParam.Role.USER)
                .content(query)
                .build()
        )

        val response = anthropic.messages().create(
            messageParamsBuilder
                .messages(messages)
                .tools(tools)
                .build()
        )

        val finalText = mutableListOf<String>()
        response.content().forEach { content ->
            when {
                content.isText() -> finalText.add(content.text().getOrNull()?.text() ?: "")

                content.isToolUse() -> {
                    val toolName = content.toolUse().get().name()
                    val toolArgs =
                        content.toolUse().get()._input().convert(object : TypeReference<Map<String, JsonValue>>() {})

                    val result = mcp.callTool(
                        name = toolName,
                        arguments = toolArgs ?: emptyMap()
                    )
                    finalText.add("[Calling tool $toolName with args $toolArgs]")

                    messages.add(
                        MessageParam.builder()
                            .role(MessageParam.Role.USER)
                            .content(
                                """
                                    "type": "tool_result",
                                    "tool_name": $toolName,
                                    "result": ${result?.content?.joinToString("\n") { (it as TextContent).text ?: "" }}
                                """.trimIndent()
                            )
                            .build()
                    )

                    val aiResponse = anthropic.messages().create(
                        messageParamsBuilder
                            .messages(messages)
                            .build()
                    )

                    finalText.add(aiResponse.content().first().text().getOrNull()?.text() ?: "")
                }
            }
        }

        return finalText.joinToString("\n", prefix = "", postfix = "")
    }
    ```

    ### Interactive chat

    We'll add the chat loop:

    ```kotlin  theme={null}
    suspend fun chatLoop() {
        println("\nMCP Client Started!")
        println("Type your queries or 'quit' to exit.")

        while (true) {
            print("\nQuery: ")
            val message = readLine() ?: break
            if (message.lowercase() == "quit") break
            val response = processQuery(message)
            println("\n$response")
        }
    }
    ```

    ### Main entry point

    Finally, we'll add the main execution function:

    ```kotlin  theme={null}
    fun main(args: Array<String>) = runBlocking {
        if (args.isEmpty()) throw IllegalArgumentException("Usage: java -jar <your_path>/build/libs/kotlin-mcp-client-0.1.0-all.jar <path_to_server_script>")
        val serverPath = args.first()
        val client = MCPClient()
        client.use {
            client.connectToServer(serverPath)
            client.chatLoop()
        }
    }
    ```

    ## Running the client

    To run your client with any MCP server:

    ```bash  theme={null}
    ./gradlew build

    # Run the client
    java -jar build/libs/<your-jar-name>.jar path/to/server.jar # jvm server
    java -jar build/libs/<your-jar-name>.jar path/to/server.py # python server
    java -jar build/libs/<your-jar-name>.jar path/to/build/index.js # node server
    ```

    <Note>
      If you're continuing the weather tutorial from the server quickstart, your command might look something like this: `java -jar build/libs/kotlin-mcp-client-0.1.0-all.jar .../samples/weather-stdio-server/build/libs/weather-stdio-server-0.1.0-all.jar`
    </Note>

    **The client will:**

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude

    ## How it works

    Here's a high-level workflow schema:

    ```mermaid  theme={null}
    ---
    config:
        theme: neutral
    ---
    sequenceDiagram
        actor User
        participant Client
        participant Claude
        participant MCP_Server as MCP Server
        participant Tools

        User->>Client: Send query
        Client<<->>MCP_Server: Get available tools
        Client->>Claude: Send query with tool descriptions
        Claude-->>Client: Decide tool execution
        Client->>MCP_Server: Request tool execution
        MCP_Server->>Tools: Execute chosen tools
        Tools-->>MCP_Server: Return results
        MCP_Server-->>Client: Send results
        Client->>Claude: Send tool results
        Claude-->>Client: Provide final response
        Client-->>User: Display response
    ```

    When you submit a query:

    1. The client gets the list of available tools from the server
    2. Your query is sent to Claude along with tool descriptions
    3. Claude decides which tools (if any) to use
    4. The client executes any requested tool calls through the server
    5. Results are sent back to Claude
    6. Claude provides a natural language response
    7. The response is displayed to you

    ## Best practices

    1. **Error Handling**
       * Leverage Kotlin's type system to model errors explicitly
       * Wrap external tool and API calls in `try-catch` blocks when exceptions are possible
       * Provide clear and meaningful error messages
       * Handle network timeouts and connection issues gracefully

    2. **Security**
       * Store API keys and secrets securely in `local.properties`, environment variables, or secret managers
       * Validate all external responses to avoid unexpected or unsafe data usage
       * Be cautious with permissions and trust boundaries when using tools

    ## Troubleshooting

    ### Server Path Issues

    * Double-check the path to your server script is correct
    * Use the absolute path if the relative path isn't working
    * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
    * Make sure that the required runtime is installed (java for Java, npm for Node.js, or uv for Python)
    * Verify the server file has the correct extension (.jar for Java, .js for Node.js or .py for Python)

    Example of correct path usage:

    ```bash  theme={null}
    # Relative path
    java -jar build/libs/client.jar ./server/build/libs/server.jar

    # Absolute path
    java -jar build/libs/client.jar /Users/username/projects/mcp-server/build/libs/server.jar

    # Windows path (either format works)
    java -jar build/libs/client.jar C:/projects/mcp-server/build/libs/server.jar
    java -jar build/libs/client.jar C:\\projects\\mcp-server\\build\\libs\\server.jar
    ```

    ### Response Timing

    * The first response might take up to 30 seconds to return
    * This is normal and happens while:
      * The server initializes
      * Claude processes the query
      * Tools are being executed
    * Subsequent responses are typically faster
    * Don't interrupt the process during this initial waiting period

    ### Common Error Messages

    If you see:

    * `Connection refused`: Ensure the server is running and the path is correct
    * `Tool execution failed`: Verify the tool's required environment variables are set
    * `ANTHROPIC_API_KEY is not set`: Check your environment variables
  </Tab>

  <Tab title="C#">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartClient)

    ## System Requirements

    Before starting, ensure your system meets these requirements:

    * .NET 8.0 or higher
    * Anthropic API key (Claude)
    * Windows, Linux, or macOS

    ## Setting up your environment

    First, create a new .NET project:

    ```bash  theme={null}
    dotnet new console -n QuickstartClient
    cd QuickstartClient
    ```

    Then, add the required dependencies to your project:

    ```bash  theme={null}
    dotnet add package ModelContextProtocol --prerelease
    dotnet add package Anthropic.SDK
    dotnet add package Microsoft.Extensions.Hosting
    dotnet add package Microsoft.Extensions.AI
    ```

    ## Setting up your API key

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).

    ```bash  theme={null}
    dotnet user-secrets init
    dotnet user-secrets set "ANTHROPIC_API_KEY" "<your key here>"
    ```

    ## Creating the Client

    ### Basic Client Structure

    First, let's setup the basic client class in the file `Program.cs`:

    ```csharp  theme={null}
    using Anthropic.SDK;
    using Microsoft.Extensions.AI;
    using Microsoft.Extensions.Configuration;
    using Microsoft.Extensions.Hosting;
    using ModelContextProtocol.Client;
    using ModelContextProtocol.Protocol.Transport;

    var builder = Host.CreateApplicationBuilder(args);

    builder.Configuration
        .AddEnvironmentVariables()
        .AddUserSecrets<Program>();
    ```

    This creates the beginnings of a .NET console application that can read the API key from user secrets.

    Next, we'll setup the MCP Client:

    ```csharp  theme={null}
    var (command, arguments) = GetCommandAndArguments(args);

    var clientTransport = new StdioClientTransport(new()
    {
        Name = "Demo Server",
        Command = command,
        Arguments = arguments,
    });

    await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

    var tools = await mcpClient.ListToolsAsync();
    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
    }
    ```

    Add this function at the end of the `Program.cs` file:

    ```csharp  theme={null}
    static (string command, string[] arguments) GetCommandAndArguments(string[] args)
    {
        return args switch
        {
            [var script] when script.EndsWith(".py") => ("python", args),
            [var script] when script.EndsWith(".js") => ("node", args),
            [var script] when Directory.Exists(script) || (File.Exists(script) && script.EndsWith(".csproj")) => ("dotnet", ["run", "--project", script, "--no-build"]),
            _ => throw new NotSupportedException("An unsupported server script was provided. Supported scripts are .py, .js, or .csproj")
        };
    }
    ```

    This creates an MCP client that will connect to a server that is provided as a command line argument. It then lists the available tools from the connected server.

    ### Query processing logic

    Now let's add the core functionality for processing queries and handling tool calls:

    ```csharp  theme={null}
    using var anthropicClient = new AnthropicClient(new APIAuthentication(builder.Configuration["ANTHROPIC_API_KEY"]))
        .Messages
        .AsBuilder()
        .UseFunctionInvocation()
        .Build();

    var options = new ChatOptions
    {
        MaxOutputTokens = 1000,
        ModelId = "claude-sonnet-4-20250514",
        Tools = [.. tools]
    };

    Console.ForegroundColor = ConsoleColor.Green;
    Console.WriteLine("MCP Client Started!");
    Console.ResetColor();

    PromptForInput();
    while(Console.ReadLine() is string query && !"exit".Equals(query, StringComparison.OrdinalIgnoreCase))
    {
        if (string.IsNullOrWhiteSpace(query))
        {
            PromptForInput();
            continue;
        }

        await foreach (var message in anthropicClient.GetStreamingResponseAsync(query, options))
        {
            Console.Write(message);
        }
        Console.WriteLine();

        PromptForInput();
    }

    static void PromptForInput()
    {
        Console.WriteLine("Enter a command (or 'exit' to quit):");
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.Write("> ");
        Console.ResetColor();
    }
    ```

    ## Key Components Explained

    ### 1. Client Initialization

    * The client is initialized using `McpClientFactory.CreateAsync()`, which sets up the transport type and command to run the server.

    ### 2. Server Connection

    * Supports Python, Node.js, and .NET servers.
    * The server is started using the command specified in the arguments.
    * Configures to use stdio for communication with the server.
    * Initializes the session and available tools.

    ### 3. Query Processing

    * Leverages [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/ai-extensions) for the chat client.
    * Configures the `IChatClient` to use automatic tool (function) invocation.
    * The client reads user input and sends it to the server.
    * The server processes the query and returns a response.
    * The response is displayed to the user.

    ## Running the Client

    To run your client with any MCP server:

    ```bash  theme={null}
    dotnet run -- path/to/server.csproj # dotnet server
    dotnet run -- path/to/server.py # python server
    dotnet run -- path/to/server.js # node server
    ```

    <Note>
      If you're continuing the weather tutorial from the server quickstart, your command might look something like this: `dotnet run -- path/to/QuickstartWeatherServer`.
    </Note>

    The client will:

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude
    4. Exit the session when done

    Here's an example of what it should look like it connected to a weather server quickstart:

    <Frame>
      <img src="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=fcf28dde150d6db879402ad8150c6b23" data-og-width="1115" width="1115" data-og-height="666" height="666" data-path="images/quickstart-dotnet-client.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?w=280&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=0c82cdfe1350b4a924a44d7beaa39f70 280w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?w=560&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=4fd6f3ed867741b44ae12940788be646 560w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?w=840&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=1b5fcfaf8b63b9ea71bf36aa20388a28 840w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?w=1100&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=cb969889d05ec8771c12b887f2940c7d 1100w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?w=1650&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=81b2cb62f60a9f3afb2d66cf3ee3df79 1650w, https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/quickstart-dotnet-client.png?w=2500&fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=ac9271a3dd0d7b424bb390ad0c31e14e 2500w" />
    </Frame>
  </Tab>
</Tabs>


## Next steps

<CardGroup cols={2}>
  <Card title="Example servers" icon="grid" href="/examples">
    Check out our gallery of official MCP servers and implementations
  </Card>

  <Card title="Example clients" icon="cubes" href="/clients">
    View the list of clients that support MCP integrations
  </Card>
</CardGroup>



---

**Navigation:** [Index](./index.md) | [Next →](./02-build-an-mcp-server.md)
