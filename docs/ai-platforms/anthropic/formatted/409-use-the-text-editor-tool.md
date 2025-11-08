---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use the text editor tool

<Tabs>
  <Tab title="Claude 4">
    Provide the text editor tool (named `str_replace_based_edit_tool`) to Claude using the Messages API.

    You can optionally specify a `max_characters` parameter to control truncation when viewing large files.

    >   **📝 Note**
>
> `max_characters` is only compatible with `text_editor_20250728` and later versions of the text editor tool.
```bash
      curl https://api.anthropic.com/v1/messages \
        -H "content-type: application/json" \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -d '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "tools": [
            {
              "type": "text_editor_20250728",
              "name": "str_replace_based_edit_tool",
              "max_characters": 10000
            }
          ],
          "messages": [
            {
              "role": "user",
              "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
            }
          ]
        }'
```
```python
      import anthropic

      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool",
                  "max_characters": 10000
              }
          ],
          messages=[
              {
                  "role": "user", 
                  "content": "There's a syntax error in my primes.py file. Can you help me fix it?"
              }
          ]
      )
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const anthropic = new Anthropic();

      const response = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools: [
          {
            type: "text_editor_20250728",
            name: "str_replace_based_edit_tool",
            max_characters: 10000
          }
        ],
        messages: [
          {
            role: "user",
            content: "There's a syntax error in my primes.py file. Can you help me fix it?"
          }
        ]
      });
```
```java
      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.ToolStrReplaceBasedEditTool20250728;

      public class TextEditorToolExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              ToolStrReplaceBasedEditTool20250728 editorTool = ToolStrReplaceBasedEditTool20250728.builder()
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_SONNET_4_0)
                      .maxTokens(1024)
                      .addTool(editorTool)
                      .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
                      .build();

              Message message = client.messages().create(params);
          }
      }
```
  </Tab>

  <Tab title="Claude Sonnet 3.7">
    Provide the text editor tool (named `str_replace_editor`) to Claude using the Messages API:
```bash
      curl https://api.anthropic.com/v1/messages \
        -H "content-type: application/json" \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -d '{
          "model": "claude-3-7-sonnet-20250219",
          "max_tokens": 1024,
          "tools": [
            {
              "type": "text_editor_20250124",
              "name": "str_replace_editor"
            }
          ],
          "messages": [
            {
              "role": "user",
              "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
            }
          ]
        }'
```
```python
      import anthropic

      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-3-7-sonnet-20250219",
          max_tokens=1024,
          tools=[
              {
                  "type": "text_editor_20250124",
                  "name": "str_replace_editor"
              }
          ],
          messages=[
              {
                  "role": "user", 
                  "content": "There's a syntax error in my primes.py file. Can you help me fix it?"
              }
          ]
      )
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const anthropic = new Anthropic();

      const response = await anthropic.messages.create({
        model: "claude-3-7-sonnet-20250219",
        max_tokens: 1024,
        tools: [
          {
            type: "text_editor_20250124",
            name: "str_replace_editor"
          }
        ],
        messages: [
          {
            role: "user",
            content: "There's a syntax error in my primes.py file. Can you help me fix it?"
          }
        ]
      });
```
```java
      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.ToolTextEditor20250124;

      public class TextEditorToolExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              ToolTextEditor20250124 editorTool = ToolTextEditor20250124.builder()
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_3_7_SONNET_LATEST)
                      .maxTokens(1024)
                      .addTool(editorTool)
                      .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
                      .build();

              Message message = client.messages().create(params);
          }
      }
```
  </Tab>
</Tabs>

The text editor tool can be used in the following way:

<Steps>
  <Step title="Provide Claude with the text editor tool and a user prompt">
    * Include the text editor tool in your API request
    * Provide a user prompt that may require examining or modifying files, such as "Can you fix the syntax error in my code?"
  </Step>

  <Step title="Claude uses the tool to examine files or directories">
    * Claude assesses what it needs to look at and uses the `view` command to examine file contents or list directory contents
    * The API response will contain a `tool_use` content block with the `view` command
  </Step>

  <Step title="Execute the view command and return results">
    * Extract the file or directory path from Claude's tool use request
    * Read the file's contents or list the directory contents
    * If a `max_characters` parameter was specified in the tool configuration, truncate the file contents to that length
    * Return the results to Claude by continuing the conversation with a new `user` message containing a `tool_result` content block
  </Step>

  <Step title="Claude uses the tool to modify files">
    * After examining the file or directory, Claude may use a command such as `str_replace` to make changes or `insert` to add text at a specific line number.
    * If Claude uses the `str_replace` command, Claude constructs a properly formatted tool use request with the old text and new text to replace it with
  </Step>

  <Step title="Execute the edit and return results">
    * Extract the file path, old text, and new text from Claude's tool use request
    * Perform the text replacement in the file
    * Return the results to Claude
  </Step>

  <Step title="Claude provides its analysis and explanation">
    * After examining and possibly editing the files, Claude provides a complete explanation of what it found and what changes it made
  </Step>
