# Task using schema-based operations

**Navigation:** [← Previous](./08-create-an-agent-with-asana-capabilities.md) | [Index](./index.md) | [Next →](./10-create-an-agent-with-stripe-capabilities.md)

---

# Task using schema-based operations
schema_task = Task(
    description="""
    1. Get all projects and their custom issue types
    2. For each custom issue type, describe the action schema
    3. Create issues using the dynamic schema for complex custom fields
    4. Update issues with custom field values based on business rules
    """,
    agent=schema_specialist,
    expected_output="Custom issues created and updated using dynamic schemas"
)

crew = Crew(
    agents=[schema_specialist],
    tasks=[schema_task]
)

crew.kickoff()
```


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



# Linear Integration
Source: https://docs.crewai.com/en/enterprise/integrations/linear

Software project and bug tracking with Linear integration for CrewAI.


## Overview

Enable your agents to manage issues, projects, and development workflows through Linear. Create and update issues, manage project timelines, organize teams, and streamline your software development process with AI-powered automation.


## Prerequisites

Before using the Linear integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Linear account with appropriate workspace permissions
* Connected your Linear account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Linear Integration

### 1. Connect Your Linear Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Linear** in the Authentication Integrations section
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


## Usage Examples

### Basic Linear Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Linear capabilities
linear_agent = Agent(
    role="Development Manager",
    goal="Manage Linear issues and track development progress efficiently",
    backstory="An AI assistant specialized in software development project management.",
    apps=['linear']  # All Linear actions will be available
)


# Task to create a bug report
create_bug_task = Task(
    description="Create a high-priority bug report for the authentication system and assign it to the backend team",
    agent=linear_agent,
    expected_output="Bug report created successfully with issue ID"
)


# Run the task
crew = Crew(
    agents=[linear_agent],
    tasks=[create_bug_task]
)

crew.kickoff()
```

### Filtering Specific Linear Tools

```python  theme={null}

issue_manager = Agent(
    role="Issue Manager",
    goal="Create and manage Linear issues efficiently",
    backstory="An AI assistant that focuses on issue creation and lifecycle management.",
    apps=['linear/create_issue']
)


# Task to manage issue workflow
issue_workflow = Task(
    description="Create a feature request issue and update the status of related issues to reflect current progress",
    agent=issue_manager,
    expected_output="Feature request created and related issues updated"
)

crew = Crew(
    agents=[issue_manager],
    tasks=[issue_workflow]
)

crew.kickoff()
```

### Project and Team Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate projects and teams in Linear efficiently",
    backstory="An experienced project coordinator who manages development cycles and team workflows.",
    apps=['linear']
)


# Task to coordinate project setup
project_coordination = Task(
    description="""
    1. Search for engineering teams in Linear
    2. Create a new project for Q2 feature development
    3. Associate the project with relevant teams
    4. Create initial project milestones as issues
    """,
    agent=project_coordinator,
    expected_output="Q2 project created with teams assigned and initial milestones established"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[project_coordination]
)

crew.kickoff()
```

### Issue Hierarchy and Sub-task Management

```python  theme={null}
from crewai import Agent, Task, Crew

task_organizer = Agent(
    role="Task Organizer",
    goal="Organize complex issues into manageable sub-tasks",
    backstory="An AI assistant that breaks down complex development work into organized sub-tasks.",
    apps=['linear']
)


# Task to create issue hierarchy
hierarchy_task = Task(
    description="""
    1. Search for large feature issues that need to be broken down
    2. For each complex issue, create sub-issues for different components
    3. Update the parent issues with proper descriptions and links to sub-issues
    4. Assign sub-issues to appropriate team members based on expertise
    """,
    agent=task_organizer,
    expected_output="Complex issues broken down into manageable sub-tasks with proper assignments"
)

crew = Crew(
    agents=[task_organizer],
    tasks=[hierarchy_task]
)

crew.kickoff()
```

### Automated Development Workflow

```python  theme={null}
from crewai import Agent, Task, Crew

workflow_automator = Agent(
    role="Workflow Automator",
    goal="Automate development workflow processes in Linear",
    backstory="An AI assistant that automates repetitive development workflow tasks.",
    apps=['linear']
)


# Complex workflow automation task
automation_task = Task(
    description="""
    1. Search for issues that have been in progress for more than 7 days
    2. Update their priorities based on due dates and project importance
    3. Create weekly sprint planning issues for each team
    4. Archive completed issues from the previous cycle
    5. Generate project status reports as new issues
    """,
    agent=workflow_automator,
    expected_output="Development workflow automated with updated priorities, sprint planning, and status reports"
)

crew = Crew(
    agents=[workflow_automator],
    tasks=[automation_task]
)

crew.kickoff()
```


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



# Microsoft Excel Integration
Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_excel

Workbook and data management with Microsoft Excel integration for CrewAI.


## Overview

Enable your agents to create and manage Excel workbooks, worksheets, tables, and charts in OneDrive or SharePoint. Manipulate data ranges, create visualizations, manage tables, and streamline your spreadsheet workflows with AI-powered automation.


## Prerequisites

Before using the Microsoft Excel integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Microsoft 365 account with Excel and OneDrive/SharePoint access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Microsoft Excel Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Excel** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for files and Excel workbook access
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
  <Accordion title="microsoft_excel/create_workbook">
    **Description:** Create a new Excel workbook in OneDrive or SharePoint.

    **Parameters:**

    * `file_path` (string, required): Path where to create the workbook (e.g., 'MyWorkbook.xlsx')
    * `worksheets` (array, optional): Initial worksheets to create
      ```json  theme={null}
      [
        {
          "name": "Sheet1"
        },
        {
          "name": "Data"
        }
      ]
      ```
  </Accordion>

  <Accordion title="microsoft_excel/get_workbooks">
    **Description:** Get all Excel workbooks from OneDrive or SharePoint.

    **Parameters:**

    * `select` (string, optional): Select specific properties to return
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

  <Accordion title="microsoft_excel/get_worksheets">
    **Description:** Get all worksheets in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `select` (string, optional): Select specific properties to return (e.g., 'id,name,position')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

  <Accordion title="microsoft_excel/create_worksheet">
    **Description:** Create a new worksheet in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `name` (string, required): Name of the new worksheet
  </Accordion>

  <Accordion title="microsoft_excel/get_range_data">
    **Description:** Get data from a specific range in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
  </Accordion>

  <Accordion title="microsoft_excel/update_range_data">
    **Description:** Update data in a specific range in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
    * `values` (array, required): 2D array of values to set in the range
      ```json  theme={null}
      [
        ["Name", "Age", "City"],
        ["John", 30, "New York"],
        ["Jane", 25, "Los Angeles"]
      ]
      ```
  </Accordion>

  <Accordion title="microsoft_excel/add_table">
    **Description:** Create a table in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range for the table (e.g., 'A1:D10')
    * `has_headers` (boolean, optional): Whether the first row contains headers. Default: true
  </Accordion>

  <Accordion title="microsoft_excel/get_tables">
    **Description:** Get all tables in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

  <Accordion title="microsoft_excel/add_table_row">
    **Description:** Add a new row to an Excel table.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `table_name` (string, required): Name of the table
    * `values` (array, required): Array of values for the new row
      ```json  theme={null}
      ["John Doe", 35, "Manager", "Sales"]
      ```
  </Accordion>

  <Accordion title="microsoft_excel/create_chart">
    **Description:** Create a chart in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `chart_type` (string, required): Type of chart (e.g., 'ColumnClustered', 'Line', 'Pie')
    * `source_data` (string, required): Range of data for the chart (e.g., 'A1:B10')
    * `series_by` (string, optional): How to interpret the data ('Auto', 'Columns', or 'Rows'). Default: Auto
  </Accordion>

  <Accordion title="microsoft_excel/get_cell">
    **Description:** Get the value of a single cell in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `row` (integer, required): Row number (0-based)
    * `column` (integer, required): Column number (0-based)
  </Accordion>

  <Accordion title="microsoft_excel/get_used_range">
    **Description:** Get the used range of an Excel worksheet (contains all data).

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

  <Accordion title="microsoft_excel/list_charts">
    **Description:** Get all charts in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

  <Accordion title="microsoft_excel/delete_worksheet">
    **Description:** Delete a worksheet from an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet to delete
  </Accordion>

  <Accordion title="microsoft_excel/delete_table">
    **Description:** Delete a table from an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `table_name` (string, required): Name of the table to delete
  </Accordion>

  <Accordion title="microsoft_excel/list_names">
    **Description:** Get all named ranges in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Excel Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Excel capabilities
excel_agent = Agent(
    role="Excel Data Manager",
    goal="Manage Excel workbooks and data efficiently",
    backstory="An AI assistant specialized in Excel data management and analysis.",
    apps=['microsoft_excel']  # All Excel actions will be available
)


# Task to create and populate a workbook
data_management_task = Task(
    description="Create a new sales report workbook with data analysis and charts",
    agent=excel_agent,
    expected_output="Excel workbook created with sales data, analysis, and visualizations"
)


# Run the task
crew = Crew(
    agents=[excel_agent],
    tasks=[data_management_task]
)

crew.kickoff()
```

### Data Analysis and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze data in Excel and create comprehensive reports",
    backstory="An AI assistant that specializes in data analysis and Excel reporting.",
    apps=[
        'microsoft_excel/get_workbooks',
        'microsoft_excel/get_range_data',
        'microsoft_excel/create_chart',
        'microsoft_excel/add_table'
    ]
)


