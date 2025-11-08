---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implement the bash tool

The bash tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

<Steps>
  <Step title="Set up a bash environment">
    Create a persistent bash session that Claude can interact with:
```python
    import subprocess
    import threading
    import queue

    class BashSession:
        def __init__(self):
            self.process = subprocess.Popen(
                ['/bin/bash'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            self.output_queue = queue.Queue()
            self.error_queue = queue.Queue()
            self._start_readers()
```
  </Step>

  <Step title="Handle command execution">
    Create a function to execute commands and capture output:
```python
    def execute_command(self, command):
        # Send command to bash

        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()
        
        # Capture output with timeout

        output = self._read_output(timeout=10)
        return output
```
  </Step>

  <Step title="Process Claude's tool calls">
    Extract and execute commands from Claude's responses:
```python
    for content in response.content:
        if content.type == "tool_use" and content.name == "bash":
            if content.input.get("restart"):
                bash_session.restart()
                result = "Bash session restarted"
            else:
                command = content.input.get("command")
                result = bash_session.execute_command(command)
            
            # Return result to Claude

            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }
```
  </Step>

  <Step title="Implement safety measures">
    Add validation and restrictions:
```python
    def validate_command(command):
        # Block dangerous commands

        dangerous_patterns = ['rm -rf /', 'format', ':(){:|:&};:']
        for pattern in dangerous_patterns:
            if pattern in command:
                return False, f"Command contains dangerous pattern: {pattern}"
        
        # Add more validation as needed

        return True, None
```
  </Step>
</Steps>

### Handle errors

When implementing the bash tool, handle various error scenarios:

<AccordionGroup>
  <Accordion title="Command execution timeout">
    If a command takes too long to execute:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Command timed out after 30 seconds",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="Command not found">
    If a command doesn't exist:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "bash: nonexistentcommand: command not found",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="Permission denied">
    If there are permission issues:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "bash: /root/sensitive-file: Permission denied",
          "is_error": true
        }
      ]
    }
```
  </Accordion>
</AccordionGroup>

### Follow implementation best practices

<AccordionGroup>
  <Accordion title="Use command timeouts">
    Implement timeouts to prevent hanging commands:
```python
    def execute_with_timeout(command, timeout=30):
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return f"Command timed out after {timeout} seconds"
```
  </Accordion>

  <Accordion title="Maintain session state">
    Keep the bash session persistent to maintain environment variables and working directory:
```python
    # Commands run in the same session maintain state

    commands = [
        "cd /tmp",
        "echo 'Hello' > test.txt",
        "cat test.txt"  # This works because we're still in /tmp

    ]
```
  </Accordion>

  <Accordion title="Handle large outputs">
    Truncate very large outputs to prevent token limit issues:
```python
    def truncate_output(output, max_lines=100):
        lines = output.split('\n')
        if len(lines) > max_lines:
            truncated = '\n'.join(lines[:max_lines])
            return f"{truncated}\n\n... Output truncated ({len(lines)} total lines) ..."
        return output
```
  </Accordion>

  <Accordion title="Log all commands">
    Keep an audit trail of executed commands:
```python
    import logging

    def log_command(command, output, user_id):
        logging.info(f"User {user_id} executed: {command}")
        logging.info(f"Output: {output[:200]}...")  # Log first 200 chars

```
  </Accordion>

  <Accordion title="Sanitize outputs">
    Remove sensitive information from command outputs:
```python
    def sanitize_output(output):
        # Remove potential secrets or credentials

        import re
        # Example: Remove AWS credentials

        output = re.sub(r'aws_access_key_id\s*=\s*\S+', 'aws_access_key_id=***', output)
        output = re.sub(r'aws_secret_access_key\s*=\s*\S+', 'aws_secret_access_key=***', output)
        return output
```typescript
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