</Steps>

### Text editor tool commands

The text editor tool supports several commands for viewing and modifying files:

#### view

The `view` command allows Claude to examine the contents of a file or list the contents of a directory. It can read the entire file or a specific range of lines.

Parameters:

* `command`: Must be "view"
* `path`: The path to the file or directory to view
* `view_range` (optional): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed, and -1 for the end line means read to the end of the file. This parameter only applies when viewing files, not directories.

<Accordion title="Example view commands">
```json
  // Example for viewing a file
  {
    "type": "tool_use",
    "id": "toolu_01A09q90qw90lq917835lq9",
    "name": "str_replace_editor",
    "input": {
      "command": "view",
      "path": "primes.py"
    }
  }

  // Example for viewing a directory
  {
    "type": "tool_use",
    "id": "toolu_02B19r91rw91mr917835mr9",
    "name": "str_replace_editor",
    "input": {
      "command": "view",
      "path": "src/"
    }
  }
```
</Accordion>

#### str\_replace

The `str_replace` command allows Claude to replace a specific string in a file with a new string. This is used for making precise edits.

Parameters:

* `command`: Must be "str\_replace"
* `path`: The path to the file to modify
* `old_str`: The text to replace (must match exactly, including whitespace and indentation)
* `new_str`: The new text to insert in place of the old text

<Accordion title="Example str_replace command">
```json
  {
    "type": "tool_use",
    "id": "toolu_01A09q90qw90lq917835lq9",
    "name": "str_replace_editor",
    "input": {
      "command": "str_replace",
      "path": "primes.py",
      "old_str": "for num in range(2, limit + 1)",
      "new_str": "for num in range(2, limit + 1):"
    }
  }
```
</Accordion>

#### create

The `create` command allows Claude to create a new file with specified content.

Parameters:

* `command`: Must be "create"
* `path`: The path where the new file should be created
* `file_text`: The content to write to the new file

<Accordion title="Example create command">
```json
  {
    "type": "tool_use",
    "id": "toolu_01A09q90qw90lq917835lq9",
    "name": "str_replace_editor",
    "input": {
      "command": "create",
      "path": "test_primes.py",
      "file_text": "import unittest\nimport primes\n\nclass TestPrimes(unittest.TestCase):\n    def test_is_prime(self):\n        self.assertTrue(primes.is_prime(2))\n        self.assertTrue(primes.is_prime(3))\n        self.assertFalse(primes.is_prime(4))\n\nif __name__ == '__main__':\n    unittest.main()"
    }
  }
```
</Accordion>

#### insert

The `insert` command allows Claude to insert text at a specific location in a file.

Parameters:

* `command`: Must be "insert"
* `path`: The path to the file to modify
* `insert_line`: The line number after which to insert the text (0 for beginning of file)
* `new_str`: The text to insert

<Accordion title="Example insert command">
```json
  {
    "type": "tool_use",
    "id": "toolu_01A09q90qw90lq917835lq9",
    "name": "str_replace_editor",
    "input": {
      "command": "insert",
      "path": "primes.py",
      "insert_line": 0,
      "new_str": "\"\"\"Module for working with prime numbers.\n\nThis module provides functions to check if a number is prime\nand to generate a list of prime numbers up to a given limit.\n\"\"\"\n"
    }
  }
```
</Accordion>

#### undo\_edit

The `undo_edit` command allows Claude to revert the last edit made to a file.

>   **📝 Note**
>
> This command is only available in Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)). It is not supported in Claude 4 models using the `text_editor_20250728`.

Parameters:

* `command`: Must be "undo\_edit"
* `path`: The path to the file whose last edit should be undone

<Accordion title="Example undo_edit command">
```json
  {
    "type": "tool_use",
    "id": "toolu_01A09q90qw90lq917835lq9",
    "name": "str_replace_editor",
    "input": {
      "command": "undo_edit",
      "path": "primes.py"
    }
  }
```
</Accordion>

### Example: Fixing a syntax error with the text editor tool

<Tabs>
  <Tab title="Claude 4">
    This example demonstrates how Claude 4 models use the text editor tool to fix a syntax error in a Python file.

    First, your application provides Claude with the text editor tool and a prompt to fix a syntax error:
