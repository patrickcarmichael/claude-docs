---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Process PDFs with Claude

### Send your first PDF request

Let's start with a simple example using the Messages API. You can provide PDFs to Claude in three ways:

1. As a URL reference to a PDF hosted online
2. As a base64-encoded PDF in `document` content blocks
3. By a `file_id` from the [Files API](/en/docs/build-with-claude/files)

#### Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:
```bash
   curl https://api.anthropic.com/v1/messages \
     -H "content-type: application/json" \
     -H "x-api-key: $ANTHROPIC_API_KEY" \
     -H "anthropic-version: 2023-06-01" \
     -d '{
       "model": "claude-sonnet-4-5",
       "max_tokens": 1024,
       "messages": [{
           "role": "user",
           "content": [{
               "type": "document",
               "source": {
                   "type": "url",
                   "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
               }
           },
           {
               "type": "text",
               "text": "What are the key findings in this document?"
           }]
       }]
   }'
```
```Python
  import anthropic

  client = anthropic.Anthropic()
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "url",
                          "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
                      }
                  },
                  {
                      "type": "text",
                      "text": "What are the key findings in this document?"
                  }
              ]
          }
      ],
  )

  print(message.content)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'document',
              source: {
                type: 'url',
                url: 'https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf',
              },
            },
            {
              type: 'text',
              text: 'What are the key findings in this document?',
            },
          ],
        },
      ],
    });
    
    console.log(response);
  }

  main();
```
```java
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.*;

  public class PdfExample {
      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Create document block with URL
          DocumentBlockParam documentParam = DocumentBlockParam.builder()
                  .urlPdfSource("https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf")
                  .build();

          // Create a message with document and text content blocks
          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_4_20250514)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(
                          List.of(
                                  ContentBlockParam.ofDocument(documentParam),
                                  ContentBlockParam.ofText(
                                          TextBlockParam.builder()
                                                  .text("What are the key findings in this document?")
                                                  .build()
                                  )
                          )
                  )
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message.content());
      }
  }
```

#### Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn't available:
```bash
  # Method 1: Fetch and encode a remote PDF

  curl -s "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf" | base64 | tr -d '\n' > pdf_base64.txt

  # Method 2: Encode a local PDF file

  # base64 document.pdf | tr -d '\n' > pdf_base64.txt

  # Create a JSON request file using the pdf_base64.txt content

  jq -n --rawfile PDF_BASE64 pdf_base64.txt '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [{
          "role": "user",
          "content": [{
              "type": "document",
              "source": {
                  "type": "base64",
                  "media_type": "application/pdf",
                  "data": $PDF_BASE64
              }
          },
          {
              "type": "text",
              "text": "What are the key findings in this document?"
          }]
      }]
  }' > request.json

  # Send the API request using the JSON file

  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d @request.json
```
```Python
  import anthropic
  import base64
  import httpx

  # First, load and encode the PDF 

  pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
  pdf_data = base64.standard_b64encode(httpx.get(pdf_url).content).decode("utf-8")

  # Alternative: Load from a local file

  # with open("document.pdf", "rb") as f:

  #     pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

  # Send to Claude using base64 encoding

  client = anthropic.Anthropic()
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "base64",
                          "media_type": "application/pdf",
                          "data": pdf_data
                      }
                  },
                  {
                      "type": "text",
                      "text": "What are the key findings in this document?"
                  }
              ]
          }
      ],
  )

  print(message.content)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';
  import fetch from 'node-fetch';
  import fs from 'fs';

  async function main() {
    // Method 1: Fetch and encode a remote PDF
    const pdfURL = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf";
    const pdfResponse = await fetch(pdfURL);
    const arrayBuffer = await pdfResponse.arrayBuffer();
    const pdfBase64 = Buffer.from(arrayBuffer).toString('base64');
    
    // Method 2: Load from a local file
    // const pdfBase64 = fs.readFileSync('document.pdf').toString('base64');
    
    // Send the API request with base64-encoded PDF
    const anthropic = new Anthropic();
    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'document',
              source: {
                type: 'base64',
                media_type: 'application/pdf',
                data: pdfBase64,
              },
            },
            {
              type: 'text',
              text: 'What are the key findings in this document?',
            },
          ],
        },
      ],
    });
    
    console.log(response);
  }

  main();
```
```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.util.Base64;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.ContentBlockParam;
  import com.anthropic.models.messages.DocumentBlockParam;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;

  public class PdfExample {
      public static void main(String[] args) throws IOException, InterruptedException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Method 1: Download and encode a remote PDF
          String pdfUrl = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf";
          HttpClient httpClient = HttpClient.newHttpClient();
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(pdfUrl))
                  .GET()
                  .build();

          HttpResponse<byte[]> response = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray());
          String pdfBase64 = Base64.getEncoder().encodeToString(response.body());

          // Method 2: Load from a local file
          // byte[] fileBytes = Files.readAllBytes(Path.of("document.pdf"));
          // String pdfBase64 = Base64.getEncoder().encodeToString(fileBytes);

          // Create document block with base64 data
          DocumentBlockParam documentParam = DocumentBlockParam.builder()
                  .base64PdfSource(pdfBase64)
                  .build();

          // Create a message with document and text content blocks
          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_4_20250514)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(
                          List.of(
                                  ContentBlockParam.ofDocument(documentParam),
                                  ContentBlockParam.ofText(TextBlockParam.builder().text("What are the key findings in this document?").build())
                          )
                  )
                  .build();

          Message message = client.messages().create(params);
          message.content().stream()
                  .flatMap(contentBlock -> contentBlock.text().stream())
                  .forEach(textBlock -> System.out.println(textBlock.text()));
      }
  }
```

