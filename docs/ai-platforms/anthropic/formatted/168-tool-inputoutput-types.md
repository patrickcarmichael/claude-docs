---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool Input/Output Types

Documentation of input/output schemas for all built-in Claude Code tools. While the Python SDK doesn't export these as types, they represent the structure of tool inputs and outputs in messages.

### Task

**Tool name:** `Task`

**Input:**
```python
{
    "description": str,      # A short (3-5 word) description of the task

    "prompt": str,           # The task for the agent to perform

    "subagent_type": str     # The type of specialized agent to use

}
```

**Output:**
```python
{
    "result": str,                    # Final result from the subagent

    "usage": dict | None,             # Token usage statistics

    "total_cost_usd": float | None,  # Total cost in USD

    "duration_ms": int | None         # Execution duration in milliseconds

}
```

### Bash

**Tool name:** `Bash`

**Input:**
```python
{
    "command": str,                  # The command to execute

    "timeout": int | None,           # Optional timeout in milliseconds (max 600000)

    "description": str | None,       # Clear, concise description (5-10 words)

    "run_in_background": bool | None # Set to true to run in background

}
```

**Output:**
```python
{
    "output": str,              # Combined stdout and stderr output

    "exitCode": int,            # Exit code of the command

    "killed": bool | None,      # Whether command was killed due to timeout

    "shellId": str | None       # Shell ID for background processes

}
```

### Edit

**Tool name:** `Edit`

**Input:**
```python
{
    "file_path": str,           # The absolute path to the file to modify

    "old_string": str,          # The text to replace

    "new_string": str,          # The text to replace it with

    "replace_all": bool | None  # Replace all occurrences (default False)

}
```

**Output:**
```python
{
    "message": str,      # Confirmation message

    "replacements": int, # Number of replacements made

    "file_path": str     # File path that was edited

}
```

### Read

**Tool name:** `Read`

**Input:**
```python
{
    "file_path": str,       # The absolute path to the file to read

    "offset": int | None,   # The line number to start reading from

    "limit": int | None     # The number of lines to read

}
```

**Output (Text files):**
```python
{
    "content": str,         # File contents with line numbers

    "total_lines": int,     # Total number of lines in file

    "lines_returned": int   # Lines actually returned

}
```

**Output (Images):**
```python
{
    "image": str,       # Base64 encoded image data

    "mime_type": str,   # Image MIME type

    "file_size": int    # File size in bytes

}
```

### Write

**Tool name:** `Write`

**Input:**
```python
{
    "file_path": str,  # The absolute path to the file to write

    "content": str     # The content to write to the file

}
```

**Output:**
```python
{
    "message": str,        # Success message

    "bytes_written": int,  # Number of bytes written

    "file_path": str       # File path that was written

}
```

### Glob

**Tool name:** `Glob`

**Input:**
```python
{
    "pattern": str,       # The glob pattern to match files against

    "path": str | None    # The directory to search in (defaults to cwd)

}
```

**Output:**
```python
{
    "matches": list[str],  # Array of matching file paths

    "count": int,          # Number of matches found

    "search_path": str     # Search directory used

}
```

### Grep

**Tool name:** `Grep`

**Input:**
```python
{
    "pattern": str,                    # The regular expression pattern

    "path": str | None,                # File or directory to search in

    "glob": str | None,                # Glob pattern to filter files

    "type": str | None,                # File type to search

    "output_mode": str | None,         # "content", "files_with_matches", or "count"

    "-i": bool | None,                 # Case insensitive search

    "-n": bool | None,                 # Show line numbers

    "-B": int | None,                  # Lines to show before each match

    "-A": int | None,                  # Lines to show after each match

    "-C": int | None,                  # Lines to show before and after

    "head_limit": int | None,          # Limit output to first N lines/entries

    "multiline": bool | None           # Enable multiline mode

}
```

**Output (content mode):**
```python
{
    "matches": [
        {
            "file": str,
            "line_number": int | None,
            "line": str,
            "before_context": list[str] | None,
            "after_context": list[str] | None
        }
    ],
    "total_matches": int
}
```

