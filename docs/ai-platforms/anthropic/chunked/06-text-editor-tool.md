**Navigation:** [← Previous](./05-how-to-implement-tool-use.md) | [Index](./index.md) | [Next →](./07-citations.md)

---

# Text editor tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/text-editor-tool



Claude can use an Anthropic-defined text editor tool to view and modify text files, helping you debug, fix, and improve your code or other text documents. This allows Claude to directly interact with your files, providing hands-on assistance rather than just suggesting changes.

## Model compatibility

| Model                                                                      | Tool Version           |
| -------------------------------------------------------------------------- | ---------------------- |
| Claude 4.x models                                                          | `text_editor_20250728` |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `text_editor_20250124` |

<Warning>
  The `text_editor_20250728` tool for Claude 4 models does not include the `undo_edit` command. If you require this functionality, you'll need to use Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)).
</Warning>

<Warning>
  Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## When to use the text editor tool

Some examples of when to use the text editor tool are:

* **Code debugging**: Have Claude identify and fix bugs in your code, from syntax errors to logic issues.
* **Code refactoring**: Let Claude improve your code structure, readability, and performance through targeted edits.
* **Documentation generation**: Ask Claude to add docstrings, comments, or README files to your codebase.
* **Test creation**: Have Claude create unit tests for your code based on its understanding of the implementation.

## Use the text editor tool

<Tabs>
  <Tab title="Claude 4">
    Provide the text editor tool (named `str_replace_based_edit_tool`) to Claude using the Messages API.

    You can optionally specify a `max_characters` parameter to control truncation when viewing large files.

    <Note>
      `max_characters` is only compatible with `text_editor_20250728` and later versions of the text editor tool.
    </Note>

    <CodeGroup>
      ```bash Shell theme={null}
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

      ```python Python theme={null}
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

      ```typescript TypeScript theme={null}
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

      ```java Java theme={null}
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
    </CodeGroup>
  </Tab>

  <Tab title="Claude Sonnet 3.7">
    Provide the text editor tool (named `str_replace_editor`) to Claude using the Messages API:

    <CodeGroup>
      ```bash Shell theme={null}
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

      ```python Python theme={null}
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

      ```typescript TypeScript theme={null}
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

      ```java Java theme={null}
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
    </CodeGroup>
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
  ```json  theme={null}
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
  ```json  theme={null}
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
  ```json  theme={null}
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
  ```json  theme={null}
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

<Note>
  This command is only available in Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)). It is not supported in Claude 4 models using the `text_editor_20250728`.
</Note>

Parameters:

* `command`: Must be "undo\_edit"
* `path`: The path to the file whose last edit should be undone

<Accordion title="Example undo_edit command">
  ```json  theme={null}
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

    <CodeGroup>
      ```bash Shell theme={null}
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

      ```python Python theme={null}
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

      ```typescript TypeScript theme={null}
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

      ```java Java theme={null}
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
    </CodeGroup>

    Claude will use the text editor tool first to view the file:

    ```json  theme={null}
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

    <CodeGroup>
      ```bash Shell theme={null}
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

      ```python Python theme={null}
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

      ```typescript TypeScript theme={null}
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

      ```java Java theme={null}
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
      ```
    </CodeGroup>

    <Tip>
      **Line numbers**

      In the example above, the `view` tool result includes file contents with line numbers prepended to each line (e.g., "1: def is\_prime(n):"). Line numbers are not required, but they are essential for successfully using the `view_range` parameter to examine specific sections of files and the `insert_line` parameter to add content at precise locations.
    </Tip>

    Claude will identify the syntax error and use the `str_replace` command to fix it:

    ```json  theme={null}
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

    <CodeGroup>
      ```python Python theme={null}
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

      ```typescript TypeScript theme={null}
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

      ```java Java theme={null}
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
    </CodeGroup>

    Finally, Claude will provide a complete explanation of the fix:

    ````json  theme={null}
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

    ```python  theme={null}
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

    <Note>
      The Claude Sonnet 3.7 examples follow the same format as the Claude 4 examples above, using the same tool calls and responses but with the `text_editor_20250124` tool type and `str_replace_editor` name.
    </Note>
  </Tab>
</Tabs>

***

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

    ```python  theme={null}
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

    ```python  theme={null}
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

<Warning>
  When implementing the text editor tool, keep in mind:

  1. **Security**: The tool has access to your local filesystem, so implement proper security measures.
  2. **Backup**: Always create backups before allowing edits to important files.
  3. **Validation**: Validate all inputs to prevent unintended changes.
  4. **Unique matching**: Make sure replacements match exactly one location to avoid unintended edits.
</Warning>

### Handle errors

When using the text editor tool, various errors may occur. Here is guidance on how to handle them:

<AccordionGroup>
  <Accordion title="File not found">
    If Claude tries to view or modify a file that doesn't exist, return an appropriate error message in the `tool_result`:

    ```json  theme={null}
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

    ```json  theme={null}
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

    ```json  theme={null}
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

    ```json  theme={null}
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

    ```python  theme={null}
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

    ```python  theme={null}
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

    ```python  theme={null}
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
    ```
  </Accordion>
</AccordionGroup>

***

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool                                                                                                | Additional input tokens |
| --------------------------------------------------------------------------------------------------- | ----------------------- |
| `text_editor_20250429` (Claude 4.x)                                                                 | 700 tokens              |
| `text_editor_20250124` (Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations))) | 700 tokens              |

For more detailed information about tool pricing, see [Tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing).

## Integrate the text editor tool with other tools

The text editor tool can be used alongside other Claude tools. When combining tools, ensure you:

* Match the tool version with the model you're using
* Account for the additional token usage for all tools included in your request

## Change log

| Date             | Version                | Changes                                                                                                                                                                                                                                                               |
| ---------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| July 28, 2025    | `text_editor_20250728` | Release of an updated text editor Tool that fixes some issues and adds an optional `max_characters` parameter. It is otherwise identical to `text_editor_20250429`.                                                                                                   |
| April 29, 2025   | `text_editor_20250429` | Release of the text editor Tool for Claude 4. This version removes the `undo_edit` command but maintains all other capabilities. The tool name has been updated to reflect its str\_replace-based architecture.                                                       |
| March 13, 2025   | `text_editor_20250124` | Introduction of standalone text editor Tool documentation. This version is optimized for Claude Sonnet 3.7 but has identical capabilities to the previous version.                                                                                                    |
| October 22, 2024 | `text_editor_20241022` | Initial release of the text editor Tool with Claude Sonnet 3.5 ([retired](/en/docs/about-claude/model-deprecations)). Provides capabilities for viewing, creating, and editing files through the `view`, `create`, `str_replace`, `insert`, and `undo_edit` commands. |

## Next steps

Here are some ideas for how to use the text editor tool in more convenient and powerful ways:

* **Integrate with your development workflow**: Build the text editor tool into your development tools or IDE
* **Create a code review system**: Have Claude review your code and make improvements
* **Build a debugging assistant**: Create a system where Claude can help you diagnose and fix issues in your code
* **Implement file format conversion**: Let Claude help you convert files from one format to another
* **Automate documentation**: Set up workflows for Claude to automatically document your code

As you build applications with the text editor tool, we're excited to see how you leverage Claude's capabilities to enhance your development workflow and productivity.

<CardGroup cols={3}>
  <Card title="Tool use overview" icon="screwdriver-wrench" href="/en/docs/agents-and-tools/tool-use/overview">
    Learn how to implement tool workflows for use with Claude.
  </Card>

  {" "}

  <Card title="Token-efficient tool use" icon="bolt-lightning" href="/en/docs/agents-and-tools/tool-use/token-efficient-tool-use">
    Reduce latency and costs when using tools with Claude Sonnet 3.7.
  </Card>

  <Card title="Bash tool" icon="terminal" href="/en/docs/agents-and-tools/tool-use/bash-tool">
    Execute shell commands with Claude.
  </Card>
