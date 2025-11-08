---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Notion account has appropriate permissions to read user information
* Verify that the OAuth connection includes required scopes for user access and comment creation
* Check that you have permissions to comment on the target pages or discussions

**User Access Issues**

* Ensure you have workspace admin permissions to list all users
* Verify that user IDs are correct and users exist in the workspace
* Check that the workspace allows API access to user information

**Comment Creation Issues**

* Verify that page IDs or discussion IDs are correct and accessible
* Ensure that rich text content follows Notion's API format specifications
* Check that you have comment permissions on the target pages or discussions

**API Rate Limits**

* Be mindful of Notion's API rate limits when making multiple requests
* Implement appropriate delays between requests if needed
* Consider pagination for large user lists

**Parent Object Specification**

* Ensure parent object type is correctly specified (page\_id or discussion\_id)
* Verify that the parent page or discussion exists and is accessible
* Check that the parent object ID format is correct

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Notion integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex communication automation task](./1892-complex-communication-automation-task.md)

**Next:** [Salesforce Integration →](./1894-salesforce-integration.md)
