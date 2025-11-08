---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Optimize PDF processing

### Improve performance

Follow these best practices for optimal results:

* Place PDFs before text in your requests
* Use standard fonts
* Ensure text is clear and legible
* Rotate pages to proper upright orientation
* Use logical page numbers (from PDF viewer) in prompts
* Split large PDFs into chunks when needed
* Enable prompt caching for repeated analysis

### Scale your implementation

For high-volume processing, consider these approaches:

#### Use prompt caching

Cache PDFs to improve performance on repeated queries:
```bash
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
              },
              "cache_control": {
                "type": "ephemeral"
              }
          },
          {
              "type": "text",
              "text": "Which model has the highest human preference win rates across each use-case?"
          }]
      }]
  }' > request.json

  # Then make the API call using the JSON file

  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d @request.json
```
```python
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
                      },
                      "cache_control": {"type": "ephemeral"}
                  },
                  {
                      "type": "text",
                      "text": "Analyze this document."
                  }
              ]
          }
      ],
  )
```
```TypeScript
  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      {
        content: [
          {
            type: 'document',
            source: {
              media_type: 'application/pdf',
              type: 'base64',
              data: pdfBase64,
            },
            cache_control: { type: 'ephemeral' },
          },
          {
            type: 'text',
            text: 'Which model has the highest human preference win rates across each use-case?',
          },
        ],
        role: 'user',
      },
    ],
  });
  console.log(response);
```
```java
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Paths;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.Base64PdfSource;
  import com.anthropic.models.messages.CacheControlEphemeral;
  import com.anthropic.models.messages.ContentBlockParam;
  import com.anthropic.models.messages.DocumentBlockParam;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;

  public class MessagesDocumentExample {

      public static void main(String[] args) throws IOException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Read PDF file as base64
          byte[] pdfBytes = Files.readAllBytes(Paths.get("pdf_base64.txt"));
          String pdfBase64 = new String(pdfBytes);

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_4_20250514)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(List.of(
                          ContentBlockParam.ofDocument(
                                  DocumentBlockParam.builder()
                                          .source(Base64PdfSource.builder()
                                                  .data(pdfBase64)
                                                  .build())
                                          .cacheControl(CacheControlEphemeral.builder().build())
                                          .build()),
                          ContentBlockParam.ofText(
                                  TextBlockParam.builder()
                                          .text("Which model has the highest human preference win rates across each use-case?")
                                          .build())
                  ))
                  .build();


          Message message = client.messages().create(params);
          System.out.println(message);
      }
  }
```

#### Process document batches

Use the Message Batches API for high-volume workflows:
```bash
  # Create a JSON request file using the pdf_base64.txt content

  jq -n --rawfile PDF_BASE64 pdf_base64.txt '
  {
    "requests": [
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [
                  {
                      "role": "user",
                      "content": [
                          {
                              "type": "document",
                              "source": {
                                  "type": "base64",
                                  "media_type": "application/pdf",
                                  "data": $PDF_BASE64
                              }
                          },
                          {
                              "type": "text",
                              "text": "Which model has the highest human preference win rates across each use-case?"
                          }
                      ]
                  }
                ]
            }
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [
                  {
                      "role": "user",
                      "content": [
                          {
                              "type": "document",
                              "source": {
                                  "type": "base64",
                                  "media_type": "application/pdf",
                                  "data": $PDF_BASE64
                              }
                          },
                          {
                              "type": "text",
                              "text": "Extract 5 key insights from this document."
                          }
                      ]
                  }
                ]
            }
        }
    ]
  }
  ' > request.json

  # Then make the API call using the JSON file

  curl https://api.anthropic.com/v1/messages/batches \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d @request.json
```
```python
  message_batch = client.messages.batches.create(
      requests=[
          {
              "custom_id": "doc1",
              "params": {
                  "model": "claude-sonnet-4-5",
                  "max_tokens": 1024,
                  "messages": [
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
                                  "text": "Summarize this document."
                              }
                          ]
                      }
                  ]
              }
          }
      ]
  )
```
```TypeScript
  const response = await anthropic.messages.batches.create({
    requests: [
      {
        custom_id: 'my-first-request',
        params: {
          max_tokens: 1024,
          messages: [
            {
              content: [
                {
                  type: 'document',
                  source: {
                    media_type: 'application/pdf',
                    type: 'base64',
                    data: pdfBase64,
                  },
                },
                {
                  type: 'text',
                  text: 'Which model has the highest human preference win rates across each use-case?',
                },
              ],
              role: 'user',
            },
          ],
          model: 'claude-sonnet-4-5',
        },
      },
      {
        custom_id: 'my-second-request',
        params: {
          max_tokens: 1024,
          messages: [
            {
              content: [
                {
                  type: 'document',
                  source: {
                    media_type: 'application/pdf',
                    type: 'base64',
                    data: pdfBase64,
                  },
                },
                {
                  type: 'text',
                  text: 'Extract 5 key insights from this document.',
                },
              ],
              role: 'user',
            },
          ],
          model: 'claude-sonnet-4-5',
        },
      }
    ],
  });
  console.log(response);
```
```java
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Paths;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;
  import com.anthropic.models.messages.batches.*;

  public class MessagesBatchDocumentExample {

      public static void main(String[] args) throws IOException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Read PDF file as base64
          byte[] pdfBytes = Files.readAllBytes(Paths.get("pdf_base64.txt"));
          String pdfBase64 = new String(pdfBytes);

          BatchCreateParams params = BatchCreateParams.builder()
                  .addRequest(BatchCreateParams.Request.builder()
                          .customId("my-first-request")
                          .params(BatchCreateParams.Request.Params.builder()
                                  .model(Model.CLAUDE_OPUS_4_20250514)
                                  .maxTokens(1024)
                                  .addUserMessageOfBlockParams(List.of(
                                          ContentBlockParam.ofDocument(
                                                  DocumentBlockParam.builder()
                                                          .source(Base64PdfSource.builder()
                                                                  .data(pdfBase64)
                                                                  .build())
                                                          .build()
                                          ),
                                          ContentBlockParam.ofText(
                                                  TextBlockParam.builder()
                                                          .text("Which model has the highest human preference win rates across each use-case?")
                                                          .build()
                                          )
                                  ))
                                  .build())
                          .build())
                  .addRequest(BatchCreateParams.Request.builder()
                          .customId("my-second-request")
                          .params(BatchCreateParams.Request.Params.builder()
                                  .model(Model.CLAUDE_OPUS_4_20250514)
                                  .maxTokens(1024)
                                  .addUserMessageOfBlockParams(List.of(
                                          ContentBlockParam.ofDocument(
                                          DocumentBlockParam.builder()
                                                  .source(Base64PdfSource.builder()
                                                          .data(pdfBase64)
                                                          .build())
                                                  .build()
                                          ),
                                          ContentBlockParam.ofText(
                                                  TextBlockParam.builder()
                                                          .text("Extract 5 key insights from this document.")
                                                          .build()
                                          )
                                  ))
                                  .build())
                          .build())
                  .build();

          MessageBatch batch = client.messages().batches().create(params);
          System.out.println(batch);
      }
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