</CardGroup>


# Token-efficient tool use
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use



Starting with Claude Sonnet 3.7, Claude is capable of calling tools in a token-efficient manner. Requests save an average of 14% in output tokens, up to 70%, which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.

<Info>
  Token-efficient tool use is a beta feature that **only works with Claude 3.7 Sonnet**. To use this beta feature, add the beta header `token-efficient-tools-2025-02-19` to a tool use request. This header has no effect on other Claude models.

  All [Claude 4 models](/en/docs/about-claude/models/overview) support token-efficient tool use by default. No beta header is needed.
</Info>

<Warning>
  Token-efficient tool use does not currently work with [`disable_parallel_tool_use`](/en/docs/agents-and-tools/tool-use/implement-tool-use).
</Warning>

Here's an example of how to use token-efficient tools with the API in Claude Sonnet 3.7:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: token-efficient-tools-2025-02-19" \
    -d '{
      "model": "claude-3-7-sonnet-20250219",
      "max_tokens": 1024,
      "tools": [
        {
          "name": "get_weather",
          "description": "Get the current weather in a given location",
          "input_schema": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Tell me the weather in San Francisco."
        }
      ]
    }' | jq '.usage'
  ```

  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      max_tokens=1024,
      model="claude-3-7-sonnet-20250219",
      tools=[{
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": [
            "location"
          ]
        }
      }],
      messages=[{
        "role": "user",
        "content": "Tell me the weather in San Francisco."
      }],
      betas=["token-efficient-tools-2025-02-19"]
  )

  print(response.usage)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const message = await anthropic.beta.messages.create({
    model: "claude-3-7-sonnet-20250219",
    max_tokens: 1024,
    tools: [{
      name: "get_weather",
      description: "Get the current weather in a given location",
      input_schema: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and state, e.g. San Francisco, CA"
          }
        },
        required: ["location"]
      }
    }],
    messages: [{ 
      role: "user", 
      content: "Tell me the weather in San Francisco." 
    }],
    betas: ["token-efficient-tools-2025-02-19"]
  });

  console.log(message.usage);
  ```

  ```Java Java theme={null}
  import java.util.List;
  import java.util.Map;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaTool;
  import com.anthropic.models.beta.messages.MessageCreateParams;

  import static com.anthropic.models.beta.AnthropicBeta.TOKEN_EFFICIENT_TOOLS_2025_02_19;

  public class TokenEfficientToolsExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          BetaTool.InputSchema schema = BetaTool.InputSchema.builder()
                  .properties(JsonValue.from(Map.of(
                          "location",
                          Map.of(
                                  "type", "string",
                                  "description", "The city and state, e.g. San Francisco, CA"
                          )
                  )))
                  .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model("claude-3-7-sonnet-20250219")
                  .maxTokens(1024)
                  .betas(List.of(TOKEN_EFFICIENT_TOOLS_2025_02_19))
                  .addTool(BetaTool.builder()
                          .name("get_weather")
                          .description("Get the current weather in a given location")
                          .inputSchema(schema)
                          .build())
                  .addUserMessage("Tell me the weather in San Francisco.")
                  .build();

          BetaMessage message = client.beta().messages().create(params);
          System.out.println(message.usage());
      }
  }
  ```
</CodeGroup>

The above request should, on average, use fewer input and output tokens than a normal request. To confirm this, try making the same request but remove `token-efficient-tools-2025-02-19` from the beta headers list.

<Tip>
  To keep the benefits of prompt caching, use the beta header consistently for requests you'd like to cache. If you selectively use it, prompt caching will fail.
</Tip>


# Web fetch tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool



The web fetch tool allows Claude to retrieve full content from specified web pages and PDF documents.

<Note>
  The web fetch tool is currently in beta. To enable it, use the beta header `web-fetch-2025-09-10` in your API requests.

  Please use [this form](https://forms.gle/NhWcgmkcvPCMmPE86) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation.
</Note>

<Warning>
  Enabling the web fetch tool in environments where Claude processes untrusted input alongside sensitive data poses data exfiltration risks. We recommend only using this tool in trusted environments or when handling non-sensitive data.

  To minimize exfiltration risks, Claude is not allowed to dynamically construct URLs. Claude can only fetch URLs that have been explicitly provided by the user or that come from previous web search or web fetch results. However, there is still residual risk that should be carefully considered when using this tool.

  If data exfiltration is a concern, consider:

  * Disabling the web fetch tool entirely
  * Using the `max_uses` parameter to limit the number of requests
  * Using the `allowed_domains` parameter to restrict to known safe domains
</Warning>

## Supported models

Web fetch is available on:

* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)
* Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) (`claude-3-7-sonnet-20250219`)
* Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
* Claude Haiku 3.5 (`claude-3-5-haiku-latest`)
* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)

## How web fetch works

When you add the web fetch tool to your API request:

1. Claude decides when to fetch content based on the prompt and available URLs.
2. The API retrieves the full text content from the specified URL.
3. For PDFs, automatic text extraction is performed.
4. Claude analyzes the fetched content and provides a response with optional citations.

<Note>
  The web fetch tool currently does not support web sites dynamically rendered via Javascript.
</Note>

## How to use web fetch

Provide the web fetch tool in your API request:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: web-fetch-2025-09-10" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "messages": [
              {
                  "role": "user",
                  "content": "Please analyze the content at https://example.com/article"
              }
          ],
          "tools": [{
              "type": "web_fetch_20250910",
              "name": "web_fetch",
              "max_uses": 5
          }]
      }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": "Please analyze the content at https://example.com/article"
          }
      ],
      tools=[{
          "type": "web_fetch_20250910",
          "name": "web_fetch",
          "max_uses": 5
      }],
      extra_headers={
          "anthropic-beta": "web-fetch-2025-09-10"
      }
  )
  print(response)
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    const response = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: "Please analyze the content at https://example.com/article"
        }
      ],
      tools: [{
        type: "web_fetch_20250910",
        name: "web_fetch",
        max_uses: 5
      }],
      headers: {
        "anthropic-beta": "web-fetch-2025-09-10"
      }
    });

    console.log(response);
  }

  main().catch(console.error);
  ```
</CodeGroup>

### Tool definition

The web fetch tool supports the following parameters:

```json JSON theme={null}
{
  "type": "web_fetch_20250910",
  "name": "web_fetch",

  // Optional: Limit the number of fetches per request
  "max_uses": 10,

  // Optional: Only fetch from these domains
  "allowed_domains": ["example.com", "docs.example.com"],

  // Optional: Never fetch from these domains
  "blocked_domains": ["private.example.com"],

  // Optional: Enable citations for fetched content
  "citations": {
    "enabled": true
  },

  // Optional: Maximum content length in tokens
  "max_content_tokens": 100000
}
```

#### Max uses

The `max_uses` parameter limits the number of web fetches performed. If Claude attempts more fetches than allowed, the `web_fetch_tool_result` will be an error with the `max_uses_exceeded` error code. There is currently no default limit.

#### Domain filtering

When using domain filters:

* Domains should not include the HTTP/HTTPS scheme (use `example.com` instead of `https://example.com`)
* Subdomains are automatically included (`example.com` covers `docs.example.com`)
* Subpaths are supported (`example.com/blog`)
* You can use either `allowed_domains` or `blocked_domains`, but not both in the same request.

<Warning>
  Be aware that Unicode characters in domain names can create security vulnerabilities through homograph attacks, where visually similar characters from different scripts can bypass domain filters. For example, `аmazon.com` (using Cyrillic 'а') may appear identical to `amazon.com` but represents a different domain.

  When configuring domain allow/block lists:

  * Use ASCII-only domain names when possible
  * Consider that URL parsers may handle Unicode normalization differently
  * Test your domain filters with potential homograph variations
  * Regularly audit your domain configurations for suspicious Unicode characters
