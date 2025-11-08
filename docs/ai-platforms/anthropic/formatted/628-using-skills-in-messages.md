---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using Skills in Messages

### Container Parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills per request.

The structure is identical for both Anthropic and custom Skills—specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:
```python
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "pptx",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Create a presentation about renewable energy"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'pptx',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Create a presentation about renewable energy'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
```
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "anthropic",
            "skill_id": "pptx",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Create a presentation about renewable energy"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
```

### Downloading Generated Files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**

1. Skills create files during code execution
2. Response includes `file_id` for each created file
3. Use Files API to download the actual file content
4. Save locally or process as needed

**Example: Creating and downloading an Excel file**
```python
  import anthropic

  client = anthropic.Anthropic()

  # Step 1: Use a Skill to create a file

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=[{
          "role": "user",
          "content": "Create an Excel file with a simple budget spreadsheet"
      }],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Step 2: Extract file IDs from the response

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

  # Step 3: Download the file using Files API

  for file_id in extract_file_ids(response):
      file_metadata = client.beta.files.retrieve_metadata(
          file_id=file_id,
          betas=["files-api-2025-04-14"]
      )
      file_content = client.beta.files.download(
          file_id=file_id,
          betas=["files-api-2025-04-14"]
      )

      # Step 4: Save to disk

      file_content.write_to_file(file_metadata.filename)
      print(f"Downloaded: {file_metadata.filename}")
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  // Step 1: Use a Skill to create a file
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages: [{
      role: 'user',
      content: 'Create an Excel file with a simple budget spreadsheet'
    }],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Step 2: Extract file IDs from the response
  function extractFileIds(response: any): string[] {
    const fileIds: string[] = [];
    for (const item of response.content) {
      if (item.type === 'bash_code_execution_tool_result') {
        const contentItem = item.content;
        if (contentItem.type === 'bash_code_execution_result') {
          for (const file of contentItem.content) {
            if ('file_id' in file) {
              fileIds.push(file.file_id);
            }
          }
        }
      }
    }
    return fileIds;
  }

  // Step 3: Download the file using Files API
  const fs = require('fs');
  for (const fileId of extractFileIds(response)) {
    const fileMetadata = await client.beta.files.retrieve_metadata(fileId, {
      betas: ['files-api-2025-04-14']
    });
    const fileContent = await client.beta.files.download(fileId, {
      betas: ['files-api-2025-04-14']
    });

    // Step 4: Save to disk
    fs.writeFileSync(fileMetadata.filename, Buffer.from(await fileContent.arrayBuffer()));
    console.log(`Downloaded: ${fileMetadata.filename}`);
  }
