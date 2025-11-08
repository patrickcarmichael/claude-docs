---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Input Format Support

OpenRouter supports both **direct URLs** and **base64-encoded data** for multimodal inputs:

### URLs (Recommended for public content)

* **Images**: `https://example.com/image.jpg`
* **PDFs**: `https://example.com/document.pdf`
* **Audio**: Not supported via URL (base64 only)
* **Video**: Provider-specific (e.g., YouTube links for Gemini on AI Studio)

### Base64 Encoding (Required for local files)

* **Images**: `data:image/jpeg;base64,{base64_data}`
* **PDFs**: `data:application/pdf;base64,{base64_data}`
* **Audio**: Raw base64 string with format specification
* **Video**: `data:video/mp4;base64,{base64_data}`

>   **ℹ️ Info**
>
> URLs are more efficient for large files as they don't require local encoding and reduce request payload size. Base64 encoding is required for local files or when the content is not publicly accessible.

  **Note for video URLs**: Video URL support varies by provider. For example, Google Gemini on AI Studio only supports YouTube links. See the [video inputs documentation](/docs/features/multimodal/videos) for provider-specific details.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
