**Navigation:** [← Previous](./06-text-editor-tool.md) | [Index](./index.md) | [Next →](./08-building-with-extended-thinking.md)

---

# Citations
Source: https://docs.claude.com/en/docs/build-with-claude/citations



Claude is capable of providing detailed citations when answering questions about documents, helping you track and verify information sources in responses.

All [active models](/en/docs/about-claude/models/overview) support citations, with the exception of Haiku 3.

<Warning>
  *Citations with Claude Sonnet 3.7*

  Claude Sonnet 3.7 may be less likely to make citations compared to other Claude models without more explicit instructions from the user. When using citations with Claude Sonnet 3.7, we recommend including additional instructions in the `user` turn, like `"Use citations to back up your answer."` for example.

  We've also observed that when the model is asked to structure its response, it is unlikely to use citations unless explicitly told to use citations within that format. For example, if the model is asked to use `<result>` tags in its response, you should add something like `"Always use citations in your answer, even within <result> tags."`
</Warning>

<Tip>
  Please share your feedback and suggestions about the citations feature using this [form](https://forms.gle/9n9hSrKnKe3rpowH9).
</Tip>

Here's an example of how to use citations with the Messages API:

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "document",
              "source": {
                "type": "text",
                "media_type": "text/plain",
                "data": "The grass is green. The sky is blue."
              },
              "title": "My Document",
              "context": "This is a trustworthy document.",
              "citations": {"enabled": true}
            },
            {
              "type": "text",
              "text": "What color is the grass and sky?"
            }
          ]
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
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "text",
                          "media_type": "text/plain",
                          "data": "The grass is green. The sky is blue."
                      },
                      "title": "My Document",
                      "context": "This is a trustworthy document.",
                      "citations": {"enabled": True}
                  },
                  {
                      "type": "text",
                      "text": "What color is the grass and sky?"
                  }
              ]
          }
      ]
  )
  print(response)
  ```

  ```java Java theme={null}
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;

  public class DocumentExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          PlainTextSource source = PlainTextSource.builder()
                  .data("The grass is green. The sky is blue.")
                  .build();

          DocumentBlockParam documentParam = DocumentBlockParam.builder()
                  .source(source)
                  .title("My Document")
                  .context("This is a trustworthy document.")
                  .citations(CitationsConfigParam.builder().enabled(true).build())
                  .build();
          
          TextBlockParam textBlockParam = TextBlockParam.builder()
                  .text("What color is the grass and sky?")
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(List.of(ContentBlockParam.ofDocument(documentParam), ContentBlockParam.ofText(textBlockParam)))
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message);
      }
  }
  ```
</CodeGroup>

<Tip>
  **Comparison with prompt-based approaches**

  In comparison with prompt-based citations solutions, the citations feature has the following advantages:

  * **Cost savings:** If your prompt-based approach asks Claude to output direct quotes, you may see cost savings due to the fact that `cited_text` does not count towards your output tokens.
  * **Better citation reliability:** Because we parse citations into the respective response formats mentioned above and extract `cited_text`, citations are guaranteed to contain valid pointers to the provided documents.
  * **Improved citation quality:** In our evals, we found the citations feature to be significantly more likely to cite the most relevant quotes from documents as compared to purely prompt-based approaches.
</Tip>

***

## How citations work

Integrate citations with Claude in these steps:

<Steps>
  <Step title="Provide document(s) and enable citations">
    * Include documents in any of the supported formats: [PDFs](#pdf-documents), [plain text](#plain-text-documents), or [custom content](#custom-content-documents) documents
    * Set `citations.enabled=true` on each of your documents. Currently, citations must be enabled on all or none of the documents within a request.
    * Note that only text citations are currently supported and image citations are not yet possible.
  </Step>

  <Step title="Documents get processed">
    * Document contents are "chunked" in order to define the minimum granularity of possible citations. For example, sentence chunking would allow Claude to cite a single sentence or chain together multiple consecutive sentences to cite a paragraph (or longer)!
      * **For PDFs:** Text is extracted as described in [PDF Support](/en/docs/build-with-claude/pdf-support) and content is chunked into sentences. Citing images from PDFs is not currently supported.
      * **For plain text documents:** Content is chunked into sentences that can be cited from.
      * **For custom content documents:** Your provided content blocks are used as-is and no further chunking is done.
  </Step>

  <Step title="Claude provides cited response">
    * Responses may now include multiple text blocks where each text block can contain a claim that Claude is making and a list of citations that support the claim.
    * Citations reference specific locations in source documents. The format of these citations are dependent on the type of document being cited from.
      * **For PDFs:** citations will include the page number range (1-indexed).
      * **For plain text documents:** Citations will include the character index range (0-indexed).
      * **For custom content documents:** Citations will include the content block index range (0-indexed) corresponding to the original content list provided.
    * Document indices are provided to indicate the reference source and are 0-indexed according to the list of all documents in your original request.
  </Step>
</Steps>

<Tip>
  **Automatic chunking vs custom content**

  By default, plain text and PDF documents are automatically chunked into sentences. If you need more control over citation granularity (e.g., for bullet points or transcripts), use custom content documents instead. See [Document Types](#document-types) for more details.

  For example, if you want Claude to be able to cite specific sentences from your RAG chunks, you should put each RAG chunk into a plain text document. Otherwise, if you do not want any further chunking to be done, or if you want to customize any additional chunking, you can put RAG chunks into custom content document(s).
</Tip>

### Citable vs non-citable content

* Text found within a document's `source` content can be cited from.
* `title` and `context` are optional fields that will be passed to the model but not used towards cited content.
* `title` is limited in length so you may find the `context` field to be useful in storing any document metadata as text or stringified json.

### Citation indices

* Document indices are 0-indexed from the list of all document content blocks in the request (spanning across all messages).
* Character indices are 0-indexed with exclusive end indices.
* Page numbers are 1-indexed with exclusive end page numbers.
* Content block indices are 0-indexed with exclusive end indices from the `content` list provided in the custom content document.

### Token costs

* Enabling citations incurs a slight increase in input tokens due to system prompt additions and document chunking.
* However, the citations feature is very efficient with output tokens. Under the hood, the model is outputting citations in a standardized format that are then parsed into cited text and document location indices. The `cited_text` field is provided for convenience and does not count towards output tokens.
* When passed back in subsequent conversation turns, `cited_text` is also not counted towards input tokens.

### Feature compatibility

Citations works in conjunction with other API features including [prompt caching](/en/docs/build-with-claude/prompt-caching), [token counting](/en/docs/build-with-claude/token-counting) and [batch processing](/en/docs/build-with-claude/batch-processing).

#### Using Prompt Caching with Citations

Citations and prompt caching can be used together effectively.

The citation blocks generated in responses cannot be cached directly, but the source documents they reference can be cached. To optimize performance, apply `cache_control` to your top-level document content blocks.

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Long document content (e.g., technical documentation)
  long_document = "This is a very long document with thousands of words..." + " ... " * 1000  # Minimum cacheable length

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "text",
                          "media_type": "text/plain",
                          "data": long_document
                      },
                      "citations": {"enabled": True},
                      "cache_control": {"type": "ephemeral"}  # Cache the document content
                  },
                  {
                      "type": "text",
                      "text": "What does this document say about API features?"
                  }
              ]
          }
      ]
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  // Long document content (e.g., technical documentation)
  const longDocument = "This is a very long document with thousands of words..." + " ... ".repeat(1000);  // Minimum cacheable length

  const response = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "document",
            source: {
              type: "text",
              media_type: "text/plain",
              data: longDocument
            },
            citations: { enabled: true },
            cache_control: { type: "ephemeral" }  // Cache the document content
          },
          {
            type: "text",
            text: "What does this document say about API features?"
          }
        ]
      }
    ]
  });
  ```

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
              "content": [
                  {
                      "type": "document",
                      "source": {
                          "type": "text",
                          "media_type": "text/plain",
                          "data": "This is a very long document with thousands of words..."
                      },
                      "citations": {"enabled": true},
                      "cache_control": {"type": "ephemeral"}
                  },
                  {
                      "type": "text",
                      "text": "What does this document say about API features?"
                  }
              ]
          }
      ]
  }'
  ```
</CodeGroup>

In this example:

* The document content is cached using `cache_control` on the document block
* Citations are enabled on the document
* Claude can generate responses with citations while benefiting from cached document content
* Subsequent requests using the same document will benefit from the cached content

## Document Types

### Choosing a document type

We support three document types for citations. Documents can be provided directly in the message (base64, text, or URL) or uploaded via the [Files API](/en/docs/build-with-claude/files) and referenced by `file_id`:

| Type           | Best for                                                        | Chunking               | Citation format               |
| :------------- | :-------------------------------------------------------------- | :--------------------- | :---------------------------- |
| Plain text     | Simple text documents, prose                                    | Sentence               | Character indices (0-indexed) |
| PDF            | PDF files with text content                                     | Sentence               | Page numbers (1-indexed)      |
| Custom content | Lists, transcripts, special formatting, more granular citations | No additional chunking | Block indices (0-indexed)     |

<Note>
  .csv, .xlsx, .docx, .md, and .txt files are not supported as document blocks. Convert these to plain text and include directly in message content. See [Working with other file formats](/en/docs/build-with-claude/files#working-with-other-file-formats).
</Note>

### Plain text documents

Plain text documents are automatically chunked into sentences. You can provide them inline or by reference with their `file_id`:

<Tabs>
  <Tab title="Inline text">
    ```python  theme={null}
    {
        "type": "document",
        "source": {
            "type": "text",
            "media_type": "text/plain",
            "data": "Plain text content..."
        },
        "title": "Document Title", # optional
        "context": "Context about the document that will not be cited from", # optional
        "citations": {"enabled": True}
    }
    ```
  </Tab>

  <Tab title="Files API">
    ```python  theme={null}
    {
        "type": "document",
        "source": {
            "type": "file",
            "file_id": "file_011CNvxoj286tYUAZFiZMf1U"
        },
        "title": "Document Title", # optional
        "context": "Context about the document that will not be cited from", # optional
        "citations": {"enabled": True}
    }
    ```
  </Tab>
</Tabs>

<Accordion title="Example plain text citation">
  ```python  theme={null}
  {
      "type": "char_location",
      "cited_text": "The exact text being cited", # not counted towards output tokens
      "document_index": 0,
      "document_title": "Document Title",
      "start_char_index": 0,    # 0-indexed
      "end_char_index": 50      # exclusive
  }
  ```
</Accordion>

### PDF documents

PDF documents can be provided as base64-encoded data or by `file_id`. PDF text is extracted and chunked into sentences. As image citations are not yet supported, PDFs that are scans of documents and do not contain extractable text will not be citable.

<Tabs>
  <Tab title="Base64">
    ```python  theme={null}
    {
        "type": "document",
        "source": {
            "type": "base64",
            "media_type": "application/pdf",
            "data": base64_encoded_pdf_data
        },
        "title": "Document Title", # optional
        "context": "Context about the document that will not be cited from", # optional
        "citations": {"enabled": True}
    }
    ```
  </Tab>

  <Tab title="Files API">
    ```python  theme={null}
    {
        "type": "document",
        "source": {
            "type": "file",
            "file_id": "file_011CNvxoj286tYUAZFiZMf1U"
        },
        "title": "Document Title", # optional
        "context": "Context about the document that will not be cited from", # optional
        "citations": {"enabled": True}
    }
    ```
  </Tab>
</Tabs>

<Accordion title="Example PDF citation">
  ```python  theme={null}
  {
      "type": "page_location",
      "cited_text": "The exact text being cited", # not counted towards output tokens
      "document_index": 0,     
      "document_title": "Document Title", 
      "start_page_number": 1,  # 1-indexed
      "end_page_number": 2     # exclusive
  }
  ```
</Accordion>

### Custom content documents

Custom content documents give you control over citation granularity. No additional chunking is done and chunks are provided to the model according to the content blocks provided.

```python  theme={null}
{
    "type": "document",
    "source": {
        "type": "content",
        "content": [
            {"type": "text", "text": "First chunk"},
            {"type": "text", "text": "Second chunk"}
        ]
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

<Accordion title="Example citation">
  ```python  theme={null}
  {
      "type": "content_block_location",
      "cited_text": "The exact text being cited", # not counted towards output tokens
      "document_index": 0,
      "document_title": "Document Title",
      "start_block_index": 0,   # 0-indexed
      "end_block_index": 1      # exclusive
  }
  ```
</Accordion>

***

## Response Structure

When citations are enabled, responses include multiple text blocks with citations:

```python  theme={null}
{
    "content": [
        {
            "type": "text",
            "text": "According to the document, "
        },
        {
            "type": "text",
            "text": "the grass is green",
            "citations": [{
                "type": "char_location",
                "cited_text": "The grass is green.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 0,
                "end_char_index": 20
            }]
        },
        {
            "type": "text",
            "text": " and "
        },
        {
            "type": "text",
            "text": "the sky is blue",
            "citations": [{
                "type": "char_location",
                "cited_text": "The sky is blue.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 20,
                "end_char_index": 36
            }]
        },
        {
            "type": "text",
            "text": ". Information from page 5 states that ",
        },
        {
            "type": "text",
            "text": "water is essential",
            "citations": [{
                "type": "page_location",
                "cited_text": "Water is essential for life.",
                "document_index": 1,
                "document_title": "PDF Document",
                "start_page_number": 5,
                "end_page_number": 6
            }]
        },
        {
            "type": "text",
            "text": ". The custom document mentions ",
        },
        {
            "type": "text",
            "text": "important findings",
            "citations": [{
                "type": "content_block_location",
                "cited_text": "These are important findings.",
                "document_index": 2,
                "document_title": "Custom Content Document",
                "start_block_index": 0,
                "end_block_index": 1
            }]
        }
    ]
}
```

### Streaming Support

For streaming responses, we've added a `citations_delta` type that contains a single citation to be added to the `citations` list on the current `text` content block.

<AccordionGroup>
  <Accordion title="Example streaming events">
    ```python  theme={null}
    event: message_start
    data: {"type": "message_start", ...}

    event: content_block_start
    data: {"type": "content_block_start", "index": 0, ...}

    event: content_block_delta
    data: {"type": "content_block_delta", "index": 0, 
           "delta": {"type": "text_delta", "text": "According to..."}}

    event: content_block_delta
    data: {"type": "content_block_delta", "index": 0,
           "delta": {"type": "citations_delta", 
                     "citation": {
                         "type": "char_location",
                         "cited_text": "...",
                         "document_index": 0,
                         ...
                     }}}

    event: content_block_stop
    data: {"type": "content_block_stop", "index": 0}

    event: message_stop
    data: {"type": "message_stop"}
    ```
  </Accordion>
</AccordionGroup>


# Claude Code Analytics API
Source: https://docs.claude.com/en/docs/build-with-claude/claude-code-analytics-api

Programmatically access your organization's Claude Code usage analytics and productivity metrics with the Claude Code Analytics Admin API.

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>

The Claude Code Analytics Admin API provides programmatic access to daily aggregated usage metrics for Claude Code users, enabling organizations to analyze developer productivity and build custom dashboards. This API bridges the gap between our basic [Analytics dashboard](https://console.anthropic.com/claude-code) and the complex OpenTelemetry integration.

This API enables you to better monitor, analyze, and optimize your Claude Code adoption:

* **Developer Productivity Analysis:** Track sessions, lines of code added/removed, commits, and pull requests created using Claude Code
* **Tool Usage Metrics:** Monitor acceptance and rejection rates for different Claude Code tools (Edit, Write, NotebookEdit)
* **Cost Analysis:** View estimated costs and token usage broken down by Claude model
* **Custom Reporting:** Export data to build executive dashboards and reports for management teams
* **Usage Justification:** Provide metrics to justify and expand Claude Code adoption internally

<Check>
  **Admin API key required**

  This API is part of the [Admin API](/en/docs/build-with-claude/administration-api). These endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the [Claude Console](https://console.anthropic.com/settings/admin-keys).
</Check>

## Quick start

Get your organization's Claude Code analytics for a specific day:

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
limit=20" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

<Tip>
  **Set a User-Agent header for integrations**

  If you're building an integration, set your User-Agent header to help us understand usage patterns:

  ```
  User-Agent: YourApp/1.0.0 (https://yourapp.com)
  ```
</Tip>

## Claude Code Analytics API

Track Claude Code usage, productivity metrics, and developer activity across your organization with the `/v1/organizations/usage_report/claude_code` endpoint.

### Key concepts

* **Daily aggregation**: Returns metrics for a single day specified by the `starting_at` parameter
* **User-level data**: Each record represents one user's activity for the specified day
* **Productivity metrics**: Track sessions, lines of code, commits, pull requests, and tool usage
* **Token and cost data**: Monitor usage and estimated costs broken down by Claude model
* **Cursor-based pagination**: Handle large datasets with stable pagination using opaque cursors
* **Data freshness**: Metrics are available with up to 1-hour delay for consistency

For complete parameter details and response schemas, see the [Claude Code Analytics API reference](/en/api/admin-api/claude-code/get-claude-code-usage-report).

### Basic examples

#### Get analytics for a specific day

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

#### Get analytics with pagination

```bash  theme={null}
# First request
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
limit=20" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"

# Subsequent request using cursor from response
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
page=page_MjAyNS0wNS0xNFQwMDowMDowMFo=" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

### Request parameters

| Parameter     | Type    | Required | Description                                                             |
| ------------- | ------- | -------- | ----------------------------------------------------------------------- |
| `starting_at` | string  | Yes      | UTC date in YYYY-MM-DD format. Returns metrics for this single day only |
| `limit`       | integer | No       | Number of records per page (default: 20, max: 1000)                     |
| `page`        | string  | No       | Opaque cursor token from previous response's `next_page` field          |

### Available metrics

Each response record contains the following metrics for a single user on a single day:

#### Dimensions

* **date**: Date in RFC 3339 format (UTC timestamp)
* **actor**: The user or API key that performed the Claude Code actions (either `user_actor` with `email_address` or `api_actor` with `api_key_name`)
* **organization\_id**: Organization UUID
* **customer\_type**: Type of customer account (`api` for API customers, `subscription` for Pro/Team customers)
* **terminal\_type**: Type of terminal or environment where Claude Code was used (e.g., `vscode`, `iTerm.app`, `tmux`)

#### Core metrics

* **num\_sessions**: Number of distinct Claude Code sessions initiated by this actor
* **lines\_of\_code.added**: Total number of lines of code added across all files by Claude Code
* **lines\_of\_code.removed**: Total number of lines of code removed across all files by Claude Code
* **commits\_by\_claude\_code**: Number of git commits created through Claude Code's commit functionality
* **pull\_requests\_by\_claude\_code**: Number of pull requests created through Claude Code's PR functionality

#### Tool action metrics

Breakdown of tool action acceptance and rejection rates by tool type:

* **edit\_tool.accepted/rejected**: Number of Edit tool proposals that the user accepted/rejected
* **write\_tool.accepted/rejected**: Number of Write tool proposals that the user accepted/rejected
* **notebook\_edit\_tool.accepted/rejected**: Number of NotebookEdit tool proposals that the user accepted/rejected

#### Model breakdown

For each Claude model used:

* **model**: Claude model identifier (e.g., `claude-sonnet-4-5-20250929`)
* **tokens.input/output**: Input and output token counts for this model
* **tokens.cache\_read/cache\_creation**: Cache-related token usage for this model
* **estimated\_cost.amount**: Estimated cost in cents USD for this model
* **estimated\_cost.currency**: Currency code for the cost amount (currently always `USD`)

### Response structure

The API returns data in the following format:

```json  theme={null}
{
  "data": [
    {
      "date": "2025-09-01T00:00:00Z",
      "actor": {
        "type": "user_actor",
        "email_address": "developer@company.com"
      },
      "organization_id": "dc9f6c26-b22c-4831-8d01-0446bada88f1",
      "customer_type": "api",
      "terminal_type": "vscode",
      "core_metrics": {
        "num_sessions": 5,
        "lines_of_code": {
          "added": 1543,
          "removed": 892
        },
        "commits_by_claude_code": 12,
        "pull_requests_by_claude_code": 2
      },
      "tool_actions": {
        "edit_tool": {
          "accepted": 45,
          "rejected": 5
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 3,
          "rejected": 0
        }
      },
      "model_breakdown": [
        {
          "model": "claude-sonnet-4-5-20250929",
          "tokens": {
            "input": 100000,
            "output": 35000,
            "cache_read": 10000,
            "cache_creation": 5000
          },
          "estimated_cost": {
            "currency": "USD",
            "amount": 1025
          }
        }
      ]
    }
  ],
  "has_more": false,
  "next_page": null
}
```

## Pagination

The API supports cursor-based pagination for organizations with large numbers of users:

1. Make your initial request with optional `limit` parameter
2. If `has_more` is `true` in the response, use the `next_page` value in your next request
3. Continue until `has_more` is `false`

The cursor encodes the position of the last record and ensures stable pagination even as new data arrives. Each pagination session maintains a consistent data boundary to ensure you don't miss or duplicate records.

## Common use cases

* **Executive dashboards**: Create high-level reports showing Claude Code impact on development velocity
* **AI tool comparison**: Export metrics to compare Claude Code with other AI coding tools like Copilot and Cursor
* **Developer productivity analysis**: Track individual and team productivity metrics over time
* **Cost tracking and allocation**: Monitor spending patterns and allocate costs by team or project
* **Adoption monitoring**: Identify which teams and users are getting the most value from Claude Code
* **ROI justification**: Provide concrete metrics to justify and expand Claude Code adoption internally

## Frequently asked questions

### How fresh is the analytics data?

Claude Code analytics data typically appears within 1 hour of user activity completion. To ensure consistent pagination results, only data older than 1 hour is included in responses.

### Can I get real-time metrics?

No, this API provides daily aggregated metrics only. For real-time monitoring, consider using the [OpenTelemetry integration](https://code.claude.com/docs/monitoring-usage).

### How are users identified in the data?

Users are identified through the `actor` field in two ways:

* **`user_actor`**: Contains `email_address` for users who authenticate via OAuth (most common)
* **`api_actor`**: Contains `api_key_name` for users who authenticate via API key

The `customer_type` field indicates whether the usage is from `api` customers (API PAYG) or `subscription` customers (Pro/Team plans).

### What's the data retention period?

Historical Claude Code analytics data is retained and accessible through the API. There is no specified deletion period for this data.

### Which Claude Code deployments are supported?

This API only tracks Claude Code usage on the Claude API (1st party). Usage on Amazon Bedrock, Google Vertex AI, or other third-party platforms is not included.

### What does it cost to use this API?

The Claude Code Analytics API is free to use for all organizations with access to the Admin API.

### How do I calculate tool acceptance rates?

Tool acceptance rate = `accepted / (accepted + rejected)` for each tool type. For example, if the edit tool shows 45 accepted and 5 rejected, the acceptance rate is 90%.

### What time zone is used for the date parameter?

All dates are in UTC. The `starting_at` parameter should be in YYYY-MM-DD format and represents UTC midnight for that day.

## See also

The Claude Code Analytics API helps you understand and optimize your team's development workflow. Learn more about related features:

* [Admin API overview](/en/docs/build-with-claude/administration-api)
* [Admin API reference](/en/api/admin-api)
* [Claude Code Analytics dashboard](https://console.anthropic.com/claude-code)
* [Usage and Cost API](/en/docs/build-with-claude/usage-cost-api) - Track API usage across all Anthropic services
* [Identity and access management](https://code.claude.com/docs/iam)
* [Monitoring usage with OpenTelemetry](https://code.claude.com/docs/monitoring-usage) for custom metrics and alerting


# Claude on Amazon Bedrock
Source: https://docs.claude.com/en/docs/build-with-claude/claude-on-amazon-bedrock

Anthropic's Claude models are now generally available through Amazon Bedrock.

export const ModelId = ({children, style = {}}) => {
  const copiedNotice = 'Copied!';
  const handleClick = e => {
    const element = e.currentTarget;
    const textSpan = element.querySelector('.model-id-text');
    const copiedSpan = element.querySelector('.model-id-copied');
    navigator.clipboard.writeText(children).then(() => {
      textSpan.style.opacity = '0';
      copiedSpan.style.opacity = '1';
      element.style.backgroundColor = '#d4edda';
      element.style.borderColor = '#c3e6cb';
      setTimeout(() => {
        textSpan.style.opacity = '1';
        copiedSpan.style.opacity = '0';
        element.style.backgroundColor = '#f5f5f5';
        element.style.borderColor = 'transparent';
      }, 2000);
    }).catch(error => {
      console.error('Failed to copy:', error);
    });
  };
  const handleMouseEnter = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip && copiedSpan.style.opacity !== '1') {
      tooltip.style.opacity = '1';
    }
    element.style.backgroundColor = '#e8e8e8';
    element.style.borderColor = '#d0d0d0';
  };
  const handleMouseLeave = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip) {
      tooltip.style.opacity = '0';
    }
    if (copiedSpan.style.opacity !== '1') {
      element.style.backgroundColor = '#f5f5f5';
      element.style.borderColor = 'transparent';
    }
  };
  const defaultStyle = {
    cursor: 'pointer',
    position: 'relative',
    transition: 'all 0.2s ease',
    display: 'inline-block',
    userSelect: 'none',
    backgroundColor: '#f5f5f5',
    padding: '2px 4px',
    borderRadius: '4px',
    fontFamily: 'Monaco, Consolas, "Courier New", monospace',
    fontSize: '0.75em',
    border: '1px solid transparent',
    ...style
  };
  return <span onClick={handleClick} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} style={defaultStyle}>
      <span className="model-id-text" style={{
    transition: 'opacity 0.1s ease'
  }}>
        {children}
      </span>
      <span className="model-id-copied" style={{
    position: 'absolute',
    top: '2px',
    left: '4px',
    right: '4px',
    opacity: '0',
    transition: 'opacity 0.1s ease',
    color: '#155724'
  }}>
        {copiedNotice}
      </span>
    </span>;
};

Calling Claude through Bedrock slightly differs from how you would call Claude when using Anthropic's client SDK's. This guide will walk you through the process of completing an API call to Claude on Bedrock in either Python or TypeScript.

Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

## Install and configure the AWS CLI

1. [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`
2. Configure your AWS credentials using the AWS configure command (see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)) or find your credentials by navigating to "Command line or programmatic access" within your AWS dashboard and following the directions in the popup modal.
3. Verify that your credentials are working:

```bash Shell theme={null}
aws sts get-caller-identity
```

## Install an SDK for accessing Bedrock

Anthropic's [client SDKs](/en/api/client-sdks) support Bedrock. You can also use an AWS SDK like `boto3` directly.

<CodeGroup>
  ```Python Python theme={null}
  pip install -U "anthropic[bedrock]"
  ```

  ```TypeScript TypeScript theme={null}
  npm install @anthropic-ai/bedrock-sdk
  ```

  ```Python Boto3 (Python) theme={null}
  pip install boto3>=1.28.59
  ```
</CodeGroup>

## Accessing Bedrock

### Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

#### API model IDs

| Model                                                                            | Base Bedrock model ID                                        | `global` | `us` | `eu` | `jp` | `apac` |
| :------------------------------------------------------------------------------- | :----------------------------------------------------------- | :------- | :--- | :--- | :--- | :----- |
| Claude Sonnet 4.5                                                                | <ModelId>anthropic.claude-sonnet-4-5-20250929-v1:0</ModelId> | Yes      | Yes  | Yes  | Yes  | No     |
| Claude Sonnet 4                                                                  | <ModelId>anthropic.claude-sonnet-4-20250514-v1:0</ModelId>   | Yes      | Yes  | Yes  | No   | Yes    |
| Claude Sonnet 3.7 <Tooltip tip="Deprecated as of October 28, 2025.">⚠️</Tooltip> | <ModelId>anthropic.claude-3-7-sonnet-20250219-v1:0</ModelId> | No       | Yes  | Yes  | No   | Yes    |
| Claude Opus 4.1                                                                  | <ModelId>anthropic.claude-opus-4-1-20250805-v1:0</ModelId>   | No       | Yes  | No   | No   | No     |
| Claude Opus 4                                                                    | <ModelId>anthropic.claude-opus-4-20250514-v1:0</ModelId>     | No       | Yes  | No   | No   | No     |
| Claude Opus 3 <Tooltip tip="Deprecated as of June 30, 2025.">⚠️</Tooltip>        | <ModelId>anthropic.claude-3-opus-20240229-v1:0</ModelId>     | No       | Yes  | No   | No   | No     |
| Claude Haiku 4.5                                                                 | <ModelId>anthropic.claude-haiku-4-5-20251001-v1:0</ModelId>  | Yes      | Yes  | Yes  | No   | No     |
| Claude Haiku 3.5                                                                 | <ModelId>anthropic.claude-3-5-haiku-20241022-v1:0</ModelId>  | No       | Yes  | No   | No   | No     |
| Claude Haiku 3                                                                   | <ModelId>anthropic.claude-3-haiku-20240307-v1:0</ModelId>    | No       | Yes  | Yes  | No   | Yes    |

For more information about regional vs global model IDs, see the [Global vs regional endpoints](#global-vs-regional-endpoints) section below.

### List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

<CodeGroup>
  ```bash AWS CLI theme={null}
  aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"
  ```

  ```python Boto3 (Python) theme={null}
  import boto3

  bedrock = boto3.client(service_name="bedrock")
  response = bedrock.list_foundation_models(byProvider="anthropic")

  for summary in response["modelSummaries"]:
      print(summary["modelId"])
  ```
</CodeGroup>

### Making requests

The following examples show how to generate text from Claude on Bedrock:

<CodeGroup>
  ```Python Python theme={null}
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(
      # Authenticate by either providing the keys below or use the default AWS credential providers, such as
      # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
      aws_access_key="<access key>",
      aws_secret_key="<secret key>",
      # Temporary credentials can be used with aws_session_token.
      # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
      aws_session_token="<session_token>",
      # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,
      # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
      aws_region="us-west-2",
  )

  message = client.messages.create(
      model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}]
  )
  print(message.content)
  ```

  ```TypeScript TypeScript theme={null}
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  const client = new AnthropicBedrock({
    // Authenticate by either providing the keys below or use the default AWS credential providers, such as
    // using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    awsAccessKey: '<access key>',
    awsSecretKey: '<secret key>',

    // Temporary credentials can be used with awsSessionToken.
    // Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    awsSessionToken: '<session_token>',

    // awsRegion changes the aws region to which the request is made. By default, we read AWS_REGION,
    // and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
    awsRegion: 'us-west-2',
  });

  async function main() {
    const message = await client.messages.create({
      model: 'global.anthropic.claude-sonnet-4-5-20250929-v1:0',
      max_tokens: 256,
      messages: [{"role": "user", "content": "Hello, world"}]
    });
    console.log(message);
  }
  main().catch(console.error);
  ```

  ```python Boto3 (Python) theme={null}
  import boto3
  import json

  bedrock = boto3.client(service_name="bedrock-runtime")
  body = json.dumps({
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "Hello, world"}],
    "anthropic_version": "bedrock-2023-05-31"
  })

  response = bedrock.invoke_model(body=body, modelId="global.anthropic.claude-sonnet-4-5-20250929-v1:0")

  response_body = json.loads(response.get("body").read())
  print(response_body.get("content"))
  ```
</CodeGroup>

See our [client SDKs](/en/api/client-sdks) for more details, and the official Bedrock docs [here](https://docs.aws.amazon.com/bedrock/).

## Activity logging

Bedrock provides an [invocation logging service](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) that allows customers to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis in order to understand your activity and investigate any potential misuse.

<Note>
  Turning on this service does not give AWS or Anthropic any access to your content.
</Note>

## Feature support

You can find all the features currently supported on Bedrock [here](/en/api/overview).

### PDF Support on Bedrock

PDF support is available on Amazon Bedrock through both the Converse API and InvokeModel API. For detailed information about PDF processing capabilities and limitations, see the [PDF support documentation](/en/docs/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

**Important considerations for Converse API users:**

* Visual PDF analysis (charts, images, layouts) requires citations to be enabled
* Without citations, only basic text extraction is available
* For full control without forced citations, use the InvokeModel API

For more details on the two document processing modes and their limitations, refer to the [PDF support guide](/en/docs/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

### 1M token context window

Claude Sonnet 4 and 4.5 support the [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) on Amazon Bedrock.

<Note>
  The 1M token context window is currently in beta. To use the extended context window, include the `context-1m-2025-08-07` beta header in your [Bedrock API requests](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html).
</Note>

## Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Amazon Bedrock offers two endpoint types:

* **Global endpoints**: Dynamic routing for maximum availability
* **Regional endpoints**: Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.

<Note>
  This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4, Opus 4, and earlier) maintain their existing pricing structures.
</Note>

### When to use each option

**Global endpoints (recommended):**

* Provide maximum availability and uptime
* Dynamically route requests to regions with available capacity
* No pricing premium
* Best for applications where data residency is flexible

**Regional endpoints (CRIS):**

* Route traffic through specific geographic regions
* Required for data residency and compliance requirements
* Available for US, EU, Japan, and Australia
* 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints (default for Sonnet 4.5 and 4):**

The model IDs for Claude Sonnet 4.5 and 4 already include the `global.` prefix:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(aws_region="us-west-2")

  message = client.messages.create(
      model="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}]
  )
  ```

  ```typescript TypeScript theme={null}
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  const client = new AnthropicBedrock({
    awsRegion: 'us-west-2',
  });

  const message = await client.messages.create({
    model: 'global.anthropic.claude-sonnet-4-5-20250929-v1:0',
    max_tokens: 256,
    messages: [{role: "user", content: "Hello, world"}]
  });
  ```
</CodeGroup>

**Using regional endpoints (CRIS):**

To use regional endpoints, remove the `global.` prefix from the model ID:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(aws_region="us-west-2")

  # Using US regional endpoint (CRIS)
  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",  # No global. prefix
      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}]
  )
  ```

  ```typescript TypeScript theme={null}
  import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

  const client = new AnthropicBedrock({
    awsRegion: 'us-west-2',
  });

  // Using US regional endpoint (CRIS)
  const message = await client.messages.create({
    model: 'anthropic.claude-sonnet-4-5-20250929-v1:0',  // No global. prefix
    max_tokens: 256,
    messages: [{role: "user", content: "Hello, world"}]
  });
  ```
</CodeGroup>

### Additional resources

* **AWS Bedrock pricing:** [aws.amazon.com/bedrock/pricing](https://aws.amazon.com/bedrock/pricing/)
* **AWS pricing documentation:** [Bedrock pricing guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html)
* **AWS blog post:** [Introducing Claude Sonnet 4.5 in Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)
* **Anthropic pricing details:** [Pricing documentation](/en/docs/about-claude/pricing#third-party-platform-pricing)


# Claude on Vertex AI
Source: https://docs.claude.com/en/docs/build-with-claude/claude-on-vertex-ai

Anthropic's Claude models are now generally available through [Vertex AI](https://cloud.google.com/vertex-ai).

export const ModelId = ({children, style = {}}) => {
  const copiedNotice = 'Copied!';
  const handleClick = e => {
    const element = e.currentTarget;
    const textSpan = element.querySelector('.model-id-text');
    const copiedSpan = element.querySelector('.model-id-copied');
    navigator.clipboard.writeText(children).then(() => {
      textSpan.style.opacity = '0';
      copiedSpan.style.opacity = '1';
      element.style.backgroundColor = '#d4edda';
      element.style.borderColor = '#c3e6cb';
      setTimeout(() => {
        textSpan.style.opacity = '1';
        copiedSpan.style.opacity = '0';
        element.style.backgroundColor = '#f5f5f5';
        element.style.borderColor = 'transparent';
      }, 2000);
    }).catch(error => {
      console.error('Failed to copy:', error);
    });
  };
  const handleMouseEnter = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip && copiedSpan.style.opacity !== '1') {
      tooltip.style.opacity = '1';
    }
    element.style.backgroundColor = '#e8e8e8';
    element.style.borderColor = '#d0d0d0';
  };
  const handleMouseLeave = e => {
    const element = e.currentTarget;
    const copiedSpan = element.querySelector('.model-id-copied');
    const tooltip = element.querySelector('.copy-tooltip');
    if (tooltip) {
      tooltip.style.opacity = '0';
    }
    if (copiedSpan.style.opacity !== '1') {
      element.style.backgroundColor = '#f5f5f5';
      element.style.borderColor = 'transparent';
    }
  };
  const defaultStyle = {
    cursor: 'pointer',
    position: 'relative',
    transition: 'all 0.2s ease',
    display: 'inline-block',
    userSelect: 'none',
    backgroundColor: '#f5f5f5',
    padding: '2px 4px',
    borderRadius: '4px',
    fontFamily: 'Monaco, Consolas, "Courier New", monospace',
    fontSize: '0.75em',
    border: '1px solid transparent',
    ...style
  };
  return <span onClick={handleClick} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} style={defaultStyle}>
      <span className="model-id-text" style={{
    transition: 'opacity 0.1s ease'
  }}>
        {children}
      </span>
      <span className="model-id-copied" style={{
    position: 'absolute',
    top: '2px',
    left: '4px',
    right: '4px',
    opacity: '0',
    transition: 'opacity 0.1s ease',
    color: '#155724'
  }}>
        {copiedNotice}
      </span>
    </span>;
};

The Vertex API for accessing Claude is nearly-identical to the [Messages API](/en/api/messages) and supports all of the same options, with two key differences:

* In Vertex, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
* In Vertex, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Vertex is also supported by Anthropic's official [client SDKs](/en/api/client-sdks). This guide will walk you through the process of making a request to Claude on Vertex AI in either Python or TypeScript.

Note that this guide assumes you have already have a GCP project that is able to use Vertex AI. See [using the Claude 3 models from Anthropic](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for more information on the setup required, as well as a full walkthrough.

## Install an SDK for accessing Vertex AI

First, install Anthropic's [client SDK](/en/api/client-sdks) for your language of choice.

<CodeGroup>
  ```Python Python theme={null}
  pip install -U google-cloud-aiplatform "anthropic[vertex]"
  ```

  ```TypeScript TypeScript theme={null}
  npm install @anthropic-ai/vertex-sdk
  ```
</CodeGroup>

## Accessing Vertex AI

### Model Availability

Note that Anthropic model availability varies by region. Search for "Claude" in the [Vertex AI Model Garden](https://cloud.google.com/model-garden) or go to [Use Claude 3](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for the latest information.

#### API model IDs

| Model                                                                            | Vertex AI API model ID                         |
| -------------------------------------------------------------------------------- | ---------------------------------------------- |
| Claude Sonnet 4.5                                                                | <ModelId>claude-sonnet-4-5\@20250929</ModelId> |
| Claude Sonnet 4                                                                  | <ModelId>claude-sonnet-4\@20250514</ModelId>   |
| Claude Sonnet 3.7 <Tooltip tip="Deprecated as of October 28, 2025.">⚠️</Tooltip> | <ModelId>claude-3-7-sonnet\@20250219</ModelId> |
| Claude Opus 4.1                                                                  | <ModelId>claude-opus-4-1\@20250805</ModelId>   |
| Claude Opus 4                                                                    | <ModelId>claude-opus-4\@20250514</ModelId>     |
| Claude Opus 3 <Tooltip tip="Deprecated as of June 30, 2025.">⚠️</Tooltip>        | <ModelId>claude-3-opus\@20240229</ModelId>     |
| Claude Haiku 4.5                                                                 | <ModelId>claude-haiku-4-5\@20251001</ModelId>  |
| Claude Haiku 3.5                                                                 | <ModelId>claude-3-5-haiku\@20241022</ModelId>  |
| Claude Haiku 3                                                                   | <ModelId>claude-3-haiku\@20240307</ModelId>    |

### Making requests

Before running requests you may need to run `gcloud auth application-default login` to authenticate with GCP.

The following examples shows how to generate text from Claude on Vertex AI:

<CodeGroup>
  ```Python Python theme={null}
  from anthropic import AnthropicVertex

  project_id = "MY_PROJECT_ID"
  region = "global"

  client = AnthropicVertex(project_id=project_id, region=region)

  message = client.messages.create(
      model="claude-sonnet-4-5@20250929",
      max_tokens=100,
      messages=[
          {
              "role": "user",
              "content": "Hey Claude!",
          }
      ],
  )
  print(message)
  ```

  ```TypeScript TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  const projectId = 'MY_PROJECT_ID';
  const region = 'global';

  // Goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex({
    projectId,
    region,
  });

  async function main() {
    const result = await client.messages.create({
      model: 'claude-sonnet-4-5@20250929',
      max_tokens: 100,
      messages: [
        {
          role: 'user',
          content: 'Hey Claude!',
        },
      ],
    });
    console.log(JSON.stringify(result, null, 2));
  }

  main();
  ```

  ```bash Shell theme={null}
  MODEL_ID=claude-sonnet-4-5@20250929
  LOCATION=global
  PROJECT_ID=MY_PROJECT_ID

  curl \
  -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://$LOCATION-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/anthropic/models/${MODEL_ID}:streamRawPredict -d \
  '{
    "anthropic_version": "vertex-2023-10-16",
    "messages": [{
      "role": "user",
      "content": "Hey Claude!"
    }],
    "max_tokens": 100,
  }'
  ```
</CodeGroup>

See our [client SDKs](/en/api/client-sdks) and the official [Vertex AI docs](https://cloud.google.com/vertex-ai/docs) for more details.

## Activity logging

Vertex provides a [request-response logging service](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/request-response-logging) that allows customers to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis in order to understand your activity and investigate any potential misuse.

<Note>
  Turning on this service does not give Google or Anthropic any access to your content.
</Note>

## Feature support

You can find all the features currently supported on Vertex [here](/en/api/overview).

## Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Google Vertex AI offers two endpoint types:

* **Global endpoints**: Dynamic routing for maximum availability
* **Regional endpoints**: Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.

<Note>
  This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4, Opus 4, and earlier) maintain their existing pricing structures.
</Note>

### When to use each option

**Global endpoints (recommended):**

* Provide maximum availability and uptime
* Dynamically route requests to regions with available capacity
* No pricing premium
* Best for applications where data residency is flexible
* Only supports pay-as-you-go traffic (provisioned throughput requires regional endpoints)

**Regional endpoints:**

* Route traffic through specific geographic regions
* Required for data residency and compliance requirements
* Support both pay-as-you-go and provisioned throughput
* 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints (recommended):**

Set the `region` parameter to `"global"` when initializing the client:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import AnthropicVertex

  project_id = "MY_PROJECT_ID"
  region = "global"

  client = AnthropicVertex(project_id=project_id, region=region)

  message = client.messages.create(
      model="claude-sonnet-4-5@20250929",
      max_tokens=100,
      messages=[
          {
              "role": "user",
              "content": "Hey Claude!",
          }
      ],
  )
  print(message)
  ```

  ```typescript TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  const projectId = 'MY_PROJECT_ID';
  const region = 'global';

  const client = new AnthropicVertex({
    projectId,
    region,
  });

  const result = await client.messages.create({
    model: 'claude-sonnet-4-5@20250929',
    max_tokens: 100,
    messages: [
      {
        role: 'user',
        content: 'Hey Claude!',
      },
    ],
  });
  ```
</CodeGroup>

**Using regional endpoints:**

Specify a specific region like `"us-east1"` or `"europe-west1"`:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import AnthropicVertex

  project_id = "MY_PROJECT_ID"
  region = "us-east1"  # Specify a specific region

  client = AnthropicVertex(project_id=project_id, region=region)

  message = client.messages.create(
      model="claude-sonnet-4-5@20250929",
      max_tokens=100,
      messages=[
          {
              "role": "user",
              "content": "Hey Claude!",
          }
      ],
  )
  print(message)
  ```

  ```typescript TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  const projectId = 'MY_PROJECT_ID';
  const region = 'us-east1';  // Specify a specific region

  const client = new AnthropicVertex({
    projectId,
    region,
  });

  const result = await client.messages.create({
    model: 'claude-sonnet-4-5@20250929',
    max_tokens: 100,
    messages: [
      {
        role: 'user',
        content: 'Hey Claude!',
      },
    ],
  });
  ```
</CodeGroup>

### Additional resources

* **Google Vertex AI pricing:** [cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
* **Claude models documentation:** [Claude on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude)
* **Google blog post:** [Global endpoint for Claude models](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai)
* **Anthropic pricing details:** [Pricing documentation](/en/docs/about-claude/pricing#third-party-platform-pricing)


# Context editing
Source: https://docs.claude.com/en/docs/build-with-claude/context-editing

Automatically manage conversation context as it grows with context editing.

<Note>
  Context editing is currently in beta with support for tool result clearing and thinking block clearing. To enable it, use the beta header `context-management-2025-06-27` in your API requests.

  Please reach out through our [feedback form](https://forms.gle/YXC2EKGMhjN1c4L88) to share your feedback on this feature.
</Note>

## Overview

Context editing allows you to automatically manage conversation context as it grows, helping you optimize costs and stay within context window limits. The API provides different strategies for managing context:

* **Tool result clearing** (`clear_tool_uses_20250919`): Automatically clears tool use/result pairs when conversation context exceeds your configured threshold
* **Thinking block clearing** (`clear_thinking_20251015`): Manages [thinking blocks](/en/docs/build-with-claude/extended-thinking) by clearing older thinking blocks from previous turns

Each strategy can be configured independently and applied together to optimize your specific use case.

## Context editing strategies

### Tool result clearing

The `clear_tool_uses_20250919` strategy clears tool results when conversation context grows beyond your configured threshold. When activated, the API automatically clears the oldest tool results in chronological order, replacing them with placeholder text to let Claude know the tool result was removed. By default, only tool results are cleared. You can optionally clear both tool results and tool calls (the tool use parameters) by setting `clear_tool_inputs` to true.

### Thinking block clearing

The `clear_thinking_20251015` strategy manages `thinking` blocks in conversations when extended thinking is enabled. This strategy automatically clears older thinking blocks from previous turns.

<Tip>
  **Default behavior**: When extended thinking is enabled without configuring the `clear_thinking_20251015` strategy, the API automatically keeps only the thinking blocks from the last assistant turn (equivalent to `keep: {type: "thinking_turns", value: 1}`).

  To maximize cache hits, preserve all thinking blocks by setting `keep: "all"`.
</Tip>

<Note>
  An assistant conversation turn may include multiple content blocks (e.g. when using tools) and multiple thinking blocks (e.g. with [interleaved thinking](/en/docs/build-with-claude/extended-thinking#interleaved-thinking)).
</Note>

<Tip>
  **Context editing happens server-side**

  Context editing is applied **server-side** before the prompt reaches Claude. Your client application maintains the full, unmodified conversation history—you do not need to sync your client state with the edited version. Continue managing your full conversation history locally as you normally would.
</Tip>

<Tip>
  **Context editing and prompt caching**

  Context editing's interaction with [prompt caching](/en/docs/build-with-claude/prompt-caching) varies by strategy:

  * **Tool result clearing**: Invalidates cached prompt prefixes when content is cleared. To account for this, we recommend clearing enough tokens to make the cache invalidation worthwhile. Use the `clear_at_least` parameter to ensure a minimum number of tokens is cleared each time. You'll incur cache write costs each time content is cleared, but subsequent requests can reuse the newly cached prefix.

  * **Thinking block clearing**: When thinking blocks are **kept** in context (not cleared), the prompt cache is preserved, enabling cache hits and reducing input token costs. When thinking blocks are **cleared**, the cache is invalidated at the point where clearing occurs. Configure the `keep` parameter based on whether you want to prioritize cache performance or context window availability.
</Tip>

## Supported models

Context editing is available on:

* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)
* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)
* Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)

## Tool result clearing usage

The simplest way to enable tool result clearing is to specify only the strategy type, as all other [configuration options](#configuration-options-for-tool-result-clearing) will use their default values:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Search for recent developments in AI"
              }
          ],
          "tools": [
              {
                  "type": "web_search_20250305",
                  "name": "web_search"
              }
          ],
          "context_management": {
              "edits": [
                  {"type": "clear_tool_uses_20250919"}
              ]
          }
      }'
  ```

  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Search for recent developments in AI"
          }
      ],
      tools=[
          {
              "type": "web_search_20250305",
              "name": "web_search"
          }
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {"type": "clear_tool_uses_20250919"}
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Search for recent developments in AI"
      }
    ],
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search"
      }
    ],
    context_management: {
      edits: [
        { type: "clear_tool_uses_20250919" }
      ]
    },
    betas: ["context-management-2025-06-27"]
  });
  ```
</CodeGroup>

### Advanced configuration

You can customize the tool result clearing behavior with additional parameters:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Create a simple command line calculator app using Python"
              }
          ],
          "tools": [
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool",
                  "max_characters": 10000
              },
              {
                  "type": "web_search_20250305",
                  "name": "web_search",
                  "max_uses": 3
              }
          ],
          "context_management": {
              "edits": [
                  {
                      "type": "clear_tool_uses_20250919",
                      "trigger": {
                          "type": "input_tokens",
                          "value": 30000
                      },
                      "keep": {
                          "type": "tool_uses",
                          "value": 3
                      },
                      "clear_at_least": {
                          "type": "input_tokens",
                          "value": 5000
                      },
                      "exclude_tools": ["web_search"]
                  }
              ]
          }
      }'
  ```

  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Create a simple command line calculator app using Python"
          }
      ],
      tools=[
          {
              "type": "text_editor_20250728",
              "name": "str_replace_based_edit_tool",
              "max_characters": 10000
          },
          {
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 3
          }
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_tool_uses_20250919",
                  # Trigger clearing when threshold is exceeded
                  "trigger": {
                      "type": "input_tokens",
                      "value": 30000
                  },
                  # Number of tool uses to keep after clearing
                  "keep": {
                      "type": "tool_uses",
                      "value": 3
                  },
                  # Optional: Clear at least this many tokens
                  "clear_at_least": {
                      "type": "input_tokens",
                      "value": 5000
                  },
                  # Exclude these tools from being cleared
                  "exclude_tools": ["web_search"]
              }
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Create a simple command line calculator app using Python"
      }
    ],
    tools: [
      {
        type: "text_editor_20250728",
        name: "str_replace_based_edit_tool",
        max_characters: 10000
      },
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 3
      }
    ],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_tool_uses_20250919",
          // Trigger clearing when threshold is exceeded
          trigger: {
            type: "input_tokens",
            value: 30000
          },
          // Number of tool uses to keep after clearing
          keep: {
            type: "tool_uses",
            value: 3
          },
          // Optional: Clear at least this many tokens
          clear_at_least: {
            type: "input_tokens",
            value: 5000
          },
          // Exclude these tools from being cleared
          exclude_tools: ["web_search"]
        }
      ]
    }
  });
  ```
</CodeGroup>

## Thinking block clearing usage

Enable thinking block clearing to manage context and prompt caching effectively when extended thinking is enabled:

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5-20250929",
          "max_tokens": 1024,
          "messages": [...],
          "thinking": {
              "type": "enabled",
              "budget_tokens": 10000
          },
          "context_management": {
              "edits": [
                  {
                      "type": "clear_thinking_20251015",
                      "keep": {
                          "type": "thinking_turns",
                          "value": 2
                      }
                  }
              ]
          }
      }'
  ```

  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      messages=[...],
      thinking={
          "type": "enabled",
          "budget_tokens": 10000
      },
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_thinking_20251015",
                  "keep": {
                      "type": "thinking_turns",
                      "value": 2
                  }
              }
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    messages: [...],
    thinking: {
      type: "enabled",
      budget_tokens: 10000
    },
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_thinking_20251015",
          keep: {
            type: "thinking_turns",
            value: 2
          }
        }
      ]
    }
  });
  ```
</CodeGroup>

### Configuration options for thinking block clearing

The `clear_thinking_20251015` strategy supports the following configuration:

| Configuration option | Default                              | Description                                                                                                                                                                                              |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keep`               | `{type: "thinking_turns", value: 1}` | Defines how many recent assistant turns with thinking blocks to preserve. Use `{type: "thinking_turns", value: N}` where N must be > 0 to keep the last N turns, or `"all"` to keep all thinking blocks. |

**Example configurations:**

```json  theme={null}
// Keep thinking blocks from the last 3 assistant turns
{
  "type": "clear_thinking_20251015",
  "keep": {
    "type": "thinking_turns",
    "value": 3
  }
}

// Keep all thinking blocks (maximizes cache hits)
{
  "type": "clear_thinking_20251015",
  "keep": "all"
}
```

### Combining strategies

You can use both thinking block clearing and tool result clearing together:

<Note>
  When using multiple strategies, the `clear_thinking_20251015` strategy must be listed first in the `edits` array.
</Note>

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      messages=[...],
      thinking={
          "type": "enabled",
          "budget_tokens": 10000
      },
      tools=[...],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_thinking_20251015",
                  "keep": {
                      "type": "thinking_turns",
                      "value": 2
                  }
              },
              {
                  "type": "clear_tool_uses_20250919",
                  "trigger": {
                      "type": "input_tokens",
                      "value": 50000
                  },
                  "keep": {
                      "type": "tool_uses",
                      "value": 5
                  }
              }
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    messages: [...],
    thinking: {
      type: "enabled",
      budget_tokens: 10000
    },
    tools: [...],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_thinking_20251015",
          keep: {
            type: "thinking_turns",
            value: 2
          }
        },
        {
          type: "clear_tool_uses_20250919",
          trigger: {
            type: "input_tokens",
            value: 50000
          },
          keep: {
            type: "tool_uses",
            value: 5
          }
        }
      ]
    }
  });
  ```
</CodeGroup>

## Configuration options for tool result clearing

| Configuration option | Default              | Description                                                                                                                                                                                                                                           |
| -------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trigger`            | 100,000 input tokens | Defines when the context editing strategy activates. Once the prompt exceeds this threshold, clearing will begin. You can specify this value in either `input_tokens` or `tool_uses`.                                                                 |
| `keep`               | 3 tool uses          | Defines how many recent tool use/result pairs to keep after clearing occurs. The API removes the oldest tool interactions first, preserving the most recent ones.                                                                                     |
| `clear_at_least`     | None                 | Ensures a minimum number of tokens is cleared each time the strategy activates. If the API can't clear at least the specified amount, the strategy will not be applied. This helps determine if context clearing is worth breaking your prompt cache. |
| `exclude_tools`      | None                 | List of tool names whose tool uses and results should never be cleared. Useful for preserving important context.                                                                                                                                      |
| `clear_tool_inputs`  | `false`              | Controls whether the tool call parameters are cleared along with the tool results. By default, only the tool results are cleared while keeping Claude's original tool calls visible.                                                                  |

## Context editing response

You can see which context edits were applied to your request using the `context_management` response field, along with helpful statistics about the content and input tokens cleared.

```json Response theme={null}
{
    "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
    "type": "message",
    "role": "assistant",
    "content": [...],
    "usage": {...},
    "context_management": {
        "applied_edits": [
            // When using `clear_thinking_20251015`
            {
                "type": "clear_thinking_20251015",
                "cleared_thinking_turns": 3,
                "cleared_input_tokens": 15000
            },
            // When using `clear_tool_uses_20250919`
            {
                "type": "clear_tool_uses_20250919",
                "cleared_tool_uses": 8,
                "cleared_input_tokens": 50000
            }
        ]
    }
}
```

For streaming responses, the context edits will be included in the final `message_delta` event:

```json Streaming Response theme={null}
{
    "type": "message_delta",
    "delta": {
        "stop_reason": "end_turn",
        "stop_sequence": null
    },
    "usage": {
        "output_tokens": 1024
    },
    "context_management": {
        "applied_edits": [...]
    }
}
```

## Token counting

The [token counting](/en/docs/build-with-claude/token-counting) endpoint supports context management, allowing you to preview how many tokens your prompt will use after context editing is applied.

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages/count_tokens \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "messages": [
              {
                  "role": "user",
                  "content": "Continue our conversation..."
              }
          ],
          "tools": [...],
          "context_management": {
              "edits": [
                  {
                      "type": "clear_tool_uses_20250919",
                      "trigger": {
                          "type": "input_tokens",
                          "value": 30000
                      },
                      "keep": {
                          "type": "tool_uses",
                          "value": 5
                      }
                  }
              ]
          }
      }'
  ```

  ```python Python theme={null}
  response = client.beta.messages.count_tokens(
      model="claude-sonnet-4-5",
      messages=[
          {
              "role": "user",
              "content": "Continue our conversation..."
          }
      ],
      tools=[...],  # Your tool definitions
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_tool_uses_20250919",
                  "trigger": {
                      "type": "input_tokens",
                      "value": 30000
                  },
                  "keep": {
                      "type": "tool_uses",
                      "value": 5
                  }
              }
          ]
      }
  )

  print(f"Original tokens: {response.context_management['original_input_tokens']}")
  print(f"After clearing: {response.input_tokens}")
  print(f"Savings: {response.context_management['original_input_tokens'] - response.input_tokens} tokens")
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.countTokens({
    model: "claude-sonnet-4-5",
    messages: [
      {
        role: "user",
        content: "Continue our conversation..."
      }
    ],
    tools: [...],  // Your tool definitions
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_tool_uses_20250919",
          trigger: {
            type: "input_tokens",
            value: 30000
          },
          keep: {
            type: "tool_uses",
            value: 5
          }
        }
      ]
    }
  });

  console.log(`Original tokens: ${response.context_management?.original_input_tokens}`);
  console.log(`After clearing: ${response.input_tokens}`);
  console.log(`Savings: ${(response.context_management?.original_input_tokens || 0) - response.input_tokens} tokens`);
  ```
</CodeGroup>

```json Response theme={null}
{
    "input_tokens": 25000,
    "context_management": {
        "original_input_tokens": 70000
    }
}
```

The response shows both the final token count after context management is applied (`input_tokens`) and the original token count before any clearing occurred (`original_input_tokens`).

## Using with the Memory Tool

Context editing can be combined with the [memory tool](/en/docs/agents-and-tools/tool-use/memory-tool). When your conversation context approaches the configured clearing threshold, Claude receives an automatic warning to preserve important information. This enables Claude to save tool results or context to its memory files before they're cleared from the conversation history.

This combination allows you to:

* **Preserve important context**: Claude can write essential information from tool results to memory files before those results are cleared
* **Maintain long-running workflows**: Enable agentic workflows that would otherwise exceed context limits by offloading information to persistent storage
* **Access information on demand**: Claude can look up previously cleared information from memory files when needed, rather than keeping everything in the active context window

For example, in a file editing workflow where Claude performs many operations, Claude can summarize completed changes to memory files as the context grows. When tool results are cleared, Claude retains access to that information through its memory system and can continue working effectively.

To use both features together, enable them in your API request:

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[...],
      tools=[
          {
              "type": "memory_20250818",
              "name": "memory"
          },
          # Your other tools
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {"type": "clear_tool_uses_20250919"}
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [...],
    tools: [
      {
        type: "memory_20250818",
        name: "memory"
      },
      // Your other tools
    ],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        { type: "clear_tool_uses_20250919" }
      ]
    }
  });
  ```
</CodeGroup>


# Context windows
Source: https://docs.claude.com/en/docs/build-with-claude/context-windows



## Understanding the context window

The "context window" refers to the entirety of the amount of text a language model can look back on and reference when generating new text plus the new text it generates. This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model's ability to handle longer prompts or maintain coherence over extended conversations.

The diagram below illustrates the standard context window behavior for API requests<sup>1</sup>:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=eb9f2edc592262a3c2d498c3bf4e2ed1" alt="Context window diagram" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=db4d0f21a31307573711b71116ea01b9 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e6c125e2f420030b1f11bc4fecba581a 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9ee47a86de4979a05a3c91127170af2a 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=43902ab9eeb100a1141f24a33238c37f 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e0c2f2b71fdb70b2b5c9bbfbb1a80e44 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=03a77b1bf4bde454fc4bffbd15d88fad 2500w" />

*<sup>1</sup>For chat interfaces, such as for [claude.ai](https://claude.ai/), context windows can also be set up on a rolling "first in, first out" system.*

* **Progressive token accumulation:** As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely.
* **Linear growth pattern:** The context usage grows linearly with each turn, with previous turns preserved completely.
* **200K token capacity:** The total available context window (200,000 tokens) represents the maximum capacity for storing conversation history and generating new output from Claude.
* **Input-output flow:** Each turn consists of:
  * **Input phase:** Contains all previous conversation history plus the current user message
  * **Output phase:** Generates a text response that becomes part of a future input

## The context window with extended thinking

When using [extended thinking](/en/docs/build-with-claude/extended-thinking), all input and output tokens, including the tokens used for thinking, count toward the context window limit, with a few nuances in multi-turn situations.

The thinking budget tokens are a subset of your `max_tokens` parameter, are billed as output tokens, and count towards rate limits.

However, previous thinking blocks are automatically stripped from the context window calculation by the Claude API and are not part of the conversation history that the model "sees" for subsequent turns, preserving token capacity for actual conversation content.

The diagram below demonstrates the specialized token management when extended thinking is enabled:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=3ad289c01610a87c8ec1214faa09578d" alt="Context window diagram with extended thinking" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window-thinking.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a8e00261582812914cb53efe0a936e7a 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=4c0f43f4dd4e6f67c32820de8a7eba04 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c265f69b5e1dac0f8f000d9f33253093 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=6bfb8b7c35aaf9ad13283a1108b7ec0b 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=de6d6671e549c0a407b5cc1d3cb9b078 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e41fb48241b7526f815f05125d349f07 2500w" />

* **Stripping extended thinking:** Extended thinking blocks (shown in dark gray) are generated during each turn's output phase, **but are not carried forward as input tokens for subsequent turns**. You do not need to strip the thinking blocks yourself. The Claude API automatically does this for you if you pass them back.
* **Technical implementation details:**
  * The API automatically excludes thinking blocks from previous turns when you pass them back as part of the conversation history.
  * Extended thinking tokens are billed as output tokens only once, during their generation.
  * The effective context window calculation becomes: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`.
  * Thinking tokens include both `thinking` blocks and `redacted_thinking` blocks.

