---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Authentication Errors**

* Ensure your Google account has the necessary permissions for Google Docs access.
* Verify that the OAuth connection includes all required scopes (`https://www.googleapis.com/auth/documents`).

**Document ID Issues**

* Double-check document IDs for correctness.
* Ensure the document exists and is accessible to your account.
* Document IDs can be found in the Google Docs URL.

**Text Insertion and Range Operations**

* When using `insert_text` or `delete_content_range`, ensure index positions are valid.
* Remember that Google Docs uses zero-based indexing.
* The document must have content at the specified index positions.

**Batch Update Request Formatting**

* When using `batch_update`, ensure the `requests` array is correctly formatted according to the Google Docs API documentation.
* Complex updates require specific JSON structures for each request type.

**Replace Text Operations**

* For `replace_text`, ensure the `containsText` parameter exactly matches the text you want to replace.
* Use `matchCase` parameter to control case sensitivity.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Docs integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to format document](./1708-task-to-format-document.md)

**Next:** [Google Drive Integration →](./1710-google-drive-integration.md)
