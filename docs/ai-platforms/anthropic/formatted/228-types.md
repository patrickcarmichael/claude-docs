---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Types

### `Options`

Configuration object for the `query()` function.

| Property                     | Type                                                                                              | Default                    | Description                                                                                                                                                                                                                                               |
| :--------------------------- | :------------------------------------------------------------------------------------------------ | :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `abortController`            | `AbortController`                                                                                 | `new AbortController()`    | Controller for cancelling operations                                                                                                                                                                                                                      |
| `additionalDirectories`      | `string[]`                                                                                        | `[]`                       | Additional directories Claude can access                                                                                                                                                                                                                  |
| `agents`                     | `Record<string, [`AgentDefinition`](#agentdefinition)>`                                           | `undefined`                | Programmatically define subagents                                                                                                                                                                                                                         |
| `allowedTools`               | `string[]`                                                                                        | All tools                  | List of allowed tool names                                                                                                                                                                                                                                |
| `canUseTool`                 | [`CanUseTool`](#canusetool)                                                                       | `undefined`                | Custom permission function for tool usage                                                                                                                                                                                                                 |
| `continue`                   | `boolean`                                                                                         | `false`                    | Continue the most recent conversation                                                                                                                                                                                                                     |
| `cwd`                        | `string`                                                                                          | `process.cwd()`            | Current working directory                                                                                                                                                                                                                                 |
| `disallowedTools`            | `string[]`                                                                                        | `[]`                       | List of disallowed tool names                                                                                                                                                                                                                             |
| `env`                        | `Dict<string>`                                                                                    | `process.env`              | Environment variables                                                                                                                                                                                                                                     |
| `executable`                 | `'bun' \| 'deno' \| 'node'`                                                                       | Auto-detected              | JavaScript runtime to use                                                                                                                                                                                                                                 |
| `executableArgs`             | `string[]`                                                                                        | `[]`                       | Arguments to pass to the executable                                                                                                                                                                                                                       |
| `extraArgs`                  | `Record<string, string \| null>`                                                                  | `{}`                       | Additional arguments                                                                                                                                                                                                                                      |
| `fallbackModel`              | `string`                                                                                          | `undefined`                | Model to use if primary fails                                                                                                                                                                                                                             |
| `forkSession`                | `boolean`                                                                                         | `false`                    | When resuming with `resume`, fork to a new session ID instead of continuing the original session                                                                                                                                                          |
| `hooks`                      | `Partial<Record<`[`HookEvent`](#hookevent)`, `[`HookCallbackMatcher`](#hookcallbackmatcher)`[]>>` | `{}`                       | Hook callbacks for events                                                                                                                                                                                                                                 |
| `includePartialMessages`     | `boolean`                                                                                         | `false`                    | Include partial message events                                                                                                                                                                                                                            |
| `maxThinkingTokens`          | `number`                                                                                          | `undefined`                | Maximum tokens for thinking process                                                                                                                                                                                                                       |
| `maxTurns`                   | `number`                                                                                          | `undefined`                | Maximum conversation turns                                                                                                                                                                                                                                |
| `mcpServers`                 | `Record<string, [`McpServerConfig`](#mcpserverconfig)>`                                           | `{}`                       | MCP server configurations                                                                                                                                                                                                                                 |
| `model`                      | `string`                                                                                          | Default from CLI           | Claude model to use                                                                                                                                                                                                                                       |
| `pathToClaudeCodeExecutable` | `string`                                                                                          | Auto-detected              | Path to Claude Code executable                                                                                                                                                                                                                            |
| `permissionMode`             | [`PermissionMode`](#permissionmode)                                                               | `'default'`                | Permission mode for the session                                                                                                                                                                                                                           |
| `permissionPromptToolName`   | `string`                                                                                          | `undefined`                | MCP tool name for permission prompts                                                                                                                                                                                                                      |
| `plugins`                    | [`SdkPluginConfig`](#sdkpluginconfig)`[]`                                                         | `[]`                       | Load custom plugins from local paths. See [Plugins](/en/docs/agent-sdk/plugins) for details                                                                                                                                                               |
| `resume`                     | `string`                                                                                          | `undefined`                | Session ID to resume                                                                                                                                                                                                                                      |
| `settingSources`             | [`SettingSource`](#settingsource)`[]`                                                             | `[]` (no settings)         | Control which filesystem settings to load. When omitted, no settings are loaded. **Note:** Must include `'project'` to load CLAUDE.md files                                                                                                               |
| `stderr`                     | `(data: string) => void`                                                                          | `undefined`                | Callback for stderr output                                                                                                                                                                                                                                |
| `strictMcpConfig`            | `boolean`                                                                                         | `false`                    | Enforce strict MCP validation                                                                                                                                                                                                                             |
| `systemPrompt`               | `string \| { type: 'preset'; preset: 'claude_code'; append?: string }`                            | `undefined` (empty prompt) | System prompt configuration. Pass a string for custom prompt, or `{ type: 'preset', preset: 'claude_code' }` to use Claude Code's system prompt. When using the preset object form, add `append` to extend the system prompt with additional instructions |

### `Query`

Interface returned by the `query()` function.
```typescript
interface Query extends AsyncGenerator<SDKMessage, void> {
  interrupt(): Promise<void>;
  setPermissionMode(mode: PermissionMode): Promise<void>;
}
```

#### Methods

| Method                | Description                                                          |
| :-------------------- | :------------------------------------------------------------------- |
| `interrupt()`         | Interrupts the query (only available in streaming input mode)        |
| `setPermissionMode()` | Changes the permission mode (only available in streaming input mode) |

### `AgentDefinition`

Configuration for a subagent defined programmatically.
```typescript
type AgentDefinition = {
  description: string;
  tools?: string[];
  prompt: string;
  model?: 'sonnet' | 'opus' | 'haiku' | 'inherit';
}
```

| Field         | Required | Description                                                    |
| :------------ | :------- | :------------------------------------------------------------- |
| `description` | Yes      | Natural language description of when to use this agent         |
| `tools`       | No       | Array of allowed tool names. If omitted, inherits all tools    |
| `prompt`      | Yes      | The agent's system prompt                                      |
| `model`       | No       | Model override for this agent. If omitted, uses the main model |

### `SettingSource`

Controls which filesystem-based configuration sources the SDK loads settings from.
```typescript
type SettingSource = 'user' | 'project' | 'local';
```

| Value       | Description                                  | Location                      |
| :---------- | :------------------------------------------- | :---------------------------- |
| `'user'`    | Global user settings                         | `~/.claude/settings.json`     |
| `'project'` | Shared project settings (version controlled) | `.claude/settings.json`       |
| `'local'`   | Local project settings (gitignored)          | `.claude/settings.local.json` |

#### Default behavior

When `settingSources` is **omitted** or **undefined**, the SDK does **not** load any filesystem settings. This provides isolation for SDK applications.

#### Why use settingSources?

**Load all filesystem settings (legacy behavior):**
```typescript
// Load all settings like SDK v0.0.x did
const result = query({
  prompt: "Analyze this code",
  options: {
    settingSources: ['user', 'project', 'local']  // Load all settings
  }
});
```

**Load only specific setting sources:**
```typescript
// Load only project settings, ignore user and local
const result = query({
  prompt: "Run CI checks",
  options: {
    settingSources: ['project']  // Only .claude/settings.json
  }
});
```

**Testing and CI environments:**
```typescript
// Ensure consistent behavior in CI by excluding local settings
const result = query({
  prompt: "Run tests",
  options: {
    settingSources: ['project'],  // Only team-shared settings
    permissionMode: 'bypassPermissions'
  }
});
```

**SDK-only applications:**
```typescript
// Define everything programmatically (default behavior)
// No filesystem dependencies - settingSources defaults to []
const result = query({
  prompt: "Review this PR",
  options: {
    // settingSources: [] is the default, no need to specify
    agents: { /* ... */ },
    mcpServers: { /* ... */ },
    allowedTools: ['Read', 'Grep', 'Glob']
  }
});
```

**Loading CLAUDE.md project instructions:**
```typescript
// Load project settings to include CLAUDE.md files
const result = query({
  prompt: "Add a new feature following project conventions",
  options: {
    systemPrompt: {
      type: 'preset',
      preset: 'claude_code'  // Required to use CLAUDE.md
    },
    settingSources: ['project'],  // Loads CLAUDE.md from project directory
    allowedTools: ['Read', 'Write', 'Edit']
  }
});
```

#### Settings precedence

When multiple sources are loaded, settings are merged with this precedence (highest to lowest):

1. Local settings (`.claude/settings.local.json`)
2. Project settings (`.claude/settings.json`)
3. User settings (`~/.claude/settings.json`)

Programmatic options (like `agents`, `allowedTools`) always override filesystem settings.

### `PermissionMode`

```typescript
type PermissionMode =
  | 'default'           // Standard permission behavior
  | 'acceptEdits'       // Auto-accept file edits
  | 'bypassPermissions' // Bypass all permission checks
  | 'plan'              // Planning mode - no execution
```

### `CanUseTool`

Custom permission function type for controlling tool usage.
```typescript
type CanUseTool = (
  toolName: string,
  input: ToolInput,
  options: {
    signal: AbortSignal;
    suggestions?: PermissionUpdate[];
  }
) => Promise<PermissionResult>;
```

### `PermissionResult`

Result of a permission check.
```typescript
type PermissionResult = 
  | {
      behavior: 'allow';
      updatedInput: ToolInput;
      updatedPermissions?: PermissionUpdate[];
    }
  | {
      behavior: 'deny';
      message: string;
      interrupt?: boolean;
    }
```

### `McpServerConfig`

Configuration for MCP servers.
```typescript
type McpServerConfig = 
  | McpStdioServerConfig
  | McpSSEServerConfig
  | McpHttpServerConfig
  | McpSdkServerConfigWithInstance;
```

#### `McpStdioServerConfig`

```typescript
type McpStdioServerConfig = {
  type?: 'stdio';
  command: string;
  args?: string[];
  env?: Record<string, string>;
}
```

#### `McpSSEServerConfig`

```typescript
type McpSSEServerConfig = {
  type: 'sse';
  url: string;
  headers?: Record<string, string>;
}
```

#### `McpHttpServerConfig`

```typescript
type McpHttpServerConfig = {
  type: 'http';
  url: string;
  headers?: Record<string, string>;
}
```

#### `McpSdkServerConfigWithInstance`

```typescript
type McpSdkServerConfigWithInstance = {
  type: 'sdk';
  name: string;
  instance: McpServer;
}
```

### `SdkPluginConfig`

Configuration for loading plugins in the SDK.
```typescript
type SdkPluginConfig = {
  type: 'local';
  path: string;
}
```

| Field  | Type      | Description                                                |
| :----- | :-------- | :--------------------------------------------------------- |
| `type` | `'local'` | Must be `'local'` (only local plugins currently supported) |
| `path` | `string`  | Absolute or relative path to the plugin directory          |

**Example:**
```typescript
plugins: [
  { type: 'local', path: './my-plugin' },
  { type: 'local', path: '/absolute/path/to/plugin' }
]
```

For complete information on creating and using plugins, see [Plugins](/en/docs/agent-sdk/plugins).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