This architecture is token efficient and allows for extensive reasoning without token waste, as thinking blocks can be substantial in length.

<Note>
  You can read more about the context window and extended thinking in our [extended thinking guide](/en/docs/build-with-claude/extended-thinking).
</Note>

## The context window with extended thinking and tool use

The diagram below illustrates the context window token management when combining extended thinking with tool use:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=557310c0bf57d88b7a6e550abd35bc75" alt="Context window diagram with extended thinking and tool use" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window-thinking-tools.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a086ebd51148723ed500a924fb6c62a6 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9d97e97afa9bc41f92232cd60044f716 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=65ed1d60de36587470712b2ca5ab4f45 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=174dc8d916dfdf284c86fddb4c9175f3 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=881aaf0622f43065cc942538f88562af 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fd086e656df4fd7bf8cc2e6584689d58 2500w" />

<Steps>
  <Step title="First turn architecture">
    * **Input components:** Tools configuration and user message
    * **Output components:** Extended thinking + text response + tool use request
    * **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.
  </Step>

  <Step title="Tool result handling (turn 2)">
    * **Input components:** Every block in the first turn as well as the `tool_result`. The extended thinking block **must** be returned with the corresponding tool results. This is the only case wherein you **have to** return thinking blocks.
    * **Output components:** After tool results have been passed back to Claude, Claude will respond with only text (no additional extended thinking until the next `user` message).
    * **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.
  </Step>

  <Step title="Third Step">
    * **Input components:** All inputs and the output from the previous turn is carried forward with the exception of the thinking block, which can be dropped now that Claude has completed the entire tool use cycle. The API will automatically strip the thinking block for you if you pass it back, or you can feel free to strip it yourself at this stage. This is also where you would add the next `User` turn.
    * **Output components:** Since there is a new `User` turn outside of the tool use cycle, Claude will generate a new extended thinking block and continue from there.
    * **Token calculation:** Previous thinking tokens are automatically stripped from context window calculations. All other previous blocks still count as part of the token window, and the thinking block in the current `Assistant` turn counts as part of the context window.
  </Step>