```
```bash
  # Step 1: Use a Skill to create a file

  RESPONSE=$(curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Create an Excel file with a simple budget spreadsheet"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }')

  # Step 2: Extract file_id from response (using jq)

  FILE_ID=$(echo "$RESPONSE" | jq -r '.content[] | select(.type=="bash_code_execution_tool_result") | .content | select(.type=="bash_code_execution_result") | .content[] | select(.file_id) | .file_id')

  # Step 3: Get filename from metadata

  FILENAME=$(curl "https://api.anthropic.com/v1/files/$FILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" | jq -r '.filename')

  # Step 4: Download the file using Files API

  curl "https://api.anthropic.com/v1/files/$FILE_ID/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    --output "$FILENAME"

  echo "Downloaded: $FILENAME"
```

**Additional Files API operations:**
```python
  # Get file metadata

  file_info = client.beta.files.retrieve_metadata(
      file_id=file_id,
      betas=["files-api-2025-04-14"]
  )
  print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

  # List all files

  files = client.beta.files.list(betas=["files-api-2025-04-14"])
  for file in files.data:
      print(f"{file.filename} - {file.created_at}")

  # Delete a file

  client.beta.files.delete(
      file_id=file_id,
      betas=["files-api-2025-04-14"]
  )
```
```typescript
  // Get file metadata
  const fileInfo = await client.beta.files.retrieve_metadata(fileId, {
    betas: ['files-api-2025-04-14']
  });
  console.log(`Filename: ${fileInfo.filename}, Size: ${fileInfo.size_bytes} bytes`);

  // List all files
  const files = await client.beta.files.list({
    betas: ['files-api-2025-04-14']
  });
  for (const file of files.data) {
    console.log(`${file.filename} - ${file.created_at}`);
  }

  // Delete a file
  await client.beta.files.delete(fileId, {
    betas: ['files-api-2025-04-14']
  });
```
```bash
  # Get file metadata

  curl "https://api.anthropic.com/v1/files/$FILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"

  # List all files

  curl "https://api.anthropic.com/v1/files" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"

  # Delete a file

  curl -X DELETE "https://api.anthropic.com/v1/files/$FILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"
```

>   **📝 Note**
>
> For complete details on the Files API, see the [Files API documentation](/en/api/files-content).

### Multi-Turn Conversations

Reuse the same container across multiple messages by specifying the container ID:
```python
  # First request creates container

  response1 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=[{"role": "user", "content": "Analyze this sales data"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Continue conversation with same container

  messages = [
      {"role": "user", "content": "Analyze this sales data"},
      {"role": "assistant", "content": response1.content},
      {"role": "user", "content": "What was the total revenue?"}
  ]

  response2 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "id": response1.container.id,  # Reuse container

          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=messages,
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
```
```typescript
  // First request creates container
  const response1 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages: [{role: 'user', content: 'Analyze this sales data'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Continue conversation with same container
  const messages = [
    {role: 'user', content: 'Analyze this sales data'},
    {role: 'assistant', content: response1.content},
    {role: 'user', content: 'What was the total revenue?'}
  ];

  const response2 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      id: response1.container.id,  // Reuse container
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages,
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
```

### Long-Running Operations

Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:
```python
  messages = [{"role": "user", "content": "Process this large dataset"}]
  max_retries = 10

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
          ]
      },
      messages=messages,
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Handle pause_turn for long operations

  for i in range(max_retries):
      if response.stop_reason != "pause_turn":
          break

      messages.append({"role": "assistant", "content": response.content})
      response = client.beta.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=4096,
          betas=["code-execution-2025-08-25", "skills-2025-10-02"],
          container={
              "id": response.container.id,
              "skills": [
                  {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
              ]
          },
          messages=messages,
          tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
      )
```
```typescript
  let messages = [{role: 'user' as const, content: 'Process this large dataset'}];
  const maxRetries = 10;

  let response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'custom', skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv', version: 'latest'}
      ]
    },
    messages,
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Handle pause_turn for long operations
  for (let i = 0; i < maxRetries; i++) {
    if (response.stop_reason !== 'pause_turn') {
      break;
    }

    messages.push({role: 'assistant', content: response.content});
    response = await client.beta.messages.create({
      model: 'claude-sonnet-4-5-20250929',
      max_tokens: 4096,
      betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
      container: {
        id: response.container.id,
        skills: [
          {type: 'custom', skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv', version: 'latest'}
        ]
      },
      messages,
      tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
    });
  }
```
```bash
  # Initial request

  RESPONSE=$(curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Process this large dataset"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }')

  # Check stop_reason and handle pause_turn in a loop

  STOP_REASON=$(echo "$RESPONSE" | jq -r '.stop_reason')
  CONTAINER_ID=$(echo "$RESPONSE" | jq -r '.container.id')

  while [ "$STOP_REASON" = "pause_turn" ]; do
    # Continue with same container

    RESPONSE=$(curl https://api.anthropic.com/v1/messages \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
      -H "content-type: application/json" \
      -d "{
        \"model\": \"claude-sonnet-4-5-20250929\",
        \"max_tokens\": 4096,
        \"container\": {
          \"id\": \"$CONTAINER_ID\",
          \"skills\": [{
            \"type\": \"custom\",
            \"skill_id\": \"skill_01AbCdEfGhIjKlMnOpQrStUv\",
            \"version\": \"latest\"
          }]
        },
        \"messages\": [/* include conversation history */],
        \"tools\": [{
          \"type\": \"code_execution_20250825\",
          \"name\": \"code_execution\"
        }]
      }")

    STOP_REASON=$(echo "$RESPONSE" | jq -r '.stop_reason')
  done
```javascript

>   **📝 Note**
>
> The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation and provide additional guidance.

### Using Multiple Skills

Combine multiple Skills in a single request to handle complex workflows:
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "xlsx",
                  "version": "latest"
              },
              {
                  "type": "anthropic",
                  "skill_id": "pptx",
                  "version": "latest"
              },
              {
                  "type": "custom",
                  "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Analyze sales data and create a presentation"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
```
```typescript
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'xlsx',
          version: 'latest'
        },
        {
          type: 'anthropic',
          skill_id: 'pptx',
          version: 'latest'
        },
        {
          type: 'custom',
          skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Analyze sales data and create a presentation'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
```
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "anthropic",
            "skill_id": "xlsx",
            "version": "latest"
          },
          {
            "type": "anthropic",
            "skill_id": "pptx",
            "version": "latest"
          },
          {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Analyze sales data and create a presentation"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
```

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
