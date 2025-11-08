---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for file access (e.g., `Files.Read.All`, `Files.ReadWrite.All`).
* Verify that the OAuth connection includes all required scopes.

**File Creation Issues**

* When creating text documents, ensure the `file_name` ends with `.txt` extension.
* Verify that you have write permissions to the target location (OneDrive/SharePoint).

**Document Access Issues**

* Double-check document IDs for correctness when accessing specific documents.
* Ensure the referenced documents exist and are accessible.
* Note that this integration works best with text files (.txt) for content operations.

**Content Retrieval Limitations**

* The `get_document_content` action works best with text files (.txt).
* For complex Word documents (.docx), consider using the document properties action to get metadata.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Word integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to organize documents](./1878-task-to-organize-documents.md)

**Next:** [Notion Integration →](./1880-notion-integration.md)
