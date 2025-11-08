---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Linear account has necessary permissions for the target workspace
* Verify that the OAuth connection includes required scopes for Linear API
* Check if you have create/edit permissions for issues and projects in the workspace

**Invalid IDs and References**

* Double-check team IDs, issue IDs, and project IDs for correct UUID format
* Ensure referenced entities (teams, projects, cycles) exist and are accessible
* Verify that issue identifiers follow the correct format (e.g., "ABC-1")

**Team and Project Association Issues**

* Use LINEAR\_SEARCH\_TEAMS to get valid team IDs before creating issues or projects
* Ensure teams exist and are active in your workspace
* Verify that team IDs are properly formatted as UUIDs

**Issue Status and Priority Problems**

* Check that status IDs reference valid workflow states for the team
* Ensure priority values are within the valid range for your Linear configuration
* Verify that custom fields and labels exist before referencing them

**Date and Time Format Issues**

* Use ISO 8601 format for due dates and timestamps
* Ensure time zones are handled correctly for due date calculations
* Verify that date values are valid and in the future for due dates

**Search and Filter Issues**

* Ensure search queries are properly formatted and not empty
* Use valid field names in filter formulas: `title`, `number`, `project`, `createdAt`
* Test simple filters before building complex multi-condition queries
* Verify that operator types match the data types of the fields being filtered

**Sub-issue Creation Problems**

* Ensure parent issue IDs are valid and accessible
* Verify that the team ID for sub-issues matches or is compatible with the parent issue's team
* Check that parent issues are not already archived or deleted

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Linear integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex workflow automation task](./1792-complex-workflow-automation-task.md)

**Next:** [Microsoft Excel Integration →](./1794-microsoft-excel-integration.md)
