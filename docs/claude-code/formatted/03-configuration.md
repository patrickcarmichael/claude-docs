---
title: "Configuration"
description: "Settings and customization options"
weight: 3
---

# Configuration

# Manage Claude's memory
Source: https://code.claude.com/docs/en/memory

Learn how to manage Claude Code's memory across sessions with different memory locations and best practices.

Claude Code can remember your preferences across sessions, like style guidelines and common commands in your workflow.

## Determine memory type

Claude Code offers four memory locations in a hierarchical structure, each serving a different purpose:

| Memory Type                | Location                                                                                                                                                | Purpose                                             | Use Case Examples                                                    | Shared With                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
| **Enterprise policy**      | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br />Linux: `/etc/claude-code/CLAUDE.md`<br />Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization       |
| **Project memory**         | `./CLAUDE.md` or `./.claude/CLAUDE.md`                                                                                                                  | Team-shared instructions for the project            | Project architecture, coding standards, common workflows             | Team members via source control |
| **User memory**            | `~/.claude/CLAUDE.md`                                                                                                                                   | Personal preferences for all projects               | Code styling preferences, personal tooling shortcuts                 | Just you (all projects)         |
| **Project memory (local)** | `./CLAUDE.local.md`                                                                                                                                     | Personal project-specific preferences               | *(Deprecated, see below)* Your sandbox URLs, preferred test data     | Just you (current project)      |

All memory files are automatically loaded into Claude Code's context when launched. Files higher in the hierarchy take precedence and are loaded first, providing a foundation that more specific memories build upon.

## CLAUDE.md imports

CLAUDE.md files can import additional files using `@path/to/import` syntax. The following example imports 3 files:

```
See @README for project overview and @package.json for available npm commands for this project.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

Both relative and absolute paths are allowed. In particular, importing files in user's home dir is a convenient way for your team members to provide individual instructions that are not checked into the repository. Previously CLAUDE.local.md served a similar purpose, but is now deprecated in favor of imports since they work better across multiple git worktrees.

```
# Individual Preferences
- @~/.claude/my-project-instructions.md
```

To avoid potential collisions, imports are not evaluated inside markdown code spans and code blocks.

```
This code span will not be treated as an import: `@anthropic-ai/claude-code`
```

Imported files can recursively import additional files, with a max-depth of 5 hops. You can see what memory files are loaded by running `/memory` command.

## How Claude looks up memories

Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to (but not including) the root directory */* and reads any CLAUDE.md or CLAUDE.local.md files it finds. This is especially convenient when working in large repositories where you run Claude Code in *foo/bar/*, and have memories in both *foo/CLAUDE.md* and *foo/bar/CLAUDE.md*.

Claude will also discover CLAUDE.md nested in subtrees under your current working directory. Instead of loading them at launch, they are only included when Claude reads files in those subtrees.

## Quickly add memories with the `#` shortcut

The fastest way to add a memory is to start your input with the `#` character:

```
# Always use descriptive variable names
```

You'll be prompted to select which memory file to store this in.

## Directly edit memories with `/memory`

Use the `/memory` slash command during a session to open any memory file in your system editor for more extensive additions or organization.

## Set up project memory

Suppose you want to set up a CLAUDE.md file to store important project information, conventions, and frequently used commands. Project memory can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`.

Bootstrap a CLAUDE.md for your codebase with the following command:

```
> /init 
```


> **💡 Tip:** Tips:

  * Include frequently used commands (build, test, lint) to avoid repeated searches
  * Document code style preferences and naming conventions
  * Add important architectural patterns specific to your project
  * CLAUDE.md memories can be used for both instructions shared with your team and for your individual preferences.



## Organization-level memory management

Enterprise organizations can deploy centrally managed CLAUDE.md files that apply to all users.

To set up organization-level memory management:

1. Create the enterprise memory file in the appropriate location for your operating system:

* macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`
* Linux/WSL: `/etc/claude-code/CLAUDE.md`
* Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md`

2. Deploy via your configuration management system (MDM, Group Policy, Ansible, etc.) to ensure consistent distribution across all developer machines.

## Memory best practices

* **Be specific**: "Use 2-space indentation" is better than "Format code properly".
* **Use structure to organize**: Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
* **Review periodically**: Update memories as your project evolves to ensure Claude is always using the most up to date information and context.


# Model configuration
Source: https://code.claude.com/docs/en/model-config

Learn about the Claude Code model configuration, including model aliases like `opusplan`

## Available models

For the `model` setting in Claude Code, you can either configure:

* A **model alias**
* A full **[model name](https://docs.claude.com/en/docs/about-claude/models/overview#model-names)**
* For Bedrock, an ARN

### Model aliases

Model aliases provide a convenient way to select model settings without
remembering exact version numbers:

| Model alias      | Behavior                                                                                                                                                                |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`default`**    | Recommended model setting, depending on your account type                                                                                                               |
| **`sonnet`**     | Uses the latest Sonnet model (currently Sonnet 4.5) for daily coding tasks                                                                                              |
| **`opus`**       | Uses Opus model (currently Opus 4.1) for specialized complex reasoning tasks                                                                                            |
| **`haiku`**      | Uses the fast and efficient Haiku model for simple tasks                                                                                                                |
| **`sonnet[1m]`** | Uses Sonnet with a [1 million token context window](https://docs.claude.com/en/docs/build-with-claude/context-windows#1m-token-context-window) window for long sessions |
| **`opusplan`**   | Special mode that uses `opus` during plan mode, then switches to `sonnet` for execution                                                                                 |

### Setting your model

You can configure your model in several ways, listed in order of priority:

1. **During session** - Use `/model <alias|name>` to switch models mid-session
2. **At startup** - Launch with `claude --model <alias|name>`
3. **Environment variable** - Set `ANTHROPIC_MODEL=<alias|name>`
4. **Settings** - Configure permanently in your settings file using the `model`
   field.

Example usage:

```bash
# Start with Opus
claude --model opus