</Warning>

#### Content limits

The `max_content_tokens` parameter limits the amount of content that will be included in the context. If the fetched content exceeds this limit, it will be truncated. This helps control token usage when fetching large documents.

<Note>
  The `max_content_tokens` parameter limit is approximate. The actual number of input tokens used can vary by a small amount.
</Note>

#### Citations

Unlike web search where citations are always enabled, citations are optional for web fetch. Set `"citations": {"enabled": true}` to enable Claude to cite specific passages from fetched documents.

<Note>
  When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing and/or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.
</Note>

### Response

Here's an example response structure:

```json  theme={null}
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to fetch
    {
      "type": "text",
      "text": "I'll fetch the content from the article to analyze it."
    },
    // 2. The fetch request
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01234567890abcdef",
      "name": "web_fetch",
      "input": {
        "url": "https://example.com/article"
      }
    },
    // 3. Fetch results
    {
      "type": "web_fetch_tool_result",
      "tool_use_id": "srvtoolu_01234567890abcdef",
      "content": {
        "type": "web_fetch_result",
        "url": "https://example.com/article",
        "content": {
          "type": "document",
          "source": {
            "type": "text",
            "media_type": "text/plain",
            "data": "Full text content of the article..."
          },
          "title": "Article Title",
          "citations": {"enabled": true}
        },
        "retrieved_at": "2025-08-25T10:30:00Z"
      }
    },
    // 4. Claude's analysis with citations (if enabled)
    {
      "text": "Based on the article, ",
      "type": "text"
    },
    {
      "text": "the main argument presented is that artificial intelligence will transform healthcare",
      "type": "text",
      "citations": [
        {
          "type": "char_location",
          "document_index": 0,
          "document_title": "Article Title",
          "start_char_index": 1234,
          "end_char_index": 1456,
          "cited_text": "Artificial intelligence is poised to revolutionize healthcare delivery..."
        }
      ]
    }
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 25039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_fetch_requests": 1
    }
  },
  "stop_reason": "end_turn"
}
```

#### Fetch results

Fetch results include:

* `url`: The URL that was fetched
* `content`: A document block containing the fetched content
* `retrieved_at`: Timestamp when the content was retrieved

<Note>
  The web fetch tool caches results to improve performance and reduce redundant requests. This means the content returned may not always be the latest version available at the URL. The cache behavior is managed automatically and may change over time to optimize for different content types and usage patterns.
</Note>

For PDF documents, the content will be returned as base64-encoded data:

```json  theme={null}
{
  "type": "web_fetch_tool_result",
  "tool_use_id": "srvtoolu_02",
  "content": {
    "type": "web_fetch_result",
    "url": "https://example.com/paper.pdf",
    "content": {
      "type": "document",
      "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBvYmo..."
      },
      "citations": {"enabled": true}
    },
    "retrieved_at": "2025-08-25T10:30:02Z"
  }
}
```

#### Errors

When the web fetch tool encounters an error, the Claude API returns a 200 (success) response with the error represented in the response body:

```json  theme={null}
{
  "type": "web_fetch_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_fetch_tool_error",
    "error_code": "url_not_accessible"
  }
}
```

These are the possible error codes:

* `invalid_input`: Invalid URL format
* `url_too_long`: URL exceeds maximum length (250 characters)
* `url_not_allowed`: URL blocked by domain filtering rules and model restrictions
* `url_not_accessible`: Failed to fetch content (HTTP error)
* `too_many_requests`: Rate limit exceeded
* `unsupported_content_type`: Content type not supported (only text and PDF)
* `max_uses_exceeded`: Maximum web fetch tool uses exceeded
* `unavailable`: An internal error occurred

## URL validation

For security reasons, the web fetch tool can only fetch URLs that have previously appeared in the conversation context. This includes:

* URLs in user messages
* URLs in client-side tool results
* URLs from previous web search or web fetch results

The tool cannot fetch arbitrary URLs that Claude generates or URLs from container-based server tools (Code Execution, Bash, etc.).

## Combined search and fetch

Web fetch works seamlessly with web search for comprehensive information gathering:

```python  theme={null}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Find recent articles about quantum computing and analyze the most relevant one in detail"
        }
    ],
    tools=[
        {
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 3
        },
        {
            "type": "web_fetch_20250910",
            "name": "web_fetch",
            "max_uses": 5,
            "citations": {"enabled": True}
        }
    ],
    extra_headers={
        "anthropic-beta": "web-fetch-2025-09-10"
    }
)
```

In this workflow, Claude will:

1. Use web search to find relevant articles
2. Select the most promising results
3. Use web fetch to retrieve full content
4. Provide detailed analysis with citations

## Prompt caching

Web fetch works with [prompt caching](/en/docs/build-with-claude/prompt-caching). To enable prompt caching, add `cache_control` breakpoints in your request. Cached fetch results can be reused across conversation turns.

```python  theme={null}
import anthropic

client = anthropic.Anthropic()

# First request with web fetch
messages = [
    {
        "role": "user",
        "content": "Analyze this research paper: https://arxiv.org/abs/2024.12345"
    }
]

response1 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=messages,
    tools=[{
        "type": "web_fetch_20250910",
        "name": "web_fetch"
    }],
    extra_headers={
        "anthropic-beta": "web-fetch-2025-09-10"
    }
)

# Add Claude's response to conversation
messages.append({
    "role": "assistant",
    "content": response1.content
})

# Second request with cache breakpoint
messages.append({
    "role": "user",
    "content": "What methodology does the paper use?",
    "cache_control": {"type": "ephemeral"}
})

response2 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=messages,
    tools=[{
        "type": "web_fetch_20250910",
        "name": "web_fetch"
    }],
    extra_headers={
        "anthropic-beta": "web-fetch-2025-09-10"
    }
)

# The second response benefits from cached fetch results
print(f"Cache read tokens: {response2.usage.get('cache_read_input_tokens', 0)}")
```

## Streaming

With streaming enabled, fetch events are part of the stream with a pause during content retrieval:

```javascript  theme={null}
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to fetch

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_fetch"}}

// Fetch URL streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"url\":\"https://example.com/article\"}"}}

// Pause while fetch executes

// Fetch results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_fetch_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "web_fetch_result", "url": "https://example.com/article", "content": {"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": "Article content..."}}}}}

// Claude's response continues...
```

## Batch requests

You can include the web fetch tool in the [Messages Batches API](/en/docs/build-with-claude/batch-processing). Web fetch tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

## Usage and pricing

Web fetch usage has **no additional charges** beyond standard token costs:

```json  theme={null}
"usage": {
  "input_tokens": 25039,
  "output_tokens": 931,
  "cache_read_input_tokens": 0,
  "cache_creation_input_tokens": 0,
  "server_tool_use": {
    "web_fetch_requests": 1
  }
}
```

The web fetch tool is available on the Claude API at **no additional cost**. You only pay standard token costs for the fetched content that becomes part of your conversation context.

To protect against inadvertently fetching large content that would consume excessive tokens, use the `max_content_tokens` parameter to set appropriate limits based on your use case and budget considerations.

Example token usage for typical content:

* Average web page (10KB): \~2,500 tokens
* Large documentation page (100KB): \~25,000 tokens
* Research paper PDF (500KB): \~125,000 tokens


# Web search tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool



The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. Claude automatically cites sources from search results as part of its answer.

<Note>
  Please reach out through our [feedback form](https://forms.gle/sWjBtsrNEY2oKGuE8) to share your experience with the web search tool.
</Note>

## Supported models

Web search is available on:

* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)
* Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) (`claude-3-7-sonnet-20250219`)
* Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
* Claude Haiku 3.5 (`claude-3-5-haiku-latest`)
* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)

## How web search works

When you add the web search tool to your API request:

