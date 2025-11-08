---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for file access (e.g., `Files.Read`, `Files.ReadWrite`).
* Verify that the OAuth connection includes all required scopes.

**File Upload Issues**

* Ensure `file_name` and `content` are provided for file uploads.
* Content must be Base64 encoded for binary files.
* Check that you have write permissions to OneDrive.

**File/Folder ID Issues**

* Double-check item IDs for correctness when accessing specific files or folders.
* Item IDs are returned by other operations like `list_files` or `search_files`.
* Ensure the referenced items exist and are accessible.

**Search and Filter Operations**

* Use appropriate search terms for `search_files` operations.
* For `filter` parameters, use proper OData syntax.

**File Operations (Copy/Move)**

* For `move_item`, ensure both `item_id` and `parent_id` are provided.
* For `copy_item`, only `item_id` is required; `parent_id` defaults to root if not specified.
* Verify that destination folders exist and are accessible.

**Sharing Link Creation**

* Ensure the item exists before creating sharing links.
* Choose appropriate `type` and `scope` based on your sharing requirements.
* `anonymous` scope allows access without sign-in; `organization` requires organizational account.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft OneDrive integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to organize and share files](./1821-task-to-organize-and-share-files.md)

**Next:** [Microsoft Outlook Integration →](./1823-microsoft-outlook-integration.md)
