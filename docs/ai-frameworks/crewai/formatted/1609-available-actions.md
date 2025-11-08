---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="asana/create_comment">
    **Description:** Create a comment in Asana.

    **Parameters:**

    * `task` (string, required): Task ID - The ID of the Task the comment will be added to. The comment will be authored by the currently authenticated user.
    * `text` (string, required): Text (example: "This is a comment.").
  </Accordion>

  <Accordion title="asana/create_project">
    **Description:** Create a project in Asana.

    **Parameters:**

    * `name` (string, required): Name (example: "Stuff to buy").
    * `workspace` (string, required): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Projects in. Defaults to the user's first Workspace if left blank.
    * `team` (string, optional): Team - Use Connect Portal Workflow Settings to allow users to select which Team to share this Project with. Defaults to the user's first Team if left blank.
    * `notes` (string, optional): Notes (example: "These are things we need to purchase.").
  </Accordion>

  <Accordion title="asana/get_projects">
    **Description:** Get a list of projects in Asana.

    **Parameters:**

    * `archived` (string, optional): Archived - Choose "true" to show archived projects, "false" to display only active projects, or "default" to show both archived and active projects.
      * Options: `default`, `true`, `false`
  </Accordion>

  <Accordion title="asana/get_project_by_id">
    **Description:** Get a project by ID in Asana.

    **Parameters:**

    * `projectFilterId` (string, required): Project ID.
  </Accordion>

  <Accordion title="asana/create_task">
    **Description:** Create a task in Asana.

    **Parameters:**

    * `name` (string, required): Name (example: "Task Name").
    * `workspace` (string, optional): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Tasks in. Defaults to the user's first Workspace if left blank..
    * `project` (string, optional): Project - Use Connect Portal Workflow Settings to allow users to select which Project to create this Task in.
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

  <Accordion title="asana/update_task">
    **Description:** Update a task in Asana.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the Task that will be updated.
    * `completeStatus` (string, optional): Completed Status.
      * Options: `true`, `false`
    * `name` (string, optional): Name (example: "Task Name").
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

  <Accordion title="asana/get_tasks">
    **Description:** Get a list of tasks in Asana.

    **Parameters:**

    * `workspace` (string, optional): Workspace - The ID of the Workspace to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Workspace.
    * `project` (string, optional): Project - The ID of the Project to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `assignee` (string, optional): Assignee - The ID of the assignee to filter tasks on. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `completedSince` (string, optional): Completed since - Only return tasks that are either incomplete or that have been completed since this time (ISO or Unix timestamp). (example: "2014-04-25T16:15:47-04:00").
  </Accordion>

  <Accordion title="asana/get_tasks_by_id">
    **Description:** Get a list of tasks by ID in Asana.

    **Parameters:**

    * `taskId` (string, required): Task ID.
  </Accordion>

  <Accordion title="asana/get_task_by_external_id">
    **Description:** Get a task by external ID in Asana.

    **Parameters:**

    * `gid` (string, required): External ID - The ID that this task is associated or synced with, from your application.
  </Accordion>

  <Accordion title="asana/add_task_to_section">
    **Description:** Add a task to a section in Asana.

    **Parameters:**

    * `sectionId` (string, required): Section ID - The ID of the section to add this task to.
    * `taskId` (string, required): Task ID - The ID of the task. (example: "1204619611402340").
    * `beforeTaskId` (string, optional): Before Task ID - The ID of a task in this section that this task will be inserted before. Cannot be used with After Task ID. (example: "1204619611402340").
    * `afterTaskId` (string, optional): After Task ID - The ID of a task in this section that this task will be inserted after. Cannot be used with Before Task ID. (example: "1204619611402340").
  </Accordion>

  <Accordion title="asana/get_teams">
    **Description:** Get a list of teams in Asana.

    **Parameters:**

    * `workspace` (string, required): Workspace - Returns the teams in this workspace visible to the authorized user.
  </Accordion>

  <Accordion title="asana/get_workspaces">
    **Description:** Get a list of workspaces in Asana.

    **Parameters:** None required.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Asana Integration](./1608-setting-up-asana-integration.md)

**Next:** [Usage Examples →](./1610-usage-examples.md)