1. Claude decides when to search based on the prompt.
2. The API executes the searches and provides Claude with the results. This process may repeat multiple times throughout a single request.
3. At the end of its turn, Claude provides a final response with cited sources.

## How to use web search

<Note>
  Your organization's administrator must enable web search in [Console](https://console.anthropic.com/settings/privacy).
</Note>

Provide the web search tool in your API request:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "messages": [
              {
                  "role": "user",
                  "content": "What's the weather in NYC?"
              }
          ],
          "tools": [{
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 5
          }]
      }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": "What's the weather in NYC?"
          }
      ],
      tools=[{
          "type": "web_search_20250305",
          "name": "web_search",
          "max_uses": 5
      }]
  )
  print(response)
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    const response = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: "What's the weather in NYC?"
        }
      ],
      tools: [{
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 5
      }]
    });

    console.log(response);
  }

  main().catch(console.error);
  ```
</CodeGroup>

### Tool definition

The web search tool supports the following parameters:

```json JSON theme={null}
{
  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    "country": "US",
    "timezone": "America/Los_Angeles"
  }
}
```

#### Max uses

The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` will be an error with the `max_uses_exceeded` error code.

#### Domain filtering

When using domain filters:

* Domains should not include the HTTP/HTTPS scheme (use `example.com` instead of `https://example.com`)
* Subdomains are automatically included (`example.com` covers `docs.example.com`)
* Specific subdomains restrict results to only that subdomain (`docs.example.com` returns only results from that subdomain, not from `example.com` or `api.example.com`)
* Subpaths are supported (`example.com/blog`)
* You can use either `allowed_domains` or `blocked_domains`, but not both in the same request.

<Note>
  Request-level domain restrictions must be compatible with organization-level domain restrictions configured in the Console. Request-level domains can only further restrict domains, not override or expand beyond the organization-level list. If your request includes domains that conflict with organization settings, the API will return a validation error.
</Note>

#### Localization

The `user_location` parameter allows you to localize search results based on a user's location.

* `type`: The type of location (must be `approximate`)
* `city`: The city name
* `region`: The region or state
* `country`: The country
* `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### Response

Here's an example response structure:

```json  theme={null}
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
    {
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    },
    // 2. The search query used
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
      }
    },
    // 3. Search results
    {
      "type": "web_search_tool_result",
      "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "content": [
        {
          "type": "web_search_result",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
          "page_age": "April 30, 2025"
        }
      ]
    },
    {
      "text": "Based on the search results, ",
      "type": "text"
    },
    // 4. Claude's response with citations
    {
      "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
      "type": "text",
      "citations": [
        {
          "type": "web_search_result_location",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
          "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
        }
      ]
    }
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 6039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_search_requests": 1
    }
  },
  "stop_reason": "end_turn"
}
```

#### Search results

Search results include:

* `url`: The URL of the source page
* `title`: The title of the source page
* `page_age`: When the site was last updated
* `encrypted_content`: Encrypted content that must be passed back in multi-turn conversations for citations

#### Citations

Citations are always enabled for web search, and each `web_search_result_location` includes:

* `url`: The URL of the cited source
* `title`: The title of the cited source
* `encrypted_index`: A reference that must be passed back for multi-turn conversations.
* `cited_text`: Up to 150 characters of the cited content

The web search citation fields `cited_text`, `title`, and `url` do not count towards input or output token usage.

<Note>
  When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing and/or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.
</Note>

#### Errors

When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:

```json  theme={null}
{
  "type": "web_search_tool_result",
  "tool_use_id": "servertoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"
  }
}
```

These are the possible error codes:

* `too_many_requests`: Rate limit exceeded
* `invalid_input`: Invalid search query parameter
* `max_uses_exceeded`: Maximum web search tool uses exceeded
* `query_too_long`: Query exceeds maximum length
* `unavailable`: An internal error occurred

#### `pause_turn` stop reason

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation.

## Prompt caching

Web search works with [prompt caching](/en/docs/build-with-claude/prompt-caching). To enable prompt caching, add at least one `cache_control` breakpoint in your request. The system will automatically cache up until the last `web_search_tool_result` block when executing the tool.

For multi-turn conversations, set a `cache_control` breakpoint on or after the last `web_search_tool_result` block to reuse cached content.

For example, to use prompt caching with web search for a multi-turn conversation:

<CodeGroup>
  ```python  theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # First request with web search and cache breakpoint
  messages = [
      {
          "role": "user",
          "content": "What's the current weather in San Francisco today?"
      }
  ]

  response1 = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=messages,
      tools=[{
          "type": "web_search_20250305",
          "name": "web_search",
          "user_location": {
              "type": "approximate",
              "city": "San Francisco",
              "region": "California",
              "country": "US",
              "timezone": "America/Los_Angeles"
          }
      }]
  )

  # Add Claude's response to the conversation
  messages.append({
      "role": "assistant",
      "content": response1.content
  })

  # Second request with cache breakpoint after the search results
  messages.append({
      "role": "user",
      "content": "Should I expect rain later this week?",
      "cache_control": {"type": "ephemeral"}  # Cache up to this point
  })

  response2 = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=messages,
      tools=[{
          "type": "web_search_20250305",
          "name": "web_search",
          "user_location": {
              "type": "approximate",
              "city": "San Francisco",
              "region": "California",
              "country": "US",
              "timezone": "America/Los_Angeles"
          }
      }]
  )
  # The second response will benefit from cached search results
  # while still being able to perform new searches if needed
  print(f"Cache read tokens: {response2.usage.get('cache_read_input_tokens', 0)}")
  ```
</CodeGroup>

## Streaming

With streaming enabled, you'll receive search events as part of the stream. There will be a pause while the search executes:

```javascript  theme={null}
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to search

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}

