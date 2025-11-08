---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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
```python
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
```typescript
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
```bash
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

In this example:

* The document content is cached using `cache_control` on the document block
* Citations are enabled on the document
* Claude can generate responses with citations while benefiting from cached document content
* Subsequent requests using the same document will benefit from the cached content

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
