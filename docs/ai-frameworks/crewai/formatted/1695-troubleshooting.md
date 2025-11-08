---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Google account has appropriate permissions for contacts access
* Verify that the OAuth connection includes required scopes for Google Contacts API
* Check that directory access permissions are granted for organization contacts

**Resource Name Format Issues**

* Ensure resource names follow the correct format (e.g., 'people/c123456789' for contacts)
* Verify that contact group resource names use the format 'contactGroups/groupId'
* Check that resource names exist and are accessible

**Search and Query Issues**

* Ensure search queries are properly formatted and not empty
* Use appropriate readMask fields for the data you need
* Verify that search sources are correctly specified (contacts vs profiles)

**Contact Creation and Updates**

* Ensure required fields are provided when creating contacts
* Verify that email addresses and phone numbers are properly formatted
* Check that updatePersonFields parameter includes all fields being updated

**Directory Access Issues**

* Ensure you have appropriate permissions to access organization directory
* Verify that directory sources are correctly specified
* Check that your organization allows API access to directory information

**Pagination and Limits**

* Be mindful of page size limits (varies by endpoint)
* Use pageToken for pagination through large result sets
* Respect API rate limits and implement appropriate delays

**Contact Groups and Organization**

* Ensure contact group names are unique when creating new groups
* Verify that contacts exist before adding them to groups
* Check that you have permissions to modify contact groups

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Contacts integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex contact management task](./1694-complex-contact-management-task.md)

**Next:** [Google Docs Integration →](./1696-google-docs-integration.md)