// Claude's response with citations (omitted in this example)
```

## Batch requests

You can include the web search tool in the [Messages Batches API](/en/docs/build-with-claude/batch-processing). Web search tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

## Usage and pricing

Web search usage is charged in addition to token usage:

```json  theme={null}
"usage": {
  "input_tokens": 105,
  "output_tokens": 6039,
  "cache_read_input_tokens": 7123,
  "cache_creation_input_tokens": 7345,
  "server_tool_use": {
    "web_search_requests": 1
  }
}
```

Web search is available on the Claude API for **\$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.


# Admin API overview
Source: https://docs.claude.com/en/docs/build-with-claude/administration-api



<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>

The [Admin API](/en/api/admin-api) allows you to programmatically manage your organization's resources, including organization members, workspaces, and API keys. This provides programmatic control over administrative tasks that would otherwise require manual configuration in the [Claude Console](https://console.anthropic.com).

<Check>
  **The Admin API requires special access**

  The Admin API requires a special Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Claude Console.
</Check>

## How the Admin API works

When you use the Admin API:

1. You make requests using your Admin API key in the `x-api-key` header
2. The API allows you to manage:
   * Organization members and their roles
   * Organization member invites
   * Workspaces and their members
   * API keys

This is useful for:

* Automating user onboarding/offboarding
* Programmatically managing workspace access
* Monitoring and managing API key usage

## Organization roles and permissions

There are five organization-level roles. See more details [here](https://support.claude.com/en/articles/10186004-api-console-roles-and-permissions).

| Role               | Permissions                                                                |
| ------------------ | -------------------------------------------------------------------------- |
| user               | Can use Workbench                                                          |
| claude\_code\_user | Can use Workbench and [Claude Code](https://code.claude.com/docs/overview) |
| developer          | Can use Workbench and manage API keys                                      |
| billing            | Can use Workbench and manage billing details                               |
| admin              | Can do all of the above, plus manage users                                 |

## Key concepts

### Organization Members

You can list [organization members](/en/api/admin-api/users/get-user), update member roles, and remove members.

<CodeGroup>
  ```bash Shell theme={null}
  # List organization members
  curl "https://api.anthropic.com/v1/organizations/users?limit=10" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

  # Update member role
  curl "https://api.anthropic.com/v1/organizations/users/{user_id}" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
    --data '{"role": "developer"}'

  # Remove member
  curl --request DELETE "https://api.anthropic.com/v1/organizations/users/{user_id}" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
  ```
</CodeGroup>

### Organization Invites

You can invite users to organizations and manage those [invites](/en/api/admin-api/invites/get-invite).

<CodeGroup>
  ```bash Shell theme={null}
  # Create invite
  curl --request POST "https://api.anthropic.com/v1/organizations/invites" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
    --data '{
      "email": "newuser@domain.com",
      "role": "developer"
    }'

  # List invites
  curl "https://api.anthropic.com/v1/organizations/invites?limit=10" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

  # Delete invite
  curl --request DELETE "https://api.anthropic.com/v1/organizations/invites/{invite_id}" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
  ```
</CodeGroup>

### Workspaces

Create and manage [workspaces](/en/api/admin-api/workspaces/get-workspace) ([console](https://console.anthropic.com/settings/workspaces)) to organize your resources:

<CodeGroup>
  ```bash Shell theme={null}
  # Create workspace
  curl --request POST "https://api.anthropic.com/v1/organizations/workspaces" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
    --data '{"name": "Production"}'

  # List workspaces
  curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

  # Archive workspace
  curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/archive" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
  ```
</CodeGroup>

### Workspace Members

Manage [user access to specific workspaces](/en/api/admin-api/workspace_members/get-workspace-member):

<CodeGroup>
  ```bash Shell theme={null}
  # Add member to workspace
  curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
    --data '{
      "user_id": "user_xxx",
      "workspace_role": "workspace_developer"
    }'

  # List workspace members
  curl "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members?limit=10" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

  # Update member role
  curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
    --data '{
      "workspace_role": "workspace_admin"
    }'

  # Remove member from workspace
  curl --request DELETE "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
  ```
</CodeGroup>

### API Keys

Monitor and manage [API keys](/en/api/admin-api/apikeys/get-api-key):

<CodeGroup>
  ```bash Shell theme={null}
  # List API keys
  curl "https://api.anthropic.com/v1/organizations/api_keys?limit=10&status=active&workspace_id=wrkspc_xxx" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

  # Update API key
  curl --request POST "https://api.anthropic.com/v1/organizations/api_keys/{api_key_id}" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
    --data '{
      "status": "inactive",
      "name": "New Key Name"
    }'
  ```
</CodeGroup>

## Accessing organization info

Get information about your organization programmatically with the `/v1/organizations/me` endpoint.

For example:

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/me" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

```json  theme={null}
{
  "id": "12345678-1234-5678-1234-567812345678",
  "type": "organization",
  "name": "Organization Name"
}
```

This endpoint is useful for programmatically determining which organization an Admin API key belongs to.

For complete parameter details and response schemas, see the [Organization Info API reference](/en/api/admin-api/organization/get-me).

## Accessing usage and cost reports

To access usage and cost reports for your organization, use the Usage and Cost API endpoints:

* The [**Usage endpoint**](/en/docs/build-with-claude/usage-cost-api#usage-api) (`/v1/organizations/usage_report/messages`) provides detailed usage data, including token counts and request metrics, grouped by various dimensions such as workspace, user, and model.
* The [**Cost endpoint**](/en/docs/build-with-claude/usage-cost-api#cost-api) (`/v1/organizations/cost_report`) provides cost data associated with your organization's usage, allowing you to track expenses and allocate costs by workspace or description.

These endpoints provide detailed insights into your organization's usage and associated costs.

## Accessing Claude Code analytics

For organizations using Claude Code, the [**Claude Code Analytics API**](/en/docs/build-with-claude/claude-code-analytics-api) provides detailed productivity metrics and usage insights:

* The [**Claude Code Analytics endpoint**](/en/docs/build-with-claude/claude-code-analytics-api) (`/v1/organizations/usage_report/claude_code`) provides daily aggregated metrics for Claude Code usage, including sessions, lines of code, commits, pull requests, tool usage statistics, and cost data broken down by user and model.

This API enables you to track developer productivity, analyze Claude Code adoption, and build custom dashboards for your organization.

## Best practices

To effectively use the Admin API:

* Use meaningful names and descriptions for workspaces and API keys
* Implement proper error handling for failed operations
* Regularly audit member roles and permissions
* Clean up unused workspaces and expired invites
* Monitor API key usage and rotate keys periodically

## FAQ

<AccordionGroup>
  <Accordion title="What permissions are needed to use the Admin API?">
    Only organization members with the admin role can use the Admin API. They must also have a special Admin API key (starting with `sk-ant-admin`).
  </Accordion>

  <Accordion title="Can I create new API keys through the Admin API?">
    No, new API keys can only be created through the Claude Console for security reasons. The Admin API can only manage existing API keys.
  </Accordion>

  <Accordion title="What happens to API keys when removing a user?">
    API keys persist in their current state as they are scoped to the Organization, not to individual users.
  </Accordion>

  <Accordion title="Can organization admins be removed via the API?">
    No, organization members with the admin role cannot be removed via the API for security reasons.
  </Accordion>

  <Accordion title="How long do organization invites last?">
    Organization invites expire after 21 days. There is currently no way to modify this expiration period.
  </Accordion>

  <Accordion title="Are there limits on workspaces?">
    Yes, you can have a maximum of 100 workspaces per Organization. Archived workspaces do not count towards this limit.
  </Accordion>

  <Accordion title="What's the Default Workspace?">
    Every Organization has a "Default Workspace" that cannot be edited or removed, and has no ID. This Workspace does not appear in workspace list endpoints.
  </Accordion>

  <Accordion title="How do organization roles affect Workspace access?">
    Organization admins automatically get the `workspace_admin` role to all workspaces. Organization billing members automatically get the `workspace_billing` role. Organization users and developers must be manually added to each workspace.
  </Accordion>

  <Accordion title="Which roles can be assigned in workspaces?">
    Organization users and developers can be assigned `workspace_admin`, `workspace_developer`, or `workspace_user` roles. The `workspace_billing` role can't be manually assigned - it's inherited from having the organization `billing` role.
  </Accordion>

  <Accordion title="Can organization admin or billing members' workspace roles be changed?">
    Only organization billing members can have their workspace role upgraded to an admin role. Otherwise, organization admins and billing members can't have their workspace roles changed or be removed from workspaces while they hold those organization roles. Their workspace access must be modified by changing their organization role first.
  </Accordion>

  <Accordion title="What happens to workspace access when organization roles change?">
    If an organization admin or billing member is demoted to user or developer, they lose access to all workspaces except ones where they were manually assigned roles. When users are promoted to admin or billing roles, they gain automatic access to all workspaces.
  </Accordion>
</AccordionGroup>


# Batch processing
Source: https://docs.claude.com/en/docs/build-with-claude/batch-processing



Batch processing is a powerful approach for handling large volumes of requests efficiently. Instead of processing requests one at a time with immediate responses, batch processing allows you to submit multiple requests together for asynchronous processing. This pattern is particularly useful when:

* You need to process large volumes of data
* Immediate responses are not required
* You want to optimize for cost efficiency
* You're running large-scale evaluations or analyses

The Message Batches API is our first implementation of this pattern.

***

# Message Batches API

The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of [Messages](/en/api/messages) requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput.

You can [explore the API reference directly](/en/api/creating-message-batches), in addition to this guide.

## How the Message Batches API works

When you send a request to the Message Batches API:

1. The system creates a new Message Batch with the provided Messages requests.
2. The batch is then processed asynchronously, with each request handled independently.
3. You can poll for the status of the batch and retrieve results when processing has ended for all requests.

This is especially useful for bulk operations that don't require immediate results, such as:

* Large-scale evaluations: Process thousands of test cases efficiently.
* Content moderation: Analyze large volumes of user-generated content asynchronously.
* Data analysis: Generate insights or summaries for large datasets.
* Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries).

### Batch limitations

* A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first.
* We process each batch as fast as possible, with most batches completing within 1 hour. You will be able to access batch results when all messages have completed or after 24 hours, whichever comes first. Batches will expire if processing does not complete within 24 hours.
* Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download.
* Batches are scoped to a [Workspace](https://console.anthropic.com/settings/workspaces). You may view all batches—and their results—that were created within the Workspace that your API key belongs to.
* Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See [Message Batches API rate limits](/en/api/rate-limits#message-batches-api). Additionally, we may slow down processing based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours.
* Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured [spend limit](https://console.anthropic.com/settings/limits).

### Supported models

All [active models](/en/docs/about-claude/models/overview) support the Message Batches API.

### What can be batched

Any request that you can make to the Messages API can be included in a batch. This includes:

* Vision
* Tool use
* System messages
* Multi-turn conversations
* Any beta features

Since each request in the batch is processed independently, you can mix different types of requests within a single batch.

<Tip>
  Since batches can take longer than 5 minutes to process, consider using the [1-hour cache duration](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration) with prompt caching for better cache hit rates when processing batches with shared context.
</Tip>

***

## Pricing

The Batches API offers significant cost savings. All usage is charged at 50% of the standard API prices.

| Model                                                                      | Batch input    | Batch output   |
| -------------------------------------------------------------------------- | -------------- | -------------- |
| Claude Opus 4.1                                                            | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Opus 4                                                              | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Sonnet 4.5                                                          | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Sonnet 4                                                            | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Haiku 4.5                                                           | \$0.50 / MTok  | \$2.50 / MTok  |
| Claude Haiku 3.5                                                           | \$0.40 / MTok  | \$2 / MTok     |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Haiku 3                                                             | \$0.125 / MTok | \$0.625 / MTok |

***

## How to use the Message Batches API

### Prepare and create your batch

A Message Batch is composed of a list of requests to create a Message. The shape of an individual request is comprised of:

* A unique `custom_id` for identifying the Messages request
* A `params` object with the standard [Messages API](/en/api/messages) parameters

You can [create a batch](/en/api/creating-message-batches) by passing this list into the `requests` parameter:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages/batches \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "requests": [
          {
              "custom_id": "my-first-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "messages": [
                      {"role": "user", "content": "Hello, world"}
                  ]
              }
          },
          {
              "custom_id": "my-second-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "messages": [
                      {"role": "user", "content": "Hi again, friend"}
                  ]
              }
          }
      ]
  }'
  ```

  ```python Python theme={null}
  import anthropic
  from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
  from anthropic.types.messages.batch_create_params import Request

  client = anthropic.Anthropic()

  message_batch = client.messages.batches.create(
      requests=[
          Request(
              custom_id="my-first-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  messages=[{
                      "role": "user",
                      "content": "Hello, world",
                  }]
              )
          ),
          Request(
              custom_id="my-second-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  messages=[{
                      "role": "user",
                      "content": "Hi again, friend",
                  }]
              )
          )
      ]
  )

  print(message_batch)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const messageBatch = await anthropic.messages.batches.create({
    requests: [{
      custom_id: "my-first-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        messages: [
          {"role": "user", "content": "Hello, world"}
        ]
      }
    }, {
      custom_id: "my-second-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        messages: [
          {"role": "user", "content": "Hi again, friend"}
        ]
      }
    }]
  });

  console.log(messageBatch)
  ```

  ```java Java theme={null}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.batches.*;

  public class BatchExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          BatchCreateParams params = BatchCreateParams.builder()
              .addRequest(BatchCreateParams.Request.builder()
                  .customId("my-first-request")
                  .params(BatchCreateParams.Request.Params.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addUserMessage("Hello, world")
                      .build())
                  .build())
              .addRequest(BatchCreateParams.Request.builder()
                  .customId("my-second-request")
                  .params(BatchCreateParams.Request.Params.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addUserMessage("Hi again, friend")
                      .build())
                  .build())
              .build();

          MessageBatch messageBatch = client.messages().batches().create(params);

          System.out.println(messageBatch);
      }
  }
  ```
