---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Microsoft account has appropriate permissions for SharePoint sites
* Verify that the OAuth connection includes required scopes (Sites.Read.All, Sites.ReadWrite.All)
* Check that you have access to the specific sites and lists you're trying to access

**Site and List ID Issues**

* Verify that site IDs and list IDs are correct and properly formatted
* Ensure that sites and lists exist and are accessible to your account
* Use the get\_sites and get\_site\_lists actions to discover valid IDs

**Field and Schema Issues**

* Ensure field names match exactly with the SharePoint list schema
* Verify that required fields are included when creating or updating list items
* Check that field types and values are compatible with the list column definitions

**File Upload Issues**

* Ensure file paths are properly formatted and don't contain invalid characters
* Verify that you have write permissions to the target document library
* Check that file content is properly encoded for upload

**OData Query Issues**

* Use proper OData syntax for filter, select, expand, and orderby parameters
* Verify that property names used in queries exist in the target resources
* Test simple queries before building complex filter expressions

**Pagination and Performance**

* Use top and skip parameters appropriately for large result sets
* Implement proper pagination for lists with many items
* Consider using select parameters to return only needed properties

**Document Library Operations**

* Ensure you have proper permissions for document library operations
* Verify that drive item IDs are correct when deleting files or folders
* Check that file paths don't conflict with existing content

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft SharePoint integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task for data integration](./1850-task-for-data-integration.md)

**Next:** [Microsoft Teams Integration →](./1852-microsoft-teams-integration.md)