# Switch to Sonnet during session
/model sonnet
```

Example settings file:

```
{
    "permissions": {
        ...
    },
    "model": "opus"
}
```

## Special model behavior

### `default` model setting

The behavior of `default` depends on your account type.

For certain Max users, Claude Code will automatically fall back to Sonnet if you
hit a usage threshold with Opus.

### `opusplan` model setting

The `opusplan` model alias provides an automated hybrid approach:

* **In plan mode** - Uses `opus` for complex reasoning and architecture
  decisions
* **In execution mode** - Automatically switches to `sonnet` for code generation
  and implementation

This gives you the best of both worlds: Opus's superior reasoning for planning,
and Sonnet's efficiency for execution.

### Extended context with \[1m]

For Console/API users, the `[1m]` suffix can be added to full model names to
enable a
[1 million token context window](https://docs.claude.com/en/docs/build-with-claude/context-windows#1m-token-context-window).

```bash
# Example of using a full model name with the [1m] suffix
/model anthropic.claude-sonnet-4-5-20250929-v1:0[1m]
```

Note: Extended context models have
[different pricing](https://docs.claude.com/en/docs/about-claude/pricing#long-context-pricing).

## Checking your current model

You can see which model you're currently using in several ways:

1. In [status line](/en/statusline) (if configured)
2. In `/status`, which also displays your account information.

## Environment variables

You can use the following environment variables, which must be full **model
names**, to control the model names that the aliases map to.

| Env var                          | Description                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------- |
| `ANTHROPIC_DEFAULT_OPUS_MODEL`   | The model to use for `opus`, or for `opusplan` when Plan Mode is active.                      |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | The model to use for `sonnet`, or for `opusplan` when Plan Mode is not active.                |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL`  | The model to use for `haiku`, or [background functionality](/en/costs#background-token-usage) |
| `CLAUDE_CODE_SUBAGENT_MODEL`     | The model to use for [subagents](/en/sub-agents)                                              |

Note: `ANTHROPIC_SMALL_FAST_MODEL` is deprecated in favor of
`ANTHROPIC_DEFAULT_HAIKU_MODEL`.

### Prompt caching configuration

Claude Code automatically uses [prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) to optimize performance and reduce costs. You can disable prompt caching globally or for specific model tiers:

| Env var                         | Description                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------- |
| `DISABLE_PROMPT_CACHING`        | Set to `1` to disable prompt caching for all models (takes precedence over per-model settings) |
| `DISABLE_PROMPT_CACHING_HAIKU`  | Set to `1` to disable prompt caching for Haiku models only                                     |
| `DISABLE_PROMPT_CACHING_SONNET` | Set to `1` to disable prompt caching for Sonnet models only                                    |
| `DISABLE_PROMPT_CACHING_OPUS`   | Set to `1` to disable prompt caching for Opus models only                                      |

These environment variables give you fine-grained control over prompt caching behavior. The global `DISABLE_PROMPT_CACHING` setting takes precedence over the model-specific settings, allowing you to quickly disable all caching when needed. The per-model settings are useful for selective control, such as when debugging specific models or working with cloud providers that may have different caching implementations.


# Output styles
Source: https://code.claude.com/docs/en/output-styles

Adapt Claude Code for uses beyond software engineering

Output styles allow you to use Claude Code as any type of agent while keeping
its core capabilities, such as running local scripts, reading/writing files, and
tracking TODOs.

## Built-in output styles

Claude Code's **Default** output style is the existing system prompt, designed
to help you complete software engineering tasks efficiently.

There are two additional built-in output styles focused on teaching you the
codebase and how Claude operates:

* **Explanatory**: Provides educational "Insights" in between helping you
  complete software engineering tasks. Helps you understand implementation
  choices and codebase patterns.

* **Learning**: Collaborative, learn-by-doing mode where Claude will not only
  share "Insights" while coding, but also ask you to contribute small, strategic
  pieces of code yourself. Claude Code will add `TODO(human)` markers in your
  code for you to implement.

## How output styles work

Output styles directly modify Claude Code's system prompt.

* Non-default output styles exclude instructions specific to code generation and
  efficient output normally built into Claude Code (such as responding concisely
  and verifying code with tests).
* Instead, these output styles have their own custom instructions added to the
  system prompt.

## Change your output style

You can either:

* Run `/output-style` to access the menu and select your output style (this can
  also be accessed from the `/config` menu)

* Run `/output-style [style]`, such as `/output-style explanatory`, to directly
  switch to a style

These changes apply to the [local project level](/en/settings)
and are saved in `.claude/settings.local.json`.

## Create a custom output style

To set up a new output style with Claude's help, run
`/output-style:new I want an output style that ...`

By default, output styles created through `/output-style:new` are saved as
markdown files at the user level in `~/.claude/output-styles` and can be used
across projects. They have the following structure:

```markdown
---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]
```

You can also create your own output style Markdown files and save them either at
the user level (`~/.claude/output-styles`) or the project level
(`.claude/output-styles`).

## Comparisons to related features

### Output Styles vs. CLAUDE.md vs. --append-system-prompt

Output styles completely "turn off" the parts of Claude Code's default system
prompt specific to software engineering. Neither CLAUDE.md nor
`--append-system-prompt` edit Claude Code's default system prompt. CLAUDE.md
adds the contents as a user message *following* Claude Code's default system
prompt. `--append-system-prompt` appends the content to the system prompt.

### Output Styles vs. [Agents](/en/sub-agents)

Output styles directly affect the main agent loop and only affect the system
prompt. Agents are invoked to handle specific tasks and can include additional
settings like the model to use, the tools they have available, and some context
about when to use the agent.

### Output Styles vs. [Custom Slash Commands](/en/slash-commands)

You can think of output styles as "stored system prompts" and custom slash
commands as "stored prompts".


# Claude Code settings
Source: https://code.claude.com/docs/en/settings

Configure Claude Code with global and project-level settings, and environment variables.

Claude Code offers a variety of settings to configure its behavior to meet your needs. You can configure Claude Code by running the `/config` command when using the interactive REPL, which opens a tabbed Settings interface where you can view status information and modify configuration options.

## Settings files

The `settings.json` file is our official mechanism for configuring Claude
Code through hierarchical settings:

* **User settings** are defined in `~/.claude/settings.json` and apply to all
  projects.
* **Project settings** are saved in your project directory:
  * `.claude/settings.json` for settings that are checked into source control and shared with your team
  * `.claude/settings.local.json` for settings that are not checked in, useful for personal preferences and experimentation. Claude Code will configure git to ignore `.claude/settings.local.json` when it is created.
* For enterprise deployments of Claude Code, we also support **enterprise
  managed policy settings**. These take precedence over user and project
  settings. System administrators can deploy policies to:
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Linux and WSL: `/etc/claude-code/managed-settings.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`
* Enterprise deployments can also configure **managed MCP servers** that override
  user-configured servers. See [Enterprise MCP configuration](/en/mcp#enterprise-mcp-configuration):
  * macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
  * Linux and WSL: `/etc/claude-code/managed-mcp.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-mcp.json`

```JSON
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  },
  "companyAnnouncements": [
    "Welcome to Acme Corp! Review our code guidelines at docs.acme.com",
    "Reminder: Code reviews required for all PRs",
    "New security policy in effect"
  ]
}
```

### Available settings

`settings.json` supports a number of options:

| Key                          | Description                                                                                                                                                                                                                                                      | Example                                                                 |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| `apiKeyHelper`               | Custom script, to be executed in `/bin/sh`, to generate an auth value. This value will be sent as `X-Api-Key` and `Authorization: Bearer` headers for model requests                                                                                             | `/bin/generate_temp_api_key.sh`                                         |
| `cleanupPeriodDays`          | How long to locally retain chat transcripts based on last activity date (default: 30 days)                                                                                                                                                                       | `20`                                                                    |
| `companyAnnouncements`       | Announcement to display to users at startup. If multiple announcements are provided, they will be cycled through at random.                                                                                                                                      | `["Welcome to Acme Corp! Review our code guidelines at docs.acme.com"]` |
| `env`                        | Environment variables that will be applied to every session                                                                                                                                                                                                      | `{"FOO": "bar"}`                                                        |
| `includeCoAuthoredBy`        | Whether to include the `co-authored-by Claude` byline in git commits and pull requests (default: `true`)                                                                                                                                                         | `false`                                                                 |
| `permissions`                | See table below for structure of permissions.                                                                                                                                                                                                                    |                                                                         |
| `hooks`                      | Configure custom commands to run before or after tool executions. See [hooks documentation](/en/hooks)                                                                                                                                                           | `{"PreToolUse": {"Bash": "echo 'Running command...'"}}`                 |
| `disableAllHooks`            | Disable all [hooks](/en/hooks)                                                                                                                                                                                                                                   | `true`                                                                  |
| `model`                      | Override the default model to use for Claude Code                                                                                                                                                                                                                | `"claude-sonnet-4-5-20250929"`                                          |
| `statusLine`                 | Configure a custom status line to display context. See [statusLine documentation](/en/statusline)                                                                                                                                                                | `{"type": "command", "command": "~/.claude/statusline.sh"}`             |
| `outputStyle`                | Configure an output style to adjust the system prompt. See [output styles documentation](/en/output-styles)                                                                                                                                                      | `"Explanatory"`                                                         |
| `forceLoginMethod`           | Use `claudeai` to restrict login to Claude.ai accounts, `console` to restrict login to Claude Console (API usage billing) accounts                                                                                                                               | `claudeai`                                                              |
| `forceLoginOrgUUID`          | Specify the UUID of an organization to automatically select it during login, bypassing the organization selection step. Requires `forceLoginMethod` to be set                                                                                                    | `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`                                |
| `enableAllProjectMcpServers` | Automatically approve all MCP servers defined in project `.mcp.json` files                                                                                                                                                                                       | `true`                                                                  |
| `enabledMcpjsonServers`      | List of specific MCP servers from `.mcp.json` files to approve                                                                                                                                                                                                   | `["memory", "github"]`                                                  |
| `disabledMcpjsonServers`     | List of specific MCP servers from `.mcp.json` files to reject                                                                                                                                                                                                    | `["filesystem"]`                                                        |
| `allowedMcpServers`          | When set in managed-settings.json, allowlist of MCP servers users can configure. Undefined = no restrictions, empty array = lockdown. Applies to all scopes. Denylist takes precedence. See [Enterprise MCP configuration](/en/mcp#enterprise-mcp-configuration) | `[{ "serverName": "github" }]`                                          |
| `deniedMcpServers`           | When set in managed-settings.json, denylist of MCP servers that are explicitly blocked. Applies to all scopes including enterprise servers. Denylist takes precedence over allowlist. See [Enterprise MCP configuration](/en/mcp#enterprise-mcp-configuration)   | `[{ "serverName": "filesystem" }]`                                      |
| `awsAuthRefresh`             | Custom script that modifies the `.aws` directory (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                                 | `aws sso login --profile myprofile`                                     |
| `awsCredentialExport`        | Custom script that outputs JSON with AWS credentials (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                             | `/bin/generate_aws_grant.sh`                                            |

### Permission settings

| Keys                           | Description                                                                                                                                                                                                                                                                                 | Example                                                                |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| `allow`                        | Array of [permission rules](/en/iam#configuring-permissions) to allow tool use. **Note:** Bash rules use prefix matching, not regex                                                                                                                                                         | `[ "Bash(git diff:*)" ]`                                               |
| `ask`                          | Array of [permission rules](/en/iam#configuring-permissions) to ask for confirmation upon tool use.                                                                                                                                                                                         | `[ "Bash(git push:*)" ]`                                               |
| `deny`                         | Array of [permission rules](/en/iam#configuring-permissions) to deny tool use. Use this to also exclude sensitive files from Claude Code access. **Note:** Bash patterns are prefix matches and can be bypassed (see [Bash permission limitations](/en/iam#tool-specific-permission-rules)) | `[ "WebFetch", "Bash(curl:*)", "Read(./.env)", "Read(./secrets/**)" ]` |
| `additionalDirectories`        | Additional [working directories](/en/iam#working-directories) that Claude has access to                                                                                                                                                                                                     | `[ "../docs/" ]`                                                       |
| `defaultMode`                  | Default [permission mode](/en/iam#permission-modes) when opening Claude Code                                                                                                                                                                                                                | `"acceptEdits"`                                                        |
| `disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode from being activated. This disables the `--dangerously-skip-permissions` command-line flag. See [managed policy settings](/en/iam#enterprise-managed-policy-settings)                                                                | `"disable"`                                                            |

### Sandbox settings

Configure advanced sandboxing behavior. Sandboxing isolates bash commands from your filesystem and network. See [Sandboxing](/en/sandboxing) for details.

**Filesystem and network restrictions** are configured via Read, Edit, and WebFetch permission rules, not via these sandbox settings.

| Keys                        | Description                                                                                                                                                                                                                                                                                                                       | Example                   |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| `enabled`                   | Enable bash sandboxing (macOS/Linux only). Default: false                                                                                                                                                                                                                                                                         | `true`                    |
| `autoAllowBashIfSandboxed`  | Auto-approve bash commands when sandboxed. Default: true                                                                                                                                                                                                                                                                          | `true`                    |
| `excludedCommands`          | Commands that should run outside of the sandbox                                                                                                                                                                                                                                                                                   | `["git", "docker"]`       |
| `allowUnsandboxedCommands`  | Allow commands to run outside the sandbox via the `dangerouslyDisableSandbox` parameter. When set to `false`, the `dangerouslyDisableSandbox` escape hatch is completely disabled and all commands must run sandboxed (or be in `excludedCommands`). Useful for enterprise policies that require strict sandboxing. Default: true | `false`                   |
| `network.allowUnixSockets`  | Unix socket paths accessible in sandbox (for SSH agents, etc.)                                                                                                                                                                                                                                                                    | `["~/.ssh/agent-socket"]` |
| `network.allowLocalBinding` | Allow binding to localhost ports (MacOS only). Default: false                                                                                                                                                                                                                                                                     | `true`                    |
| `network.httpProxyPort`     | HTTP proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                        | `8080`                    |
| `network.socksProxyPort`    | SOCKS5 proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy.                                                                                                                                                                                                                      | `8081`                    |
| `enableWeakerNestedSandbox` | Enable weaker sandbox for unprivileged Docker environments (Linux only). **Reduces security.** Default: false                                                                                                                                                                                                                     | `true`                    |

**Configuration example:**

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker"],
    "network": {
      "allowUnixSockets": [
        "/var/run/docker.sock"
      ],
      "allowLocalBinding": true
    }
  },
  "permissions": {
    "deny": [
      "Read(.envrc)",
      "Read(~/.aws/**)"
    ]
  }
}
```

**Filesystem access** is controlled via Read/Edit permissions:

* Read deny rules block file reads in sandbox
* Edit allow rules permit file writes (in addition to the defaults, e.g. the current working directory)
* Edit deny rules block writes within allowed paths

**Network access** is controlled via WebFetch permissions:

* WebFetch allow rules permit network domains
* WebFetch deny rules block network domains

### Settings precedence

Settings are applied in order of precedence (highest to lowest):

1. **Enterprise managed policies** (`managed-settings.json`)
   * Deployed by IT/DevOps
   * Cannot be overridden

2. **Command line arguments**
   * Temporary overrides for a specific session

3. **Local project settings** (`.claude/settings.local.json`)
   * Personal project-specific settings

4. **Shared project settings** (`.claude/settings.json`)
   * Team-shared project settings in source control

5. **User settings** (`~/.claude/settings.json`)
   * Personal global settings

This hierarchy ensures that enterprise security policies are always enforced while still allowing teams and individuals to customize their experience.

### Key points about the configuration system

* **Memory files (CLAUDE.md)**: Contain instructions and context that Claude loads at startup
* **Settings files (JSON)**: Configure permissions, environment variables, and tool behavior
* **Slash commands**: Custom commands that can be invoked during a session with `/command-name`
* **MCP servers**: Extend Claude Code with additional tools and integrations
* **Precedence**: Higher-level configurations (Enterprise) override lower-level ones (User/Project)
* **Inheritance**: Settings are merged, with more specific settings adding to or overriding broader ones

### System prompt availability


> **Note:** Unlike for claude.ai, we do not publish Claude Code's internal system prompt on this website. Use CLAUDE.md files or `--append-system-prompt` to add custom instructions to Claude Code's behavior.



### Excluding sensitive files

To prevent Claude Code from accessing files containing sensitive information (e.g., API keys, secrets, environment files), use the `permissions.deny` setting in your `.claude/settings.json` file:

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./build)"
    ]
  }
}
```

This replaces the deprecated `ignorePatterns` configuration. Files matching these patterns will be completely invisible to Claude Code, preventing any accidental exposure of sensitive data.

## Subagent configuration

Claude Code supports custom AI subagents that can be configured at both user and project levels. These subagents are stored as Markdown files with YAML frontmatter:

* **User subagents**: `~/.claude/agents/` - Available across all your projects
* **Project subagents**: `.claude/agents/` - Specific to your project and can be shared with your team

Subagent files define specialized AI assistants with custom prompts and tool permissions. Learn more about creating and using subagents in the [subagents documentation](/en/sub-agents).

## Plugin configuration

Claude Code supports a plugin system that lets you extend functionality with custom commands, agents, hooks, and MCP servers. Plugins are distributed through marketplaces and can be configured at both user and repository levels.

### Plugin settings

Plugin-related settings in `settings.json`:

```json
{
  "enabledPlugins": {
    "formatter@company-tools": true,
    "deployer@company-tools": true,
    "analyzer@security-plugins": false
  },
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": "github",
      "repo": "company/claude-plugins"
    }
  }
}
```

#### `enabledPlugins`

Controls which plugins are enabled. Format: `"plugin-name@marketplace-name": true/false`

**Scopes**:

* **User settings** (`~/.claude/settings.json`): Personal plugin preferences
* **Project settings** (`.claude/settings.json`): Project-specific plugins shared with team
* **Local settings** (`.claude/settings.local.json`): Per-machine overrides (not committed)

**Example**:

```json
{
  "enabledPlugins": {
    "code-formatter@team-tools": true,
    "deployment-tools@team-tools": true,
    "experimental-features@personal": false
  }
}
```

#### `extraKnownMarketplaces`

Defines additional marketplaces that should be made available for the repository. Typically used in repository-level settings to ensure team members have access to required plugin sources.

**When a repository includes `extraKnownMarketplaces`**:

1. Team members are prompted to install the marketplace when they trust the folder
2. Team members are then prompted to install plugins from that marketplace
3. Users can skip unwanted marketplaces or plugins (stored in user settings)
4. Installation respects trust boundaries and requires explicit consent

**Example**:

```json
{
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": {
        "source": "github",
        "repo": "company-org/claude-plugins"
      }
    },
    "security-plugins": {
      "source": {
        "source": "git",
        "url": "https://git.company.com/security/plugins.git"
      }
    }
  }
}
```

**Marketplace source types**:

* `github`: GitHub repository (uses `repo`)
* `git`: Any git URL (uses `url`)
* `directory`: Local filesystem path (uses `path`, for development only)

### Managing plugins

Use the `/plugin` command to manage plugins interactively:

* Browse available plugins from marketplaces
* Install/uninstall plugins
* Enable/disable plugins
* View plugin details (commands, agents, hooks provided)
* Add/remove marketplaces

Learn more about the plugin system in the [plugins documentation](/en/plugins).

## Environment variables

Claude Code supports the following environment variables to control its behavior:


> **Note:** All environment variables can also be configured in [`settings.json`](#available-settings). This is useful as a way to automatically set environment variables for each session, or to roll out a set of environment variables for your whole team or organization.



| Variable                                   | Purpose                                                                                                                                                                                                                                                                                                                                                                                      |
| :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ANTHROPIC_API_KEY`                        | API key sent as `X-Api-Key` header, typically for the Claude SDK (for interactive usage, run `/login`)                                                                                                                                                                                                                                                                                       |
| `ANTHROPIC_AUTH_TOKEN`                     | Custom value for the `Authorization` header (the value you set here will be prefixed with `Bearer `)                                                                                                                                                                                                                                                                                         |
| `ANTHROPIC_CUSTOM_HEADERS`                 | Custom headers you want to add to the request (in `Name: Value` format)                                                                                                                                                                                                                                                                                                                      |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL`            | See [Model configuration](/en/model-config#environment-variables)                                                                                                                                                                                                                                                                                                                            |
| `ANTHROPIC_DEFAULT_OPUS_MODEL`             | See [Model configuration](/en/model-config#environment-variables)                                                                                                                                                                                                                                                                                                                            |
| `ANTHROPIC_DEFAULT_SONNET_MODEL`           | See [Model configuration](/en/model-config#environment-variables)                                                                                                                                                                                                                                                                                                                            |
| `ANTHROPIC_MODEL`                          | Name of the model setting to use (see [Model Configuration](/en/model-config#environment-variables))                                                                                                                                                                                                                                                                                         |
| `ANTHROPIC_SMALL_FAST_MODEL`               | \[DEPRECATED] Name of [Haiku-class model for background tasks](/en/costs)                                                                                                                                                                                                                                                                                                                    |
| `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION`    | Override AWS region for the Haiku-class model when using Bedrock                                                                                                                                                                                                                                                                                                                             |
| `AWS_BEARER_TOKEN_BEDROCK`                 | Bedrock API key for authentication (see [Bedrock API keys](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/))                                                                                                                                                                                                                           |
| `BASH_DEFAULT_TIMEOUT_MS`                  | Default timeout for long-running bash commands                                                                                                                                                                                                                                                                                                                                               |
| `BASH_MAX_OUTPUT_LENGTH`                   | Maximum number of characters in bash outputs before they are middle-truncated                                                                                                                                                                                                                                                                                                                |
| `BASH_MAX_TIMEOUT_MS`                      | Maximum timeout the model can set for long-running bash commands                                                                                                                                                                                                                                                                                                                             |
| `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | Return to the original working directory after each Bash command                                                                                                                                                                                                                                                                                                                             |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`        | Interval in milliseconds at which credentials should be refreshed (when using `apiKeyHelper`)                                                                                                                                                                                                                                                                                                |
| `CLAUDE_CODE_CLIENT_CERT`                  | Path to client certificate file for mTLS authentication                                                                                                                                                                                                                                                                                                                                      |
| `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`        | Passphrase for encrypted CLAUDE\_CODE\_CLIENT\_KEY (optional)                                                                                                                                                                                                                                                                                                                                |
| `CLAUDE_CODE_CLIENT_KEY`                   | Path to client private key file for mTLS authentication                                                                                                                                                                                                                                                                                                                                      |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Equivalent of setting `DISABLE_AUTOUPDATER`, `DISABLE_BUG_COMMAND`, `DISABLE_ERROR_REPORTING`, and `DISABLE_TELEMETRY`                                                                                                                                                                                                                                                                       |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE`       | Set to `1` to disable automatic terminal title updates based on conversation context                                                                                                                                                                                                                                                                                                         |
| `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL`        | Skip auto-installation of IDE extensions                                                                                                                                                                                                                                                                                                                                                     |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS`            | Set the maximum number of output tokens for most requests                                                                                                                                                                                                                                                                                                                                    |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH`            | Skip AWS authentication for Bedrock (e.g. when using an LLM gateway)                                                                                                                                                                                                                                                                                                                         |
| `CLAUDE_CODE_SKIP_VERTEX_AUTH`             | Skip Google authentication for Vertex (e.g. when using an LLM gateway)                                                                                                                                                                                                                                                                                                                       |
| `CLAUDE_CODE_SUBAGENT_MODEL`               | See [Model configuration](/en/model-config)                                                                                                                                                                                                                                                                                                                                                  |
| `CLAUDE_CODE_USE_BEDROCK`                  | Use [Bedrock](/en/amazon-bedrock)                                                                                                                                                                                                                                                                                                                                                            |
| `CLAUDE_CODE_USE_VERTEX`                   | Use [Vertex](/en/google-vertex-ai)                                                                                                                                                                                                                                                                                                                                                           |
| `DISABLE_AUTOUPDATER`                      | Set to `1` to disable automatic updates.                                                                                                                                                                                                                                                                                                                                                     |
| `DISABLE_BUG_COMMAND`                      | Set to `1` to disable the `/bug` command                                                                                                                                                                                                                                                                                                                                                     |
| `DISABLE_COST_WARNINGS`                    | Set to `1` to disable cost warning messages                                                                                                                                                                                                                                                                                                                                                  |
| `DISABLE_ERROR_REPORTING`                  | Set to `1` to opt out of Sentry error reporting                                                                                                                                                                                                                                                                                                                                              |
| `DISABLE_NON_ESSENTIAL_MODEL_CALLS`        | Set to `1` to disable model calls for non-critical paths like flavor text                                                                                                                                                                                                                                                                                                                    |
| `DISABLE_PROMPT_CACHING`                   | Set to `1` to disable prompt caching for all models (takes precedence over per-model settings)                                                                                                                                                                                                                                                                                               |
| `DISABLE_PROMPT_CACHING_HAIKU`             | Set to `1` to disable prompt caching for Haiku models                                                                                                                                                                                                                                                                                                                                        |
| `DISABLE_PROMPT_CACHING_OPUS`              | Set to `1` to disable prompt caching for Opus models                                                                                                                                                                                                                                                                                                                                         |
| `DISABLE_PROMPT_CACHING_SONNET`            | Set to `1` to disable prompt caching for Sonnet models                                                                                                                                                                                                                                                                                                                                       |
| `DISABLE_TELEMETRY`                        | Set to `1` to opt out of Statsig telemetry (note that Statsig events do not include user data like code, file paths, or bash commands)                                                                                                                                                                                                                                                       |
| `HTTP_PROXY`                               | Specify HTTP proxy server for network connections                                                                                                                                                                                                                                                                                                                                            |
| `HTTPS_PROXY`                              | Specify HTTPS proxy server for network connections                                                                                                                                                                                                                                                                                                                                           |
| `MAX_MCP_OUTPUT_TOKENS`                    | Maximum number of tokens allowed in MCP tool responses. Claude Code displays a warning when output exceeds 10,000 tokens (default: 25000)                                                                                                                                                                                                                                                    |
| `MAX_THINKING_TOKENS`                      | Enable [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) and set the token budget for the thinking process. Extended thinking improves performance on complex reasoning and coding tasks but impacts [prompt caching efficiency](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks). Disabled by default. |
| `MCP_TIMEOUT`                              | Timeout in milliseconds for MCP server startup                                                                                                                                                                                                                                                                                                                                               |
| `MCP_TOOL_TIMEOUT`                         | Timeout in milliseconds for MCP tool execution                                                                                                                                                                                                                                                                                                                                               |
| `NO_PROXY`                                 | List of domains and IPs to which requests will be directly issued, bypassing proxy                                                                                                                                                                                                                                                                                                           |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET`           | Maximum number of characters for slash command metadata shown to [SlashCommand tool](/en/slash-commands#slashcommand-tool) (default: 15000)                                                                                                                                                                                                                                                  |
| `USE_BUILTIN_RIPGREP`                      | Set to `0` to use system-installed `rg` intead of `rg` included with Claude Code                                                                                                                                                                                                                                                                                                             |
| `VERTEX_REGION_CLAUDE_3_5_HAIKU`           | Override region for Claude 3.5 Haiku when using Vertex AI                                                                                                                                                                                                                                                                                                                                    |
| `VERTEX_REGION_CLAUDE_3_7_SONNET`          | Override region for Claude 3.7 Sonnet when using Vertex AI                                                                                                                                                                                                                                                                                                                                   |
| `VERTEX_REGION_CLAUDE_4_0_OPUS`            | Override region for Claude 4.0 Opus when using Vertex AI                                                                                                                                                                                                                                                                                                                                     |
| `VERTEX_REGION_CLAUDE_4_0_SONNET`          | Override region for Claude 4.0 Sonnet when using Vertex AI                                                                                                                                                                                                                                                                                                                                   |
| `VERTEX_REGION_CLAUDE_4_1_OPUS`            | Override region for Claude 4.1 Opus when using Vertex AI                                                                                                                                                                                                                                                                                                                                     |

## Tools available to Claude

Claude Code has access to a set of powerful tools that help it understand and modify your codebase:

| Tool             | Description                                                         | Permission Required |
| :--------------- | :------------------------------------------------------------------ | :------------------ |
| **Bash**         | Executes shell commands in your environment                         | Yes                 |
| **Edit**         | Makes targeted edits to specific files                              | Yes                 |
| **Glob**         | Finds files based on pattern matching                               | No                  |
| **Grep**         | Searches for patterns in file contents                              | No                  |
| **NotebookEdit** | Modifies Jupyter notebook cells                                     | Yes                 |
| **NotebookRead** | Reads and displays Jupyter notebook contents                        | No                  |
| **Read**         | Reads the contents of files                                         | No                  |
| **SlashCommand** | Runs a [custom slash command](/en/slash-commands#slashcommand-tool) | Yes                 |
| **Task**         | Runs a sub-agent to handle complex, multi-step tasks                | No                  |
| **TodoWrite**    | Creates and manages structured task lists                           | No                  |
| **WebFetch**     | Fetches content from a specified URL                                | Yes                 |
| **WebSearch**    | Performs web searches with domain filtering                         | Yes                 |
| **Write**        | Creates or overwrites files                                         | Yes                 |

Permission rules can be configured using `/allowed-tools` or in [permission settings](/en/settings#available-settings). Also see [Tool-specific permission rules](/en/iam#tool-specific-permission-rules).

### Extending tools with hooks

You can run custom commands before or after any tool executes using
[Claude Code hooks](/en/hooks-guide).

For example, you could automatically run a Python formatter after Claude
modifies Python files, or prevent modifications to production configuration
files by blocking Write operations to certain paths.

## See also

* [Identity and Access Management](/en/iam#configuring-permissions) - Learn about Claude Code's permission system
* [IAM and access control](/en/iam#enterprise-managed-policy-settings) - Enterprise policy management
* [Troubleshooting](/en/troubleshooting#auto-updater-issues) - Solutions for common configuration issues


# Status line configuration
Source: https://code.claude.com/docs/en/statusline

Create a custom status line for Claude Code to display contextual information

Make Claude Code your own with a custom status line that displays at the bottom of the Claude Code interface, similar to how terminal prompts (PS1) work in shells like Oh-my-zsh.

## Create a custom status line

You can either:

* Run `/statusline` to ask Claude Code to help you set up a custom status line. By default, it will try to reproduce your terminal's prompt, but you can provide additional instructions about the behavior you want to Claude Code, such as `/statusline show the model name in orange`

* Directly add a `statusLine` command to your `.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0 // Optional: set to 0 to let status line go to edge
  }
}
```

## How it Works

* The status line is updated when the conversation messages update
* Updates run at most every 300ms
* The first line of stdout from your command becomes the status line text
* ANSI color codes are supported for styling your status line
* Claude Code passes contextual information about the current session (model, directories, etc.) as JSON to your script via stdin

## JSON Input Structure

Your status line command receives structured data via stdin in JSON format:

```json
{
  "hook_event_name": "Status",
  "session_id": "abc123...",
  "transcript_path": "/path/to/transcript.json",
  "cwd": "/current/working/directory",
  "model": {
    "id": "claude-opus-4-1",
    "display_name": "Opus"
  },
  "workspace": {
    "current_dir": "/current/working/directory",
    "project_dir": "/original/project/directory"
  },
  "version": "1.0.80",
  "output_style": {
    "name": "default"
  },
  "cost": {
    "total_cost_usd": 0.01234,
    "total_duration_ms": 45000,
    "total_api_duration_ms": 2300,
    "total_lines_added": 156,
    "total_lines_removed": 23
  }
}
```

## Example Scripts

### Simple Status Line

```bash
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}"
```

### Git-Aware Status Line

```bash
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