```bash
      curl https://api.anthropic.com/v1/messages \
        -H "content-type: application/json" \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -d '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "tools": [
            {
              "type": "text_editor_20250728",
              "name": "str_replace_based_edit_tool"
            }
          ],
          "messages": [
            {
              "role": "user",
              "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
            }
          ]
        }'
```
```python
      import anthropic

      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool"
              }
          ],
          messages=[
              {
                  "role": "user", 
                  "content": "There's a syntax error in my primes.py file. Can you help me fix it?"
              }
          ]
      )
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const anthropic = new Anthropic();

      const response = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools: [
          {
            type: "text_editor_20250728",
            name: "str_replace_based_edit_tool"
          }
        ],
        messages: [
          {
            role: "user",
            content: "There's a syntax error in my primes.py file. Can you help me fix it?"
          }
        ]
      });
```
```java
      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.ToolStrReplaceBasedEditTool20250728;

      public class TextEditorToolExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              ToolStrReplaceBasedEditTool20250728 editorTool = ToolStrReplaceBasedEditTool20250728.builder()
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_SONNET_4_0)
                      .maxTokens(1024)
                      .addTool(editorTool)
                      .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
                      .build();

              Message message = client.messages().create(params);
          }
      }
```

    Claude will use the text editor tool first to view the file:
```json
    {
      "id": "msg_01XAbCDeFgHiJkLmNoPQrStU",
      "model": "claude-sonnet-4-5",
      "stop_reason": "tool_use",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
        },
        {
          "type": "tool_use",
          "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
          "name": "str_replace_based_edit_tool",
          "input": {
            "command": "view",
            "path": "primes.py"
          }
        }
      ]
    }
```
    Your application should then read the file and return its contents to Claude:
```bash
      curl https://api.anthropic.com/v1/messages \
        -H "content-type: application/json" \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -d '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "tools": [
            {
              "type": "text_editor_20250728",
              "name": "str_replace_based_edit_tool"
            }
          ],
          "messages": [
            {
              "role": "user",
              "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
            },
            {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I'\''ll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
                      },
                      {
                          "type": "tool_use",
                          "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                          "name": "str_replace_based_edit_tool",
                          "input": {
                              "command": "view",
                              "path": "primes.py"
                          }
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                          "content": "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()"
                      }
                  ]
              }
          ]
        }'
```
```python
      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool"
              }
          ],
          messages=[
              {
                  "role": "user", 
                  "content": "There's a syntax error in my primes.py file. Can you help me fix it?"
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
                      },
                      {
                          "type": "tool_use",
                          "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                          "name": "str_replace_based_edit_tool",
                          "input": {
                              "command": "view",
                              "path": "primes.py"
                          }
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                          "content": "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()"
                      }
                  ]
              }
          ]
      )
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const anthropic = new Anthropic();

      const response = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools: [
          {
            type: "text_editor_20250728",
            name: "str_replace_based_edit_tool"
          }
        ],
        messages: [
          {
            role: "user",
            content: "There's a syntax error in my primes.py file. Can you help me fix it?"
          },
          {
            role: "assistant",
            content: [
                {
                    type: "text",
                    text: "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
                },
                {
                    type: "tool_use",
                    id: "toolu_01AbCdEfGhIjKlMnOpQrStU",
                    name: "str_replace_based_edit_tool",
                    input: {
                        command: "view",
                        path: "primes.py"
                    }
                }
            ]
          },
          {
            role: "user",
            content: [
                {
                    type: "tool_result",
                    tool_use_id: "toolu_01AbCdEfGhIjKlMnOpQrStU",
                    content: "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()"
                }
            ]
          }
        ]
      });
```
```java
      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.ToolStrReplaceBasedEditTool20250728;

      public class TextEditorToolExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              ToolStrReplaceBasedEditTool20250728 editorTool = ToolStrReplaceBasedEditTool20250728.builder()
                  .build();

              MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_SONNET_4_0)
                  .maxTokens(1024)
                  .addTool(editorTool)
                  .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
                  .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
```python

    <Tip>
      **Line numbers**

      In the example above, the `view` tool result includes file contents with line numbers prepended to each line (e.g., "1: def is\_prime(n):"). Line numbers are not required, but they are essential for successfully using the `view_range` parameter to examine specific sections of files and the `insert_line` parameter to add content at precise locations.
    </Tip>

    Claude will identify the syntax error and use the `str_replace` command to fix it:
```json
    {
      "id": "msg_01VwXyZAbCdEfGhIjKlMnO",
      "model": "claude-sonnet-4-5",
      "stop_reason": "tool_use",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
        },
        {
          "type": "tool_use",
          "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
          "name": "str_replace_based_edit_tool",
          "input": {
            "command": "str_replace",
            "path": "primes.py",
            "old_str": "    for num in range(2, limit + 1)",
            "new_str": "    for num in range(2, limit + 1):"
          }
        }
      ]
    }
```
    Your application should then make the edit and return the result:
