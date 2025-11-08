# Integrations & Extensions

**Navigation:** [← Previous: CI/CD](./05-cicd.md) | [Index](./index.md) | [Next: Advanced Features →](./07-advanced.md)

> **Note:** This is part of the chunked llms-full.txt. For organized topic documentation, see [../README.md](../README.md)

---

# JetBrains IDEs
Source: https://code.claude.com/docs/en/jetbrains

Use Claude Code with JetBrains IDEs including IntelliJ, PyCharm, WebStorm, and more

Claude Code integrates with JetBrains IDEs through a dedicated plugin, providing features like interactive diff viewing, selection context sharing, and more.

## Supported IDEs

The Claude Code plugin works with most JetBrains IDEs, including:

* IntelliJ IDEA
* PyCharm
* Android Studio
* WebStorm
* PhpStorm
* GoLand

## Features

* **Quick launch**: Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open Claude Code directly from your editor, or click the Claude Code button in the UI
* **Diff viewing**: Code changes can be displayed directly in the IDE diff viewer instead of the terminal
* **Selection context**: The current selection/tab in the IDE is automatically shared with Claude Code
* **File reference shortcuts**: Use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Linux/Windows) to insert file references (e.g., @File#L1-99)
* **Diagnostic sharing**: Diagnostic errors (lint, syntax, etc.) from the IDE are automatically shared with Claude as you work

## Installation

### Marketplace Installation

Find and install the [Claude Code plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) from the JetBrains marketplace and restart your IDE.

### Auto-Installation

The plugin may also be auto-installed when you run `claude` in the integrated terminal. The IDE must be restarted completely to take effect.

<Note>
  After installing the plugin, you must restart your IDE completely for it to take effect. You may need to restart multiple times.
</Note>

## Usage

### From Your IDE

Run `claude` from your IDE's integrated terminal, and all integration features will be active.

### From External Terminals

Use the `/ide` command in any external terminal to connect Claude Code to your JetBrains IDE and activate all features:

```bash  theme={null}
claude
> /ide
```

If you want Claude to have access to the same files as your IDE, start Claude Code from the same directory as your IDE project root.

## Configuration

### Claude Code Settings

Configure IDE integration through Claude Code's settings:

1. Run `claude`
2. Enter the `/config` command
3. Set the diff tool to `auto` for automatic IDE detection

### Plugin Settings

Configure the Claude Code plugin by going to **Settings → Tools → Claude Code \[Beta]**:

#### General Settings

* **Claude command**: Specify a custom command to run Claude (e.g., `claude`, `/usr/local/bin/claude`, or `npx @anthropic/claude`)
* **Suppress notification for Claude command not found**: Skip notifications about not finding the Claude command
* **Enable using Option+Enter for multi-line prompts** (macOS only): When enabled, Option+Enter inserts new lines in Claude Code prompts. Disable if experiencing issues with the Option key being captured unexpectedly (requires terminal restart)
* **Enable automatic updates**: Automatically check for and install plugin updates (applied on restart)

<Tip>
  For WSL users: Set `wsl -d Ubuntu -- bash -lic "claude"` as your Claude command (replace `Ubuntu` with your WSL distribution name)
</Tip>

#### ESC Key Configuration

If the ESC key doesn't interrupt Claude Code operations in JetBrains terminals:

1. Go to **Settings → Tools → Terminal**
2. Either:
   * Uncheck "Move focus to the editor with Escape", or
   * Click "Configure terminal keybindings" and delete the "Switch focus to Editor" shortcut
3. Apply the changes

This allows the ESC key to properly interrupt Claude Code operations.

## Special Configurations

### Remote Development

<Warning>
  When using JetBrains Remote Development, you must install the plugin in the remote host via **Settings → Plugin (Host)**.
</Warning>

The plugin must be installed on the remote host, not on your local client machine.

### WSL Configuration

<Warning>
  WSL users may need additional configuration for IDE detection to work properly. See our [WSL troubleshooting guide](/en/troubleshooting#jetbrains-ide-not-detected-on-wsl2) for detailed setup instructions.
</Warning>

WSL configuration may require:

* Proper terminal configuration
* Networking mode adjustments
* Firewall settings updates

## Troubleshooting

### Plugin Not Working

* Ensure you're running Claude Code from the project root directory
* Check that the JetBrains plugin is enabled in the IDE settings
* Completely restart the IDE (you may need to do this multiple times)
* For Remote Development, ensure the plugin is installed in the remote host

### IDE Not Detected

* Verify the plugin is installed and enabled
* Restart the IDE completely
* Check that you're running Claude Code from the integrated terminal
* For WSL users, see the [WSL troubleshooting guide](/en/troubleshooting#jetbrains-ide-not-detected-on-wsl2)

### Command Not Found

If clicking the Claude icon shows "command not found":

1. Verify Claude Code is installed: `npm list -g @anthropic-ai/claude-code`
2. Configure the Claude command path in plugin settings
3. For WSL users, use the WSL command format mentioned in the configuration section

## Security Considerations

When Claude Code runs in a JetBrains IDE with auto-edit permissions enabled, it may be able to modify IDE configuration files that can be automatically executed by your IDE. This may increase the risk of running Claude Code in auto-edit mode and allow bypassing Claude Code's permission prompts for bash execution.

When running in JetBrains IDEs, consider:

* Using manual approval mode for edits
* Taking extra care to ensure Claude is only used with trusted prompts
* Being aware of which files Claude Code has access to modify

For additional help, see our [troubleshooting guide](/en/troubleshooting).


# Connect Claude Code to tools via MCP
Source: https://code.claude.com/docs/en/mcp

Learn how to connect Claude Code to your tools with the Model Context Protocol.

export const MCPServersTable = ({platform = "all"}) => {
  const generateClaudeCodeCommand = server => {
    if (server.customCommands && server.customCommands.claudeCode) {
      return server.customCommands.claudeCode;
    }
    if (server.urls.http) {
      return `claude mcp add --transport http ${server.name.toLowerCase().replace(/[^a-z0-9]/g, '-')} ${server.urls.http}`;
    }
    if (server.urls.sse) {
      return `claude mcp add --transport sse ${server.name.toLowerCase().replace(/[^a-z0-9]/g, '-')} ${server.urls.sse}`;
    }
    if (server.urls.stdio) {
      const envFlags = server.authentication && server.authentication.envVars ? server.authentication.envVars.map(v => `--env ${v}=YOUR_${v.split('_').pop()}`).join(' ') : '';
      const baseCommand = `claude mcp add --transport stdio ${server.name.toLowerCase().replace(/[^a-z0-9]/g, '-')}`;
      return envFlags ? `${baseCommand} ${envFlags} -- ${server.urls.stdio}` : `${baseCommand} -- ${server.urls.stdio}`;
    }
    return null;
  };
  const servers = [{
    name: "Airtable",
    category: "Databases & Data Management",
    description: "Read/write records, manage bases and tables",
    documentation: "https://github.com/domdomegg/airtable-mcp-server",
    urls: {
      stdio: "npx -y airtable-mcp-server"
    },
    authentication: {
      type: "api_key",
      envVars: ["AIRTABLE_API_KEY"]
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: true
    }
  }, {
    name: "Figma",
    category: "Design & Media",
    description: "Generate better code by bringing in full Figma context",
    documentation: "https://developers.figma.com",
    urls: {
      http: "https://mcp.figma.com/mcp"
    },
    customCommands: {
      claudeCode: "claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    },
    notes: "Visit developers.figma.com for local server setup."
  }, {
    name: "Asana",
    category: "Project Management & Documentation",
    description: "Interact with your Asana workspace to keep projects on track",
    documentation: "https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server",
    urls: {
      sse: "https://mcp.asana.com/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Atlassian",
    category: "Project Management & Documentation",
    description: "Manage your Jira tickets and Confluence docs",
    documentation: "https://www.atlassian.com/platform/remote-mcp-server",
    urls: {
      sse: "https://mcp.atlassian.com/v1/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "ClickUp",
    category: "Project Management & Documentation",
    description: "Task management, project tracking",
    documentation: "https://github.com/hauptsacheNet/clickup-mcp",
    urls: {
      stdio: "npx -y @hauptsache.net/clickup-mcp"
    },
    authentication: {
      type: "api_key",
      envVars: ["CLICKUP_API_KEY", "CLICKUP_TEAM_ID"]
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: true
    }
  }, {
    name: "Cloudflare",
    category: "Infrastructure & DevOps",
    description: "Build applications, analyze traffic, monitor performance, and manage security settings through Cloudflare",
    documentation: "https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/",
    urls: {},
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "Multiple services available. See documentation for specific server URLs. Claude Code can use the Cloudflare CLI if installed."
  }, {
    name: "Cloudinary",
    category: "Design & Media",
    description: "Upload, manage, transform, and analyze your media assets",
    documentation: "https://cloudinary.com/documentation/cloudinary_llm_mcp#mcp_servers",
    urls: {},
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "Multiple services available. See documentation for specific server URLs."
  }, {
    name: "Intercom",
    category: "Project Management & Documentation",
    description: "Access real-time customer conversations, tickets, and user data",
    documentation: "https://developers.intercom.com/docs/guides/mcp",
    urls: {
      http: "https://mcp.intercom.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "invideo",
    category: "Design & Media",
    description: "Build video creation capabilities into your applications",
    documentation: "https://invideo.io/ai/mcp",
    urls: {
      sse: "https://mcp.invideo.io/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Linear",
    category: "Project Management & Documentation",
    description: "Integrate with Linear's issue tracking and project management",
    documentation: "https://linear.app/docs/mcp",
    urls: {
      http: "https://mcp.linear.app/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Notion",
    category: "Project Management & Documentation",
    description: "Read docs, update pages, manage tasks",
    documentation: "https://developers.notion.com/docs/mcp",
    urls: {
      http: "https://mcp.notion.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    }
  }, {
    name: "PayPal",
    category: "Payments & Commerce",
    description: "Integrate PayPal commerce capabilities, payment processing, transaction management",
    documentation: "https://www.paypal.ai/",
    urls: {
      http: "https://mcp.paypal.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Plaid",
    category: "Payments & Commerce",
    description: "Analyze, troubleshoot, and optimize Plaid integrations. Banking data, financial account linking",
    documentation: "https://plaid.com/blog/plaid-mcp-ai-assistant-claude/",
    urls: {
      sse: "https://api.dashboard.plaid.com/mcp/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Sentry",
    category: "Development & Testing Tools",
    description: "Monitor errors, debug production issues",
    documentation: "https://docs.sentry.io/product/sentry-mcp/",
    urls: {
      http: "https://mcp.sentry.dev/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    }
  }, {
    name: "Square",
    category: "Payments & Commerce",
    description: "Use an agent to build on Square APIs. Payments, inventory, orders, and more",
    documentation: "https://developer.squareup.com/docs/mcp",
    urls: {
      sse: "https://mcp.squareup.com/sse"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Socket",
    category: "Development & Testing Tools",
    description: "Security analysis for dependencies",
    documentation: "https://github.com/SocketDev/socket-mcp",
    urls: {
      http: "https://mcp.socket.dev/"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: false,
      claudeDesktop: false
    }
  }, {
    name: "Stripe",
    category: "Payments & Commerce",
    description: "Payment processing, subscription management, and financial transactions",
    documentation: "https://docs.stripe.com/mcp",
    urls: {
      http: "https://mcp.stripe.com"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Workato",
    category: "Automation & Integration",
    description: "Access any application, workflows or data via Workato, made accessible for AI",
    documentation: "https://docs.workato.com/mcp.html",
    urls: {},
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "MCP servers are programmatically generated"
  }, {
    name: "Zapier",
    category: "Automation & Integration",
    description: "Connect to nearly 8,000 apps through Zapier's automation platform",
    documentation: "https://help.zapier.com/hc/en-us/articles/36265392843917",
    urls: {},
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    },
    notes: "Generate a user-specific URL at mcp.zapier.com"
  }, {
    name: "Box",
    category: "Project Management & Documentation",
    description: "Ask questions about your enterprise content, get insights from unstructured data, automate content workflows",
    documentation: "https://box.dev/guides/box-mcp/remote/",
    urls: {
      http: "https://mcp.box.com/"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Canva",
    category: "Design & Media",
    description: "Browse, summarize, autofill, and even generate new Canva designs directly from Claude",
    documentation: "https://www.canva.dev/docs/connect/canva-mcp-server-setup/",
    urls: {
      http: "https://mcp.canva.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Daloopa",
    category: "Databases & Data Management",
    description: "Supplies high quality fundamental financial data sourced from SEC Filings, investor presentations",
    documentation: "https://docs.daloopa.com/docs/daloopa-mcp",
    urls: {
      http: "https://mcp.daloopa.com/server/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Fireflies",
    category: "Project Management & Documentation",
    description: "Extract valuable insights from meeting transcripts and summaries",
    documentation: "https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol",
    urls: {
      http: "https://api.fireflies.ai/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "HubSpot",
    category: "Databases & Data Management",
    description: "Access and manage HubSpot CRM data by fetching contacts, companies, and deals, and creating and updating records",
    documentation: "https://developers.hubspot.com/mcp",
    urls: {
      http: "https://mcp.hubspot.com/anthropic"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Hugging Face",
    category: "Development & Testing Tools",
    description: "Provides access to Hugging Face Hub information and Gradio AI Applications",
    documentation: "https://huggingface.co/settings/mcp",
    urls: {
      http: "https://huggingface.co/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Jam",
    category: "Development & Testing Tools",
    description: "Debug faster with AI agents that can access Jam recordings like video, console logs, network requests, and errors",
    documentation: "https://jam.dev/docs/debug-a-jam/mcp",
    urls: {
      http: "https://mcp.jam.dev/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Monday",
    category: "Project Management & Documentation",
    description: "Manage monday.com boards by creating items, updating columns, assigning owners, setting timelines, adding CRM activities, and writing summaries",
    documentation: "https://developer.monday.com/apps/docs/mondaycom-mcp-integration",
    urls: {
      http: "https://mcp.monday.com/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Netlify",
    category: "Infrastructure & DevOps",
    description: "Create, deploy, and manage websites on Netlify. Control all aspects of your site from creating secrets to enforcing access controls to aggregating form submissions",
    documentation: "https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/",
    urls: {
      http: "https://netlify-mcp.netlify.app/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Stytch",
    category: "Infrastructure & DevOps",
    description: "Configure and manage Stytch authentication services, redirect URLs, email templates, and workspace settings",
    documentation: "https://stytch.com/docs/workspace-management/stytch-mcp",
    urls: {
      http: "http://mcp.stytch.dev/mcp"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }, {
    name: "Vercel",
    category: "Infrastructure & DevOps",
    description: "Vercel's official MCP server, allowing you to search and navigate documentation, manage projects and deployments, and analyze deployment logs—all in one place",
    documentation: "https://vercel.com/docs/mcp/vercel-mcp",
    urls: {
      http: "https://mcp.vercel.com/"
    },
    authentication: {
      type: "oauth"
    },
    availability: {
      claudeCode: true,
      mcpConnector: true,
      claudeDesktop: false
    }
  }];
  const filteredServers = servers.filter(server => {
    if (platform === "claudeCode") {
      return server.availability.claudeCode;
    } else if (platform === "mcpConnector") {
      return server.availability.mcpConnector;
    } else if (platform === "claudeDesktop") {
      return server.availability.claudeDesktop;
    } else if (platform === "all") {
      return true;
    } else {
      throw new Error(`Unknown platform: ${platform}`);
    }
  });
  const serversByCategory = filteredServers.reduce((acc, server) => {
    if (!acc[server.category]) {
      acc[server.category] = [];
    }
    acc[server.category].push(server);
    return acc;
  }, {});
  const categoryOrder = ["Development & Testing Tools", "Project Management & Documentation", "Databases & Data Management", "Payments & Commerce", "Design & Media", "Infrastructure & DevOps", "Automation & Integration"];
  return <>
      <style jsx>{`
        .cards-container {
          display: grid;
          gap: 1rem;
          margin-bottom: 2rem;
        }
        .server-card {
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 6px;
          padding: 1rem;
        }
        .command-row {
          display: flex;
          align-items: center;
          gap: 0.25rem;
        }
        .command-row code {
          font-size: 0.75rem;
          overflow-x: auto;
        }
      `}</style>
      
      {categoryOrder.map(category => {
    if (!serversByCategory[category]) return null;
    return <div key={category}>
            <h3>{category}</h3>
            <div className="cards-container">
              {serversByCategory[category].map(server => {
      const claudeCodeCommand = generateClaudeCodeCommand(server);
      const mcpUrl = server.urls.http || server.urls.sse;
      const commandToShow = platform === "claudeCode" ? claudeCodeCommand : mcpUrl;
      return <div key={server.name} className="server-card">
                    <div>
                      {server.documentation ? <a href={server.documentation}>
                          <strong>{server.name}</strong>
                        </a> : <strong>{server.name}</strong>}
                    </div>
                    
                    <p style={{
        margin: '0.5rem 0',
        fontSize: '0.9rem'
      }}>
                      {server.description}
                      {server.notes && <span style={{
        display: 'block',
        marginTop: '0.25rem',
        fontSize: '0.8rem',
        fontStyle: 'italic',
        opacity: 0.7
      }}>
                          {server.notes}
                        </span>}
                    </p>
                    
                    {commandToShow && <>
                      <p style={{
        display: 'block',
        fontSize: '0.75rem',
        fontWeight: 500,
        minWidth: 'fit-content',
        marginTop: '0.5rem',
        marginBottom: 0
      }}>
                        {platform === "claudeCode" ? "Command" : "URL"}
                      </p>
                      <div className="command-row">
                        <code>
                          {commandToShow}
                        </code>
                      </div>
                    </>}
                  </div>;
    })}
            </div>
          </div>;
  })}
    </>;
};

Claude Code can connect to hundreds of external tools and data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open-source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs.

## What you can do with MCP

With MCP servers connected, you can ask Claude Code to:

* **Implement features from issue trackers**: "Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub."
* **Analyze monitoring data**: "Check Sentry and Statsig to check the usage of the feature described in ENG-4521."
* **Query databases**: "Find emails of 10 random users who used feature ENG-4521, based on our Postgres database."
* **Integrate designs**: "Update our standard email template based on the new Figma designs that were posted in Slack"
* **Automate workflows**: "Create Gmail drafts inviting these 10 users to a feedback session about the new feature."

## Popular MCP servers

Here are some commonly used MCP servers you can connect to Claude Code:

<Warning>
  Use third party MCP servers at your own risk - Anthropic has not verified
  the correctness or security of all these servers.
  Make sure you trust MCP servers you are installing.
  Be especially careful when using MCP servers that could fetch untrusted
  content, as these can expose you to prompt injection risk.
</Warning>

<MCPServersTable platform="claudeCode" />

<Note>
  **Need a specific integration?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers), or build your own using the [MCP SDK](https://modelcontextprotocol.io/quickstart/server).
</Note>

## Installing MCP servers

MCP servers can be configured in three different ways depending on your needs:

### Option 1: Add a remote HTTP server

HTTP servers are the recommended option for connecting to remote MCP servers. This is the most widely supported transport for cloud-based services.

```bash  theme={null}
# Basic syntax
claude mcp add --transport http <name> <url>

# Real example: Connect to Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Example with Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Option 2: Add a remote SSE server

<Warning>
  The SSE (Server-Sent Events) transport is deprecated. Use HTTP servers instead, where available.
</Warning>

```bash  theme={null}
# Basic syntax
claude mcp add --transport sse <name> <url>

# Real example: Connect to Asana
claude mcp add --transport sse asana https://mcp.asana.com/sse

# Example with authentication header
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"
```

### Option 3: Add a local stdio server

Stdio servers run as local processes on your machine. They're ideal for tools that need direct system access or custom scripts.

```bash  theme={null}
# Basic syntax
claude mcp add --transport stdio <name> <command> [args...]

# Real example: Add Airtable server
claude mcp add --transport stdio airtable --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server
```

<Note>
  **Understanding the "--" parameter:**
  The `--` (double dash) separates Claude's own CLI flags from the command and arguments that get passed to the MCP server. Everything before `--` are options for Claude (like `--env`, `--scope`), and everything after `--` is the actual command to run the MCP server.

  For example:

  * `claude mcp add --transport stdio myserver -- npx server` → runs `npx server`
  * `claude mcp add --transport stdio myserver --env KEY=value -- python server.py --port 8080` → runs `python server.py --port 8080` with `KEY=value` in environment

  This prevents conflicts between Claude's flags and the server's flags.
</Note>

### Managing your servers

Once configured, you can manage your MCP servers with these commands:

```bash  theme={null}
# List all configured servers
claude mcp list

# Get details for a specific server
claude mcp get github

# Remove a server
claude mcp remove github

# (within Claude Code) Check server status
/mcp
```

<Tip>
  Tips:

  * Use the `--scope` flag to specify where the configuration is stored:
    * `local` (default): Available only to you in the current project (was called `project` in older versions)
    * `project`: Shared with everyone in the project via `.mcp.json` file
    * `user`: Available to you across all projects (was called `global` in older versions)
  * Set environment variables with `--env` flags (e.g., `--env KEY=value`)
  * Configure MCP server startup timeout using the MCP\_TIMEOUT environment variable (e.g., `MCP_TIMEOUT=10000 claude` sets a 10-second timeout)
  * Claude Code will display a warning when MCP tool output exceeds 10,000 tokens. To increase this limit, set the `MAX_MCP_OUTPUT_TOKENS` environment variable (e.g., `MAX_MCP_OUTPUT_TOKENS=50000`)
  * Use `/mcp` to authenticate with remote servers that require OAuth 2.0 authentication
</Tip>

<Warning>
  **Windows Users**: On native Windows (not WSL), local MCP servers that use `npx` require the `cmd /c` wrapper to ensure proper execution.

  ```bash  theme={null}
  # This creates command="cmd" which Windows can execute
  claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
  ```

  Without the `cmd /c` wrapper, you'll encounter "Connection closed" errors because Windows cannot directly execute `npx`. (See the note above for an explanation of the `--` parameter.)
</Warning>

### Plugin-provided MCP servers

[Plugins](/en/plugins) can bundle MCP servers, automatically providing tools and integrations when the plugin is enabled. Plugin MCP servers work identically to user-configured servers.

**How plugin MCP servers work**:

* Plugins define MCP servers in `.mcp.json` at the plugin root or inline in `plugin.json`
* When a plugin is enabled, its MCP servers start automatically
* Plugin MCP tools appear alongside manually configured MCP tools
* Plugin servers are managed through plugin installation (not `/mcp` commands)

**Example plugin MCP configuration**:

In `.mcp.json` at plugin root:

```json  theme={null}
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```

Or inline in `plugin.json`:

```json  theme={null}
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```

**Plugin MCP features**:

* **Automatic lifecycle**: Servers start when plugin enables, but you must restart Claude Code to apply MCP server changes (enabling or disabling)
* **Environment variables**: Use `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths
* **User environment access**: Access to same environment variables as manually configured servers
* **Multiple transport types**: Support stdio, SSE, and HTTP transports (transport support may vary by server)

**Viewing plugin MCP servers**:

```bash  theme={null}
# Within Claude Code, see all MCP servers including plugin ones
/mcp
```

Plugin servers appear in the list with indicators showing they come from plugins.

**Benefits of plugin MCP servers**:

* **Bundled distribution**: Tools and servers packaged together
* **Automatic setup**: No manual MCP configuration needed
* **Team consistency**: Everyone gets the same tools when plugin is installed

See the [plugin components reference](/en/plugins-reference#mcp-servers) for details on bundling MCP servers with plugins.

## MCP installation scopes

MCP servers can be configured at three different scope levels, each serving distinct purposes for managing server accessibility and sharing. Understanding these scopes helps you determine the best way to configure servers for your specific needs.

### Local scope

Local-scoped servers represent the default configuration level and are stored in your project-specific user settings. These servers remain private to you and are only accessible when working within the current project directory. This scope is ideal for personal development servers, experimental configurations, or servers containing sensitive credentials that shouldn't be shared.

```bash  theme={null}
# Add a local-scoped server (default)
claude mcp add --transport http stripe https://mcp.stripe.com

# Explicitly specify local scope
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

### Project scope

Project-scoped servers enable team collaboration by storing configurations in a `.mcp.json` file at your project's root directory. This file is designed to be checked into version control, ensuring all team members have access to the same MCP tools and services. When you add a project-scoped server, Claude Code automatically creates or updates this file with the appropriate configuration structure.

```bash  theme={null}
# Add a project-scoped server
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp
```

The resulting `.mcp.json` file follows a standardized format:

```json  theme={null}
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

For security reasons, Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files. If you need to reset these approval choices, use the `claude mcp reset-project-choices` command.

### User scope

User-scoped servers provide cross-project accessibility, making them available across all projects on your machine while remaining private to your user account. This scope works well for personal utility servers, development tools, or services you frequently use across different projects.

```bash  theme={null}
# Add a user server
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### Choosing the right scope

Select your scope based on:

* **Local scope**: Personal servers, experimental configurations, or sensitive credentials specific to one project
* **Project scope**: Team-shared servers, project-specific tools, or services required for collaboration
* **User scope**: Personal utilities needed across multiple projects, development tools, or frequently-used services

### Scope hierarchy and precedence

MCP server configurations follow a clear precedence hierarchy. When servers with the same name exist at multiple scopes, the system resolves conflicts by prioritizing local-scoped servers first, followed by project-scoped servers, and finally user-scoped servers. This design ensures that personal configurations can override shared ones when needed.

### Environment variable expansion in `.mcp.json`

Claude Code supports environment variable expansion in `.mcp.json` files, allowing teams to share configurations while maintaining flexibility for machine-specific paths and sensitive values like API keys.

**Supported syntax:**

* `${VAR}` - Expands to the value of environment variable `VAR`
* `${VAR:-default}` - Expands to `VAR` if set, otherwise uses `default`

**Expansion locations:**
Environment variables can be expanded in:

* `command` - The server executable path
* `args` - Command-line arguments
* `env` - Environment variables passed to the server
* `url` - For HTTP server types
* `headers` - For HTTP server authentication

**Example with variable expansion:**

```json  theme={null}
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

If a required environment variable is not set and has no default value, Claude Code will fail to parse the config.

## Practical examples

{/* ### Example: Automate browser testing with Playwright

  ```bash
  # 1. Add the Playwright MCP server
  claude mcp add --transport stdio playwright -- npx -y @playwright/mcp@latest

  # 2. Write and run browser tests
  > "Test if the login flow works with test@example.com"
  > "Take a screenshot of the checkout page on mobile"
  > "Verify that the search feature returns results"
  ``` */}

### Example: Monitor errors with Sentry

```bash  theme={null}
# 1. Add the Sentry MCP server
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 2. Use /mcp to authenticate with your Sentry account
> /mcp

# 3. Debug production issues
> "What are the most common errors in the last 24 hours?"
> "Show me the stack trace for error ID abc123"
> "Which deployment introduced these new errors?"
```

### Example: Connect to GitHub for code reviews

```bash  theme={null}
# 1. Add the GitHub MCP server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/

# 2. In Claude Code, authenticate if needed
> /mcp
# Select "Authenticate" for GitHub

# 3. Now you can ask Claude to work with GitHub
> "Review PR #456 and suggest improvements"
> "Create a new issue for the bug we just found"
> "Show me all open PRs assigned to me"
```

### Example: Query your PostgreSQL database

```bash  theme={null}
# 1. Add the database server with your connection string
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"

# 2. Query your database naturally
> "What's our total revenue this month?"
> "Show me the schema for the orders table"
> "Find customers who haven't made a purchase in 90 days"
```

## Authenticate with remote MCP servers

Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections.

<Steps>
  <Step title="Add the server that requires authentication">
    For example:

    ```bash  theme={null}
    claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
    ```
  </Step>

  <Step title="Use the /mcp command within Claude Code">
    In Claude code, use the command:

    ```
    > /mcp
    ```

    Then follow the steps in your browser to login.
  </Step>
</Steps>

<Tip>
  Tips:

  * Authentication tokens are stored securely and refreshed automatically
  * Use "Clear authentication" in the `/mcp` menu to revoke access
  * If your browser doesn't open automatically, copy the provided URL
  * OAuth authentication works with HTTP servers
</Tip>

## Add MCP servers from JSON configuration

If you have a JSON configuration for an MCP server, you can add it directly:

<Steps>
  <Step title="Add an MCP server from JSON">
    ```bash  theme={null}
    # Basic syntax
    claude mcp add-json <name> '<json>'

    # Example: Adding an HTTP server with JSON configuration
    claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

    # Example: Adding a stdio server with JSON configuration
    claude mcp add-json local-weather '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'
    ```
  </Step>

  <Step title="Verify the server was added">
    ```bash  theme={null}
    claude mcp get weather-api
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Make sure the JSON is properly escaped in your shell
  * The JSON must conform to the MCP server configuration schema
  * You can use `--scope user` to add the server to your user configuration instead of the project-specific one
</Tip>

## Import MCP servers from Claude Desktop

If you've already configured MCP servers in Claude Desktop, you can import them:

<Steps>
  <Step title="Import servers from Claude Desktop">
    ```bash  theme={null}
    # Basic syntax 
    claude mcp add-from-claude-desktop 
    ```
  </Step>

  <Step title="Select which servers to import">
    After running the command, you'll see an interactive dialog that allows you to select which servers you want to import.
  </Step>

  <Step title="Verify the servers were imported">
    ```bash  theme={null}
    claude mcp list 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * This feature only works on macOS and Windows Subsystem for Linux (WSL)
  * It reads the Claude Desktop configuration file from its standard location on those platforms
  * Use the `--scope user` flag to add servers to your user configuration
  * Imported servers will have the same names as in Claude Desktop
  * If servers with the same names already exist, they will get a numerical suffix (e.g., `server_1`)
</Tip>

## Use Claude Code as an MCP server

You can use Claude Code itself as an MCP server that other applications can connect to:

```bash  theme={null}
# Start Claude as a stdio MCP server
claude mcp serve
```

You can use this in Claude Desktop by adding this configuration to claude\_desktop\_config.json:

```json  theme={null}
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

<Warning>
  **Configuring the executable path**: The `command` field must reference the Claude Code executable. If the `claude` command is not in your system's PATH, you'll need to specify the full path to the executable.

  To find the full path:

  ```bash  theme={null}
  which claude
  ```

  Then use the full path in your configuration:

  ```json  theme={null}
  {
    "mcpServers": {
      "claude-code": {
        "type": "stdio",
        "command": "/full/path/to/claude",
        "args": ["mcp", "serve"],
        "env": {}
      }
    }
  }
  ```

  Without the correct executable path, you'll encounter errors like `spawn claude ENOENT`.
</Warning>

<Tip>
  Tips:

  * The server provides access to Claude's tools like View, Edit, LS, etc.
  * In Claude Desktop, try asking Claude to read files in a directory, make edits, and more.
  * Note that this MCP server is simply exposing Claude Code's tools to your MCP client, so your own client is responsible for implementing user confirmation for individual tool calls.
</Tip>

## MCP output limits and warnings

When MCP tools produce large outputs, Claude Code helps manage the token usage to prevent overwhelming your conversation context:

* **Output warning threshold**: Claude Code displays a warning when any MCP tool output exceeds 10,000 tokens
* **Configurable limit**: You can adjust the maximum allowed MCP output tokens using the `MAX_MCP_OUTPUT_TOKENS` environment variable
* **Default limit**: The default maximum is 25,000 tokens

To increase the limit for tools that produce large outputs:

```bash  theme={null}
# Set a higher limit for MCP tool outputs
export MAX_MCP_OUTPUT_TOKENS=50000
claude
```

This is particularly useful when working with MCP servers that:

* Query large datasets or databases
* Generate detailed reports or documentation
* Process extensive log files or debugging information

<Warning>
  If you frequently encounter output warnings with specific MCP servers, consider increasing the limit or configuring the server to paginate or filter its responses.
</Warning>

## Use MCP resources

MCP servers can expose resources that you can reference using @ mentions, similar to how you reference files.

### Reference MCP resources

<Steps>
  <Step title="List available resources">
    Type `@` in your prompt to see available resources from all connected MCP servers. Resources appear alongside files in the autocomplete menu.
  </Step>

  <Step title="Reference a specific resource">
    Use the format `@server:protocol://resource/path` to reference a resource:

    ```
    > Can you analyze @github:issue://123 and suggest a fix?
    ```

    ```
    > Please review the API documentation at @docs:file://api/authentication
    ```
  </Step>

  <Step title="Multiple resource references">
    You can reference multiple resources in a single prompt:

    ```
    > Compare @postgres:schema://users with @docs:file://database/user-model
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Resources are automatically fetched and included as attachments when referenced
  * Resource paths are fuzzy-searchable in the @ mention autocomplete
  * Claude Code automatically provides tools to list and read MCP resources when servers support them
  * Resources can contain any type of content that the MCP server provides (text, JSON, structured data, etc.)
</Tip>

## Use MCP prompts as slash commands

MCP servers can expose prompts that become available as slash commands in Claude Code.

### Execute MCP prompts

<Steps>
  <Step title="Discover available prompts">
    Type `/` to see all available commands, including those from MCP servers. MCP prompts appear with the format `/mcp__servername__promptname`.
  </Step>

  <Step title="Execute a prompt without arguments">
    ```
    > /mcp__github__list_prs
    ```
  </Step>

  <Step title="Execute a prompt with arguments">
    Many prompts accept arguments. Pass them space-separated after the command:

    ```
    > /mcp__github__pr_review 456
    ```

    ```
    > /mcp__jira__create_issue "Bug in login flow" high
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * MCP prompts are dynamically discovered from connected servers
  * Arguments are parsed based on the prompt's defined parameters
  * Prompt results are injected directly into the conversation
  * Server and prompt names are normalized (spaces become underscores)
</Tip>

## Enterprise MCP configuration

For organizations that need centralized control over MCP servers, Claude Code supports enterprise-managed MCP configurations. This allows IT administrators to:

* **Control which MCP servers employees can access**: Deploy a standardized set of approved MCP servers across the organization
* **Prevent unauthorized MCP servers**: Optionally restrict users from adding their own MCP servers
* **Disable MCP entirely**: Remove MCP functionality completely if needed

### Setting up enterprise MCP configuration

System administrators can deploy an enterprise MCP configuration file alongside the managed settings file:

* **macOS**: `/Library/Application Support/ClaudeCode/managed-mcp.json`
* **Windows**: `C:\ProgramData\ClaudeCode\managed-mcp.json`
* **Linux**: `/etc/claude-code/managed-mcp.json`

The `managed-mcp.json` file uses the same format as a standard `.mcp.json` file:

```json  theme={null}
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"],
      "env": {
        "COMPANY_API_URL": "https://internal.company.com"
      }
    }
  }
}
```

### Restricting MCP servers with allowlists and denylists

In addition to providing enterprise-managed servers, administrators can control which MCP servers users are allowed to configure using `allowedMcpServers` and `deniedMcpServers` in the `managed-settings.json` file:

* **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
* **Windows**: `C:\ProgramData\ClaudeCode\managed-settings.json`
* **Linux**: `/etc/claude-code/managed-settings.json`

```json  theme={null}
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "sentry" },
    { "serverName": "company-internal" }
  ],
  "deniedMcpServers": [
    { "serverName": "filesystem" }
  ]
}
```

**Allowlist behavior (`allowedMcpServers`)**:

* `undefined` (default): No restrictions - users can configure any MCP server
* Empty array `[]`: Complete lockdown - users cannot configure any MCP servers
* List of server names: Users can only configure the specified servers

**Denylist behavior (`deniedMcpServers`)**:

* `undefined` (default): No servers are blocked
* Empty array `[]`: No servers are blocked
* List of server names: Specified servers are explicitly blocked across all scopes

**Important notes**:

* These restrictions apply to all scopes: user, project, local, and even enterprise servers from `managed-mcp.json`
* **Denylist takes absolute precedence**: If a server appears in both lists, it will be blocked

<Note>
  **Enterprise configuration precedence**: The enterprise MCP configuration has the highest precedence and cannot be overridden by user, local, or project configurations.
</Note>


# Plugin marketplaces
Source: https://code.claude.com/docs/en/plugin-marketplaces

Create and manage plugin marketplaces to distribute Claude Code extensions across teams and communities.

Plugin marketplaces are catalogs of available plugins that make it easy to discover, install, and manage Claude Code extensions. This guide shows you how to use existing marketplaces and create your own for team distribution.

## Overview

A marketplace is a JSON file that lists available plugins and describes where to find them. Marketplaces provide:

* **Centralized discovery**: Browse plugins from multiple sources in one place
* **Version management**: Track and update plugin versions automatically
* **Team distribution**: Share required plugins across your organization
* **Flexible sources**: Support for git repositories, GitHub repos, local paths, and package managers

### Prerequisites

* Claude Code installed and running
* Basic familiarity with JSON file format
* For creating marketplaces: Git repository or local development environment

## Add and use marketplaces

Add marketplaces using the `/plugin marketplace` commands to access plugins from different sources:

### Add GitHub marketplaces

```shell Add a GitHub repository containing .claude-plugin/marketplace.json theme={null}
/plugin marketplace add owner/repo
```

### Add Git repositories

```shell Add any git repository theme={null}
/plugin marketplace add https://gitlab.com/company/plugins.git
```

### Add local marketplaces for development

```shell Add local directory containing .claude-plugin/marketplace.json theme={null}
/plugin marketplace add ./my-marketplace
```

```shell Add direct path to marketplace.json file theme={null}
/plugin marketplace add ./path/to/marketplace.json
```

```shell Add remote marketplace.json via URL theme={null}
/plugin marketplace add https://url.of/marketplace.json
```

### Install plugins from marketplaces

Once you've added marketplaces, install plugins directly:

```shell Install from any known marketplace theme={null}
/plugin install plugin-name@marketplace-name
```

```shell Browse available plugins interactively theme={null}
/plugin
```

### Verify marketplace installation

After adding a marketplace:

1. **List marketplaces**: Run `/plugin marketplace list` to confirm it's added
2. **Browse plugins**: Use `/plugin` to see available plugins from your marketplace
3. **Test installation**: Try installing a plugin to verify the marketplace works correctly

## Configure team marketplaces

Set up automatic marketplace installation for team projects by specifying required marketplaces in `.claude/settings.json`:

```json  theme={null}
{
  "extraKnownMarketplaces": {
    "team-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    },
    "project-specific": {
      "source": {
        "source": "git",
        "url": "https://git.company.com/project-plugins.git"
      }
    }
  }
}
```

When team members trust the repository folder, Claude Code automatically installs these marketplaces and any plugins specified in the `enabledPlugins` field.

***

## Create your own marketplace

Build and distribute custom plugin collections for your team or community.

### Prerequisites for marketplace creation

* Git repository (GitHub, GitLab, or other git hosting)
* Understanding of JSON file format
* One or more plugins to distribute

### Create the marketplace file

Create `.claude-plugin/marketplace.json` in your repository root:

```json  theme={null}
{
  "name": "company-tools",
  "owner": {
    "name": "DevTools Team",
    "email": "devtools@company.com"
  },
  "plugins": [
    {
      "name": "code-formatter",
      "source": "./plugins/formatter",
      "description": "Automatic code formatting on save",
      "version": "2.1.0",
      "author": {
        "name": "DevTools Team"
      }
    },
    {
      "name": "deployment-tools",
      "source": {
        "source": "github",
        "repo": "company/deploy-plugin"
      },
      "description": "Deployment automation tools"
    }
  ]
}
```

### Marketplace schema

#### Required fields

| Field     | Type   | Description                                    |
| :-------- | :----- | :--------------------------------------------- |
| `name`    | string | Marketplace identifier (kebab-case, no spaces) |
| `owner`   | object | Marketplace maintainer information             |
| `plugins` | array  | List of available plugins                      |

#### Optional metadata

| Field                  | Type   | Description                           |
| :--------------------- | :----- | :------------------------------------ |
| `metadata.description` | string | Brief marketplace description         |
| `metadata.version`     | string | Marketplace version                   |
| `metadata.pluginRoot`  | string | Base path for relative plugin sources |

### Plugin entries

<Note>
  Plugin entries are based on the *plugin manifest schema* (with all fields made optional) plus marketplace-specific fields (`source`, `category`, `tags`, `strict`), with `name` being required.
</Note>

**Required fields:**

| Field    | Type           | Description                               |
| :------- | :------------- | :---------------------------------------- |
| `name`   | string         | Plugin identifier (kebab-case, no spaces) |
| `source` | string\|object | Where to fetch the plugin from            |

#### Optional plugin fields

**Standard metadata fields:**

| Field         | Type    | Description                                                       |
| :------------ | :------ | :---------------------------------------------------------------- |
| `description` | string  | Brief plugin description                                          |
| `version`     | string  | Plugin version                                                    |
| `author`      | object  | Plugin author information                                         |
| `homepage`    | string  | Plugin homepage or documentation URL                              |
| `repository`  | string  | Source code repository URL                                        |
| `license`     | string  | SPDX license identifier (e.g., MIT, Apache-2.0)                   |
| `keywords`    | array   | Tags for plugin discovery and categorization                      |
| `category`    | string  | Plugin category for organization                                  |
| `tags`        | array   | Tags for searchability                                            |
| `strict`      | boolean | Require plugin.json in plugin folder (default: true) <sup>1</sup> |

**Component configuration fields:**

| Field        | Type           | Description                                      |
| :----------- | :------------- | :----------------------------------------------- |
| `commands`   | string\|array  | Custom paths to command files or directories     |
| `agents`     | string\|array  | Custom paths to agent files                      |
| `hooks`      | string\|object | Custom hooks configuration or path to hooks file |
| `mcpServers` | string\|object | MCP server configurations or path to MCP config  |

*<sup>1 - When `strict: true` (default), the plugin must include a `plugin.json` manifest file, and marketplace fields supplement those values. When `strict: false`, the plugin.json is optional. If it's missing, the marketplace entry serves as the complete plugin manifest.</sup>*

### Plugin sources

#### Relative paths

For plugins in the same repository:

```json  theme={null}
{
  "name": "my-plugin",
  "source": "./plugins/my-plugin"
}
```

#### GitHub repositories

```json  theme={null}
{
  "name": "github-plugin",
  "source": {
    "source": "github",
    "repo": "owner/plugin-repo"
  }
}
```

#### Git repositories

```json  theme={null}
{
  "name": "git-plugin",
  "source": {
    "source": "url",
    "url": "https://gitlab.com/team/plugin.git"
  }
}
```

#### Advanced plugin entries

Plugin entries can override default component locations and provide additional metadata. Note that `${CLAUDE_PLUGIN_ROOT}` is an environment variable that resolves to the plugin's installation directory (for details see [Environment variables](/en/plugins-reference#environment-variables)):

```json  theme={null}
{
  "name": "enterprise-tools",
  "source": {
    "source": "github",
    "repo": "company/enterprise-plugin"
  },
  "description": "Enterprise workflow automation tools",
  "version": "2.1.0",
  "author": {
    "name": "Enterprise Team",
    "email": "enterprise@company.com"
  },
  "homepage": "https://docs.company.com/plugins/enterprise-tools",
  "repository": "https://github.com/company/enterprise-plugin",
  "license": "MIT",
  "keywords": ["enterprise", "workflow", "automation"],
  "category": "productivity",
  "commands": [
    "./commands/core/",
    "./commands/enterprise/",
    "./commands/experimental/preview.md"
  ],
  "agents": [
    "./agents/security-reviewer.md",
    "./agents/compliance-checker.md"
  ],
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"}]
      }
    ]
  },
  "mcpServers": {
    "enterprise-db": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"]
    }
  },
  "strict": false
}
```

<Note>
  **Schema relationship**: Plugin entries use the plugin manifest schema with all fields made optional, plus marketplace-specific fields (`source`, `strict`, `category`, `tags`). This means any field valid in a `plugin.json` file can also be used in a marketplace entry. When `strict: false`, the marketplace entry serves as the complete plugin manifest if no `plugin.json` exists. When `strict: true` (default), marketplace fields supplement the plugin's own manifest file.
</Note>

***

## Host and distribute marketplaces

Choose the best hosting strategy for your plugin distribution needs.

### Host on GitHub (recommended)

GitHub provides the easiest distribution method:

1. **Create a repository**: Set up a new repository for your marketplace
2. **Add marketplace file**: Create `.claude-plugin/marketplace.json` with your plugin definitions
3. **Share with teams**: Team members add with `/plugin marketplace add owner/repo`

**Benefits**: Built-in version control, issue tracking, and team collaboration features.

### Host on other git services

Any git hosting service works for marketplace distribution, using a URL to an arbitrary git repository.

For example, using GitLab:

```shell  theme={null}
/plugin marketplace add https://gitlab.com/company/plugins.git
```

### Use local marketplaces for development

Test your marketplace locally before distribution:

```shell Add local marketplace for testing theme={null}
/plugin marketplace add ./my-local-marketplace
```

```shell Test plugin installation theme={null}
/plugin install test-plugin@my-local-marketplace
```

## Manage marketplace operations

### List known marketplaces

```shell List all configured marketplaces theme={null}
/plugin marketplace list
```

Shows all configured marketplaces with their sources and status.

### Update marketplace metadata

```shell Refresh marketplace metadata theme={null}
/plugin marketplace update marketplace-name
```

Refreshes plugin listings and metadata from the marketplace source.

### Remove a marketplace

```shell Remove a marketplace theme={null}
/plugin marketplace remove marketplace-name
```

Removes the marketplace from your configuration.

<Warning>
  Removing a marketplace will uninstall any plugins you installed from it.
</Warning>

***

## Troubleshooting marketplaces

### Common marketplace issues

#### Marketplace not loading

**Symptoms**: Can't add marketplace or see plugins from it

**Solutions**:

* Verify the marketplace URL is accessible
* Check that `.claude-plugin/marketplace.json` exists at the specified path
* Ensure JSON syntax is valid using `claude plugin validate`
* For private repositories, confirm you have access permissions

#### Plugin installation failures

**Symptoms**: Marketplace appears but plugin installation fails

**Solutions**:

* Verify plugin source URLs are accessible
* Check that plugin directories contain required files
* For GitHub sources, ensure repositories are public or you have access
* Test plugin sources manually by cloning/downloading

### Validation and testing

Test your marketplace before sharing:

```bash Validate marketplace JSON syntax theme={null}
claude plugin validate .
```

```shell Add marketplace for testing theme={null}
/plugin marketplace add ./path/to/marketplace
```

```shell Install test plugin theme={null}
/plugin install test-plugin@marketplace-name
```

For complete plugin testing workflows, see [Test your plugins locally](/en/plugins#test-your-plugins-locally). For technical troubleshooting, see [Plugins reference](/en/plugins-reference).

***

## Next steps

### For marketplace users

* **Discover community marketplaces**: Search GitHub for Claude Code plugin collections
* **Contribute feedback**: Report issues and suggest improvements to marketplace maintainers
* **Share useful marketplaces**: Help your team discover valuable plugin collections

### For marketplace creators

* **Build plugin collections**: Create themed marketplace around specific use cases
* **Establish versioning**: Implement clear versioning and update policies
* **Community engagement**: Gather feedback and maintain active marketplace communities
* **Documentation**: Provide clear README files explaining your marketplace contents

### For organizations

* **Private marketplaces**: Set up internal marketplaces for proprietary tools
* **Governance policies**: Establish guidelines for plugin approval and security review
* **Training resources**: Help teams discover and adopt useful plugins effectively

## See also

* [Plugins](/en/plugins) - Installing and using plugins
* [Plugins reference](/en/plugins-reference) - Complete technical specifications and schemas
* [Plugin development](/en/plugins#develop-more-complex-plugins) - Creating your own plugins
* [Settings](/en/settings#plugin-configuration) - Plugin configuration options


# Plugins
Source: https://code.claude.com/docs/en/plugins

Extend Claude Code with custom commands, agents, hooks, Skills, and MCP servers through the plugin system.

<Tip>
  For complete technical specifications and schemas, see [Plugins reference](/en/plugins-reference). For marketplace management, see [Plugin marketplaces](/en/plugin-marketplaces).
</Tip>

Plugins let you extend Claude Code with custom functionality that can be shared across projects and teams. Install plugins from [marketplaces](/en/plugin-marketplaces) to add pre-built commands, agents, hooks, Skills, and MCP servers, or create your own to automate your workflows.

## Quickstart

Let's create a simple greeting plugin to get you familiar with the plugin system. We'll build a working plugin that adds a custom command, test it locally, and understand the core concepts.

### Prerequisites

* Claude Code installed on your machine
* Basic familiarity with command-line tools

### Create your first plugin

<Steps>
  <Step title="Create the marketplace structure">
    ```bash  theme={null}
    mkdir test-marketplace
    cd test-marketplace
    ```
  </Step>

  <Step title="Create the plugin directory">
    ```bash  theme={null}
    mkdir my-first-plugin
    cd my-first-plugin
    ```
  </Step>

  <Step title="Create the plugin manifest">
    ```bash Create .claude-plugin/plugin.json theme={null}
    mkdir .claude-plugin
    cat > .claude-plugin/plugin.json << 'EOF'
    {
    "name": "my-first-plugin",
    "description": "A simple greeting plugin to learn the basics",
    "version": "1.0.0",
    "author": {
    "name": "Your Name"
    }
    }
    EOF
    ```
  </Step>

  <Step title="Add a custom command">
    ```bash Create commands/hello.md theme={null}
    mkdir commands
    cat > commands/hello.md << 'EOF'
    ---
    description: Greet the user with a personalized message
    ---

    # Hello Command

    Greet the user warmly and ask how you can help them today. Make the greeting personal and encouraging.
    EOF
    ```
  </Step>

  <Step title="Create the marketplace manifest">
    ```bash Create marketplace.json theme={null}
    cd ..
    mkdir .claude-plugin
    cat > .claude-plugin/marketplace.json << 'EOF'
    {
    "name": "test-marketplace",
    "owner": {
    "name": "Test User"
    },
    "plugins": [
    {
      "name": "my-first-plugin",
      "source": "./my-first-plugin",
      "description": "My first test plugin"
    }
    ]
    }
    EOF
    ```
  </Step>

  <Step title="Install and test your plugin">
    ```bash Start Claude Code from parent directory theme={null}
    cd ..
    claude
    ```

    ```shell Add the test marketplace theme={null}
    /plugin marketplace add ./test-marketplace
    ```

    ```shell Install your plugin theme={null}
    /plugin install my-first-plugin@test-marketplace
    ```

    Select "Install now". You'll then need to restart Claude Code in order to use the new plugin.

    ```shell Try your new command theme={null}
    /hello
    ```

    You'll see Claude use your greeting command! Check `/help` to see your new command listed.
  </Step>
</Steps>

You've successfully created and tested a plugin with these key components:

* **Plugin manifest** (`.claude-plugin/plugin.json`) - Describes your plugin's metadata
* **Commands directory** (`commands/`) - Contains your custom slash commands
* **Test marketplace** - Allows you to test your plugin locally

### Plugin structure overview

Your plugin follows this basic structure:

```
my-first-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                 # Custom slash commands (optional)
│   └── hello.md
├── agents/                   # Custom agents (optional)
│   └── helper.md
├── skills/                   # Agent Skills (optional)
│   └── my-skill/
│       └── SKILL.md
└── hooks/                    # Event handlers (optional)
    └── hooks.json
```

**Additional components you can add:**

* **Commands**: Create markdown files in `commands/` directory
* **Agents**: Create agent definitions in `agents/` directory
* **Skills**: Create `SKILL.md` files in `skills/` directory
* **Hooks**: Create `hooks/hooks.json` for event handling
* **MCP servers**: Create `.mcp.json` for external tool integration

<Note>
  **Next steps**: Ready to add more features? Jump to [Develop more complex plugins](#develop-more-complex-plugins) to add agents, hooks, and MCP servers. For complete technical specifications of all plugin components, see [Plugins reference](/en/plugins-reference).
</Note>

***

## Install and manage plugins

Learn how to discover, install, and manage plugins to extend your Claude Code capabilities.

### Prerequisites

* Claude Code installed and running
* Basic familiarity with command-line interfaces

### Add marketplaces

Marketplaces are catalogs of available plugins. Add them to discover and install plugins:

```shell Add a marketplace theme={null}
/plugin marketplace add your-org/claude-plugins
```

```shell Browse available plugins theme={null}
/plugin
```

For detailed marketplace management including Git repositories, local development, and team distribution, see [Plugin marketplaces](/en/plugin-marketplaces).

### Install plugins

#### Via interactive menu (recommended for discovery)

```shell Open the plugin management interface theme={null}
/plugin
```

Select "Browse Plugins" to see available options with descriptions, features, and installation options.

#### Via direct commands (for quick installation)

```shell Install a specific plugin theme={null}
/plugin install formatter@your-org
```

```shell Enable a disabled plugin theme={null}
/plugin enable plugin-name@marketplace-name
```

```shell Disable without uninstalling theme={null}
/plugin disable plugin-name@marketplace-name
```

```shell Completely remove a plugin theme={null}
/plugin uninstall plugin-name@marketplace-name
```

### Verify installation

After installing a plugin:

1. **Check available commands**: Run `/help` to see new commands
2. **Test plugin features**: Try the plugin's commands and features
3. **Review plugin details**: Use `/plugin` → "Manage Plugins" to see what the plugin provides

## Set up team plugin workflows

Configure plugins at the repository level to ensure consistent tooling across your team. When team members trust your repository folder, Claude Code automatically installs specified marketplaces and plugins.

**To set up team plugins:**

1. Add marketplace and plugin configuration to your repository's `.claude/settings.json`
2. Team members trust the repository folder
3. Plugins install automatically for all team members

For complete instructions including configuration examples, marketplace setup, and rollout best practices, see [Configure team marketplaces](/en/plugin-marketplaces#how-to-configure-team-marketplaces).

***

## Develop more complex plugins

Once you're comfortable with basic plugins, you can create more sophisticated extensions.

### Add Skills to your plugin

Plugins can include [Agent Skills](/en/skills) to extend Claude's capabilities. Skills are model-invoked—Claude autonomously uses them based on the task context.

To add Skills to your plugin, create a `skills/` directory at your plugin root and add Skill folders with `SKILL.md` files. Plugin Skills are automatically available when the plugin is installed.

For complete Skill authoring guidance, see [Agent Skills](/en/skills).

### Organize complex plugins

For plugins with many components, organize your directory structure by functionality. For complete directory layouts and organization patterns, see [Plugin directory structure](/en/plugins-reference#plugin-directory-structure).

### Test your plugins locally

When developing plugins, use a local marketplace to test changes iteratively. This workflow builds on the quickstart pattern and works for plugins of any complexity.

<Steps>
  <Step title="Set up your development structure">
    Organize your plugin and marketplace for testing:

    ```bash Create directory structure theme={null}
    mkdir dev-marketplace
    cd dev-marketplace
    mkdir my-plugin
    ```

    This creates:

    ```
    dev-marketplace/
    ├── .claude-plugin/marketplace.json  (you'll create this)
    └── my-plugin/                        (your plugin under development)
        ├── .claude-plugin/plugin.json
        ├── commands/
        ├── agents/
        └── hooks/
    ```
  </Step>

  <Step title="Create the marketplace manifest">
    ```bash Create marketplace.json theme={null}
    mkdir .claude-plugin
    cat > .claude-plugin/marketplace.json << 'EOF'
    {
    "name": "dev-marketplace",
    "owner": {
    "name": "Developer"
    },
    "plugins": [
    {
      "name": "my-plugin",
      "source": "./my-plugin",
      "description": "Plugin under development"
    }
    ]
    }
    EOF
    ```
  </Step>

  <Step title="Install and test">
    ```bash Start Claude Code from parent directory theme={null}
    cd ..
    claude
    ```

    ```shell Add your development marketplace theme={null}
    /plugin marketplace add ./dev-marketplace
    ```

    ```shell Install your plugin theme={null}
    /plugin install my-plugin@dev-marketplace
    ```

    Test your plugin components:

    * Try your commands with `/command-name`
    * Check that agents appear in `/agents`
    * Verify hooks work as expected
  </Step>

  <Step title="Iterate on your plugin">
    After making changes to your plugin code:

    ```shell Uninstall the current version theme={null}
    /plugin uninstall my-plugin@dev-marketplace
    ```

    ```shell Reinstall to test changes theme={null}
    /plugin install my-plugin@dev-marketplace
    ```

    Repeat this cycle as you develop and refine your plugin.
  </Step>
</Steps>

<Note>
  **For multiple plugins**: Organize plugins in subdirectories like `./plugins/plugin-name` and update your marketplace.json accordingly. See [Plugin sources](/en/plugin-marketplaces#plugin-sources) for organization patterns.
</Note>

### Debug plugin issues

If your plugin isn't working as expected:

1. **Check the structure**: Ensure your directories are at the plugin root, not inside `.claude-plugin/`
2. **Test components individually**: Check each command, agent, and hook separately
3. **Use validation and debugging tools**: See [Debugging and development tools](/en/plugins-reference#debugging-and-development-tools) for CLI commands and troubleshooting techniques

### Share your plugins

When your plugin is ready to share:

1. **Add documentation**: Include a README.md with installation and usage instructions
2. **Version your plugin**: Use semantic versioning in your `plugin.json`
3. **Create or use a marketplace**: Distribute through plugin marketplaces for easy installation
4. **Test with others**: Have team members test the plugin before wider distribution

<Note>
  For complete technical specifications, debugging techniques, and distribution strategies, see [Plugins reference](/en/plugins-reference).
</Note>

***

## Next steps

Now that you understand Claude Code's plugin system, here are suggested paths for different goals:

### For plugin users

* **Discover plugins**: Browse community marketplaces for useful tools
* **Team adoption**: Set up repository-level plugins for your projects
* **Marketplace management**: Learn to manage multiple plugin sources
* **Advanced usage**: Explore plugin combinations and workflows

### For plugin developers

* **Create your first marketplace**: [Plugin marketplaces guide](/en/plugin-marketplaces)
* **Advanced components**: Dive deeper into specific plugin components:
  * [Slash commands](/en/slash-commands) - Command development details
  * [Subagents](/en/sub-agents) - Agent configuration and capabilities
  * [Agent Skills](/en/skills) - Extend Claude's capabilities
  * [Hooks](/en/hooks) - Event handling and automation
  * [MCP](/en/mcp) - External tool integration
* **Distribution strategies**: Package and share your plugins effectively
* **Community contribution**: Consider contributing to community plugin collections

### For team leads and administrators

* **Repository configuration**: Set up automatic plugin installation for team projects
* **Plugin governance**: Establish guidelines for plugin approval and security review
* **Marketplace maintenance**: Create and maintain organization-specific plugin catalogs
* **Training and documentation**: Help team members adopt plugin workflows effectively

## See also

* [Plugin marketplaces](/en/plugin-marketplaces) - Creating and managing plugin catalogs
* [Slash commands](/en/slash-commands) - Understanding custom commands
* [Subagents](/en/sub-agents) - Creating and using specialized agents
* [Agent Skills](/en/skills) - Extend Claude's capabilities
* [Hooks](/en/hooks) - Automating workflows with event handlers
* [MCP](/en/mcp) - Connecting to external tools and services
* [Settings](/en/settings) - Configuration options for plugins


# Plugins reference
Source: https://code.claude.com/docs/en/plugins-reference

Complete technical reference for Claude Code plugin system, including schemas, CLI commands, and component specifications.

<Tip>
  For hands-on tutorials and practical usage, see [Plugins](/en/plugins). For plugin management across teams and communities, see [Plugin marketplaces](/en/plugin-marketplaces).
</Tip>

This reference provides complete technical specifications for the Claude Code plugin system, including component schemas, CLI commands, and development tools.

## Plugin components reference

This section documents the five types of components that plugins can provide.

### Commands

Plugins add custom slash commands that integrate seamlessly with Claude Code's command system.

**Location**: `commands/` directory in plugin root

**File format**: Markdown files with frontmatter

For complete details on plugin command structure, invocation patterns, and features, see [Plugin commands](/en/slash-commands#plugin-commands).

### Agents

Plugins can provide specialized subagents for specific tasks that Claude can invoke automatically when appropriate.

**Location**: `agents/` directory in plugin root

**File format**: Markdown files describing agent capabilities

**Agent structure**:

```markdown  theme={null}
---
description: What this agent specializes in
capabilities: ["task1", "task2", "task3"]
---

# Agent Name

Detailed description of the agent's role, expertise, and when Claude should invoke it.

## Capabilities
- Specific task the agent excels at
- Another specialized capability
- When to use this agent vs others

## Context and examples
Provide examples of when this agent should be used and what kinds of problems it solves.
```

**Integration points**:

* Agents appear in the `/agents` interface
* Claude can invoke agents automatically based on task context
* Agents can be invoked manually by users
* Plugin agents work alongside built-in Claude agents

### Skills

Plugins can provide Agent Skills that extend Claude's capabilities. Skills are model-invoked—Claude autonomously decides when to use them based on the task context.

**Location**: `skills/` directory in plugin root

**File format**: Directories containing `SKILL.md` files with frontmatter

**Skill structure**:

```
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (optional)
│   └── scripts/ (optional)
└── code-reviewer/
    └── SKILL.md
```

**Integration behavior**:

* Plugin Skills are automatically discovered when the plugin is installed
* Claude autonomously invokes Skills based on matching task context
* Skills can include supporting files alongside SKILL.md

For SKILL.md format and complete Skill authoring guidance, see:

* [Use Skills in Claude Code](/en/skills)
* [Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview#skill-structure)

### Hooks

Plugins can provide event handlers that respond to Claude Code events automatically.

**Location**: `hooks/hooks.json` in plugin root, or inline in plugin.json

**Format**: JSON configuration with event matchers and actions

**Hook configuration**:

```json  theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

**Available events**:

* `PreToolUse`: Before Claude uses any tool
* `PostToolUse`: After Claude uses any tool
* `UserPromptSubmit`: When user submits a prompt
* `Notification`: When Claude Code sends notifications
* `Stop`: When Claude attempts to stop
* `SubagentStop`: When a subagent attempts to stop
* `SessionStart`: At the beginning of sessions
* `SessionEnd`: At the end of sessions
* `PreCompact`: Before conversation history is compacted

**Hook types**:

* `command`: Execute shell commands or scripts
* `validation`: Validate file contents or project state
* `notification`: Send alerts or status updates

### MCP servers

Plugins can bundle Model Context Protocol (MCP) servers to connect Claude Code with external tools and services.

**Location**: `.mcp.json` in plugin root, or inline in plugin.json

**Format**: Standard MCP server configuration

**MCP server configuration**:

```json  theme={null}
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

**Integration behavior**:

* Plugin MCP servers start automatically when the plugin is enabled
* Servers appear as standard MCP tools in Claude's toolkit
* Server capabilities integrate seamlessly with Claude's existing tools
* Plugin servers can be configured independently of user MCP servers

***

## Plugin manifest schema

The `plugin.json` file defines your plugin's metadata and configuration. This section documents all supported fields and options.

### Complete schema

```json  theme={null}
{
  "name": "plugin-name",
  "version": "1.2.0",
  "description": "Brief plugin description",
  "author": {
    "name": "Author Name",
    "email": "author@example.com",
    "url": "https://github.com/author"
  },
  "homepage": "https://docs.example.com/plugin",
  "repository": "https://github.com/author/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "commands": ["./custom/commands/special.md"],
  "agents": "./custom/agents/",
  "hooks": "./config/hooks.json",
  "mcpServers": "./mcp-config.json"
}
```

### Required fields

| Field  | Type   | Description                               | Example              |
| :----- | :----- | :---------------------------------------- | :------------------- |
| `name` | string | Unique identifier (kebab-case, no spaces) | `"deployment-tools"` |

### Metadata fields

| Field         | Type   | Description                         | Example                                            |
| :------------ | :----- | :---------------------------------- | :------------------------------------------------- |
| `version`     | string | Semantic version                    | `"2.1.0"`                                          |
| `description` | string | Brief explanation of plugin purpose | `"Deployment automation tools"`                    |
| `author`      | object | Author information                  | `{"name": "Dev Team", "email": "dev@company.com"}` |
| `homepage`    | string | Documentation URL                   | `"https://docs.example.com"`                       |
| `repository`  | string | Source code URL                     | `"https://github.com/user/plugin"`                 |
| `license`     | string | License identifier                  | `"MIT"`, `"Apache-2.0"`                            |
| `keywords`    | array  | Discovery tags                      | `["deployment", "ci-cd"]`                          |

### Component path fields

| Field        | Type           | Description                          | Example                                |
| :----------- | :------------- | :----------------------------------- | :------------------------------------- |
| `commands`   | string\|array  | Additional command files/directories | `"./custom/cmd.md"` or `["./cmd1.md"]` |
| `agents`     | string\|array  | Additional agent files               | `"./custom/agents/"`                   |
| `hooks`      | string\|object | Hook config path or inline config    | `"./hooks.json"`                       |
| `mcpServers` | string\|object | MCP config path or inline config     | `"./mcp.json"`                         |

### Path behavior rules

**Important**: Custom paths supplement default directories - they don't replace them.

* If `commands/` exists, it's loaded in addition to custom command paths
* All paths must be relative to plugin root and start with `./`
* Commands from custom paths use the same naming and namespacing rules
* Multiple paths can be specified as arrays for flexibility

**Path examples**:

```json  theme={null}
{
  "commands": [
    "./specialized/deploy.md",
    "./utilities/batch-process.md"
  ],
  "agents": [
    "./custom-agents/reviewer.md",
    "./custom-agents/tester.md"
  ]
}
```

### Environment variables

**`${CLAUDE_PLUGIN_ROOT}`**: Contains the absolute path to your plugin directory. Use this in hooks, MCP servers, and scripts to ensure correct paths regardless of installation location.

```json  theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/process.sh"
          }
        ]
      }
    ]
  }
}
```

***

## Plugin directory structure

### Standard plugin layout

A complete plugin follows this structure:

```
enterprise-plugin/
├── .claude-plugin/           # Metadata directory
│   └── plugin.json          # Required: plugin manifest
├── commands/                 # Default command location
│   ├── status.md
│   └──  logs.md
├── agents/                   # Default agent location
│   ├── security-reviewer.md
│   ├── performance-tester.md
│   └── compliance-checker.md
├── skills/                   # Agent Skills
│   ├── code-reviewer/
│   │   └── SKILL.md
│   └── pdf-processor/
│       ├── SKILL.md
│       └── scripts/
├── hooks/                    # Hook configurations
│   ├── hooks.json           # Main hook config
│   └── security-hooks.json  # Additional hooks
├── .mcp.json                # MCP server definitions
├── scripts/                 # Hook and utility scripts
│   ├── security-scan.sh
│   ├── format-code.py
│   └── deploy.js
├── LICENSE                  # License file
└── CHANGELOG.md             # Version history
```

<Warning>
  The `.claude-plugin/` directory contains the `plugin.json` file. All other directories (commands/, agents/, skills/, hooks/) must be at the plugin root, not inside `.claude-plugin/`.
</Warning>

### File locations reference

| Component       | Default Location             | Purpose                          |
| :-------------- | :--------------------------- | :------------------------------- |
| **Manifest**    | `.claude-plugin/plugin.json` | Required metadata file           |
| **Commands**    | `commands/`                  | Slash command markdown files     |
| **Agents**      | `agents/`                    | Subagent markdown files          |
| **Skills**      | `skills/`                    | Agent Skills with SKILL.md files |
| **Hooks**       | `hooks/hooks.json`           | Hook configuration               |
| **MCP servers** | `.mcp.json`                  | MCP server definitions           |

***

## Debugging and development tools

### Debugging commands

Use `claude --debug` to see plugin loading details:

```bash  theme={null}
claude --debug
```

This shows:

* Which plugins are being loaded
* Any errors in plugin manifests
* Command, agent, and hook registration
* MCP server initialization

### Common issues

| Issue                  | Cause                           | Solution                                             |
| :--------------------- | :------------------------------ | :--------------------------------------------------- |
| Plugin not loading     | Invalid `plugin.json`           | Validate JSON syntax                                 |
| Commands not appearing | Wrong directory structure       | Ensure `commands/` at root, not in `.claude-plugin/` |
| Hooks not firing       | Script not executable           | Run `chmod +x script.sh`                             |
| MCP server fails       | Missing `${CLAUDE_PLUGIN_ROOT}` | Use variable for all plugin paths                    |
| Path errors            | Absolute paths used             | All paths must be relative and start with `./`       |

***

## Distribution and versioning reference

### Version management

Follow semantic versioning for plugin releases:

```json  theme={null}

## See also

- [Plugins](/en/plugins) - Tutorials and practical usage
- [Plugin marketplaces](/en/plugin-marketplaces) - Creating and managing marketplaces
- [Slash commands](/en/slash-commands) - Command development details
- [Subagents](/en/sub-agents) - Agent configuration and capabilities
- [Agent Skills](/en/skills) - Extend Claude's capabilities
- [Hooks](/en/hooks) - Event handling and automation
- [MCP](/en/mcp) - External tool integration
- [Settings](/en/settings) - Configuration options for plugins
```


# Visual Studio Code
Source: https://code.claude.com/docs/en/vs-code

Use Claude Code with Visual Studio Code through our native extension or CLI integration

<img src="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=300652d5678c63905e6b0ea9e50835f8" alt="Claude Code VS Code Extension Interface" data-og-width="2500" width="2500" data-og-height="1155" height="1155" data-path="images/vs-code-extension-interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=280&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=87630c671517a3d52e9aee627041696e 280w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=560&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=716b093879204beec8d952649ef75292 560w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=840&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=c1525d1a01513acd9d83d8b5a8fe2fc8 840w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=1100&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=1d90021d58bbb51f871efec13af955c3 1100w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=1650&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=7babdd25440099886f193cfa99af88ae 1650w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=2500&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=08c92eedfb56fe61a61e480fb63784b6 2500w" />

## VS Code Extension (Beta)

The VS Code extension, available in beta, lets you see Claude's changes in real-time through a native graphical interface integrated directly into your IDE. The VS Code extension makes it easier to access and interact with Claude Code for users who prefer a visual interface over the terminal.

### Features

The VS Code extension provides:

* **Native IDE experience**: Dedicated Claude Code sidebar panel accessed via the Spark icon
* **Plan mode with editing**: Review and edit Claude's plans before accepting them
* **Auto-accept edits mode**: Automatically apply Claude's changes as they're made
* **Extended thinking**: Toggle extended thinking on/off using the Extended Thinking button in the bottom-right corner of the prompt input
* **File management**: @-mention files or attach files and images using the system file picker
* **MCP server usage**: Use Model Context Protocol servers configured through the CLI
* **Conversation history**: Easy access to past conversations
* **Multiple sessions**: Run multiple Claude Code sessions simultaneously
* **Keyboard shortcuts**: Support for most shortcuts from the CLI
* **Slash commands**: Access most CLI slash commands directly in the extension

### Requirements

* VS Code 1.98.0 or higher

### Installation

Download and install the extension from the [Visual Studio Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code).

### How It Works

Once installed, you can start using Claude Code through the VS Code interface:

1. Click the Spark icon in your editor's sidebar to open the Claude Code panel
2. Prompt Claude Code in the same way you would in the terminal
3. Watch as Claude analyzes your code and suggests changes
4. Review and accept edits directly in the interface
   * **Tip**: Drag the sidebar wider to see inline diffs, then click on them to expand for full details

### Using Third-Party Providers (Vertex and Bedrock)

The VS Code extension supports using Claude Code with third-party providers like Amazon Bedrock and Google Vertex AI. When configured with these providers, the extension will not prompt for login. To use third-party providers, configure environment variables in the VS Code extension settings:

1. Open VS Code settings
2. Search for "Claude Code: Environment Variables"
3. Add the required environment variables

#### Environment Variables

| Variable                      | Description                            | Required               | Example                                          |
| :---------------------------- | :------------------------------------- | :--------------------- | :----------------------------------------------- |
| `CLAUDE_CODE_USE_BEDROCK`     | Enable Amazon Bedrock integration      | Required for Bedrock   | `"1"` or `"true"`                                |
| `CLAUDE_CODE_USE_VERTEX`      | Enable Google Vertex AI integration    | Required for Vertex AI | `"1"` or `"true"`                                |
| `ANTHROPIC_API_KEY`           | API key for third-party access         | Required               | `"your-api-key"`                                 |
| `AWS_REGION`                  | AWS region for Bedrock                 |                        | `"us-east-2"`                                    |
| `AWS_PROFILE`                 | AWS profile for Bedrock authentication |                        | `"your-profile"`                                 |
| `CLOUD_ML_REGION`             | Region for Vertex AI                   |                        | `"global"` or `"us-east5"`                       |
| `ANTHROPIC_VERTEX_PROJECT_ID` | GCP project ID for Vertex AI           |                        | `"your-project-id"`                              |
| `ANTHROPIC_MODEL`             | Override primary model                 | Override model ID      | `"us.anthropic.claude-sonnet-4-5-20250929-v1:0"` |
| `ANTHROPIC_SMALL_FAST_MODEL`  | Override small/fast model              | Optional               | `"us.anthropic.claude-3-5-haiku-20241022-v1:0"`  |
| `CLAUDE_CODE_SKIP_AUTH_LOGIN` | Disable all prompts to login           | Optional               | `"1"` or `"true"`                                |

For detailed setup instructions and additional configuration options, see:

* [Claude Code on Amazon Bedrock](/en/amazon-bedrock)
* [Claude Code on Google Vertex AI](/en/google-vertex-ai)

### Not Yet Implemented

The following features are not yet available in the VS Code extension:

* **MCP server and Plugin configuration UI**: Type `/mcp` to open the terminal-based MCP server configuration, or `/plugin` for Plugin configuration. Once configured, MCP servers and Plugins will work in the extension. You can also [configure MCP servers through the CLI](/en/mcp) first, then the extension will use them.
* **Subagents configuration**: Configure [subagents through the CLI](/en/sub-agents) to use them in VS Code
* **Checkpoints**: Save and restore conversation state at specific points
* **Conversation rewinding**: The `/rewind` command is coming soon
* **Advanced shortcuts**:
  * `#` shortcut to add to memory (not supported)
  * `!` shortcut to run bash commands directly (not supported)
* **Tab completion**: File path completion with tab key
* **Model selection UI for older models**: To use older model versions like `claude-sonnet-4-20250514`, open VS Code settings for Claude Code (the `/General Config` command) and insert the model string directly into the 'Selected Model' field

We are working on adding these features in future updates.

## Security Considerations

When Claude Code runs in VS Code with auto-edit permissions enabled, it may be able to modify IDE configuration files that can be automatically executed by your IDE. This may increase the risk of running Claude Code in auto-edit mode and allow bypassing Claude Code's permission prompts for bash execution.

When running in VS Code, consider:

* Enabling [VS Code Restricted Mode](https://code.visualstudio.com/docs/editor/workspace-trust#_restricted-mode) for untrusted workspaces
* Using manual approval mode for edits
* Taking extra care to ensure Claude is only used with trusted prompts

## Legacy CLI Integration

The first VS Code integration that we released allows Claude Code running in the terminal to interact with your IDE. It provides selection context sharing (current selection/tab is automatically shared with Claude Code), diff viewing in the IDE instead of terminal, file reference shortcuts (`Cmd+Option+K` on Mac or `Alt+Ctrl+K` on Windows/Linux to insert file references like @File#L1-99), and automatic diagnostic sharing (lint and syntax errors).

The legacy integration auto-installs when you run `claude` from VS Code's integrated terminal. Simply run `claude` from the terminal and all features activate. For external terminals, use the `/ide` command to connect Claude Code to your VS Code instance. To configure, run `claude`, enter `/config`, and set the diff tool to `auto` for automatic IDE detection.

Both the extension and CLI integration work with Visual Studio Code, Cursor, Windsurf, and VSCodium.

## Troubleshooting

### Extension Not Installing

* Ensure you have a compatible version of VS Code (1.85.0 or later)
* Check that VS Code has permission to install extensions
* Try installing directly from the Marketplace website

### Claude Code Never Responds

If Claude Code is not responding to your prompts:

1. **Check your internet connection**: Ensure you have a stable internet connection
2. **Start a new conversation**: Try starting a fresh conversation to see if the issue persists
3. **Try the CLI**: Run `claude` from the terminal to see if you get more detailed error messages
4. **File a bug report**: If the problem continues, [file an issue on GitHub](https://github.com/anthropics/claude-code/issues) with details about the error

### Legacy Integration Not Working

* Ensure you're running Claude Code from VS Code's integrated terminal
* Ensure the CLI for your IDE variant is installed:
  * VS Code: `code` command should be available
  * Cursor: `cursor` command should be available
  * Windsurf: `windsurf` command should be available
  * VSCodium: `codium` command should be available
* If the command isn't installed:
  1. Open command palette with `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
  2. Search for "Shell Command: Install 'code' command in PATH" (or equivalent for your IDE)

For additional help, see our [troubleshooting guide](/en/troubleshooting).



---

**Navigation:** [← Previous: CI/CD](./05-cicd.md) | [Index](./index.md) | [Next: Advanced Features →](./07-advanced.md)
