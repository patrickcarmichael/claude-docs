---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Jira account has necessary permissions for the target projects
* Verify that the OAuth connection includes required scopes for Jira API
* Check if you have create/edit permissions for issues in the specified projects

**Invalid Project or Issue Keys**

* Double-check project keys and issue keys for correct format (e.g., "PROJ-123")
* Ensure projects exist and are accessible to your account
* Verify that issue keys reference existing issues

**Issue Type and Status Issues**

* Use JIRA\_GET\_ISSUE\_TYPES\_BY\_PROJECT to get valid issue types for a project
* Use JIRA\_GET\_ISSUE\_STATUS\_BY\_PROJECT to get valid statuses
* Ensure issue types and statuses are available in the target project

**JQL Query Problems**

* Test JQL queries in Jira's issue search before using in API calls
* Ensure field names in JQL are spelled correctly and exist in your Jira instance
* Use proper JQL syntax for complex queries

**Custom Fields and Schema Issues**

* Use JIRA\_DESCRIBE\_ACTION\_SCHEMA to get the correct schema for complex issue types
* Ensure custom field IDs are correct (e.g., "customfield\_10001")
* Verify that custom fields are available in the target project and issue type

**Filter Formula Issues**

* Ensure filter formulas follow the correct JSON structure for disjunctive normal form
* Use valid field names that exist in your Jira configuration
* Test simple filters before building complex multi-condition queries

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Jira integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task using schema-based operations](./1778-task-using-schema-based-operations.md)

**Next:** [Linear Integration →](./1780-linear-integration.md)
