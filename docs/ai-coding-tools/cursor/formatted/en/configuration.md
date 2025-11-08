---
title: "Configuration"
source: "https://docs.cursor.com/en/cli/reference/configuration"
language: "en"
language_name: "English"
---

# Configuration
Source: https://docs.cursor.com/en/cli/reference/configuration

Agent CLI configuration reference for cli-config.json

Configure the Agent CLI using the `cli-config.json` file.

## File location

<div class="full-width-table">
  | Type    | Platform    | Path                                       |
  | :------ | :---------- | :----------------------------------------- |
  | Global  | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global  | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Project | All         | `<project>/.cursor/cli.json`               |
</div>

<Note>Only permissions can be configured at the project level. All other CLI settings must be set globally.</Note>

Override with environment variables:

* **`CURSOR_CONFIG_DIR`**: custom directory path
* **`XDG_CONFIG_HOME`** (Linux/BSD): uses `$XDG_CONFIG_HOME/cursor/cli-config.json`

## Schema

### Required fields

<div class="full-width-table">
  | Field               | Type      | Description                                                             |
  | :------------------ | :-------- | :---------------------------------------------------------------------- |
  | `version`           | number    | Config schema version (current: `1`)                                    |
  | `editor.vimMode`    | boolean   | Enable Vim keybindings (default: `false`)                               |
  | `permissions.allow` | string\[] | Permitted operations (see [Permissions](/en/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Forbidden operations (see [Permissions](/en/cli/reference/permissions)) |
</div>

### Optional fields

<div class="full-width-table">
  | Field                    | Type    | Description                     |
  | :----------------------- | :------ | :------------------------------ |
  | `model`                  | object  | Selected model configuration    |
  | `hasChangedDefaultModel` | boolean | CLI-managed model override flag |
</div>

## Examples

### Minimal config

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

### Enable Vim mode

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

### Configure permissions

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

See [Permissions](/en/cli/reference/permissions) for available permission types and examples.

## Troubleshooting

**Config errors**: Move the file aside and restart:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Changes don't persist**: Ensure valid JSON and write permissions. Some fields are CLI-managed and may be overwritten.

## Notes

* Pure JSON format (no comments)
* CLI performs self-repair for missing fields
* Corrupted files are backed up as `.bad` and recreated
* Permission entries are exact strings (see [Permissions](/en/cli/reference/permissions) for details)

---

← Previous: [Authentication](./authentication.md) | [Index](./index.md) | Next: [Output format](./output-format.md) →