```python
      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool"
              }
          ],
          messages=[
              # Previous messages...

              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
                      },
                      {
                          "type": "tool_use",
                          "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                          "name": "str_replace_based_edit_tool",
                          "input": {
                              "command": "str_replace",
                              "path": "primes.py",
                              "old_str": "    for num in range(2, limit + 1)",
                              "new_str": "    for num in range(2, limit + 1):"
                          }
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                          "content": "Successfully replaced text at exactly one location."
                      }
                  ]
              }
          ]
      )
```
```typescript
      const response = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools: [
          {
            type: "text_editor_20250728",
            name: "str_replace_based_edit_tool"
          }
        ],
        messages: [
          // Previous messages...
          {
            role: "assistant",
            content: [
              {
                type: "text",
                text: "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
              },
              {
                type: "tool_use",
                id: "toolu_01PqRsTuVwXyZAbCdEfGh",
                name: "str_replace_based_edit_tool",
                input: {
                  command: "str_replace",
                  path: "primes.py",
                  old_str: "    for num in range(2, limit + 1)",
                  new_str: "    for num in range(2, limit + 1):"
                }
              }
            ]
          },
          {
            role: "user",
            content: [
              {
                type: "tool_result",
                tool_use_id: "toolu_01PqRsTuVwXyZAbCdEfGh",
                content: "Successfully replaced text at exactly one location."
              }
            ]
          }
        ]
      });
```
```java
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.ContentBlockParam;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.MessageParam;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.TextBlockParam;
      import com.anthropic.models.messages.ToolResultBlockParam;
      import com.anthropic.models.messages.ToolStrReplaceBasedEditTool20250728;
      import com.anthropic.models.messages.ToolUseBlockParam;

      public class TextEditorConversationExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_SONNET_4_0)
                      .maxTokens(1024)
                      .addTool(ToolStrReplaceBasedEditTool20250728.builder()
                              .build())
                      // Previous messages would go here
                      .addAssistantMessageOfBlockParams(
                              List.of(
                                      ContentBlockParam.ofText(TextBlockParam.builder()
                                              .text("I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you.")
                                              .build()),
                                      ContentBlockParam.ofToolUse(ToolUseBlockParam.builder()
                                              .id("toolu_01PqRsTuVwXyZAbCdEfGh")
                                              .name("str_replace_based_edit_tool")
                                              .input(JsonValue.from(Map.of(
                                                      "command", "str_replace",
                                                      "path", "primes.py",
                                                      "old_str", "    for num in range(2, limit + 1)",
                                                      "new_str", "    for num in range(2, limit + 1):"
                                              )))
                                              .build()
                                      )
                              )
                      )
                      .addUserMessageOfBlockParams(List.of(
                              ContentBlockParam.ofToolResult(ToolResultBlockParam.builder()
                                      .toolUseId("toolu_01PqRsTuVwXyZAbCdEfGh")
                                      .content("Successfully replaced text at exactly one location.")
                                      .build()
                              )
                      ))
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
```

    Finally, Claude will provide a complete explanation of the fix:
````json
    {
      "id": "msg_01IjKlMnOpQrStUvWxYzAb",
      "model": "claude-sonnet-4-5",
      "stop_reason": "end_turn",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I've fixed the syntax error in your primes.py file. The issue was in the `get_primes` function at line 19. There was a missing colon (:) at the end of the for loop line.\n\nHere's what I changed:\n\nFrom:\n```python\nfor num in range(2, limit + 1)\n```\n\nTo:\n```python\nfor num in range(2, limit + 1):\n```\n\nIn Python, a colon is required at the end of statements that start a new code block, such as for loops, if statements, function definitions, etc. Without the colon, Python raises a syntax error because it doesn't know where the code block begins.\n\nYour code should now run correctly. The function will properly generate a list of prime numbers up to the specified limit."
        }
      ]
    }
````
  </Tab>

  <Tab title="Claude Sonnet 3.7">
    This example demonstrates how Claude Sonnet 3.7 uses the text editor tool to fix a syntax error in a Python file.

    First, your application provides Claude with the text editor tool and a prompt to fix a syntax error:
```python
    import anthropic

    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        tools=[
            {
                "type": "text_editor_20250124",
                "name": "str_replace_editor"
            }
        ],
        messages=[
            {
                "role": "user", 
                "content": "There's a syntax error in my primes.py file. Can you help me fix it?"
            }
        ]
    )

    print(response)
```
    >   **📝 Note**
>
> The Claude Sonnet 3.7 examples follow the same format as the Claude 4 examples above, using the same tool calls and responses but with the `text_editor_20250124` tool type and `str_replace_editor` name.
  </Tab>
</Tabs>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