**Output (files\_with\_matches mode):**
```python
{
    "files": list[str],  # Files containing matches

    "count": int         # Number of files with matches

}
```

### NotebookEdit

**Tool name:** `NotebookEdit`

**Input:**
```python
{
    "notebook_path": str,                     # Absolute path to the Jupyter notebook

    "cell_id": str | None,                    # The ID of the cell to edit

    "new_source": str,                        # The new source for the cell

    "cell_type": "code" | "markdown" | None,  # The type of the cell

    "edit_mode": "replace" | "insert" | "delete" | None  # Edit operation type

}
```

**Output:**
```python
{
    "message": str,                              # Success message

    "edit_type": "replaced" | "inserted" | "deleted",  # Type of edit performed

    "cell_id": str | None,                       # Cell ID that was affected

    "total_cells": int                           # Total cells in notebook after edit

}
```

### WebFetch

**Tool name:** `WebFetch`

**Input:**
```python
{
    "url": str,     # The URL to fetch content from

    "prompt": str   # The prompt to run on the fetched content

}
```

**Output:**
```python
{
    "response": str,           # AI model's response to the prompt

    "url": str,                # URL that was fetched

    "final_url": str | None,   # Final URL after redirects

    "status_code": int | None  # HTTP status code

}
```

### WebSearch

**Tool name:** `WebSearch`

**Input:**
```python
{
    "query": str,                        # The search query to use

    "allowed_domains": list[str] | None, # Only include results from these domains

    "blocked_domains": list[str] | None  # Never include results from these domains

}
```

**Output:**
```python
{
    "results": [
        {
            "title": str,
            "url": str,
            "snippet": str,
            "metadata": dict | None
        }
    ],
    "total_results": int,
    "query": str
}
```

### TodoWrite

**Tool name:** `TodoWrite`

**Input:**
```python
{
    "todos": [
        {
            "content": str,                              # The task description

            "status": "pending" | "in_progress" | "completed",  # Task status

            "activeForm": str                            # Active form of the description

        }
    ]
}
```

**Output:**
```python
{
    "message": str,  # Success message

    "stats": {
        "total": int,
        "pending": int,
        "in_progress": int,
        "completed": int
    }
}
```

### BashOutput

**Tool name:** `BashOutput`

**Input:**
```python
{
    "bash_id": str,       # The ID of the background shell

    "filter": str | None  # Optional regex to filter output lines

}
```

**Output:**
```python
{
    "output": str,                                      # New output since last check

    "status": "running" | "completed" | "failed",       # Current shell status

    "exitCode": int | None                              # Exit code when completed

}
```

### KillBash

**Tool name:** `KillBash`

**Input:**
```python
{
    "shell_id": str  # The ID of the background shell to kill

}
```

**Output:**
```python
{
    "message": str,  # Success message

    "shell_id": str  # ID of the killed shell

}
```

### ExitPlanMode

**Tool name:** `ExitPlanMode`

**Input:**
```python
{
    "plan": str  # The plan to run by the user for approval

}
```

**Output:**
```python
{
    "message": str,          # Confirmation message

    "approved": bool | None  # Whether user approved the plan

}
```

### ListMcpResources

**Tool name:** `ListMcpResources`

**Input:**
```python
{
    "server": str | None  # Optional server name to filter resources by

}
```

**Output:**
```python
{
    "resources": [
        {
            "uri": str,
            "name": str,
            "description": str | None,
            "mimeType": str | None,
            "server": str
        }
    ],
    "total": int
}
```

### ReadMcpResource

**Tool name:** `ReadMcpResource`

**Input:**
```python
{
    "server": str,  # The MCP server name

    "uri": str      # The resource URI to read

}
```

**Output:**
```python
{
    "contents": [
        {
            "uri": str,
            "mimeType": str | None,
            "text": str | None,
            "blob": str | None
        }
    ],
    "server": str
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
