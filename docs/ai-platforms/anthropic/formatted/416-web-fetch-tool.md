---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Web fetch tool

Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool


The web fetch tool allows Claude to retrieve full content from specified web pages and PDF documents.

>   **📝 Note**
>
> The web fetch tool is currently in beta. To enable it, use the beta header `web-fetch-2025-09-10` in your API requests.

  Please use [this form](https://forms.gle/NhWcgmkcvPCMmPE86) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation.

>   **⚠️ Warning**
>
> Enabling the web fetch tool in environments where Claude processes untrusted input alongside sensitive data poses data exfiltration risks. We recommend only using this tool in trusted environments or when handling non-sensitive data.

  To minimize exfiltration risks, Claude is not allowed to dynamically construct URLs. Claude can only fetch URLs that have been explicitly provided by the user or that come from previous web search or web fetch results. However, there is still residual risk that should be carefully considered when using this tool.

  If data exfiltration is a concern, consider:

  * Disabling the web fetch tool entirely
  * Using the `max_uses` parameter to limit the number of requests
  * Using the `allowed_domains` parameter to restrict to known safe domains

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
