---
title: "Cascade Hooks (Beta)"
source: "https://docs.windsurf.com/windsurf/cascade/hooks"
---

# Cascade Hooks (Beta)
Source: https://docs.windsurf.com/windsurf/cascade/hooks



Cascade Hooks enable you to execute custom shell commands at key points during Cascade's workflow. This powerful extensibility feature allows you to log operations, enforce guardrails, run validation checks, or integrate with external systems.

<Warning>
  **Beta Release**: Cascade Hooks are currently in beta and undergoing active development. Features and APIs may change. Please contact [Windsurf Support](https://windsurf.com/support) with feedback or bug reports.
</Warning>

<Note>
  Hooks are designed for power users and enterprise teams who need fine-grained control over Cascade's behavior. They require basic shell scripting knowledge.
</Note>

## What You Can Build

Hooks unlock a wide range of automation and governance capabilities:

* **Logging & Analytics**: Track every file read, code change, or command executed by Cascade for compliance and usage analysis
* **Security Controls**: Block Cascade from accessing sensitive files or running dangerous commands
* **Quality Assurance**: Run linters, formatters, or tests automatically after code modifications
* **Custom Workflows**: Integrate with issue trackers, notification systems, or deployment pipelines
* **Team Standardization**: Enforce coding standards and best practices across your organization

## How Hooks Work

Hooks are shell commands that run automatically when specific Cascade actions occur. Each hook:

1. **Receives context** (details about the action being performed) via JSON as standard input
2. **Executes your script** - Python, Bash, Node.js, or any executable
3. **Returns a result** via exit code and output streams

For **pre-hooks** (executed before an action), your script can **block the action** by exiting with exit code `2`. This makes pre-hooks ideal for implementing security policies or validation checks.

## Configuration

Hooks are configured in JSON files that can be placed at three different levels. Cascade loads and merges hooks from all locations, giving teams flexibility in how they distribute and manage hook configurations.

#### System-Level

System-level hooks are ideal for organization-wide policies enforced on shared development machines. For example, you can use them to enforce security policies, compliance requirements, or mandatory code review workflows.

* **macOS**: `/Library/Application Support/Windsurf/hooks.json`
* **Linux/WSL**: `/etc/windsurf/hooks.json`
* **Windows**: `C:\ProgramData\Windsurf\hooks.json`

#### User-Level

User-level hooks are perfect for personal preferences and optional workflows.

* **Location**: `~/.codeium/windsurf/hooks.json`

#### Workspace-Level

Workspace-level hooks allow teams to version control project-specific policies alongside their code. They may include custom validation rules, project-specific integrations, or team-specific workflows.

* **Location**: `.windsurf/hooks.json` in your workspace root

<Note>
  Hooks from all three locations are **merged together**. If the same hook event is configured in multiple locations, all hooks will execute in order: system → user → workspace.
</Note>

### Basic Structure

Here is an example of the basic structure of the hooks configuration:

```json  theme={null}
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "python3 /path/to/your/script.py",
        "show_output": true
      }
    ],
    "post_write_code": [
      {
        "command": "python3 /path/to/another/script.py",
        "show_output": true
      }
    ]
  }
}
```

### Configuration Options

Each hook accepts the following parameters:

| Parameter           | Type    | Description                                                                                             |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `command`           | string  | The shell command to execute. Can be any valid executable with arguments.                               |
| `show_output`       | boolean | Whether to display the hook's stdout/stderr output on the user-facing Cascade UI. Useful for debugging. |
| `working_directory` | string  | Optional. The directory to execute the command from. Defaults to your workspace root.                   |

## Hook Events

Cascade provides eight hook events that cover the most critical actions in the agent workflow.

### Common Input Structure

All hooks receive a JSON object with the following common fields:

| Field               | Type   | Description                                                        |
| ------------------- | ------ | ------------------------------------------------------------------ |
| `agent_action_name` | string | The hook event name (e.g., "pre\_read\_code", "post\_write\_code") |
| `trajectory_id`     | string | Unique identifier for the overall Cascade conversation             |
| `execution_id`      | string | Unique identifier for the single agent turn                        |
| `timestamp`         | string | ISO 8601 timestamp when the hook was triggered                     |
| `tool_info`         | object | Event-specific information (varies by hook type)                   |

In the following examples, the common fields are omitted for brevity. There are eight major types of hook events:

### pre\_read\_code

Triggered **before** Cascade reads a code file. This may block the action if the hook exits with code 2.

**Use cases**: Restrict file access, log read operations, check permissions

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_read_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py"
  }
}
```

This `file_path` may be a directory path when Cascade reads a directory recursively.

### post\_read\_code

Triggered **after** Cascade successfully reads a code file.

**Use cases**: Log successful reads, track file access patterns

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_read_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py"
  }
}
```

This `file_path` may be a directory path when Cascade reads a directory recursively.

### pre\_write\_code

Triggered **before** Cascade writes or modifies a code file. This may block the action if the hook exits with code 2.

**Use cases**: Prevent modifications to protected files, backup files before changes

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_write_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py",
    "edits": [
      {
        "old_string": "def old_function():\n    pass",
        "new_string": "def new_function():\n    return True"
      }
    ]
  }
}
```

### post\_write\_code

Triggered **after** Cascade writes or modifies a code file.

**Use cases**: Run linters, formatters, or tests; log code changes

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_write_code",
  "tool_info": {
    "file_path": "/Users/yourname/project/file.py",
    "edits": [
      {
        "old_string": "import os",
        "new_string": "import os\nimport sys"
      }
    ]
  }
}
```

### pre\_run\_command

Triggered **before** Cascade executes a terminal command. This may block the action if the hook exits with code 2.

