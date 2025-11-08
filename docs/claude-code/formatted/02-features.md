---
title: "Features"
description: "Core features and capabilities"
weight: 2
---

# Features

# Checkpointing
Source: https://code.claude.com/docs/en/checkpointing

Automatically track and rewind Claude's edits to quickly recover from unwanted changes.

Claude Code automatically tracks Claude's file edits as you work, allowing you to quickly undo changes and rewind to previous states if anything gets off track.

## How checkpoints work

As you work with Claude, checkpointing automatically captures the state of your code before each edit. This safety net lets you pursue ambitious, wide-scale tasks knowing you can always return to a prior code state.

### Automatic tracking

Claude Code tracks all changes made by its file editing tools:

* Every user prompt creates a new checkpoint
* Checkpoints persist across sessions, so you can access them in resumed conversations
* Automatically cleaned up along with sessions after 30 days (configurable)

### Rewinding changes

Press `Esc` twice (`Esc` + `Esc`) or use the `/rewind` command to open up the rewind menu. You can choose to restore:

* **Conversation only**: Rewind to a user message while keeping code changes
* **Code only**: Revert file changes while keeping the conversation
* **Both code and conversation**: Restore both to a prior point in the session

## Common use cases

Checkpoints are particularly useful when:

* **Exploring alternatives**: Try different implementation approaches without losing your starting point
* **Recovering from mistakes**: Quickly undo changes that introduced bugs or broke functionality
* **Iterating on features**: Experiment with variations knowing you can revert to working states

## Limitations

### Bash command changes not tracked

Checkpointing does not track files modified by bash commands. For example, if Claude Code runs:

```bash
rm file.txt
mv old.txt new.txt
cp source.txt dest.txt
```

These file modifications cannot be undone through rewind. Only direct file edits made through Claude's file editing tools are tracked.

### External changes not tracked

Checkpointing only tracks files that have been edited within the current session. Manual changes you make to files outside of Claude Code and edits from other concurrent sessions are normally not captured, unless they happen to modify the same files as the current session.

### Not a replacement for version control

Checkpoints are designed for quick, session-level recovery. For permanent version history and collaboration:

* Continue using version control (ex. Git) for commits, branches, and long-term history
* Checkpoints complement but don't replace proper version control
* Think of checkpoints as "local undo" and Git as "permanent history"

## See also

* [Interactive mode](/en/interactive-mode) - Keyboard shortcuts and session controls
* [Slash commands](/en/slash-commands) - Accessing checkpoints using `/rewind`
* [CLI reference](/en/cli-reference) - Command-line options


# Headless mode
Source: https://code.claude.com/docs/en/headless

Run Claude Code programmatically without interactive UI

## Overview

The headless mode allows you to run Claude Code programmatically from command line scripts and automation tools without any interactive UI.

## Basic usage

The primary command-line interface to Claude Code is the `claude` command. Use the `--print` (or `-p`) flag to run in non-interactive mode and print the final result:

```bash
claude -p "Stage my changes and write a set of commits for them" \
  --allowedTools "Bash,Read" \
  --permission-mode acceptEdits
```

## Configuration Options

Headless mode leverages all the CLI options available in Claude Code. Here are the key ones for automation and scripting:

| Flag                       | Description                                                                                            | Example                                                                                                                   |
| :------------------------- | :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| `--print`, `-p`            | Run in non-interactive mode                                                                            | `claude -p "query"`                                                                                                       |
| `--output-format`          | Specify output format (`text`, `json`, `stream-json`)                                                  | `claude -p --output-format json`                                                                                          |
| `--resume`, `-r`           | Resume a conversation by session ID                                                                    | `claude --resume abc123`                                                                                                  |
| `--continue`, `-c`         | Continue the most recent conversation                                                                  | `claude --continue`                                                                                                       |
| `--verbose`                | Enable verbose logging                                                                                 | `claude --verbose`                                                                                                        |
| `--append-system-prompt`   | Append to system prompt (only with `--print`)                                                          | `claude --append-system-prompt "Custom instruction"`                                                                      |
| `--allowedTools`           | Space-separated list of allowed tools, or <br /><br /> string of comma-separated list of allowed tools | `claude --allowedTools mcp__slack mcp__filesystem`<br /><br />`claude --allowedTools "Bash(npm install),mcp__filesystem"` |
| `--disallowedTools`        | Space-separated list of denied tools, or <br /><br /> string of comma-separated list of denied tools   | `claude --disallowedTools mcp__splunk mcp__github`<br /><br />`claude --disallowedTools "Bash(git commit),mcp__github"`   |
| `--mcp-config`             | Load MCP servers from a JSON file                                                                      | `claude --mcp-config servers.json`                                                                                        |
| `--permission-prompt-tool` | MCP tool for handling permission prompts (only with `--print`)                                         | `claude --permission-prompt-tool mcp__auth__prompt`                                                                       |

For a complete list of CLI options and features, see the [CLI reference](/en/cli-reference) documentation.

## Multi-turn conversations

For multi-turn conversations, you can resume conversations or continue from the most recent session:

```bash
# Continue the most recent conversation
claude --continue "Now refactor this for better performance"

# Resume a specific conversation by session ID
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"

# Resume in non-interactive mode
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Fix all linting issues" --no-interactive
```

## Output Formats

### Text Output (Default)

```bash
claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...
```

### JSON Output

Returns structured data including metadata:

```bash
claude -p "How does the data layer work?" --output-format json
```

Response format:

```json
{
  "type": "result",
  "subtype": "success",
  "total_cost_usd": 0.003,
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 800,
  "num_turns": 6,
  "result": "The response text here...",
  "session_id": "abc123"
}
```

### Streaming JSON Output

Streams each message as it is received:

```bash
claude -p "Build an application" --output-format stream-json
```

Each conversation begins with an initial `init` system message, followed by a list of user and assistant messages, followed by a final `result` system message with stats. Each message is emitted as a separate JSON object.

## Input Formats

### Text Input (Default)

```bash
# Direct argument
claude -p "Explain this code"

# From stdin
echo "Explain this code" | claude -p
```

### Streaming JSON Input

A stream of messages provided via `stdin` where each message represents a user turn. This allows multiple turns of a conversation without re-launching the `claude` binary and allows providing guidance to the model while it is processing a request.

