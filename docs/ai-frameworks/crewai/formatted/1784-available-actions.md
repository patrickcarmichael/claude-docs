---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="linear/create_issue">
    **Description:** Create a new issue in Linear.

    **Parameters:**

    * `teamId` (string, required): Team ID - Specify the Team ID of the parent for this new issue. Use Connect Portal Workflow Settings to allow users to select a Team ID. (example: "a70bdf0f-530a-4887-857d-46151b52b47c").
    * `title` (string, required): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `statusId` (string, optional): Status - Specify the state or status of this issue.
    * `priority` (string, optional): Priority - Specify the priority of this issue as an integer.
    * `dueDate` (string, optional): Due Date - Specify the due date of this issue in ISO 8601 format.
    * `cycleId` (string, optional): Cycle ID - Specify the cycle associated with this issue.
    * `additionalFields` (object, optional): Additional Fields.
      ```json  theme={null}
      {
        "assigneeId": "a70bdf0f-530a-4887-857d-46151b52b47c",
        "labelIds": ["a70bdf0f-530a-4887-857d-46151b52b47c"]
      }
      ```
  </Accordion>

  <Accordion title="linear/update_issue">
    **Description:** Update an issue in Linear.

    **Parameters:**

    * `issueId` (string, required): Issue ID - Specify the Issue ID of the issue to update. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
    * `title` (string, optional): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `statusId` (string, optional): Status - Specify the state or status of this issue.
    * `priority` (string, optional): Priority - Specify the priority of this issue as an integer.
    * `dueDate` (string, optional): Due Date - Specify the due date of this issue in ISO 8601 format.
    * `cycleId` (string, optional): Cycle ID - Specify the cycle associated with this issue.
    * `additionalFields` (object, optional): Additional Fields.
      ```json  theme={null}
      {
        "assigneeId": "a70bdf0f-530a-4887-857d-46151b52b47c",
        "labelIds": ["a70bdf0f-530a-4887-857d-46151b52b47c"]
      }
      ```
  </Accordion>

  <Accordion title="linear/get_issue_by_id">
    **Description:** Get an issue by ID in Linear.

    **Parameters:**

    * `issueId` (string, required): Issue ID - Specify the record ID of the issue to fetch. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
  </Accordion>

  <Accordion title="linear/get_issue_by_issue_identifier">
    **Description:** Get an issue by issue identifier in Linear.

    **Parameters:**

    * `externalId` (string, required): External ID - Specify the human-readable Issue identifier of the issue to fetch. (example: "ABC-1").
  </Accordion>

  <Accordion title="linear/search_issue">
    **Description:** Search issues in Linear.

    **Parameters:**

    * `queryTerm` (string, required): Query Term - The search term to look for.
    * `issueFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "title",
                "operator": "$stringContains",
                "value": "bug"
              }
            ]
          }
        ]
      }
      ```
      Available fields: `title`, `number`, `project`, `createdAt`
      Available operators: `$stringExactlyMatches`, `$stringDoesNotExactlyMatch`, `$stringIsIn`, `$stringIsNotIn`, `$stringStartsWith`, `$stringDoesNotStartWith`, `$stringEndsWith`, `$stringDoesNotEndWith`, `$stringContains`, `$stringDoesNotContain`, `$stringGreaterThan`, `$stringLessThan`, `$numberGreaterThanOrEqualTo`, `$numberLessThanOrEqualTo`, `$numberGreaterThan`, `$numberLessThan`, `$dateTimeAfter`, `$dateTimeBefore`
  </Accordion>

  <Accordion title="linear/delete_issue">
    **Description:** Delete an issue in Linear.

    **Parameters:**

    * `issueId` (string, required): Issue ID - Specify the record ID of the issue to delete. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
  </Accordion>

  <Accordion title="linear/archive_issue">
    **Description:** Archive an issue in Linear.

    **Parameters:**

    * `issueId` (string, required): Issue ID - Specify the record ID of the issue to archive. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
  </Accordion>

  <Accordion title="linear/create_sub_issue">
    **Description:** Create a sub-issue in Linear.

    **Parameters:**

    * `parentId` (string, required): Parent ID - Specify the Issue ID for the parent of this new issue.
    * `teamId` (string, required): Team ID - Specify the Team ID of the parent for this new sub-issue. Use Connect Portal Workflow Settings to allow users to select a Team ID. (example: "a70bdf0f-530a-4887-857d-46151b52b47c").
    * `title` (string, required): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `additionalFields` (object, optional): Additional Fields.
      ```json  theme={null}
      {
        "lead": "linear_user_id"
      }
      ```
  </Accordion>

  <Accordion title="linear/create_project">
    **Description:** Create a new project in Linear.

    **Parameters:**

    * `teamIds` (object, required): Team ID - Specify the team ID(s) this project is associated with as a string or a JSON array. Use Connect Portal User Settings to allow your user to select a Team ID.
      ```json  theme={null}
      [
        "a70bdf0f-530a-4887-857d-46151b52b47c",
        "4ac7..."
      ]
      ```
    * `projectName` (string, required): Project Name - Specify the name of the project. (example: "My Linear Project").
    * `description` (string, optional): Project Description - Specify a description for this project.
    * `additionalFields` (object, optional): Additional Fields.
      ```json  theme={null}
      {
        "state": "planned",
        "description": ""
      }
      ```
  </Accordion>

  <Accordion title="linear/update_project">
    **Description:** Update a project in Linear.

    **Parameters:**

    * `projectId` (string, required): Project ID - Specify the ID of the project to update. (example: "a6634484-6061-4ac7-9739-7dc5e52c796b").
    * `projectName` (string, optional): Project Name - Specify the name of the project to update. (example: "My Linear Project").
    * `description` (string, optional): Project Description - Specify a description for this project.
    * `additionalFields` (object, optional): Additional Fields.
      ```json  theme={null}
      {
        "state": "planned",
        "description": ""
      }
      ```
  </Accordion>

  <Accordion title="linear/get_project_by_id">
    **Description:** Get a project by ID in Linear.

    **Parameters:**

    * `projectId` (string, required): Project ID - Specify the Project ID of the project to fetch. (example: "a6634484-6061-4ac7-9739-7dc5e52c796b").
  </Accordion>

  <Accordion title="linear/delete_project">
    **Description:** Delete a project in Linear.

    **Parameters:**

    * `projectId` (string, required): Project ID - Specify the Project ID of the project to delete. (example: "a6634484-6061-4ac7-9739-7dc5e52c796b").
  </Accordion>

  <Accordion title="linear/search_teams">
    **Description:** Search teams in Linear.

    **Parameters:**

    * `teamFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "name",
                "operator": "$stringContains",
                "value": "Engineering"
              }
            ]
          }
        ]
      }
      ```
      Available fields: `id`, `name`
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Linear Integration](./1783-setting-up-linear-integration.md)

**Next:** [Usage Examples →](./1785-usage-examples.md)
