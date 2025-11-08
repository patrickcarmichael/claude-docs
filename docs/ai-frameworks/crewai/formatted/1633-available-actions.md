---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="clickup/search_tasks">
    **Description:** Search for tasks in ClickUp using advanced filters.

    **Parameters:**

    * `taskFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "statuses%5B%5D",
                "operator": "$stringExactlyMatches",
                "value": "open"
              }
            ]
          }
        ]
      }
      ```
      Available fields: `space_ids%5B%5D`, `project_ids%5B%5D`, `list_ids%5B%5D`, `statuses%5B%5D`, `include_closed`, `assignees%5B%5D`, `tags%5B%5D`, `due_date_gt`, `due_date_lt`, `date_created_gt`, `date_created_lt`, `date_updated_gt`, `date_updated_lt`
  </Accordion>

  <Accordion title="clickup/get_task_in_list">
    **Description:** Get tasks in a specific list in ClickUp.

    **Parameters:**

    * `listId` (string, required): List - Select a List to get tasks from. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `taskFilterFormula` (string, optional): Search for tasks that match specified filters. For example: name=task1.
  </Accordion>

  <Accordion title="clickup/create_task">
    **Description:** Create a task in ClickUp.

    **Parameters:**

    * `listId` (string, required): List - Select a List to create this task in. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `name` (string, required): Name - The task name.
    * `description` (string, optional): Description - Task description.
    * `status` (string, optional): Status - Select a Status for this task. Use Connect Portal User Settings to allow users to select a ClickUp Status.
    * `assignees` (string, optional): Assignees - Select a Member (or an array of member IDs) to be assigned to this task. Use Connect Portal User Settings to allow users to select a ClickUp Member.
    * `dueDate` (string, optional): Due Date - Specify a date for this task to be due on.
    * `additionalFields` (string, optional): Additional Fields - Specify additional fields to include on this task as JSON.
  </Accordion>

  <Accordion title="clickup/update_task">
    **Description:** Update a task in ClickUp.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the task to update.
    * `listId` (string, required): List - Select a List to create this task in. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `name` (string, optional): Name - The task name.
    * `description` (string, optional): Description - Task description.
    * `status` (string, optional): Status - Select a Status for this task. Use Connect Portal User Settings to allow users to select a ClickUp Status.
    * `assignees` (string, optional): Assignees - Select a Member (or an array of member IDs) to be assigned to this task. Use Connect Portal User Settings to allow users to select a ClickUp Member.
    * `dueDate` (string, optional): Due Date - Specify a date for this task to be due on.
    * `additionalFields` (string, optional): Additional Fields - Specify additional fields to include on this task as JSON.
  </Accordion>

  <Accordion title="clickup/delete_task">
    **Description:** Delete a task in ClickUp.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the task to delete.
  </Accordion>

  <Accordion title="clickup/get_list">
    **Description:** Get List information in ClickUp.

    **Parameters:**

    * `spaceId` (string, required): Space ID - The ID of the space containing the lists.
  </Accordion>

  <Accordion title="clickup/get_custom_fields_in_list">
    **Description:** Get Custom Fields in a List in ClickUp.

    **Parameters:**

    * `listId` (string, required): List ID - The ID of the list to get custom fields from.
  </Accordion>

  <Accordion title="clickup/get_all_fields_in_list">
    **Description:** Get All Fields in a List in ClickUp.

    **Parameters:**

    * `listId` (string, required): List ID - The ID of the list to get all fields from.
  </Accordion>

  <Accordion title="clickup/get_space">
    **Description:** Get Space information in ClickUp.

    **Parameters:**

    * `spaceId` (string, optional): Space ID - The ID of the space to retrieve.
  </Accordion>

  <Accordion title="clickup/get_folders">
    **Description:** Get Folders in ClickUp.

    **Parameters:**

    * `spaceId` (string, required): Space ID - The ID of the space containing the folders.
  </Accordion>

  <Accordion title="clickup/get_member">
    **Description:** Get Member information in ClickUp.

    **Parameters:** None required.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up ClickUp Integration](./1632-setting-up-clickup-integration.md)

**Next:** [Usage Examples →](./1634-usage-examples.md)