# Show git branch if in a git repo
GIT_BRANCH=""
if git rev-parse --git-dir > /dev/null 2>&1; then
    BRANCH=$(git branch --show-current 2>/dev/null)
    if [ -n "$BRANCH" ]; then
        GIT_BRANCH=" | 🌿 $BRANCH"
    fi
fi

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}$GIT_BRANCH"
```

### Python Example

```python
#!/usr/bin/env python3
import json
import sys
import os

# Read JSON from stdin
data = json.load(sys.stdin)

# Extract values
model = data['model']['display_name']
current_dir = os.path.basename(data['workspace']['current_dir'])

# Check for git branch
git_branch = ""
if os.path.exists('.git'):
    try:
        with open('.git/HEAD', 'r') as f:
            ref = f.read().strip()
            if ref.startswith('ref: refs/heads/'):
                git_branch = f" | 🌿 {ref.replace('ref: refs/heads/', '')}"
    except:
        pass

print(f"[{model}] 📁 {current_dir}{git_branch}")
```

### Node.js Example

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Read JSON from stdin
let input = '';
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
    const data = JSON.parse(input);
    
    // Extract values
    const model = data.model.display_name;
    const currentDir = path.basename(data.workspace.current_dir);
    
    // Check for git branch
    let gitBranch = '';
    try {
        const headContent = fs.readFileSync('.git/HEAD', 'utf8').trim();
        if (headContent.startsWith('ref: refs/heads/')) {
            gitBranch = ` | 🌿 ${headContent.replace('ref: refs/heads/', '')}`;
        }
    } catch (e) {
        // Not a git repo or can't read HEAD
    }
    
    console.log(`[${model}] 📁 ${currentDir}${gitBranch}`);
});
```