</CodeGroup>

In this example, two separate requests are batched together for asynchronous processing. Each request has a unique `custom_id` and contains the standard parameters you'd use for a Messages API call.

<Tip>
  **Test your batch requests with the Messages API**

  Validation of the `params` object for each message request is performed asynchronously, and validation errors are returned when processing of the entire batch has ended. You can ensure that you are building your input correctly by verifying your request shape with the [Messages API](/en/api/messages) first.
</Tip>

When a batch is first created, the response will have a processing status of `in_progress`.

```JSON JSON theme={null}
{
  "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

### Tracking your batch

The Message Batch's `processing_status` field indicates the stage of processing the batch is in. It starts as `in_progress`, then updates to `ended` once all the requests in the batch have finished processing, and results are ready. You can monitor the state of your batch by visiting the [Console](https://console.anthropic.com/settings/workspaces/default/batches), or using the [retrieval endpoint](/en/api/retrieving-message-batches).

#### Polling for Message Batch completion

To poll a Message Batch, you'll need its `id`, which is provided in the response when creating a batch or by listing batches. You can implement a polling loop that checks the batch status periodically until processing has ended:

<CodeGroup>
  ```python Python theme={null}
  import anthropic
  import time

  client = anthropic.Anthropic()

  message_batch = None
  while True:
      message_batch = client.messages.batches.retrieve(
          MESSAGE_BATCH_ID
      )
      if message_batch.processing_status == "ended":
          break

      print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
      time.sleep(60)
  print(message_batch)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  let messageBatch;
  while (true) {
    messageBatch = await anthropic.messages.batches.retrieve(
      MESSAGE_BATCH_ID
    );
    if (messageBatch.processing_status === 'ended') {
      break;
    }

    console.log(`Batch ${messageBatch} is still processing... waiting`);
    await new Promise(resolve => setTimeout(resolve, 60_000));
  }
  console.log(messageBatch);
  ```

  ```bash Shell theme={null}
  #!/bin/sh

  until [[ $(curl -s "https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID" \
            --header "x-api-key: $ANTHROPIC_API_KEY" \
            --header "anthropic-version: 2023-06-01" \
            | grep -o '"processing_status":[[:space:]]*"[^"]*"' \
            | cut -d'"' -f4) == "ended" ]]; do
      echo "Batch $MESSAGE_BATCH_ID is still processing..."
      sleep 60
  done

  echo "Batch $MESSAGE_BATCH_ID has finished processing"
  ```
</CodeGroup>

### Listing all Message Batches

You can list all Message Batches in your Workspace using the [list endpoint](/en/api/listing-message-batches). The API supports pagination, automatically fetching additional pages as needed:

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Automatically fetches more pages as needed.
  for message_batch in client.messages.batches.list(
      limit=20
  ):
      print(message_batch)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Automatically fetches more pages as needed.
  for await (const messageBatch of anthropic.messages.batches.list({
    limit: 20
  })) {
    console.log(messageBatch);
  }
  ```

  ```bash Shell theme={null}
  #!/bin/sh

  if ! command -v jq &> /dev/null; then
      echo "Error: This script requires jq. Please install it first."
      exit 1
  fi

  BASE_URL="https://api.anthropic.com/v1/messages/batches"

  has_more=true
  after_id=""

  while [ "$has_more" = true ]; do
      # Construct URL with after_id if it exists
      if [ -n "$after_id" ]; then
          url="${BASE_URL}?limit=20&after_id=${after_id}"
      else
          url="$BASE_URL?limit=20"
      fi

      response=$(curl -s "$url" \
                --header "x-api-key: $ANTHROPIC_API_KEY" \
                --header "anthropic-version: 2023-06-01")

      # Extract values using jq
      has_more=$(echo "$response" | jq -r '.has_more')
      after_id=$(echo "$response" | jq -r '.last_id')

      # Process and print each entry in the data array
      echo "$response" | jq -c '.data[]' | while read -r entry; do
          echo "$entry" | jq '.'
      done
  done
  ```

  ```java Java theme={null}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.batches.*;

  public class BatchListExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Automatically fetches more pages as needed
          for (MessageBatch messageBatch : client.messages().batches().list(
                  BatchListParams.builder()
                          .limit(20)
                          .build()
          )) {
              System.out.println(messageBatch);
          }
      }
  }
  ```