</Steps>

* **Considerations for tool use with extended thinking:**
  * When posting tool results, the entire unmodified thinking block that accompanies that specific tool request (including signature/redacted portions) must be included.
  * The effective context window calculation for extended thinking with tool use becomes: `context_window = input_tokens + current_turn_tokens`.
  * The system uses cryptographic signatures to verify thinking block authenticity. Failing to preserve thinking blocks during tool use can break Claude's reasoning continuity. Thus, if you modify thinking blocks, the API will return an error.

<Note>
  Claude 4 models support [interleaved thinking](/en/docs/build-with-claude/extended-thinking#interleaved-thinking), which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.

  Claude Sonnet 3.7 does not support interleaved thinking, so there is no interleaving of extended thinking and tool calls without a non-`tool_result` user turn in between.

  For more information about using tools with extended thinking, see our [extended thinking guide](/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use).
</Note>

## 1M token context window

Claude Sonnet 4 and 4.5 support a 1-million token context window. This extended context window allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases.

<Note>
  The 1M token context window is currently in beta for organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4 and Sonnet 4.5.
</Note>

To use the 1M token context window, include the `context-1m-2025-08-07` [beta header](/en/api/beta-headers) in your API requests:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import Anthropic

  client = Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Process this large document..."}
      ],
      betas=["context-1m-2025-08-07"]
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const msg = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      { role: 'user', content: 'Process this large document...' }
    ],
    betas: ['context-1m-2025-08-07']
  });
  ```

  ```curl cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: context-1m-2025-08-07" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Process this large document..."}
      ]
    }'
  ```
</CodeGroup>

**Important considerations:**

* **Beta status**: This is a beta feature subject to change. Features and pricing may be modified or removed in future releases.
* **Usage tier requirement**: The 1M token context window is available to organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. Lower tier organizations must advance to usage tier 4 to access this feature.
* **Availability**: The 1M token context window is currently available on the Claude API, [Amazon Bedrock](/en/docs/build-with-claude/claude-on-amazon-bedrock), and [Google Cloud's Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai).
* **Pricing**: Requests exceeding 200K tokens are automatically charged at premium rates (2x input, 1.5x output pricing). See the [pricing documentation](/en/docs/about-claude/pricing#long-context-pricing) for details.
* **Rate limits**: Long context requests have dedicated rate limits. See the [rate limits documentation](/en/api/rate-limits#long-context-rate-limits) for details.
* **Multimodal considerations**: When processing large numbers of images or pdfs, be aware that the files can vary in token usage. When pairing a large prompt with a large number of images, you may hit [request size limits](/en/api/overview#request-size-limits).

## Context awareness in Claude Sonnet 4.5 and Haiku 4.5

Claude Sonnet 4.5 and Claude Haiku 4.5 feature **context awareness**, enabling these models to track their remaining context window (i.e. "token budget") throughout a conversation. This enables Claude to execute tasks and manage context more effectively by understanding how much space it has to work. Claude is natively trained to use this context precisely to persist in the task until the very end, rather than having to guess how many tokens are remaining. For a model, lacking context awareness is like competing in a cooking show without a clock. Claude 4.5 models change this by explicitly informing the model about its remaining context, so it can take maximum advantage of the available tokens.

**How it works:**

At the start of a conversation, Claude receives information about its total context window:

```
<budget:token_budget>200000</budget:token_budget>
```

The budget is set to 200K tokens (standard), 500K tokens (Claude.ai Enterprise), or 1M tokens (beta, for eligible organizations).

After each tool call, Claude receives an update on remaining capacity:

```
<system_warning>Token usage: 35000/200000; 165000 remaining</system_warning>
```

This awareness helps Claude determine how much capacity remains for work and enables more effective execution on long-running tasks. Image tokens are included in these budgets.

**Benefits:**

Context awareness is particularly valuable for:

* Long-running agent sessions that require sustained focus
* Multi-context-window workflows where state transitions matter
* Complex tasks requiring careful token management

For prompting guidance on leveraging context awareness, see our [Claude 4 best practices guide](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#context-awareness-and-multi-window-workflows).

## Context window management with newer Claude models

In newer Claude models (starting with Claude Sonnet 3.7), if the sum of prompt tokens and output tokens exceeds the model's context window, the system will return a validation error rather than silently truncating the context. This change provides more predictable behavior but requires more careful token management.

To plan your token usage and ensure you stay within context window limits, you can use the [token counting API](/en/docs/build-with-claude/token-counting) to estimate how many tokens your messages will use before sending them to Claude.

See our [model comparison](/en/docs/about-claude/models/overview#model-comparison-table) table for a list of context window sizes by model.

# Next steps

<CardGroup cols={2}>
  <Card title="Model comparison table" icon="scale-balanced" href="/en/docs/about-claude/models/overview#model-comparison-table">
    See our model comparison table for a list of context window sizes and input / output token pricing by model.
  </Card>

  <Card title="Extended thinking overview" icon="head-side-gear" href="/en/docs/build-with-claude/extended-thinking">
    Learn more about how extended thinking works and how to implement it alongside other features such as tool use and prompt caching.
  </Card>
</CardGroup>


# Embeddings
Source: https://docs.claude.com/en/docs/build-with-claude/embeddings

Text embeddings are numerical representations of text that enable measuring semantic similarity. This guide introduces embeddings, their applications, and how to use embedding models for tasks like search, recommendations, and anomaly detection.

## Before implementing embeddings

When selecting an embeddings provider, there are several factors you can consider depending on your needs and preferences:

* Dataset size & domain specificity: size of the model training dataset and its relevance to the domain you want to embed. Larger or more domain-specific data generally produces better in-domain embeddings
* Inference performance: embedding lookup speed and end-to-end latency. This is a particularly important consideration for large scale production deployments
* Customization: options for continued training on private data, or specialization of models for very specific domains. This can improve performance on unique vocabularies

## How to get embeddings with Anthropic

Anthropic does not offer its own embedding model. One embeddings provider that has a wide variety of options and capabilities encompassing all of the above considerations is Voyage AI.

Voyage AI makes state-of-the-art embedding models and offers customized models for specific industry domains such as finance and healthcare, or bespoke fine-tuned models for individual customers.

The rest of this guide is for Voyage AI, but we encourage you to assess a variety of embeddings vendors to find the best fit for your specific use case.

## Available Models

Voyage recommends using the following text embedding models:

| Model              | Context Length | Embedding Dimension            | Description                                                                                                                                                                                                                                           |
| ------------------ | -------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `voyage-3-large`   | 32,000         | 1024 (default), 256, 512, 2048 | The best general-purpose and multilingual retrieval quality. See [blog post](https://blog.voyageai.com/2025/01/07/voyage-3-large/) for details.                                                                                                       |
| `voyage-3.5`       | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for general-purpose and multilingual retrieval quality. See [blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details.                                                                                                      |
| `voyage-3.5-lite`  | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for latency and cost. See [blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details.                                                                                                                                        |
| `voyage-code-3`    | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for **code** retrieval. See [blog post](https://blog.voyageai.com/2024/12/04/voyage-code-3/) for details.                                                                                                                                   |
| `voyage-finance-2` | 32,000         | 1024                           | Optimized for **finance** retrieval and RAG. See [blog post](https://blog.voyageai.com/2024/06/03/domain-specific-embeddings-finance-edition-voyage-finance-2/) for details.                                                                          |
| `voyage-law-2`     | 16,000         | 1024                           | Optimized for **legal** and **long-context** retrieval and RAG. Also improved performance across all domains. See [blog post](https://blog.voyageai.com/2024/04/15/domain-specific-embeddings-and-retrieval-legal-edition-voyage-law-2/) for details. |

Additionally, the following multimodal embedding models are recommended:

| Model                 | Context Length | Embedding Dimension | Description                                                                                                                                                                                                                                          |
| --------------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `voyage-multimodal-3` | 32000          | 1024                | Rich multimodal embedding model that can vectorize interleaved text and content-rich images, such as screenshots of PDFs, slides, tables, figures, and more. See [blog post](https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/) for details. |

Need help deciding which text embedding model to use? Check out the [FAQ](https://docs.voyageai.com/docs/faq#what-embedding-models-are-available-and-which-one-should-i-use\&ref=anthropic).

## Getting started with Voyage AI

To access Voyage embeddings:

1. Sign up on Voyage AI's website
2. Obtain an API key
3. Set the API key as an environment variable for convenience:

```bash  theme={null}
export VOYAGE_API_KEY="<your secret key>"
```

You can obtain the embeddings by either using the official [`voyageai` Python package](https://github.com/voyage-ai/voyageai-python) or HTTP requests, as described below.

### Voyage Python library

The `voyageai` package can be installed using the following command:

```bash  theme={null}
pip install -U voyageai
```

Then, you can create a client object and start using it to embed your texts:

```python  theme={null}
import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-3.5", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