### Helper Function Approach

For more complex bash scripts, you can create helper functions:

```bash
#!/bin/bash
# Read JSON input once
input=$(cat)

# Helper functions for common extractions
get_model_name() { echo "$input" | jq -r '.model.display_name'; }
get_current_dir() { echo "$input" | jq -r '.workspace.current_dir'; }
get_project_dir() { echo "$input" | jq -r '.workspace.project_dir'; }
get_version() { echo "$input" | jq -r '.version'; }
get_cost() { echo "$input" | jq -r '.cost.total_cost_usd'; }
get_duration() { echo "$input" | jq -r '.cost.total_duration_ms'; }
get_lines_added() { echo "$input" | jq -r '.cost.total_lines_added'; }
get_lines_removed() { echo "$input" | jq -r '.cost.total_lines_removed'; }

# Use the helpers
MODEL=$(get_model_name)
DIR=$(get_current_dir)
echo "[$MODEL] 📁 ${DIR##*/}"
```

## Tips

* Keep your status line concise - it should fit on one line
* Use emojis (if your terminal supports them) and colors to make information scannable
* Use `jq` for JSON parsing in Bash (see examples above)
* Test your script by running it manually with mock JSON input: `echo '{"model":{"display_name":"Test"},"workspace":{"current_dir":"/test"}}' | ./statusline.sh`
* Consider caching expensive operations (like git status) if needed

## Troubleshooting

* If your status line doesn't appear, check that your script is executable (`chmod +x`)
* Ensure your script outputs to stdout (not stderr)




---

[← Previous: Features](./02-features.md) | [📑 Index](./index.md) | [Next: Deployment →](./04-deployment.md)
