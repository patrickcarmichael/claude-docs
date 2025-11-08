---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use the Files API

>   **📝 Note**
>
> To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

### Uploading a file

Upload a file to be referenced in future API calls:
```bash
  curl -X POST https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -F "file=@/path/to/document.pdf"
```
```python
  import anthropic

  client = anthropic.Anthropic()
  client.beta.files.upload(
    file=("document.pdf", open("/path/to/document.pdf", "rb"), "application/pdf"),
  )
```
```typescript
  import Anthropic, { toFile } from '@anthropic-ai/sdk';
  import fs from "fs";

  const anthropic = new Anthropic();

  await anthropic.beta.files.upload({
    file: await toFile(fs.createReadStream('/path/to/document.pdf'), undefined, { type: 'application/pdf' })
  }, {
    betas: ['files-api-2025-04-14']
  });
```

The response from uploading a file will include:
```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1024000,
  "created_at": "2025-01-01T00:00:00Z",
  "downloadable": false
}
```

### Using a file in messages

Once uploaded, reference the file using its `file_id`:
```bash
  curl -X POST https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Please summarize this document for me."          
            },
            {
              "type": "document",
              "source": {
                "type": "file",
                "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
              }
            }
          ]
        }
      ]
    }'
```
```python
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Please summarize this document for me."
                  },
                  {
                      "type": "document",
                      "source": {
                          "type": "file",
                          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
                      }
                  }
              ]
          }
      ],
      betas=["files-api-2025-04-14"],
  )
  print(response)
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Please summarize this document for me."
          },
          {
            type: "document",
            source: {
              type: "file",
              file_id: "file_011CNha8iCJcU1wXNR6q4V8w"
            }
          }
        ]
      }
    ],
    betas: ["files-api-2025-04-14"],
  });

  console.log(response);
```

### File types and content blocks

The Files API supports different file types that correspond to different content block types:

| File Type                                                                                       | MIME Type                                            | Content Block Type | Use Case                            |
| :---------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :----------------- | :---------------------------------- |
| PDF                                                                                             | `application/pdf`                                    | `document`         | Text analysis, document processing  |
| Plain text                                                                                      | `text/plain`                                         | `document`         | Text analysis, processing           |
| Images                                                                                          | `image/jpeg`, `image/png`, `image/gif`, `image/webp` | `image`            | Image analysis, visual tasks        |
| [Datasets, others](/en/docs/agents-and-tools/tool-use/code-execution-tool#supported-file-types) | Varies                                               | `container_upload` | Analyze data, create visualizations |

### Working with other file formats

For file types that are not supported as `document` blocks (.csv, .txt, .md, .docx, .xlsx), convert the files to plain text, and include the content directly in your message:
```bash
  # Example: Reading a text file and sending it as plain text

  # Note: For files with special characters, consider base64 encoding

  TEXT_CONTENT=$(cat document.txt | jq -Rs .)

  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d @- <<EOF
  {
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Here's the document content:\n\n${TEXT_CONTENT}\n\nPlease summarize this document."
          }
        ]
      }
    ]
  }
  EOF
```
```python
  import pandas as pd
  import anthropic

  client = anthropic.Anthropic()

  # Example: Reading a CSV file

  df = pd.read_csv('data.csv')
  csv_content = df.to_string()

  # Send as plain text in the message

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": f"Here's the CSV data:\n\n{csv_content}\n\nPlease analyze this data."
                  }
              ]
          }
      ]
  )

  print(response.content[0].text)
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const anthropic = new Anthropic();

  async function analyzeDocument() {
    // Example: Reading a text file
    const textContent = fs.readFileSync('document.txt', 'utf-8');

    // Send as plain text in the message
    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'text',
              text: `Here's the document content:\n\n${textContent}\n\nPlease summarize this document.`
            }
          ]
        }
      ]
    });

    console.log(response.content[0].text);
  }

  analyzeDocument();
```

>   **📝 Note**
>
> For .docx files containing images, convert them to PDF format first, then use [PDF support](/en/docs/build-with-claude/pdf-support) to take advantage of the built-in image parsing. This allows using citations from the PDF document.

#### Document blocks

For PDFs and text files, use the `document` content block:
```json
{
  "type": "document",
  "source": {
    "type": "file",
    "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
  },
  "title": "Document Title", // Optional
  "context": "Context about the document", // Optional  
  "citations": {"enabled": true} // Optional, enables citations
}
```

#### Image blocks

For images, use the `image` content block:
```json
{
  "type": "image",
  "source": {
    "type": "file",
    "file_id": "file_011CPMxVD3fHLUhvTqtsQA5w"
  }
}
```

### Managing files

#### List files

Retrieve a list of your uploaded files:
```bash
  curl https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"
```
```python
  import anthropic

  client = anthropic.Anthropic()
  files = client.beta.files.list()
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();
  const files = await anthropic.beta.files.list({
    betas: ['files-api-2025-04-14'],
  });
```

#### Get file metadata

Retrieve information about a specific file:
```bash
  curl https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"
```
```python
  import anthropic

  client = anthropic.Anthropic()
  file = client.beta.files.retrieve_metadata("file_011CNha8iCJcU1wXNR6q4V8w")
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();
  const file = await anthropic.beta.files.retrieveMetadata(
    "file_011CNha8iCJcU1wXNR6q4V8w",
    { betas: ['files-api-2025-04-14'] },
  );
```

#### Delete a file

Remove a file from your workspace:
```bash
  curl -X DELETE https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"
```
```python
  import anthropic

  client = anthropic.Anthropic()
  result = client.beta.files.delete("file_011CNha8iCJcU1wXNR6q4V8w")
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();
  const result = await anthropic.beta.files.delete(
    "file_011CNha8iCJcU1wXNR6q4V8w",
    { betas: ['files-api-2025-04-14'] },
  );
```

### Downloading a file

Download files that have been created by skills or the code execution tool:
```bash
  curl -X GET "https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    --output downloaded_file.txt
```
```python
  import anthropic

  client = anthropic.Anthropic()
  file_content = client.beta.files.download("file_011CNha8iCJcU1wXNR6q4V8w")

  # Save to file

  with open("downloaded_file.txt", "w") as f:
      f.write(file_content.decode('utf-8'))
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const anthropic = new Anthropic();

  const fileContent = await anthropic.beta.files.download(
    "file_011CNha8iCJcU1wXNR6q4V8w",
    { betas: ['files-api-2025-04-14'] },
  );

  // Save to file
  fs.writeFileSync("downloaded_file.txt", fileContent);
```

>   **📝 Note**
>
> You can only download files that were created by [skills](/en/docs/build-with-claude/skills-guide) or the [code execution tool](/en/docs/agents-and-tools/tool-use/code-execution-tool). Files that you uploaded cannot be downloaded.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
