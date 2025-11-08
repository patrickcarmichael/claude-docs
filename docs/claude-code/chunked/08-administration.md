# Administration & Monitoring

**Navigation:** [← Previous: Advanced Features](./07-advanced.md) | [Index](./index.md) | [Next: Reference →](./09-reference.md)

> **Note:** This is part of the chunked llms-full.txt. For organized topic documentation, see [../README.md](../README.md)

---

# Analytics
Source: https://code.claude.com/docs/en/analytics

View detailed usage insights and productivity metrics for your organization's Claude Code deployment.

Claude Code provides an analytics dashboard that helps organizations understand developer usage patterns, track productivity metrics, and optimize their Claude Code adoption.

<Note>
  Analytics are currently available only for organizations using Claude Code with the Claude API through the Claude Console.
</Note>

## Access analytics

Navigate to the analytics dashboard at [console.anthropic.com/claude-code](https://console.anthropic.com/claude-code).

### Required roles

* **Primary Owner**
* **Owner**
* **Billing**
* **Admin**
* **Developer**

<Note>
  Users with **User**, **Claude Code User** or **Membership Admin** roles cannot access analytics.
</Note>

## Available metrics

### Lines of code accepted

Total lines of code written by Claude Code that users have accepted in their sessions.

* Excludes rejected code suggestions
* Doesn't track subsequent deletions

### Suggestion accept rate

Percentage of times users accept code editing tool usage, including:

* Edit
* Write
* NotebookEdit

### Activity

**users**: Number of active users in a given day (number on left Y-axis)

**sessions**: Number of active sessions in a given day (number on right Y-axis)

### Spend

**users**: Number of active users in a given day (number on left Y-axis)

**spend**: Total dollars spent in a given day (number on right Y-axis)

### Team insights

**Members**: All users who have authenticated to Claude Code

* API key users are displayed by **API key identifier**
* OAuth users are displayed by **email address**

**Spend this month:** Per-user total spend for the current month.

**Lines this month:** Per-user total of accepted code lines for the current month.

## Using analytics effectively

### Monitor adoption

Track team member status to identify:

* Active users who can share best practices
* Overall adoption trends across your organization

### Measure productivity

Tool acceptance rates and code metrics help you:

* Understand developer satisfaction with Claude Code suggestions
* Track code generation effectiveness
* Identify opportunities for training or process improvements

## Related resources

* [Monitoring usage with OpenTelemetry](/en/monitoring-usage) for custom metrics and alerting
* [Identity and access management](/en/iam) for role configuration


# Manage costs effectively
Source: https://code.claude.com/docs/en/costs

Learn how to track and optimize token usage and costs when using Claude Code.

Claude Code consumes tokens for each interaction. The average cost is \$6 per developer per day, with daily costs remaining below \$12 for 90% of users.

For team usage, Claude Code charges by API token consumption. On average, Claude Code costs \~\$100-200/developer per month with Sonnet 4.5 though there is large variance depending on how many instances users are running and whether they're using it in automation.

## Track your costs

### Using the `/cost` command

<Note>
  The `/cost` command is not intended for Claude Max and Pro subscribers.
</Note>

The `/cost` command provides detailed token usage statistics for your current session:

```
Total cost:            $0.55
Total duration (API):  6m 19.7s
Total duration (wall): 6h 33m 10.2s
Total code changes:    0 lines added, 0 lines removed
```

### Additional tracking options

Check [historical usage](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-console) in the Claude Console (requires Admin or Billing role) and set [workspace spend limits](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces) for the Claude Code workspace (requires Admin role).

<Note>
  When you first authenticate Claude Code with your Claude Console account, a workspace called "Claude Code" is automatically created for you. This workspace provides centralized cost tracking and management for all Claude Code usage in your organization. You cannot create API keys for this workspace - it is exclusively for Claude Code authentication and usage.
</Note>

## Managing costs for teams

When using Claude API, you can limit the total Claude Code workspace spend. To configure, [follow these instructions](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces). Admins can view cost and usage reporting by [following these instructions](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-console).

On Bedrock and Vertex, Claude Code does not send metrics from your cloud. In order to get cost metrics, several large enterprises reported using [LiteLLM](/en/third-party-integrations#litellm), which is an open-source tool that helps companies [track spend by key](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend). This project is unaffiliated with Anthropic and we have not audited its security.

### Rate limit recommendations

When setting up Claude Code for teams, consider these Token Per Minute (TPM) and Request Per Minute (RPM) per-user recommendations based on your organization size:

| Team size     | TPM per user | RPM per user |
| ------------- | ------------ | ------------ |
| 1-5 users     | 200k-300k    | 5-7          |
| 5-20 users    | 100k-150k    | 2.5-3.5      |
| 20-50 users   | 50k-75k      | 1.25-1.75    |
| 50-100 users  | 25k-35k      | 0.62-0.87    |
| 100-500 users | 15k-20k      | 0.37-0.47    |
| 500+ users    | 10k-15k      | 0.25-0.35    |

For example, if you have 200 users, you might request 20k TPM for each user, or 4 million total TPM (200\*20,000 = 4 million).

The TPM per user decreases as team size grows because we expect fewer users to use Claude Code concurrently in larger organizations. These rate limits apply at the organization level, not per individual user, which means individual users can temporarily consume more than their calculated share when others aren't actively using the service.

<Note>
  If you anticipate scenarios with unusually high concurrent usage (such as live training sessions with large groups), you may need higher TPM allocations per user.
</Note>

## Reduce token usage

* **Compact conversations:**

  * Claude uses auto-compact by default when context exceeds 95% capacity
  * Toggle auto-compact: Run `/config` and navigate to "Auto-compact enabled"
  * Use `/compact` manually when context gets large
  * Add custom instructions: `/compact Focus on code samples and API usage`
  * Customize compaction by adding to CLAUDE.md:

    ```markdown  theme={null}
    # Summary instructions

    When you are using compact, please focus on test output and code changes
    ```

* **Write specific queries:** Avoid vague requests that trigger unnecessary scanning

* **Break down complex tasks:** Split large tasks into focused interactions

* **Clear history between tasks:** Use `/clear` to reset context

Costs can vary significantly based on:

* Size of codebase being analyzed
* Complexity of queries
* Number of files being searched or modified
* Length of conversation history
* Frequency of compacting conversations

## Background token usage

Claude Code uses tokens for some background functionality even when idle:

* **Conversation summarization**: Background jobs that summarize previous conversations for the `claude --resume` feature
* **Command processing**: Some commands like `/cost` may generate requests to check status

These background processes consume a small amount of tokens (typically under \$0.04 per session) even without active interaction.

## Tracking version changes and updates

### Current version information

To check your current Claude Code version and installation details:

```bash  theme={null}
claude doctor
```

This command shows your version, installation type, and system information.

### Understanding changes in Claude Code behavior

Claude Code regularly receives updates that may change how features work, including cost reporting:

* **Version tracking**: Use `claude doctor` to see your current version
* **Behavior changes**: Features like `/cost` may display information differently across versions
* **Documentation access**: Claude always has access to the latest documentation, which can help explain current feature behavior

### When cost reporting changes

If you notice changes in how costs are displayed (such as the `/cost` command showing different information):

1. **Verify your version**: Run `claude doctor` to confirm your current version
2. **Consult documentation**: Ask Claude directly about current feature behavior, as it has access to up-to-date documentation
3. **Contact support**: For specific billing questions, contact Anthropic support through your Console account

<Note>
  For team deployments, we recommend starting with a small pilot group to
  establish usage patterns before wider rollout.
</Note>


# Data usage
Source: https://code.claude.com/docs/en/data-usage

Learn about Anthropic's data usage policies for Claude

## Data policies

### Data training policy

**Consumer users (Free, Pro, and Max plans)**:
Starting August 28, 2025, we're giving you the choice to allow your data to be used to improve future Claude models.

We will train new models using data from Free, Pro, and Max accounts when this setting is on (including when you use Claude Code from these accounts).

* If you're a current user, you can select your preference now and your selection will immediately go into effect.
  This setting will only apply to new or resumed chats and coding sessions on Claude. Previous chats with no additional activity will not be used for model training.
* You have until October 8, 2025 to make your selection.
  If you're a new user, you can pick your setting for model training during the signup process.
  You can change your selection at any time in your Privacy Settings.

**Commercial users**: (Team and Enterprise plans, API, 3rd-party platforms, and Claude Gov) maintain existing policies: Anthropic does not train generative models using code or prompts sent to Claude Code under commercial terms, unless the customer has chosen to provide their data to us for model improvement (e.g. [Developer Partner Program](https://support.claude.com/en/articles/11174108-about-the-development-partner-program)).

### Development Partner Program

If you explicitly opt in to methods to provide us with materials to train on, such as via the [Development Partner Program](https://support.claude.com/en/articles/11174108-about-the-development-partner-program), we may use those materials provided to train our models. An organization admin can expressly opt-in to the Development Partner Program for their organization. Note that this program is available only for Anthropic first-party API, and not for Bedrock or Vertex users.

### Feedback using the `/bug` command

If you choose to send us feedback about Claude Code using the `/bug` command, we may use your feedback to improve our products and services. Transcripts shared via `/bug` are retained for 5 years.

### Session quality surveys

When you see the "How is Claude doing this session?" prompt in Claude Code, responding to this survey (including selecting "Dismiss"), only your numeric rating (1, 2, 3, or dismiss) is recorded. We do not collect or store any conversation transcripts, inputs, outputs, or other session data as part of this survey. Unlike thumbs up/down feedback or `/bug` reports, this session quality survey is a simple product satisfaction metric. Your responses to this survey do not impact your data training preferences and cannot be used to train our AI models.

### Data retention

Anthropic retains Claude Code data based on your account type and preferences.

**Consumer users (Free, Pro, and Max plans)**:

* Users who allow data use for model improvement: 5-year retention period to support model development and safety improvements
* Users who don't allow data use for model improvement: 30-day retention period
* Privacy settings can be changed at any time at [claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls).

**Commercial users (Team, Enterprise, and API)**:

* Standard: 30-day retention period
* Zero data retention: Available with appropriately configured API keys - Claude Code will not retain chat transcripts on servers
* Local caching: Claude Code clients may store sessions locally for up to 30 days to enable session resumption (configurable)

Learn more about data retention practices in our [Privacy Center](https://privacy.anthropic.com/).

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) (for Team, Enterprise, and API users) or [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (for Free, Pro, and Max users) and [Privacy Policy](https://www.anthropic.com/legal/privacy).

## Data flow and dependencies

<img src="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=4672f138596e864633b4b7c7ae4ae812" alt="Claude Code data flow diagram" data-og-width="1597" width="1597" data-og-height="1285" height="1285" data-path="images/claude-code-data-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=280&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=5d9bdaf7ea50fc38dc01bbde7b952835 280w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=560&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=525736e5860ac9f262de4b40c9c68a0e 560w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=840&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=5262f9d1a1d0cffb0d5944e49b2d72be 840w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=1100&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=ec74e6b2f87b667f6d0e2278c20944de 1100w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=1650&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=05f11b1d061b6ddbb69969d4e535547a 1650w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=2500&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=9b9cce0fb5989bd1d27f143825be73ff 2500w" />

Claude Code is installed from [NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code). Claude Code runs locally. In order to interact with the LLM, Claude Code sends data over the network. This data includes all user prompts and model outputs. The data is encrypted in transit via TLS and is not encrypted at rest. Claude Code is compatible with most popular VPNs and LLM proxies.

Claude Code is built on Anthropic's APIs. For details regarding our API's security controls, including our API logging procedures, please refer to compliance artifacts offered in the [Anthropic Trust Center](https://trust.anthropic.com).

### Cloud execution

<Note>
  The above data flow diagram and description applies to Claude Code CLI running locally on your machine. For cloud-based sessions using Claude Code on the web, see the section below.
</Note>

When using [Claude Code on the web](/en/claude-code-on-the-web), sessions run in Anthropic-managed virtual machines instead of locally. In cloud environments:

* **Code storage**: Your repository is cloned to an isolated VM and automatically deleted after session completion
* **Credentials**: GitHub authentication is handled through a secure proxy; your GitHub credentials never enter the sandbox
* **Network traffic**: All outbound traffic goes through a security proxy for audit logging and abuse prevention
* **Data retention**: Code and session data are subject to the retention and usage policies for your account type
* **Session data**: Prompts, code changes, and outputs follow the same data policies as local Claude Code usage

For security details about cloud execution, see [Security](/en/security#cloud-execution-security).

## Telemetry services

Claude Code connects from users' machines to the Statsig service to log operational metrics such as latency, reliability, and usage patterns. This logging does not include any code or file paths. Data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Statsig security documentation](https://www.statsig.com/trust/security). To opt out of Statsig telemetry, set the `DISABLE_TELEMETRY` environment variable.

Claude Code connects from users' machines to Sentry for operational error logging. The data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Sentry security documentation](https://sentry.io/security/). To opt out of error logging, set the `DISABLE_ERROR_REPORTING` environment variable.

When users run the `/bug` command, a copy of their full conversation history including code is sent to Anthropic. The data is encrypted in transit and at rest. Optionally, a Github issue is created in our public repository. To opt out of bug reporting, set the `DISABLE_BUG_COMMAND` environment variable.

## Default behaviors by API provider

By default, we disable all non-essential traffic (including error reporting, telemetry, and bug reporting functionality) when using Bedrock or Vertex. You can also opt out of all of these at once by setting the `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` environment variable. Here are the full default behaviors:

| Service                         | Claude API                                               | Vertex API                                            | Bedrock API                                            |
| ------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------ |
| **Statsig (Metrics)**           | Default on.<br />`DISABLE_TELEMETRY=1` to disable.       | Default off.<br />`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.<br />`CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Sentry (Errors)**             | Default on.<br />`DISABLE_ERROR_REPORTING=1` to disable. | Default off.<br />`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.<br />`CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Claude API (`/bug` reports)** | Default on.<br />`DISABLE_BUG_COMMAND=1` to disable.     | Default off.<br />`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.<br />`CLAUDE_CODE_USE_BEDROCK` must be 1. |

All environment variables can be checked into `settings.json` ([read more](/en/settings)).


# Identity and Access Management
Source: https://code.claude.com/docs/en/iam

Learn how to configure user authentication, authorization, and access controls for Claude Code in your organization.

## Authentication methods

Setting up Claude Code requires access to Anthropic models. For teams, you can set up Claude Code access in one of three ways:

* Claude API via the Claude Console
* Amazon Bedrock
* Google Vertex AI

### Claude API authentication

**To set up Claude Code access for your team via Claude API:**

1. Use your existing Claude Console account or create a new Claude Console account
2. You can add users through either method below:
   * Bulk invite users from within the Console (Console -> Settings -> Members -> Invite)
   * [Set up SSO](https://support.claude.com/en/articles/10280258-setting-up-single-sign-on-on-the-api-console)
3. When inviting users, they need one of the following roles:
   * "Claude Code" role means users can only create Claude Code API keys
   * "Developer" role means users can create any kind of API key
4. Each invited user needs to complete these steps:
   * Accept the Console invite
   * [Check system requirements](/en/setup#system-requirements)
   * [Install Claude Code](/en/setup#installation)
   * Login with Console account credentials

### Cloud provider authentication

**To set up Claude Code access for your team via Bedrock or Vertex:**

1. Follow the [Bedrock docs](/en/amazon-bedrock) or [Vertex docs](/en/google-vertex-ai)
2. Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](/en/settings).
3. Users can [install Claude Code](/en/setup#installation)

## Access control and permissions

We support fine-grained permissions so that you're able to specify exactly what the agent is allowed to do (e.g. run tests, run linter) and what it is not allowed to do (e.g. update cloud infrastructure). These permission settings can be checked into version control and distributed to all developers in your organization, as well as customized by individual developers.

### Permission system

Claude Code uses a tiered permission system to balance power and safety:

| Tool Type         | Example              | Approval Required | "Yes, don't ask again" Behavior               |
| :---------------- | :------------------- | :---------------- | :-------------------------------------------- |
| Read-only         | File reads, LS, Grep | No                | N/A                                           |
| Bash Commands     | Shell execution      | Yes               | Permanently per project directory and command |
| File Modification | Edit/write files     | Yes               | Until session end                             |

### Configuring permissions

You can view & manage Claude Code's tool permissions with `/permissions`. This UI lists all permission rules and the settings.json file they are sourced from.

* **Allow** rules will allow Claude Code to use the specified tool without further manual approval.
* **Ask** rules will ask the user for confirmation whenever Claude Code tries to use the specified tool. Ask rules take precedence over allow rules.
* **Deny** rules will prevent Claude Code from using the specified tool. Deny rules take precedence over allow and ask rules.
* **Additional directories** extend Claude's file access to directories beyond the initial working directory.
* **Default mode** controls Claude's permission behavior when encountering new requests.

Permission rules use the format: `Tool` or `Tool(optional-specifier)`

A rule that is just the tool name matches any use of that tool. For example, adding `Bash` to the list of allow rules would allow Claude Code to use the Bash tool without requiring user approval.

#### Permission modes

Claude Code supports several permission modes that can be set as the `defaultMode` in [settings files](/en/settings#settings-files):

| Mode                | Description                                                                  |
| :------------------ | :--------------------------------------------------------------------------- |
| `default`           | Standard behavior - prompts for permission on first use of each tool         |
| `acceptEdits`       | Automatically accepts file edit permissions for the session                  |
| `plan`              | Plan Mode - Claude can analyze but not modify files or execute commands      |
| `bypassPermissions` | Skips all permission prompts (requires safe environment - see warning below) |

#### Working directories

By default, Claude has access to files in the directory where it was launched. You can extend this access:

* **During startup**: Use `--add-dir <path>` CLI argument
* **During session**: Use `/add-dir` slash command
* **Persistent configuration**: Add to `additionalDirectories` in [settings files](/en/settings#settings-files)

Files in additional directories follow the same permission rules as the original working directory - they become readable without prompts, and file editing permissions follow the current permission mode.

#### Tool-specific permission rules

Some tools support more fine-grained permission controls:

**Bash**

* `Bash(npm run build)` Matches the exact Bash command `npm run build`
* `Bash(npm run test:*)` Matches Bash commands starting with `npm run test`
* `Bash(curl http://site.com/:*)` Matches curl commands that start with exactly `curl http://site.com/`

<Tip>
  Claude Code is aware of shell operators (like `&&`) so a prefix match rule like `Bash(safe-cmd:*)` won't give it permission to run the command `safe-cmd && other-cmd`
</Tip>

<Warning>
  Important limitations of Bash permission patterns:

  1. This tool uses **prefix matches**, not regex or glob patterns
  2. The wildcard `:*` only works at the end of a pattern to match any continuation
  3. Patterns like `Bash(curl http://github.com/:*)` can be bypassed in many ways:
     * Options before URL: `curl -X GET http://github.com/...` won't match
     * Different protocol: `curl https://github.com/...` won't match
     * Redirects: `curl -L http://bit.ly/xyz` (redirects to github)
     * Variables: `URL=http://github.com && curl $URL` won't match
     * Extra spaces: `curl  http://github.com` won't match

  For more reliable URL filtering, consider:

  * Using the WebFetch tool with `WebFetch(domain:github.com)` permission
  * Instructing Claude Code about your allowed curl patterns via CLAUDE.md
  * Using hooks for custom permission validation
</Warning>

**Read & Edit**

`Edit` rules apply to all built-in tools that edit files. Claude will make a best-effort attempt to apply `Read` rules to all built-in tools that read files like Grep, Glob, and LS.

Read & Edit rules both follow the [gitignore](https://git-scm.com/docs/gitignore) specification with four distinct pattern types:

| Pattern            | Meaning                                | Example                          | Matches                            |
| ------------------ | -------------------------------------- | -------------------------------- | ---------------------------------- |
| `//path`           | **Absolute** path from filesystem root | `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**`          |
| `~/path`           | Path from **home** directory           | `Read(~/Documents/*.pdf)`        | `/Users/alice/Documents/*.pdf`     |
| `/path`            | Path **relative to settings file**     | `Edit(/src/**/*.ts)`             | `<settings file path>/src/**/*.ts` |
| `path` or `./path` | Path **relative to current directory** | `Read(*.env)`                    | `<cwd>/*.env`                      |

<Warning>
  A pattern like `/Users/alice/file` is NOT an absolute path - it's relative to your settings file! Use `//Users/alice/file` for absolute paths.
</Warning>

* `Edit(/docs/**)` - Edits in `<project>/docs/` (NOT `/docs/`!)
* `Read(~/.zshrc)` - Reads your home directory's `.zshrc`
* `Edit(//tmp/scratch.txt)` - Edits the absolute path `/tmp/scratch.txt`
* `Read(src/**)` - Reads from `<current-directory>/src/`

**WebFetch**

* `WebFetch(domain:example.com)` Matches fetch requests to example.com

**MCP**

* `mcp__puppeteer` Matches any tool provided by the `puppeteer` server (name configured in Claude Code)
* `mcp__puppeteer__puppeteer_navigate` Matches the `puppeteer_navigate` tool provided by the `puppeteer` server

<Warning>
  Unlike other permission types, MCP permissions do NOT support wildcards (`*`).

  To approve all tools from an MCP server:

  * ✅ Use: `mcp__github` (approves ALL GitHub tools)
  * ❌ Don't use: `mcp__github__*` (wildcards are not supported)

  To approve specific tools only, list each one:

  * ✅ Use: `mcp__github__get_issue`
  * ✅ Use: `mcp__github__list_issues`
</Warning>

### Additional permission control with hooks

[Claude Code hooks](/en/hooks-guide) provide a way to register custom shell commands to perform permission evaluation at runtime. When Claude Code makes a tool call, PreToolUse hooks run before the permission system runs, and the hook output can determine whether to approve or deny the tool call in place of the permission system.

### Enterprise managed policy settings

For enterprise deployments of Claude Code, we support enterprise managed policy settings that take precedence over user and project settings. This allows system administrators to enforce security policies that users cannot override.

System administrators can deploy policies to:

* macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
* Linux and WSL: `/etc/claude-code/managed-settings.json`
* Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`

These policy files follow the same format as regular [settings files](/en/settings#settings-files) but cannot be overridden by user or project settings. This ensures consistent security policies across your organization.

### Settings precedence

When multiple settings sources exist, they are applied in the following order (highest to lowest precedence):

1. Enterprise policies
2. Command line arguments
3. Local project settings (`.claude/settings.local.json`)
4. Shared project settings (`.claude/settings.json`)
5. User settings (`~/.claude/settings.json`)

This hierarchy ensures that organizational policies are always enforced while still allowing flexibility at the project and user levels where appropriate.

## Credential management

Claude Code securely manages your authentication credentials:

* **Storage location**: On macOS, API keys, OAuth tokens, and other credentials are stored in the encrypted macOS Keychain.
* **Supported authentication types**: Claude.ai credentials, Claude API credentials, Bedrock Auth, and Vertex Auth.
* **Custom credential scripts**: The [`apiKeyHelper`](/en/settings#available-settings) setting can be configured to run a shell script that returns an API key.
* **Refresh intervals**: By default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.


# Legal and compliance
Source: https://code.claude.com/docs/en/legal-and-compliance

Legal agreements, compliance certifications, and security information for Claude Code.

## Legal agreements

### License

Your use of Claude Code is subject to:

* [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) - for Team, Enterprise, and Claude API users
* [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) - for Free, Pro, and Max users

### Commercial agreements

Whether you're using the Claude API directly (1P) or accessing it through AWS Bedrock or Google Vertex (3P), your existing commercial agreement will apply to Claude Code usage, unless we've mutually agreed otherwise.

## Compliance

### Healthcare compliance (BAA)

If a customer has a Business Associate Agreement (BAA) with us, and wants to use Claude Code, the BAA will automatically extend to cover Claude Code if the customer has executed a BAA and has Zero Data Retention (ZDR) activated. The BAA will be applicable to that customer's API traffic flowing through Claude Code.

## Security and trust

### Trust and safety

You can find more information in the [Anthropic Trust Center](https://trust.anthropic.com) and [Transparency Hub](https://www.anthropic.com/transparency).

### Security vulnerability reporting

Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/anthropic-vdp/reports/new?type=team\&report_type=vulnerability).

***

© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.


# Monitoring
Source: https://code.claude.com/docs/en/monitoring-usage

Learn how to enable and configure OpenTelemetry for Claude Code.

Claude Code supports OpenTelemetry (OTel) metrics and events for monitoring and observability.

All metrics are time series data exported via OpenTelemetry's standard metrics protocol, and events are exported via OpenTelemetry's logs/events protocol. It is the user's responsibility to ensure their metrics and logs backends are properly configured and that the aggregation granularity meets their monitoring requirements.

<Note>
  OpenTelemetry support is currently in beta and details are subject to change.
</Note>

## Quick Start

Configure OpenTelemetry using environment variables:

```bash  theme={null}
# 1. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1

# 2. Choose exporters (both are optional - configure only what you need)
export OTEL_METRICS_EXPORTER=otlp       # Options: otlp, prometheus, console
export OTEL_LOGS_EXPORTER=otlp          # Options: otlp, console

# 3. Configure OTLP endpoint (for OTLP exporter)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# 4. Set authentication (if required)
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"

# 5. For debugging: reduce export intervals
export OTEL_METRIC_EXPORT_INTERVAL=10000  # 10 seconds (default: 60000ms)
export OTEL_LOGS_EXPORT_INTERVAL=5000     # 5 seconds (default: 5000ms)

# 6. Run Claude Code
claude
```

<Note>
  The default export intervals are 60 seconds for metrics and 5 seconds for logs. During setup, you may want to use shorter intervals for debugging purposes. Remember to reset these for production use.
</Note>

For full configuration options, see the [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options).

## Administrator Configuration

Administrators can configure OpenTelemetry settings for all users through the managed settings file. This allows for centralized control of telemetry settings across an organization. See the [settings precedence](/en/settings#settings-precedence) for more information about how settings are applied.

The managed settings file is located at:

* macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
* Linux and WSL: `/etc/claude-code/managed-settings.json`
* Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`

Example managed settings configuration:

```json  theme={null}
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.company.com:4317",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer company-token"
  }
}
```

<Note>
  Managed settings can be distributed via MDM (Mobile Device Management) or other device management solutions. Environment variables defined in the managed settings file have high precedence and cannot be overridden by users.
</Note>

## Configuration Details

### Common Configuration Variables

| Environment Variable                            | Description                                               | Example Values                       |
| ----------------------------------------------- | --------------------------------------------------------- | ------------------------------------ |
| `CLAUDE_CODE_ENABLE_TELEMETRY`                  | Enables telemetry collection (required)                   | `1`                                  |
| `OTEL_METRICS_EXPORTER`                         | Metrics exporter type(s) (comma-separated)                | `console`, `otlp`, `prometheus`      |
| `OTEL_LOGS_EXPORTER`                            | Logs/events exporter type(s) (comma-separated)            | `console`, `otlp`                    |
| `OTEL_EXPORTER_OTLP_PROTOCOL`                   | Protocol for OTLP exporter (all signals)                  | `grpc`, `http/json`, `http/protobuf` |
| `OTEL_EXPORTER_OTLP_ENDPOINT`                   | OTLP collector endpoint (all signals)                     | `http://localhost:4317`              |
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL`           | Protocol for metrics (overrides general)                  | `grpc`, `http/json`, `http/protobuf` |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`           | OTLP metrics endpoint (overrides general)                 | `http://localhost:4318/v1/metrics`   |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL`              | Protocol for logs (overrides general)                     | `grpc`, `http/json`, `http/protobuf` |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`              | OTLP logs endpoint (overrides general)                    | `http://localhost:4318/v1/logs`      |
| `OTEL_EXPORTER_OTLP_HEADERS`                    | Authentication headers for OTLP                           | `Authorization=Bearer token`         |
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY`         | Client key for mTLS authentication                        | Path to client key file              |
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_CERTIFICATE` | Client certificate for mTLS authentication                | Path to client cert file             |
| `OTEL_METRIC_EXPORT_INTERVAL`                   | Export interval in milliseconds (default: 60000)          | `5000`, `60000`                      |
| `OTEL_LOGS_EXPORT_INTERVAL`                     | Logs export interval in milliseconds (default: 5000)      | `1000`, `10000`                      |
| `OTEL_LOG_USER_PROMPTS`                         | Enable logging of user prompt content (default: disabled) | `1` to enable                        |

### Metrics Cardinality Control

The following environment variables control which attributes are included in metrics to manage cardinality:

| Environment Variable                | Description                                     | Default Value | Example to Disable |
| ----------------------------------- | ----------------------------------------------- | ------------- | ------------------ |
| `OTEL_METRICS_INCLUDE_SESSION_ID`   | Include session.id attribute in metrics         | `true`        | `false`            |
| `OTEL_METRICS_INCLUDE_VERSION`      | Include app.version attribute in metrics        | `false`       | `true`             |
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | Include user.account\_uuid attribute in metrics | `true`        | `false`            |

These variables help control the cardinality of metrics, which affects storage requirements and query performance in your metrics backend. Lower cardinality generally means better performance and lower storage costs but less granular data for analysis.

### Dynamic Headers

For enterprise environments that require dynamic authentication, you can configure a script to generate headers dynamically:

#### Settings Configuration

Add to your `.claude/settings.json`:

```json  theme={null}
{
  "otelHeadersHelper": "/bin/generate_opentelemetry_headers.sh"
}
```

#### Script Requirements

The script must output valid JSON with string key-value pairs representing HTTP headers:

```bash  theme={null}
#!/bin/bash
# Example: Multiple headers
echo "{\"Authorization\": \"Bearer $(get-token.sh)\", \"X-API-Key\": \"$(get-api-key.sh)\"}"
```

#### Important Limitations

**Headers are fetched only at startup, not during runtime.** This is due to OpenTelemetry exporter architecture limitations.

For scenarios requiring frequent token refresh, use an OpenTelemetry Collector as a proxy that can refresh its own headers.

### Multi-Team Organization Support

Organizations with multiple teams or departments can add custom attributes to distinguish between different groups using the `OTEL_RESOURCE_ATTRIBUTES` environment variable:

```bash  theme={null}
# Add custom attributes for team identification
export OTEL_RESOURCE_ATTRIBUTES="department=engineering,team.id=platform,cost_center=eng-123"
```

These custom attributes will be included in all metrics and events, allowing you to:

* Filter metrics by team or department
* Track costs per cost center
* Create team-specific dashboards
* Set up alerts for specific teams

<Warning>
  **Important formatting requirements for OTEL\_RESOURCE\_ATTRIBUTES:**

  The `OTEL_RESOURCE_ATTRIBUTES` environment variable follows the [W3C Baggage specification](https://www.w3.org/TR/baggage/), which has strict formatting requirements:

  * **No spaces allowed**: Values cannot contain spaces. For example, `user.organizationName=My Company` is invalid
  * **Format**: Must be comma-separated key=value pairs: `key1=value1,key2=value2`
  * **Allowed characters**: Only US-ASCII characters excluding control characters, whitespace, double quotes, commas, semicolons, and backslashes
  * **Special characters**: Characters outside the allowed range must be percent-encoded

  **Examples:**

  ```bash  theme={null}
  # ❌ Invalid - contains spaces
  export OTEL_RESOURCE_ATTRIBUTES="org.name=John's Organization"

  # ✅ Valid - use underscores or camelCase instead
  export OTEL_RESOURCE_ATTRIBUTES="org.name=Johns_Organization"
  export OTEL_RESOURCE_ATTRIBUTES="org.name=JohnsOrganization"

  # ✅ Valid - percent-encode special characters if needed
  export OTEL_RESOURCE_ATTRIBUTES="org.name=John%27s%20Organization"
  ```

  Note: Quoting the entire key=value pair (e.g., `"key=value with spaces"`) is not supported by the OpenTelemetry specification and will result in attributes being prefixed with quotes.
</Warning>

### Example Configurations

```bash  theme={null}
# Console debugging (1-second intervals)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console
export OTEL_METRIC_EXPORT_INTERVAL=1000

# OTLP/gRPC
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Prometheus
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=prometheus

# Multiple exporters
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console,otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/json

# Different endpoints/backends for metrics and logs
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_METRICS_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://metrics.company.com:4318
export OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://logs.company.com:4317

# Metrics only (no events/logs)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Events/logs only (no metrics)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

## Available Metrics and Events

### Standard Attributes

All metrics and events share these standard attributes:

| Attribute           | Description                                                   | Controlled By                                       |
| ------------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| `session.id`        | Unique session identifier                                     | `OTEL_METRICS_INCLUDE_SESSION_ID` (default: true)   |
| `app.version`       | Current Claude Code version                                   | `OTEL_METRICS_INCLUDE_VERSION` (default: false)     |
| `organization.id`   | Organization UUID (when authenticated)                        | Always included when available                      |
| `user.account_uuid` | Account UUID (when authenticated)                             | `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default: true) |
| `terminal.type`     | Terminal type (e.g., `iTerm.app`, `vscode`, `cursor`, `tmux`) | Always included when detected                       |

### Metrics

Claude Code exports the following metrics:

| Metric Name                           | Description                                     | Unit   |
| ------------------------------------- | ----------------------------------------------- | ------ |
| `claude_code.session.count`           | Count of CLI sessions started                   | count  |
| `claude_code.lines_of_code.count`     | Count of lines of code modified                 | count  |
| `claude_code.pull_request.count`      | Number of pull requests created                 | count  |
| `claude_code.commit.count`            | Number of git commits created                   | count  |
| `claude_code.cost.usage`              | Cost of the Claude Code session                 | USD    |
| `claude_code.token.usage`             | Number of tokens used                           | tokens |
| `claude_code.code_edit_tool.decision` | Count of code editing tool permission decisions | count  |
| `claude_code.active_time.total`       | Total active time in seconds                    | s      |

### Metric Details

#### Session Counter

Incremented at the start of each session.

**Attributes**:

* All [standard attributes](#standard-attributes)

#### Lines of Code Counter

Incremented when code is added or removed.

**Attributes**:

* All [standard attributes](#standard-attributes)
* `type`: (`"added"`, `"removed"`)

#### Pull Request Counter

Incremented when creating pull requests via Claude Code.

**Attributes**:

* All [standard attributes](#standard-attributes)

#### Commit Counter

Incremented when creating git commits via Claude Code.

**Attributes**:

* All [standard attributes](#standard-attributes)

#### Cost Counter

Incremented after each API request.

**Attributes**:

* All [standard attributes](#standard-attributes)
* `model`: Model identifier (e.g., "claude-sonnet-4-5-20250929")

#### Token Counter

Incremented after each API request.

**Attributes**:

* All [standard attributes](#standard-attributes)
* `type`: (`"input"`, `"output"`, `"cacheRead"`, `"cacheCreation"`)
* `model`: Model identifier (e.g., "claude-sonnet-4-5-20250929")

#### Code Edit Tool Decision Counter

Incremented when user accepts or rejects Edit, Write, or NotebookEdit tool usage.

**Attributes**:

* All [standard attributes](#standard-attributes)
* `tool`: Tool name (`"Edit"`, `"Write"`, `"NotebookEdit"`)
* `decision`: User decision (`"accept"`, `"reject"`)
* `language`: Programming language of the edited file (e.g., `"TypeScript"`, `"Python"`, `"JavaScript"`, `"Markdown"`). Returns `"unknown"` for unrecognized file extensions.

#### Active Time Counter

Tracks actual time spent actively using Claude Code (not idle time). This metric is incremented during user interactions such as typing prompts or receiving responses.

**Attributes**:

* All [standard attributes](#standard-attributes)

### Events

Claude Code exports the following events via OpenTelemetry logs/events (when `OTEL_LOGS_EXPORTER` is configured):

#### User Prompt Event

Logged when a user submits a prompt.

**Event Name**: `claude_code.user_prompt`

**Attributes**:

* All [standard attributes](#standard-attributes)
* `event.name`: `"user_prompt"`
* `event.timestamp`: ISO 8601 timestamp
* `prompt_length`: Length of the prompt
* `prompt`: Prompt content (redacted by default, enable with `OTEL_LOG_USER_PROMPTS=1`)

#### Tool Result Event

Logged when a tool completes execution.

**Event Name**: `claude_code.tool_result`

**Attributes**:

* All [standard attributes](#standard-attributes)
* `event.name`: `"tool_result"`
* `event.timestamp`: ISO 8601 timestamp
* `tool_name`: Name of the tool
* `success`: `"true"` or `"false"`
* `duration_ms`: Execution time in milliseconds
* `error`: Error message (if failed)
* `decision`: Either `"accept"` or `"reject"`
* `source`: Decision source - `"config"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`
* `tool_parameters`: JSON string containing tool-specific parameters (when available)
  * For Bash tool: includes `bash_command`, `full_command`, `timeout`, `description`, `sandbox`

#### API Request Event

Logged for each API request to Claude.

**Event Name**: `claude_code.api_request`

**Attributes**:

* All [standard attributes](#standard-attributes)
* `event.name`: `"api_request"`
* `event.timestamp`: ISO 8601 timestamp
* `model`: Model used (e.g., "claude-sonnet-4-5-20250929")
* `cost_usd`: Estimated cost in USD
* `duration_ms`: Request duration in milliseconds
* `input_tokens`: Number of input tokens
* `output_tokens`: Number of output tokens
* `cache_read_tokens`: Number of tokens read from cache
* `cache_creation_tokens`: Number of tokens used for cache creation

#### API Error Event

Logged when an API request to Claude fails.

**Event Name**: `claude_code.api_error`

**Attributes**:

* All [standard attributes](#standard-attributes)
* `event.name`: `"api_error"`
* `event.timestamp`: ISO 8601 timestamp
* `model`: Model used (e.g., "claude-sonnet-4-5-20250929")
* `error`: Error message
* `status_code`: HTTP status code (if applicable)
* `duration_ms`: Request duration in milliseconds
* `attempt`: Attempt number (for retried requests)

#### Tool Decision Event

Logged when a tool permission decision is made (accept/reject).

**Event Name**: `claude_code.tool_decision`

**Attributes**:

* All [standard attributes](#standard-attributes)
* `event.name`: `"tool_decision"`
* `event.timestamp`: ISO 8601 timestamp
* `tool_name`: Name of the tool (e.g., "Read", "Edit", "Write", "NotebookEdit", etc.)
* `decision`: Either `"accept"` or `"reject"`
* `source`: Decision source - `"config"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`

## Interpreting Metrics and Events Data

The metrics exported by Claude Code provide valuable insights into usage patterns and productivity. Here are some common visualizations and analyses you can create:

### Usage Monitoring

| Metric                                                        | Analysis Opportunity                                      |
| ------------------------------------------------------------- | --------------------------------------------------------- |
| `claude_code.token.usage`                                     | Break down by `type` (input/output), user, team, or model |
| `claude_code.session.count`                                   | Track adoption and engagement over time                   |
| `claude_code.lines_of_code.count`                             | Measure productivity by tracking code additions/removals  |
| `claude_code.commit.count` & `claude_code.pull_request.count` | Understand impact on development workflows                |

### Cost Monitoring

The `claude_code.cost.usage` metric helps with:

* Tracking usage trends across teams or individuals
* Identifying high-usage sessions for optimization

<Note>
  Cost metrics are approximations. For official billing data, refer to your API provider (Claude Console, AWS Bedrock, or Google Cloud Vertex).
</Note>

### Alerting and Segmentation

Common alerts to consider:

* Cost spikes
* Unusual token consumption
* High session volume from specific users

All metrics can be segmented by `user.account_uuid`, `organization.id`, `session.id`, `model`, and `app.version`.

### Event Analysis

The event data provides detailed insights into Claude Code interactions:

**Tool Usage Patterns**: Analyze tool result events to identify:

* Most frequently used tools
* Tool success rates
* Average tool execution times
* Error patterns by tool type

**Performance Monitoring**: Track API request durations and tool execution times to identify performance bottlenecks.

## Backend Considerations

Your choice of metrics and logs backends will determine the types of analyses you can perform:

### For Metrics:

* **Time series databases (e.g., Prometheus)**: Rate calculations, aggregated metrics
* **Columnar stores (e.g., ClickHouse)**: Complex queries, unique user analysis
* **Full-featured observability platforms (e.g., Honeycomb, Datadog)**: Advanced querying, visualization, alerting

### For Events/Logs:

* **Log aggregation systems (e.g., Elasticsearch, Loki)**: Full-text search, log analysis
* **Columnar stores (e.g., ClickHouse)**: Structured event analysis
* **Full-featured observability platforms (e.g., Honeycomb, Datadog)**: Correlation between metrics and events

For organizations requiring Daily/Weekly/Monthly Active User (DAU/WAU/MAU) metrics, consider backends that support efficient unique value queries.

## Service Information

All metrics and events are exported with the following resource attributes:

* `service.name`: `claude-code`
* `service.version`: Current Claude Code version
* `os.type`: Operating system type (e.g., `linux`, `darwin`, `windows`)
* `os.version`: Operating system version string
* `host.arch`: Host architecture (e.g., `amd64`, `arm64`)
* `wsl.version`: WSL version number (only present when running on Windows Subsystem for Linux)
* Meter Name: `com.anthropic.claude_code`

## ROI Measurement Resources

For a comprehensive guide on measuring return on investment for Claude Code, including telemetry setup, cost analysis, productivity metrics, and automated reporting, see the [Claude Code ROI Measurement Guide](https://github.com/anthropics/claude-code-monitoring-guide). This repository provides ready-to-use Docker Compose configurations, Prometheus and OpenTelemetry setups, and templates for generating productivity reports integrated with tools like Linear.

## Security/Privacy Considerations

* Telemetry is opt-in and requires explicit configuration
* Sensitive information like API keys or file contents are never included in metrics or events
* User prompt content is redacted by default - only prompt length is recorded. To enable user prompt logging, set `OTEL_LOG_USER_PROMPTS=1`

## Monitoring Claude Code on Amazon Bedrock

For detailed Claude Code usage monitoring guidance for Amazon Bedrock, see [Claude Code Monitoring Implementation (Bedrock)](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/MONITORING.md).


# Security
Source: https://code.claude.com/docs/en/security

Learn about Claude Code's security safeguards and best practices for safe usage.

## How we approach security

### Security foundation

Your code's security is paramount. Claude Code is built with security at its core, developed according to Anthropic's comprehensive security program. Learn more and access resources (SOC 2 Type 2 report, ISO 27001 certificate, etc.) at [Anthropic Trust Center](https://trust.anthropic.com).

### Permission-based architecture

Claude Code uses strict read-only permissions by default. When additional actions are needed (editing files, running tests, executing commands), Claude Code requests explicit permission. Users control whether to approve actions once or allow them automatically.

We designed Claude Code to be transparent and secure. For example, we require approval for bash commands before executing them, giving you direct control. This approach enables users and organizations to configure permissions directly.

For detailed permission configuration, see [Identity and Access Management](/en/iam).

### Built-in protections

To mitigate risks in agentic systems:

* **Sandboxed bash tool**: [Sandbox](/en/sandboxing) bash commands with filesystem and network isolation, reducing permission prompts while maintaining security. Enable with `/sandbox` to define boundaries where Claude Code can work autonomously
* **Write access restriction**: Claude Code can only write to the folder where it was started and its subfolders—it cannot modify files in parent directories without explicit permission. While Claude Code can read files outside the working directory (useful for accessing system libraries and dependencies), write operations are strictly confined to the project scope, creating a clear security boundary
* **Prompt fatigue mitigation**: Support for allowlisting frequently used safe commands per-user, per-codebase, or per-organization
* **Accept Edits mode**: Batch accept multiple edits while maintaining permission prompts for commands with side effects

### User responsibility

Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval.

## Protect against prompt injection

Prompt injection is a technique where an attacker attempts to override or manipulate an AI assistant's instructions by inserting malicious text. Claude Code includes several safeguards against these attacks:

### Core protections

* **Permission system**: Sensitive operations require explicit approval
* **Context-aware analysis**: Detects potentially harmful instructions by analyzing the full request
* **Input sanitization**: Prevents command injection by processing user inputs
* **Command blocklist**: Blocks risky commands that fetch arbitrary content from the web like `curl` and `wget` by default. When explicitly allowed, be aware of [permission pattern limitations](/en/iam#tool-specific-permission-rules)

### Privacy safeguards

We have implemented several safeguards to protect your data, including:

* Limited retention periods for sensitive information (see the [Privacy Center](https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-my-data) to learn more)
* Restricted access to user session data
* User control over data training preferences. Consumer users can change their [privacy settings](https://claude.ai/settings/privacy) at any time.

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) (for Team, Enterprise, and API users) or [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (for Free, Pro, and Max users) and [Privacy Policy](https://www.anthropic.com/legal/privacy).

### Additional safeguards

* **Network request approval**: Tools that make network requests require user approval by default
* **Isolated context windows**: Web fetch uses a separate context window to avoid injecting potentially malicious prompts
* **Trust verification**: First-time codebase runs and new MCP servers require trust verification
  * Note: Trust verification is disabled when running non-interactively with the `-p` flag
* **Command injection detection**: Suspicious bash commands require manual approval even if previously allowlisted
* **Fail-closed matching**: Unmatched commands default to requiring manual approval
* **Natural language descriptions**: Complex bash commands include explanations for user understanding
* **Secure credential storage**: API keys and tokens are encrypted. See [Credential Management](/en/iam#credential-management)

<Warning>
  **Windows WebDAV security risk**: When running Claude Code on Windows, we recommend against enabling WebDAV or allowing Claude Code to access paths such as `\\*` that may contain WebDAV subdirectories. [WebDAV has been deprecated by Microsoft](https://learn.microsoft.com/en-us/windows/whats-new/deprecated-features#:~:text=The%20Webclient%20\(WebDAV\)%20service%20is%20deprecated) due to security risks. Enabling WebDAV may allow Claude Code to trigger network requests to remote hosts, bypassing the permission system.
</Warning>

**Best practices for working with untrusted content**:

1. Review suggested commands before approval
2. Avoid piping untrusted content directly to Claude
3. Verify proposed changes to critical files
4. Use virtual machines (VMs) to run scripts and make tool calls, especially when interacting with external web services
5. Report suspicious behavior with `/bug`

<Warning>
  While these protections significantly reduce risk, no system is completely
  immune to all attacks. Always maintain good security practices when working
  with any AI tool.
</Warning>

## MCP security

Claude Code allows users to configure Model Context Protocol (MCP) servers. The list of allowed MCP servers is configured in your source code, as part of Claude Code settings engineers check into source control.

We encourage either writing your own MCP servers or using MCP servers from providers that you trust. You are able to configure Claude Code permissions for MCP servers. Anthropic does not manage or audit any MCP servers.

## IDE security

See [here](/en/vs-code#security) for more information on the security of running Claude Code in an IDE.

## Cloud execution security

When using [Claude Code on the web](/en/claude-code-on-the-web), additional security controls are in place:

* **Isolated virtual machines**: Each cloud session runs in an isolated, Anthropic-managed VM
* **Network access controls**: Network access is limited by default and can be configured to be disabled or allow only specific domains
* **Credential protection**: Authentication is handled through a secure proxy that uses a scoped credential inside the sandbox, which is then translated to your actual GitHub authentication token
* **Branch restrictions**: Git push operations are restricted to the current working branch
* **Audit logging**: All operations in cloud environments are logged for compliance and audit purposes
* **Automatic cleanup**: Cloud environments are automatically terminated after session completion

For more details on cloud execution, see [Claude Code on the web](/en/claude-code-on-the-web).

## Security best practices

### Working with sensitive code

* Review all suggested changes before approval
* Use project-specific permission settings for sensitive repositories
* Consider using [devcontainers](/en/devcontainer) for additional isolation
* Regularly audit your permission settings with `/permissions`

### Team security

* Use [enterprise managed policies](/en/iam#enterprise-managed-policy-settings) to enforce organizational standards
* Share approved permission configurations through version control
* Train team members on security best practices
* Monitor Claude Code usage through [OpenTelemetry metrics](/en/monitoring-usage)

### Reporting security issues

If you discover a security vulnerability in Claude Code:

1. Do not disclose it publicly
2. Report it through our [HackerOne program](https://hackerone.com/anthropic-vdp/reports/new?type=team\&report_type=vulnerability)
3. Include detailed reproduction steps
4. Allow time for us to address the issue before public disclosure

## Related resources

* [Sandboxing](/en/sandboxing) - Filesystem and network isolation for bash commands
* [Identity and Access Management](/en/iam) - Configure permissions and access controls
* [Monitoring usage](/en/monitoring-usage) - Track and audit Claude Code activity
* [Development containers](/en/devcontainer) - Secure, isolated environments
* [Anthropic Trust Center](https://trust.anthropic.com) - Security certifications and compliance



---

**Navigation:** [← Previous: Advanced Features](./07-advanced.md) | [Index](./index.md) | [Next: Reference →](./09-reference.md)