`result.embeddings` will be a list of two embedding vectors, each containing 1024 floating-point numbers. After running the above code, the two embeddings will be printed on the screen:

```
[-0.013131560757756233, 0.019828535616397858, ...]   # embedding for "Sample text 1"
[-0.0069352793507277966, 0.020878976210951805, ...]  # embedding for "Sample text 2"
```

When creating the embeddings, you can specify a few other arguments to the `embed()` function.

For more information on the Voyage python package, see [the Voyage documentation](https://docs.voyageai.com/docs/embeddings#python-api).

### Voyage HTTP API

You can also get embeddings by requesting Voyage HTTP API. For example, you can send an HTTP request through the `curl` command in a terminal:

```bash  theme={null}
curl https://api.voyageai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-3.5"
  }'
```

The response you would get is a JSON object containing the embeddings and the token usage:

```json  theme={null}
{
  "object": "list",
  "data": [
    {
      "embedding": [-0.013131560757756233, 0.019828535616397858, ...],
      "index": 0
    },
    {
      "embedding": [-0.0069352793507277966, 0.020878976210951805, ...],
      "index": 1
    }
  ],
  "model": "voyage-3.5",
  "usage": {
    "total_tokens": 10
  }
}

```

For more information on the Voyage HTTP API, see [the Voyage documentation](https://docs.voyageai.com/reference/embeddings-api).

### AWS Marketplace

Voyage embeddings are available on [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-snt4gb6fd7ljg). Instructions for accessing Voyage on AWS are available [here](https://docs.voyageai.com/docs/aws-marketplace-model-package?ref=anthropic).

## Quickstart example

Now that we know how to get embeddings, let's see a brief example.

Suppose we have a small corpus of six documents to retrieve from

```python  theme={null}
documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
]

```

We will first use Voyage to convert each of them into an embedding vector

```python  theme={null}
import voyageai

vo = voyageai.Client()

# Embed the documents
doc_embds = vo.embed(
    documents, model="voyage-3.5", input_type="document"
).embeddings
```

The embeddings will allow us to do semantic search / retrieval in the vector space. Given an example query,

```python  theme={null}
query = "When is Apple's conference call scheduled?"
```

we convert it into an embedding, and conduct a nearest neighbor search to find the most relevant document based on the distance in the embedding space.

```python  theme={null}
import numpy as np

# Embed the query
query_embd = vo.embed(
    [query], model="voyage-3.5", input_type="query"
).embeddings[0]

# Compute the similarity
# Voyage embeddings are normalized to length 1, therefore dot-product
# and cosine similarity are the same.
similarities = np.dot(doc_embds, query_embd)

retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```

Note that we use `input_type="document"` and `input_type="query"` for embedding the document and query, respectively. More specification can be found [here](/en/docs/build-with-claude/embeddings#voyage-python-package).

The output would be the 5th document, which is indeed the most relevant to the query:

```
Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.
```

If you are looking for a detailed set of cookbooks on how to do RAG with embeddings, including vector databases, check out our [RAG cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb).

## FAQ

<AccordionGroup>
  <Accordion title="Why do Voyage embeddings have superior quality?">
    Embedding models rely on powerful neural networks to capture and compress semantic context, similar to generative models. Voyage's team of experienced AI researchers optimizes every component of the embedding process, including:

    * Model architecture
    * Data collection
    * Loss functions
    * Optimizer selection

    Learn more about Voyage's technical approach on their [blog](https://blog.voyageai.com/).
  </Accordion>

  <Accordion title="What embedding models are available and which should I use?">
    For general-purpose embedding, we recommend:

    * `voyage-3-large`: Best quality
    * `voyage-3.5-lite`: Lowest latency and cost
    * `voyage-3.5`: Balanced performance with superior retrieval quality at a competitive price point

    For retrieval, use the `input_type` parameter to specify whether the text is a query or document type.

    Domain-specific models:

    * Legal tasks: `voyage-law-2`
    * Code and programming documentation: `voyage-code-3`
    * Finance-related tasks: `voyage-finance-2`
  </Accordion>

  <Accordion title="Which similarity function should I use?">
    You can use Voyage embeddings with either dot-product similarity, cosine similarity, or Euclidean distance. An explanation about embedding similarity can be found [here](https://www.pinecone.io/learn/vector-similarity/).

    Voyage AI embeddings are normalized to length 1, which means that:

    * Cosine similarity is equivalent to dot-product similarity, while the latter can be computed more quickly.
    * Cosine similarity and Euclidean distance will result in the identical rankings.
  </Accordion>

  <Accordion title="What is the relationship between characters, words, and tokens?">
    Please see this [page](https://docs.voyageai.com/docs/tokenization?ref=anthropic).
  </Accordion>

  <Accordion title="When and how should I use the input_type parameter?">
    For all retrieval tasks and use cases (e.g., RAG), we recommend that the `input_type` parameter be used to specify whether the input text is a query or document. Do not omit `input_type` or set `input_type=None`. Specifying whether input text is a query or document can create better dense vector representations for retrieval, which can lead to better retrieval quality.

    When using the `input_type` parameter, special prompts are prepended to the input text prior to embedding. Specifically:

    > 📘 **Prompts associated with `input_type`**
    >
    > * For a query, the prompt is “Represent the query for retrieving supporting documents: “.
    > * For a document, the prompt is “Represent the document for retrieval: “.
    > * Example
    >   * When `input_type="query"`, a query like "When is Apple's conference call scheduled?" will become "**Represent the query for retrieving supporting documents:** When is Apple's conference call scheduled?"
    >   * When `input_type="document"`, a query like "Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET." will become "**Represent the document for retrieval:** Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET."

    `voyage-large-2-instruct`, as the name suggests, is trained to be responsive to additional instructions that are prepended to the input text. For classification, clustering, or other [MTEB](https://huggingface.co/mteb) subtasks, please use the instructions [here](https://github.com/voyage-ai/voyage-large-2-instruct).
  </Accordion>

  <Accordion title="What quantization options are available?">
    Quantization in embeddings converts high-precision values, like 32-bit single-precision floating-point numbers, to lower-precision formats such as 8-bit integers or 1-bit binary values, reducing storage, memory, and costs by 4x and 32x, respectively. Supported Voyage models enable quantization by specifying the output data type with the `output_dtype` parameter:

    * `float`: Each returned embedding is a list of 32-bit (4-byte) single-precision floating-point numbers. This is the default and provides the highest precision / retrieval accuracy.
    * `int8` and `uint8`: Each returned embedding is a list of 8-bit (1-byte) integers ranging from -128 to 127 and 0 to 255, respectively.
    * `binary` and `ubinary`: Each returned embedding is a list of 8-bit integers that represent bit-packed, quantized single-bit embedding values: `int8` for `binary` and `uint8` for `ubinary`. The length of the returned list of integers is 1/8 of the actual dimension of the embedding. The binary type uses the offset binary method, which you can learn more about in the FAQ below.

    > **Binary quantization example**
    >
    > Consider the following eight embedding values: -0.03955078, 0.006214142, -0.07446289, -0.039001465, 0.0046463013, 0.00030612946, -0.08496094, and 0.03994751. With binary quantization, values less than or equal to zero will be quantized to a binary zero, and positive values to a binary one, resulting in the following binary sequence: 0, 1, 0, 0, 1, 1, 0, 1. These eight bits are then packed into a single 8-bit integer, 01001101 (with the leftmost bit as the most significant bit).
    >
    > * `ubinary`: The binary sequence is directly converted and represented as the unsigned integer (`uint8`) 77.
    > * `binary`: The binary sequence is represented as the signed integer (`int8`) -51, calculated using the offset binary method (77 - 128 = -51).
  </Accordion>

  <Accordion title="How can I truncate Matryoshka embeddings?">
    Matryoshka learning creates embeddings with coarse-to-fine representations within a single vector. Voyage models, such as `voyage-code-3`, that support multiple output dimensions generate such Matryoshka embeddings. You can truncate these vectors by keeping the leading subset of dimensions. For example, the following Python code demonstrates how to truncate 1024-dimensional vectors to 256 dimensions:

    ```python  theme={null}
    import voyageai
    import numpy as np

    def embd_normalize(v: np.ndarray) -> np.ndarray:
        """
        Normalize the rows of a 2D numpy array to unit vectors by dividing each row by its Euclidean
        norm. Raises a ValueError if any row has a norm of zero to prevent division by zero.
        """
        row_norms = np.linalg.norm(v, axis=1, keepdims=True)
        if np.any(row_norms == 0):
            raise ValueError("Cannot normalize rows with a norm of zero.")
        return v / row_norms


    vo = voyageai.Client()

    # Generate voyage-code-3 vectors, which by default are 1024-dimensional floating-point numbers
    embd = vo.embed(['Sample text 1', 'Sample text 2'], model='voyage-code-3').embeddings

    # Set shorter dimension
    short_dim = 256

    # Resize and normalize vectors to shorter dimension
    resized_embd = embd_normalize(np.array(embd)[:, :short_dim]).tolist()
    ```
  </Accordion>
</AccordionGroup>

## Pricing

Visit Voyage's [pricing page](https://docs.voyageai.com/docs/pricing?ref=anthropic) for the most up to date pricing details.



---

**Navigation:** [← Previous](./06-text-editor-tool.md) | [Index](./index.md) | [Next →](./08-building-with-extended-thinking.md)
