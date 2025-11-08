---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Download the created file

The presentation was created in the code execution container and saved as a file. The response includes a file reference with a file ID. Extract the file ID and download it using the Files API:
```python
  # Extract file ID from response

  file_id = None
  for block in response.content:
      if block.type == 'tool_use' and block.name == 'code_execution':
          # File ID is in the tool result

          for result_block in block.content:
              if hasattr(result_block, 'file_id'):
                  file_id = result_block.file_id
                  break

  if file_id:
      # Download the file

      file_content = client.beta.files.download(
          file_id=file_id,
          betas=["files-api-2025-04-14"]
      )

      # Save to disk

      with open("renewable_energy.pptx", "wb") as f:
          file_content.write_to_file(f.name)

      print(f"Presentation saved to renewable_energy.pptx")
```
```typescript
  // Extract file ID from response
  let fileId: string | null = null;
  for (const block of response.content) {
    if (block.type === 'tool_use' && block.name === 'code_execution') {
      // File ID is in the tool result
      for (const resultBlock of block.content) {
        if ('file_id' in resultBlock) {
          fileId = resultBlock.file_id;
          break;
        }
      }
    }
  }

  if (fileId) {
    // Download the file
    const fileContent = await client.beta.files.download(fileId, {
      betas: ['files-api-2025-04-14']
    });

    // Save to disk
    const fs = require('fs');
    fs.writeFileSync('renewable_energy.pptx', Buffer.from(await fileContent.arrayBuffer()));

    console.log('Presentation saved to renewable_energy.pptx');
  }
```
```bash
  # Extract file_id from response (using jq)

  FILE_ID=$(echo "$RESPONSE" | jq -r '.content[] | select(.type=="tool_use" and .name=="code_execution") | .content[] | select(.file_id) | .file_id')

  # Download the file

  curl "https://api.anthropic.com/v1/files/$FILE_ID/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    --output renewable_energy.pptx

  echo "Presentation saved to renewable_energy.pptx"
```

>   **📝 Note**
>
> For complete details on working with generated files, see the [code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
