# Create an agent with Asana capabilities

**Navigation:** [← Previous](./07-traces.md) | [Index](./index.md) | [Next →](./09-task-using-schema-based-operations.md)

---

# Create an agent with Asana capabilities
asana_agent = Agent(
    role="Project Manager",
    goal="Manage tasks and projects in Asana efficiently",
    backstory="An AI assistant specialized in project management and task coordination.",
    apps=['asana']  # All Asana actions will be available
)


# Task to create a new project
create_project_task = Task(
    description="Create a new project called 'Q1 Marketing Campaign' in the Marketing workspace",
    agent=asana_agent,
    expected_output="Confirmation that the project was created successfully with project ID"
)


# Run the task
crew = Crew(
    agents=[asana_agent],
    tasks=[create_project_task]
)

crew.kickoff()
```

### Filtering Specific Asana Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Asana actions only
task_manager_agent = Agent(
    role="Task Manager",
    goal="Create and manage tasks efficiently",
    backstory="An AI assistant that focuses on task creation and management.",
    apps=[
        'asana/create_task',
        'asana/update_task',
        'asana/get_tasks'
    ]  # Specific Asana actions
)


# Task to create and assign a task
task_management = Task(
    description="Create a task called 'Review quarterly reports' and assign it to the appropriate team member",
    agent=task_manager_agent,
    expected_output="Task created and assigned successfully"
)

crew = Crew(
    agents=[task_manager_agent],
    tasks=[task_management]
)

crew.kickoff()
```

### Advanced Project Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate project activities and track progress",
    backstory="An experienced project coordinator who ensures projects run smoothly.",
    apps=['asana']
)


# Complex task involving multiple Asana operations
coordination_task = Task(
    description="""
    1. Get all active projects in the workspace
    2. For each project, get the list of incomplete tasks
    3. Create a summary report task in the 'Management Reports' project
    4. Add comments to overdue tasks to request status updates
    """,
    agent=project_coordinator,
    expected_output="Summary report created and status update requests sent for overdue tasks"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
```



# Box Integration
Source: https://docs.crewai.com/en/enterprise/integrations/box

File storage and document management with Box integration for CrewAI.


## Overview

Enable your agents to manage files, folders, and documents through Box. Upload files, organize folder structures, search content, and streamline your team's document management with AI-powered automation.


## Prerequisites

Before using the Box integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Box account with appropriate permissions
* Connected your Box account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Box Integration

### 1. Connect Your Box Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Box** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file and folder management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="box/save_file">
    **Description:** Save a file from URL in Box.

    **Parameters:**

    * `fileAttributes` (object, required): Attributes - File metadata including name, parent folder, and timestamps.
      ```json  theme={null}
      {
        "content_created_at": "2012-12-12T10:53:43-08:00",
        "content_modified_at": "2012-12-12T10:53:43-08:00",
        "name": "qwerty.png",
        "parent": { "id": "1234567" }
      }
      ```
    * `file` (string, required): File URL - Files must be smaller than 50MB in size. (example: "[https://picsum.photos/200/300](https://picsum.photos/200/300)").
  </Accordion>

  <Accordion title="box/save_file_from_object">
    **Description:** Save a file in Box.

    **Parameters:**

    * `file` (string, required): File - Accepts a File Object containing file data. Files must be smaller than 50MB in size.
    * `fileName` (string, required): File Name (example: "qwerty.png").
    * `folder` (string, optional): Folder - Use Connect Portal Workflow Settings to allow users to select the File's Folder destination. Defaults to the user's root folder if left blank.
  </Accordion>

  <Accordion title="box/get_file_by_id">
    **Description:** Get a file by ID in Box.

    **Parameters:**

    * `fileId` (string, required): File ID - The unique identifier that represents a file. (example: "12345").
  </Accordion>

  <Accordion title="box/list_files">
    **Description:** List files in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
    * `filterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "direction",
                "operator": "$stringExactlyMatches",
                "value": "ASC"
              }
            ]
          }
        ]
      }
      ```
  </Accordion>

  <Accordion title="box/create_folder">
    **Description:** Create a folder in Box.

    **Parameters:**

    * `folderName` (string, required): Name - The name for the new folder. (example: "New Folder").
    * `folderParent` (object, required): Parent Folder - The parent folder where the new folder will be created.
      ```json  theme={null}
      {
        "id": "123456"
      }
      ```
  </Accordion>

  <Accordion title="box/move_folder">
    **Description:** Move a folder in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
    * `folderName` (string, required): Name - The name for the folder. (example: "New Folder").
    * `folderParent` (object, required): Parent Folder - The new parent folder destination.
      ```json  theme={null}
      {
        "id": "123456"
      }
      ```
  </Accordion>

  <Accordion title="box/get_folder_by_id">
    **Description:** Get a folder by ID in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
  </Accordion>

  <Accordion title="box/search_folders">
    **Description:** Search folders in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The folder to search within.
    * `filterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "sort",
                "operator": "$stringExactlyMatches",
                "value": "name"
              }
            ]
          }
        ]
      }
      ```
  </Accordion>

  <Accordion title="box/delete_folder">
    **Description:** Delete a folder in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
    * `recursive` (boolean, optional): Recursive - Delete a folder that is not empty by recursively deleting the folder and all of its content.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Box Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Box capabilities
box_agent = Agent(
    role="Document Manager",
    goal="Manage files and folders in Box efficiently",
    backstory="An AI assistant specialized in document management and file organization.",
    apps=['box']  # All Box actions will be available
)


# Task to create a folder structure
create_structure_task = Task(
    description="Create a folder called 'Project Files' in the root directory and upload a document from URL",
    agent=box_agent,
    expected_output="Folder created and file uploaded successfully"
)


# Run the task
crew = Crew(
    agents=[box_agent],
    tasks=[create_structure_task]
)

crew.kickoff()
```

### Filtering Specific Box Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Box actions only
file_organizer_agent = Agent(
    role="File Organizer",
    goal="Organize and manage file storage efficiently",
    backstory="An AI assistant that focuses on file organization and storage management.",
    apps=['box/create_folder', 'box/save_file', 'box/list_files']  # Specific Box actions
)


# Task to organize files
organization_task = Task(
    description="Create a folder structure for the marketing team and organize existing files",
    agent=file_organizer_agent,
    expected_output="Folder structure created and files organized"
)

crew = Crew(
    agents=[file_organizer_agent],
    tasks=[organization_task]
)

crew.kickoff()
```

### Advanced File Management

```python  theme={null}
from crewai import Agent, Task, Crew

file_manager = Agent(
    role="File Manager",
    goal="Maintain organized file structure and manage document lifecycle",
    backstory="An experienced file manager who ensures documents are properly organized and accessible.",
    apps=['box']
)


# Complex task involving multiple Box operations
management_task = Task(
    description="""
    1. List all files in the root folder
    2. Create monthly archive folders for the current year
    3. Move old files to appropriate archive folders
    4. Generate a summary report of the file organization
    """,
    agent=file_manager,
    expected_output="Files organized into archive structure with summary report"
)

crew = Crew(
    agents=[file_manager],
    tasks=[management_task]
)

crew.kickoff()
```



# ClickUp Integration
Source: https://docs.crewai.com/en/enterprise/integrations/clickup

Task and productivity management with ClickUp integration for CrewAI.


## Overview

Enable your agents to manage tasks, projects, and productivity workflows through ClickUp. Create and update tasks, organize projects, manage team assignments, and streamline your productivity management with AI-powered automation.


## Prerequisites

Before using the ClickUp integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A ClickUp account with appropriate permissions
* Connected your ClickUp account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up ClickUp Integration

### 1. Connect Your ClickUp Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **ClickUp** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for task and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


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


## Usage Examples

### Basic ClickUp Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Clickup capabilities
clickup_agent = Agent(
    role="Task Manager",
    goal="Manage tasks and projects in ClickUp efficiently",
    backstory="An AI assistant specialized in task management and productivity coordination.",
    apps=['clickup']  # All Clickup actions will be available
)


# Task to create a new task
create_task = Task(
    description="Create a task called 'Review Q1 Reports' in the Marketing list with high priority",
    agent=clickup_agent,
    expected_output="Task created successfully with task ID"
)


# Run the task
crew = Crew(
    agents=[clickup_agent],
    tasks=[create_task]
)

crew.kickoff()
```

### Filtering Specific ClickUp Tools

```python  theme={null}

task_coordinator = Agent(
    role="Task Coordinator",
    goal="Create and manage tasks efficiently",
    backstory="An AI assistant that focuses on task creation and status management.",
    apps=['clickup/create_task']
)


# Task to manage task workflow
task_workflow = Task(
    description="Create a task for project planning and assign it to the development team",
    agent=task_coordinator,
    expected_output="Task created and assigned successfully"
)

crew = Crew(
    agents=[task_coordinator],
    tasks=[task_workflow]
)

crew.kickoff()
```

### Advanced Project Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_manager = Agent(
    role="Project Manager",
    goal="Coordinate project activities and track team productivity",
    backstory="An experienced project manager who ensures projects are delivered on time.",
    apps=['clickup']
)


# Complex task involving multiple ClickUp operations
project_coordination = Task(
    description="""
    1. Get all open tasks in the current space
    2. Identify overdue tasks and update their status
    3. Create a weekly report task summarizing project progress
    4. Assign the report task to the team lead
    """,
    agent=project_manager,
    expected_output="Project status updated and weekly report task created and assigned"
)

crew = Crew(
    agents=[project_manager],
    tasks=[project_coordination]
)

crew.kickoff()
```

### Task Search and Management

```python  theme={null}
from crewai import Agent, Task, Crew

task_analyst = Agent(
    role="Task Analyst",
    goal="Analyze task patterns and optimize team productivity",
    backstory="An AI assistant that analyzes task data to improve team efficiency.",
    apps=['clickup']
)


# Task to analyze and optimize task distribution
task_analysis = Task(
    description="""
    Search for all tasks assigned to team members in the last 30 days,
    analyze completion patterns, and create optimization recommendations
    """,
    agent=task_analyst,
    expected_output="Task analysis report with optimization recommendations"
)

