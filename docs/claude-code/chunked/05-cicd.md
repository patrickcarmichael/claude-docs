# CI/CD & Automation

**Navigation:** [← Previous: Deployment](./04-deployment.md) | [Index](./index.md) | [Next: Integrations →](./06-integrations.md)

> **Note:** This is part of the chunked llms-full.txt. For organized topic documentation, see [../README.md](../README.md)

---

# Common workflows
Source: https://code.claude.com/docs/en/common-workflows

Learn about common workflows with Claude Code.

Each task in this document includes clear instructions, example commands, and best practices to help you get the most from Claude Code.

## Understand new codebases

### Get a quick codebase overview

Suppose you've just joined a new project and need to understand its structure quickly.

<Steps>
  <Step title="Navigate to the project root directory">
    ```bash  theme={null}
    cd /path/to/project 
    ```
  </Step>

  <Step title="Start Claude Code">
    ```bash  theme={null}
    claude 
    ```
  </Step>

  <Step title="Ask for a high-level overview">
    ```
    > give me an overview of this codebase 
    ```
  </Step>

  <Step title="Dive deeper into specific components">
    ```
    > explain the main architecture patterns used here 
    ```

    ```
    > what are the key data models?
    ```

    ```
    > how is authentication handled?
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Start with broad questions, then narrow down to specific areas
  * Ask about coding conventions and patterns used in the project
  * Request a glossary of project-specific terms
</Tip>

### Find relevant code

Suppose you need to locate code related to a specific feature or functionality.

<Steps>
  <Step title="Ask Claude to find relevant files">
    ```
    > find the files that handle user authentication 
    ```
  </Step>

  <Step title="Get context on how components interact">
    ```
    > how do these authentication files work together? 
    ```
  </Step>

  <Step title="Understand the execution flow">
    ```
    > trace the login process from front-end to database 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Be specific about what you're looking for
  * Use domain language from the project
</Tip>

***

## Fix bugs efficiently

Suppose you've encountered an error message and need to find and fix its source.

<Steps>
  <Step title="Share the error with Claude">
    ```
    > I'm seeing an error when I run npm test 
    ```
  </Step>

  <Step title="Ask for fix recommendations">
    ```
    > suggest a few ways to fix the @ts-ignore in user.ts 
    ```
  </Step>

  <Step title="Apply the fix">
    ```
    > update user.ts to add the null check you suggested 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Tell Claude the command to reproduce the issue and get a stack trace
  * Mention any steps to reproduce the error
  * Let Claude know if the error is intermittent or consistent
</Tip>

***

## Refactor code

Suppose you need to update old code to use modern patterns and practices.

<Steps>
  <Step title="Identify legacy code for refactoring">
    ```
    > find deprecated API usage in our codebase 
    ```
  </Step>

  <Step title="Get refactoring recommendations">
    ```
    > suggest how to refactor utils.js to use modern JavaScript features 
    ```
  </Step>

  <Step title="Apply the changes safely">
    ```
    > refactor utils.js to use ES2024 features while maintaining the same behavior 
    ```
  </Step>

  <Step title="Verify the refactoring">
    ```
    > run tests for the refactored code 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Ask Claude to explain the benefits of the modern approach
  * Request that changes maintain backward compatibility when needed
  * Do refactoring in small, testable increments
</Tip>

***

## Use specialized subagents

Suppose you want to use specialized AI subagents to handle specific tasks more effectively.

<Steps>
  <Step title="View available subagents">
    ```
    > /agents
    ```

    This shows all available subagents and lets you create new ones.
  </Step>

  <Step title="Use subagents automatically">
    Claude Code will automatically delegate appropriate tasks to specialized subagents:

    ```
    > review my recent code changes for security issues
    ```

    ```
    > run all tests and fix any failures
    ```
  </Step>

  <Step title="Explicitly request specific subagents">
    ```
    > use the code-reviewer subagent to check the auth module
    ```

    ```
    > have the debugger subagent investigate why users can't log in
    ```
  </Step>

  <Step title="Create custom subagents for your workflow">
    ```
    > /agents
    ```

    Then select "Create New subagent" and follow the prompts to define:

    * Subagent type (e.g., `api-designer`, `performance-optimizer`)
    * When to use it
    * Which tools it can access
    * Its specialized system prompt
  </Step>
</Steps>

<Tip>
  Tips:

  * Create project-specific subagents in `.claude/agents/` for team sharing
  * Use descriptive `description` fields to enable automatic delegation
  * Limit tool access to what each subagent actually needs
  * Check the [subagents documentation](/en/sub-agents) for detailed examples
</Tip>

***

## Use Plan Mode for safe code analysis

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely.

### When to use Plan Mode

* **Multi-step implementation**: When your feature requires making edits to many files
* **Code exploration**: When you want to research the codebase thoroughly before changing anything
* **Interactive development**: When you want to iterate on the direction with Claude

### How to use Plan Mode

**Turn on Plan Mode during a session**

You can switch into Plan Mode during a session using **Shift+Tab** to cycle through permission modes.

If you are in Normal Mode, **Shift+Tab** will first switch into Auto-Accept Mode, indicated by `⏵⏵ accept edits on` at the bottom of the terminal. A subsequent **Shift+Tab** will switch into Plan Mode, indicated by `⏸ plan mode on`.

**Start a new session in Plan Mode**

To start a new session in Plan Mode, use the `--permission-mode plan` flag:

```bash  theme={null}
claude --permission-mode plan
```

**Run "headless" queries in Plan Mode**

You can also run a query in Plan Mode directly with `-p` (i.e., in ["headless mode"](/en/headless)):

```bash  theme={null}
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

### Example: Planning a complex refactor

```bash  theme={null}
claude --permission-mode plan
```

```
> I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Claude will analyze the current implementation and create a comprehensive plan. Refine with follow-ups:

```
> What about backward compatibility?
> How should we handle database migration?
```

### Configure Plan Mode as default

```json  theme={null}
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

See [settings documentation](/en/settings#available-settings) for more configuration options.

***

## Work with tests

Suppose you need to add tests for uncovered code.

<Steps>
  <Step title="Identify untested code">
    ```
    > find functions in NotificationsService.swift that are not covered by tests 
    ```
  </Step>

  <Step title="Generate test scaffolding">
    ```
    > add tests for the notification service 
    ```
  </Step>

  <Step title="Add meaningful test cases">
    ```
    > add test cases for edge conditions in the notification service 
    ```
  </Step>

  <Step title="Run and verify tests">
    ```
    > run the new tests and fix any failures 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Ask for tests that cover edge cases and error conditions
  * Request both unit and integration tests when appropriate
  * Have Claude explain the testing strategy
</Tip>

***

## Create pull requests

Suppose you need to create a well-documented pull request for your changes.

<Steps>
  <Step title="Summarize your changes">
    ```
    > summarize the changes I've made to the authentication module 
    ```
  </Step>

  <Step title="Generate a PR with Claude">
    ```
    > create a pr 
    ```
  </Step>

  <Step title="Review and refine">
    ```
    > enhance the PR description with more context about the security improvements 
    ```
  </Step>

  <Step title="Add testing details">
    ```
    > add information about how these changes were tested 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Ask Claude directly to make a PR for you
  * Review Claude's generated PR before submitting
  * Ask Claude to highlight potential risks or considerations
</Tip>

## Handle documentation

Suppose you need to add or update documentation for your code.

<Steps>
  <Step title="Identify undocumented code">
    ```
    > find functions without proper JSDoc comments in the auth module 
    ```
  </Step>

  <Step title="Generate documentation">
    ```
    > add JSDoc comments to the undocumented functions in auth.js 
    ```
  </Step>

  <Step title="Review and enhance">
    ```
    > improve the generated documentation with more context and examples 
    ```
  </Step>

  <Step title="Verify documentation">
    ```
    > check if the documentation follows our project standards 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Specify the documentation style you want (JSDoc, docstrings, etc.)
  * Ask for examples in the documentation
  * Request documentation for public APIs, interfaces, and complex logic