Each message is a JSON 'User message' object, following the same format as the output message schema. Messages are formatted using the [jsonl](https://jsonlines.org/) format where each line of input is a complete JSON object. Streaming JSON input requires `-p` and `--output-format stream-json`.

```bash
echo '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Explain this code"}]}}' | claude -p --output-format=stream-json --input-format=stream-json --verbose
```

## Agent Integration Examples

### SRE Incident Response Bot

```bash
#!/bin/bash

# Automated incident response agent
investigate_incident() {
    local incident_description="$1"
    local severity="${2:-medium}"

    claude -p "Incident: $incident_description (Severity: $severity)" \
      --append-system-prompt "You are an SRE expert. Diagnose the issue, assess impact, and provide immediate action items." \
      --output-format json \
      --allowedTools "Bash,Read,WebSearch,mcp__datadog" \
      --mcp-config monitoring-tools.json
}

# Usage
investigate_incident "Payment API returning 500 errors" "high"
```

### Automated Security Review

```bash
# Security audit agent for pull requests
audit_pr() {
    local pr_number="$1"

    gh pr diff "$pr_number" | claude -p \
      --append-system-prompt "You are a security engineer. Review this PR for vulnerabilities, insecure patterns, and compliance issues." \
      --output-format json \
      --allowedTools "Read,Grep,WebSearch"
}

# Usage and save to file
audit_pr 123 > security-report.json
```

### Multi-turn Legal Assistant

```bash
# Legal document review with session persistence
session_id=$(claude -p "Start legal review session" --output-format json | jq -r '.session_id')

# Review contract in multiple steps
claude -p --resume "$session_id" "Review contract.pdf for liability clauses"
claude -p --resume "$session_id" "Check compliance with GDPR requirements"
claude -p --resume "$session_id" "Generate executive summary of risks"
```

## Best Practices

* **Use JSON output format** for programmatic parsing of responses:

  ```bash
  # Parse JSON response with jq
  result=$(claude -p "Generate code" --output-format json)
  code=$(echo "$result" | jq -r '.result')
  cost=$(echo "$result" | jq -r '.cost_usd')
  ```

* **Handle errors gracefully** - check exit codes and stderr:

  ```bash
  if ! claude -p "$prompt" 2>error.log; then
      echo "Error occurred:" >&2
      cat error.log >&2
      exit 1
  fi
  ```

* **Use session management** for maintaining context in multi-turn conversations

* **Consider timeouts** for long-running operations:

  ```bash
  timeout 300 claude -p "$complex_prompt" || echo "Timed out after 5 minutes"
  ```

* **Respect rate limits** when making multiple requests by adding delays between calls

## Related Resources

* [CLI usage and controls](/en/cli-reference) - Complete CLI documentation
* [Common workflows](/en/common-workflows) - Step-by-step guides for common use cases


# Interactive mode
Source: https://code.claude.com/docs/en/interactive-mode

Complete reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions.

## Keyboard shortcuts


> **Note:** Keyboard shortcuts may vary by platform and terminal. Press `?` to see available shortcuts for your environment.



### General controls

| Shortcut                                     | Description                                                                                     | Context                                                     |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `Ctrl+C`                                     | Cancel current input or generation                                                              | Standard interrupt                                          |
| `Ctrl+D`                                     | Exit Claude Code session                                                                        | EOF signal                                                  |
| `Ctrl+L`                                     | Clear terminal screen                                                                           | Keeps conversation history                                  |
| `Ctrl+O`                                     | Toggle verbose output                                                                           | Shows detailed tool usage and execution                     |
| `Ctrl+R`                                     | Reverse search command history                                                                  | Search through previous commands interactively              |
| `Ctrl+V` (macOS/Linux) or `Alt+V` (Windows)  | Paste image from clipboard                                                                      | Pastes an image or path to an image file                    |
| `Up/Down arrows`                             | Navigate command history                                                                        | Recall previous inputs                                      |
| `Esc` + `Esc`                                | Rewind the code/conversation                                                                    | Restore the code and/or conversation to a previous point    |
| `Tab`                                        | Toggle [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) | Switch between Thinking on and Thinking off                 |
| `Shift+Tab` or `Alt+M` (some configurations) | Toggle permission modes                                                                         | Switch between Auto-Accept Mode, Plan Mode, and normal mode |

### Multiline input

| Method           | Shortcut       | Context                           |
| :--------------- | :------------- | :-------------------------------- |
| Quick escape     | `\` + `Enter`  | Works in all terminals            |
| macOS default    | `Option+Enter` | Default on macOS                  |
| Terminal setup   | `Shift+Enter`  | After `/terminal-setup`           |
| Control sequence | `Ctrl+J`       | Line feed character for multiline |
| Paste mode       | Paste directly | For code blocks, logs             |


> **💡 Tip:** Configure your preferred line break behavior in terminal settings. Run `/terminal-setup` to install Shift+Enter binding for iTerm2 and VS Code terminals.



### Quick commands

| Shortcut     | Description                        | Notes                                                         |
| :----------- | :--------------------------------- | :------------------------------------------------------------ |
| `#` at start | Memory shortcut - add to CLAUDE.md | Prompts for file selection                                    |
| `/` at start | Slash command                      | See [slash commands](/en/slash-commands)                      |
| `!` at start | Bash mode                          | Run commands directly and add execution output to the session |
| `@`          | File path mention                  | Trigger file path autocomplete                                |

## Vim editor mode

Enable vim-style editing with `/vim` command or configure permanently via `/config`.

### Mode switching

| Command | Action                      | From mode |
| :------ | :-------------------------- | :-------- |
| `Esc`   | Enter NORMAL mode           | INSERT    |
| `i`     | Insert before cursor        | NORMAL    |
| `I`     | Insert at beginning of line | NORMAL    |
| `a`     | Insert after cursor         | NORMAL    |
| `A`     | Insert at end of line       | NORMAL    |
| `o`     | Open line below             | NORMAL    |
| `O`     | Open line above             | NORMAL    |

### Navigation (NORMAL mode)

| Command         | Action                    |
| :-------------- | :------------------------ |
| `h`/`j`/`k`/`l` | Move left/down/up/right   |
| `w`             | Next word                 |
| `e`             | End of word               |
| `b`             | Previous word             |
| `0`             | Beginning of line         |
| `$`             | End of line               |
| `^`             | First non-blank character |
| `gg`            | Beginning of input        |
| `G`             | End of input              |

### Editing (NORMAL mode)

| Command        | Action                  |
| :------------- | :---------------------- |
| `x`            | Delete character        |
| `dd`           | Delete line             |
| `D`            | Delete to end of line   |
| `dw`/`de`/`db` | Delete word/to end/back |
| `cc`           | Change line             |
| `C`            | Change to end of line   |
| `cw`/`ce`/`cb` | Change word/to end/back |
| `.`            | Repeat last change      |

## Command history

Claude Code maintains command history for the current session:

* History is stored per working directory
* Cleared with `/clear` command
* Use Up/Down arrows to navigate (see keyboard shortcuts above)
* **Note**: History expansion (`!`) is disabled by default

### Reverse search with Ctrl+R

Press `Ctrl+R` to interactively search through your command history:

1. **Start search**: Press `Ctrl+R` to activate reverse history search
2. **Type query**: Enter text to search for in previous commands - the search term will be highlighted in matching results
3. **Navigate matches**: Press `Ctrl+R` again to cycle through older matches
4. **Accept match**:
   * Press `Tab` or `Esc` to accept the current match and continue editing
   * Press `Enter` to accept and execute the command immediately
5. **Cancel search**:
   * Press `Ctrl+C` to cancel and restore your original input
   * Press `Backspace` on empty search to cancel

The search displays matching commands with the search term highlighted, making it easy to find and reuse previous inputs.

## Background bash commands

Claude Code supports running bash commands in the background, allowing you to continue working while long-running processes execute.

### How backgrounding works

When Claude Code runs a command in the background, it runs the command asynchronously and immediately returns a background task ID. Claude Code can respond to new prompts while the command continues executing in the background.

To run commands in the background, you can either:

* Prompt Claude Code to run a command in the background
* Press Ctrl+B to move a regular Bash tool invocation to the background. (Tmux users must press Ctrl+B twice due to tmux's prefix key.)

**Key features:**

* Output is buffered and Claude can retrieve it using the BashOutput tool
* Background tasks have unique IDs for tracking and output retrieval
* Background tasks are automatically cleaned up when Claude Code exits

**Common backgrounded commands:**

* Build tools (webpack, vite, make)
* Package managers (npm, yarn, pnpm)
* Test runners (jest, pytest)
* Development servers
* Long-running processes (docker, terraform)

### Bash mode with `!` prefix

Run bash commands directly without going through Claude by prefixing your input with `!`:

```bash
! npm test
! git status
! ls -la
```

Bash mode:

* Adds the command and its output to the conversation context
* Shows real-time progress and output
* Supports the same `Ctrl+B` backgrounding for long-running commands
* Does not require Claude to interpret or approve the command

This is useful for quick shell operations while maintaining conversation context.

## See also

* [Slash commands](/en/slash-commands) - Interactive session commands
* [Checkpointing](/en/checkpointing) - Rewind Claude's edits and restore previous states
* [CLI reference](/en/cli-reference) - Command-line flags and options
* [Settings](/en/settings) - Configuration options
* [Memory management](/en/memory) - Managing CLAUDE.md files


# Sandboxing
Source: https://code.claude.com/docs/en/sandboxing

Learn how Claude Code's sandboxed bash tool provides filesystem and network isolation for safer, more autonomous agent execution.

## Overview

Claude Code features native sandboxing to provide a more secure environment for agent execution while reducing the need for constant permission prompts. Instead of asking permission for each bash command, sandboxing creates defined boundaries upfront where Claude Code can work more freely with reduced risk.

The sandboxed bash tool uses OS-level primitives to enforce both filesystem and network isolation.

## Why sandboxing matters

Traditional permission-based security requires constant user approval for bash commands. While this provides control, it can lead to:

* **Approval fatigue**: Repeatedly clicking "approve" can cause users to pay less attention to what they're approving
* **Reduced productivity**: Constant interruptions slow down development workflows
* **Limited autonomy**: Claude Code cannot work as efficiently when waiting for approvals

Sandboxing addresses these challenges by:

1. **Defining clear boundaries**: Specify exactly which directories and network hosts Claude Code can access
2. **Reducing permission prompts**: Safe commands within the sandbox don't require approval
3. **Maintaining security**: Attempts to access resources outside the sandbox trigger immediate notifications
4. **Enabling autonomy**: Claude Code can run more independently within defined limits


> **⚠️ Warning:** Effective sandboxing requires **both** filesystem and network isolation. Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys. Without filesystem isolation, a compromised agent could backdoor system resources to gain network access. When configuring sandboxing it is important to ensure that your configured settings do not create bypasses in these systems.



## How it works

### Filesystem isolation

The sandboxed bash tool restricts file system access to specific directories:

* **Default writes behavior**: Read and write access to the current working directory and its subdirectories
* **Default read behavior**: Read access to the entire computer, except certain denied directories
* **Blocked access**: Cannot modify files outside the current working directory without explicit permission
* **Configurable**: Define custom allowed and denied paths through settings

### Network isolation

Network access is controlled through a proxy server running outside the sandbox:

* **Domain restrictions**: Only approved domains can be accessed
* **User confirmation**: New domain requests trigger permission prompts
* **Custom proxy support**: Advanced users can implement custom rules on outgoing traffic
* **Comprehensive coverage**: Restrictions apply to all scripts, programs, and subprocesses spawned by commands

### OS-level enforcement

The sandboxed bash tool leverages operating system security primitives:

* **Linux**: Uses [bubblewrap](https://github.com/containers/bubblewrap) for isolation
* **macOS**: Uses Seatbelt for sandbox enforcement

These OS-level restrictions ensure that all child processes spawned by Claude Code's commands inherit the same security boundaries.

## Getting started

### Enable sandboxing

You can enable sandboxing by running the `/sandbox` slash command:

```
> /sandbox
```

This activates the sandboxed bash tool with default settings, allowing access to your current working directory while blocking access to sensitive system locations.

### Configure sandboxing

Customize sandbox behavior through your `settings.json` file. See [Settings](/en/settings#sandbox-settings) for complete configuration reference.


> **💡 Tip:** Not all commands are compatible with sandboxing out of the box. Some notes that may help you make the most out of the sandbox:

  * Many CLI tools require accessing certain hosts. As you use these tools, they will request permission to access certain hosts. Granting permission will allow them to access these hosts now and in the future, enabling them to safely execute inside the sandbox.
  * `watchman` is incompatible with running in the sandbox. If you're running `jest`, consider using `jest --no-watchman`
  * `docker` is incompatible with running in the sandbox. Consider specifying `docker` in `excludedCommands` to force it to run outside of the sandbox.




> **Note:** Claude Code includes an intentional escape hatch mechanism that allows commands to run outside the sandbox when necessary. When a command fails due to sandbox restrictions (such as network connectivity issues or incompatible tools), Claude is prompted to analyze the failure and may retry the command with the `dangerouslyDisableSandbox` parameter. Commands that use this parameter go through the normal Claude Code permissions flow requiring user permission to execute. This allows Claude Code to handle edge cases where certain tools or network operations cannot function within sandbox constraints.

  You can disable this escape hatch by setting `"allowUnsandboxedCommands": false` in your [sandbox settings](/en/settings#sandbox-settings). When disabled, the `dangerouslyDisableSandbox` parameter is completely ignored and all commands must run sandboxed or be explicitly listed in `excludedCommands`.



## Security benefits

### Protection against prompt injection

Even if an attacker successfully manipulates Claude Code's behavior through prompt injection, the sandbox ensures your system remains secure:

**Filesystem protection:**

* Cannot modify critical config files such as `~/.bashrc`
* Cannot modify system-level files in `/bin/`
* Cannot read files that are denied in your [Claude permission settings](/en/iam#configuring-permissions)

**Network protection:**

* Cannot exfiltrate data to attacker-controlled servers
* Cannot download malicious scripts from unauthorized domains
* Cannot make unexpected API calls to unapproved services
* Cannot contact any domains not explicitly allowed

**Monitoring and control:**

* All access attempts outside the sandbox are blocked at the OS level
* You receive immediate notifications when boundaries are tested
* You can choose to deny, allow once, or permanently update your configuration

### Reduced attack surface

Sandboxing limits the potential damage from:

* **Malicious dependencies**: NPM packages or other dependencies with harmful code
* **Compromised scripts**: Build scripts or tools with security vulnerabilities
* **Social engineering**: Attacks that trick users into running dangerous commands
* **Prompt injection**: Attacks that trick Claude into running dangerous commands

### Transparent operation

When Claude Code attempts to access network resources outside the sandbox:

1. The operation is blocked at the OS level
2. You receive an immediate notification
3. You can choose to:
   * Deny the request
   * Allow it once
   * Update your sandbox configuration to permanently allow it

## Security Limitations

* Network Sandboxing Limitations: The network filtering system operates by restricting the domains that processes are allowed to connect to. It does not otherwise inspect the traffic passing through the proxy and users are responsible for ensuring they only allow trusted domains in their policy.


> **⚠️ Warning:** Users should be aware of potential risks that come from allowing broad domains like `github.com` that may allow for data exfiltration. Also, in some cases it may be possible to bypass the network filtering through [domain fronting](https://en.wikipedia.org/wiki/Domain_fronting).



* Privilege Escalation via Unix Sockets: The `allowUnixSockets` configuration can inadvertently grant access to powerful system services that could lead to sandbox bypasses. For example, if it is used to allow access to `/var/run/docker.sock` this would effectively grant access to the host system through exploiting the docker socket. Users are encouraged to carefully consider any unix sockets that they allow through the sandbox.
* Filesystem Permission Escalation: Overly broad filesystem write permissions can enable privilege escalation attacks. Allowing writes to directories containing executables in `$PATH`, system configuration directories, or user shell configuration files (`.bashrc`, `.zshrc`) can lead to code execution in different security contexts when other users or system processes access these files.
* Linux Sandbox Strength: The Linux implementation provides strong filesystem and network isolation but includes an `enableWeakerNestedSandbox` mode that enables it to work inside of Docker environments without privileged namespaces. This option considerably weakens security and should only be used incases where additional isolation is otherwise enforced.

## Advanced usage

### Custom proxy configuration

For organizations requiring advanced network security, you can implement a custom proxy to:

* Decrypt and inspect HTTPS traffic
* Apply custom filtering rules
* Log all network requests
* Integrate with existing security infrastructure

```json
{
  "sandbox": {
    "network": {
      "httpProxyPort": 8080,
      "socksProxyPort": 8081
    }
  }
}
```

### Integration with existing security tools

The sandboxed bash tool works alongside:

* **IAM policies**: Combine with [permission settings](/en/iam) for defense-in-depth
* **Development containers**: Use with [devcontainers](/en/devcontainer) for additional isolation
* **Enterprise policies**: Enforce sandbox configurations through [managed settings](/en/settings#settings-precedence)

## Best practices

1. **Start restrictive**: Begin with minimal permissions and expand as needed
2. **Monitor logs**: Review sandbox violation attempts to understand Claude Code's needs
3. **Use environment-specific configs**: Different sandbox rules for development vs. production contexts
4. **Combine with permissions**: Use sandboxing alongside IAM policies for comprehensive security
5. **Test configurations**: Verify your sandbox settings don't block legitimate workflows

## Open source

The sandbox runtime is available as an open source npm package for use in your own agent projects. This enables the broader AI agent community to build safer, more secure autonomous systems. This can also be used to sandbox other programs you may wish to run. For example, to sandbox an MCP server you could run:

```bash
npx @anthropic-ai/sandbox-runtime <command-to-sandbox>
```

For implementation details and source code, visit the [GitHub repository](https://github.com/anthropic-experimental/sandbox-runtime).

## Limitations

* **Performance overhead**: Minimal, but some filesystem operations may be slightly slower
* **Compatibility**: Some tools that require specific system access patterns may need configuration adjustments, or may even need to be run outside of the sandbox
* **Platform support**: Currently supports Linux and macOS; Windows support planned

## See also

* [Security](/en/security) - Comprehensive security features and best practices
* [IAM](/en/iam) - Permission configuration and access control
* [Settings](/en/settings) - Complete configuration reference
* [CLI reference](/en/cli-reference) - Command-line options including `-sb`


# Agent Skills
Source: https://code.claude.com/docs/en/skills

Create, manage, and share Skills to extend Claude's capabilities in Claude Code.

This guide shows you how to create, use, and manage Agent Skills in Claude Code. Skills are modular capabilities that extend Claude's functionality through organized folders containing instructions, scripts, and resources.

## Prerequisites

* Claude Code version 1.0 or later
* Basic familiarity with [Claude Code](/en/quickstart)

## What are Agent Skills?

Agent Skills package expertise into discoverable capabilities. Each Skill consists of a `SKILL.md` file with instructions that Claude reads when relevant, plus optional supporting files like scripts and templates.

**How Skills are invoked**: Skills are **model-invoked**—Claude autonomously decides when to use them based on your request and the Skill's description. This is different from slash commands, which are **user-invoked** (you explicitly type `/command` to trigger them).

**Benefits**:

* Extend Claude's capabilities for your specific workflows
* Share expertise across your team via git
* Reduce repetitive prompting
* Compose multiple Skills for complex tasks

Learn more in the [Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).


> **Note:** For a deep dive into the architecture and real-world applications of Agent Skills, read our engineering blog: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).



## Create a Skill

Skills are stored as directories containing a `SKILL.md` file.

### Personal Skills

Personal Skills are available across all your projects. Store them in `~/.claude/skills/`:

```bash
mkdir -p ~/.claude/skills/my-skill-name
```

**Use personal Skills for**:

* Your individual workflows and preferences
* Experimental Skills you're developing
* Personal productivity tools

### Project Skills

Project Skills are shared with your team. Store them in `.claude/skills/` within your project:

```bash
mkdir -p .claude/skills/my-skill-name
```

**Use project Skills for**:

* Team workflows and conventions
* Project-specific expertise
* Shared utilities and scripts

Project Skills are checked into git and automatically available to team members.

### Plugin Skills

Skills can also come from [Claude Code plugins](/en/plugins). Plugins may bundle Skills that are automatically available when the plugin is installed. These Skills work the same way as personal and project Skills.

## Write SKILL.md

Create a `SKILL.md` file with YAML frontmatter and Markdown content:

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this Skill.
```

**Field requirements**:

* `name`: Must use lowercase letters, numbers, and hyphens only (max 64 characters)
* `description`: Brief description of what the Skill does and when to use it (max 1024 characters)

The `description` field is critical for Claude to discover when to use your Skill. It should include both what the Skill does and when Claude should use it.

See the [best practices guide](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) for complete authoring guidance including validation rules.

## Add supporting files

Create additional files alongside SKILL.md:

```
my-skill/
├── SKILL.md (required)
├── reference.md (optional documentation)
├── examples.md (optional examples)
├── scripts/
│   └── helper.py (optional utility)
└── templates/
    └── template.txt (optional template)
```

Reference these files from SKILL.md:

````markdown
For advanced usage, see [reference.md](reference.md).

Run the helper script:
```bash
python scripts/helper.py input.txt
```
````

Claude reads these files only when needed, using progressive disclosure to manage context efficiently.

## Restrict tool access with allowed-tools

Use the `allowed-tools` frontmatter field to limit which tools Claude can use when a Skill is active:

```yaml
---
name: safe-file-reader
description: Read files without making changes. Use when you need read-only file access.
allowed-tools: Read, Grep, Glob
---

# Safe File Reader

This Skill provides read-only file access.

## Instructions
1. Use Read to view file contents
2. Use Grep to search within files
3. Use Glob to find files by pattern
```

When this Skill is active, Claude can only use the specified tools (Read, Grep, Glob) without needing to ask for permission. This is useful for:

* Read-only Skills that shouldn't modify files
* Skills with limited scope (e.g., only data analysis, no file writing)
* Security-sensitive workflows where you want to restrict capabilities

If `allowed-tools` is not specified, Claude will ask for permission to use tools as normal, following the standard permission model.


> **Note:** `allowed-tools` is only supported for Skills in Claude Code.



## View available Skills

Skills are automatically discovered by Claude from three sources:

* Personal Skills: `~/.claude/skills/`
* Project Skills: `.claude/skills/`
* Plugin Skills: bundled with installed plugins

**To view all available Skills**, ask Claude directly:

```
What Skills are available?
```

or

```
List all available Skills
```

This will show all Skills from all sources, including plugin Skills.

**To inspect a specific Skill**, you can also check the filesystem:

```bash
# List personal Skills
ls ~/.claude/skills/

# List project Skills (if in a project directory)
ls .claude/skills/

# View a specific Skill's content
cat ~/.claude/skills/my-skill/SKILL.md
```

## Test a Skill

After creating a Skill, test it by asking questions that match your description.

**Example**: If your description mentions "PDF files":

```
Can you help me extract text from this PDF?
```

Claude autonomously decides to use your Skill if it matches the request—you don't need to explicitly invoke it. The Skill activates automatically based on the context of your question.

## Debug a Skill

If Claude doesn't use your Skill, check these common issues:

### Make description specific

**Too vague**:

```yaml
description: Helps with documents
```

**Specific**:

```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

Include both what the Skill does and when to use it in the description.

### Verify file path

**Personal Skills**: `~/.claude/skills/skill-name/SKILL.md`
**Project Skills**: `.claude/skills/skill-name/SKILL.md`

Check the file exists:

```bash
# Personal
ls ~/.claude/skills/my-skill/SKILL.md

# Project
ls .claude/skills/my-skill/SKILL.md
```

### Check YAML syntax

Invalid YAML prevents the Skill from loading. Verify the frontmatter:

```bash
cat SKILL.md | head -n 10
```

Ensure:

* Opening `---` on line 1
* Closing `---` before Markdown content
* Valid YAML syntax (no tabs, correct indentation)

### View errors

Run Claude Code with debug mode to see Skill loading errors:

```bash
claude --debug
```

## Share Skills with your team

**Recommended approach**: Distribute Skills through [plugins](/en/plugins).

To share Skills via plugin:

1. Create a plugin with Skills in the `skills/` directory
2. Add the plugin to a marketplace
3. Team members install the plugin

For complete instructions, see [Add Skills to your plugin](/en/plugins#add-skills-to-your-plugin).

You can also share Skills directly through project repositories:

### Step 1: Add Skill to your project

Create a project Skill:

```bash
mkdir -p .claude/skills/team-skill
# Create SKILL.md
```

### Step 2: Commit to git

```bash
git add .claude/skills/
git commit -m "Add team Skill for PDF processing"
git push
```

### Step 3: Team members get Skills automatically

When team members pull the latest changes, Skills are immediately available:

```bash
git pull
claude  # Skills are now available
```

## Update a Skill

Edit SKILL.md directly:

```bash
# Personal Skill
code ~/.claude/skills/my-skill/SKILL.md

# Project Skill
code .claude/skills/my-skill/SKILL.md
```

Changes take effect the next time you start Claude Code. If Claude Code is already running, restart it to load the updates.

## Remove a Skill

Delete the Skill directory:

```bash
# Personal
rm -rf ~/.claude/skills/my-skill

# Project
rm -rf .claude/skills/my-skill
git commit -m "Remove unused Skill"
```

## Best practices

### Keep Skills focused

One Skill should address one capability:

**Focused**:

* "PDF form filling"
* "Excel data analysis"
* "Git commit messages"

**Too broad**:

* "Document processing" (split into separate Skills)
* "Data tools" (split by data type or operation)

### Write clear descriptions

Help Claude discover when to use Skills by including specific triggers in your description:

**Clear**:

```yaml
description: Analyze Excel spreadsheets, create pivot tables, and generate charts. Use when working with Excel files, spreadsheets, or analyzing tabular data in .xlsx format.
```

**Vague**:

```yaml
description: For files
```

### Test with your team

Have teammates use Skills and provide feedback:

* Does the Skill activate when expected?
* Are the instructions clear?
* Are there missing examples or edge cases?

### Document Skill versions

You can document Skill versions in your SKILL.md content to track changes over time. Add a version history section:

```markdown
# My Skill

## Version History
- v2.0.0 (2025-10-01): Breaking changes to API
- v1.1.0 (2025-09-15): Added new features
- v1.0.0 (2025-09-01): Initial release
```

This helps team members understand what changed between versions.

## Troubleshooting

### Claude doesn't use my Skill

**Symptom**: You ask a relevant question but Claude doesn't use your Skill.

**Check**: Is the description specific enough?

Vague descriptions make discovery difficult. Include both what the Skill does and when to use it, with key terms users would mention.

**Too generic**:

```yaml
description: Helps with data
```

**Specific**:

```yaml
description: Analyze Excel spreadsheets, generate pivot tables, create charts. Use when working with Excel files, spreadsheets, or .xlsx files.
```

**Check**: Is the YAML valid?

Run validation to check for syntax errors:

```bash
# View frontmatter
cat .claude/skills/my-skill/SKILL.md | head -n 15

# Check for common issues
# - Missing opening or closing ---
# - Tabs instead of spaces
# - Unquoted strings with special characters
```

**Check**: Is the Skill in the correct location?

```bash
# Personal Skills
ls ~/.claude/skills/*/SKILL.md

# Project Skills
ls .claude/skills/*/SKILL.md
```

### Skill has errors

**Symptom**: The Skill loads but doesn't work correctly.

**Check**: Are dependencies available?

Claude will automatically install required dependencies (or ask for permission to install them) when it needs them.

**Check**: Do scripts have execute permissions?

```bash
chmod +x .claude/skills/my-skill/scripts/*.py
```

**Check**: Are file paths correct?

Use forward slashes (Unix style) in all paths:

**Correct**: `scripts/helper.py`
**Wrong**: `scripts\helper.py` (Windows style)

### Multiple Skills conflict

**Symptom**: Claude uses the wrong Skill or seems confused between similar Skills.

**Be specific in descriptions**: Help Claude choose the right Skill by using distinct trigger terms in your descriptions.

Instead of:

```yaml
# Skill 1
description: For data analysis

# Skill 2
description: For analyzing data
```

Use:

```yaml
# Skill 1
description: Analyze sales data in Excel files and CRM exports. Use for sales reports, pipeline analysis, and revenue tracking.

# Skill 2
description: Analyze log files and system metrics data. Use for performance monitoring, debugging, and system diagnostics.
```

## Examples

### Simple Skill (single file)

```
commit-helper/
└── SKILL.md
```

```yaml
---
name: generating-commit-messages
description: Generates clear commit messages from git diffs. Use when writing commit messages or reviewing staged changes.
---

# Generating Commit Messages

## Instructions

1. Run `git diff --staged` to see changes
2. I'll suggest a commit message with:
   - Summary under 50 characters
   - Detailed description
   - Affected components

## Best practices

- Use present tense
- Explain what and why, not how
```

### Skill with tool permissions

```
code-reviewer/
└── SKILL.md
```

```yaml
---
name: code-reviewer
description: Review code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
allowed-tools: Read, Grep, Glob
---

# Code Reviewer

## Review checklist

1. Code organization and structure
2. Error handling
3. Performance considerations
4. Security concerns
5. Test coverage

## Instructions

1. Read the target files using Read tool
2. Search for patterns using Grep
3. Find related files using Glob
4. Provide detailed feedback on code quality
```

### Multi-file Skill

```
pdf-processing/
├── SKILL.md
├── FORMS.md
├── REFERENCE.md
└── scripts/
    ├── fill_form.py
    └── validate.py
```

**SKILL.md**:

````yaml
---
name: pdf-processing
description: Extract text, fill forms, merge PDFs. Use when working with PDF files, forms, or document extraction. Requires pypdf and pdfplumber packages.
---

# PDF Processing

## Quick start

Extract text:
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For form filling, see [FORMS.md](FORMS.md).
For detailed API reference, see [REFERENCE.md](REFERENCE.md).

## Requirements

Packages must be installed in your environment:
```bash
pip install pypdf pdfplumber
```
````


> **Note:** List required packages in the description. Packages must be installed in your environment before Claude can use them.



Claude loads additional files only when needed.

## Next steps



  - **[Authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)**
    Write Skills that Claude can use effectively
  

  - **[Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)**
    Learn how Skills work across Claude products
  

  - **[Use Skills in the Agent SDK](https://docs.claude.com/en/docs/agent-sdk/skills)**
    Use Skills programmatically with TypeScript and Python
  

  - **[Get started with Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart)**
    Create your first Skill
  




# Slash commands
Source: https://code.claude.com/docs/en/slash-commands

Control Claude's behavior during an interactive session with slash commands.

## Built-in slash commands

| Command                   | Purpose                                                                                                                     |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| `/add-dir`                | Add additional working directories                                                                                          |
| `/agents`                 | Manage custom AI subagents for specialized tasks                                                                            |
| `/bashes`                 | List and manage background tasks                                                                                            |
| `/bug`                    | Report bugs (sends conversation to Anthropic)                                                                               |
| `/clear`                  | Clear conversation history                                                                                                  |
| `/compact [instructions]` | Compact conversation with optional focus instructions                                                                       |
| `/config`                 | Open the Settings interface (Config tab)                                                                                    |
| `/context`                | Visualize current context usage as a colored grid                                                                           |
| `/cost`                   | Show token usage statistics (see [cost tracking guide](/en/costs#using-the-cost-command) for subscription-specific details) |
| `/doctor`                 | Checks the health of your Claude Code installation                                                                          |
| `/exit`                   | Exit the REPL                                                                                                               |
| `/export [filename]`      | Export the current conversation to a file or clipboard                                                                      |
| `/help`                   | Get usage help                                                                                                              |
| `/hooks`                  | Manage hook configurations for tool events                                                                                  |
| `/init`                   | Initialize project with CLAUDE.md guide                                                                                     |
| `/login`                  | Switch Anthropic accounts                                                                                                   |
| `/logout`                 | Sign out from your Anthropic account                                                                                        |
| `/mcp`                    | Manage MCP server connections and OAuth authentication                                                                      |
| `/memory`                 | Edit CLAUDE.md memory files                                                                                                 |
| `/model`                  | Select or change the AI model                                                                                               |
| `/output-style [style]`   | Set the output style directly or from a selection menu                                                                      |
| `/permissions`            | View or update [permissions](/en/iam#configuring-permissions)                                                               |
| `/pr_comments`            | View pull request comments                                                                                                  |
| `/privacy-settings`       | View and update your privacy settings                                                                                       |
| `/review`                 | Request code review                                                                                                         |
| `/sandbox`                | Enable sandboxed bash tool with filesystem and network isolation for safer, more autonomous execution                       |
| `/rewind`                 | Rewind the conversation and/or code                                                                                         |
| `/status`                 | Open the Settings interface (Status tab) showing version, model, account, and connectivity                                  |
| `/statusline`             | Set up Claude Code's status line UI                                                                                         |
| `/terminal-setup`         | Install Shift+Enter key binding for newlines (iTerm2 and VSCode only)                                                       |
| `/todos`                  | List current todo items                                                                                                     |
| `/usage`                  | Show plan usage limits and rate limit status (subscription plans only)                                                      |
| `/vim`                    | Enter vim mode for alternating insert and command modes                                                                     |

## Custom slash commands

Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands are organized by scope (project-specific or personal) and support namespacing through directory structures.

### Syntax

```
/<command-name> [arguments]
```

#### Parameters

| Parameter        | Description                                                       |
| :--------------- | :---------------------------------------------------------------- |
| `<command-name>` | Name derived from the Markdown filename (without `.md` extension) |
| `[arguments]`    | Optional arguments passed to the command                          |

### Command types

#### Project commands

Commands stored in your repository and shared with your team. When listed in `/help`, these commands show "(project)" after their description.

**Location**: `.claude/commands/`

In the following example, we create the `/optimize` command:

```bash
# Create a project command
mkdir -p .claude/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .claude/commands/optimize.md
```

#### Personal commands

Commands available across all your projects. When listed in `/help`, these commands show "(user)" after their description.

**Location**: `~/.claude/commands/`

In the following example, we create the `/security-review` command:

```bash
# Create a personal command
mkdir -p ~/.claude/commands
echo "Review this code for security vulnerabilities:" > ~/.claude/commands/security-review.md
```

### Features

#### Namespacing

Organize commands in subdirectories. The subdirectories are used for organization and appear in the command description, but they do not affect the command name itself. The description will show whether the command comes from the project directory (`.claude/commands`) or the user-level directory (`~/.claude/commands`), along with the subdirectory name.

Conflicts between user and project level commands are not supported. Otherwise, multiple commands with the same base file name can coexist.

For example, a file at `.claude/commands/frontend/component.md` creates the command `/component` with description showing "(project:frontend)".
Meanwhile, a file at `~/.claude/commands/component.md` creates the command `/component` with description showing "(user)".

#### Arguments

Pass dynamic values to commands using argument placeholders:

##### All arguments with `$ARGUMENTS`

The `$ARGUMENTS` placeholder captures all arguments passed to the command:

```bash
# Command definition
echo 'Fix issue #$ARGUMENTS following our coding standards' > .claude/commands/fix-issue.md

# Usage
> /fix-issue 123 high-priority
# $ARGUMENTS becomes: "123 high-priority"
```

##### Individual arguments with `$1`, `$2`, etc.

Access specific arguments individually using positional parameters (similar to shell scripts):

```bash
# Command definition  
echo 'Review PR #$1 with priority $2 and assign to $3' > .claude/commands/review-pr.md

# Usage
> /review-pr 456 high alice
# $1 becomes "456", $2 becomes "high", $3 becomes "alice"
```

Use positional arguments when you need to:

* Access arguments individually in different parts of your command
* Provide defaults for missing arguments
* Build more structured commands with specific parameter roles

#### Bash command execution

Execute bash commands before the slash command runs using the `!` prefix. The output is included in the command context. You *must* include `allowed-tools` with the `Bash` tool, but you can choose the specific bash commands to allow.

For example:

```markdown
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Based on the above changes, create a single git commit.
```

#### File references

Include file contents in commands using the `@` prefix to [reference files](/en/common-workflows#reference-files-and-directories).

For example:

```markdown
# Reference a specific file

Review the implementation in @src/utils/helpers.js

# Reference multiple files

Compare @src/old-version.js with @src/new-version.js
```

#### Thinking mode

Slash commands can trigger extended thinking by including [extended thinking keywords](/en/common-workflows#use-extended-thinking).

### Frontmatter

Command files support frontmatter, useful for specifying metadata about the command:

| Frontmatter                | Purpose                                                                                                                                                                               | Default                             |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------- |
| `allowed-tools`            | List of tools the command can use                                                                                                                                                     | Inherits from the conversation      |
| `argument-hint`            | The arguments expected for the slash command. Example: `argument-hint: add [tagId] \| remove [tagId] \| list`. This hint is shown to the user when auto-completing the slash command. | None                                |
| `description`              | Brief description of the command                                                                                                                                                      | Uses the first line from the prompt |
| `model`                    | Specific model string (see [Models overview](https://docs.claude.com/en/docs/about-claude/models/overview))                                                                           | Inherits from the conversation      |
| `disable-model-invocation` | Whether to prevent `SlashCommand` tool from calling this command                                                                                                                      | false                               |

For example:

```markdown
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
argument-hint: [message]
description: Create a git commit
model: claude-3-5-haiku-20241022
---

Create a git commit with message: $ARGUMENTS
```

Example using positional arguments:

```markdown
---
argument-hint: [pr-number] [priority] [assignee]
description: Review pull request
---

Review PR #$1 with priority $2 and assign to $3.
Focus on security, performance, and code style.
```

## Plugin commands

[Plugins](/en/plugins) can provide custom slash commands that integrate seamlessly with Claude Code. Plugin commands work exactly like user-defined commands but are distributed through [plugin marketplaces](/en/plugin-marketplaces).

### How plugin commands work

Plugin commands are:

* **Namespaced**: Commands can use the format `/plugin-name:command-name` to avoid conflicts (plugin prefix is optional unless there are name collisions)
* **Automatically available**: Once a plugin is installed and enabled, its commands appear in `/help`
* **Fully integrated**: Support all command features (arguments, frontmatter, bash execution, file references)

### Plugin command structure

**Location**: `commands/` directory in plugin root

**File format**: Markdown files with frontmatter

**Basic command structure**:

```markdown
---
description: Brief description of what the command does
---

# Command Name

Detailed instructions for Claude on how to execute this command.
Include specific guidance on parameters, expected outcomes, and any special considerations.
```

**Advanced command features**:

* **Arguments**: Use placeholders like `{arg1}` in command descriptions
* **Subdirectories**: Organize commands in subdirectories for namespacing
* **Bash integration**: Commands can execute shell scripts and programs
* **File references**: Commands can reference and modify project files

### Invocation patterns

```shell
/command-name
```

```shell
/plugin-name:command-name
```

```shell
/command-name arg1 arg2
```

## MCP slash commands

MCP servers can expose prompts as slash commands that become available in Claude Code. These commands are dynamically discovered from connected MCP servers.

### Command format

MCP commands follow the pattern:

```
/mcp__<server-name>__<prompt-name> [arguments]
```

### Features

#### Dynamic discovery

MCP commands are automatically available when:

* An MCP server is connected and active
* The server exposes prompts through the MCP protocol
* The prompts are successfully retrieved during connection

#### Arguments

MCP prompts can accept arguments defined by the server:

```
# Without arguments
> /mcp__github__list_prs

# With arguments
> /mcp__github__pr_review 456
> /mcp__jira__create_issue "Bug title" high
```

#### Naming conventions

* Server and prompt names are normalized
* Spaces and special characters become underscores
* Names are lowercased for consistency

### Managing MCP connections

Use the `/mcp` command to:

* View all configured MCP servers
* Check connection status
* Authenticate with OAuth-enabled servers
* Clear authentication tokens
* View available tools and prompts from each server

### MCP permissions and wildcards

When configuring [permissions for MCP tools](/en/iam#tool-specific-permission-rules), note that **wildcards are not supported**:

* ✅ **Correct**: `mcp__github` (approves ALL tools from the github server)
* ✅ **Correct**: `mcp__github__get_issue` (approves specific tool)
* ❌ **Incorrect**: `mcp__github__*` (wildcards not supported)

To approve all tools from an MCP server, use just the server name: `mcp__servername`. To approve specific tools only, list each tool individually.

## `SlashCommand` tool

The `SlashCommand` tool allows Claude to execute [custom slash commands](/en/slash-commands#custom-slash-commands) programmatically
during a conversation. This gives Claude the ability to invoke custom commands
on your behalf when appropriate.

To encourage Claude to trigger `SlashCommand` tool, your instructions (prompts,
CLAUDE.md, etc.) generally need to reference the command by name with its slash.

Example:

```
> Run /write-unit-test when you are about to start writing tests.
```

This tool puts each available custom slash command's metadata into context up to the
character budget limit. You can use `/context` to monitor token usage and follow
the operations below to manage context.

### `SlashCommand` tool supported commands

`SlashCommand` tool only supports custom slash commands that:

* Are user-defined. Built-in commands like `/compact` and `/init` are *not* supported.
* Have the `description` frontmatter field populated. We use the `description` in the context.

For Claude Code versions >= 1.0.124, you can see which custom slash commands
`SlashCommand` tool can invoke by running `claude --debug` and triggering a query.

### Disable `SlashCommand` tool

To prevent Claude from executing any slash commands via the tool:

```bash
/permissions
# Add to deny rules: SlashCommand
```

This will also remove SlashCommand tool (and the slash command descriptions) from context.

### Disable specific commands only

To prevent a specific slash command from becoming available, add
`disable-model-invocation: true` to the slash command's frontmatter.

This will also remove the command's metadata from context.

### `SlashCommand` permission rules

The permission rules support:

* **Exact match**: `SlashCommand:/commit` (allows only `/commit` with no arguments)
* **Prefix match**: `SlashCommand:/review-pr:*` (allows `/review-pr` with any arguments)

### Character budget limit

The `SlashCommand` tool includes a character budget to limit the size of command
descriptions shown to Claude. This prevents token overflow when many commands
are available.

The budget includes each custom slash command's name, args, and description.

* **Default limit**: 15,000 characters
* **Custom limit**: Set via `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable

When the character budget is exceeded, Claude will see only a subset of the
available commands. In `/context`, a warning will show with "M of N commands".

## Skills vs slash commands

**Slash commands** and **Agent Skills** serve different purposes in Claude Code:

### Use slash commands for

**Quick, frequently-used prompts**:

* Simple prompt snippets you use often
* Quick reminders or templates
* Frequently-used instructions that fit in one file

**Examples**:

* `/review` → "Review this code for bugs and suggest improvements"
* `/explain` → "Explain this code in simple terms"
* `/optimize` → "Analyze this code for performance issues"

### Use Skills for

**Comprehensive capabilities with structure**:

* Complex workflows with multiple steps
* Capabilities requiring scripts or utilities
* Knowledge organized across multiple files
* Team workflows you want to standardize

**Examples**:

* PDF processing Skill with form-filling scripts and validation
* Data analysis Skill with reference docs for different data types
* Documentation Skill with style guides and templates

### Key differences

| Aspect         | Slash Commands                   | Agent Skills                        |
| -------------- | -------------------------------- | ----------------------------------- |
| **Complexity** | Simple prompts                   | Complex capabilities                |
| **Structure**  | Single .md file                  | Directory with SKILL.md + resources |
| **Discovery**  | Explicit invocation (`/command`) | Automatic (based on context)        |
| **Files**      | One file only                    | Multiple files, scripts, templates  |
| **Scope**      | Project or personal              | Project or personal                 |
| **Sharing**    | Via git                          | Via git                             |

### Example comparison

**As a slash command**:

```markdown
# .claude/commands/review.md
Review this code for:
- Security vulnerabilities
- Performance issues
- Code style violations
```

Usage: `/review` (manual invocation)

**As a Skill**:

```
.claude/skills/code-review/
├── SKILL.md (overview and workflows)
├── SECURITY.md (security checklist)
├── PERFORMANCE.md (performance patterns)
├── STYLE.md (style guide reference)
└── scripts/
    └── run-linters.sh
```

Usage: "Can you review this code?" (automatic discovery)

The Skill provides richer context, validation scripts, and organized reference material.

### When to use each

**Use slash commands**:

* You invoke the same prompt repeatedly
* The prompt fits in a single file
* You want explicit control over when it runs

**Use Skills**:

* Claude should discover the capability automatically
* Multiple files or scripts are needed
* Complex workflows with validation steps
* Team needs standardized, detailed guidance

Both slash commands and Skills can coexist. Use the approach that fits your needs.

Learn more about [Agent Skills](/en/skills).

## See also

* [Plugins](/en/plugins) - Extend Claude Code with custom commands through plugins
* [Identity and Access Management](/en/iam) - Complete guide to permissions, including MCP tool permissions
* [Interactive mode](/en/interactive-mode) - Shortcuts, input modes, and interactive features
* [CLI reference](/en/cli-reference) - Command-line flags and options
* [Settings](/en/settings) - Configuration options
* [Memory management](/en/memory) - Managing Claude's memory across sessions


# Subagents
Source: https://code.claude.com/docs/en/sub-agents

Create and use specialized AI subagents in Claude Code for task-specific workflows and improved context management.

Custom subagents in Claude Code are specialized AI assistants that can be invoked to handle specific types of tasks. They enable more efficient problem-solving by providing task-specific configurations with customized system prompts, tools and a separate context window.

## What are subagents?

Subagents are pre-configured AI personalities that Claude Code can delegate tasks to. Each subagent:

* Has a specific purpose and expertise area
* Uses its own context window separate from the main conversation
* Can be configured with specific tools it's allowed to use
* Includes a custom system prompt that guides its behavior

When Claude Code encounters a task that matches a subagent's expertise, it can delegate that task to the specialized subagent, which works independently and returns results.

## Key benefits



  - **[Context preservation](#)**
    Each subagent operates in its own context, preventing pollution of the main conversation and keeping it focused on high-level objectives.
  

  - **[Specialized expertise](#)**
    Subagents can be fine-tuned with detailed instructions for specific domains, leading to higher success rates on designated tasks.
  

  - **[Reusability](#)**
    Once created, subagents can be used across different projects and shared with your team for consistent workflows.
  

  - **[Flexible permissions](#)**
    Each subagent can have different tool access levels, allowing you to limit powerful tools to specific subagent types.
  



## Quick start

To create your first subagent:

<Steps>
  <Step title="Open the subagents interface">
    Run the following command:

    ```
    /agents
    ```
  </Step>

  <Step title="Select 'Create New Agent'">
    Choose whether to create a project-level or user-level subagent
  </Step>

  <Step title="Define the subagent">
    * **Recommended**: Generate with Claude first, then customize to make it yours
    * Describe your subagent in detail and when it should be used
    * Select the tools you want to grant access to (or leave blank to inherit all tools)
    * The interface shows all available tools, making selection easy
    * If you're generating with Claude, you can also edit the system prompt in your own editor by pressing `e`
  </Step>

  <Step title="Save and use">
    Your subagent is now available! Claude will use it automatically when appropriate, or you can invoke it explicitly:

    ```
    > Use the code-reviewer subagent to check my recent changes
    ```
  </Step>
</Steps>

## Subagent configuration

### File locations

Subagents are stored as Markdown files with YAML frontmatter in two possible locations:

| Type                  | Location            | Scope                         | Priority |
| :-------------------- | :------------------ | :---------------------------- | :------- |
| **Project subagents** | `.claude/agents/`   | Available in current project  | Highest  |
| **User subagents**    | `~/.claude/agents/` | Available across all projects | Lower    |

When subagent names conflict, project-level subagents take precedence over user-level subagents.

### Plugin agents

[Plugins](/en/plugins) can provide custom subagents that integrate seamlessly with Claude Code. Plugin agents work identically to user-defined agents and appear in the `/agents` interface.

**Plugin agent locations**: Plugins include agents in their `agents/` directory (or custom paths specified in the plugin manifest).

**Using plugin agents**:

* Plugin agents appear in `/agents` alongside your custom agents
* Can be invoked explicitly: "Use the code-reviewer agent from the security-plugin"
* Can be invoked automatically by Claude when appropriate
* Can be managed (viewed, inspected) through `/agents` interface

See the [plugin components reference](/en/plugins-reference#agents) for details on creating plugin agents.

### CLI-based configuration

You can also define subagents dynamically using the `--agents` CLI flag, which accepts a JSON object:

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

**Priority**: CLI-defined subagents have lower priority than project-level subagents but higher priority than user-level subagents.

**Use case**: This approach is useful for:

* Quick testing of subagent configurations
* Session-specific subagents that don't need to be saved
* Automation scripts that need custom subagents
* Sharing subagent definitions in documentation or scripts

For detailed information about the JSON format and all available options, see the [CLI reference documentation](/en/cli-reference#agents-flag-format).

### File format

Each subagent is defined in a Markdown file with this structure:

```markdown
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
model: sonnet  # Optional - specify model alias or 'inherit'
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.

Include specific instructions, best practices, and any constraints
the subagent should follow.
```

#### Configuration fields

| Field         | Required | Description                                                                                                                                                                                                     |
| :------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | Yes      | Unique identifier using lowercase letters and hyphens                                                                                                                                                           |
| `description` | Yes      | Natural language description of the subagent's purpose                                                                                                                                                          |
| `tools`       | No       | Comma-separated list of specific tools. If omitted, inherits all tools from the main thread                                                                                                                     |
| `model`       | No       | Model to use for this subagent. Can be a model alias (`sonnet`, `opus`, `haiku`) or `'inherit'` to use the main conversation's model. If omitted, defaults to the [configured subagent model](/en/model-config) |

### Model selection

The `model` field allows you to control which [AI model](/en/model-config) the subagent uses:

* **Model alias**: Use one of the available aliases: `sonnet`, `opus`, or `haiku`
* **`'inherit'`**: Use the same model as the main conversation (useful for consistency)
* **Omitted**: If not specified, uses the default model configured for subagents (`sonnet`)


> **Note:** Using `'inherit'` is particularly useful when you want your subagents to adapt to the model choice of the main conversation, ensuring consistent capabilities and response style throughout your session.



### Available tools

Subagents can be granted access to any of Claude Code's internal tools. See the [tools documentation](/en/settings#tools-available-to-claude) for a complete list of available tools.


> **💡 Tip:** **Recommended:** Use the `/agents` command to modify tool access - it provides an interactive interface that lists all available tools, including any connected MCP server tools, making it easier to select the ones you need.



You have two options for configuring tools:

* **Omit the `tools` field** to inherit all tools from the main thread (default), including MCP tools
* **Specify individual tools** as a comma-separated list for more granular control (can be edited manually or via `/agents`)

**MCP Tools**: Subagents can access MCP tools from configured MCP servers. When the `tools` field is omitted, subagents inherit all MCP tools available to the main thread.

## Managing subagents

### Using the /agents command (Recommended)

The `/agents` command provides a comprehensive interface for subagent management:

```
/agents
```

This opens an interactive menu where you can:

* View all available subagents (built-in, user, and project)
* Create new subagents with guided setup
* Edit existing custom subagents, including their tool access
* Delete custom subagents
* See which subagents are active when duplicates exist
* **Easily manage tool permissions** with a complete list of available tools

### Direct file management

You can also manage subagents by working directly with their files:

```bash
# Create a project subagent
mkdir -p .claude/agents
echo '---
name: test-runner
description: Use proactively to run tests and fix failures
---

You are a test automation expert. When you see code changes, proactively run the appropriate tests. If tests fail, analyze the failures and fix them while preserving the original test intent.' > .claude/agents/test-runner.md

# Create a user subagent
mkdir -p ~/.claude/agents
# ... create subagent file
```

## Using subagents effectively

### Automatic delegation

Claude Code proactively delegates tasks based on:

* The task description in your request
* The `description` field in subagent configurations
* Current context and available tools


> **💡 Tip:** To encourage more proactive subagent use, include phrases like "use PROACTIVELY" or "MUST BE USED" in your `description` field.



### Explicit invocation

Request a specific subagent by mentioning it in your command:

```
> Use the test-runner subagent to fix failing tests
> Have the code-reviewer subagent look at my recent changes
> Ask the debugger subagent to investigate this error
```

## Built-in subagents

Claude Code includes built-in subagents that are available out of the box:

### Plan subagent

The Plan subagent is a specialized built-in agent designed for use during plan mode. When Claude is operating in plan mode (non-execution mode), it uses the Plan subagent to conduct research and gather information about your codebase before presenting a plan.

**Key characteristics:**

* **Model**: Uses Sonnet for more capable analysis
* **Tools**: Has access to Read, Glob, Grep, and Bash tools for codebase exploration
* **Purpose**: Searches files, analyzes code structure, and gathers context
* **Automatic invocation**: Claude automatically uses this agent when in plan mode and needs to research the codebase

**How it works:**
When you're in plan mode and Claude needs to understand your codebase to create a plan, it delegates research tasks to the Plan subagent. This prevents infinite nesting of agents (subagents cannot spawn other subagents) while still allowing Claude to gather the necessary context.

**Example scenario:**

```
User: [In plan mode] Help me refactor the authentication module

Claude: Let me research your authentication implementation first...
[Internally invokes Plan subagent to explore auth-related files]
[Plan subagent searches codebase and returns findings]
Claude: Based on my research, here's my proposed plan...
```


> **💡 Tip:** The Plan subagent is only used in plan mode. In normal execution mode, Claude uses the general-purpose agent or other custom subagents you've created.



## Example subagents

### Code reviewer

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

### Debugger

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not just symptoms.
```

### Data scientist

```markdown
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
model: sonnet
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.
```

## Best practices

* **Start with Claude-generated agents**: We highly recommend generating your initial subagent with Claude and then iterating on it to make it personally yours. This approach gives you the best results - a solid foundation that you can customize to your specific needs.

* **Design focused subagents**: Create subagents with single, clear responsibilities rather than trying to make one subagent do everything. This improves performance and makes subagents more predictable.

* **Write detailed prompts**: Include specific instructions, examples, and constraints in your system prompts. The more guidance you provide, the better the subagent will perform.

* **Limit tool access**: Only grant tools that are necessary for the subagent's purpose. This improves security and helps the subagent focus on relevant actions.

* **Version control**: Check project subagents into version control so your team can benefit from and improve them collaboratively.

## Advanced usage

### Chaining subagents

For complex workflows, you can chain multiple subagents:

```
> First use the code-analyzer subagent to find performance issues, then use the optimizer subagent to fix them
```

### Dynamic subagent selection

Claude Code intelligently selects subagents based on context. Make your `description` fields specific and action-oriented for best results.

### Resumable subagents

Subagents can be resumed to continue previous conversations, which is particularly useful for long-running research or analysis tasks that need to be continued across multiple invocations.

**How it works:**

* Each subagent execution is assigned a unique `agentId`
* The agent's conversation is stored in a separate transcript file: `agent-{agentId}.jsonl`
* You can resume a previous agent by providing its `agentId` via the `resume` parameter
* When resumed, the agent continues with full context from its previous conversation

**Example workflow:**

Initial invocation:

```
> Use the code-analyzer agent to start reviewing the authentication module

[Agent completes initial analysis and returns agentId: "abc123"]
```

Resume the agent:

```
> Resume agent abc123 and now analyze the authorization logic as well

[Agent continues with full context from previous conversation]
```

**Use cases:**

* **Long-running research**: Break down large codebase analysis into multiple sessions
* **Iterative refinement**: Continue refining a subagent's work without losing context
* **Multi-step workflows**: Have a subagent work on related tasks sequentially while maintaining context

**Technical details:**

* Agent transcripts are stored in your project directory
* Recording is disabled during resume to avoid duplicating messages
* Both synchronous and asynchronous agents can be resumed
* The `resume` parameter accepts the agent ID from a previous execution

**Programmatic usage:**

If you're using the Agent SDK or interacting with the AgentTool directly, you can pass the `resume` parameter:

```typescript
{
  "description": "Continue analysis",
  "prompt": "Now examine the error handling patterns",
  "subagent_type": "code-analyzer",
  "resume": "abc123"  // Agent ID from previous execution
}
```


> **💡 Tip:** Keep track of agent IDs for tasks you may want to resume later. Claude Code displays the agent ID when a subagent completes its work.



## Performance considerations

* **Context efficiency**: Agents help preserve main context, enabling longer overall sessions
* **Latency**: Subagents start off with a clean slate each time they are invoked and may add latency as they gather context that they require to do their job effectively.

## Related documentation

* [Plugins](/en/plugins) - Extend Claude Code with custom agents through plugins
* [Slash commands](/en/slash-commands) - Learn about other built-in commands
* [Settings](/en/settings) - Configure Claude Code behavior
* [Hooks](/en/hooks) - Automate workflows with event handlers




---

[← Previous: Getting Started](./01-getting-started.md) | [📑 Index](./index.md) | [Next: Configuration →](./03-configuration.md)
