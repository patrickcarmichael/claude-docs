---
title: "Model Context Protocol (MCP)"
source: "https://docs.windsurf.com/windsurf/cascade/mcp"
---

# Model Context Protocol (MCP)
Source: https://docs.windsurf.com/windsurf/cascade/mcp



**MCP (Model Context Protocol)** is a protocol that enables LLMs to access custom tools and services.
An MCP client (Cascade, in this case) can make requests to MCP servers to access tools that they provide.
Cascade now natively integrates with MCP, allowing you to bring your own selection of MCP servers for Cascade to use.
See the [official MCP docs](https://modelcontextprotocol.io/) for more information.

<Note>Enterprise users must manually turn this on via settings</Note>

## Adding a new MCP plugin

New MCP plugins can be added from the Plugin Store, which you can access by clicking on the `Plugins` icon in the top right menu in the Cascade panel, or from the `Windsurf Settings` > `Cascade` > `Plugins` section.

If you cannot find your desired MCP plugin, you can add it manually by editing the raw `mcp_config.json` file.

Official MCP plugins will show up with a blue checkmark, indicating that they are made by the parent service company.

When you click on a plugin, simply click `Install` to expose the server and its tools to Cascade.

Windsurf supports two [transport types](https://modelcontextprotocol.io/docs/concepts/transports) for MCP servers: `stdio` and `http`.

For `http` servers, the URL should reflect that of the endpoint and resemble `https://<your-server-url>/mcp`.

We can also support streamable HTTP transport and MCP Authentication.

<Note>Make sure to press the refresh button after you add a new MCP plugin.</Note>

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d755c65b22df71e8d035f440cb2fff22" data-og-width="1138" width="1138" data-og-height="828" height="828" data-path="assets/windsurf/cascade/mcp/mcp-plugin-store.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a7e3ab90cf04cdfabbdd580f83aea2b2 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=0011e35c9f6a2202f26e3485ef017b2c 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=92c63c6e862e266842486022c402866d 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=26f17c37647e79435ca3ade47e087147 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1202cfe8ef04923199de9625ffe8aaa6 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-plugin-store.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d582ec77762e3e0ca99d65d5525e64a6 2500w" />
</Frame>

## Configuring MCP tools

Each plugin has a certain number of tools it has access to. Cascade has a limit of 100 total tools that it has access to at any given time.

At the plugin level, you can navigate to the Tools tab and toggle the tools that you wish to enable. Or, from the `Windsurf Settings`, you can click on the `Manage plugins` button.

<Frame>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=30757b56f44e15c789a6f9f50dfa6035" data-og-width="1130" width="1130" data-og-height="700" height="700" data-path="assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ba55e144bbb094c2cc9425c5225a01a1 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f3b5992248f1c307fec42269b6172b43 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a4d03feb4bc0128fab8236a5184f5aed 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=4067473f9a179c67e3dabd16db2c870b 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=1b6598d6418581175716d87b40903fee 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/mcp/mcp-manage-plugin-tools.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=5d12db70cab4e15dbf199f629d4d40d4 2500w" />
</Frame>

## mcp\_config.json

The `~/.codeium/windsurf/mcp_config.json` file is a JSON file that contains a list of servers that Cascade can connect to.

The JSON should follow the same schema as the config file for Claude Desktop.

Here’s an example configuration, which sets up a single server for GitHub:

```json  theme={null}
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_PERSONAL_ACCESS_TOKEN>"
      }
    }
  }
}
```

It's important to note that for HTTP servers, the configuration is slightly different and requires a `serverUrl` field.

Here's an example configuration for an HTTP server:

```json  theme={null}
{
  "mcpServers": {
    "figma": {
      "serverUrl": "<your-server-url>/mcp"
    }
  }
}
```

<Note>For Figma Dev Mode MCP server, make sure you have updated to the latest Figma desktop app version to use the new `/mcp` endpoint.</Note>

Be sure to provide the required arguments and environment variables for the servers that you want to use.

See the [official MCP server reference repository](https://github.com/modelcontextprotocol/servers) or [OpenTools](https://opentools.com/) for some example servers.

## Admin Controls (Teams & Enterprises)

Team admins can toggle MCP access for their team, as well as whitelist approved MCP servers for their team to use:

<Card title="MCP Team Settings" horizontal={true} icon="hammer" href="https://windsurf.com/team/settings">
  Configurable MCP settings for your team.
</Card>

<Warning>The above link will only work if you have admin privileges for your team.</Warning>

By default, users within a team will be able to configure their own MCP servers. However, once you whitelist even a single MCP server, **all non-whitelisted servers will be blocked** for your team.

### How Server Matching Works

When you whitelist an MCP server, the system uses **regex pattern matching** with the following rules:

* **Full String Matching**: All patterns are automatically anchored (wrapped with `^(?:pattern)$`) to prevent partial matches
* **Command Field**: Must match exactly or according to your regex pattern
* **Arguments Array**: Each argument is matched individually against its corresponding pattern
* **Array Length**: The number of arguments must match exactly between whitelist and user config
* **Special Characters**: Characters like `$`, `.`, `[`, `]`, `(`, `)` have special regex meaning and should be escaped with `\` if you want literal matching

### Configuration Options

<AccordionGroup>
  <Accordion title="Option 1: Plugin Store Default (Recommended)" description="Leave the Server Config (JSON) field empty to allow the default configuration from the Windsurf MCP Plugin Store.">
    **Admin Whitelist Configuration:**

    * **Server ID**: `github-mcp-server`
    * **Server Config (JSON)**: *(leave empty)*

    ```json  theme={null}
    {}
    ```

    **Matching User Config (`mcp_config.json`):**

    ```json  theme={null}
    {
      "mcpServers": {
        "github-mcp-server": {
          "command": "docker",
          "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server"
          ],
          "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
          }
        }
      }
    }
    ```

    This allows users to install the GitHub MCP server with any valid configuration, as long as the server ID matches the plugin store entry.
  </Accordion>

  <Accordion title="Option 2: Exact Match Configuration" description="Provide the exact configuration that users must use. Users must match this configuration exactly.">
    **Admin Whitelist Configuration:**

    * **Server ID**: `github-mcp-server`
    * **Server Config (JSON)**:

    ```json  theme={null}
    {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    }
    ```

    **Matching User Config (`mcp_config.json`):**

    ```json  theme={null}
    {
      "mcpServers": {
        "github-mcp-server": {
          "command": "docker",
          "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server"
          ],
          "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
          }
        }
      }
    }
    ```

    Users must use this exact configuration - any deviation in command or args will be blocked. The `env` section can have different values.
  </Accordion>

  <Accordion title="Option 3: Flexible Regex Patterns" description="Use regex patterns to allow variations in user configurations while maintaining security controls.">
    **Admin Whitelist Configuration:**

    * **Server ID**: `python-mcp-server`
    * **Server Config (JSON)**:

    ```json  theme={null}
    {
      "command": "python3",
      "args": ["/.*\\.py", "--port", "[0-9]+"]
    }
    ```

    **Matching User Config (`mcp_config.json`):**

    ```json  theme={null}
    {
      "mcpServers": {
        "python-mcp-server": {
          "command": "python3",
          "args": ["/home/user/my_server.py", "--port", "8080"],
          "env": {
            "PYTHONPATH": "/home/user/mcp"
          }
        }
      }
    }
    ```

    This example allows users flexibility while maintaining security:

    * The regex `/.*\\.py` matches any Python file path like `/home/user/my_server.py`
    * The regex `[0-9]+` matches any numeric port like `8080` or `3000`
    * Users can customize file paths and ports while admins ensure only Python scripts are executed
  </Accordion>
</AccordionGroup>

### Common Regex Patterns

| Pattern         | Matches                   | Example                |
| --------------- | ------------------------- | ---------------------- |
| `.*`            | Any string                | `/home/user/script.py` |
| `[0-9]+`        | Any number                | `8080`, `3000`         |
| `[a-zA-Z0-9_]+` | Alphanumeric + underscore | `api_key_123`          |
| `\\$HOME`       | Literal `$HOME`           | `$HOME` (not expanded) |
| `\\.py`         | Literal `.py`             | `script.py`            |
| `\\[cli\\]`     | Literal `[cli]`           | `mcp[cli]`             |

## Notes

### Admin Configuration Guidelines

* **Environment Variables**: The `env` section is not regex-matched and can be configured freely by users
* **Disabled Tools**: The `disabledTools` array is handled separately and not part of whitelist matching
* **Case Sensitivity**: All matching is case-sensitive
* **Error Handling**: Invalid regex patterns will be logged and result in access denial
* **Testing**: Test your regex patterns carefully - overly restrictive patterns may block legitimate use cases

### Troubleshooting

If users report that their MCP servers aren't working after whitelisting:

1. **Check Exact Matching**: Ensure the whitelist pattern exactly matches the user's configuration
2. **Verify Regex Escaping**: Special characters may need escaping (e.g., `\.` for literal dots)
3. **Review Logs**: Invalid regex patterns are logged with warnings
4. **Test Patterns**: Use a regex tester to verify your patterns work as expected

Remember: Once you whitelist any server, **all other servers are automatically blocked** for your team members.

### General Information

* Since MCP tool calls can invoke code written by arbitrary server implementers, we do not assume liability
  for MCP tool call failures. To reiterate:
* We currently support an MCP server's [tools](https://modelcontextprotocol.io/docs/concepts/tools) and [resources](https://modelcontextprotocol.io/docs/concepts/resources), not [prompts](https://modelcontextprotocol.io/docs/concepts/prompts).

---

← Previous: [Commit to git](./commit-to-git.md) | [Index](./index.md) | Next: [Memories & Rules](./memories-rules.md) →