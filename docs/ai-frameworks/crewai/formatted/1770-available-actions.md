---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="jira/create_issue">
    **Description:** Create an issue in Jira.

    **Parameters:**

    * `summary` (string, required): Summary - A brief one-line summary of the issue. (example: "The printer stopped working").
    * `project` (string, optional): Project - The project which the issue belongs to. Defaults to the user's first project if not provided. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `issueType` (string, optional): Issue type - Defaults to Task if not provided.
    * `jiraIssueStatus` (string, optional): Status - Defaults to the project's first status if not provided.
    * `assignee` (string, optional): Assignee - Defaults to the authenticated user if not provided.
    * `descriptionType` (string, optional): Description Type - Select the Description Type.
      * Options: `description`, `descriptionJSON`
    * `description` (string, optional): Description - A detailed description of the issue. This field appears only when 'descriptionType' = 'description'.
    * `additionalFields` (string, optional): Additional Fields - Specify any other fields that should be included in JSON format. Use Connect Portal Workflow Settings to allow users to select which Issue Fields to update.
      ```json  theme={null}
      {
        "customfield_10001": "value"
      }
      ```
  </Accordion>

  <Accordion title="jira/update_issue">
    **Description:** Update an issue in Jira.

    **Parameters:**

    * `issueKey` (string, required): Issue Key (example: "TEST-1234").
    * `summary` (string, optional): Summary - A brief one-line summary of the issue. (example: "The printer stopped working").
    * `issueType` (string, optional): Issue type - Use Connect Portal Workflow Settings to allow users to select an Issue Type.
    * `jiraIssueStatus` (string, optional): Status - Use Connect Portal Workflow Settings to allow users to select a Status.
    * `assignee` (string, optional): Assignee - Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `descriptionType` (string, optional): Description Type - Select the Description Type.
      * Options: `description`, `descriptionJSON`
    * `description` (string, optional): Description - A detailed description of the issue. This field appears only when 'descriptionType' = 'description'.
    * `additionalFields` (string, optional): Additional Fields - Specify any other fields that should be included in JSON format.
  </Accordion>

  <Accordion title="jira/get_issue_by_key">
    **Description:** Get an issue by key in Jira.

    **Parameters:**

    * `issueKey` (string, required): Issue Key (example: "TEST-1234").
  </Accordion>

  <Accordion title="jira/filter_issues">
    **Description:** Search issues in Jira using filters.

    **Parameters:**

    * `jqlQuery` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "status",
                "operator": "$stringExactlyMatches",
                "value": "Open"
              }
            ]
          }
        ]
      }
      ```
      Available operators: `$stringExactlyMatches`, `$stringDoesNotExactlyMatch`, `$stringIsIn`, `$stringIsNotIn`, `$stringContains`, `$stringDoesNotContain`, `$stringGreaterThan`, `$stringLessThan`
    * `limit` (string, optional): Limit results - Limit the maximum number of issues to return. Defaults to 10 if left blank.
  </Accordion>

  <Accordion title="jira/search_by_jql">
    **Description:** Search issues by JQL in Jira.

    **Parameters:**

    * `jqlQuery` (string, required): JQL Query (example: "project = PROJECT").
    * `paginationParameters` (object, optional): Pagination parameters for paginated results.
      ```json  theme={null}
      {
        "pageCursor": "cursor_string"
      }
      ```
  </Accordion>

  <Accordion title="jira/update_issue_any">
    **Description:** Update any issue in Jira. Use DESCRIBE\_ACTION\_SCHEMA to get properties schema for this function.

    **Parameters:** No specific parameters - use JIRA\_DESCRIBE\_ACTION\_SCHEMA first to get the expected schema.
  </Accordion>

  <Accordion title="jira/describe_action_schema">
    **Description:** Get the expected schema for an issue type. Use this function first if no other function matches the issue type you want to operate on.

    **Parameters:**

    * `issueTypeId` (string, required): Issue Type ID.
    * `projectKey` (string, required): Project key.
    * `operation` (string, required): Operation Type value, for example CREATE\_ISSUE or UPDATE\_ISSUE.
  </Accordion>

  <Accordion title="jira/get_projects">
    **Description:** Get Projects in Jira.

    **Parameters:**

    * `paginationParameters` (object, optional): Pagination Parameters.
      ```json  theme={null}
      {
        "pageCursor": "cursor_string"
      }
      ```
  </Accordion>

  <Accordion title="jira/get_issue_types_by_project">
    **Description:** Get Issue Types by project in Jira.

    **Parameters:**

    * `project` (string, required): Project key.
  </Accordion>

  <Accordion title="jira/get_issue_types">
    **Description:** Get all Issue Types in Jira.

    **Parameters:** None required.
  </Accordion>

  <Accordion title="jira/get_issue_status_by_project">
    **Description:** Get issue statuses for a given project.

    **Parameters:**

    * `project` (string, required): Project key.
  </Accordion>

  <Accordion title="jira/get_all_assignees_by_project">
    **Description:** Get assignees for a given project.

    **Parameters:**

    * `project` (string, required): Project key.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Jira Integration](./1769-setting-up-jira-integration.md)

**Next:** [Usage Examples →](./1771-usage-examples.md)
