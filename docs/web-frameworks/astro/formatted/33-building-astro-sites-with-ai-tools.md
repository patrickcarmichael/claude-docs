---
title: "Building Astro sites with AI tools"
section: 33
---

# Building Astro sites with AI tools

> Resources and tips for building Astro sites with AI assistance

AI-powered editors and agentic coding tools generally have good knowledge of Astro’s core APIs and concepts. However, some may use older APIs and may not be aware of newer features or recent changes to the framework.

This guide covers how to enhance AI tools with up-to-date Astro knowledge and provides best practices for building Astro sites with AI assistance.

## Context files

[Section titled “Context files”](#context-files)

Astro provides [`llms.txt`](https://docs.astro.build/llms.txt) and [`llms-full.txt`](https://docs.astro.build/llms-full.txt) files that contains the full docs content in a format optimized for AI consumption. These are static files of the Astro Docs content in a streamlined Markdown format. Some AI tools can auto-discover these files if you provide `https://docs.astro.build` as a docs source.

While these files provide a minimal, easy-to-parse version of Astro’s documentation, they are large files that will use a lot of tokens if used directly in context and will need to be updated regularly to stay current. They are best used as a fallback when the AI tool does not have access to the latest documentation in other ways. [The MCP server](#astro-docs-mcp-server) provides more efficient access to the full documentation with real-time search capabilities, making it the preferred option when available.

## Astro Docs MCP Server

[Section titled “Astro Docs MCP Server”](#astro-docs-mcp-server)

You can ensure your AI tools have current Astro knowledge through the Astro Docs MCP (Model Context Protocol) server. This provides real-time access to the latest documentation, helping AI tools avoid outdated recommendations and ensuring they understand current best practices.

What is MCP?

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is a standardized way for AI tools to access external tools and data sources.

Unlike AI models trained on static data, the MCP server provides access to the latest Astro documentation. The server is free, open-source, and runs remotely with nothing to install locally.

The Astro Docs MCP server uses the [kapa.ai](https://www.kapa.ai/) API to maintain an up-to-date index of the Astro documentation.

### Server Details

[Section titled “Server Details”](#server-details)

* **Name**: Astro Docs
* **URL**: `https://mcp.docs.astro.build/mcp`
* **Transport**: Streamable HTTP

### Installation

[Section titled “Installation”](#installation)

The setup process varies depending on your AI development tool. You may see some tools refer to MCP servers as connectors, adapters, extensions, or plugins.

#### Manual setup

[Section titled “Manual setup”](#manual-setup)

Many tools support a common JSON configuration format for MCP servers. If there are not specific instructions for your chosen tool, you may be able to add the Astro Docs MCP server by including the following configuration in your tool’s MCP settings:

* Streamable HTTP

  mcp.json

  ```json
  {
    "mcpServers": {
      "Astro docs": {
        "type": "http",
        "url": "https://mcp.docs.astro.build/mcp"
      }
    }
  }
  ```jsx
* Local Proxy

  mcp.json

  ```json
  {
    "mcpServers": {
      "Astro docs": {
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
      }
    }
  }
  ```jsx
#### Claude Code CLI

[Section titled “Claude Code CLI”](#claude-code-cli)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) is an agentic coding tool that runs on the command line. Enabling the Astro Docs MCP server allows it to access the latest documentation while generating Astro code.

Install using the terminal command:

```shell
claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp
```jsx
[More info on using MCP servers with Claude Code](https://docs.anthropic.com/en/docs/claude-code/mcp)

#### Claude Code GitHub Action

[Section titled “Claude Code GitHub Action”](#claude-code-github-action)

Claude Code also provides a GitHub Action that can be used to run commands in response to GitHub events. Enabling the Astro Docs MCP server allows it to access the latest documentation while answering questions in comments or generating Astro code.

You can configure it to use the Astro Docs MCP server for documentation access by adding the following to the workflow file:

.github/workflows/claude.yml

```yaml

---

[← Previous](32-the-same-name-as-your-git-branch.md) | [Index](index.md) | [Next →](index.md)
