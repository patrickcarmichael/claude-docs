---
title: "Getting Started"
description: "Introduction, quickstart, and installation guide"
weight: 1
---

# Getting Started

# Claude Code overview
Source: https://code.claude.com/docs/en/overview

Learn about Claude Code, Anthropic's agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before.

## Get started in 30 seconds

Prerequisites:

* A [Claude.ai](https://claude.ai) (recommended) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:**



**macOS/Linux:**

```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

**Homebrew:**

```bash
    brew install --cask claude-code
    ```

**Windows:**

```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

**NPM:**

```bash
    npm install -g @anthropic-ai/claude-code
    ```

    Requires [Node.js 18+](https://nodejs.org/en/download/)



**Start using Claude Code:**

```bash
cd your-project
claude
```

You'll be prompted to log in on first use. That's it! [Continue with Quickstart (5 mins) →](/en/quickstart)


> **💡 Tip:** See [advanced setup](/en/setup) for installation options or [troubleshooting](/en/troubleshooting) if you hit issues.




> **Note:** **New VS Code Extension (Beta)**: Prefer a graphical interface? Our new [VS Code extension](/en/vs-code) provides an easy-to-use native IDE experience without requiring terminal familiarity. Simply install from the marketplace and start coding with Claude directly in your sidebar.



## What Claude Code does for you

* **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
* **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
* **Navigate any codebase**: Ask anything about your team's codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](/en/mcp) can pull from external datasources like Google Drive, Figma, and Slack.
* **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## Why developers love Claude Code

* **Works in your terminal**: Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
* **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](/en/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
* **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
* **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](/en/security), [privacy](/en/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.

## Next steps



  - **[Quickstart](/en/quickstart)**
    See Claude Code in action with practical examples
  

  - **[Common workflows](/en/common-workflows)**
    Step-by-step guides for common workflows
  

  - **[Troubleshooting](/en/troubleshooting)**
    Solutions for common issues with Claude Code
  

  - **[IDE setup](/en/vs-code)**
    Add Claude Code to your IDE
  



## Additional resources



  - **[Build with the Agent SDK](https://docs.claude.com/en/docs/agent-sdk/overview)**
    Create custom AI agents with the Claude Agent SDK
  

  - **[Host on AWS or GCP](/en/third-party-integrations)**
    Configure Claude Code with Amazon Bedrock or Google Vertex AI
  

  - **[Settings](/en/settings)**
    Customize Claude Code for your workflow
  

  - **[Commands](/en/cli-reference)**
    Learn about CLI commands and controls
  

  - **[Reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)**
    Clone our development container reference implementation
  

  - **[Security](/en/security)**
    Discover Claude Code's safeguards and best practices for safe usage
  

  - **[Privacy and data usage](/en/data-usage)**
    Understand how Claude Code handles your data
  




# Quickstart
Source: https://code.claude.com/docs/en/quickstart

Welcome to Claude Code!

This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you'll understand how to use Claude Code for common development tasks.

## Before you begin

Make sure you have:

* A terminal or command prompt open
* A code project to work with
* A [Claude.ai](https://claude.ai) (recommended) or [Claude Console](https://console.anthropic.com/) account

## Step 1: Install Claude Code

To install Claude Code, use one of the following methods:



**Native Install (Recommended):**

**Homebrew (macOS, Linux):**

    ```sh
    brew install --cask claude-code
    ```

    **macOS, Linux, WSL:**

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Windows PowerShell:**

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    **Windows CMD:**

    ```batch
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```

**NPM:**

If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):

    ```sh
    npm install -g @anthropic-ai/claude-code
    ```



## Step 2: Log in to your account

Claude Code requires an account to use. When you start an interactive session with the `claude` command, you'll need to log in:

```bash
claude
# You'll be prompted to log in on first use
```

```bash
/login
# Follow the prompts to log in with your account
```

You can log in using either account type:

* [Claude.ai](https://claude.ai) (subscription plans - recommended)
* [Claude Console](https://console.anthropic.com/) (API access with pre-paid credits)

Once logged in, your credentials are stored and you won't need to log in again.


> **Note:** When you first authenticate Claude Code with your Claude Console account, a workspace called "Claude Code" is automatically created for you. This workspace provides centralized cost tracking and management for all Claude Code usage in your organization.




> **Note:** You can have both account types under the same email address. If you need to log in again or switch accounts, use the `/login` command within Claude Code.



## Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:

```bash
cd /path/to/your/project
claude
```

You'll see the Claude Code welcome screen with your session information, recent conversations, and latest updates. Type `/help` for available commands or `/resume` to continue a previous conversation.


> **💡 Tip:** After logging in (Step 2), your credentials are stored on your system. Learn more in [Credential Management](/en/iam#credential-management).



## Step 4: Ask your first question

Let's start with understanding your codebase. Try one of these commands:

```
> what does this project do?
```

Claude will analyze your files and provide a summary. You can also ask more specific questions:

```
> what technologies does this project use?
```

```
> where is the main entry point?
```

```
> explain the folder structure
```

You can also ask Claude about its own capabilities:

```
> what can Claude Code do?
```

```
> how do I use slash commands in Claude Code?
```

```
> can Claude Code work with Docker?
```


> **Note:** Claude Code reads your files as needed - you don't have to manually add context. Claude also has access to its own documentation and can answer questions about its features and capabilities.



## Step 5: Make your first code change

Now let's make Claude Code do some actual coding. Try a simple task:

```
> add a hello world function to the main file
```

Claude Code will:

1. Find the appropriate file
2. Show you the proposed changes
3. Ask for your approval
4. Make the edit


> **Note:** Claude Code always asks for permission before modifying files. You can approve individual changes or enable "Accept all" mode for a session.



## Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:

```
> what files have I changed?
```

```
> commit my changes with a descriptive message
```

You can also prompt for more complex Git operations:

```
> create a new branch called feature/quickstart
```

```
> show me the last 5 commits
```

```
> help me resolve merge conflicts
```

## Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation.

Describe what you want in natural language:

```
> add input validation to the user registration form
```

Or fix existing issues:

```
> there's a bug where users can submit empty forms - fix it
```

Claude Code will:

* Locate the relevant code
* Understand the context
* Implement a solution
* Run tests if available

## Step 8: Test out other common workflows

There are a number of ways to work with Claude:

**Refactor code**

```
> refactor the authentication module to use async/await instead of callbacks
```

**Write tests**

```
> write unit tests for the calculator functions
```

**Update documentation**

```
> update the README with installation instructions
```

**Code review**

```
> review my changes and suggest improvements
```


> **💡 Tip:** **Remember**: Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.



## Essential commands

Here are the most important commands for daily use:

| Command             | What it does                      | Example                             |
| ------------------- | --------------------------------- | ----------------------------------- |
| `claude`            | Start interactive mode            | `claude`                            |
| `claude "task"`     | Run a one-time task               | `claude "fix the build error"`      |
| `claude -p "query"` | Run one-off query, then exit      | `claude -p "explain this function"` |
| `claude -c`         | Continue most recent conversation | `claude -c`                         |
| `claude -r`         | Resume a previous conversation    | `claude -r`                         |
| `claude commit`     | Create a Git commit               | `claude commit`                     |
| `/clear`            | Clear conversation history        | `> /clear`                          |
| `/help`             | Show available commands           | `> /help`                           |
| `exit` or Ctrl+C    | Exit Claude Code                  | `> exit`                            |

See the [CLI reference](/en/cli-reference) for a complete list of commands.

## Pro tips for beginners



  
**Be specific with your requests**

Instead of: "fix the bug"

    Try: "fix the login bug where users see a blank screen after entering wrong credentials"


  
**Use step-by-step instructions**

Break complex tasks into steps:

    ```
    > 1. create a new database table for user profiles
    ```

    ```
    > 2. create an API endpoint to get and update user profiles
    ```

    ```
    > 3. build a webpage that allows users to see and edit their information
    ```


  
**Let Claude explore first**

Before making changes, let Claude understand your code:

    ```
    > analyze the database schema
    ```

    ```
    > build a dashboard showing products that are most frequently returned by our UK customers
    ```


  
**Save time with shortcuts**

* Press `?` to see all available keyboard shortcuts
    * Use Tab for command completion
    * Press ↑ for command history
    * Type `/` to see all slash commands




## What's next?

Now that you've learned the basics, explore more advanced features:



  - **[Common workflows](/en/common-workflows)**
    Step-by-step guides for common tasks
  

  - **[CLI reference](/en/cli-reference)**
    Master all commands and options
  

  - **[Configuration](/en/settings)**
    Customize Claude Code for your workflow
  

  - **[Claude Code on the web](/en/claude-code-on-the-web)**
    Run tasks asynchronously in the cloud
  



## Getting help

* **In Claude Code**: Type `/help` or ask "how do I..."
* **Documentation**: You're here! Browse other guides
* **Community**: Join our [Discord](https://www.anthropic.com/discord) for tips and support


# Set up Claude Code
Source: https://code.claude.com/docs/en/setup

Install, authenticate, and start using Claude Code on your development machine.

## System requirements

* **Operating Systems**: macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (with WSL 1, WSL 2, or Git for Windows)
* **Hardware**: 4GB+ RAM
* **Software**: [Node.js 18+](https://nodejs.org/en/download) (only required for NPM installation)
* **Network**: Internet connection required for authentication and AI processing
* **Shell**: Works best in Bash, Zsh or Fish
* **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)

### Additional dependencies

* **ripgrep**: Usually included with Claude Code. If search functionality fails, see [search troubleshooting](/en/troubleshooting#search-and-discovery-issues).

## Standard installation

To install Claude Code, use one of the following methods:



**Native Install (Recommended):**

**Homebrew (macOS, Linux):**

    ```sh
    brew install --cask claude-code
    ```

    **macOS, Linux, WSL:**

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Windows PowerShell:**

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    **Windows CMD:**

    ```batch
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```

**NPM:**

If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):

    ```sh
    npm install -g @anthropic-ai/claude-code
    ```




> **Note:** Some users may be automatically migrated to an improved installation method.



After the installation process completes, navigate to your project and start Claude Code:

```bash
cd your-awesome-project
claude
```

Claude Code offers the following authentication options:

1. **Claude Console**: The default option. Connect through the Claude Console and complete the OAuth process. Requires active billing at [console.anthropic.com](https://console.anthropic.com). A "Claude Code" workspace will be automatically created for usage tracking and cost management. Note that you cannot create API keys for the Claude Code workspace - it is dedicated exclusively for Claude Code usage.
2. **Claude App (with Pro or Max plan)**: Subscribe to Claude's [Pro or Max plan](https://claude.com/pricing) for a unified subscription that includes both Claude Code and the web interface. Get more value at the same price point while managing your account in one place. Log in with your Claude.ai account. During launch, choose the option that matches your subscription type.
3. **Enterprise platforms**: Configure Claude Code to use [Amazon Bedrock or Google Vertex AI](/en/third-party-integrations) for enterprise deployments with your existing cloud infrastructure.


> **Note:** Claude Code securely stores your credentials. See [Credential Management](/en/iam#credential-management) for details.



## Windows setup

**Option 1: Claude Code within WSL**

* Both WSL 1 and WSL 2 are supported

**Option 2: Claude Code on native Windows with Git Bash**

* Requires [Git for Windows](https://git-scm.com/downloads/win)
* For portable Git installations, specify the path to your `bash.exe`:
  ```powershell
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  ```

## Alternative installation methods

Claude Code offers multiple installation methods to suit different environments.

If you encounter any issues during installation, consult the [troubleshooting guide](/en/troubleshooting#linux-permission-issues).


> **💡 Tip:** Run `claude doctor` after installation to check your installation type and version.



### Native installation options

The native installation is the recommended method and offers several benefits:

* One self-contained executable
* No Node.js dependency
* Improved auto-updater stability

If you have an existing installation of Claude Code, use `claude install` to migrate to the native binary installation.

For advanced installation options with the native installer:

**macOS, Linux, WSL:**

```bash
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version number
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```


> **Note:** **Alpine Linux and other musl/uClibc-based distributions**: The native build requires you to install `libgcc`, `libstdc++`, and `ripgrep`. Install (Alpine: `apk add libgcc libstdc++ ripgrep`) and set `USE_BUILTIN_RIPGREP=0`.




> **Note:** Claude Code installed via Homebrew will auto-update outside of the brew directory unless explicitly disabled with the `DISABLE_AUTOUPDATER` environment variable (see [Auto updates](#auto-updates) section).



**Windows PowerShell:**

```powershell
# Install stable version (default)
irm https://claude.ai/install.ps1 | iex

# Install latest version
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest

# Install specific version number
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
```

**Windows CMD:**

```batch
REM Install stable version (default)
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

REM Install latest version
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd latest && del install.cmd

REM Install specific version number
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
```


> **💡 Tip:** Make sure that you remove any outdated aliases or symlinks before installing.



### NPM installation

For environments where NPM is preferred or required:

```sh
npm install -g @anthropic-ai/claude-code
```


> **⚠️ Warning:** Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks.
  If you encounter permission errors, see [configure Claude Code](/en/troubleshooting#linux-permission-issues) for recommended solutions.



### Local installation

* After global install via npm, use `claude migrate-installer` to move to local
* Avoids autoupdater npm permission issues
* Some users may be automatically migrated to this method

## Running on AWS or GCP

By default, Claude Code uses the Claude API.

For details on running Claude Code on AWS or GCP, see [third-party integrations](/en/third-party-integrations).

## Update Claude Code

### Auto updates

Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.

* **Update checks**: Performed on startup and periodically while running
* **Update process**: Downloads and installs automatically in the background
* **Notifications**: You'll see a notification when updates are installed
* **Applying updates**: Updates take effect the next time you start Claude Code

**Disable auto-updates:**

Set the `DISABLE_AUTOUPDATER` environment variable in your shell or [settings.json file](/en/settings):

```bash
export DISABLE_AUTOUPDATER=1
```

### Update manually

```bash
claude update
```


# Optimize your terminal setup
Source: https://code.claude.com/docs/en/terminal-config

Claude Code works best when your terminal is properly configured. Follow these guidelines to optimize your experience.

### Themes and appearance

Claude cannot control the theme of your terminal. That's handled by your terminal application. You can match Claude Code's theme to your terminal any time via the `/config` command.

For additional customization of the Claude Code interface itself, you can configure a [custom status line](/en/statusline) to display contextual information like the current model, working directory, or git branch at the bottom of your terminal.

### Line breaks

You have several options for entering linebreaks into Claude Code:

* **Quick escape**: Type `\` followed by Enter to create a newline
* **Keyboard shortcut**: Set up a keybinding to insert a newline

#### Set up Shift+Enter (VS Code or iTerm2):

Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter.

#### Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):

**For Mac Terminal.app:**

1. Open Settings → Profiles → Keyboard
2. Check "Use Option as Meta Key"

**For iTerm2 and VS Code terminal:**

1. Open Settings → Profiles → Keys
2. Under General, set Left/Right Option key to "Esc+"

### Notification setup

Never miss when Claude completes a task with proper notification configuration:

#### iTerm 2 system notifications

For iTerm 2 alerts when tasks complete:

1. Open iTerm 2 Preferences
2. Navigate to Profiles → Terminal
3. Enable "Silence bell" and Filter Alerts → "Send escape sequence-generated alerts"
4. Set your preferred notification delay

Note that these notifications are specific to iTerm 2 and not available in the default macOS Terminal.

#### Custom notification hooks

For advanced notification handling, you can create [notification hooks](/en/hooks#notification) to run your own logic.

### Handling large inputs

When working with extensive code or long instructions:

* **Avoid direct pasting**: Claude Code may struggle with very long pasted content
* **Use file-based workflows**: Write content to a file and ask Claude to read it
* **Be aware of VS Code limitations**: The VS Code terminal is particularly prone to truncating long pastes

### Vim Mode

Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`.

The supported subset includes:

* Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
* Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
* Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)




---

[📑 Index](./index.md) | [Next: Features →](./02-features.md)