**Use cases**: Block dangerous commands, log all command executions, add safety checks

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_run_command",
  "tool_info": {
    "command_line": "npm install package-name",
    "cwd": "/Users/yourname/project"
  }
}
```

### post\_run\_command

Triggered **after** Cascade executes a terminal command.

**Use cases**: Log command results, trigger follow-up actions

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_run_command",
  "tool_info": {
    "command_line": "npm install package-name",
    "cwd": "/Users/yourname/project"
  }
}
```

### pre\_mcp\_tool\_use

Triggered **before** Cascade invokes an MCP (Model Context Protocol) tool. This may block the action if the hook exits with code 2.

**Use cases**: Log MCP usage, restrict which MCP tools can be used

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "pre_mcp_tool_use",
  "tool_info": {
    "mcp_server_name": "github",
    "mcp_tool_arguments": {
      "owner": "code-owner",
      "repo": "my-cool-repo",
      "title": "Bug report",
      "body": "Description of the bug here"
    },
    "mcp_tool_name": "create_issue"
  }
}
```

### post\_mcp\_tool\_use

Triggered **after** Cascade successfully invokes an MCP tool.

**Use cases**: Log MCP operations, track API usage, see MCP results

**Input JSON**:

```json  theme={null}
{
  "agent_action_name": "post_mcp_tool_use",
  "tool_info": {
    "mcp_result": "...",
    "mcp_server_name": "github",
    "mcp_tool_arguments": {
      "owner": "code-owner",
      "perPage": 1,
      "repo": "my-cool-repo",
      "sha": "main"
    },
    "mcp_tool_name": "list_commits"
  }
}
```

## Exit Codes

Your hook scripts communicate results through exit codes:

| Exit Code | Meaning        | Effect                                                                                               |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| `0`       | Success        | Action proceeds normally                                                                             |
| `2`       | Blocking Error | The Cascade agent will see the error message from stderr. For pre-hooks, this **blocks** the action. |
| Any other | Error          | Action proceeds normally                                                                             |

<Warning>
  Only **pre-hooks** (pre\_read\_code, pre\_write\_code, pre\_run\_command, pre\_mcp\_tool\_use) can block actions using exit code 2. Post-hooks cannot block since the action has already occurred.
</Warning>

Keep in mind that the user can see any hook-generated standard output and standard error in the Cascade UI if `show_output` is true.

## Example Use Cases

### Logging All Cascade Actions

Track every action Cascade takes for auditing purposes.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_read_code": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_write_code": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_run_command": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ],
    "post_mcp_tool_use": [
      {
        "command": "python3 /Users/yourname/hooks/log_input.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`log_input.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()
    
    # Parse the JSON
    try:
        data = json.loads(input_data)
        
        # Write formatted JSON to file
        with open("/Users/yourname/hooks/input.txt", "a") as f:
            f.write('\n' + '='*80 + '\n')
            f.write(json.dumps(data, indent=2, separators=(',', ': ')))
            f.write('\n')
    
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This script appends every hook invocation to a log file, creating an audit trail of all Cascade actions. You may transform the input data or perform custom logic as you see fit.

### Restricting File Access

Prevent Cascade from reading files outside a specific directory.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "pre_read_code": [
      {
        "command": "python3 /Users/yourname/hooks/block_read_access.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`block_read_access.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

ALLOWED_PREFIX = "/Users/yourname/my-project/"

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()

    # Parse the JSON
    try:
        data = json.loads(input_data)

        if data.get("agent_action_name") == "pre_read_code":
            tool_info = data.get("tool_info", {})
            file_path = tool_info.get("file_path", "")
            
            if not file_path.startswith(ALLOWED_PREFIX):
                print(f"Access denied: Cascade is only allowed to read files under {ALLOWED_PREFIX}", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks the action
            
            print(f"Access granted: {file_path}", file=sys.stdout)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

When Cascade attempts to read a file outside the allowed directory, this hook blocks the operation and displays an error message.

### Blocking Dangerous Commands

Prevent Cascade from executing potentially harmful commands.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "pre_run_command": [
      {
        "command": "python3 /Users/yourname/hooks/block_dangerous_commands.py",
        "show_output": true
      }
    ]
  }
}
```

**Script** (`block_dangerous_commands.py`):

```python  theme={null}
#!/usr/bin/env python3

import sys
import json

DANGEROUS_COMMANDS = ["rm -rf", "sudo rm", "format", "del /f"]

def main():
    # Read the JSON data from stdin
    input_data = sys.stdin.read()

    # Parse the JSON
    try:
        data = json.loads(input_data)

        if data.get("agent_action_name") == "pre_run_command":
            tool_info = data.get("tool_info", {})
            command = tool_info.get("command_line", "")

            for dangerous_cmd in DANGEROUS_COMMANDS:
                if dangerous_cmd in command:
                    print(f"Command blocked: '{dangerous_cmd}' is not allowed for safety reasons.", file=sys.stderr)
                    sys.exit(2)  # Exit code 2 blocks the command
            
            print(f"Command approved: {command}", file=sys.stdout)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This hook scans commands for dangerous patterns and blocks them before execution.

### Running Code Formatters After Edits

Automatically format code files after Cascade modifies them.

**Config** (`~/.codeium/windsurf/hooks.json`):

```json  theme={null}
{
  "hooks": {
    "post_write_code": [
      {
        "command": "bash /Users/yourname/hooks/format_code.sh",
        "show_output": false
      }
    ]
  }
}
```

**Script** (`format_code.sh`):

```bash  theme={null}
#!/bin/bash

---

← Previous: [Simultaneous Cascades](./simultaneous-cascades.md) | [Index](./index.md) | Next: [Read JSON from stdin](./read-json-from-stdin.md) →