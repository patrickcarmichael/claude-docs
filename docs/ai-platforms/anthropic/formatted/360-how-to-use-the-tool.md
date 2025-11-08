---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use the tool

### Execute Bash commands

Ask Claude to check system information and install packages:
```bash
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Check the Python version and list installed packages"
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
```
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Check the Python version and list installed packages"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
```
```typescript
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: "Check the Python version and list installed packages"
    }],
    tools: [{
      type: "code_execution_20250825",
      name: "code_execution"
    }]
  });
```

### Create and edit files directly

Claude can create, view, and edit files directly in the sandbox using the file manipulation capabilities:
```bash
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
```
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
```
```typescript
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
    }],
    tools: [{
      type: "code_execution_20250825",
      name: "code_execution"
    }]
  });
```

### Upload and analyze your own files

To analyze your own data files (CSV, Excel, images, etc.), upload them via the Files API and reference them in your request:

>   **📝 Note**
>
> Using the Files API with Code Execution requires two beta headers: `"anthropic-beta": "code-execution-2025-08-25,files-api-2025-04-14"`

The Python environment can process various file types uploaded via the Files API, including:

* CSV
* Excel (.xlsx, .xls)
* JSON
* XML
* Images (JPEG, PNG, GIF, WebP)
* Text files (.txt, .md, .py, etc)

#### Upload and analyze files

1. **Upload your file** using the [Files API](/en/docs/build-with-claude/files)
2. **Reference the file** in your message using a `container_upload` content block
3. **Include the code execution tool** in your API request
```bash
  # First, upload a file

  curl https://api.anthropic.com/v1/files \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: files-api-2025-04-14" \
      --form 'file=@"data.csv"' \

  # Then use the file_id with code execution

  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25,files-api-2025-04-14" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": [
                  {"type": "text", "text": "Analyze this CSV data"},
                  {"type": "container_upload", "file_id": "file_abc123"}
              ]
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
```
```python
  import anthropic

  client = anthropic.Anthropic()

  # Upload a file

  file_object = client.beta.files.upload(
      file=open("data.csv", "rb"),
  )

  # Use the file_id with code execution

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": [
              {"type": "text", "text": "Analyze this CSV data"},
              {"type": "container_upload", "file_id": file_object.id}
          ]
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';
  import { createReadStream } from 'fs';

  const anthropic = new Anthropic();

  async function main() {
    // Upload a file
    const fileObject = await anthropic.beta.files.create({
      file: createReadStream("data.csv"),
    });

    // Use the file_id with code execution
    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: [
          { type: "text", text: "Analyze this CSV data" },
          { type: "container_upload", file_id: fileObject.id }
        ]
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    console.log(response);
  }

  main().catch(console.error);
```

#### Retrieve generated files

When Claude creates files during code execution, you can retrieve these files using the Files API:
```python
  from anthropic import Anthropic

  # Initialize the client

  client = Anthropic()

  # Request code execution that creates files

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Create a matplotlib visualization and save it as output.png"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  # Extract file IDs from the response

  def extract_file_ids(response):
      file_ids = []
      for item in response.content:
          if item.type == 'bash_code_execution_tool_result':
              content_item = item.content
              if content_item.type == 'bash_code_execution_result':
                  for file in content_item.content:
                      if hasattr(file, 'file_id'):
                          file_ids.append(file.file_id)
      return file_ids

  # Download the created files

  for file_id in extract_file_ids(response):
      file_metadata = client.beta.files.retrieve_metadata(file_id)
      file_content = client.beta.files.download(file_id)
      file_content.write_to_file(file_metadata.filename)
      print(f"Downloaded: {file_metadata.filename}")
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';
  import { writeFileSync } from 'fs';

  // Initialize the client
  const anthropic = new Anthropic();

  async function main() {
    // Request code execution that creates files
    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: "Create a matplotlib visualization and save it as output.png"
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    // Extract file IDs from the response
    function extractFileIds(response: any): string[] {
      const fileIds: string[] = [];
      for (const item of response.content) {
        if (item.type === 'bash_code_execution_tool_result') {
          const contentItem = item.content;
          if (contentItem.type === 'bash_code_execution_result' && contentItem.content) {
            for (const file of contentItem.content) {
              fileIds.push(file.file_id);
            }
          }
        }
      }
      return fileIds;
    }

    // Download the created files
    const fileIds = extractFileIds(response);
    for (const fileId of fileIds) {
      const fileMetadata = await anthropic.beta.files.retrieveMetadata(fileId);
      const fileContent = await anthropic.beta.files.download(fileId);

      // Convert ReadableStream to Buffer and save
      const chunks: Uint8Array[] = [];
      for await (const chunk of fileContent) {
        chunks.push(chunk);
      }
      const buffer = Buffer.concat(chunks);
      writeFileSync(fileMetadata.filename, buffer);
      console.log(`Downloaded: ${fileMetadata.filename}`);
    }
  }

  main().catch(console.error);
```

### Combine operations

A complex workflow using all capabilities:
```bash
  # First, upload a file

  curl https://api.anthropic.com/v1/files \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: files-api-2025-04-14" \
      --form 'file=@"data.csv"' \
      > file_response.json

  # Extract file_id (using jq)

  FILE_ID=$(jq -r '.id' file_response.json)

  # Then use it with code execution

  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25,files-api-2025-04-14" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": [
                  {
                      "type": "text", 
                      "text": "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"
                  },
                  {
                      "type": "container_upload", 
                      "file_id": "'$FILE_ID'"
                  }
              ]
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
```
```python
  # Upload a file

  file_object = client.beta.files.upload(
      file=open("data.csv", "rb"),
  )

  # Use it with code execution

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": [
              {"type": "text", "text": "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"},
              {"type": "container_upload", "file_id": file_object.id}
          ]
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  # Claude might:

  # 1. Use bash to check file size and preview data

  # 2. Use text_editor to write Python code to analyze the CSV and create visualizations

  # 3. Use bash to run the Python code

  # 4. Use text_editor to create a README.md with findings

  # 5. Use bash to organize files into a report directory

```
```typescript
  // Upload a file
  const fileObject = await anthropic.beta.files.create({
    file: createReadStream("data.csv"),
  });

  // Use it with code execution
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: [
        {type: "text", text: "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"},
        {type: "container_upload", file_id: fileObject.id}
      ]
    }],
    tools: [{
      type: "code_execution_20250825",
      name: "code_execution"
    }]
  });

  // Claude might:
  // 1. Use bash to check file size and preview data
  // 2. Use text_editor to write Python code to analyze the CSV and create visualizations
  // 3. Use bash to run the Python code
  // 4. Use text_editor to create a README.md with findings
  // 5. Use bash to organize files into a report directory
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