# Task to analyze existing data
analysis_task = Task(
    description="Analyze sales data in existing workbooks and create summary charts and tables",
    agent=data_analyst,
    expected_output="Data analyzed with summary charts and tables created"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Workbook Creation and Structure

```python  theme={null}
from crewai import Agent, Task, Crew

workbook_creator = Agent(
    role="Workbook Creator",
    goal="Create structured Excel workbooks with multiple worksheets and data organization",
    backstory="An AI assistant that creates well-organized Excel workbooks for various business needs.",
    apps=['microsoft_excel']
)


# Task to create structured workbooks
creation_task = Task(
    description="""
    1. Create a new quarterly report workbook
    2. Add multiple worksheets for different departments
    3. Create tables with headers for data organization
    4. Set up charts for key metrics visualization
    """,
    agent=workbook_creator,
    expected_output="Structured workbook created with multiple worksheets, tables, and charts"
)

crew = Crew(
    agents=[workbook_creator],
    tasks=[creation_task]
)

crew.kickoff()
```

### Data Manipulation and Updates

```python  theme={null}
from crewai import Agent, Task, Crew

data_manipulator = Agent(
    role="Data Manipulator",
    goal="Update and manipulate data in Excel worksheets efficiently",
    backstory="An AI assistant that handles data updates, table management, and range operations.",
    apps=['microsoft_excel']
)


# Task to manipulate data
manipulation_task = Task(
    description="""
    1. Get data from existing worksheets
    2. Update specific ranges with new information
    3. Add new rows to existing tables
    4. Create additional charts based on updated data
    5. Organize data across multiple worksheets
    """,
    agent=data_manipulator,
    expected_output="Data updated across worksheets with new charts and organized structure"
)

crew = Crew(
    agents=[data_manipulator],
    tasks=[manipulation_task]
)

crew.kickoff()
```

### Advanced Excel Automation

```python  theme={null}
from crewai import Agent, Task, Crew

excel_automator = Agent(
    role="Excel Automator",
    goal="Automate complex Excel workflows and data processing",
    backstory="An AI assistant that automates sophisticated Excel operations and data workflows.",
    apps=['microsoft_excel']
)


# Complex automation task
automation_task = Task(
    description="""
    1. Scan all Excel workbooks for specific data patterns
    2. Create consolidated reports from multiple workbooks
    3. Generate charts and tables for trend analysis
    4. Set up named ranges for easy data reference
    5. Create dashboard worksheets with key metrics
    6. Clean up unused worksheets and tables
    """,
    agent=excel_automator,
    expected_output="Automated Excel workflow completed with consolidated reports and dashboards"
)

crew = Crew(
    agents=[excel_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

### Financial Modeling and Analysis

```python  theme={null}
from crewai import Agent, Task, Crew

financial_modeler = Agent(
    role="Financial Modeler",
    goal="Create financial models and analysis in Excel",
    backstory="An AI assistant specialized in financial modeling and analysis using Excel.",
    apps=['microsoft_excel']
)


# Task for financial modeling
modeling_task = Task(
    description="""
    1. Create financial model workbooks with multiple scenarios
    2. Set up input tables for assumptions and variables
    3. Create calculation worksheets with formulas and logic
    4. Generate charts for financial projections and trends
    5. Add summary tables for key financial metrics
    6. Create sensitivity analysis tables
    """,
    agent=financial_modeler,
    expected_output="Financial model created with scenarios, calculations, and analysis charts"
)

crew = Crew(
    agents=[financial_modeler],
    tasks=[modeling_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Permission Errors**

* Ensure your Microsoft account has appropriate permissions for Excel and OneDrive/SharePoint
* Verify that the OAuth connection includes required scopes (Files.Read.All, Files.ReadWrite.All)
* Check that you have access to the specific workbooks you're trying to modify

**File ID and Path Issues**

* Verify that file IDs are correct and files exist in your OneDrive or SharePoint
* Ensure file paths are properly formatted when creating new workbooks
* Check that workbook files have the correct .xlsx extension

**Worksheet and Range Issues**

* Verify that worksheet names exist in the specified workbook
* Ensure range addresses are properly formatted (e.g., 'A1:C10')
* Check that ranges don't exceed worksheet boundaries

**Data Format Issues**

* Ensure data values are properly formatted for Excel (strings, numbers, integers)
* Verify that 2D arrays for ranges have consistent row and column counts
* Check that table data includes proper headers when has\_headers is true

**Chart Creation Issues**

* Verify that chart types are supported (ColumnClustered, Line, Pie, etc.)
* Ensure source data ranges contain appropriate data for the chart type
* Check that the source data range exists and contains data

**Table Management Issues**

* Ensure table names are unique within worksheets
* Verify that table ranges don't overlap with existing tables
* Check that new row data matches the table's column structure

**Cell and Range Operations**

* Verify that row and column indices are 0-based for cell operations
* Ensure ranges contain data when using get\_used\_range
* Check that named ranges exist before referencing them

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Excel integration setup or troubleshooting.
</Card>



# Microsoft OneDrive Integration
Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_onedrive

File and folder management with Microsoft OneDrive integration for CrewAI.


## Overview

Enable your agents to upload, download, and manage files and folders in Microsoft OneDrive. Automate file operations, organize content, create sharing links, and streamline your cloud storage workflows with AI-powered automation.


## Prerequisites

Before using the Microsoft OneDrive integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Microsoft account with OneDrive access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Microsoft OneDrive Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft OneDrive** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file access
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
  <Accordion title="microsoft_onedrive/list_files">
    **Description:** List files and folders in OneDrive.

    **Parameters:**

    * `top` (integer, optional): Number of items to retrieve (max 1000). Default is `50`.
    * `orderby` (string, optional): Order by field (e.g., "name asc", "lastModifiedDateTime desc"). Default is "name asc".
    * `filter` (string, optional): OData filter expression.
  </Accordion>

  <Accordion title="microsoft_onedrive/get_file_info">
    **Description:** Get information about a specific file or folder.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder.
  </Accordion>

  <Accordion title="microsoft_onedrive/download_file">
    **Description:** Download a file from OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file to download.
  </Accordion>

  <Accordion title="microsoft_onedrive/upload_file">
    **Description:** Upload a file to OneDrive.

    **Parameters:**

    * `file_name` (string, required): Name of the file to upload.
    * `content` (string, required): Base64 encoded file content.
  </Accordion>

  <Accordion title="microsoft_onedrive/create_folder">
    **Description:** Create a new folder in OneDrive.

    **Parameters:**

    * `folder_name` (string, required): Name of the folder to create.
  </Accordion>

  <Accordion title="microsoft_onedrive/delete_item">
    **Description:** Delete a file or folder from OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to delete.
  </Accordion>

  <Accordion title="microsoft_onedrive/copy_item">
    **Description:** Copy a file or folder in OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to copy.
    * `parent_id` (string, optional): The ID of the destination folder (optional, defaults to root).
    * `new_name` (string, optional): New name for the copied item (optional).
  </Accordion>

  <Accordion title="microsoft_onedrive/move_item">
    **Description:** Move a file or folder in OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to move.
    * `parent_id` (string, required): The ID of the destination folder.
    * `new_name` (string, optional): New name for the item (optional).
  </Accordion>

  <Accordion title="microsoft_onedrive/search_files">
    **Description:** Search for files and folders in OneDrive.

    **Parameters:**

    * `query` (string, required): Search query string.
    * `top` (integer, optional): Number of results to return (max 1000). Default is `50`.
  </Accordion>

  <Accordion title="microsoft_onedrive/share_item">
    **Description:** Create a sharing link for a file or folder.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to share.
    * `type` (string, optional): Type of sharing link. Enum: `view`, `edit`, `embed`. Default is `view`.
    * `scope` (string, optional): Scope of the sharing link. Enum: `anonymous`, `organization`. Default is `anonymous`.
  </Accordion>

  <Accordion title="microsoft_onedrive/get_thumbnails">
    **Description:** Get thumbnails for a file.

    **Parameters:**

    * `item_id` (string, required): The ID of the file.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Microsoft OneDrive Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Microsoft OneDrive capabilities
onedrive_agent = Agent(
    role="File Manager",
    goal="Manage files and folders in OneDrive efficiently",
    backstory="An AI assistant specialized in Microsoft OneDrive file operations and organization.",
    apps=['microsoft_onedrive']  # All OneDrive actions will be available
)


# Task to list files and create a folder
organize_files_task = Task(
    description="List all files in my OneDrive root directory and create a new folder called 'Project Documents'.",
    agent=onedrive_agent,
    expected_output="List of files displayed and new folder 'Project Documents' created."
)


# Run the task
crew = Crew(
    agents=[onedrive_agent],
    tasks=[organize_files_task]
)

crew.kickoff()
```

### File Upload and Management

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent focused on file operations
file_operator = Agent(
    role="File Operator",
    goal="Upload, download, and manage files with precision",
    backstory="An AI assistant skilled in file handling and content management.",
    apps=['microsoft_onedrive/upload_file', 'microsoft_onedrive/download_file', 'microsoft_onedrive/get_file_info']
)


# Task to upload and manage a file
file_management_task = Task(
    description="Upload a text file named 'report.txt' with content 'This is a sample report for the project.' Then get information about the uploaded file.",
    agent=file_operator,
    expected_output="File uploaded successfully and file information retrieved."
)

crew = Crew(
    agents=[file_operator],
    tasks=[file_management_task]
)

crew.kickoff()
```

### File Organization and Sharing

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent for file organization and sharing
file_organizer = Agent(
    role="File Organizer",
    goal="Organize files and create sharing links for collaboration",
    backstory="An AI assistant that excels at organizing files and managing sharing permissions.",
    apps=['microsoft_onedrive/search_files', 'microsoft_onedrive/move_item', 'microsoft_onedrive/share_item', 'microsoft_onedrive/create_folder']
)


# Task to organize and share files
organize_share_task = Task(
    description="Search for files containing 'presentation' in the name, create a folder called 'Presentations', move the found files to this folder, and create a view-only sharing link for the folder.",
    agent=file_organizer,
    expected_output="Files organized into 'Presentations' folder and sharing link created."
)

crew = Crew(
    agents=[file_organizer],
    tasks=[organize_share_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for file access (e.g., `Files.Read`, `Files.ReadWrite`).
* Verify that the OAuth connection includes all required scopes.

**File Upload Issues**

* Ensure `file_name` and `content` are provided for file uploads.
* Content must be Base64 encoded for binary files.
* Check that you have write permissions to OneDrive.

**File/Folder ID Issues**

* Double-check item IDs for correctness when accessing specific files or folders.
* Item IDs are returned by other operations like `list_files` or `search_files`.
* Ensure the referenced items exist and are accessible.

**Search and Filter Operations**

* Use appropriate search terms for `search_files` operations.
* For `filter` parameters, use proper OData syntax.

**File Operations (Copy/Move)**

* For `move_item`, ensure both `item_id` and `parent_id` are provided.
* For `copy_item`, only `item_id` is required; `parent_id` defaults to root if not specified.
* Verify that destination folders exist and are accessible.

**Sharing Link Creation**

* Ensure the item exists before creating sharing links.
* Choose appropriate `type` and `scope` based on your sharing requirements.
* `anonymous` scope allows access without sign-in; `organization` requires organizational account.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft OneDrive integration setup or troubleshooting.
</Card>



# Microsoft Outlook Integration
Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_outlook

Email, calendar, and contact management with Microsoft Outlook integration for CrewAI.


## Overview

Enable your agents to access and manage Outlook emails, calendar events, and contacts. Send emails, retrieve messages, manage calendar events, and organize contacts with AI-powered automation.


## Prerequisites

Before using the Microsoft Outlook integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Microsoft account with Outlook access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Microsoft Outlook Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Outlook** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for mail, calendar, and contact access
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
  <Accordion title="microsoft_outlook/get_messages">
    **Description:** Get email messages from the user's mailbox.

    **Parameters:**

    * `top` (integer, optional): Number of messages to retrieve (max 1000). Default is `10`.
    * `filter` (string, optional): OData filter expression (e.g., "isRead eq false").
    * `search` (string, optional): Search query string.
    * `orderby` (string, optional): Order by field (e.g., "receivedDateTime desc"). Default is "receivedDateTime desc".
    * `select` (string, optional): Select specific properties to return.
    * `expand` (string, optional): Expand related resources inline.
  </Accordion>

  <Accordion title="microsoft_outlook/send_email">
    **Description:** Send an email message.

    **Parameters:**

    * `to_recipients` (array, required): Array of recipient email addresses.
    * `cc_recipients` (array, optional): Array of CC recipient email addresses.
    * `bcc_recipients` (array, optional): Array of BCC recipient email addresses.
    * `subject` (string, required): Email subject.
    * `body` (string, required): Email body content.
    * `body_type` (string, optional): Body content type. Enum: `Text`, `HTML`. Default is `HTML`.
    * `importance` (string, optional): Message importance level. Enum: `low`, `normal`, `high`. Default is `normal`.
    * `reply_to` (array, optional): Array of reply-to email addresses.
    * `save_to_sent_items` (boolean, optional): Whether to save the message to Sent Items folder. Default is `true`.
  </Accordion>

  <Accordion title="microsoft_outlook/get_calendar_events">
    **Description:** Get calendar events from the user's calendar.

    **Parameters:**

    * `top` (integer, optional): Number of events to retrieve (max 1000). Default is `10`.
    * `skip` (integer, optional): Number of events to skip. Default is `0`.
    * `filter` (string, optional): OData filter expression (e.g., "start/dateTime ge '2024-01-01T00:00:00Z'").
    * `orderby` (string, optional): Order by field (e.g., "start/dateTime asc"). Default is "start/dateTime asc".
  </Accordion>

  <Accordion title="microsoft_outlook/create_calendar_event">
    **Description:** Create a new calendar event.

    **Parameters:**

    * `subject` (string, required): Event subject/title.
    * `body` (string, optional): Event body/description.
    * `start_datetime` (string, required): Start date and time in ISO 8601 format (e.g., '2024-01-20T10:00:00').
    * `end_datetime` (string, required): End date and time in ISO 8601 format.
    * `timezone` (string, optional): Time zone (e.g., 'Pacific Standard Time'). Default is `UTC`.
    * `location` (string, optional): Event location.
    * `attendees` (array, optional): Array of attendee email addresses.
  </Accordion>

  <Accordion title="microsoft_outlook/get_contacts">
    **Description:** Get contacts from the user's address book.

    **Parameters:**

    * `top` (integer, optional): Number of contacts to retrieve (max 1000). Default is `10`.
    * `skip` (integer, optional): Number of contacts to skip. Default is `0`.
    * `filter` (string, optional): OData filter expression.
    * `orderby` (string, optional): Order by field (e.g., "displayName asc"). Default is "displayName asc".
  </Accordion>

  <Accordion title="microsoft_outlook/create_contact">
    **Description:** Create a new contact in the user's address book.

    **Parameters:**

    * `displayName` (string, required): Contact's display name.
    * `givenName` (string, optional): Contact's first name.
    * `surname` (string, optional): Contact's last name.
    * `emailAddresses` (array, optional): Array of email addresses. Each item is an object with `address` (string) and `name` (string).
    * `businessPhones` (array, optional): Array of business phone numbers.
    * `homePhones` (array, optional): Array of home phone numbers.
    * `jobTitle` (string, optional): Contact's job title.
    * `companyName` (string, optional): Contact's company name.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Microsoft Outlook Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Microsoft Outlook capabilities
outlook_agent = Agent(
    role="Email Assistant",
    goal="Manage emails, calendar events, and contacts efficiently",
    backstory="An AI assistant specialized in Microsoft Outlook operations and communication management.",
    apps=['microsoft_outlook']  # All Outlook actions will be available
)


# Task to send an email
send_email_task = Task(
    description="Send an email to 'colleague@example.com' with subject 'Project Update' and body 'Hi, here is the latest project update. Best regards.'",
    agent=outlook_agent,
    expected_output="Email sent successfully to colleague@example.com"
)


# Run the task
crew = Crew(
    agents=[outlook_agent],
    tasks=[send_email_task]
)

crew.kickoff()
```

### Email Management and Search

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent focused on email management
email_manager = Agent(
    role="Email Manager",
    goal="Retrieve, search, and organize email messages",
    backstory="An AI assistant skilled in email organization and management.",
    apps=['microsoft_outlook/get_messages']
)


# Task to search and retrieve emails
search_emails_task = Task(
    description="Get the latest 20 unread emails and provide a summary of the most important ones.",
    agent=email_manager,
    expected_output="Summary of the most important unread emails with key details."
)

crew = Crew(
    agents=[email_manager],
    tasks=[search_emails_task]
)

crew.kickoff()
```

### Calendar and Contact Management

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent for calendar and contact management
scheduler = Agent(
    role="Calendar and Contact Manager",
    goal="Manage calendar events and maintain contact information",
    backstory="An AI assistant that handles scheduling and contact organization.",
    apps=['microsoft_outlook/create_calendar_event', 'microsoft_outlook/get_calendar_events', 'microsoft_outlook/create_contact']
)


# Task to create a meeting and add a contact
schedule_task = Task(
    description="Create a calendar event for tomorrow at 2 PM titled 'Team Meeting' with location 'Conference Room A', and create a new contact for 'John Smith' with email 'john.smith@example.com' and job title 'Project Manager'.",
    agent=scheduler,
    expected_output="Calendar event created and new contact added successfully."
)

crew = Crew(
    agents=[scheduler],
    tasks=[schedule_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for mail, calendar, and contact access.
* Required scopes include: `Mail.Read`, `Mail.Send`, `Calendars.Read`, `Calendars.ReadWrite`, `Contacts.Read`, `Contacts.ReadWrite`.
* Verify that the OAuth connection includes all required scopes.

**Email Sending Issues**

* Ensure `to_recipients`, `subject`, and `body` are provided for `send_email`.
* Check that email addresses are properly formatted.
* Verify that the account has `Mail.Send` permissions.

**Calendar Event Creation**

* Ensure `subject`, `start_datetime`, and `end_datetime` are provided.
* Use proper ISO 8601 format for datetime fields (e.g., '2024-01-20T10:00:00').
* Verify timezone settings if events appear at incorrect times.

**Contact Management**

* For `create_contact`, ensure `displayName` is provided as it's required.
* When providing `emailAddresses`, use the proper object format with `address` and `name` properties.

**Search and Filter Issues**

* Use proper OData syntax for `filter` parameters.
* For date filters, use ISO 8601 format (e.g., "receivedDateTime ge '2024-01-01T00:00:00Z'").

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Outlook integration setup or troubleshooting.
</Card>



# Microsoft SharePoint Integration
Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_sharepoint

Site, list, and document management with Microsoft SharePoint integration for CrewAI.


## Overview

Enable your agents to access and manage SharePoint sites, lists, and document libraries. Retrieve site information, manage list items, upload and organize files, and streamline your SharePoint workflows with AI-powered automation.


## Prerequisites

Before using the Microsoft SharePoint integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Microsoft 365 account with SharePoint access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Microsoft SharePoint Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft SharePoint** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for SharePoint sites and content access
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
  <Accordion title="microsoft_sharepoint/get_sites">
    **Description:** Get all SharePoint sites the user has access to.

    **Parameters:**

    * `search` (string, optional): Search query to filter sites
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `skip` (integer, optional): Number of items to skip. Minimum: 0
    * `orderby` (string, optional): Order results by specified properties (e.g., 'displayName desc')
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_site">
    **Description:** Get information about a specific SharePoint site.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl,drives')
    * `expand` (string, optional): Expand related resources inline (e.g., 'drives,lists')
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_site_lists">
    **Description:** Get all lists in a SharePoint site.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_list">
    **Description:** Get information about a specific list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_list_items">
    **Description:** Get items from a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `expand` (string, optional): Expand related data (e.g., 'fields')
  </Accordion>

  <Accordion title="microsoft_sharepoint/create_list_item">
    **Description:** Create a new item in a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `fields` (object, required): The field values for the new item
      ```json  theme={null}
      {
        "Title": "New Item Title",
        "Description": "Item description",
        "Status": "Active"
      }
      ```
  </Accordion>

  <Accordion title="microsoft_sharepoint/update_list_item">
    **Description:** Update an item in a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to update
    * `fields` (object, required): The field values to update
      ```json  theme={null}
      {
        "Title": "Updated Title",
        "Status": "Completed"
      }
      ```
  </Accordion>

  <Accordion title="microsoft_sharepoint/delete_list_item">
    **Description:** Delete an item from a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to delete
  </Accordion>

  <Accordion title="microsoft_sharepoint/upload_file_to_library">
    **Description:** Upload a file to a SharePoint document library.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `file_path` (string, required): The path where to upload the file (e.g., 'folder/filename.txt')
    * `content` (string, required): The file content to upload
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_drive_items">
    **Description:** Get files and folders from a SharePoint document library.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

  <Accordion title="microsoft_sharepoint/delete_drive_item">
    **Description:** Delete a file or folder from SharePoint document library.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `item_id` (string, required): The ID of the file or folder to delete
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic SharePoint Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with SharePoint capabilities
sharepoint_agent = Agent(
    role="SharePoint Manager",
    goal="Manage SharePoint sites, lists, and documents efficiently",
    backstory="An AI assistant specialized in SharePoint content management and collaboration.",
    apps=['microsoft_sharepoint']  # All SharePoint actions will be available
)


# Task to organize SharePoint content
content_organization_task = Task(
    description="List all accessible SharePoint sites and organize content by department",
    agent=sharepoint_agent,
    expected_output="SharePoint sites listed and content organized by department"
)


# Run the task
crew = Crew(
    agents=[sharepoint_agent],
    tasks=[content_organization_task]
)

crew.kickoff()
```

### List Management and Data Operations

```python  theme={null}
from crewai import Agent, Task, Crew

list_manager = Agent(
    role="List Manager",
    goal="Manage SharePoint lists and data efficiently",
    backstory="An AI assistant that focuses on SharePoint list management and data operations.",
    apps=[
        'microsoft_sharepoint/get_site_lists',
        'microsoft_sharepoint/get_list_items',
        'microsoft_sharepoint/create_list_item',
        'microsoft_sharepoint/update_list_item'
    ]
)


# Task to manage list data
list_management_task = Task(
    description="Get all lists from the project site, review items, and update status for completed tasks",
    agent=list_manager,
    expected_output="SharePoint lists reviewed and task statuses updated"
)

crew = Crew(
    agents=[list_manager],
    tasks=[list_management_task]
)

crew.kickoff()
```

### Document Library Management

```python  theme={null}
from crewai import Agent, Task, Crew

document_manager = Agent(
    role="Document Manager",
    goal="Manage SharePoint document libraries and files",
    backstory="An AI assistant that specializes in document organization and file management.",
    apps=['microsoft_sharepoint']
)


# Task to manage documents
document_task = Task(
    description="""
    1. Get all files from the main document library
    2. Upload new policy documents to the appropriate folders
    3. Organize files by department and date
    4. Remove outdated documents
    """,
    agent=document_manager,
    expected_output="Document library organized with new files uploaded and outdated files removed"
)

crew = Crew(
    agents=[document_manager],
    tasks=[document_task]
)

crew.kickoff()
```

### Site Administration and Analysis

```python  theme={null}
from crewai import Agent, Task, Crew

site_administrator = Agent(
    role="Site Administrator",
    goal="Administer and analyze SharePoint sites",
    backstory="An AI assistant that handles site administration and provides insights on site usage.",
    apps=['microsoft_sharepoint']
)


# Task for site administration
admin_task = Task(
    description="""
    1. Get information about all accessible SharePoint sites
    2. Analyze site structure and content organization
    3. Identify sites with low activity or outdated content
    4. Generate recommendations for site optimization
    """,
    agent=site_administrator,
    expected_output="Site analysis completed with optimization recommendations"
)

crew = Crew(
    agents=[site_administrator],
    tasks=[admin_task]
)

crew.kickoff()
```

### Automated Content Workflows

```python  theme={null}
from crewai import Agent, Task, Crew

workflow_automator = Agent(
    role="Workflow Automator",
    goal="Automate SharePoint content workflows and processes",
    backstory="An AI assistant that automates complex SharePoint workflows and content management processes.",
    apps=['microsoft_sharepoint']
)


# Complex workflow automation task
automation_task = Task(
    description="""
    1. Monitor project lists across multiple sites
    2. Create status reports based on list data
    3. Upload reports to designated document libraries
    4. Update project tracking lists with completion status
    5. Archive completed project documents
    6. Send notifications for overdue items
    """,
    agent=workflow_automator,
    expected_output="Automated workflow completed with status reports generated and project tracking updated"
)

crew = Crew(
    agents=[workflow_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

### Data Integration and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_integrator = Agent(
    role="Data Integrator",
    goal="Integrate and analyze data across SharePoint sites and lists",
    backstory="An AI assistant that specializes in data integration and cross-site analysis.",
    apps=['microsoft_sharepoint']
)


# Task for data integration
integration_task = Task(
    description="""
    1. Get data from multiple SharePoint lists across different sites
    2. Consolidate information into comprehensive reports
    3. Create new list items with aggregated data
    4. Upload analytical reports to executive document library
    5. Update dashboard lists with key metrics
    """,
    agent=data_integrator,
    expected_output="Data integrated across sites with comprehensive reports and updated dashboards"
)

crew = Crew(
    agents=[data_integrator],
    tasks=[integration_task]
)

crew.kickoff()
```


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



# Microsoft Teams Integration
Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_teams

Team collaboration and communication with Microsoft Teams integration for CrewAI.


## Overview

Enable your agents to access Teams data, send messages, create meetings, and manage channels. Automate team communication, schedule meetings, retrieve messages, and streamline your collaboration workflows with AI-powered automation.


## Prerequisites

Before using the Microsoft Teams integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Microsoft account with Teams access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Microsoft Teams Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Teams** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for Teams access
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
  <Accordion title="microsoft_teams/get_teams">
    **Description:** Get all teams the user is a member of.

    **Parameters:**

    * No parameters required.
  </Accordion>

  <Accordion title="microsoft_teams/get_channels">
    **Description:** Get channels in a specific team.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
  </Accordion>

  <Accordion title="microsoft_teams/send_message">
    **Description:** Send a message to a Teams channel.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `message` (string, required): The message content.
    * `content_type` (string, optional): Content type (html or text). Enum: `html`, `text`. Default is `text`.
  </Accordion>

  <Accordion title="microsoft_teams/get_messages">
    **Description:** Get messages from a Teams channel.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `top` (integer, optional): Number of messages to retrieve (max 50). Default is `20`.
  </Accordion>

  <Accordion title="microsoft_teams/create_meeting">
    **Description:** Create a Teams meeting.

    **Parameters:**

    * `subject` (string, required): Meeting subject/title.
    * `startDateTime` (string, required): Meeting start time (ISO 8601 format with timezone).
    * `endDateTime` (string, required): Meeting end time (ISO 8601 format with timezone).
  </Accordion>

  <Accordion title="microsoft_teams/search_online_meetings_by_join_url">
    **Description:** Search online meetings by Join Web URL.

    **Parameters:**

    * `join_web_url` (string, required): The join web URL of the meeting to search for.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Microsoft Teams Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Microsoft Teams capabilities
teams_agent = Agent(
    role="Teams Coordinator",
    goal="Manage Teams communication and meetings efficiently",
    backstory="An AI assistant specialized in Microsoft Teams operations and team collaboration.",
    apps=['microsoft_teams']  # All Teams actions will be available
)


# Task to list teams and channels
explore_teams_task = Task(
    description="List all teams I'm a member of and then get the channels for the first team.",
    agent=teams_agent,
    expected_output="List of teams and channels displayed."
)


# Run the task
crew = Crew(
    agents=[teams_agent],
    tasks=[explore_teams_task]
)

crew.kickoff()
```

### Messaging and Communication

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent focused on messaging
messenger = Agent(
    role="Teams Messenger",
    goal="Send and retrieve messages in Teams channels",
    backstory="An AI assistant skilled in team communication and message management.",
    apps=['microsoft_teams/send_message', 'microsoft_teams/get_messages']
)


# Task to send a message and retrieve recent messages
messaging_task = Task(
    description="Send a message 'Hello team! This is an automated update from our AI assistant.' to the General channel of team 'your_team_id', then retrieve the last 10 messages from that channel.",
    agent=messenger,
    expected_output="Message sent successfully and recent messages retrieved."
)

crew = Crew(
    agents=[messenger],
    tasks=[messaging_task]
)

crew.kickoff()
```

### Meeting Management

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent for meeting management
meeting_scheduler = Agent(
    role="Meeting Scheduler",
    goal="Create and manage Teams meetings",
    backstory="An AI assistant that handles meeting scheduling and organization.",
    apps=['microsoft_teams/create_meeting', 'microsoft_teams/search_online_meetings_by_join_url']
)


# Task to create a meeting
schedule_meeting_task = Task(
    description="Create a Teams meeting titled 'Weekly Team Sync' scheduled for tomorrow at 10:00 AM lasting for 1 hour (use proper ISO 8601 format with timezone).",
    agent=meeting_scheduler,
    expected_output="Teams meeting created successfully with meeting details."
)

crew = Crew(
    agents=[meeting_scheduler],
    tasks=[schedule_meeting_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for Teams access.
* Required scopes include: `Team.ReadBasic.All`, `Channel.ReadBasic.All`, `ChannelMessage.Send`, `ChannelMessage.Read.All`, `OnlineMeetings.ReadWrite`, `OnlineMeetings.Read`.
* Verify that the OAuth connection includes all required scopes.

**Team and Channel Access**

* Ensure you are a member of the teams you're trying to access.
* Double-check team IDs and channel IDs for correctness.
* Team and channel IDs can be obtained using the `get_teams` and `get_channels` actions.

**Message Sending Issues**

* Ensure `team_id`, `channel_id`, and `message` are provided for `send_message`.
* Verify that you have permissions to send messages to the specified channel.
* Choose appropriate `content_type` (text or html) based on your message format.

**Meeting Creation**

* Ensure `subject`, `startDateTime`, and `endDateTime` are provided.
* Use proper ISO 8601 format with timezone for datetime fields (e.g., '2024-01-20T10:00:00-08:00').
* Verify that the meeting times are in the future.

**Message Retrieval Limitations**

* The `get_messages` action can retrieve a maximum of 50 messages per request.
* Messages are returned in reverse chronological order (newest first).

**Meeting Search**

* For `search_online_meetings_by_join_url`, ensure the join URL is exact and properly formatted.
* The URL should be the complete Teams meeting join URL.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Teams integration setup or troubleshooting.
</Card>



# Microsoft Word Integration
Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_word

Document creation and management with Microsoft Word integration for CrewAI.


## Overview

Enable your agents to create, read, and manage Word documents and text files in OneDrive or SharePoint. Automate document creation, retrieve content, manage document properties, and streamline your document workflows with AI-powered automation.


## Prerequisites

Before using the Microsoft Word integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Microsoft account with Word and OneDrive/SharePoint access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Microsoft Word Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Word** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file access
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
  <Accordion title="microsoft_word/get_documents">
    **Description:** Get all Word documents from OneDrive or SharePoint.

    **Parameters:**

    * `select` (string, optional): Select specific properties to return.
    * `filter` (string, optional): Filter results using OData syntax.
    * `expand` (string, optional): Expand related resources inline.
    * `top` (integer, optional): Number of items to return (min 1, max 999).
    * `orderby` (string, optional): Order results by specified properties.
  </Accordion>

  <Accordion title="microsoft_word/create_text_document">
    **Description:** Create a text document (.txt) with content. RECOMMENDED for programmatic content creation that needs to be readable and editable.

    **Parameters:**

    * `file_name` (string, required): Name of the text document (should end with .txt).
    * `content` (string, optional): Text content for the document. Default is "This is a new text document created via API."
  </Accordion>

  <Accordion title="microsoft_word/get_document_content">
    **Description:** Get the content of a document (works best with text files).

    **Parameters:**

    * `file_id` (string, required): The ID of the document.
  </Accordion>

  <Accordion title="microsoft_word/get_document_properties">
    **Description:** Get properties and metadata of a document.

    **Parameters:**

    * `file_id` (string, required): The ID of the document.
  </Accordion>

  <Accordion title="microsoft_word/delete_document">
    **Description:** Delete a document.

    **Parameters:**

    * `file_id` (string, required): The ID of the document to delete.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Microsoft Word Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Microsoft Word capabilities
word_agent = Agent(
    role="Document Manager",
    goal="Manage Word documents and text files efficiently",
    backstory="An AI assistant specialized in Microsoft Word document operations and content management.",
    apps=['microsoft_word']  # All Word actions will be available
)


# Task to create a new text document
create_doc_task = Task(
    description="Create a new text document named 'meeting_notes.txt' with content 'Meeting Notes from January 2024: Key discussion points and action items.'",
    agent=word_agent,
    expected_output="New text document 'meeting_notes.txt' created successfully."
)


# Run the task
crew = Crew(
    agents=[word_agent],
    tasks=[create_doc_task]
)

crew.kickoff()
```

### Reading and Managing Documents

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent focused on document operations
document_reader = Agent(
    role="Document Reader",
    goal="Retrieve and analyze document content and properties",
    backstory="An AI assistant skilled in reading and analyzing document content.",
    apps=['microsoft_word/get_documents', 'microsoft_word/get_document_content', 'microsoft_word/get_document_properties']
)


# Task to list and read documents
read_docs_task = Task(
    description="List all Word documents in my OneDrive, then get the content and properties of the first document found.",
    agent=document_reader,
    expected_output="List of documents with content and properties of the first document."
)

crew = Crew(
    agents=[document_reader],
    tasks=[read_docs_task]
)

crew.kickoff()
```

### Document Cleanup and Organization

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent for document management
document_organizer = Agent(
    role="Document Organizer",
    goal="Organize and clean up document collections",
    backstory="An AI assistant that helps maintain organized document libraries.",
    apps=['microsoft_word/get_documents', 'microsoft_word/get_document_properties', 'microsoft_word/delete_document']
)


# Task to organize documents
organize_task = Task(
    description="List all documents, check their properties, and identify any documents that might be duplicates or outdated for potential cleanup.",
    agent=document_organizer,
    expected_output="Analysis of document library with recommendations for organization."
)

crew = Crew(
    agents=[document_organizer],
    tasks=[organize_task]
)

crew.kickoff()
```


## Troubleshooting

### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for file access (e.g., `Files.Read.All`, `Files.ReadWrite.All`).
* Verify that the OAuth connection includes all required scopes.

**File Creation Issues**

* When creating text documents, ensure the `file_name` ends with `.txt` extension.
* Verify that you have write permissions to the target location (OneDrive/SharePoint).

**Document Access Issues**

* Double-check document IDs for correctness when accessing specific documents.
* Ensure the referenced documents exist and are accessible.
* Note that this integration works best with text files (.txt) for content operations.

**Content Retrieval Limitations**

* The `get_document_content` action works best with text files (.txt).
* For complex Word documents (.docx), consider using the document properties action to get metadata.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Word integration setup or troubleshooting.
</Card>



# Notion Integration
Source: https://docs.crewai.com/en/enterprise/integrations/notion

User management and commenting with Notion integration for CrewAI.


## Overview

Enable your agents to manage users and create comments through Notion. Access workspace user information and create comments on pages and discussions, streamlining your collaboration workflows with AI-powered automation.


## Prerequisites

Before using the Notion integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Notion account with appropriate workspace permissions
* Connected your Notion account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Notion Integration

### 1. Connect Your Notion Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Notion** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for user access and comment creation
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
  <Accordion title="notion/list_users">
    **Description:** List all users in the workspace.

    **Parameters:**

    * `page_size` (integer, optional): Number of items returned in the response. Minimum: 1, Maximum: 100, Default: 100
    * `start_cursor` (string, optional): Cursor for pagination. Return results after this cursor.
  </Accordion>

  <Accordion title="notion/get_user">
    **Description:** Retrieve a specific user by ID.

    **Parameters:**

    * `user_id` (string, required): The ID of the user to retrieve.
  </Accordion>

  <Accordion title="notion/create_comment">
    **Description:** Create a comment on a page or discussion.

    **Parameters:**

    * `parent` (object, required): The parent page or discussion to comment on.
      ```json  theme={null}
      {
        "type": "page_id",
        "page_id": "PAGE_ID_HERE"
      }
      ```
      or
      ```json  theme={null}
      {
        "type": "discussion_id",
        "discussion_id": "DISCUSSION_ID_HERE"
      }
      ```
    * `rich_text` (array, required): The rich text content of the comment.
      ```json  theme={null}
      [
        {
          "type": "text",
          "text": {
            "content": "This is my comment text"
          }
        }
      ]
      ```
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Notion Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Notion capabilities
notion_agent = Agent(
    role="Workspace Manager",
    goal="Manage workspace users and facilitate collaboration through comments",
    backstory="An AI assistant specialized in user management and team collaboration.",
    apps=['notion']  # All Notion actions will be available
)


# Task to list workspace users
user_management_task = Task(
    description="List all users in the workspace and provide a summary of team members",
    agent=notion_agent,
    expected_output="Complete list of workspace users with their details"
)


# Run the task
crew = Crew(
    agents=[notion_agent],
    tasks=[user_management_task]
)

crew.kickoff()
```

### Filtering Specific Notion Tools

```python  theme={null}
comment_manager = Agent(
    role="Comment Manager",
    goal="Create and manage comments on Notion pages",
    backstory="An AI assistant that focuses on facilitating discussions through comments.",
    apps=['notion/create_comment']
)


# Task to create comments on pages
comment_task = Task(
    description="Create a summary comment on the project status page with key updates",
    agent=comment_manager,
    expected_output="Comment created successfully with project status updates"
)

crew = Crew(
    agents=[comment_manager],
    tasks=[comment_task]
)

crew.kickoff()
```

### User Information and Team Management

```python  theme={null}
from crewai import Agent, Task, Crew

team_coordinator = Agent(
    role="Team Coordinator",
    goal="Coordinate team activities and manage user information",
    backstory="An AI assistant that helps coordinate team activities and manages user information.",
    apps=['notion']
)


# Task to coordinate team activities
coordination_task = Task(
    description="""
    1. List all users in the workspace
    2. Get detailed information for specific team members
    3. Create comments on relevant pages to notify team members about updates
    """,
    agent=team_coordinator,
    expected_output="Team coordination completed with user information gathered and notifications sent"
)

crew = Crew(
    agents=[team_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
```

### Collaboration and Communication

```python  theme={null}
from crewai import Agent, Task, Crew

collaboration_facilitator = Agent(
    role="Collaboration Facilitator",
    goal="Facilitate team collaboration through comments and user management",
    backstory="An AI assistant that specializes in team collaboration and communication.",
    apps=['notion']
)


# Task to facilitate collaboration
collaboration_task = Task(
    description="""
    1. Identify active users in the workspace
    2. Create contextual comments on project pages to facilitate discussions
    3. Provide status updates and feedback through comments
    """,
    agent=collaboration_facilitator,
    expected_output="Collaboration facilitated with comments created and team members notified"
)

crew = Crew(
    agents=[collaboration_facilitator],
    tasks=[collaboration_task]
)

crew.kickoff()
```

### Automated Team Communication

```python  theme={null}
from crewai import Agent, Task, Crew

communication_automator = Agent(
    role="Communication Automator",
    goal="Automate team communication and user management workflows",
    backstory="An AI assistant that automates communication workflows and manages user interactions.",
    apps=['notion']
)


# Complex communication automation task
automation_task = Task(
    description="""
    1. List all workspace users and identify team roles
    2. Get specific user information for project stakeholders
    3. Create automated status update comments on key project pages
    4. Facilitate team communication through targeted comments
    """,
    agent=communication_automator,
    expected_output="Automated communication workflow completed with user management and comments"
)

crew = Crew(
    agents=[communication_automator],
    tasks=[automation_task]
)

crew.kickoff()
```


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



# Salesforce Integration
Source: https://docs.crewai.com/en/enterprise/integrations/salesforce

CRM and sales automation with Salesforce integration for CrewAI.


## Overview

Enable your agents to manage customer relationships, sales processes, and data through Salesforce. Create and update records, manage leads and opportunities, execute SOQL queries, and streamline your CRM workflows with AI-powered automation.


## Prerequisites

Before using the Salesforce integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Salesforce account with appropriate permissions
* Connected your Salesforce account through the [Integrations page](https://app.crewai.com/integrations)


## Setting Up Salesforce Integration

### 1. Connect Your Salesforce Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Salesforce** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for CRM and sales management
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


## Available Tools

### **Record Management**

<AccordionGroup>
  <Accordion title="salesforce/create_record_contact">
    **Description:** Create a new Contact record in Salesforce.

    **Parameters:**

    * `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

  <Accordion title="salesforce/create_record_lead">
    **Description:** Create a new Lead record in Salesforce.

    **Parameters:**

    * `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `Company` (string, required): Company - This field is required
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Status` (string, optional): Lead Status - Use Connect Portal Workflow Settings to select Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

  <Accordion title="salesforce/create_record_opportunity">
    **Description:** Create a new Opportunity record in Salesforce.

    **Parameters:**

    * `Name` (string, required): The Opportunity name - This field is required
    * `StageName` (string, optional): Opportunity Stage - Use Connect Portal Workflow Settings to select stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format - Defaults to 30 days from current date
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

  <Accordion title="salesforce/create_record_task">
    **Description:** Create a new Task record in Salesforce.

    **Parameters:**

    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, required): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `taskSubtype` (string, required): Task Subtype - Options: task, email, listEmail, call
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

  <Accordion title="salesforce/create_record_account">
    **Description:** Create a new Account record in Salesforce.

    **Parameters:**

    * `Name` (string, required): The Account name - This field is required
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

  <Accordion title="salesforce/create_record_any">
    **Description:** Create a record of any object type in Salesforce.

    **Note:** This is a flexible tool for creating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Updates**

<AccordionGroup>
  <Accordion title="salesforce/update_record_contact">
    **Description:** Update an existing Contact record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

  <Accordion title="salesforce/update_record_lead">
    **Description:** Update an existing Lead record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `Company` (string, optional): Company name
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact
    * `Status` (string, optional): Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

  <Accordion title="salesforce/update_record_opportunity">
    **Description:** Update an existing Opportunity record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Opportunity name
    * `StageName` (string, optional): Opportunity Stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

  <Accordion title="salesforce/update_record_task">
    **Description:** Update an existing Task record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, optional): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

  <Accordion title="salesforce/update_record_account">
    **Description:** Update an existing Account record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Account name
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

  <Accordion title="salesforce/update_record_any">
    **Description:** Update a record of any object type in Salesforce.

    **Note:** This is a flexible tool for updating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_id_contact">
    **Description:** Get a Contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Contact
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_lead">
    **Description:** Get a Lead record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Lead
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_opportunity">
    **Description:** Get an Opportunity record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Opportunity
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_task">
    **Description:** Get a Task record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Task
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_account">
    **Description:** Get an Account record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Account
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_any">
    **Description:** Get a record of any object type by its ID.

    **Parameters:**

    * `recordType` (string, required): Record Type (e.g., "CustomObject\_\_c")
    * `recordId` (string, required): Record ID
  </Accordion>
</AccordionGroup>

### **Record Search**

<AccordionGroup>
  <Accordion title="salesforce/search_records_contact">
    **Description:** Search for Contact records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_lead">
    **Description:** Search for Lead records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_opportunity">
    **Description:** Search for Opportunity records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_task">
    **Description:** Search for Task records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_account">
    **Description:** Search for Account records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_any">
    **Description:** Search for records of any object type.

    **Parameters:**

    * `recordType` (string, required): Record Type to search
    * `filterFormula` (string, optional): Filter search criteria
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **List View Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_view_id_contact">
    **Description:** Get Contact records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_lead">
    **Description:** Get Lead records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_opportunity">
    **Description:** Get Opportunity records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_task">
    **Description:** Get Task records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_account">
    **Description:** Get Account records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_any">
    **Description:** Get records of any object type from a specific List View.

    **Parameters:**

    * `recordType` (string, required): Record Type
    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **Custom Fields**

<AccordionGroup>
  <Accordion title="salesforce/create_custom_field_contact">
    **Description:** Deploy custom fields for Contact objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_lead">
    **Description:** Deploy custom fields for Lead objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_opportunity">
    **Description:** Deploy custom fields for Opportunity objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_task">
    **Description:** Deploy custom fields for Task objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_account">
    **Description:** Deploy custom fields for Account objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_any">
    **Description:** Deploy custom fields for any object type.

    **Note:** This is a flexible tool for creating custom fields on custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Advanced Operations**

<AccordionGroup>
  <Accordion title="salesforce/write_soql_query">
    **Description:** Execute custom SOQL queries against your Salesforce data.

    **Parameters:**

    * `query` (string, required): SOQL Query (e.g., "SELECT Id, Name FROM Account WHERE Name = 'Example'")
  </Accordion>

  <Accordion title="salesforce/create_custom_object">
    **Description:** Deploy a new custom object in Salesforce.

    **Parameters:**

    * `label` (string, required): Object Label for tabs, page layouts, and reports
    * `pluralLabel` (string, required): Plural Label (e.g., "Accounts")
    * `description` (string, optional): A description of the Custom Object
    * `recordName` (string, required): Record Name that appears in layouts and searches (e.g., "Account Name")
  </Accordion>

  <Accordion title="salesforce/describe_action_schema">
    **Description:** Get the expected schema for operations on specific object types.

    **Parameters:**

    * `recordType` (string, required): Record Type to describe
    * `operation` (string, required): Operation Type (e.g., "CREATE\_RECORD" or "UPDATE\_RECORD")

    **Note:** Use this function first when working with custom objects to understand their schema before performing operations.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Salesforce Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Salesforce capabilities
salesforce_agent = Agent(
    role="CRM Manager",
    goal="Manage customer relationships and sales processes efficiently",
    backstory="An AI assistant specialized in CRM operations and sales automation.",
    apps=['salesforce']  # All Salesforce actions will be available
)


# Task to create a new lead
create_lead_task = Task(
    description="Create a new lead for John Doe from Example Corp with email john.doe@example.com",
    agent=salesforce_agent,
    expected_output="Lead created successfully with lead ID"
)


# Run the task
crew = Crew(
    agents=[salesforce_agent],
    tasks=[create_lead_task]
)

crew.kickoff()
```

### Filtering Specific Salesforce Tools

```python  theme={null}

sales_manager = Agent(
    role="Sales Manager",
    goal="Manage leads and opportunities in the sales pipeline",
    backstory="An experienced sales manager who handles lead qualification and opportunity management.",
    apps=['salesforce/create_record_lead']
)


# Task to manage sales pipeline
pipeline_task = Task(
    description="Create a qualified lead and convert it to an opportunity with $50,000 value",
    agent=sales_manager,
    expected_output="Lead created and opportunity established successfully"
)

crew = Crew(
    agents=[sales_manager],
    tasks=[pipeline_task]
)

crew.kickoff()
```

### Contact and Account Management

```python  theme={null}
from crewai import Agent, Task, Crew

account_manager = Agent(
    role="Account Manager",
    goal="Manage customer accounts and maintain strong relationships",
    backstory="An AI assistant that specializes in account management and customer relationship building.",
    apps=['salesforce']
)


# Task to manage customer accounts
account_task = Task(
    description="""
    1. Create a new account for TechCorp Inc.
    2. Add John Doe as the primary contact for this account
    3. Create a follow-up task for next week to check on their project status
    """,
    agent=account_manager,
    expected_output="Account, contact, and follow-up task created successfully"
)

crew = Crew(
    agents=[account_manager],
    tasks=[account_task]
)

crew.kickoff()
```

### Advanced SOQL Queries and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Sales Data Analyst",
    goal="Generate insights from Salesforce data using SOQL queries",
    backstory="An analytical AI that excels at extracting meaningful insights from CRM data.",
    apps=['salesforce']
)


# Complex task involving SOQL queries and data analysis
analysis_task = Task(
    description="""
    1. Execute a SOQL query to find all opportunities closing this quarter
    2. Search for contacts at companies with opportunities over $100K
    3. Create a summary report of the sales pipeline status
    4. Update high-value opportunities with next steps
    """,
    agent=data_analyst,
    expected_output="Comprehensive sales pipeline analysis with actionable insights"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

This comprehensive documentation covers all the Salesforce tools organized by functionality, making it easy for users to find the specific operations they need for their CRM automation tasks.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Salesforce integration setup or troubleshooting.
</Card>



# Shopify Integration
Source: https://docs.crewai.com/en/enterprise/integrations/shopify

E-commerce and online store management with Shopify integration for CrewAI.


## Overview

Enable your agents to manage e-commerce operations through Shopify. Handle customers, orders, products, inventory, and store analytics to streamline your online business with AI-powered automation.


## Prerequisites

Before using the Shopify integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Shopify store with appropriate admin permissions
* Connected your Shopify store through the [Integrations page](https://app.crewai.com/integrations)


## Setting Up Shopify Integration

### 1. Connect Your Shopify Store

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Shopify** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for store and product management
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


## Available Tools

### **Customer Management**

<AccordionGroup>
  <Accordion title="shopify/get_customers">
    **Description:** Retrieve a list of customers from your Shopify store.

    **Parameters:**

    * `customerIds` (string, optional): Comma-separated list of customer IDs to filter by (example: "207119551, 207119552")
    * `createdAtMin` (string, optional): Only return customers created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return customers created before this date (ISO or Unix timestamp)
    * `updatedAtMin` (string, optional): Only return customers updated after this date (ISO or Unix timestamp)
    * `updatedAtMax` (string, optional): Only return customers updated before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of customers to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/search_customers">
    **Description:** Search for customers using advanced filtering criteria.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `limit` (string, optional): Maximum number of customers to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/create_customer">
    **Description:** Create a new customer in your Shopify store.

    **Parameters:**

    * `firstName` (string, required): Customer's first name
    * `lastName` (string, required): Customer's last name
    * `email` (string, required): Customer's email address
    * `company` (string, optional): Company name
    * `streetAddressLine1` (string, optional): Street address
    * `streetAddressLine2` (string, optional): Street address line 2
    * `city` (string, optional): City
    * `state` (string, optional): State or province code
    * `country` (string, optional): Country
    * `zipCode` (string, optional): Zip code
    * `phone` (string, optional): Phone number
    * `tags` (string, optional): Tags as array or comma-separated list
    * `note` (string, optional): Customer note
    * `sendEmailInvite` (boolean, optional): Whether to send email invitation
    * `metafields` (object, optional): Additional metafields in JSON format
  </Accordion>

  <Accordion title="shopify/update_customer">
    **Description:** Update an existing customer in your Shopify store.

    **Parameters:**

    * `customerId` (string, required): The ID of the customer to update
    * `firstName` (string, optional): Customer's first name
    * `lastName` (string, optional): Customer's last name
    * `email` (string, optional): Customer's email address
    * `company` (string, optional): Company name
    * `streetAddressLine1` (string, optional): Street address
    * `streetAddressLine2` (string, optional): Street address line 2
    * `city` (string, optional): City
    * `state` (string, optional): State or province code
    * `country` (string, optional): Country
    * `zipCode` (string, optional): Zip code
    * `phone` (string, optional): Phone number
    * `tags` (string, optional): Tags as array or comma-separated list
    * `note` (string, optional): Customer note
    * `sendEmailInvite` (boolean, optional): Whether to send email invitation
    * `metafields` (object, optional): Additional metafields in JSON format
  </Accordion>
</AccordionGroup>

### **Order Management**

<AccordionGroup>
  <Accordion title="shopify/get_orders">
    **Description:** Retrieve a list of orders from your Shopify store.

    **Parameters:**

    * `orderIds` (string, optional): Comma-separated list of order IDs to filter by (example: "450789469, 450789470")
    * `createdAtMin` (string, optional): Only return orders created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return orders created before this date (ISO or Unix timestamp)
    * `updatedAtMin` (string, optional): Only return orders updated after this date (ISO or Unix timestamp)
    * `updatedAtMax` (string, optional): Only return orders updated before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of orders to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/create_order">
    **Description:** Create a new order in your Shopify store.

    **Parameters:**

    * `email` (string, required): Customer email address
    * `lineItems` (object, required): Order line items in JSON format with title, price, quantity, and variant\_id
    * `sendReceipt` (boolean, optional): Whether to send order receipt
    * `fulfillmentStatus` (string, optional): Fulfillment status - Options: fulfilled, null, partial, restocked
    * `financialStatus` (string, optional): Financial status - Options: pending, authorized, partially\_paid, paid, partially\_refunded, refunded, voided
    * `inventoryBehaviour` (string, optional): Inventory behavior - Options: bypass, decrement\_ignoring\_policy, decrement\_obeying\_policy
    * `note` (string, optional): Order note
  </Accordion>

  <Accordion title="shopify/update_order">
    **Description:** Update an existing order in your Shopify store.

    **Parameters:**

    * `orderId` (string, required): The ID of the order to update
    * `email` (string, optional): Customer email address
    * `lineItems` (object, optional): Updated order line items in JSON format
    * `sendReceipt` (boolean, optional): Whether to send order receipt
    * `fulfillmentStatus` (string, optional): Fulfillment status - Options: fulfilled, null, partial, restocked
    * `financialStatus` (string, optional): Financial status - Options: pending, authorized, partially\_paid, paid, partially\_refunded, refunded, voided
    * `inventoryBehaviour` (string, optional): Inventory behavior - Options: bypass, decrement\_ignoring\_policy, decrement\_obeying\_policy
    * `note` (string, optional): Order note
  </Accordion>

  <Accordion title="shopify/get_abandoned_carts">
    **Description:** Retrieve abandoned carts from your Shopify store.

    **Parameters:**

    * `createdWithInLast` (string, optional): Restrict results to checkouts created within specified time
    * `createdAfterId` (string, optional): Restrict results to after the specified ID
    * `status` (string, optional): Show checkouts with given status - Options: open, closed (defaults to open)
    * `createdAtMin` (string, optional): Only return carts created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return carts created before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of carts to return (defaults to 250)
  </Accordion>
</AccordionGroup>

### **Product Management (REST API)**

<AccordionGroup>
  <Accordion title="shopify/get_products">
    **Description:** Retrieve a list of products from your Shopify store using REST API.

    **Parameters:**

    * `productIds` (string, optional): Comma-separated list of product IDs to filter by (example: "632910392, 632910393")
    * `title` (string, optional): Filter by product title
    * `productType` (string, optional): Filter by product type
    * `vendor` (string, optional): Filter by vendor
    * `status` (string, optional): Filter by status - Options: active, archived, draft
    * `createdAtMin` (string, optional): Only return products created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return products created before this date (ISO or Unix timestamp)
    * `updatedAtMin` (string, optional): Only return products updated after this date (ISO or Unix timestamp)
    * `updatedAtMax` (string, optional): Only return products updated before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of products to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/create_product">
    **Description:** Create a new product in your Shopify store using REST API.

    **Parameters:**

    * `title` (string, required): Product title
    * `productType` (string, required): Product type/category
    * `vendor` (string, required): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `price` (string, optional): Product price
    * `inventoryPolicy` (string, optional): Inventory policy - Options: deny, continue
    * `imageUrl` (string, optional): Product image URL
    * `isPublished` (boolean, optional): Whether product is published
    * `publishToPointToSale` (boolean, optional): Whether to publish to point of sale
  </Accordion>

  <Accordion title="shopify/update_product">
    **Description:** Update an existing product in your Shopify store using REST API.

    **Parameters:**

    * `productId` (string, required): The ID of the product to update
    * `title` (string, optional): Product title
    * `productType` (string, optional): Product type/category
    * `vendor` (string, optional): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `price` (string, optional): Product price
    * `inventoryPolicy` (string, optional): Inventory policy - Options: deny, continue
    * `imageUrl` (string, optional): Product image URL
    * `isPublished` (boolean, optional): Whether product is published
    * `publishToPointToSale` (boolean, optional): Whether to publish to point of sale
  </Accordion>
</AccordionGroup>

### **Product Management (GraphQL)**

<AccordionGroup>
  <Accordion title="shopify/get_products_graphql">
    **Description:** Retrieve products using advanced GraphQL filtering capabilities.

    **Parameters:**

    * `productFilterFormula` (object, optional): Advanced filter in disjunctive normal form with support for fields like id, title, vendor, status, handle, tag, created\_at, updated\_at, published\_at
  </Accordion>

  <Accordion title="shopify/create_product_graphql">
    **Description:** Create a new product using GraphQL API with enhanced media support.

    **Parameters:**

    * `title` (string, required): Product title
    * `productType` (string, required): Product type/category
    * `vendor` (string, required): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `media` (object, optional): Media objects with alt text, content type, and source URL
    * `additionalFields` (object, optional): Additional product fields like status, requiresSellingPlan, giftCard
  </Accordion>

  <Accordion title="shopify/update_product_graphql">
    **Description:** Update an existing product using GraphQL API with enhanced media support.

    **Parameters:**

    * `productId` (string, required): The GraphQL ID of the product to update (e.g., "gid://shopify/Product/913144112")
    * `title` (string, optional): Product title
    * `productType` (string, optional): Product type/category
    * `vendor` (string, optional): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `media` (object, optional): Updated media objects with alt text, content type, and source URL
    * `additionalFields` (object, optional): Additional product fields like status, requiresSellingPlan, giftCard
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Shopify Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Shopify capabilities
shopify_agent = Agent(
    role="E-commerce Manager",
    goal="Manage online store operations and customer relationships efficiently",
    backstory="An AI assistant specialized in e-commerce operations and online store management.",
    apps=['shopify']  # All Shopify actions will be available
)


# Task to create a new customer
create_customer_task = Task(
    description="Create a new VIP customer Jane Smith with email jane.smith@example.com and phone +1-555-0123",
    agent=shopify_agent,
    expected_output="Customer created successfully with customer ID"
)


# Run the task
crew = Crew(
    agents=[shopify_agent],
    tasks=[create_customer_task]
)

crew.kickoff()
```

### Filtering Specific Shopify Tools

```python  theme={null}

store_manager = Agent(
    role="Store Manager",
    goal="Manage customer orders and product catalog",
    backstory="An experienced store manager who handles customer relationships and inventory management.",
    apps=['shopify/create_customer']
)


# Task to manage store operations
store_task = Task(
    description="Create a new customer and process their order for 2 Premium Coffee Mugs",
    agent=store_manager,
    expected_output="Customer created and order processed successfully"
)

crew = Crew(
    agents=[store_manager],
    tasks=[store_task]
)

crew.kickoff()
```

### Product Management with GraphQL

```python  theme={null}
from crewai import Agent, Task, Crew

product_manager = Agent(
    role="Product Manager",
    goal="Manage product catalog and inventory with advanced GraphQL capabilities",
    backstory="An AI assistant that specializes in product management and catalog optimization.",
    apps=['shopify']
)


# Task to manage product catalog
catalog_task = Task(
    description="""
    1. Create a new product "Premium Coffee Mug" from Coffee Co vendor
    2. Add high-quality product images and descriptions
    3. Search for similar products from the same vendor
    4. Update product tags and pricing strategy
    """,
    agent=product_manager,
    expected_output="Product created and catalog optimized successfully"
)

crew = Crew(
    agents=[product_manager],
    tasks=[catalog_task]
)

crew.kickoff()
```

### Order and Customer Analytics

```python  theme={null}
from crewai import Agent, Task, Crew

analytics_agent = Agent(
    role="E-commerce Analyst",
    goal="Analyze customer behavior and order patterns to optimize store performance",
    backstory="An analytical AI that excels at extracting insights from e-commerce data.",
    apps=['shopify']
)


# Complex task involving multiple operations
analytics_task = Task(
    description="""
    1. Retrieve recent customer data and order history
    2. Identify abandoned carts from the last 7 days
    3. Analyze product performance and inventory levels
    4. Generate recommendations for customer retention
    """,
    agent=analytics_agent,
    expected_output="Comprehensive e-commerce analytics report with actionable insights"
)

crew = Crew(
    agents=[analytics_agent],
    tasks=[analytics_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Shopify integration setup or troubleshooting.
</Card>



# Slack Integration
Source: https://docs.crewai.com/en/enterprise/integrations/slack

Team communication and collaboration with Slack integration for CrewAI.


## Overview

Enable your agents to manage team communication through Slack. Send messages, search conversations, manage channels, and coordinate team activities to streamline your collaboration workflows with AI-powered automation.


## Prerequisites

Before using the Slack integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Slack workspace with appropriate permissions
* Connected your Slack workspace through the [Integrations page](https://app.crewai.com/integrations)


## Setting Up Slack Integration

### 1. Connect Your Slack Workspace

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Slack** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for team communication
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


## Available Tools

### **User Management**

<AccordionGroup>
  <Accordion title="slack/list_members">
    **Description:** List all members in a Slack channel.

    **Parameters:**

    * No parameters required - retrieves all channel members
  </Accordion>

  <Accordion title="slack/get_user_by_email">
    **Description:** Find a user in your Slack workspace by their email address.

    **Parameters:**

    * `email` (string, required): The email address of a user in the workspace
  </Accordion>

  <Accordion title="slack/get_users_by_name">
    **Description:** Search for users by their name or display name.

    **Parameters:**

    * `name` (string, required): User's real name to search for
    * `displayName` (string, required): User's display name to search for
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

### **Channel Management**

<AccordionGroup>
  <Accordion title="slack/list_channels">
    **Description:** List all channels in your Slack workspace.

    **Parameters:**

    * No parameters required - retrieves all accessible channels
  </Accordion>
</AccordionGroup>

### **Messaging**

<AccordionGroup>
  <Accordion title="slack/send_message">
    **Description:** Send a message to a Slack channel.

    **Parameters:**

    * `channel` (string, required): Channel name or ID - Use Connect Portal Workflow Settings to allow users to select a channel, or enter a channel name to create a new channel
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>

  <Accordion title="slack/send_direct_message">
    **Description:** Send a direct message to a specific user in Slack.

    **Parameters:**

    * `memberId` (string, required): Recipient user ID - Use Connect Portal Workflow Settings to allow users to select a workspace member
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>
</AccordionGroup>

### **Search & Discovery**

<AccordionGroup>
  <Accordion title="slack/search_messages">
    **Description:** Search for messages across your Slack workspace.

    **Parameters:**

    * `query` (string, required): Search query using Slack search syntax to find messages that match specified criteria

    **Search Query Examples:**

    * `"project update"` - Search for messages containing "project update"
    * `from:@john in:#general` - Search for messages from John in the #general channel
    * `has:link after:2023-01-01` - Search for messages with links after January 1, 2023
    * `in:@channel before:yesterday` - Search for messages in a specific channel before yesterday
  </Accordion>
</AccordionGroup>


## Block Kit Integration

Slack's Block Kit allows you to create rich, interactive messages. Here are some examples of how to use the `blocks` parameter:

### Simple Text with Attachment

```json  theme={null}
[
  {
    "text": "I am a test message",
    "attachments": [
      {
        "text": "And here's an attachment!"
      }
    ]
  }
]
```

### Rich Formatting with Sections

```json  theme={null}
[
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Project Update*\nStatus: ✅ Complete"
    }
  },
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "plain_text",
      "text": "All tasks have been completed successfully."
    }
  }
]
```


## Usage Examples

### Basic Slack Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


# Create an agent with Slack capabilities
slack_agent = Agent(
    role="Team Communication Manager",
    goal="Facilitate team communication and coordinate collaboration efficiently",
    backstory="An AI assistant specialized in team communication and workspace coordination.",
    apps=['slack']  # All Slack actions will be available
)


# Task to send project updates
update_task = Task(
    description="Send a project status update to the #general channel with current progress",
    agent=slack_agent,
    expected_output="Project update message sent successfully to team channel"
)


# Run the task
crew = Crew(
    agents=[slack_agent],
    tasks=[update_task]
)

crew.kickoff()
```

### Filtering Specific Slack Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Slack actions only
communication_manager = Agent(
    role="Communication Coordinator",
    goal="Manage team communications and ensure important messages reach the right people",
    backstory="An experienced communication coordinator who handles team messaging and notifications.",
    apps=[
        'slack/send_message',
        'slack/send_direct_message',
        'slack/search_messages'
    ]  # Using canonical action names from canonical_integrations.yml
)


# Task to coordinate team communication
coordination_task = Task(
    description="Send task completion notifications to team members and update project channels",
    agent=communication_manager,
    expected_output="Team notifications sent and project channels updated successfully"
)

crew = Crew(
    agents=[communication_manager],
    tasks=[coordination_task]
)

crew.kickoff()
```

### Advanced Messaging with Block Kit

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with Slack messaging capabilities
notification_agent = Agent(
    role="Notification Manager",
    goal="Create rich, interactive notifications and manage workspace communication",
    backstory="An AI assistant that specializes in creating engaging team notifications and updates.",
    apps=['slack/send_message']  # Specific action for sending messages
)


# Task to send rich notifications
notification_task = Task(
    description="""
    1. Send a formatted project completion message to #general with progress charts
    2. Send direct messages to team leads with task summaries
    3. Create interactive notification with action buttons for team feedback
    """,
    agent=notification_agent,
    expected_output="Rich notifications sent with interactive elements and formatted content"
)

crew = Crew(
    agents=[notification_agent],
    tasks=[notification_task]
)

crew.kickoff()
```

### Message Search and Analytics

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with Slack search and user management capabilities
analytics_agent = Agent(
    role="Communication Analyst",
    goal="Analyze team communication patterns and extract insights from conversations",
    backstory="An analytical AI that excels at understanding team dynamics through communication data.",
    apps=[
        'slack/search_messages',
        'slack/get_user_by_email',
        'slack/list_members'
    ]  # Using canonical action names from canonical_integrations.yml
)


# Complex task involving search and analysis
analysis_task = Task(
    description="""
    1. Search for recent project-related messages across all channels
    2. Find users by email to identify team members
    3. Analyze communication patterns and response times
    4. Generate weekly team communication summary
    """,
    agent=analytics_agent,
    expected_output="Comprehensive communication analysis with team insights and recommendations"
)

crew = Crew(
    agents=[analytics_agent],
    tasks=[analysis_task]
)

crew.kickoff()
```


## Contact Support

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Slack integration setup or troubleshooting.
</Card>



# Stripe Integration
Source: https://docs.crewai.com/en/enterprise/integrations/stripe

Payment processing and subscription management with Stripe integration for CrewAI.


## Overview

Enable your agents to manage payments, subscriptions, and customer billing through Stripe. Handle customer data, process subscriptions, manage products, and track financial transactions to streamline your payment workflows with AI-powered automation.


## Prerequisites

Before using the Stripe integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Stripe account with appropriate API permissions
* Connected your Stripe account through the [Integrations page](https://app.crewai.com/integrations)


## Setting Up Stripe Integration

### 1. Connect Your Stripe Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Stripe** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for payment processing
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


## Available Tools

### **Customer Management**

<AccordionGroup>
  <Accordion title="stripe/create_customer">
    **Description:** Create a new customer in your Stripe account.

    **Parameters:**

    * `emailCreateCustomer` (string, required): Customer's email address
    * `name` (string, optional): Customer's full name
    * `description` (string, optional): Customer description for internal reference
    * `metadataCreateCustomer` (object, optional): Additional metadata as key-value pairs (e.g., `{"field1": 1, "field2": 2}`)
  </Accordion>

  <Accordion title="stripe/get_customer_by_id">
    **Description:** Retrieve a specific customer by their Stripe customer ID.

    **Parameters:**

    * `idGetCustomer` (string, required): The Stripe customer ID to retrieve
  </Accordion>

  <Accordion title="stripe/get_customers">
    **Description:** Retrieve a list of customers with optional filtering.

    **Parameters:**

    * `emailGetCustomers` (string, optional): Filter customers by email address
    * `createdAfter` (string, optional): Filter customers created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter customers created before this date (Unix timestamp)
    * `limitGetCustomers` (string, optional): Maximum number of customers to return (defaults to 10)
  </Accordion>

  <Accordion title="stripe/update_customer">
    **Description:** Update an existing customer's information.

    **Parameters:**

    * `customerId` (string, required): The ID of the customer to update
    * `emailUpdateCustomer` (string, optional): Updated email address
    * `name` (string, optional): Updated customer name
    * `description` (string, optional): Updated customer description
    * `metadataUpdateCustomer` (object, optional): Updated metadata as key-value pairs
  </Accordion>
</AccordionGroup>

### **Subscription Management**

<AccordionGroup>
  <Accordion title="stripe/create_subscription">
    **Description:** Create a new subscription for a customer.

    **Parameters:**

    * `customerIdCreateSubscription` (string, required): The customer ID for whom the subscription will be created
    * `plan` (string, required): The plan ID for the subscription - Use Connect Portal Workflow Settings to allow users to select a plan
    * `metadataCreateSubscription` (object, optional): Additional metadata for the subscription
  </Accordion>

  <Accordion title="stripe/get_subscriptions">
    **Description:** Retrieve subscriptions with optional filtering.

    **Parameters:**

    * `customerIdGetSubscriptions` (string, optional): Filter subscriptions by customer ID
    * `subscriptionStatus` (string, optional): Filter by subscription status - Options: incomplete, incomplete\_expired, trialing, active, past\_due, canceled, unpaid
    * `limitGetSubscriptions` (string, optional): Maximum number of subscriptions to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Product Management**

<AccordionGroup>
  <Accordion title="stripe/create_product">
    **Description:** Create a new product in your Stripe catalog.

    **Parameters:**

    * `productName` (string, required): The product name
    * `description` (string, optional): Product description
    * `metadataProduct` (object, optional): Additional product metadata as key-value pairs
  </Accordion>

  <Accordion title="stripe/get_product_by_id">
    **Description:** Retrieve a specific product by its Stripe product ID.

    **Parameters:**

    * `productId` (string, required): The Stripe product ID to retrieve
  </Accordion>

  <Accordion title="stripe/get_products">
    **Description:** Retrieve a list of products with optional filtering.

    **Parameters:**

    * `createdAfter` (string, optional): Filter products created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter products created before this date (Unix timestamp)
    * `limitGetProducts` (string, optional): Maximum number of products to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Financial Operations**

<AccordionGroup>
  <Accordion title="stripe/get_balance_transactions">
    **Description:** Retrieve balance transactions from your Stripe account.

    **Parameters:**

    * `balanceTransactionType` (string, optional): Filter by transaction type - Options: charge, refund, payment, payment\_refund
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

  <Accordion title="stripe/get_plans">
    **Description:** Retrieve subscription plans from your Stripe account.

    **Parameters:**

    * `isPlanActive` (boolean, optional): Filter by plan status - true for active plans, false for inactive plans
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Stripe Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


---

**Navigation:** [← Previous](./08-create-an-agent-with-asana-capabilities.md) | [Index](./index.md) | [Next →](./10-create-an-agent-with-stripe-capabilities.md)
