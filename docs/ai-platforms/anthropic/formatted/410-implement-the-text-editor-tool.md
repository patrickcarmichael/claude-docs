---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implement the text editor tool

The text editor tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

The tool type depends on the model version:

* **Claude 4**: `type: "text_editor_20250728"`
* **Claude Sonnet 3.7**: `type: "text_editor_20250124"`

<Steps>
  <Step title="Initialize your editor implementation">
    Create helper functions to handle file operations like reading, writing, and modifying files. Consider implementing backup functionality to recover from mistakes.
  </Step>

  <Step title="Handle editor tool calls">
    Create a function that processes tool calls from Claude based on the command type:
```python
    def handle_editor_tool(tool_call, model_version):
        input_params = tool_call.input
        command = input_params.get('command', '')
        file_path = input_params.get('path', '')
        
        if command == 'view':
            # Read and return file contents

            pass
        elif command == 'str_replace':
            # Replace text in file

            pass
        elif command == 'create':
            # Create new file

            pass
        elif command == 'insert':
            # Insert text at location

            pass
        elif command == 'undo_edit':
            # Check if it's a Claude 4 model

            if 'str_replace_based_edit_tool' in model_version:
                return {"error": "undo_edit command is not supported in Claude 4"}
            # Restore from backup for Claude 3.7

            pass
```
  </Step>

  <Step title="Implement security measures">
    Add validation and security checks:

    * Validate file paths to prevent directory traversal
    * Create backups before making changes
    * Handle errors gracefully
    * Implement permissions checks
  </Step>

  <Step title="Process Claude's responses">
    Extract and handle tool calls from Claude's responses:
```python
    # Process tool use in Claude's response

    for content in response.content:
        if content.type == "tool_use":
            # Execute the tool based on command

            result = handle_editor_tool(content)
            
            # Return result to Claude

            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }
```
  </Step>
</Steps>

>   **⚠️ Warning**
>
> When implementing the text editor tool, keep in mind:

  1. **Security**: The tool has access to your local filesystem, so implement proper security measures.
  2. **Backup**: Always create backups before allowing edits to important files.
  3. **Validation**: Validate all inputs to prevent unintended changes.
  4. **Unique matching**: Make sure replacements match exactly one location to avoid unintended edits.

### Handle errors

When using the text editor tool, various errors may occur. Here is guidance on how to handle them:

<AccordionGroup>
  <Accordion title="File not found">
    If Claude tries to view or modify a file that doesn't exist, return an appropriate error message in the `tool_result`:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: File not found",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="Multiple matches for replacement">
    If Claude's `str_replace` command matches multiple locations in the file, return an appropriate error message:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Found 3 matches for replacement text. Please provide more context to make a unique match.",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="No matches for replacement">
    If Claude's `str_replace` command doesn't match any text in the file, return an appropriate error message:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: No match found for replacement. Please check your text and try again.",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="Permission errors">
    If there are permission issues with creating, reading, or modifying files, return an appropriate error message:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Permission denied. Cannot write to file.",
          "is_error": true
        }
      ]
    }
```
  </Accordion>
</AccordionGroup>

### Follow implementation best practices

<AccordionGroup>
  <Accordion title="Provide clear context">
    When asking Claude to fix or modify code, be specific about what files need to be examined or what issues need to be addressed. Clear context helps Claude identify the right files and make appropriate changes.

    **Less helpful prompt**: "Can you fix my code?"

    **Better prompt**: "There's a syntax error in my primes.py file that prevents it from running. Can you fix it?"
  </Accordion>

  <Accordion title="Be explicit about file paths">
    Specify file paths clearly when needed, especially if you're working with multiple files or files in different directories.

    **Less helpful prompt**: "Review my helper file"

    **Better prompt**: "Can you check my utils/helpers.py file for any performance issues?"
  </Accordion>

  <Accordion title="Create backups before editing">
    Implement a backup system in your application that creates copies of files before allowing Claude to edit them, especially for important or production code.
```python
    def backup_file(file_path):
        """Create a backup of a file before editing."""
        backup_path = f"{file_path}.backup"
        if os.path.exists(file_path):
            with open(file_path, 'r') as src, open(backup_path, 'w') as dst:
                dst.write(src.read())
```
  </Accordion>

  <Accordion title="Handle unique text replacement carefully">
    The `str_replace` command requires an exact match for the text to be replaced. Your application should ensure that there is exactly one match for the old text or provide appropriate error messages.
```python
    def safe_replace(file_path, old_text, new_text):
        """Replace text only if there's exactly one match."""
        with open(file_path, 'r') as f:
            content = f.read()
        
        count = content.count(old_text)
        if count == 0:
            return "Error: No match found"
        elif count > 1:
            return f"Error: Found {count} matches"
        else:
            new_content = content.replace(old_text, new_text)
            with open(file_path, 'w') as f:
                f.write(new_content)
            return "Successfully replaced text"
```
  </Accordion>

  <Accordion title="Verify changes">
    After Claude makes changes to a file, verify the changes by running tests or checking that the code still works as expected.
```python
    def verify_changes(file_path):
        """Run tests or checks after making changes."""
        try:
            # For Python files, check for syntax errors

            if file_path.endswith('.py'):
                import ast
                with open(file_path, 'r') as f:
                    ast.parse(f.read())
                return "Syntax check passed"
        except Exception as e:
            return f"Verification failed: {str(e)}"
```javascript
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
