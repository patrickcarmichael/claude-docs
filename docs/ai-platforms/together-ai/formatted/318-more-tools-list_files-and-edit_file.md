---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## More tools: `list_files` and `edit_file`

We'll want our coding agent to be able to see what files exist in a repo and also modify pre-existing files as well so we'll add two more tools:

### `list_files` Tool: Given a path to a repo, this tool lists the files in that repo.

```python
  def list_files(path="."):
      """
      Lists all files and directories in the specified path.

      Args:
          path (str): The relative path of a directory in the working directory.
                      Defaults to the current directory.

      Returns:
          str: A JSON string containing a list of files and directories.
      """
      result = []
      base_path = Path(path)

      if not base_path.exists():
          return json.dumps({"error": f"Path '{path}' does not exist"})

      for root, dirs, files in os.walk(path):
          root_path = Path(root)
          rel_root = (
              root_path.relative_to(base_path)
              if root_path != base_path
              else Path(".")
          )

          # Add directories with trailing slash

          for dir_name in dirs:
              rel_path = rel_root / dir_name
              if str(rel_path) != ".":
                  result.append(f"{rel_path}/")

          # Add files

          for file_name in files:
              rel_path = rel_root / file_name
              if str(rel_path) != ".":
                  result.append(str(rel_path))

      return json.dumps(result)


  list_files_schema = {
      "type": "function",
      "function": {
          "name": "list_files",
          "description": "List all files and directories in the specified path.",
          "parameters": {
              "type": "object",
              "properties": {
                  "path": {
                      "type": "string",
                      "description": "The relative path of a directory in the working directory. Defaults to current directory.",
                  }
              },
          },
      },
  }

  # Register the list_files function in the tools

  tools.append(list_files_schema)
```

### `edit_file` Tool: Edit files by adding new content or replacing old content

```python
  def edit_file(path, old_str, new_str):
      """
      Edit a file by replacing all occurrences of old_str with new_str.
      If old_str is empty and the file doesn't exist, create a new file with new_str.

      Args:
          path (str): The relative path of the file to edit
          old_str (str): The string to replace
          new_str (str): The string to replace with

      Returns:
          str: "OK" if successful
      """

      if not path or old_str == new_str:
          raise ValueError("Invalid input parameters")

      try:
          with open(path, "r") as file:
              old_content = file.read()
      except FileNotFoundError:
          if old_str == "":
              # Create a new file if old_str is empty and file doesn't exist

              with open(path, "w") as file:
                  file.write(new_str)
              return "OK"
          else:
              raise FileNotFoundError(f"File not found: {path}")

      new_content = old_content.replace(old_str, new_str)

      if old_content == new_content and old_str != "":
          raise ValueError("old_str not found in file")

      with open(path, "w") as file:
          file.write(new_content)

      return "OK"


  # Define the function schema for the edit_file tool

  edit_file_schema = {
      "type": "function",
      "function": {
          "name": "edit_file",
          "description": "Edit a file by replacing all occurrences of a string with another string",
          "parameters": {
              "type": "object",
              "properties": {
                  "path": {
                      "type": "string",
                      "description": "The relative path of the file to edit",
                  },
                  "old_str": {
                      "type": "string",
                      "description": "The string to replace (empty string for new files)",
                  },
                  "new_str": {
                      "type": "string",
                      "description": "The string to replace with",
                  },
              },
              "required": ["path", "old_str", "new_str"],
          },
      },
  }

  # Update the tools list to include the edit_file function

  tools.append(edit_file_schema)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