crew = Crew(
    agents=[task_analyst],
    tasks=[task_analysis]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with ClickUp integration setup or troubleshooting.
</Card>



# GitHub Integration
Source: https://docs.crewai.com/en/enterprise/integrations/github

Repository and issue management with GitHub integration for CrewAI.


## Overview

Enable your agents to manage repositories, issues, and releases through GitHub. Create and update issues, manage releases, track project development, and streamline your software development workflow with AI-powered automation.


## Prerequisites

Before using the GitHub integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A GitHub account with appropriate repository permissions
* Connected your GitHub account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up GitHub Integration

### 1. Connect Your GitHub Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **GitHub** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for repository and issue management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="github/create_issue">
    **Description:** Create an issue in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `title` (string, required): Issue Title - Specify the title of the issue to create.
    * `body` (string, optional): Issue Body - Specify the body contents of the issue to create.
    * `assignees` (string, optional): Assignees - Specify the assignee(s)' GitHub login as an array of strings for this issue. (example: `["octocat"]`).
  </Accordion>

  <Accordion title="github/update_issue">
    **Description:** Update an issue in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `issue_number` (string, required): Issue Number - Specify the number of the issue to update.
    * `title` (string, required): Issue Title - Specify the title of the issue to update.
    * `body` (string, optional): Issue Body - Specify the body contents of the issue to update.
    * `assignees` (string, optional): Assignees - Specify the assignee(s)' GitHub login as an array of strings for this issue. (example: `["octocat"]`).
    * `state` (string, optional): State - Specify the updated state of the issue.
      * Options: `open`, `closed`
  </Accordion>

  <Accordion title="github/get_issue_by_number">
    **Description:** Get an issue by number in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `issue_number` (string, required): Issue Number - Specify the number of the issue to fetch.
  </Accordion>

  <Accordion title="github/lock_issue">
    **Description:** Lock an issue in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `issue_number` (string, required): Issue Number - Specify the number of the issue to lock.
    * `lock_reason` (string, required): Lock Reason - Specify a reason for locking the issue or pull request conversation.
      * Options: `off-topic`, `too heated`, `resolved`, `spam`
  </Accordion>

  <Accordion title="github/search_issue">
    **Description:** Search for issues in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `filter` (object, required): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "assignee",
                "operator": "$stringExactlyMatches",
                "value": "octocat"
              }
            ]
          }
        ]
      }
      ```
      Available fields: `assignee`, `creator`, `mentioned`, `labels`
  </Accordion>

  <Accordion title="github/create_release">
    **Description:** Create a release in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `tag_name` (string, required): Name - Specify the name of the release tag to be created. (example: "v1.0.0").
    * `target_commitish` (string, optional): Target - Specify the target of the release. This can either be a branch name or a commit SHA. Defaults to the main branch. (example: "master").
    * `body` (string, optional): Body - Specify a description for this release.
    * `draft` (string, optional): Draft - Specify whether the created release should be a draft (unpublished) release.
      * Options: `true`, `false`
    * `prerelease` (string, optional): Prerelease - Specify whether the created release should be a prerelease.
      * Options: `true`, `false`
    * `discussion_category_name` (string, optional): Discussion Category Name - If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository.
    * `generate_release_notes` (string, optional): Release Notes - Specify whether the created release should automatically create release notes using the provided name and body specified.
      * Options: `true`, `false`
  </Accordion>

  <Accordion title="github/update_release">
    **Description:** Update a release in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `id` (string, required): Release ID - Specify the ID of the release to update.
    * `tag_name` (string, optional): Name - Specify the name of the release tag to be updated. (example: "v1.0.0").
    * `target_commitish` (string, optional): Target - Specify the target of the release. This can either be a branch name or a commit SHA. Defaults to the main branch. (example: "master").
    * `body` (string, optional): Body - Specify a description for this release.
    * `draft` (string, optional): Draft - Specify whether the created release should be a draft (unpublished) release.
      * Options: `true`, `false`
    * `prerelease` (string, optional): Prerelease - Specify whether the created release should be a prerelease.
      * Options: `true`, `false`
    * `discussion_category_name` (string, optional): Discussion Category Name - If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository.
    * `generate_release_notes` (string, optional): Release Notes - Specify whether the created release should automatically create release notes using the provided name and body specified.
      * Options: `true`, `false`
  </Accordion>

  <Accordion title="github/get_release_by_id">
    **Description:** Get a release by ID in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `id` (string, required): Release ID - Specify the release ID of the release to fetch.
  </Accordion>

  <Accordion title="github/get_release_by_tag_name">
    **Description:** Get a release by tag name in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `tag_name` (string, required): Name - Specify the tag of the release to fetch. (example: "v1.0.0").
  </Accordion>

  <Accordion title="github/delete_release">
    **Description:** Delete a release in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `id` (string, required): Release ID - Specify the ID of the release to delete.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic GitHub Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Github capabilities
github_agent = Agent(
    role="Repository Manager",
    goal="Manage GitHub repositories, issues, and releases efficiently",
    backstory="An AI assistant specialized in repository management and issue tracking.",
    apps=['github']  # All Github actions will be available
)


# Task to create a new issue
create_issue_task = Task(
    description="Create a bug report issue for the login functionality in the main repository",
    agent=github_agent,
    expected_output="Issue created successfully with issue number"
)


# Run the task
crew = Crew(
    agents=[github_agent],
    tasks=[create_issue_task]
)

crew.kickoff()
```

### Filtering Specific GitHub Tools

```python  theme={null}

issue_manager = Agent(
    role="Issue Manager",
    goal="Create and manage GitHub issues efficiently",
    backstory="An AI assistant that focuses on issue tracking and management.",
    apps=['github/create_issue']
)


# Task to manage issue workflow
issue_workflow = Task(
    description="Create a feature request issue and assign it to the development team",
    agent=issue_manager,
    expected_output="Feature request issue created and assigned successfully"
)

crew = Crew(
    agents=[issue_manager],
    tasks=[issue_workflow]
)

crew.kickoff()
```

### Release Management

```python  theme={null}
from crewai import Agent, Task, Crew

release_manager = Agent(
    role="Release Manager",
    goal="Manage software releases and versioning",
    backstory="An experienced release manager who handles version control and release processes.",
    apps=['github']
)


# Task to create a new release
release_task = Task(
    description="""
    Create a new release v2.1.0 for the project with:
    - Auto-generated release notes
    - Target the main branch
    - Include a description of new features and bug fixes
    """,
    agent=release_manager,
    expected_output="Release v2.1.0 created successfully with release notes"
)

crew = Crew(
    agents=[release_manager],
    tasks=[release_task]
)

crew.kickoff()
```

### Issue Tracking and Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Track and coordinate project issues and development progress",
    backstory="An AI assistant that helps coordinate development work and track project progress.",
    apps=['github']
)


