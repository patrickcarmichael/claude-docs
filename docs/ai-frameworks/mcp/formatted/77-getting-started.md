---
title: "Mcp: Getting started"
description: "Getting started section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Getting started


### Installation and basic usage

The Inspector runs directly through `npx` without requiring installation:

```bash  theme={null}
npx @modelcontextprotocol/inspector <command>
```

```bash  theme={null}
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### Inspecting servers from npm or PyPI

A common way to start server packages from [npm](https://npmjs.com) or [PyPI](https://pypi.org).

<Tabs>
  <Tab title="npm package">
    ```bash  theme={null}
    npx -y @modelcontextprotocol/inspector npx <package-name> <args>
    # For example
    npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem /Users/username/Desktop
    ```
  </Tab>

  <Tab title="PyPI package">
    ```bash  theme={null}
    npx @modelcontextprotocol/inspector uvx <package-name> <args>
    # For example
    npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
    ```
  </Tab>
</Tabs>

#### Inspecting locally developed servers

To inspect servers locally developed or downloaded as a repository, the most common
way is:

<Tabs>
  <Tab title="TypeScript">
    ```bash  theme={null}
    npx @modelcontextprotocol/inspector node path/to/server/index.js args...
    ```
  </Tab>

  <Tab title="Python">
    ```bash  theme={null}
    npx @modelcontextprotocol/inspector \
      uv \
      --directory path/to/server \
      run \
      package-name \
      args...
    ```
  </Tab>
</Tabs>

Please carefully read any attached README for the most accurate instructions.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← MCP Inspector](./76-mcp-inspector.md)

**Next:** [Feature overview →](./78-feature-overview.md)
