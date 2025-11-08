---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Defining Tools for the Agent

To make this workflow of instructing the model to use tools and then running the functions it calls and sending it the response more convenient people have built scaffolding where we can pass in pre-specified tools to LLMs as follows:
```python
  # Let define a function that you would use to read a file


  def read_file(path: str) -> str:
      """
      Reads the content of a file and returns it as a string.

      Args:
          path: The relative path of a file in the working directory.

      Returns:
          The content of the file as a string.

      Raises:
          FileNotFoundError: If the specified file does not exist.
          PermissionError: If the user does not have permission to read the file.
      """
      try:
          with open(path, "r", encoding="utf-8") as file:
              content = file.read()
          return content
      except FileNotFoundError:
          raise FileNotFoundError(f"The file '{path}' was not found.")
      except PermissionError:
          raise PermissionError(f"You don't have permission to read '{path}'.")
      except Exception as e:
          raise Exception(f"An error occurred while reading '{path}': {str(e)}")


  read_file_schema = {
      "type": "function",
      "function": {
          "name": "read_file",
          "description": "The relative path of a file in the working directory.",
          "parameters": {
              "properties": {
                  "path": {
                      "description": "The relative path of a file in the working directory.",
                      "title": "Path",
                      "type": "string",
                  }
              },
              "type": "object",
          },
      },
  }
```

Function schema:
```json
{'type': 'function',
 'function': {'name': 'read_file',
  'description': 'The relative path of a file in the working directory.',
  'parameters': {'properties': {'path': {'description': 'The relative path of a file in the working directory.',
     'title': 'Path',
     'type': 'string'}},
   'type': 'object'}}}
```

We can now pass these function/tool into an LLM and if needed it will use it to read files!

Lets create a file first:
```bash
  echo "my favourite colour is cyan sanguine" >> secret.txt
```

Now lets see if the model can use the new `read_file` tool to discover the secret!
```python
  import os
  import json

  messages = [
      {
          "role": "system",
          "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
          "role": "user",
          "content": "Read the file secret.txt and reveal the secret!",
      },
  ]
  tools = [read_file_schema]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=messages,
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
```

This will output a tool call from the model:
```json
[
  {
    "id": "call_kx9yu9ti0ejjabt7kexrsn1c",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"secret.txt\"}"
    },
    "index": 0
  }
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