# Complex task involving multiple GitHub operations
coordination_task = Task(
    description="""
    1. Search for all open issues assigned to the current milestone
    2. Identify overdue issues and update their priority labels
    3. Create a weekly progress report issue
    4. Lock resolved issues that have been inactive for 30 days
    """,
    agent=project_coordinator,
    expected_output="Project coordination completed with progress report and issue management"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with GitHub integration setup or troubleshooting.
</Card>



# Gmail Integration
Source: https://docs.crewai.com/en/enterprise/integrations/gmail

Email and contact management with Gmail integration for CrewAI.


## Overview

Enable your agents to manage emails, contacts, and drafts through Gmail. Send emails, search messages, manage contacts, create drafts, and streamline your email communications with AI-powered automation.


## Prerequisites

Before using the Gmail integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Gmail account with appropriate permissions
* Connected your Gmail account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Gmail Integration

### 1. Connect Your Gmail Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Gmail** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for email and contact management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="gmail/fetch_emails">
    **Description:** Retrieve a list of messages.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `q` (string, optional): Search query to filter messages (e.g., 'from:[someone@example.com](mailto:someone@example.com) is:unread').
    * `maxResults` (integer, optional): Maximum number of messages to return (1-500). (default: 100)
    * `pageToken` (string, optional): Page token to retrieve a specific page of results.
    * `labelIds` (array, optional): Only return messages with labels that match all of the specified label IDs.
    * `includeSpamTrash` (boolean, optional): Include messages from SPAM and TRASH in the results. (default: false)
  </Accordion>

  <Accordion title="gmail/send_email">
    **Description:** Send an email.

    **Parameters:**

    * `to` (string, required): Recipient email address.
    * `subject` (string, required): Email subject line.
    * `body` (string, required): Email message content.
    * `userId` (string, optional): The user's email address or 'me' for the authenticated user. (default: "me")
    * `cc` (string, optional): CC email addresses (comma-separated).
    * `bcc` (string, optional): BCC email addresses (comma-separated).
    * `from` (string, optional): Sender email address (if different from authenticated user).
    * `replyTo` (string, optional): Reply-to email address.
    * `threadId` (string, optional): Thread ID if replying to an existing conversation.
  </Accordion>

  <Accordion title="gmail/delete_email">
    **Description:** Delete an email by ID.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user.
    * `id` (string, required): The ID of the message to delete.
  </Accordion>

  <Accordion title="gmail/create_draft">
    **Description:** Create a new draft email.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user.
    * `message` (object, required): Message object containing the draft content.
      * `raw` (string, required): Base64url encoded email message.
  </Accordion>

  <Accordion title="gmail/get_message">
    **Description:** Retrieve a specific message by ID.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the message to retrieve.
    * `format` (string, optional): The format to return the message in. Options: "full", "metadata", "minimal", "raw". (default: "full")
    * `metadataHeaders` (array, optional): When given and format is METADATA, only include headers specified.
  </Accordion>

  <Accordion title="gmail/get_attachment">
    **Description:** Retrieve a message attachment.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `messageId` (string, required): The ID of the message containing the attachment.
    * `id` (string, required): The ID of the attachment to retrieve.
  </Accordion>

  <Accordion title="gmail/fetch_thread">
    **Description:** Retrieve a specific email thread by ID.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to retrieve.
    * `format` (string, optional): The format to return the messages in. Options: "full", "metadata", "minimal". (default: "full")
    * `metadataHeaders` (array, optional): When given and format is METADATA, only include headers specified.
  </Accordion>

  <Accordion title="gmail/modify_thread">
    **Description:** Modify the labels applied to a thread.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to modify.
    * `addLabelIds` (array, optional): A list of IDs of labels to add to this thread.
    * `removeLabelIds` (array, optional): A list of IDs of labels to remove from this thread.
  </Accordion>

  <Accordion title="gmail/trash_thread">
    **Description:** Move a thread to the trash.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to trash.
  </Accordion>

  <Accordion title="gmail/untrash_thread">
    **Description:** Remove a thread from the trash.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to untrash.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Gmail Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Gmail capabilities
gmail_agent = Agent(
    role="Email Manager",
    goal="Manage email communications and messages efficiently",
    backstory="An AI assistant specialized in email management and communication.",
    apps=['gmail']  # All Gmail actions will be available
)


# Task to send a follow-up email
send_email_task = Task(
    description="Send a follow-up email to john@example.com about the project update meeting",
    agent=gmail_agent,
    expected_output="Email sent successfully with confirmation"
)


# Run the task
crew = Crew(
    agents=[gmail_agent],
    tasks=[send_email_task]
)

crew.kickoff()
```

### Filtering Specific Gmail Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Gmail actions only
email_coordinator = Agent(
    role="Email Coordinator",
    goal="Coordinate email communications and manage drafts",
    backstory="An AI assistant that focuses on email coordination and draft management.",
    apps=[
        'gmail/send_email',
        'gmail/fetch_emails',
        'gmail/create_draft'
    ]
)


# Task to prepare and send emails
email_coordination = Task(
    description="Search for emails from the marketing team, create a summary draft, and send it to stakeholders",
    agent=email_coordinator,
    expected_output="Summary email sent to stakeholders"
)

crew = Crew(
    agents=[email_coordinator],
    tasks=[email_coordination]
)

crew.kickoff()
```

### Email Search and Analysis

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with Gmail search and analysis capabilities
email_analyst = Agent(
    role="Email Analyst",
    goal="Analyze email patterns and provide insights",
    backstory="An AI assistant that analyzes email data to provide actionable insights.",
    apps=['gmail/fetch_emails', 'gmail/get_message']  # Specific actions for email analysis
)


# Task to analyze email patterns
analysis_task = Task(
    description="""
    Search for all unread emails from the last 7 days,
    categorize them by sender domain,
    and create a summary report of communication patterns
    """,
    agent=email_analyst,
    expected_output="Email analysis report with communication patterns and recommendations"
)

crew = Crew(
    agents=[email_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Thread Management

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with Gmail thread management capabilities
thread_manager = Agent(
    role="Thread Manager",
    goal="Organize and manage email threads efficiently",
    backstory="An AI assistant that specializes in email thread organization and management.",
    apps=[
        'gmail/fetch_thread',
        'gmail/modify_thread',
        'gmail/trash_thread'
    ]
)


# Task to organize email threads
thread_task = Task(
    description="""
    1. Fetch all threads from the last month
    2. Apply appropriate labels to organize threads by project
    3. Archive or trash threads that are no longer relevant
    """,
    agent=thread_manager,
    expected_output="Email threads organized with appropriate labels and cleanup completed"
)

crew = Crew(
    agents=[thread_manager],
    tasks=[thread_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Gmail integration setup or troubleshooting.
</Card>



# Google Calendar Integration
Source: https://docs.crewai.com/en/enterprise/integrations/google_calendar

Event and schedule management with Google Calendar integration for CrewAI.


## Overview

Enable your agents to manage calendar events, schedules, and availability through Google Calendar. Create and update events, manage attendees, check availability, and streamline your scheduling workflows with AI-powered automation.


## Prerequisites

Before using the Google Calendar integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Google account with Google Calendar access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Google Calendar Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Calendar** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for calendar access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="google_calendar/get_availability">
    **Description:** Get calendar availability (free/busy information).

    **Parameters:**

    * `timeMin` (string, required): Start time (RFC3339 format)
    * `timeMax` (string, required): End time (RFC3339 format)
    * `items` (array, required): Calendar IDs to check
      ```json  theme={null}
      [
        {
          "id": "calendar_id"
        }
      ]
      ```
    * `timeZone` (string, optional): Time zone used in the response. The default is UTC.
    * `groupExpansionMax` (integer, optional): Maximal number of calendar identifiers to be provided for a single group. Maximum: 100
    * `calendarExpansionMax` (integer, optional): Maximal number of calendars for which FreeBusy information is to be provided. Maximum: 50
  </Accordion>

  <Accordion title="google_calendar/create_event">
    **Description:** Create a new event in the specified calendar.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `summary` (string, required): Event title/summary
    * `start_dateTime` (string, required): Start time in RFC3339 format (e.g., 2024-01-20T10:00:00-07:00)
    * `end_dateTime` (string, required): End time in RFC3339 format
    * `description` (string, optional): Event description
    * `timeZone` (string, optional): Time zone (e.g., America/Los\_Angeles)
    * `location` (string, optional): Geographic location of the event as free-form text.
    * `attendees` (array, optional): List of attendees for the event.
      ```json  theme={null}
      [
        {
          "email": "attendee@example.com",
          "displayName": "Attendee Name",
          "optional": false
        }
      ]
      ```
    * `reminders` (object, optional): Information about the event's reminders.
      ```json  theme={null}
      {
        "useDefault": true,
        "overrides": [
          {
            "method": "email",
            "minutes": 15
          }
        ]
      }
      ```
    * `conferenceData` (object, optional): The conference-related information, such as details of a Google Meet conference.
      ```json  theme={null}
      {
        "createRequest": {
          "requestId": "unique-request-id",
          "conferenceSolutionKey": {
            "type": "hangoutsMeet"
          }
        }
      }
      ```
    * `visibility` (string, optional): Visibility of the event. Options: default, public, private, confidential. Default: default
    * `transparency` (string, optional): Whether the event blocks time on the calendar. Options: opaque, transparent. Default: opaque
  </Accordion>

  <Accordion title="google_calendar/view_events">
    **Description:** Retrieve events for the specified calendar.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `timeMin` (string, optional): Lower bound for events (RFC3339)
    * `timeMax` (string, optional): Upper bound for events (RFC3339)
    * `maxResults` (integer, optional): Maximum number of events (default 10). Minimum: 1, Maximum: 2500
    * `orderBy` (string, optional): The order of the events returned in the result. Options: startTime, updated. Default: startTime
    * `singleEvents` (boolean, optional): Whether to expand recurring events into instances and only return single one-off events and instances of recurring events. Default: true
    * `showDeleted` (boolean, optional): Whether to include deleted events (with status equals cancelled) in the result. Default: false
    * `showHiddenInvitations` (boolean, optional): Whether to include hidden invitations in the result. Default: false
    * `q` (string, optional): Free text search terms to find events that match these terms in any field.
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `timeZone` (string, optional): Time zone used in the response.
    * `updatedMin` (string, optional): Lower bound for an event's last modification time (RFC3339) to filter by.
    * `iCalUID` (string, optional): Specifies an event ID in the iCalendar format to be provided in the response.
  </Accordion>

  <Accordion title="google_calendar/update_event">
    **Description:** Update an existing event.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID
    * `eventId` (string, required): Event ID to update
    * `summary` (string, optional): Updated event title
    * `description` (string, optional): Updated event description
    * `start_dateTime` (string, optional): Updated start time
    * `end_dateTime` (string, optional): Updated end time
  </Accordion>

  <Accordion title="google_calendar/delete_event">
    **Description:** Delete a specified event.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID
    * `eventId` (string, required): Event ID to delete
  </Accordion>

  <Accordion title="google_calendar/view_calendar_list">
    **Description:** Retrieve user's calendar list.

    **Parameters:**

    * `maxResults` (integer, optional): Maximum number of entries returned on one result page. Minimum: 1
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `showDeleted` (boolean, optional): Whether to include deleted calendar list entries in the result. Default: false
    * `showHidden` (boolean, optional): Whether to show hidden entries. Default: false
    * `minAccessRole` (string, optional): The minimum access role for the user in the returned entries. Options: freeBusyReader, owner, reader, writer
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Calendar Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Google Calendar capabilities
calendar_agent = Agent(
    role="Schedule Manager",
    goal="Manage calendar events and scheduling efficiently",
    backstory="An AI assistant specialized in calendar management and scheduling coordination.",
    apps=['google_calendar']  # All Google Calendar actions will be available
)


# Task to create a meeting
create_meeting_task = Task(
    description="Create a team standup meeting for tomorrow at 9 AM with the development team",
    agent=calendar_agent,
    expected_output="Meeting created successfully with Google Meet link"
)


# Run the task
crew = Crew(
    agents=[calendar_agent],
    tasks=[create_meeting_task]
)

crew.kickoff()
```

### Filtering Specific Calendar Tools

```python  theme={null}
meeting_coordinator = Agent(
    role="Meeting Coordinator",
    goal="Coordinate meetings and check availability",
    backstory="An AI assistant that focuses on meeting scheduling and availability management.",
    apps=['google_calendar/create_event', 'google_calendar/get_availability']
)


# Task to schedule a meeting with availability check
schedule_meeting = Task(
    description="Check availability for next week and schedule a project review meeting with stakeholders",
    agent=meeting_coordinator,
    expected_output="Meeting scheduled after checking availability of all participants"
)

crew = Crew(
    agents=[meeting_coordinator],
    tasks=[schedule_meeting]
)

crew.kickoff()
```

### Event Management and Updates

```python  theme={null}
from crewai import Agent, Task, Crew

event_manager = Agent(
    role="Event Manager",
    goal="Manage and update calendar events efficiently",
    backstory="An experienced event manager who handles event logistics and updates.",
    apps=['google_calendar']
)


# Task to manage event updates
event_management = Task(
    description="""
    1. List all events for this week
    2. Update any events that need location changes to include video conference links
    3. Check availability for upcoming meetings
    """,
    agent=event_manager,
    expected_output="Weekly events updated with proper locations and availability checked"
)

crew = Crew(
    agents=[event_manager],
    tasks=[event_management]
)

crew.kickoff()
```

### Availability and Calendar Management

```python  theme={null}
from crewai import Agent, Task, Crew

availability_coordinator = Agent(
    role="Availability Coordinator",
    goal="Coordinate availability and manage calendars for scheduling",
    backstory="An AI assistant that specializes in availability management and calendar coordination.",
    apps=['google_calendar']
)


# Task to coordinate availability
availability_task = Task(
    description="""
    1. Get the list of available calendars
    2. Check availability for all calendars next Friday afternoon
    3. Create a team meeting for the first available 2-hour slot
    4. Include Google Meet link and send invitations
    """,
    agent=availability_coordinator,
    expected_output="Team meeting scheduled based on availability with all team members invited"
)

crew = Crew(
    agents=[availability_coordinator],
    tasks=[availability_task]
)

crew.kickoff()
```

### Automated Scheduling Workflows

```python  theme={null}
from crewai import Agent, Task, Crew

scheduling_automator = Agent(
    role="Scheduling Automator",
    goal="Automate scheduling workflows and calendar management",
    backstory="An AI assistant that automates complex scheduling scenarios and calendar workflows.",
    apps=['google_calendar']
)


# Complex scheduling automation task
automation_task = Task(
    description="""
    1. List all upcoming events for the next two weeks
    2. Identify any scheduling conflicts or back-to-back meetings
    3. Suggest optimal meeting times by checking availability
    4. Create buffer time between meetings where needed
    5. Update event descriptions with agenda items and meeting links
    """,
    agent=scheduling_automator,
    expected_output="Calendar optimized with resolved conflicts, buffer times, and updated meeting details"
)

crew = Crew(
    agents=[scheduling_automator],
    tasks=[automation_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Authentication Errors**

* Ensure your Google account has the necessary permissions for calendar access
* Verify that the OAuth connection includes all required scopes for Google Calendar API
* Check if calendar sharing settings allow the required access level

**Event Creation Issues**

* Verify that time formats are correct (RFC3339 format)
* Ensure attendee email addresses are properly formatted
* Check that the target calendar exists and is accessible
* Verify time zones are correctly specified

**Availability and Time Conflicts**

* Use proper RFC3339 format for time ranges when checking availability
* Ensure time zones are consistent across all operations
* Verify that calendar IDs are correct when checking multiple calendars

**Event Updates and Deletions**

* Verify that event IDs are correct and events exist
* Ensure you have edit permissions for the events
* Check that calendar ownership allows modifications

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Calendar integration setup or troubleshooting.
</Card>



# Google Contacts Integration
Source: https://docs.crewai.com/en/enterprise/integrations/google_contacts

Contact and directory management with Google Contacts integration for CrewAI.


## Overview

Enable your agents to manage contacts and directory information through Google Contacts. Access personal contacts, search directory people, create and update contact information, and manage contact groups with AI-powered automation.


## Prerequisites

Before using the Google Contacts integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Google account with Google Contacts access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Google Contacts Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Contacts** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for contacts and directory access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="google_contacts/get_contacts">
    **Description:** Retrieve user's contacts from Google Contacts.

    **Parameters:**

    * `pageSize` (integer, optional): Number of contacts to return (max 1000). Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): The token of the page to retrieve.
    * `personFields` (string, optional): Fields to include (e.g., 'names,emailAddresses,phoneNumbers'). Default: names,emailAddresses,phoneNumbers
    * `requestSyncToken` (boolean, optional): Whether the response should include a sync token. Default: false
    * `sortOrder` (string, optional): The order in which the connections should be sorted. Options: LAST\_MODIFIED\_ASCENDING, LAST\_MODIFIED\_DESCENDING, FIRST\_NAME\_ASCENDING, LAST\_NAME\_ASCENDING
  </Accordion>

  <Accordion title="google_contacts/search_contacts">
    **Description:** Search for contacts using a query string.

    **Parameters:**

    * `query` (string, required): Search query string
    * `readMask` (string, required): Fields to read (e.g., 'names,emailAddresses,phoneNumbers')
    * `pageSize` (integer, optional): Number of results to return. Minimum: 1, Maximum: 30
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `sources` (array, optional): The sources to search in. Options: READ\_SOURCE\_TYPE\_CONTACT, READ\_SOURCE\_TYPE\_PROFILE. Default: READ\_SOURCE\_TYPE\_CONTACT
  </Accordion>

  <Accordion title="google_contacts/list_directory_people">
    **Description:** List people in the authenticated user's directory.

    **Parameters:**

    * `sources` (array, required): Directory sources to search within. Options: DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_PROFILE, DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_CONTACT. Default: DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_PROFILE
    * `pageSize` (integer, optional): Number of people to return. Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `readMask` (string, optional): Fields to read (e.g., 'names,emailAddresses')
    * `requestSyncToken` (boolean, optional): Whether the response should include a sync token. Default: false
    * `mergeSources` (array, optional): Additional data to merge into the directory people responses. Options: CONTACT
  </Accordion>

  <Accordion title="google_contacts/search_directory_people">
    **Description:** Search for people in the directory.

    **Parameters:**

    * `query` (string, required): Search query
    * `sources` (string, required): Directory sources (use 'DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_PROFILE')
    * `pageSize` (integer, optional): Number of results to return
    * `readMask` (string, optional): Fields to read
  </Accordion>

  <Accordion title="google_contacts/list_other_contacts">
    **Description:** List other contacts (not in user's personal contacts).

    **Parameters:**

    * `pageSize` (integer, optional): Number of contacts to return. Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `readMask` (string, optional): Fields to read
    * `requestSyncToken` (boolean, optional): Whether the response should include a sync token. Default: false
  </Accordion>

  <Accordion title="google_contacts/search_other_contacts">
    **Description:** Search other contacts.

    **Parameters:**

    * `query` (string, required): Search query
    * `readMask` (string, required): Fields to read (e.g., 'names,emailAddresses')
    * `pageSize` (integer, optional): Number of results
  </Accordion>

  <Accordion title="google_contacts/get_person">
    **Description:** Get a single person's contact information by resource name.

    **Parameters:**

    * `resourceName` (string, required): The resource name of the person to get (e.g., 'people/c123456789')
    * `personFields` (string, optional): Fields to include (e.g., 'names,emailAddresses,phoneNumbers'). Default: names,emailAddresses,phoneNumbers
  </Accordion>

  <Accordion title="google_contacts/create_contact">
    **Description:** Create a new contact in the user's address book.

    **Parameters:**

    * `names` (array, optional): Person's names
      ```json  theme={null}
      [
        {
          "givenName": "John",
          "familyName": "Doe",
          "displayName": "John Doe"
        }
      ]
      ```
    * `emailAddresses` (array, optional): Email addresses
      ```json  theme={null}
      [
        {
          "value": "john.doe@example.com",
          "type": "work"
        }
      ]
      ```
    * `phoneNumbers` (array, optional): Phone numbers
      ```json  theme={null}
      [
        {
          "value": "+1234567890",
          "type": "mobile"
        }
      ]
      ```
    * `addresses` (array, optional): Postal addresses
      ```json  theme={null}
      [
        {
          "formattedValue": "123 Main St, City, State 12345",
          "type": "home"
        }
      ]
      ```
    * `organizations` (array, optional): Organizations/companies
      ```json  theme={null}
      [
        {
          "name": "Company Name",
          "title": "Job Title",
          "type": "work"
        }
      ]
      ```
  </Accordion>

  <Accordion title="google_contacts/update_contact">
    **Description:** Update an existing contact's information.

    **Parameters:**

    * `resourceName` (string, required): The resource name of the person to update (e.g., 'people/c123456789')
    * `updatePersonFields` (string, required): Fields to update (e.g., 'names,emailAddresses,phoneNumbers')
    * `names` (array, optional): Person's names
    * `emailAddresses` (array, optional): Email addresses
    * `phoneNumbers` (array, optional): Phone numbers
  </Accordion>

  <Accordion title="google_contacts/delete_contact">
    **Description:** Delete a contact from the user's address book.

    **Parameters:**

    * `resourceName` (string, required): The resource name of the person to delete (e.g., 'people/c123456789')
  </Accordion>

  <Accordion title="google_contacts/batch_get_people">
    **Description:** Get information about multiple people in a single request.

    **Parameters:**

    * `resourceNames` (array, required): Resource names of people to get. Maximum: 200 items
    * `personFields` (string, optional): Fields to include (e.g., 'names,emailAddresses,phoneNumbers'). Default: names,emailAddresses,phoneNumbers
  </Accordion>

  <Accordion title="google_contacts/list_contact_groups">
    **Description:** List the user's contact groups (labels).

    **Parameters:**

    * `pageSize` (integer, optional): Number of contact groups to return. Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `groupFields` (string, optional): Fields to include (e.g., 'name,memberCount,clientData'). Default: name,memberCount
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Google Contacts Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Google Contacts capabilities
contacts_agent = Agent(
    role="Contact Manager",
    goal="Manage contacts and directory information efficiently",
    backstory="An AI assistant specialized in contact management and directory operations.",
    apps=['google_contacts']  # All Google Contacts actions will be available
)


# Task to retrieve and organize contacts
contact_management_task = Task(
    description="Retrieve all contacts and organize them by company affiliation",
    agent=contacts_agent,
    expected_output="Contacts retrieved and organized by company with summary report"
)


# Run the task
crew = Crew(
    agents=[contacts_agent],
    tasks=[contact_management_task]
)

crew.kickoff()
```

### Directory Search and Management

```python  theme={null}
from crewai import Agent, Task, Crew

directory_manager = Agent(
    role="Directory Manager",
    goal="Search and manage directory people and contacts",
    backstory="An AI assistant that specializes in directory management and people search.",
    apps=[
        'google_contacts/search_directory_people',
        'google_contacts/list_directory_people',
        'google_contacts/search_contacts'
    ]
)


# Task to search and manage directory
directory_task = Task(
    description="Search for team members in the company directory and create a team contact list",
    agent=directory_manager,
    expected_output="Team directory compiled with contact information"
)

crew = Crew(
    agents=[directory_manager],
    tasks=[directory_task]
)

crew.kickoff()
```

### Contact Creation and Updates

```python  theme={null}
from crewai import Agent, Task, Crew

contact_curator = Agent(
    role="Contact Curator",
    goal="Create and update contact information systematically",
    backstory="An AI assistant that maintains accurate and up-to-date contact information.",
    apps=['google_contacts']
)


# Task to create and update contacts
curation_task = Task(
    description="""
    1. Search for existing contacts related to new business partners
    2. Create new contacts for partners not in the system
    3. Update existing contact information with latest details
    4. Organize contacts into appropriate groups
    """,
    agent=contact_curator,
    expected_output="Contact database updated with new partners and organized groups"
)

crew = Crew(
    agents=[contact_curator],
    tasks=[curation_task]
)

crew.kickoff()
```

### Contact Group Management

```python  theme={null}
from crewai import Agent, Task, Crew

group_organizer = Agent(
    role="Contact Group Organizer",
    goal="Organize contacts into meaningful groups and categories",
    backstory="An AI assistant that specializes in contact organization and group management.",
    apps=['google_contacts']
)


# Task to organize contact groups
organization_task = Task(
    description="""
    1. List all existing contact groups
    2. Analyze contact distribution across groups
    3. Create new groups for better organization
    4. Move contacts to appropriate groups based on their information
    """,
    agent=group_organizer,
    expected_output="Contacts organized into logical groups with improved structure"
)

crew = Crew(
    agents=[group_organizer],
    tasks=[organization_task]
)

crew.kickoff()
```

### Comprehensive Contact Management

```python  theme={null}
from crewai import Agent, Task, Crew

contact_specialist = Agent(
    role="Contact Management Specialist",
    goal="Provide comprehensive contact management across all sources",
    backstory="An AI assistant that handles all aspects of contact management including personal, directory, and other contacts.",
    apps=['google_contacts']
)


# Complex contact management task
comprehensive_task = Task(
    description="""
    1. Retrieve contacts from all sources (personal, directory, other)
    2. Search for duplicate contacts and merge information
    3. Update outdated contact information
    4. Create missing contacts for important stakeholders
    5. Organize contacts into meaningful groups
    6. Generate a comprehensive contact report
    """,
    agent=contact_specialist,
    expected_output="Complete contact management performed with unified contact database and detailed report"
)

crew = Crew(
    agents=[contact_specialist],
    tasks=[comprehensive_task]
)

crew.kickoff()
```


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



# Google Docs Integration
Source: https://docs.crewai.com/en/enterprise/integrations/google_docs

Document creation and editing with Google Docs integration for CrewAI.


## Overview

Enable your agents to create, edit, and manage Google Docs documents with text manipulation and formatting. Automate document creation, insert and replace text, manage content ranges, and streamline your document workflows with AI-powered automation.


## Prerequisites

Before using the Google Docs integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Google account with Google Docs access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Google Docs Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Docs** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for document access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="google_docs/create_document">
    **Description:** Create a new Google Document.

    **Parameters:**

    * `title` (string, optional): The title for the new document.
  </Accordion>

  <Accordion title="google_docs/get_document">
    **Description:** Get the contents and metadata of a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to retrieve.
    * `includeTabsContent` (boolean, optional): Whether to include tab content. Default is `false`.
    * `suggestionsViewMode` (string, optional): The suggestions view mode to apply to the document. Enum: `DEFAULT_FOR_CURRENT_ACCESS`, `PREVIEW_SUGGESTIONS_ACCEPTED`, `PREVIEW_WITHOUT_SUGGESTIONS`. Default is `DEFAULT_FOR_CURRENT_ACCESS`.
  </Accordion>

  <Accordion title="google_docs/batch_update">
    **Description:** Apply one or more updates to a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `requests` (array, required): A list of updates to apply to the document. Each item is an object representing a request.
    * `writeControl` (object, optional): Provides control over how write requests are executed. Contains `requiredRevisionId` (string) and `targetRevisionId` (string).
  </Accordion>

  <Accordion title="google_docs/insert_text">
    **Description:** Insert text into a Google Document at a specific location.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `text` (string, required): The text to insert.
    * `index` (integer, optional): The zero-based index where to insert the text. Default is `1`.
  </Accordion>

  <Accordion title="google_docs/replace_text">
    **Description:** Replace all instances of text in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `containsText` (string, required): The text to find and replace.
    * `replaceText` (string, required): The text to replace it with.
    * `matchCase` (boolean, optional): Whether the search should respect case. Default is `false`.
  </Accordion>

  <Accordion title="google_docs/delete_content_range">
    **Description:** Delete content from a specific range in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `startIndex` (integer, required): The start index of the range to delete.
    * `endIndex` (integer, required): The end index of the range to delete.
  </Accordion>

  <Accordion title="google_docs/insert_page_break">
    **Description:** Insert a page break at a specific location in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `index` (integer, optional): The zero-based index where to insert the page break. Default is `1`.
  </Accordion>

  <Accordion title="google_docs/create_named_range">
    **Description:** Create a named range in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `name` (string, required): The name for the named range.
    * `startIndex` (integer, required): The start index of the range.
    * `endIndex` (integer, required): The end index of the range.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Google Docs Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Google Docs capabilities
docs_agent = Agent(
    role="Document Creator",
    goal="Create and manage Google Docs documents efficiently",
    backstory="An AI assistant specialized in Google Docs document creation and editing.",
    apps=['google_docs']  # All Google Docs actions will be available
)


# Task to create a new document
create_doc_task = Task(
    description="Create a new Google Document titled 'Project Status Report'",
    agent=docs_agent,
    expected_output="New Google Document 'Project Status Report' created successfully"
)


# Run the task
crew = Crew(
    agents=[docs_agent],
    tasks=[create_doc_task]
)

crew.kickoff()
```

### Text Editing and Content Management

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent focused on text editing
text_editor = Agent(
    role="Document Editor",
    goal="Edit and update content in Google Docs documents",
    backstory="An AI assistant skilled in precise text editing and content management.",
    apps=['google_docs/insert_text', 'google_docs/replace_text', 'google_docs/delete_content_range']
)


# Task to edit document content
edit_content_task = Task(
    description="In document 'your_document_id', insert the text 'Executive Summary: ' at the beginning, then replace all instances of 'TODO' with 'COMPLETED'.",
    agent=text_editor,
    expected_output="Document updated with new text inserted and TODO items replaced."
)

crew = Crew(
    agents=[text_editor],
    tasks=[edit_content_task]
)

crew.kickoff()
```

### Advanced Document Operations

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent for advanced document operations
document_formatter = Agent(
    role="Document Formatter",
    goal="Apply advanced formatting and structure to Google Docs",
    backstory="An AI assistant that handles complex document formatting and organization.",
    apps=['google_docs/batch_update', 'google_docs/insert_page_break', 'google_docs/create_named_range']
)


# Task to format document
format_doc_task = Task(
    description="In document 'your_document_id', insert a page break at position 100, create a named range called 'Introduction' for characters 1-50, and apply batch formatting updates.",
    agent=document_formatter,
    expected_output="Document formatted with page break, named range, and styling applied."
)

crew = Crew(
    agents=[document_formatter],
    tasks=[format_doc_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Authentication Errors**

* Ensure your Google account has the necessary permissions for Google Docs access.
* Verify that the OAuth connection includes all required scopes (`https://www.googleapis.com/auth/documents`).

**Document ID Issues**

* Double-check document IDs for correctness.
* Ensure the document exists and is accessible to your account.
* Document IDs can be found in the Google Docs URL.

**Text Insertion and Range Operations**

* When using `insert_text` or `delete_content_range`, ensure index positions are valid.
* Remember that Google Docs uses zero-based indexing.
* The document must have content at the specified index positions.

**Batch Update Request Formatting**

* When using `batch_update`, ensure the `requests` array is correctly formatted according to the Google Docs API documentation.
* Complex updates require specific JSON structures for each request type.

**Replace Text Operations**

* For `replace_text`, ensure the `containsText` parameter exactly matches the text you want to replace.
* Use `matchCase` parameter to control case sensitivity.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Docs integration setup or troubleshooting.
</Card>



# Google Drive Integration
Source: https://docs.crewai.com/en/enterprise/integrations/google_drive

File storage and management with Google Drive integration for CrewAI.


## Overview

Enable your agents to manage files and folders through Google Drive. Upload, download, organize, and share files, create folders, and streamline your document management workflows with AI-powered automation.


## Prerequisites

Before using the Google Drive integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Google account with Google Drive access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Google Drive Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Drive** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file and folder management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="google_drive/get_file">
    **Description:** Get a file by ID from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to retrieve.
  </Accordion>

  <Accordion title="google_drive/list_files">
    **Description:** List files in Google Drive.

    **Parameters:**

    * `q` (string, optional): Query string to filter files (example: "name contains 'report'").
    * `page_size` (integer, optional): Maximum number of files to return (default: 100, max: 1000).
    * `page_token` (string, optional): Token for retrieving the next page of results.
    * `order_by` (string, optional): Sort order (example: "name", "createdTime desc", "modifiedTime").
    * `spaces` (string, optional): Comma-separated list of spaces to query (drive, appDataFolder, photos).
  </Accordion>

  <Accordion title="google_drive/upload_file">
    **Description:** Upload a file to Google Drive.

    **Parameters:**

    * `name` (string, required): Name of the file to create.
    * `content` (string, required): Content of the file to upload.
    * `mime_type` (string, optional): MIME type of the file (example: "text/plain", "application/pdf").
    * `parent_folder_id` (string, optional): ID of the parent folder where the file should be created.
    * `description` (string, optional): Description of the file.
  </Accordion>

  <Accordion title="google_drive/download_file">
    **Description:** Download a file from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to download.
    * `mime_type` (string, optional): MIME type for export (required for Google Workspace documents).
  </Accordion>

  <Accordion title="google_drive/create_folder">
    **Description:** Create a new folder in Google Drive.

    **Parameters:**

    * `name` (string, required): Name of the folder to create.
    * `parent_folder_id` (string, optional): ID of the parent folder where the new folder should be created.
    * `description` (string, optional): Description of the folder.
  </Accordion>

  <Accordion title="google_drive/delete_file">
    **Description:** Delete a file from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to delete.
  </Accordion>

  <Accordion title="google_drive/share_file">
    **Description:** Share a file in Google Drive with specific users or make it public.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to share.
    * `role` (string, required): The role granted by this permission (reader, writer, commenter, owner).
    * `type` (string, required): The type of the grantee (user, group, domain, anyone).
    * `email_address` (string, optional): The email address of the user or group to share with (required for user/group types).
    * `domain` (string, optional): The domain to share with (required for domain type).
    * `send_notification_email` (boolean, optional): Whether to send a notification email (default: true).
    * `email_message` (string, optional): A plain text custom message to include in the notification email.
  </Accordion>

  <Accordion title="google_drive/update_file">
    **Description:** Update an existing file in Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to update.
    * `name` (string, optional): New name for the file.
    * `content` (string, optional): New content for the file.
    * `mime_type` (string, optional): New MIME type for the file.
    * `description` (string, optional): New description for the file.
    * `add_parents` (string, optional): Comma-separated list of parent folder IDs to add.
    * `remove_parents` (string, optional): Comma-separated list of parent folder IDs to remove.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Google Drive Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Google Drive capabilities
drive_agent = Agent(
    role="File Manager",
    goal="Manage files and folders in Google Drive efficiently",
    backstory="An AI assistant specialized in document and file management.",
    apps=['google_drive']  # All Google Drive actions will be available
)


# Task to organize files
organize_files_task = Task(
    description="List all files in the root directory and organize them into appropriate folders",
    agent=drive_agent,
    expected_output="Summary of files organized with folder structure"
)


# Run the task
crew = Crew(
    agents=[drive_agent],
    tasks=[organize_files_task]
)

crew.kickoff()
```

### Filtering Specific Google Drive Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Google Drive actions only
file_manager_agent = Agent(
    role="Document Manager",
    goal="Upload and manage documents efficiently",
    backstory="An AI assistant that focuses on document upload and organization.",
    apps=[
        'google_drive/upload_file',
        'google_drive/create_folder',
        'google_drive/share_file'
    ]  # Specific Google Drive actions
)


# Task to upload and share documents
document_task = Task(
    description="Upload the quarterly report and share it with the finance team",
    agent=file_manager_agent,
    expected_output="Document uploaded and sharing permissions configured"
)

crew = Crew(
    agents=[file_manager_agent],
    tasks=[document_task]
)

crew.kickoff()
```

### Advanced File Management

```python  theme={null}
from crewai import Agent, Task, Crew

file_organizer = Agent(
    role="File Organizer",
    goal="Maintain organized file structure and manage permissions",
    backstory="An experienced file manager who ensures proper organization and access control.",
    apps=['google_drive']
)


# Complex task involving multiple Google Drive operations
organization_task = Task(
    description="""
    1. List all files in the shared folder
    2. Create folders for different document types (Reports, Presentations, Spreadsheets)
    3. Move files to appropriate folders based on their type
    4. Set appropriate sharing permissions for each folder
    5. Create a summary document of the organization changes
    """,
    agent=file_organizer,
    expected_output="Files organized into categorized folders with proper permissions and summary report"
)

crew = Crew(
    agents=[file_organizer],
    tasks=[organization_task]
)

crew.kickoff()
```



# Google Sheets Integration
Source: https://docs.crewai.com/en/enterprise/integrations/google_sheets

Spreadsheet data synchronization with Google Sheets integration for CrewAI.


## Overview

Enable your agents to manage spreadsheet data through Google Sheets. Read rows, create new entries, update existing data, and streamline your data management workflows with AI-powered automation. Perfect for data tracking, reporting, and collaborative data management.


## Prerequisites

Before using the Google Sheets integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Google account with Google Sheets access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)
* Spreadsheets with proper column headers for data operations


## Setting Up Google Sheets Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Sheets** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for spreadsheet access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="google_sheets/get_spreadsheet">
    **Description:** Retrieve properties and data of a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve.
    * `ranges` (array, optional): The ranges to retrieve from the spreadsheet.
    * `includeGridData` (boolean, optional): True if grid data should be returned. Default: false
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

  <Accordion title="google_sheets/get_values">
    **Description:** Returns a range of values from a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve data from.
    * `range` (string, required): The A1 notation or R1C1 notation of the range to retrieve values from.
    * `valueRenderOption` (string, optional): How values should be represented in the output. Options: FORMATTED\_VALUE, UNFORMATTED\_VALUE, FORMULA. Default: FORMATTED\_VALUE
    * `dateTimeRenderOption` (string, optional): How dates, times, and durations should be represented in the output. Options: SERIAL\_NUMBER, FORMATTED\_STRING. Default: SERIAL\_NUMBER
    * `majorDimension` (string, optional): The major dimension that results should use. Options: ROWS, COLUMNS. Default: ROWS
  </Accordion>

  <Accordion title="google_sheets/update_values">
    **Description:** Sets values in a range of a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of the range to update.
    * `values` (array, required): The data to be written. Each array represents a row.
      ```json  theme={null}
      [
        ["Value1", "Value2", "Value3"],
        ["Value4", "Value5", "Value6"]
      ]
      ```
    * `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
  </Accordion>

  <Accordion title="google_sheets/append_values">
    **Description:** Appends values to a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of a range to search for a logical table of data.
    * `values` (array, required): The data to append. Each array represents a row.
      ```json  theme={null}
      [
        ["Value1", "Value2", "Value3"],
        ["Value4", "Value5", "Value6"]
      ]
      ```
    * `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
    * `insertDataOption` (string, optional): How the input data should be inserted. Options: OVERWRITE, INSERT\_ROWS. Default: INSERT\_ROWS
  </Accordion>

  <Accordion title="google_sheets/create_spreadsheet">
    **Description:** Creates a new spreadsheet.

    **Parameters:**

    * `title` (string, required): The title of the new spreadsheet.
    * `sheets` (array, optional): The sheets that are part of the spreadsheet.
      ```json  theme={null}
      [
        {
          "properties": {
            "title": "Sheet1"
          }
        }
      ]
      ```
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Google Sheets Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Google Sheets capabilities
sheets_agent = Agent(
    role="Data Manager",
    goal="Manage spreadsheet data and track information efficiently",
    backstory="An AI assistant specialized in data management and spreadsheet operations.",
    apps=['google_sheets']
)


# Task to add new data to a spreadsheet
data_entry_task = Task(
    description="Add a new customer record to the customer database spreadsheet with name, email, and signup date",
    agent=sheets_agent,
    expected_output="New customer record added successfully to the spreadsheet"
)


# Run the task
crew = Crew(
    agents=[sheets_agent],
    tasks=[data_entry_task]
)

crew.kickoff()
```

### Filtering Specific Google Sheets Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Google Sheets actions only
data_collector = Agent(
    role="Data Collector",
    goal="Collect and organize data in spreadsheets",
    backstory="An AI assistant that focuses on data collection and organization.",
    apps=[
        'google_sheets/get_values',
        'google_sheets/update_values'
    ]
)


# Task to collect and organize data
data_collection = Task(
    description="Retrieve current inventory data and add new product entries to the inventory spreadsheet",
    agent=data_collector,
    expected_output="Inventory data retrieved and new products added successfully"
)

crew = Crew(
    agents=[data_collector],
    tasks=[data_collection]
)

crew.kickoff()
```

### Data Analysis and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze spreadsheet data and generate insights",
    backstory="An experienced data analyst who extracts insights from spreadsheet data.",
    apps=['google_sheets']
)


# Task to analyze data and create reports
analysis_task = Task(
    description="""
    1. Retrieve all sales data from the current month's spreadsheet
    2. Analyze the data for trends and patterns
    3. Create a summary report in a new row with key metrics
    """,
    agent=data_analyst,
    expected_output="Sales data analyzed and summary report created with key insights"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Spreadsheet Creation and Management

```python  theme={null}
from crewai import Agent, Task, Crew

spreadsheet_manager = Agent(
    role="Spreadsheet Manager",
    goal="Create and manage spreadsheets efficiently",
    backstory="An AI assistant that specializes in creating and organizing spreadsheets.",
    apps=['google_sheets']
)


# Task to create and set up new spreadsheets
setup_task = Task(
    description="""
    1. Create a new spreadsheet for quarterly reports
    2. Set up proper headers and structure
    3. Add initial data and formatting
    """,
    agent=spreadsheet_manager,
    expected_output="New quarterly report spreadsheet created and properly structured"
)

crew = Crew(
    agents=[spreadsheet_manager],
    tasks=[setup_task]
)

crew.kickoff()
```

### Automated Data Updates

```python  theme={null}
from crewai import Agent, Task, Crew

data_updater = Agent(
    role="Data Updater",
    goal="Automatically update and maintain spreadsheet data",
    backstory="An AI assistant that maintains data accuracy and updates records automatically.",
    apps=['google_sheets']
)


# Task to update data based on conditions
update_task = Task(
    description="""
    1. Get spreadsheet properties and structure
    2. Read current data from specific ranges
    3. Update values in target ranges with new data
    4. Append new records to the bottom of the sheet
    """,
    agent=data_updater,
    expected_output="Spreadsheet data updated successfully with new values and records"
)

crew = Crew(
    agents=[data_updater],
    tasks=[update_task]
)

crew.kickoff()
```

### Complex Data Management Workflow

```python  theme={null}
from crewai import Agent, Task, Crew

workflow_manager = Agent(
    role="Data Workflow Manager",
    goal="Manage complex data workflows across multiple spreadsheets",
    backstory="An AI assistant that orchestrates complex data operations across multiple spreadsheets.",
    apps=['google_sheets']
)


# Complex workflow task
workflow_task = Task(
    description="""
    1. Get all customer data from the main customer spreadsheet
    2. Create a new monthly summary spreadsheet
    3. Append summary data to the new spreadsheet
    4. Update customer status based on activity metrics
    5. Generate reports with proper formatting
    """,
    agent=workflow_manager,
    expected_output="Monthly customer workflow completed with new spreadsheet and updated data"
)

crew = Crew(
    agents=[workflow_manager],
    tasks=[workflow_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Permission Errors**

* Ensure your Google account has edit access to the target spreadsheets
* Verify that the OAuth connection includes required scopes for Google Sheets API
* Check that spreadsheets are shared with the authenticated account

**Spreadsheet Structure Issues**

* Ensure worksheets have proper column headers before creating or updating rows
* Verify that range notation (A1 format) is correct for the target cells
* Check that the specified spreadsheet ID exists and is accessible

**Data Type and Format Issues**

* Ensure data values match the expected format for each column
* Use proper date formats for date columns (ISO format recommended)
* Verify that numeric values are properly formatted for number columns

**Range and Cell Reference Issues**

* Use proper A1 notation for ranges (e.g., "A1:C10", "Sheet1!A1:B5")
* Ensure range references don't exceed the actual spreadsheet dimensions
* Verify that sheet names in range references match actual sheet names

**Value Input and Rendering Options**

* Choose appropriate `valueInputOption` (RAW vs USER\_ENTERED) for your data
* Select proper `valueRenderOption` based on how you want data formatted
* Consider `dateTimeRenderOption` for consistent date/time handling

**Spreadsheet Creation Issues**

* Ensure spreadsheet titles are unique and follow naming conventions
* Verify that sheet properties are properly structured when creating sheets
* Check that you have permissions to create new spreadsheets in your account

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Sheets integration setup or troubleshooting.
</Card>



# Google Slides Integration
Source: https://docs.crewai.com/en/enterprise/integrations/google_slides

Presentation creation and management with Google Slides integration for CrewAI.


## Overview

Enable your agents to create, edit, and manage Google Slides presentations. Create presentations, update content, import data from Google Sheets, manage pages and thumbnails, and streamline your presentation workflows with AI-powered automation.


## Prerequisites

Before using the Google Slides integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Google account with Google Slides access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Google Slides Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Slides** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for presentations, spreadsheets, and drive access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="google_slides/create_blank_presentation">
    **Description:** Creates a blank presentation with no content.

    **Parameters:**

    * `title` (string, required): The title of the presentation.
  </Accordion>

  <Accordion title="google_slides/get_presentation">
    **Description:** Retrieves a presentation by ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to retrieve.
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

  <Accordion title="google_slides/batch_update_presentation">
    **Description:** Applies updates, add content, or remove content from a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to update.
    * `requests` (array, required): A list of updates to apply to the presentation.
      ```json  theme={null}
      [
        {
          "insertText": {
            "objectId": "slide_id",
            "text": "Your text content here"
          }
        }
      ]
      ```
    * `writeControl` (object, optional): Provides control over how write requests are executed.
      ```json  theme={null}
      {
        "requiredRevisionId": "revision_id_string"
      }
      ```
  </Accordion>

  <Accordion title="google_slides/get_page">
    **Description:** Retrieves a specific page by its ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `pageObjectId` (string, required): The ID of the page to retrieve.
  </Accordion>

  <Accordion title="google_slides/get_thumbnail">
    **Description:** Generates a page thumbnail.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `pageObjectId` (string, required): The ID of the page for thumbnail generation.
  </Accordion>

  <Accordion title="google_slides/import_data_from_sheet">
    **Description:** Imports data from a Google Sheet into a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `sheetId` (string, required): The ID of the Google Sheet to import from.
    * `dataRange` (string, required): The range of data to import from the sheet.
  </Accordion>

  <Accordion title="google_slides/upload_file_to_drive">
    **Description:** Uploads a file to Google Drive associated with the presentation.

    **Parameters:**

    * `file` (string, required): The file data to upload.
    * `presentationId` (string, required): The ID of the presentation to link the uploaded file.
  </Accordion>

  <Accordion title="google_slides/link_file_to_presentation">
    **Description:** Links a file in Google Drive to a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `fileId` (string, required): The ID of the file to link.
  </Accordion>

  <Accordion title="google_slides/get_all_presentations">
    **Description:** Lists all presentations accessible to the user.

    **Parameters:**

    * `pageSize` (integer, optional): The number of presentations to return per page.
    * `pageToken` (string, optional): A token for pagination.
  </Accordion>

  <Accordion title="google_slides/delete_presentation">
    **Description:** Deletes a presentation by ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to delete.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Google Slides Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Google Slides capabilities
slides_agent = Agent(
    role="Presentation Manager",
    goal="Create and manage presentations efficiently",
    backstory="An AI assistant specialized in presentation creation and content management.",
    apps=['google_slides']  # All Google Slides actions will be available
)


# Task to create a presentation
create_presentation_task = Task(
    description="Create a new presentation for the quarterly business review with key slides",
    agent=slides_agent,
    expected_output="Quarterly business review presentation created with structured content"
)


# Run the task
crew = Crew(
    agents=[slides_agent],
    tasks=[create_presentation_task]
)

crew.kickoff()
```

### Presentation Content Management

```python  theme={null}
from crewai import Agent, Task, Crew

content_manager = Agent(
    role="Content Manager",
    goal="Manage presentation content and updates",
    backstory="An AI assistant that focuses on content creation and presentation updates.",
    apps=[
        'google_slides/create_blank_presentation',
        'google_slides/batch_update_presentation',
        'google_slides/get_presentation'
    ]
)


# Task to create and update presentations
content_task = Task(
    description="Create a new presentation and add content slides with charts and text",
    agent=content_manager,
    expected_output="Presentation created with updated content and visual elements"
)

crew = Crew(
    agents=[content_manager],
    tasks=[content_task]
)

crew.kickoff()
```

### Data Integration and Visualization

```python  theme={null}
from crewai import Agent, Task, Crew

data_visualizer = Agent(
    role="Data Visualizer",
    goal="Create presentations with data imported from spreadsheets",
    backstory="An AI assistant that specializes in data visualization and presentation integration.",
    apps=['google_slides']
)


# Task to create data-driven presentations
visualization_task = Task(
    description="""
    1. Create a new presentation for monthly sales report
    2. Import data from the sales spreadsheet
    3. Create charts and visualizations from the imported data
    4. Generate thumbnails for slide previews
    """,
    agent=data_visualizer,
    expected_output="Data-driven presentation created with imported spreadsheet data and visualizations"
)

crew = Crew(
    agents=[data_visualizer],
    tasks=[visualization_task]
)

crew.kickoff()
```

### Presentation Library Management

```python  theme={null}
from crewai import Agent, Task, Crew

library_manager = Agent(
    role="Presentation Library Manager",
    goal="Manage and organize presentation libraries",
    backstory="An AI assistant that manages presentation collections and file organization.",
    apps=['google_slides']
)


# Task to manage presentation library
library_task = Task(
    description="""
    1. List all existing presentations
    2. Generate thumbnails for presentation previews
    3. Upload supporting files to Drive and link to presentations
    4. Organize presentations by topic and date
    """,
    agent=library_manager,
    expected_output="Presentation library organized with thumbnails and linked supporting files"
)

crew = Crew(
    agents=[library_manager],
    tasks=[library_task]
)

crew.kickoff()
```

### Automated Presentation Workflows

```python  theme={null}
from crewai import Agent, Task, Crew

presentation_automator = Agent(
    role="Presentation Automator",
    goal="Automate presentation creation and management workflows",
    backstory="An AI assistant that automates complex presentation workflows and content generation.",
    apps=['google_slides']
)


# Complex presentation automation task
automation_task = Task(
    description="""
    1. Create multiple presentations for different departments
    2. Import relevant data from various spreadsheets
    3. Update existing presentations with new content
    4. Generate thumbnails for all presentations
    5. Link supporting documents from Drive
    6. Create a master index presentation with links to all others
    """,
    agent=presentation_automator,
    expected_output="Automated presentation workflow completed with multiple presentations and organized structure"
)

crew = Crew(
    agents=[presentation_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

### Template and Content Creation

```python  theme={null}
from crewai import Agent, Task, Crew

template_creator = Agent(
    role="Template Creator",
    goal="Create presentation templates and standardized content",
    backstory="An AI assistant that creates consistent presentation templates and content standards.",
    apps=['google_slides']
)


# Task to create templates
template_task = Task(
    description="""
    1. Create blank presentation templates for different use cases
    2. Add standard layouts and content placeholders
    3. Create sample presentations with best practices
    4. Generate thumbnails for template previews
    5. Upload template assets to Drive and link appropriately
    """,
    agent=template_creator,
    expected_output="Presentation templates created with standardized layouts and linked assets"
)

crew = Crew(
    agents=[template_creator],
    tasks=[template_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Permission Errors**

* Ensure your Google account has appropriate permissions for Google Slides
* Verify that the OAuth connection includes required scopes for presentations, spreadsheets, and drive access
* Check that presentations are shared with the authenticated account

**Presentation ID Issues**

* Verify that presentation IDs are correct and presentations exist
* Ensure you have access permissions to the presentations you're trying to modify
* Check that presentation IDs are properly formatted

**Content Update Issues**

* Ensure batch update requests are properly formatted according to Google Slides API specifications
* Verify that object IDs for slides and elements exist in the presentation
* Check that write control revision IDs are current if using optimistic concurrency

**Data Import Issues**

* Verify that Google Sheet IDs are correct and accessible
* Ensure data ranges are properly specified using A1 notation
* Check that you have read permissions for the source spreadsheets

**File Upload and Linking Issues**

* Ensure file data is properly encoded for upload
* Verify that Drive file IDs are correct when linking files
* Check that you have appropriate Drive permissions for file operations

**Page and Thumbnail Operations**

* Verify that page object IDs exist in the specified presentation
* Ensure presentations have content before attempting to generate thumbnails
* Check that page structure is valid for thumbnail generation

**Pagination and Listing Issues**

* Use appropriate page sizes for listing presentations
* Implement proper pagination using page tokens for large result sets
* Handle empty result sets gracefully

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Slides integration setup or troubleshooting.
</Card>



# HubSpot Integration
Source: https://docs.crewai.com/en/enterprise/integrations/hubspot

Manage companies and contacts in HubSpot with CrewAI.


## Overview

Enable your agents to manage companies and contacts within HubSpot. Create new records and streamline your CRM processes with AI-powered automation.


## Prerequisites

Before using the HubSpot integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription.
* A HubSpot account with appropriate permissions.
* Connected your HubSpot account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors).


## Setting Up HubSpot Integration

### 1. Connect Your HubSpot Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors).
2. Find **HubSpot** in the Authentication Integrations section.
3. Click **Connect** and complete the OAuth flow.
4. Grant the necessary permissions for company and contact management.
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="hubspot/create_company">
    **Description:** Create a new company record in HubSpot.

    **Parameters:**

    * `name` (string, required): Name of the company.
    * `domain` (string, optional): Company Domain Name.
    * `industry` (string, optional): Industry. Must be one of the predefined values from HubSpot.
    * `phone` (string, optional): Phone Number.
    * `hubspot_owner_id` (string, optional): Company owner ID.
    * `type` (string, optional): Type of the company. Available values: `PROSPECT`, `PARTNER`, `RESELLER`, `VENDOR`, `OTHER`.
    * `city` (string, optional): City.
    * `state` (string, optional): State/Region.
    * `zip` (string, optional): Postal Code.
    * `numberofemployees` (number, optional): Number of Employees.
    * `annualrevenue` (number, optional): Annual Revenue.
    * `timezone` (string, optional): Time Zone.
    * `description` (string, optional): Description.
    * `linkedin_company_page` (string, optional): LinkedIn Company Page URL.
    * `company_email` (string, optional): Company Email.
    * `first_name` (string, optional): First Name of a contact at the company.
    * `last_name` (string, optional): Last Name of a contact at the company.
    * `about_us` (string, optional): About Us.
    * `hs_csm_sentiment` (string, optional): CSM Sentiment. Available values: `at_risk`, `neutral`, `healthy`.
    * `closedate` (string, optional): Close Date.
    * `hs_keywords` (string, optional): Company Keywords. Must be one of the predefined values.
    * `country` (string, optional): Country/Region.
    * `hs_country_code` (string, optional): Country/Region Code.
    * `hs_employee_range` (string, optional): Employee range.
    * `facebook_company_page` (string, optional): Facebook Company Page URL.
    * `facebookfans` (number, optional): Number of Facebook Fans.
    * `hs_gps_coordinates` (string, optional): GPS Coordinates.
    * `hs_gps_error` (string, optional): GPS Error.
    * `googleplus_page` (string, optional): Google Plus Page URL.
    * `owneremail` (string, optional): HubSpot Owner Email.
    * `ownername` (string, optional): HubSpot Owner Name.
    * `hs_ideal_customer_profile` (string, optional): Ideal Customer Profile Tier. Available values: `tier_1`, `tier_2`, `tier_3`.
    * `hs_industry_group` (string, optional): Industry group.
    * `is_public` (boolean, optional): Is Public.
    * `hs_last_metered_enrichment_timestamp` (string, optional): Last Metered Enrichment Timestamp.
    * `hs_lead_status` (string, optional): Lead Status. Available values: `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING`.
    * `lifecyclestage` (string, optional): Lifecycle Stage. Available values: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `evangelist`, `other`.
    * `linkedinbio` (string, optional): LinkedIn Bio.
    * `hs_linkedin_handle` (string, optional): LinkedIn handle.
    * `hs_live_enrichment_deadline` (string, optional): Live enrichment deadline.
    * `hs_logo_url` (string, optional): Logo URL.
    * `hs_analytics_source` (string, optional): Original Traffic Source.
    * `hs_pinned_engagement_id` (number, optional): Pinned Engagement ID.
    * `hs_quick_context` (string, optional): Quick context.
    * `hs_revenue_range` (string, optional): Revenue range.
    * `hs_state_code` (string, optional): State/Region Code.
    * `address` (string, optional): Street Address.
    * `address2` (string, optional): Street Address 2.
    * `hs_is_target_account` (boolean, optional): Target Account.
    * `hs_target_account` (string, optional): Target Account Tier. Available values: `tier_1`, `tier_2`, `tier_3`.
    * `hs_target_account_recommendation_snooze_time` (string, optional): Target Account Recommendation Snooze Time.
    * `hs_target_account_recommendation_state` (string, optional): Target Account Recommendation State. Available values: `DISMISSED`, `NONE`, `SNOOZED`.
    * `total_money_raised` (string, optional): Total Money Raised.
    * `twitterbio` (string, optional): Twitter Bio.
    * `twitterfollowers` (number, optional): Twitter Followers.
    * `twitterhandle` (string, optional): Twitter Handle.
    * `web_technologies` (string, optional): Web Technologies used. Must be one of the predefined values.
    * `website` (string, optional): Website URL.
    * `founded_year` (string, optional): Year Founded.
  </Accordion>

  <Accordion title="hubspot/create_contact">
    **Description:** Create a new contact record in HubSpot.

    **Parameters:**

    * `email` (string, required): Email address of the contact.
    * `firstname` (string, optional): First Name.
    * `lastname` (string, optional): Last Name.
    * `phone` (string, optional): Phone Number.
    * `hubspot_owner_id` (string, optional): Contact owner.
    * `lifecyclestage` (string, optional): Lifecycle Stage. Available values: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `evangelist`, `other`.
    * `hs_lead_status` (string, optional): Lead Status. Available values: `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING`.
    * `annualrevenue` (string, optional): Annual Revenue.
    * `hs_buying_role` (string, optional): Buying Role.
    * `cc_emails` (string, optional): CC Emails.
    * `ch_customer_id` (string, optional): Chargify Customer ID.
    * `ch_customer_reference` (string, optional): Chargify Customer Reference.
    * `chargify_sites` (string, optional): Chargify Site(s).
    * `city` (string, optional): City.
    * `hs_facebook_ad_clicked` (boolean, optional): Clicked Facebook ad.
    * `hs_linkedin_ad_clicked` (string, optional): Clicked LinkedIn Ad.
    * `hs_clicked_linkedin_ad` (string, optional): Clicked on a LinkedIn Ad.
    * `closedate` (string, optional): Close Date.
    * `company` (string, optional): Company Name.
    * `company_size` (string, optional): Company size.
    * `country` (string, optional): Country/Region.
    * `hs_country_region_code` (string, optional): Country/Region Code.
    * `date_of_birth` (string, optional): Date of birth.
    * `degree` (string, optional): Degree.
    * `hs_email_customer_quarantined_reason` (string, optional): Email address quarantine reason.
    * `hs_role` (string, optional): Employment Role. Must be one of the predefined values.
    * `hs_seniority` (string, optional): Employment Seniority. Must be one of the predefined values.
    * `hs_sub_role` (string, optional): Employment Sub Role. Must be one of the predefined values.
    * `hs_employment_change_detected_date` (string, optional): Employment change detected date.
    * `hs_enriched_email_bounce_detected` (boolean, optional): Enriched Email Bounce Detected.
    * `hs_facebookid` (string, optional): Facebook ID.
    * `hs_facebook_click_id` (string, optional): Facebook click id.
    * `fax` (string, optional): Fax Number.
    * `field_of_study` (string, optional): Field of study.
    * `followercount` (number, optional): Follower Count.
    * `gender` (string, optional): Gender.
    * `hs_google_click_id` (string, optional): Google ad click id.
    * `graduation_date` (string, optional): Graduation date.
    * `owneremail` (string, optional): HubSpot Owner Email (legacy).
    * `ownername` (string, optional): HubSpot Owner Name (legacy).
    * `industry` (string, optional): Industry.
    * `hs_inferred_language_codes` (string, optional): Inferred Language Codes. Must be one of the predefined values.
    * `jobtitle` (string, optional): Job Title.
    * `hs_job_change_detected_date` (string, optional): Job change detected date.
    * `job_function` (string, optional): Job function.
    * `hs_journey_stage` (string, optional): Journey Stage. Must be one of the predefined values.
    * `kloutscoregeneral` (number, optional): Klout Score.
    * `hs_last_metered_enrichment_timestamp` (string, optional): Last Metered Enrichment Timestamp.
    * `hs_latest_source` (string, optional): Latest Traffic Source.
    * `hs_latest_source_timestamp` (string, optional): Latest Traffic Source Date.
    * `hs_legal_basis` (string, optional): Legal basis for processing contact's data.
    * `linkedinbio` (string, optional): LinkedIn Bio.
    * `linkedinconnections` (number, optional): LinkedIn Connections.
    * `hs_linkedin_url` (string, optional): LinkedIn URL.
    * `hs_linkedinid` (string, optional): Linkedin ID.
    * `hs_live_enrichment_deadline` (string, optional): Live enrichment deadline.
    * `marital_status` (string, optional): Marital Status.
    * `hs_content_membership_email` (string, optional): Member email.
    * `hs_content_membership_notes` (string, optional): Membership Notes.
    * `message` (string, optional): Message.
    * `military_status` (string, optional): Military status.
    * `mobilephone` (string, optional): Mobile Phone Number.
    * `numemployees` (string, optional): Number of Employees.
    * `hs_analytics_source` (string, optional): Original Traffic Source.
    * `photo` (string, optional): Photo.
    * `hs_pinned_engagement_id` (number, optional): Pinned engagement ID.
    * `zip` (string, optional): Postal Code.
    * `hs_language` (string, optional): Preferred language. Must be one of the predefined values.
    * `associatedcompanyid` (number, optional): Primary Associated Company ID.
    * `hs_email_optout_survey_reason` (string, optional): Reason for opting out of email.
    * `relationship_status` (string, optional): Relationship Status.
    * `hs_returning_to_office_detected_date` (string, optional): Returning to office detected date.
    * `salutation` (string, optional): Salutation.
    * `school` (string, optional): School.
    * `seniority` (string, optional): Seniority.
    * `hs_feedback_show_nps_web_survey` (boolean, optional): Should be shown an NPS web survey.
    * `start_date` (string, optional): Start date.
    * `state` (string, optional): State/Region.
    * `hs_state_code` (string, optional): State/Region Code.
    * `hs_content_membership_status` (string, optional): Status.
    * `address` (string, optional): Street Address.
    * `tax_exempt` (string, optional): Tax Exempt.
    * `hs_timezone` (string, optional): Time Zone. Must be one of the predefined values.
    * `twitterbio` (string, optional): Twitter Bio.
    * `hs_twitterid` (string, optional): Twitter ID.
    * `twitterprofilephoto` (string, optional): Twitter Profile Photo.
    * `twitterhandle` (string, optional): Twitter Username.
    * `vat_number` (string, optional): VAT Number.
    * `ch_verified` (string, optional): Verified for ACH/eCheck Payments.
    * `website` (string, optional): Website URL.
    * `hs_whatsapp_phone_number` (string, optional): WhatsApp Phone Number.
    * `work_email` (string, optional): Work email.
    * `hs_googleplusid` (string, optional): googleplus ID.
  </Accordion>

  <Accordion title="hubspot/create_deal">
    **Description:** Create a new deal record in HubSpot.

    **Parameters:**

    * `dealname` (string, required): Name of the deal.
    * `amount` (number, optional): The value of the deal.
    * `dealstage` (string, optional): The pipeline stage of the deal.
    * `pipeline` (string, optional): The pipeline the deal belongs to.
    * `closedate` (string, optional): The date the deal is expected to close.
    * `hubspot_owner_id` (string, optional): The owner of the deal.
    * `dealtype` (string, optional): The type of deal. Available values: `newbusiness`, `existingbusiness`.
    * `description` (string, optional): A description of the deal.
    * `hs_priority` (string, optional): The priority of the deal. Available values: `low`, `medium`, `high`.
  </Accordion>

  <Accordion title="hubspot/create_record_engagements">
    **Description:** Create a new engagement (e.g., note, email, call, meeting, task) in HubSpot.

    **Parameters:**

    * `engagementType` (string, required): The type of engagement. Available values: `NOTE`, `EMAIL`, `CALL`, `MEETING`, `TASK`.
    * `hubspot_owner_id` (string, optional): The user the activity is assigned to.
    * `hs_timestamp` (string, optional): The date and time of the activity.
    * `hs_note_body` (string, optional): The body of the note. (Used for `NOTE`)
    * `hs_task_subject` (string, optional): The title of the task. (Used for `TASK`)
    * `hs_task_body` (string, optional): The notes for the task. (Used for `TASK`)
    * `hs_task_status` (string, optional): The status of the task. (Used for `TASK`)
    * `hs_meeting_title` (string, optional): The title of the meeting. (Used for `MEETING`)
    * `hs_meeting_body` (string, optional): The description for the meeting. (Used for `MEETING`)
    * `hs_meeting_start_time` (string, optional): The start time of the meeting. (Used for `MEETING`)
    * `hs_meeting_end_time` (string, optional): The end time of the meeting. (Used for `MEETING`)
  </Accordion>

  <Accordion title="hubspot/update_company">
    **Description:** Update an existing company record in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the company to update.
    * `name` (string, optional): Name of the company.
    * `domain` (string, optional): Company Domain Name.
    * `industry` (string, optional): Industry.
    * `phone` (string, optional): Phone Number.
    * `city` (string, optional): City.
    * `state` (string, optional): State/Region.
    * `zip` (string, optional): Postal Code.
    * `numberofemployees` (number, optional): Number of Employees.
    * `annualrevenue` (number, optional): Annual Revenue.
    * `description` (string, optional): Description.
  </Accordion>

  <Accordion title="hubspot/create_record_any">
    **Description:** Create a record for a specified object type in HubSpot.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * Additional parameters depend on the custom object's schema.
  </Accordion>

  <Accordion title="hubspot/update_contact">
    **Description:** Update an existing contact record in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the contact to update.
    * `firstname` (string, optional): First Name.
    * `lastname` (string, optional): Last Name.
    * `email` (string, optional): Email address.
    * `phone` (string, optional): Phone Number.
    * `company` (string, optional): Company Name.
    * `jobtitle` (string, optional): Job Title.
    * `lifecyclestage` (string, optional): Lifecycle Stage.
  </Accordion>

  <Accordion title="hubspot/update_deal">
    **Description:** Update an existing deal record in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the deal to update.
    * `dealname` (string, optional): Name of the deal.
    * `amount` (number, optional): The value of the deal.
    * `dealstage` (string, optional): The pipeline stage of the deal.
    * `pipeline` (string, optional): The pipeline the deal belongs to.
    * `closedate` (string, optional): The date the deal is expected to close.
    * `dealtype` (string, optional): The type of deal.
  </Accordion>

  <Accordion title="hubspot/update_record_engagements">
    **Description:** Update an existing engagement in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the engagement to update.
    * `hs_note_body` (string, optional): The body of the note.
    * `hs_task_subject` (string, optional): The title of the task.
    * `hs_task_body` (string, optional): The notes for the task.
    * `hs_task_status` (string, optional): The status of the task.
  </Accordion>

  <Accordion title="hubspot/update_record_any">
    **Description:** Update a record for a specified object type in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update.
    * `recordType` (string, required): The object type ID of the custom object.
    * Additional parameters depend on the custom object's schema.
  </Accordion>

  <Accordion title="hubspot/list_companies">
    **Description:** Get a list of company records from HubSpot.

    **Parameters:**

    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/list_contacts">
    **Description:** Get a list of contact records from HubSpot.

    **Parameters:**

    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/list_deals">
    **Description:** Get a list of deal records from HubSpot.

    **Parameters:**

    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/get_records_engagements">
    **Description:** Get a list of engagement records from HubSpot.

    **Parameters:**

    * `objectName` (string, required): The type of engagement to fetch (e.g., "notes").
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/get_records_any">
    **Description:** Get a list of records for any specified object type in HubSpot.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/get_company">
    **Description:** Get a single company record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the company to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_contact">
    **Description:** Get a single contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the contact to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_deal">
    **Description:** Get a single deal record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the deal to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_record_by_id_engagements">
    **Description:** Get a single engagement record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the engagement to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_record_by_id_any">
    **Description:** Get a single record of any specified object type by its ID.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * `recordId` (string, required): The ID of the record to retrieve.
  </Accordion>

  <Accordion title="hubspot/search_companies">
    **Description:** Search for company records in HubSpot using a filter formula.

    **Parameters:**

    * `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_contacts">
    **Description:** Search for contact records in HubSpot using a filter formula.

    **Parameters:**

    * `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_deals">
    **Description:** Search for deal records in HubSpot using a filter formula.

    **Parameters:**

    * `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_records_engagements">
    **Description:** Search for engagement records in HubSpot using a filter formula.

    **Parameters:**

    * `engagementFilterFormula` (object, optional): A filter for engagements.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_records_any">
    **Description:** Search for records of any specified object type in HubSpot.

    **Parameters:**

    * `recordType` (string, required): The object type ID to search.
    * `filterFormula` (string, optional): The filter formula to apply.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/delete_record_companies">
    **Description:** Delete a company record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the company to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_contacts">
    **Description:** Delete a contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the contact to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_deals">
    **Description:** Delete a deal record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the deal to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_engagements">
    **Description:** Delete an engagement record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the engagement to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_any">
    **Description:** Delete a record of any specified object type by its ID.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * `recordId` (string, required): The ID of the record to delete.
  </Accordion>

  <Accordion title="hubspot/get_contacts_by_list_id">
    **Description:** Get contacts from a specific list by its ID.

    **Parameters:**

    * `listId` (string, required): The ID of the list to get contacts from.
    * `paginationParameters` (object, optional): Use `pageCursor` for subsequent pages.
  </Accordion>

  <Accordion title="hubspot/describe_action_schema">
    **Description:** Get the expected schema for a given object type and operation.

    **Parameters:**

    * `recordType` (string, required): The object type ID (e.g., 'companies').
    * `operation` (string, required): The operation type (e.g., 'CREATE\_RECORD').
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic HubSpot Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with HubSpot capabilities
hubspot_agent = Agent(
    role="CRM Manager",
    goal="Manage company and contact records in HubSpot",
    backstory="An AI assistant specialized in CRM management.",
    apps=['hubspot']  # All HubSpot actions will be available
)


# Task to create a new company
create_company_task = Task(
    description="Create a new company in HubSpot with name 'Innovate Corp' and domain 'innovatecorp.com'.",
    agent=hubspot_agent,
    expected_output="Company created successfully with confirmation"
)


# Run the task
crew = Crew(
    agents=[hubspot_agent],
    tasks=[create_company_task]
)

crew.kickoff()
```

### Filtering Specific HubSpot Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific HubSpot actions only
contact_creator = Agent(
    role="Contact Creator",
    goal="Create new contacts in HubSpot",
    backstory="An AI assistant that focuses on creating new contact entries in the CRM.",
    apps=['hubspot/create_contact']  # Only contact creation action
)


# Task to create a contact
create_contact = Task(
    description="Create a new contact for 'John Doe' with email 'john.doe@example.com'.",
    agent=contact_creator,
    expected_output="Contact created successfully in HubSpot."
)

crew = Crew(
    agents=[contact_creator],
    tasks=[create_contact]
)

crew.kickoff()
```

### Contact Management

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with HubSpot contact management capabilities
crm_manager = Agent(
    role="CRM Manager",
    goal="Manage and organize HubSpot contacts efficiently.",
    backstory="An experienced CRM manager who maintains an organized contact database.",
    apps=['hubspot']  # All HubSpot actions including contact management
)


# Task to manage contacts
contact_task = Task(
    description="Create a new contact for 'Jane Smith' at 'Global Tech Inc.' with email 'jane.smith@globaltech.com'.",
    agent=crm_manager,
    expected_output="Contact database updated with the new contact."
)

crew = Crew(
    agents=[crm_manager],
    tasks=[contact_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with HubSpot integration setup or troubleshooting.
</Card>



# Jira Integration
Source: https://docs.crewai.com/en/enterprise/integrations/jira

Issue tracking and project management with Jira integration for CrewAI.


## Overview

Enable your agents to manage issues, projects, and workflows through Jira. Create and update issues, track project progress, manage assignments, and streamline your project management with AI-powered automation.


## Prerequisites

Before using the Jira integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Jira account with appropriate project permissions
* Connected your Jira account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Jira Integration

### 1. Connect Your Jira Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Jira** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for issue and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


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


## Usage Examples

### Basic Jira Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Jira capabilities
jira_agent = Agent(
    role="Issue Manager",
    goal="Manage Jira issues and track project progress efficiently",
    backstory="An AI assistant specialized in issue tracking and project management.",
    apps=['jira']  # All Jira actions will be available
)


# Task to create a bug report
create_bug_task = Task(
    description="Create a bug report for the login functionality with high priority and assign it to the development team",
    agent=jira_agent,
    expected_output="Bug report created successfully with issue key"
)


# Run the task
crew = Crew(
    agents=[jira_agent],
    tasks=[create_bug_task]
)

crew.kickoff()
```

### Filtering Specific Jira Tools

```python  theme={null}

issue_coordinator = Agent(
    role="Issue Coordinator",
    goal="Create and manage Jira issues efficiently",
    backstory="An AI assistant that focuses on issue creation and management.",
    apps=['jira']
)


# Task to manage issue workflow
issue_workflow = Task(
    description="Create a feature request issue and update the status of related issues",
    agent=issue_coordinator,
    expected_output="Feature request created and related issues updated"
)

crew = Crew(
    agents=[issue_coordinator],
    tasks=[issue_workflow]
)

crew.kickoff()
```

### Project Analysis and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

project_analyst = Agent(
    role="Project Analyst",
    goal="Analyze project data and generate insights from Jira",
    backstory="An experienced project analyst who extracts insights from project management data.",
    apps=['jira']
)


# Task to analyze project status
analysis_task = Task(
    description="""
    1. Get all projects and their issue types
    2. Search for all open issues across projects
    3. Analyze issue distribution by status and assignee
    4. Create a summary report issue with findings
    """,
    agent=project_analyst,
    expected_output="Project analysis completed with summary report created"
)

crew = Crew(
    agents=[project_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Automated Issue Management

```python  theme={null}
from crewai import Agent, Task, Crew

automation_manager = Agent(
    role="Automation Manager",
    goal="Automate issue management and workflow processes",
    backstory="An AI assistant that automates repetitive issue management tasks.",
    apps=['jira']
)


# Task to automate issue management
automation_task = Task(
    description="""
    1. Search for all unassigned issues using JQL
    2. Get available assignees for each project
    3. Automatically assign issues based on workload and expertise
    4. Update issue priorities based on age and type
    5. Create weekly sprint planning issues
    """,
    agent=automation_manager,
    expected_output="Issues automatically assigned and sprint planning issues created"
)

crew = Crew(
    agents=[automation_manager],
    tasks=[automation_task]
)

crew.kickoff()
```

### Advanced Schema-Based Operations

```python  theme={null}
from crewai import Agent, Task, Crew

schema_specialist = Agent(
    role="Schema Specialist",
    goal="Handle complex Jira operations using dynamic schemas",
    backstory="An AI assistant that can work with dynamic Jira schemas and custom issue types.",
    apps=['jira']
)


---

**Navigation:** [← Previous](./07-traces.md) | [Index](./index.md) | [Next →](./09-task-using-schema-based-operations.md)