</CodeGroup>

### Retrieving batch results

Once batch processing has ended, each Messages request in the batch will have a result. There are 4 result types:

| Result Type | Description                                                                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded` | Request was successful. Includes the message result.                                                                                                                        |
| `errored`   | Request encountered an error and a message was not created. Possible errors include invalid requests and internal server errors. You will not be billed for these requests. |
| `canceled`  | User canceled the batch before this request could be sent to the model. You will not be billed for these requests.                                                          |
| `expired`   | Batch reached its 24 hour expiration before this request could be sent to the model. You will not be billed for these requests.                                             |

You will see an overview of your results with the batch's `request_counts`, which shows how many requests reached each of these four states.

Results of the batch are available for download at the `results_url` property on the Message Batch, and if the organization permission allows, in the Console. Because of the potentially large size of the results, it's recommended to [stream results](/en/api/retrieving-message-batch-results) back rather than download them all at once.

<CodeGroup>
  ```bash Shell theme={null}
  #!/bin/sh
  curl "https://api.anthropic.com/v1/messages/batches/msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d" \
    --header "anthropic-version: 2023-06-01" \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    | grep -o '"results_url":[[:space:]]*"[^"]*"' \
    | cut -d'"' -f4 \
    | while read -r url; do
      curl -s "$url" \
        --header "anthropic-version: 2023-06-01" \
        --header "x-api-key: $ANTHROPIC_API_KEY" \
        | sed 's/}{/}\n{/g' \
        | while IFS= read -r line
      do
        result_type=$(echo "$line" | sed -n 's/.*"result":[[:space:]]*{[[:space:]]*"type":[[:space:]]*"\([^"]*\)".*/\1/p')
        custom_id=$(echo "$line" | sed -n 's/.*"custom_id":[[:space:]]*"\([^"]*\)".*/\1/p')
        error_type=$(echo "$line" | sed -n 's/.*"error":[[:space:]]*{[[:space:]]*"type":[[:space:]]*"\([^"]*\)".*/\1/p')

        case "$result_type" in
          "succeeded")
            echo "Success! $custom_id"
            ;;
          "errored")
            if [ "$error_type" = "invalid_request" ]; then
              # Request body must be fixed before re-sending request
              echo "Validation error: $custom_id"
            else
              # Request can be retried directly
              echo "Server error: $custom_id"
            fi
            ;;
          "expired")
            echo "Expired: $line"
            ;;
        esac
      done
    done

  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Stream results file in memory-efficient chunks, processing one at a time
  for result in client.messages.batches.results(
      "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  ):
      match result.result.type:
          case "succeeded":
              print(f"Success! {result.custom_id}")
          case "errored":
              if result.result.error.type == "invalid_request":
                  # Request body must be fixed before re-sending request
                  print(f"Validation error {result.custom_id}")
              else:
                  # Request can be retried directly
                  print(f"Server error {result.custom_id}")
          case "expired":
              print(f"Request expired {result.custom_id}")
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Stream results file in memory-efficient chunks, processing one at a time
  for await (const result of await anthropic.messages.batches.results(
      "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"
  )) {
    switch (result.result.type) {
      case 'succeeded':
        console.log(`Success! ${result.custom_id}`);
        break;
      case 'errored':
        if (result.result.error.type == "invalid_request") {
          // Request body must be fixed before re-sending request
          console.log(`Validation error: ${result.custom_id}`);
        } else {
          // Request can be retried directly
          console.log(`Server error: ${result.custom_id}`);
        }
        break;
      case 'expired':
        console.log(`Request expired: ${result.custom_id}`);
        break;
    }
  }
  ```

  ```java Java theme={null}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.http.StreamResponse;
  import com.anthropic.models.messages.batches.MessageBatchIndividualResponse;
  import com.anthropic.models.messages.batches.BatchResultsParams;

  public class BatchResultsExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Stream results file in memory-efficient chunks, processing one at a time
          try (StreamResponse<MessageBatchIndividualResponse> streamResponse = client.messages()
                  .batches()
                  .resultsStreaming(
                          BatchResultsParams.builder()
                                  .messageBatchId("msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d")
                                  .build())) {

              streamResponse.stream().forEach(result -> {
                  if (result.result().isSucceeded()) {
                      System.out.println("Success! " + result.customId());
                  } else if (result.result().isErrored()) {
                      if (result.result().asErrored().error().error().isInvalidRequestError()) {
                          // Request body must be fixed before re-sending request
                          System.out.println("Validation error: " + result.customId());
                      } else {
                          // Request can be retried directly
                          System.out.println("Server error: " + result.customId());
                      }
                  } else if (result.result().isExpired()) {
                      System.out.println("Request expired: " + result.customId());
                  }
              });
          }
      }
  }
  ```
</CodeGroup>

The results will be in `.jsonl` format, where each line is a valid JSON object representing the result of a single request in the Message Batch. For each streamed result, you can do something different depending on its `custom_id` and result type. Here is an example set of results:

```JSON .jsonl file theme={null}
{"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
{"custom_id":"my-first-request","result":{"type":"succeeded","message":{"id":"msg_01FqfsLoHwgeFbguDgpz48m7","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[{"type":"text","text":"Hello! How can I assist you today? Feel free to ask me any questions or let me know if there's anything you'd like to chat about."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"output_tokens":34}}}}
```

If your result has an error, its `result.error` will be set to our standard [error shape](/en/api/errors#error-shapes).

<Tip>
  **Batch results may not match input order**

  Batch results can be returned in any order, and may not match the ordering of requests when the batch was created. In the above example, the result for the second batch request is returned before the first. To correctly match results with their corresponding requests, always use the `custom_id` field.
</Tip>

### Canceling a Message Batch

You can cancel a Message Batch that is currently processing using the [cancel endpoint](/en/api/canceling-message-batches). Immediately after cancellation, a batch's `processing_status` will be `canceling`. You can use the same polling technique described above to wait until cancellation is finalized. Canceled batches end up with a status of `ended` and may contain partial results for requests that were processed before cancellation.

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  message_batch = client.messages.batches.cancel(
      MESSAGE_BATCH_ID,
  )
  print(message_batch)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const messageBatch = await anthropic.messages.batches.cancel(
      MESSAGE_BATCH_ID
  );
  console.log(messageBatch);
  ```

  ```bash Shell theme={null}
  #!/bin/sh
  curl --request POST https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/cancel \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01"
  ```

  ```java Java theme={null}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.batches.*;

  public class BatchCancelExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          MessageBatch messageBatch = client.messages().batches().cancel(
                  BatchCancelParams.builder()
                          .messageBatchId(MESSAGE_BATCH_ID)
                          .build()
          );
          System.out.println(messageBatch);
      }
  }
  ```
</CodeGroup>

The response will show the batch in a `canceling` state:

```JSON JSON theme={null}
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch",
  "processing_status": "canceling",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": "2024-09-24T18:39:03.114875Z",
  "results_url": null
}
```

### Using prompt caching with Message Batches

The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns.

To maximize the likelihood of cache hits in your batch requests:

1. Include identical `cache_control` blocks in every Message request within your batch
2. Maintain a steady stream of requests to prevent cache entries from expiring after their 5-minute lifetime
3. Structure your requests to share as much cached content as possible

Example of implementing prompt caching in a batch:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages/batches \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "requests": [
          {
              "custom_id": "my-first-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "system": [
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  "messages": [
                      {"role": "user", "content": "Analyze the major themes in Pride and Prejudice."}
                  ]
              }
          },
          {
              "custom_id": "my-second-request",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "system": [
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  "messages": [
                      {"role": "user", "content": "Write a summary of Pride and Prejudice."}
                  ]
              }
          }
      ]
  }'
  ```

  ```python Python theme={null}
  import anthropic
  from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
  from anthropic.types.messages.batch_create_params import Request

  client = anthropic.Anthropic()

  message_batch = client.messages.batches.create(
      requests=[
          Request(
              custom_id="my-first-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  system=[
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  messages=[{
                      "role": "user",
                      "content": "Analyze the major themes in Pride and Prejudice."
                  }]
              )
          ),
          Request(
              custom_id="my-second-request",
              params=MessageCreateParamsNonStreaming(
                  model="claude-sonnet-4-5",
                  max_tokens=1024,
                  system=[
                      {
                          "type": "text",
                          "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                      },
                      {
                          "type": "text",
                          "text": "<the entire contents of Pride and Prejudice>",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ],
                  messages=[{
                      "role": "user",
                      "content": "Write a summary of Pride and Prejudice."
                  }]
              )
          )
      ]
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const messageBatch = await anthropic.messages.batches.create({
    requests: [{
      custom_id: "my-first-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: {type: "ephemeral"}
          }
        ],
        messages: [
          {"role": "user", "content": "Analyze the major themes in Pride and Prejudice."}
        ]
      }
    }, {
      custom_id: "my-second-request",
      params: {
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: {type: "ephemeral"}
          }
        ],
        messages: [
          {"role": "user", "content": "Write a summary of Pride and Prejudice."}
        ]
      }
    }]
  });
  ```

  ```java Java theme={null}
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.CacheControlEphemeral;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;
  import com.anthropic.models.messages.batches.*;

  public class BatchExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          BatchCreateParams createParams = BatchCreateParams.builder()
                  .addRequest(BatchCreateParams.Request.builder()
                          .customId("my-first-request")
                          .params(BatchCreateParams.Request.Params.builder()
                                  .model(Model.CLAUDE_OPUS_4_0)
                                  .maxTokens(1024)
                                  .systemOfTextBlockParams(List.of(
                                          TextBlockParam.builder()
                                                  .text("You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n")
                                                  .build(),
                                          TextBlockParam.builder()
                                                  .text("<the entire contents of Pride and Prejudice>")
                                                  .cacheControl(CacheControlEphemeral.builder().build())
                                                  .build()
                                  ))
                                  .addUserMessage("Analyze the major themes in Pride and Prejudice.")
                                  .build())
                          .build())
                  .addRequest(BatchCreateParams.Request.builder()
                          .customId("my-second-request")
                          .params(BatchCreateParams.Request.Params.builder()
                                  .model(Model.CLAUDE_OPUS_4_0)
                                  .maxTokens(1024)
                                  .systemOfTextBlockParams(List.of(
                                          TextBlockParam.builder()
                                                  .text("You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n")
                                                  .build(),
                                          TextBlockParam.builder()
                                                  .text("<the entire contents of Pride and Prejudice>")
                                                  .cacheControl(CacheControlEphemeral.builder().build())
                                                  .build()
                                  ))
                                  .addUserMessage("Write a summary of Pride and Prejudice.")
                                  .build())
                          .build())
                  .build();

          MessageBatch messageBatch = client.messages().batches().create(createParams);
      }
  }
  ```
</CodeGroup>

In this example, both requests in the batch include identical system messages and the full text of Pride and Prejudice marked with `cache_control` to increase the likelihood of cache hits.

### Best practices for effective batching

To get the most out of the Batches API:

* Monitor batch processing status regularly and implement appropriate retry logic for failed requests.
* Use meaningful `custom_id` values to easily match results with requests, since order is not guaranteed.
* Consider breaking very large datasets into multiple batches for better manageability.
* Dry run a single request shape with the Messages API to avoid validation errors.

### Troubleshooting common issues

If experiencing unexpected behavior:

* Verify that the total batch request size doesn't exceed 256 MB. If the request size is too large, you may get a 413 `request_too_large` error.
* Check that you're using [supported models](#supported-models) for all requests in the batch.
* Ensure each request in the batch has a unique `custom_id`.
* Ensure that it has been less than 29 days since batch `created_at` (not processing `ended_at`) time. If over 29 days have passed, results will no longer be viewable.
* Confirm that the batch has not been canceled.

Note that the failure of one request in a batch does not affect the processing of other requests.

***

## Batch storage and privacy

* **Workspace isolation**: Batches are isolated within the Workspace they are created in. They can only be accessed by API keys associated with that Workspace, or users with permission to view Workspace batches in the Console.

* **Result availability**: Batch results are available for 29 days after the batch is created, allowing ample time for retrieval and processing.

***

## FAQ

<AccordionGroup>
  <Accordion title="How long does it take for a batch to process?">
    Batches may take up to 24 hours for processing, but many will finish sooner. Actual processing time depends on the size of the batch, current demand, and your request volume. It is possible for a batch to expire and not complete within 24 hours.
  </Accordion>

  <Accordion title="Is the Batches API available for all models?">
    See [above](#supported-models) for the list of supported models.
  </Accordion>

  <Accordion title="Can I use the Message Batches API with other API features?">
    Yes, the Message Batches API supports all features available in the Messages API, including beta features. However, streaming is not supported for batch requests.
  </Accordion>

  <Accordion title="How does the Message Batches API affect pricing?">
    The Message Batches API offers a 50% discount on all usage compared to standard API prices. This applies to input tokens, output tokens, and any special tokens. For more on pricing, visit our [pricing page](https://claude.com/pricing#anthropic-api).
  </Accordion>

  <Accordion title="Can I update a batch after it's been submitted?">
    No, once a batch has been submitted, it cannot be modified. If you need to make changes, you should cancel the current batch and submit a new one. Note that cancellation may not take immediate effect.
  </Accordion>

  <Accordion title="Are there Message Batches API rate limits and do they interact with the Messages API rate limits?">
    The Message Batches API has HTTP requests-based rate limits in addition to limits on the number of requests in need of processing. See [Message Batches API rate limits](/en/api/rate-limits#message-batches-api). Usage of the Batches API does not affect rate limits in the Messages API.
  </Accordion>

  <Accordion title="How do I handle errors in my batch requests?">
    When you retrieve the results, each request will have a `result` field indicating whether it `succeeded`, `errored`, was `canceled`, or `expired`. For `errored` results, additional error information will be provided. View the error response object in the [API reference](/en/api/creating-message-batches).
  </Accordion>

  <Accordion title="How does the Message Batches API handle privacy and data separation?">
    The Message Batches API is designed with strong privacy and data separation measures:

    1. Batches and their results are isolated within the Workspace in which they were created. This means they can only be accessed by API keys from that same Workspace.
    2. Each request within a batch is processed independently, with no data leakage between requests.
    3. Results are only available for a limited time (29 days), and follow our [data retention policy](https://support.claude.com/en/articles/7996866-how-long-do-you-store-personal-data).
    4. Downloading batch results in the Console can be disabled on the organization-level or on a per-workspace basis.
  </Accordion>

  <Accordion title="Can I use prompt caching in the Message Batches API?">
    Yes, it is possible to use prompt caching with Message Batches API. However, because asynchronous batch requests can be processed concurrently and in any order, cache hits are provided on a best-effort basis.
  </Accordion>
</AccordionGroup>



---

**Navigation:** [← Previous](./05-how-to-implement-tool-use.md) | [Index](./index.md) | [Next →](./07-citations.md)