</Tip>

***

## Work with images

Suppose you need to work with images in your codebase, and you want Claude's help analyzing image content.

<Steps>
  <Step title="Add an image to the conversation">
    You can use any of these methods:

    1. Drag and drop an image into the Claude Code window
    2. Copy an image and paste it into the CLI with ctrl+v (Do not use cmd+v)
    3. Provide an image path to Claude. E.g., "Analyze this image: /path/to/your/image.png"
  </Step>

  <Step title="Ask Claude to analyze the image">
    ```
    > What does this image show?
    ```

    ```
    > Describe the UI elements in this screenshot
    ```

    ```
    > Are there any problematic elements in this diagram?
    ```
  </Step>

  <Step title="Use images for context">
    ```
    > Here's a screenshot of the error. What's causing it?
    ```

    ```
    > This is our current database schema. How should we modify it for the new feature?
    ```
  </Step>

  <Step title="Get code suggestions from visual content">
    ```
    > Generate CSS to match this design mockup
    ```

    ```
    > What HTML structure would recreate this component?
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Use images when text descriptions would be unclear or cumbersome
  * Include screenshots of errors, UI designs, or diagrams for better context
  * You can work with multiple images in a conversation
  * Image analysis works with diagrams, screenshots, mockups, and more
</Tip>

***

## Reference files and directories

Use @ to quickly include files or directories without waiting for Claude to read them.

<Steps>
  <Step title="Reference a single file">
    ```
    > Explain the logic in @src/utils/auth.js
    ```

    This includes the full content of the file in the conversation.
  </Step>

  <Step title="Reference a directory">
    ```
    > What's the structure of @src/components?
    ```

    This provides a directory listing with file information.
  </Step>

  <Step title="Reference MCP resources">
    ```
    > Show me the data from @github:repos/owner/repo/issues
    ```

    This fetches data from connected MCP servers using the format @server:resource. See [MCP resources](/en/mcp#use-mcp-resources) for details.
  </Step>
</Steps>

<Tip>
  Tips:

  * File paths can be relative or absolute
  * @ file references add CLAUDE.md in the file's directory and parent directories to context
  * Directory references show file listings, not contents
  * You can reference multiple files in a single message (e.g., "@file1.js and @file2.js")
</Tip>

***

## Use extended thinking

Suppose you're working on complex architectural decisions, challenging bugs, or planning multi-step implementations that require deep reasoning.

<Note>
  [Extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) is disabled by default in Claude Code. You can enable it on-demand by using `Tab` to toggle Thinking on, or by using prompts like "think" or "think hard". You can also enable it permanently by setting the [`MAX_THINKING_TOKENS` environment variable](/en/settings#environment-variables) in your settings.
</Note>

<Steps>
  <Step title="Provide context and ask Claude to think">
    ```
    > I need to implement a new authentication system using OAuth2 for our API. Think deeply about the best approach for implementing this in our codebase.
    ```

    Claude will gather relevant information from your codebase and
    use extended thinking, which will be visible in the interface.
  </Step>

  <Step title="Refine the thinking with follow-up prompts">
    ```
    > think about potential security vulnerabilities in this approach 
    ```

    ```
    > think hard about edge cases we should handle 
    ```
  </Step>
</Steps>

<Tip>
  Tips to get the most value out of extended thinking:

  [Extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) is most valuable for complex tasks such as:

  * Planning complex architectural changes
  * Debugging intricate issues
  * Creating implementation plans for new features
  * Understanding complex codebases
  * Evaluating tradeoffs between different approaches

  Use `Tab` to toggle Thinking on and off during a session.

  The way you prompt for thinking results in varying levels of thinking depth:

  * "think" triggers basic extended thinking
  * intensifying phrases such as "keep hard", "think more", "think a lot", or "think longer" triggers deeper thinking

  For more extended thinking prompting tips, see [Extended thinking tips](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Tip>

<Note>
  Claude will display its thinking process as italic gray text above the
  response.
</Note>

***

## Resume previous conversations

Suppose you've been working on a task with Claude Code and need to continue where you left off in a later session.

Claude Code provides two options for resuming previous conversations:

* `--continue` to automatically continue the most recent conversation
* `--resume` to display a conversation picker

<Steps>
  <Step title="Continue the most recent conversation">
    ```bash  theme={null}
    claude --continue
    ```

    This immediately resumes your most recent conversation without any prompts.
  </Step>

  <Step title="Continue in non-interactive mode">
    ```bash  theme={null}
    claude --continue --print "Continue with my task"
    ```

    Use `--print` with `--continue` to resume the most recent conversation in non-interactive mode, perfect for scripts or automation.
  </Step>

  <Step title="Show conversation picker">
    ```bash  theme={null}
    claude --resume
    ```

    This displays an interactive conversation selector with a clean list view showing:

    * Session summary (or initial prompt)
    * Metadata: time elapsed, message count, and git branch

    Use arrow keys to navigate and press Enter to select a conversation. Press Esc to exit.
  </Step>
</Steps>

<Tip>
  Tips:

  * Conversation history is stored locally on your machine
  * Use `--continue` for quick access to your most recent conversation
  * Use `--resume` when you need to select a specific past conversation
  * When resuming, you'll see the entire conversation history before continuing
  * The resumed conversation starts with the same model and configuration as the original

  How it works:

  1. **Conversation Storage**: All conversations are automatically saved locally with their full message history
  2. **Message Deserialization**: When resuming, the entire message history is restored to maintain context
  3. **Tool State**: Tool usage and results from the previous conversation are preserved
  4. **Context Restoration**: The conversation resumes with all previous context intact

  Examples:

  ```bash  theme={null}
  # Continue most recent conversation
  claude --continue

  # Continue most recent conversation with a specific prompt
  claude --continue --print "Show me our progress"

  # Show conversation picker
  claude --resume

  # Continue most recent conversation in non-interactive mode
  claude --continue --print "Run the tests again"
  ```
</Tip>

***

## Run parallel Claude Code sessions with Git worktrees

Suppose you need to work on multiple tasks simultaneously with complete code isolation between Claude Code instances.

<Steps>
  <Step title="Understand Git worktrees">
    Git worktrees allow you to check out multiple branches from the same
    repository into separate directories. Each worktree has its own working
    directory with isolated files, while sharing the same Git history. Learn
    more in the [official Git worktree
    documentation](https://git-scm.com/docs/git-worktree).
  </Step>

  <Step title="Create a new worktree">
    ```bash  theme={null}
    # Create a new worktree with a new branch 
    git worktree add ../project-feature-a -b feature-a

    # Or create a worktree with an existing branch
    git worktree add ../project-bugfix bugfix-123
    ```

    This creates a new directory with a separate working copy of your repository.
  </Step>

  <Step title="Run Claude Code in each worktree">
    ```bash  theme={null}
    # Navigate to your worktree 
    cd ../project-feature-a

    # Run Claude Code in this isolated environment
    claude
    ```
  </Step>

  <Step title="Run Claude in another worktree">
    ```bash  theme={null}
    cd ../project-bugfix
    claude
    ```
  </Step>

  <Step title="Manage your worktrees">
    ```bash  theme={null}
    # List all worktrees
    git worktree list

    # Remove a worktree when done
    git worktree remove ../project-feature-a
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Each worktree has its own independent file state, making it perfect for parallel Claude Code sessions
  * Changes made in one worktree won't affect others, preventing Claude instances from interfering with each other
  * All worktrees share the same Git history and remote connections
  * For long-running tasks, you can have Claude working in one worktree while you continue development in another
  * Use descriptive directory names to easily identify which task each worktree is for
  * Remember to initialize your development environment in each new worktree according to your project's setup. Depending on your stack, this might include:
    * JavaScript projects: Running dependency installation (`npm install`, `yarn`)
    * Python projects: Setting up virtual environments or installing with package managers
    * Other languages: Following your project's standard setup process
