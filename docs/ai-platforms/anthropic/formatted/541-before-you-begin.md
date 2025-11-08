---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Before you begin

### Check PDF requirements

Claude works with any standard PDF. However, you should ensure your request size meets these requirements when using PDF support:

| Requirement               | Limit                                  |
| ------------------------- | -------------------------------------- |
| Maximum request size      | 32MB                                   |
| Maximum pages per request | 100                                    |
| Format                    | Standard PDF (no passwords/encryption) |

Please note that both limits are on the entire request payload, including any other content sent alongside PDFs.

Since PDF support relies on Claude's vision capabilities, it is subject to the same [limitations and considerations](/en/docs/build-with-claude/vision#limitations) as other vision tasks.

### Supported platforms and models

PDF support is currently supported via direct API access and Google Vertex AI. All [active models](/en/docs/about-claude/models/overview) support PDF processing.

PDF support is now available on Amazon Bedrock with the following considerations:

### Amazon Bedrock PDF Support

When using PDF support through Amazon Bedrock's Converse API, there are two distinct document processing modes:

>   **📝 Note**
>
>   **Important**: To access Claude's full visual PDF understanding capabilities in the Converse API, you must enable citations. Without citations enabled, the API falls back to basic text extraction only. Learn more about [working with citations](/en/docs/build-with-claude/citations).

#### Document Processing Modes

1. **Converse Document Chat** (Original mode - Text extraction only)
   * Provides basic text extraction from PDFs
   * Cannot analyze images, charts, or visual layouts within PDFs
   * Uses approximately 1,000 tokens for a 3-page PDF
   * Automatically used when citations are not enabled

2. **Claude PDF Chat** (New mode - Full visual understanding)
   * Provides complete visual analysis of PDFs
   * Can understand and analyze charts, graphs, images, and visual layouts
   * Processes each page as both text and image for comprehensive understanding
   * Uses approximately 7,000 tokens for a 3-page PDF
   * **Requires citations to be enabled** in the Converse API

#### Key Limitations

* **Converse API**: Visual PDF analysis requires citations to be enabled. There is currently no option to use visual analysis without citations (unlike the InvokeModel API).
* **InvokeModel API**: Provides full control over PDF processing without forced citations.

#### Common Issues

If customers report that Claude isn't seeing images or charts in their PDFs when using the Converse API, they likely need to enable the citations flag. Without it, Converse falls back to basic text extraction only.

>   **📝 Note**
>
> This is a known constraint with the Converse API that we're working to address. For applications that require visual PDF analysis without citations, consider using the InvokeModel API instead.

>   **📝 Note**
>
> For non-PDF files like .csv, .xlsx, .docx, .md, or .txt files, see [Working with other file formats](/en/docs/build-with-claude/files#working-with-other-file-formats).

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