#### Option 3: Files API

For PDFs you'll use repeatedly, or when you want to avoid encoding overhead, use the [Files API](/en/docs/build-with-claude/files):
```bash
  # First, upload your PDF to the Files API

  curl -X POST https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -F "file=@document.pdf"

  # Then use the returned file_id in your message

  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -d '{
      "model": "claude-sonnet-4-5", 
      "max_tokens": 1024,
      "messages": [{
        "role": "user",
        "content": [{
          "type": "document",
          "source": {
            "type": "file",
            "file_id": "file_abc123"
          }
        },
        {
          "type": "text",
          "text": "What are the key findings in this document?"
        }]
      }]
    }'
```
```python
  import anthropic

  client = anthropic.Anthropic()

  # Upload the PDF file

  with open("document.pdf", "rb") as f:
      file_upload = client.beta.files.upload(file=("document.pdf", f, "application/pdf"))

  # Use the uploaded file in a message

  message = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      betas=["files-api-2025-04-14"],
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "file",
                          "file_id": file_upload.id
                      }
                  },
                  {
                      "type": "text",
                      "text": "What are the key findings in this document?"
                  }
              ]
          }
      ],
  )

  print(message.content)
```
```typescript
  import { Anthropic, toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const anthropic = new Anthropic();

  async function main() {
    // Upload the PDF file
    const fileUpload = await anthropic.beta.files.upload({
      file: toFile(fs.createReadStream('document.pdf'), undefined, { type: 'application/pdf' })
    }, {
      betas: ['files-api-2025-04-14']
    });

    // Use the uploaded file in a message
    const response = await anthropic.beta.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      betas: ['files-api-2025-04-14'],
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'document',
              source: {
                type: 'file',
                file_id: fileUpload.id
              }
            },
            {
              type: 'text',
              text: 'What are the key findings in this document?'
            }
          ]
        }
      ]
    });

    console.log(response);
  }

  main();
```
```java
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.File;
  import com.anthropic.models.files.FileUploadParams;
  import com.anthropic.models.messages.*;

  public class PdfFilesExample {
      public static void main(String[] args) throws IOException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Upload the PDF file
          File file = client.beta().files().upload(FileUploadParams.builder()
                  .file(Files.newInputStream(Path.of("document.pdf")))
                  .build());

          // Use the uploaded file in a message
          DocumentBlockParam documentParam = DocumentBlockParam.builder()
                  .fileSource(file.id())
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_4_20250514)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(
                          List.of(
                                  ContentBlockParam.ofDocument(documentParam),
                                  ContentBlockParam.ofText(
                                          TextBlockParam.builder()
                                                  .text("What are the key findings in this document?")
                                                  .build()
                                  )
                          )
                  )
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message.content());
      }
  }
```

### How PDF support works

When you send a PDF to Claude, the following steps occur:

<Steps>
  <Step title="The system extracts the contents of the document.">
    * The system converts each page of the document into an image.
    * The text from each page is extracted and provided alongside each page's image.
  </Step>

  <Step title="Claude analyzes both the text and images to better understand the document.">
    * Documents are provided as a combination of text and images for analysis.
    * This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.
  </Step>

  <Step title="Claude responds, referencing the PDF's contents if relevant.">
    Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

    * **Prompt caching**: To improve performance for repeated analysis.
    * **Batch processing**: For high-volume document processing.
    * **Tool use**: To extract specific information from documents for use as tool inputs.
  </Step>
</Steps>

### Estimate your costs

The token count of a PDF file depends on the total text extracted from the document as well as the number of pages:

* Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
* Image token costs: Since each page is converted into an image, the same [image-based cost calculations](/en/docs/build-with-claude/vision#evaluate-image-size) are applied.

You can use [token counting](/en/docs/build-with-claude/token-counting) to estimate costs for your specific PDFs.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