</Tip>

***

## Use Claude as a unix-style utility

### Add Claude to your verification process

Suppose you want to use Claude Code as a linter or code reviewer.

**Add Claude to your build script:**

```json  theme={null}
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}
```

<Tip>
  Tips:

  * Use Claude for automated code review in your CI/CD pipeline
  * Customize the prompt to check for specific issues relevant to your project
  * Consider creating multiple scripts for different types of verification
</Tip>

### Pipe in, pipe out

Suppose you want to pipe data into Claude, and get back data in a structured format.

**Pipe data through Claude:**

```bash  theme={null}
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

<Tip>
  Tips:

  * Use pipes to integrate Claude into existing shell scripts
  * Combine with other Unix tools for powerful workflows
  * Consider using --output-format for structured output
</Tip>

### Control output format

Suppose you need Claude's output in a specific format, especially when integrating Claude Code into scripts or other tools.

<Steps>
  <Step title="Use text format (default)">
    ```bash  theme={null}
    cat data.txt | claude -p 'summarize this data' --output-format text > summary.txt
    ```

    This outputs just Claude's plain text response (default behavior).
  </Step>

  <Step title="Use JSON format">
    ```bash  theme={null}
    cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json
    ```

    This outputs a JSON array of messages with metadata including cost and duration.
  </Step>

  <Step title="Use streaming JSON format">
    ```bash  theme={null}
    cat log.txt | claude -p 'parse this log file for errors' --output-format stream-json
    ```

    This outputs a series of JSON objects in real-time as Claude processes the request. Each message is a valid JSON object, but the entire output is not valid JSON if concatenated.
  </Step>
</Steps>

<Tip>
  Tips:

  * Use `--output-format text` for simple integrations where you just need Claude's response
  * Use `--output-format json` when you need the full conversation log
  * Use `--output-format stream-json` for real-time output of each conversation turn
</Tip>

***

## Create custom slash commands

Claude Code supports custom slash commands that you can create to quickly execute specific prompts or tasks.

For more details, see the [Slash commands](/en/slash-commands) reference page.

### Create project-specific commands

Suppose you want to create reusable slash commands for your project that all team members can use.

<Steps>
  <Step title="Create a commands directory in your project">
    ```bash  theme={null}
    mkdir -p .claude/commands
    ```
  </Step>

  <Step title="Create a Markdown file for each command">
    ```bash  theme={null}
    echo "Analyze the performance of this code and suggest three specific optimizations:" > .claude/commands/optimize.md 
    ```
  </Step>

  <Step title="Use your custom command in Claude Code">
    ```
    > /optimize 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Command names are derived from the filename (e.g., `optimize.md` becomes `/optimize`)
  * You can organize commands in subdirectories (e.g., `.claude/commands/frontend/component.md` creates `/component` with "(project:frontend)" shown in the description)
  * Project commands are available to everyone who clones the repository
  * The Markdown file content becomes the prompt sent to Claude when the command is invoked
</Tip>

### Add command arguments with \$ARGUMENTS

Suppose you want to create flexible slash commands that can accept additional input from users.

<Steps>
  <Step title="Create a command file with the $ARGUMENTS placeholder">
    ```bash  theme={null}
    echo 'Find and fix issue #$ARGUMENTS. Follow these steps: 1.
    Understand the issue described in the ticket 2. Locate the relevant code in
    our codebase 3. Implement a solution that addresses the root cause 4. Add
    appropriate tests 5. Prepare a concise PR description' >
    .claude/commands/fix-issue.md 
    ```
  </Step>

  <Step title="Use the command with an issue number">
    In your Claude session, use the command with arguments.

    ```
    > /fix-issue 123 
    ```

    This will replace \$ARGUMENTS with "123" in the prompt.
  </Step>
</Steps>

<Tip>
  Tips:

  * The \$ARGUMENTS placeholder is replaced with any text that follows the command
  * You can position \$ARGUMENTS anywhere in your command template
  * Other useful applications: generating test cases for specific functions, creating documentation for components, reviewing code in particular files, or translating content to specified languages
</Tip>

### Create personal slash commands

Suppose you want to create personal slash commands that work across all your projects.

<Steps>
  <Step title="Create a commands directory in your home folder">
    ```bash  theme={null}
    mkdir -p ~/.claude/commands 
    ```
  </Step>

  <Step title="Create a Markdown file for each command">
    ```bash  theme={null}
    echo "Review this code for security vulnerabilities, focusing on:" >
    ~/.claude/commands/security-review.md 
    ```
  </Step>

  <Step title="Use your personal custom command">
    ```
    > /security-review 
    ```
  </Step>
</Steps>

<Tip>
  Tips:

  * Personal commands show "(user)" in their description when listed with `/help`
  * Personal commands are only available to you and not shared with your team
  * Personal commands work across all your projects
  * You can use these for consistent workflows across different codebases
</Tip>

***

## Ask Claude about its capabilities

Claude has built-in access to its documentation and can answer questions about its own features and limitations.

### Example questions

```
> can Claude Code create pull requests?
```

```
> how does Claude Code handle permissions?
```

```
> what slash commands are available?
```

```
> how do I use MCP with Claude Code?
```

```
> how do I configure Claude Code for Amazon Bedrock?
```

```
> what are the limitations of Claude Code?
```

<Note>
  Claude provides documentation-based answers to these questions. For executable examples and hands-on demonstrations, refer to the specific workflow sections above.
</Note>

<Tip>
  Tips:

  * Claude always has access to the latest Claude Code documentation, regardless of the version you're using
  * Ask specific questions to get detailed answers
  * Claude can explain complex features like MCP integration, enterprise configurations, and advanced workflows
</Tip>

***

## Next steps

<Card title="Claude Code reference implementation" icon="code" href="https://github.com/anthropics/claude-code/tree/main/.devcontainer">
  Clone our development container reference implementation.
</Card>


# Claude Code GitHub Actions
Source: https://code.claude.com/docs/en/github-actions

Learn about integrating Claude Code into your development workflow with Claude Code GitHub Actions

Claude Code GitHub Actions brings AI-powered automation to your GitHub workflow. With a simple `@claude` mention in any PR or issue, Claude can analyze your code, create pull requests, implement features, and fix bugs - all while following your project's standards.

