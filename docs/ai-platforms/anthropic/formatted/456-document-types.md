---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Document Types

### Choosing a document type

We support three document types for citations. Documents can be provided directly in the message (base64, text, or URL) or uploaded via the [Files API](/en/docs/build-with-claude/files) and referenced by `file_id`:

| Type           | Best for                                                        | Chunking               | Citation format               |
| :------------- | :-------------------------------------------------------------- | :--------------------- | :---------------------------- |
| Plain text     | Simple text documents, prose                                    | Sentence               | Character indices (0-indexed) |
| PDF            | PDF files with text content                                     | Sentence               | Page numbers (1-indexed)      |
| Custom content | Lists, transcripts, special formatting, more granular citations | No additional chunking | Block indices (0-indexed)     |

>   **📝 Note**
>
> .csv, .xlsx, .docx, .md, and .txt files are not supported as document blocks. Convert these to plain text and include directly in message content. See [Working with other file formats](/en/docs/build-with-claude/files#working-with-other-file-formats).

### Plain text documents

Plain text documents are automatically chunked into sentences. You can provide them inline or by reference with their `file_id`:

<Tabs>
  <Tab title="Inline text">
```python
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
```python
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
```python
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
```python
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
```python
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
```python
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
```python
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
```python
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