<Note>
  Claude Code GitHub Actions is built on top of the [Claude Code
  SDK](https://docs.claude.com/en/docs/agent-sdk), which enables programmatic integration of
  Claude Code into your applications. You can use the SDK to build custom
  automation workflows beyond GitHub Actions.
</Note>

## Why use Claude Code GitHub Actions?

* **Instant PR creation**: Describe what you need, and Claude creates a complete PR with all necessary changes
* **Automated code implementation**: Turn issues into working code with a single command
* **Follows your standards**: Claude respects your `CLAUDE.md` guidelines and existing code patterns
* **Simple setup**: Get started in minutes with our installer and API key
* **Secure by default**: Your code stays on Github's runners

## What can Claude do?

Claude Code provides a powerful GitHub Action that transforms how you work with code:

### Claude Code Action

This GitHub Action allows you to run Claude Code within your GitHub Actions workflows. You can use this to build any custom workflow on top of Claude Code.

[View repository →](https://github.com/anthropics/claude-code-action)

## Setup

## Quick setup

The easiest way to set up this action is through Claude Code in the terminal. Just open claude and run `/install-github-app`.

This command will guide you through setting up the GitHub app and required secrets.

<Note>
  * You must be a repository admin to install the GitHub app and add secrets
  * The GitHub app will request read & write permissions for Contents, Issues, and Pull requests
  * This quickstart method is only available for direct Claude API users. If
    you're using AWS Bedrock or Google Vertex AI, please see the [Using with AWS
    Bedrock & Google Vertex AI](#using-with-aws-bedrock-%26-google-vertex-ai)
    section.
</Note>

## Manual setup

If the `/install-github-app` command fails or you prefer manual setup, please follow these manual setup instructions:

1. **Install the Claude GitHub app** to your repository: [https://github.com/apps/claude](https://github.com/apps/claude)

   The Claude GitHub app requires the following repository permissions:

   * **Contents**: Read & write (to modify repository files)
   * **Issues**: Read & write (to respond to issues)
   * **Pull requests**: Read & write (to create PRs and push changes)

   For more details on security and permissions, see the [security documentation](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md).
2. **Add ANTHROPIC\_API\_KEY** to your repository secrets ([Learn how to use secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions))
3. **Copy the workflow file** from [examples/claude.yml](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml) into your repository's `.github/workflows/`

<Tip>
  After completing either the quickstart or manual setup, test the action by
  tagging `@claude` in an issue or PR comment!
</Tip>

## Upgrading from Beta

<Warning>
  Claude Code GitHub Actions v1.0 introduces breaking changes that require updating your workflow files in order to upgrade to v1.0 from the beta version.
</Warning>

If you're currently using the beta version of Claude Code GitHub Actions, we recommend that you update your workflows to use the GA version. The new version simplifies configuration while adding powerful new features like automatic mode detection.

### Essential changes

All beta users must make these changes to their workflow files in order to upgrade:

1. **Update the action version**: Change `@beta` to `@v1`
2. **Remove mode configuration**: Delete `mode: "tag"` or `mode: "agent"` (now auto-detected)
3. **Update prompt inputs**: Replace `direct_prompt` with `prompt`
4. **Move CLI options**: Convert `max_turns`, `model`, `custom_instructions`, etc. to `claude_args`

### Breaking Changes Reference

| Old Beta Input        | New v1.0 Input                   |
| --------------------- | -------------------------------- |
| `mode`                | *(Removed - auto-detected)*      |
| `direct_prompt`       | `prompt`                         |
| `override_prompt`     | `prompt` with GitHub variables   |
| `custom_instructions` | `claude_args: --system-prompt`   |
| `max_turns`           | `claude_args: --max-turns`       |
| `model`               | `claude_args: --model`           |
| `allowed_tools`       | `claude_args: --allowedTools`    |
| `disallowed_tools`    | `claude_args: --disallowedTools` |
| `claude_env`          | `settings` JSON format           |

### Before and After Example

**Beta version:**

```yaml  theme={null}
- uses: anthropics/claude-code-action@beta
  with:
    mode: "tag"
    direct_prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    custom_instructions: "Follow our coding standards"
    max_turns: "10"
    model: "claude-sonnet-4-5-20250929"
```

**GA version (v1.0):**

```yaml  theme={null}
- uses: anthropics/claude-code-action@v1
  with:
    prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    claude_args: |
      --system-prompt "Follow our coding standards"
      --max-turns 10
      --model claude-sonnet-4-5-20250929
```

<Tip>
  The action now automatically detects whether to run in interactive mode (responds to `@claude` mentions) or automation mode (runs immediately with a prompt) based on your configuration.
</Tip>

## Example use cases

Claude Code GitHub Actions can help you with a variety of tasks. The [examples directory](https://github.com/anthropics/claude-code-action/tree/main/examples) contains ready-to-use workflows for different scenarios.

### Basic workflow

```yaml  theme={null}
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # Responds to @claude mentions in comments
```

### Using slash commands

```yaml  theme={null}
name: Code Review
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "/review"
          claude_args: "--max-turns 5"
```

### Custom automation with prompts

```yaml  theme={null}
name: Daily Report
on:
  schedule:
    - cron: "0 9 * * *"
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "Generate a summary of yesterday's commits and open issues"
          claude_args: "--model claude-opus-4-1-20250805"
```

### Common use cases

In issue or PR comments:

```
@claude implement this feature based on the issue description
@claude how should I implement user authentication for this endpoint?
@claude fix the TypeError in the user dashboard component
```

Claude will automatically analyze the context and respond appropriately.

## Best practices

### CLAUDE.md configuration

Create a `CLAUDE.md` file in your repository root to define code style guidelines, review criteria, project-specific rules, and preferred patterns. This file guides Claude's understanding of your project standards.

### Security considerations

<Warning>Never commit API keys directly to your repository!</Warning>

For comprehensive security guidance including permissions, authentication, and best practices, see the [Claude Code Action security documentation](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md).

Always use GitHub Secrets for API keys:

* Add your API key as a repository secret named `ANTHROPIC_API_KEY`
* Reference it in workflows: `anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}`
* Limit action permissions to only what's necessary
* Review Claude's suggestions before merging

Always use GitHub Secrets (e.g., `${{ secrets.ANTHROPIC_API_KEY }}`) rather than hardcoding API keys directly in your workflow files.

### Optimizing performance

Use issue templates to provide context, keep your `CLAUDE.md` concise and focused, and configure appropriate timeouts for your workflows.

### CI costs

When using Claude Code GitHub Actions, be aware of the associated costs:

**GitHub Actions costs:**

* Claude Code runs on GitHub-hosted runners, which consume your GitHub Actions minutes
* See [GitHub's billing documentation](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) for detailed pricing and minute limits

**API costs:**

* Each Claude interaction consumes API tokens based on the length of prompts and responses
* Token usage varies by task complexity and codebase size
* See [Claude's pricing page](https://claude.com/platform/api) for current token rates

**Cost optimization tips:**

* Use specific `@claude` commands to reduce unnecessary API calls
* Configure appropriate `--max-turns` in `claude_args` to prevent excessive iterations
* Set workflow-level timeouts to avoid runaway jobs
* Consider using GitHub's concurrency controls to limit parallel runs

## Configuration examples

The Claude Code Action v1 simplifies configuration with unified parameters:

```yaml  theme={null}
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    prompt: "Your instructions here" # Optional
    claude_args: "--max-turns 5" # Optional CLI arguments
```

Key features:

* **Unified prompt interface** - Use `prompt` for all instructions
* **Slash commands** - Pre-built prompts like `/review` or `/fix`
* **CLI passthrough** - Any Claude Code CLI argument via `claude_args`
* **Flexible triggers** - Works with any GitHub event

Visit the [examples directory](https://github.com/anthropics/claude-code-action/tree/main/examples) for complete workflow files.

<Tip>
  When responding to issue or PR comments, Claude automatically responds to @claude mentions. For other events, use the `prompt` parameter to provide instructions.
</Tip>

## Using with AWS Bedrock & Google Vertex AI

For enterprise environments, you can use Claude Code GitHub Actions with your own cloud infrastructure. This approach gives you control over data residency and billing while maintaining the same functionality.

### Prerequisites

Before setting up Claude Code GitHub Actions with cloud providers, you need:

#### For Google Cloud Vertex AI:

1. A Google Cloud Project with Vertex AI enabled
2. Workload Identity Federation configured for GitHub Actions
3. A service account with the required permissions
4. A GitHub App (recommended) or use the default GITHUB\_TOKEN

#### For AWS Bedrock:

1. An AWS account with Amazon Bedrock enabled
2. GitHub OIDC Identity Provider configured in AWS
3. An IAM role with Bedrock permissions
4. A GitHub App (recommended) or use the default GITHUB\_TOKEN

<Steps>
  <Step title="Create a custom GitHub App (Recommended for 3P Providers)">
    For best control and security when using 3P providers like Vertex AI or Bedrock, we recommend creating your own GitHub App:

    1. Go to [https://github.com/settings/apps/new](https://github.com/settings/apps/new)
    2. Fill in the basic information:
       * **GitHub App name**: Choose a unique name (e.g., "YourOrg Claude Assistant")
       * **Homepage URL**: Your organization's website or the repository URL
    3. Configure the app settings:
       * **Webhooks**: Uncheck "Active" (not needed for this integration)
    4. Set the required permissions:
       * **Repository permissions**:
         * Contents: Read & Write
         * Issues: Read & Write
         * Pull requests: Read & Write
    5. Click "Create GitHub App"
    6. After creation, click "Generate a private key" and save the downloaded `.pem` file
    7. Note your App ID from the app settings page
    8. Install the app to your repository:
       * From your app's settings page, click "Install App" in the left sidebar
       * Select your account or organization
       * Choose "Only select repositories" and select the specific repository
       * Click "Install"
    9. Add the private key as a secret to your repository:
       * Go to your repository's Settings → Secrets and variables → Actions
       * Create a new secret named `APP_PRIVATE_KEY` with the contents of the `.pem` file
    10. Add the App ID as a secret:

    * Create a new secret named `APP_ID` with your GitHub App's ID

    <Note>
      This app will be used with the [actions/create-github-app-token](https://github.com/actions/create-github-app-token) action to generate authentication tokens in your workflows.
    </Note>

    **Alternative for Claude API or if you don't want to setup your own Github app**: Use the official Anthropic app:

    1. Install from: [https://github.com/apps/claude](https://github.com/apps/claude)
    2. No additional configuration needed for authentication
  </Step>

  <Step title="Configure cloud provider authentication">
    Choose your cloud provider and set up secure authentication:

    <AccordionGroup>
      <Accordion title="AWS Bedrock">
        **Configure AWS to allow GitHub Actions to authenticate securely without storing credentials.**

        > **Security Note**: Use repository-specific configurations and grant only the minimum required permissions.

        **Required Setup**:

        1. **Enable Amazon Bedrock**:
           * Request access to Claude models in Amazon Bedrock
           * For cross-region models, request access in all required regions

        2. **Set up GitHub OIDC Identity Provider**:
           * Provider URL: `https://token.actions.githubusercontent.com`
           * Audience: `sts.amazonaws.com`

        3. **Create IAM Role for GitHub Actions**:
           * Trusted entity type: Web identity
           * Identity provider: `token.actions.githubusercontent.com`
           * Permissions: `AmazonBedrockFullAccess` policy
           * Configure trust policy for your specific repository

        **Required Values**:

        After setup, you'll need:

        * **AWS\_ROLE\_TO\_ASSUME**: The ARN of the IAM role you created

        <Tip>
          OIDC is more secure than using static AWS access keys because credentials are temporary and automatically rotated.
        </Tip>

        See [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) for detailed OIDC setup instructions.
      </Accordion>

      <Accordion title="Google Vertex AI">
        **Configure Google Cloud to allow GitHub Actions to authenticate securely without storing credentials.**

        > **Security Note**: Use repository-specific configurations and grant only the minimum required permissions.

        **Required Setup**:

        1. **Enable APIs** in your Google Cloud project:
           * IAM Credentials API
           * Security Token Service (STS) API
           * Vertex AI API

        2. **Create Workload Identity Federation resources**:
           * Create a Workload Identity Pool
           * Add a GitHub OIDC provider with:
             * Issuer: `https://token.actions.githubusercontent.com`
             * Attribute mappings for repository and owner
             * **Security recommendation**: Use repository-specific attribute conditions

        3. **Create a Service Account**:
           * Grant only `Vertex AI User` role
           * **Security recommendation**: Create a dedicated service account per repository

        4. **Configure IAM bindings**:
           * Allow the Workload Identity Pool to impersonate the service account
           * **Security recommendation**: Use repository-specific principal sets

        **Required Values**:

        After setup, you'll need:

        * **GCP\_WORKLOAD\_IDENTITY\_PROVIDER**: The full provider resource name
        * **GCP\_SERVICE\_ACCOUNT**: The service account email address

        <Tip>
          Workload Identity Federation eliminates the need for downloadable service account keys, improving security.
        </Tip>

        For detailed setup instructions, consult the [Google Cloud Workload Identity Federation documentation](https://cloud.google.com/iam/docs/workload-identity-federation).
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Add Required Secrets">
    Add the following secrets to your repository (Settings → Secrets and variables → Actions):

    #### For Claude API (Direct):

    1. **For API Authentication**:
       * `ANTHROPIC_API_KEY`: Your Claude API key from [console.anthropic.com](https://console.anthropic.com)

    2. **For GitHub App (if using your own app)**:
       * `APP_ID`: Your GitHub App's ID
       * `APP_PRIVATE_KEY`: The private key (.pem) content

    #### For Google Cloud Vertex AI

    1. **For GCP Authentication**:
       * `GCP_WORKLOAD_IDENTITY_PROVIDER`
       * `GCP_SERVICE_ACCOUNT`

    2. **For GitHub App (if using your own app)**:
       * `APP_ID`: Your GitHub App's ID
       * `APP_PRIVATE_KEY`: The private key (.pem) content

    #### For AWS Bedrock

    1. **For AWS Authentication**:
       * `AWS_ROLE_TO_ASSUME`

    2. **For GitHub App (if using your own app)**:
       * `APP_ID`: Your GitHub App's ID
       * `APP_PRIVATE_KEY`: The private key (.pem) content
  </Step>

  <Step title="Create workflow files">
    Create GitHub Actions workflow files that integrate with your cloud provider. The examples below show complete configurations for both AWS Bedrock and Google Vertex AI:

    <AccordionGroup>
      <Accordion title="AWS Bedrock workflow">
        **Prerequisites:**

        * AWS Bedrock access enabled with Claude model permissions
        * GitHub configured as an OIDC identity provider in AWS
        * IAM role with Bedrock permissions that trusts GitHub Actions

        **Required GitHub secrets:**

        | Secret Name          | Description                                       |
        | -------------------- | ------------------------------------------------- |
        | `AWS_ROLE_TO_ASSUME` | ARN of the IAM role for Bedrock access            |
        | `APP_ID`             | Your GitHub App ID (from app settings)            |
        | `APP_PRIVATE_KEY`    | The private key you generated for your GitHub App |

        ```yaml  theme={null}
        name: Claude PR Action

        permissions:
          contents: write
          pull-requests: write
          issues: write
          id-token: write

        on:
          issue_comment:
            types: [created]
          pull_request_review_comment:
            types: [created]
          issues:
            types: [opened, assigned]

        jobs:
          claude-pr:
            if: |
              (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
            runs-on: ubuntu-latest
            env:
              AWS_REGION: us-west-2
            steps:
              - name: Checkout repository
                uses: actions/checkout@v4

              - name: Generate GitHub App token
                id: app-token
                uses: actions/create-github-app-token@v2
                with:
                  app-id: ${{ secrets.APP_ID }}
                  private-key: ${{ secrets.APP_PRIVATE_KEY }}

              - name: Configure AWS Credentials (OIDC)
                uses: aws-actions/configure-aws-credentials@v4
                with:
                  role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
                  aws-region: us-west-2

              - uses: anthropics/claude-code-action@v1
                with:
                  github_token: ${{ steps.app-token.outputs.token }}
                  use_bedrock: "true"
                  claude_args: '--model us.anthropic.claude-sonnet-4-5-20250929-v1:0 --max-turns 10'
        ```

        <Tip>
          The model ID format for Bedrock includes the region prefix (e.g., `us.anthropic.claude...`) and version suffix.
        </Tip>
      </Accordion>

      <Accordion title="Google Vertex AI workflow">
        **Prerequisites:**

        * Vertex AI API enabled in your GCP project
        * Workload Identity Federation configured for GitHub
        * Service account with Vertex AI permissions

        **Required GitHub secrets:**

        | Secret Name                      | Description                                       |
        | -------------------------------- | ------------------------------------------------- |
        | `GCP_WORKLOAD_IDENTITY_PROVIDER` | Workload identity provider resource name          |
        | `GCP_SERVICE_ACCOUNT`            | Service account email with Vertex AI access       |
        | `APP_ID`                         | Your GitHub App ID (from app settings)            |
        | `APP_PRIVATE_KEY`                | The private key you generated for your GitHub App |

        ```yaml  theme={null}
        name: Claude PR Action

        permissions:
          contents: write
          pull-requests: write
          issues: write
          id-token: write

        on:
          issue_comment:
            types: [created]
          pull_request_review_comment:
            types: [created]
          issues:
            types: [opened, assigned]

        jobs:
          claude-pr:
            if: |
              (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
            runs-on: ubuntu-latest
            steps:
              - name: Checkout repository
                uses: actions/checkout@v4

              - name: Generate GitHub App token
                id: app-token
                uses: actions/create-github-app-token@v2
                with:
                  app-id: ${{ secrets.APP_ID }}
                  private-key: ${{ secrets.APP_PRIVATE_KEY }}

              - name: Authenticate to Google Cloud
                id: auth
                uses: google-github-actions/auth@v2
                with:
                  workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
                  service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

              - uses: anthropics/claude-code-action@v1
                with:
                  github_token: ${{ steps.app-token.outputs.token }}
                  trigger_phrase: "@claude"
                  use_vertex: "true"
                  claude_args: '--model claude-sonnet-4@20250514 --max-turns 10'
                env:
                  ANTHROPIC_VERTEX_PROJECT_ID: ${{ steps.auth.outputs.project_id }}
                  CLOUD_ML_REGION: us-east5
                  VERTEX_REGION_CLAUDE_3_7_SONNET: us-east5
        ```

        <Tip>
          The project ID is automatically retrieved from the Google Cloud authentication step, so you don't need to hardcode it.
        </Tip>
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>

## Troubleshooting

### Claude not responding to @claude commands

Verify the GitHub App is installed correctly, check that workflows are enabled, ensure API key is set in repository secrets, and confirm the comment contains `@claude` (not `/claude`).

### CI not running on Claude's commits

Ensure you're using the GitHub App or custom app (not Actions user), check workflow triggers include the necessary events, and verify app permissions include CI triggers.

### Authentication errors

Confirm API key is valid and has sufficient permissions. For Bedrock/Vertex, check credentials configuration and ensure secrets are named correctly in workflows.

## Advanced configuration

### Action parameters

The Claude Code Action v1 uses a simplified configuration:

| Parameter           | Description                                     | Required |
| ------------------- | ----------------------------------------------- | -------- |
| `prompt`            | Instructions for Claude (text or slash command) | No\*     |
| `claude_args`       | CLI arguments passed to Claude Code             | No       |
| `anthropic_api_key` | Claude API key                                  | Yes\*\*  |
| `github_token`      | GitHub token for API access                     | No       |
| `trigger_phrase`    | Custom trigger phrase (default: "@claude")      | No       |
| `use_bedrock`       | Use AWS Bedrock instead of Claude API           | No       |
| `use_vertex`        | Use Google Vertex AI instead of Claude API      | No       |

\*Prompt is optional - when omitted for issue/PR comments, Claude responds to trigger phrase\
\*\*Required for direct Claude API, not for Bedrock/Vertex

#### Using claude\_args

The `claude_args` parameter accepts any Claude Code CLI arguments:

```yaml  theme={null}
claude_args: "--max-turns 5 --model claude-sonnet-4-5-20250929 --mcp-config /path/to/config.json"
```

Common arguments:

* `--max-turns`: Maximum conversation turns (default: 10)
* `--model`: Model to use (e.g., `claude-sonnet-4-5-20250929`)
* `--mcp-config`: Path to MCP configuration
* `--allowed-tools`: Comma-separated list of allowed tools
* `--debug`: Enable debug output

### Alternative integration methods

While the `/install-github-app` command is the recommended approach, you can also:

* **Custom GitHub App**: For organizations needing branded usernames or custom authentication flows. Create your own GitHub App with required permissions (contents, issues, pull requests) and use the actions/create-github-app-token action to generate tokens in your workflows.
* **Manual GitHub Actions**: Direct workflow configuration for maximum flexibility
* **MCP Configuration**: Dynamic loading of Model Context Protocol servers

See the [Claude Code Action documentation](https://github.com/anthropics/claude-code-action/blob/main/docs) for detailed guides on authentication, security, and advanced configuration.

### Customizing Claude's behavior

You can configure Claude's behavior in two ways:

1. **CLAUDE.md**: Define coding standards, review criteria, and project-specific rules in a `CLAUDE.md` file at the root of your repository. Claude will follow these guidelines when creating PRs and responding to requests. Check out our [Memory documentation](/en/memory) for more details.
2. **Custom prompts**: Use the `prompt` parameter in the workflow file to provide workflow-specific instructions. This allows you to customize Claude's behavior for different workflows or tasks.

Claude will follow these guidelines when creating PRs and responding to requests.


# Claude Code GitLab CI/CD
Source: https://code.claude.com/docs/en/gitlab-ci-cd

Learn about integrating Claude Code into your development workflow with GitLab CI/CD

<Info>
  Claude Code for GitLab CI/CD is currently in beta. Features and functionality may evolve as we refine the experience.

  This integration is maintained by GitLab. For support, see the following [GitLab issue](https://gitlab.com/gitlab-org/gitlab/-/issues/573776).
</Info>

<Note>
  This integration is built on top of the [Claude Code CLI and SDK](https://docs.claude.com/en/docs/agent-sdk), enabling programmatic use of Claude in your CI/CD jobs and custom automation workflows.
</Note>

## Why use Claude Code with GitLab?

* **Instant MR creation**: Describe what you need, and Claude proposes a complete MR with changes and explanation
* **Automated implementation**: Turn issues into working code with a single command or mention
* **Project-aware**: Claude follows your `CLAUDE.md` guidelines and existing code patterns
* **Simple setup**: Add one job to `.gitlab-ci.yml` and a masked CI/CD variable
* **Enterprise-ready**: Choose Claude API, AWS Bedrock, or Google Vertex AI to meet data residency and procurement needs
* **Secure by default**: Runs in your GitLab runners with your branch protection and approvals

## How it works

Claude Code uses GitLab CI/CD to run AI tasks in isolated jobs and commit results back via MRs:

1. **Event-driven orchestration**: GitLab listens for your chosen triggers (for example, a comment that mentions `@claude` in an issue, MR, or review thread). The job collects context from the thread and repository, builds prompts from that input, and runs Claude Code.

2. **Provider abstraction**: Use the provider that fits your environment:
   * Claude API (SaaS)
   * AWS Bedrock (IAM-based access, cross-region options)
   * Google Vertex AI (GCP-native, Workload Identity Federation)

3. **Sandboxed execution**: Each interaction runs in a container with strict network and filesystem rules. Claude Code enforces workspace-scoped permissions to constrain writes. Every change flows through an MR so reviewers see the diff and approvals still apply.

Pick regional endpoints to reduce latency and meet data-sovereignty requirements while using existing cloud agreements.

## What can Claude do?

Claude Code enables powerful CI/CD workflows that transform how you work with code:

* Create and update MRs from issue descriptions or comments
* Analyze performance regressions and propose optimizations
* Implement features directly in a branch, then open an MR
* Fix bugs and regressions identified by tests or comments
* Respond to follow-up comments to iterate on requested changes

## Setup

### Quick setup

The fastest way to get started is to add a minimal job to your `.gitlab-ci.yml` and set your API key as a masked variable.

1. **Add a masked CI/CD variable**
   * Go to **Settings** → **CI/CD** → **Variables**
   * Add `ANTHROPIC_API_KEY` (masked, protected as needed)

2. **Add a Claude job to `.gitlab-ci.yml`**

```yaml  theme={null}
stages:
  - ai

claude:
  stage: ai
  image: node:24-alpine3.21
  # Adjust rules to fit how you want to trigger the job:
  # - manual runs
  # - merge request events
  # - web/API triggers when a comment contains '@claude'
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  variables:
    GIT_STRATEGY: fetch
  before_script:
    - apk update
    - apk add --no-cache git curl bash
    - npm install -g @anthropic-ai/claude-code
  script:
    # Optional: start a GitLab MCP server if your setup provides one
    - /bin/gitlab-mcp-server || true
    # Use AI_FLOW_* variables when invoking via web/API triggers with context payloads
    - echo "$AI_FLOW_INPUT for $AI_FLOW_CONTEXT on $AI_FLOW_EVENT"
    - >
      claude
      -p "${AI_FLOW_INPUT:-'Review this MR and implement the requested changes'}"
      --permission-mode acceptEdits
      --allowedTools "Bash(*) Read(*) Edit(*) Write(*) mcp__gitlab"
      --debug
```

After adding the job and your `ANTHROPIC_API_KEY` variable, test by running the job manually from **CI/CD** → **Pipelines**, or trigger it from an MR to let Claude propose updates in a branch and open an MR if needed.

<Note>
  To run on AWS Bedrock or Google Vertex AI instead of the Claude API, see the [Using with AWS Bedrock & Google Vertex AI](#using-with-aws-bedrock--google-vertex-ai) section below for authentication and environment setup.
</Note>

### Manual setup (recommended for production)

If you prefer a more controlled setup or need enterprise providers:

1. **Configure provider access**:
   * **Claude API**: Create and store `ANTHROPIC_API_KEY` as a masked CI/CD variable
   * **AWS Bedrock**: **Configure GitLab** → **AWS OIDC** and create an IAM role for Bedrock
   * **Google Vertex AI**: **Configure Workload Identity Federation for GitLab** → **GCP**

2. **Add project credentials for GitLab API operations**:
   * Use `CI_JOB_TOKEN` by default, or create a Project Access Token with `api` scope
   * Store as `GITLAB_ACCESS_TOKEN` (masked) if using a PAT

3. **Add the Claude job to `.gitlab-ci.yml`** (see examples below)

4. **(Optional) Enable mention-driven triggers**:
   * Add a project webhook for "Comments (notes)" to your event listener (if you use one)
   * Have the listener call the pipeline trigger API with variables like `AI_FLOW_INPUT` and `AI_FLOW_CONTEXT` when a comment contains `@claude`

## Example use cases

### Turn issues into MRs

In an issue comment:

```
@claude implement this feature based on the issue description
```

Claude analyzes the issue and codebase, writes changes in a branch, and opens an MR for review.

### Get implementation help

In an MR discussion:

```
@claude suggest a concrete approach to cache the results of this API call
```

Claude proposes changes, adds code with appropriate caching, and updates the MR.

### Fix bugs quickly

In an issue or MR comment:

```
@claude fix the TypeError in the user dashboard component
```

Claude locates the bug, implements a fix, and updates the branch or opens a new MR.

## Using with AWS Bedrock & Google Vertex AI

For enterprise environments, you can run Claude Code entirely on your cloud infrastructure with the same developer experience.

<Tabs>
  <Tab title="AWS Bedrock">
    ### Prerequisites

    Before setting up Claude Code with AWS Bedrock, you need:

    1. An AWS account with Amazon Bedrock access to the desired Claude models
    2. GitLab configured as an OIDC identity provider in AWS IAM
    3. An IAM role with Bedrock permissions and a trust policy restricted to your GitLab project/refs
    4. GitLab CI/CD variables for role assumption:
       * `AWS_ROLE_TO_ASSUME` (role ARN)
       * `AWS_REGION` (Bedrock region)

    ### Setup instructions

    Configure AWS to allow GitLab CI jobs to assume an IAM role via OIDC (no static keys).

    **Required setup:**

    1. Enable Amazon Bedrock and request access to your target Claude models
    2. Create an IAM OIDC provider for GitLab if not already present
    3. Create an IAM role trusted by the GitLab OIDC provider, restricted to your project and protected refs
    4. Attach least-privilege permissions for Bedrock invoke APIs

    **Required values to store in CI/CD variables:**

    * `AWS_ROLE_TO_ASSUME`
    * `AWS_REGION`

    Add variables in Settings → CI/CD → Variables:

    ```yaml  theme={null}
    # For AWS Bedrock:
    - AWS_ROLE_TO_ASSUME
    - AWS_REGION
    ```

    Use the AWS Bedrock job example above to exchange the GitLab job token for temporary AWS credentials at runtime.
  </Tab>

  <Tab title="Google Vertex AI">
    ### Prerequisites

    Before setting up Claude Code with Google Vertex AI, you need:

    1. A Google Cloud project with:
       * Vertex AI API enabled
       * Workload Identity Federation configured to trust GitLab OIDC
    2. A dedicated service account with only the required Vertex AI roles
    3. GitLab CI/CD variables for WIF:
       * `GCP_WORKLOAD_IDENTITY_PROVIDER` (full resource name)
       * `GCP_SERVICE_ACCOUNT` (service account email)

    ### Setup instructions

    Configure Google Cloud to allow GitLab CI jobs to impersonate a service account via Workload Identity Federation.

    **Required setup:**

    1. Enable IAM Credentials API, STS API, and Vertex AI API
    2. Create a Workload Identity Pool and provider for GitLab OIDC
    3. Create a dedicated service account with Vertex AI roles
    4. Grant the WIF principal permission to impersonate the service account

    **Required values to store in CI/CD variables:**

    * `GCP_WORKLOAD_IDENTITY_PROVIDER`
    * `GCP_SERVICE_ACCOUNT`

    Add variables in Settings → CI/CD → Variables:

    ```yaml  theme={null}
    # For Google Vertex AI:
    - GCP_WORKLOAD_IDENTITY_PROVIDER
    - GCP_SERVICE_ACCOUNT
    - CLOUD_ML_REGION (for example, us-east5)
    ```

    Use the Google Vertex AI job example above to authenticate without storing keys.
  </Tab>
</Tabs>

## Configuration examples

Below are ready-to-use snippets you can adapt to your pipeline.

### Basic .gitlab-ci.yml (Claude API)

```yaml  theme={null}
stages:
  - ai

claude:
  stage: ai
  image: node:24-alpine3.21
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  variables:
    GIT_STRATEGY: fetch
  before_script:
    - apk update
    - apk add --no-cache git curl bash
    - npm install -g @anthropic-ai/claude-code
  script:
    - /bin/gitlab-mcp-server || true
    - >
      claude
      -p "${AI_FLOW_INPUT:-'Summarize recent changes and suggest improvements'}"
      --permission-mode acceptEdits
      --allowedTools "Bash(*) Read(*) Edit(*) Write(*) mcp__gitlab"
      --debug
  # Claude Code will use ANTHROPIC_API_KEY from CI/CD variables
```

### AWS Bedrock job example (OIDC)

**Prerequisites:**

* Amazon Bedrock enabled with access to your chosen Claude model(s)
* GitLab OIDC configured in AWS with a role that trusts your GitLab project and refs
* IAM role with Bedrock permissions (least privilege recommended)

**Required CI/CD variables:**

* `AWS_ROLE_TO_ASSUME`: ARN of the IAM role for Bedrock access
* `AWS_REGION`: Bedrock region (for example, `us-west-2`)

```yaml  theme={null}
claude-bedrock:
  stage: ai
  image: node:24-alpine3.21
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
  before_script:
    - apk add --no-cache bash curl jq git python3 py3-pip
    - pip install --no-cache-dir awscli
    - npm install -g @anthropic-ai/claude-code
    # Exchange GitLab OIDC token for AWS credentials
    - export AWS_WEB_IDENTITY_TOKEN_FILE="${CI_JOB_JWT_FILE:-/tmp/oidc_token}"
    - if [ -n "${CI_JOB_JWT_V2}" ]; then printf "%s" "$CI_JOB_JWT_V2" > "$AWS_WEB_IDENTITY_TOKEN_FILE"; fi
    - >
      aws sts assume-role-with-web-identity
      --role-arn "$AWS_ROLE_TO_ASSUME"
      --role-session-name "gitlab-claude-$(date +%s)"
      --web-identity-token "file://$AWS_WEB_IDENTITY_TOKEN_FILE"
      --duration-seconds 3600 > /tmp/aws_creds.json
    - export AWS_ACCESS_KEY_ID="$(jq -r .Credentials.AccessKeyId /tmp/aws_creds.json)"
    - export AWS_SECRET_ACCESS_KEY="$(jq -r .Credentials.SecretAccessKey /tmp/aws_creds.json)"
    - export AWS_SESSION_TOKEN="$(jq -r .Credentials.SessionToken /tmp/aws_creds.json)"
  script:
    - /bin/gitlab-mcp-server || true
    - >
      claude
      -p "${AI_FLOW_INPUT:-'Implement the requested changes and open an MR'}"
      --permission-mode acceptEdits
      --allowedTools "Bash(*) Read(*) Edit(*) Write(*) mcp__gitlab"
      --debug
  variables:
    AWS_REGION: "us-west-2"
```

<Note>
  Model IDs for Bedrock include region-specific prefixes and version suffixes (for example, `us.anthropic.claude-sonnet-4-5-20250929-v1:0`). Pass the desired model via your job configuration or prompt if your workflow supports it.
</Note>

### Google Vertex AI job example (Workload Identity Federation)

**Prerequisites:**

* Vertex AI API enabled in your GCP project
* Workload Identity Federation configured to trust GitLab OIDC
* A service account with Vertex AI permissions

**Required CI/CD variables:**

* `GCP_WORKLOAD_IDENTITY_PROVIDER`: Full provider resource name
* `GCP_SERVICE_ACCOUNT`: Service account email
* `CLOUD_ML_REGION`: Vertex region (for example, `us-east5`)

```yaml  theme={null}
claude-vertex:
  stage: ai
  image: gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
  before_script:
    - apt-get update && apt-get install -y git nodejs npm && apt-get clean
    - npm install -g @anthropic-ai/claude-code
    # Authenticate to Google Cloud via WIF (no downloaded keys)
    - >
      gcloud auth login --cred-file=<(cat <<EOF
      {
        "type": "external_account",
        "audience": "${GCP_WORKLOAD_IDENTITY_PROVIDER}",
        "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
        "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/${GCP_SERVICE_ACCOUNT}:generateAccessToken",
        "token_url": "https://sts.googleapis.com/v1/token"
      }
      EOF
      )
    - gcloud config set project "$(gcloud projects list --format='value(projectId)' --filter="name:${CI_PROJECT_NAMESPACE}" | head -n1)" || true
  script:
    - /bin/gitlab-mcp-server || true
    - >
      CLOUD_ML_REGION="${CLOUD_ML_REGION:-us-east5}"
      claude
      -p "${AI_FLOW_INPUT:-'Review and update code as requested'}"
      --permission-mode acceptEdits
      --allowedTools "Bash(*) Read(*) Edit(*) Write(*) mcp__gitlab"
      --debug
  variables:
    CLOUD_ML_REGION: "us-east5"
```

<Note>
  With Workload Identity Federation, you do not need to store service account keys. Use repository-specific trust conditions and least-privilege service accounts.
</Note>

## Best practices

### CLAUDE.md configuration

Create a `CLAUDE.md` file at the repository root to define coding standards, review criteria, and project-specific rules. Claude reads this file during runs and follows your conventions when proposing changes.

### Security considerations

Never commit API keys or cloud credentials to your repository! Always use GitLab CI/CD variables:

* Add `ANTHROPIC_API_KEY` as a masked variable (and protect it if needed)
* Use provider-specific OIDC where possible (no long-lived keys)
* Limit job permissions and network egress
* Review Claude's MRs like any other contributor

### Optimizing performance

* Keep `CLAUDE.md` focused and concise
* Provide clear issue/MR descriptions to reduce iterations
* Configure sensible job timeouts to avoid runaway runs
* Cache npm and package installs in runners where possible

### CI costs

When using Claude Code with GitLab CI/CD, be aware of associated costs:

* **GitLab Runner time**:
  * Claude runs on your GitLab runners and consumes compute minutes
  * See your GitLab plan's runner billing for details

* **API costs**:
  * Each Claude interaction consumes tokens based on prompt and response size
  * Token usage varies by task complexity and codebase size
  * See [Anthropic pricing](https://docs.claude.com/en/docs/about-claude/pricing) for details

* **Cost optimization tips**:
  * Use specific `@claude` commands to reduce unnecessary turns
  * Set appropriate `max_turns` and job timeout values
  * Limit concurrency to control parallel runs

## Security and governance

* Each job runs in an isolated container with restricted network access
* Claude's changes flow through MRs so reviewers see every diff
* Branch protection and approval rules apply to AI-generated code
* Claude Code uses workspace-scoped permissions to constrain writes
* Costs remain under your control because you bring your own provider credentials

## Troubleshooting

### Claude not responding to @claude commands

* Verify your pipeline is being triggered (manually, MR event, or via a note event listener/webhook)
* Ensure CI/CD variables (`ANTHROPIC_API_KEY` or cloud provider settings) are present and unmasked
* Check that the comment contains `@claude` (not `/claude`) and that your mention trigger is configured

### Job can't write comments or open MRs

* Ensure `CI_JOB_TOKEN` has sufficient permissions for the project, or use a Project Access Token with `api` scope
* Check the `mcp__gitlab` tool is enabled in `--allowedTools`
* Confirm the job runs in the context of the MR or has enough context via `AI_FLOW_*` variables

### Authentication errors

* **For Claude API**: Confirm `ANTHROPIC_API_KEY` is valid and unexpired
* **For Bedrock/Vertex**: Verify OIDC/WIF configuration, role impersonation, and secret names; confirm region and model availability

## Advanced configuration

### Common parameters and variables

Claude Code supports these commonly used inputs:

* `prompt` / `prompt_file`: Provide instructions inline (`-p`) or via a file
* `max_turns`: Limit the number of back-and-forth iterations
* `timeout_minutes`: Limit total execution time
* `ANTHROPIC_API_KEY`: Required for the Claude API (not used for Bedrock/Vertex)
* Provider-specific environment: `AWS_REGION`, project/region vars for Vertex

<Note>
  Exact flags and parameters may vary by version of `@anthropic-ai/claude-code`. Run `claude --help` in your job to see supported options.
</Note>

### Customizing Claude's behavior

You can guide Claude in two primary ways:

1. **CLAUDE.md**: Define coding standards, security requirements, and project conventions. Claude reads this during runs and follows your rules.
2. **Custom prompts**: Pass task-specific instructions via `prompt`/`prompt_file` in the job. Use different prompts for different jobs (for example, review, implement, refactor).



---

**Navigation:** [← Previous: Deployment](./04-deployment.md) | [Index](./index.md) | [Next: Integrations →](./06-integrations.md)
