# Create an agent with Stripe capabilities

**Navigation:** [← Previous](./09-task-using-schema-based-operations.md) | [Index](./index.md) | [Next →](./11-replay-tasks-from-latest-crew-kickoff.md)

---

# Create an agent with Stripe capabilities
stripe_agent = Agent(
    role="Payment Manager",
    goal="Manage customer payments, subscriptions, and billing operations efficiently",
    backstory="An AI assistant specialized in payment processing and subscription management.",
    apps=['stripe']  # All Stripe actions will be available
)


# Task to create a new customer
create_customer_task = Task(
    description="Create a new premium customer John Doe with email john.doe@example.com",
    agent=stripe_agent,
    expected_output="Customer created successfully with customer ID"
)


# Run the task
crew = Crew(
    agents=[stripe_agent],
    tasks=[create_customer_task]
)

crew.kickoff()
```

### Filtering Specific Stripe Tools

```python  theme={null}

billing_manager = Agent(
    role="Billing Manager",
    goal="Handle customer billing, subscriptions, and payment processing",
    backstory="An experienced billing manager who handles subscription lifecycle and payment operations.",
    apps=['stripe']
)


# Task to manage billing operations
billing_task = Task(
    description="Create a new customer and set up their premium subscription plan",
    agent=billing_manager,
    expected_output="Customer created and subscription activated successfully"
)

crew = Crew(
    agents=[billing_manager],
    tasks=[billing_task]
)

crew.kickoff()
```

### Subscription Management

```python  theme={null}
from crewai import Agent, Task, Crew

subscription_manager = Agent(
    role="Subscription Manager",
    goal="Manage customer subscriptions and optimize recurring revenue",
    backstory="An AI assistant that specializes in subscription lifecycle management and customer retention.",
    apps=['stripe']
)


# Task to manage subscription operations
subscription_task = Task(
    description="""
    1. Create a new product "Premium Service Plan" with advanced features
    2. Set up subscription plans with different tiers
    3. Create customers and assign them to appropriate plans
    4. Monitor subscription status and handle billing issues
    """,
    agent=subscription_manager,
    expected_output="Subscription management system configured with customers and active plans"
)

crew = Crew(
    agents=[subscription_manager],
    tasks=[subscription_task]
)

crew.kickoff()
```

### Financial Analytics and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze payment data and generate financial insights",
    backstory="An analytical AI that excels at extracting insights from payment and subscription data.",
    apps=['stripe']
)


# Complex task involving financial analysis
analytics_task = Task(
    description="""
    1. Retrieve balance transactions for the current month
    2. Analyze customer payment patterns and subscription trends
    3. Identify high-value customers and subscription performance
    4. Generate monthly financial performance report
    """,
    agent=financial_analyst,
    expected_output="Comprehensive financial analysis with payment insights and recommendations"
)

crew = Crew(
    agents=[financial_analyst],
    tasks=[analytics_task]
)

crew.kickoff()
```


## Subscription Status Reference

Understanding subscription statuses:

* **incomplete** - Subscription requires payment method or payment confirmation
* **incomplete\_expired** - Subscription expired before payment was confirmed
* **trialing** - Subscription is in trial period
* **active** - Subscription is active and current
* **past\_due** - Payment failed but subscription is still active
* **canceled** - Subscription has been canceled
* **unpaid** - Payment failed and subscription is no longer active


## Metadata Usage

Metadata allows you to store additional information about customers, subscriptions, and products:

```json  theme={null}
{
  "customer_segment": "enterprise",
  "acquisition_source": "google_ads",
  "lifetime_value": "high",
  "custom_field_1": "value1"
}
```

This integration enables comprehensive payment and subscription management automation, allowing your AI agents to handle billing operations seamlessly within your Stripe ecosystem.



# Zendesk Integration
Source: https://docs.crewai.com/en/enterprise/integrations/zendesk

Customer support and helpdesk management with Zendesk integration for CrewAI.


## Overview

Enable your agents to manage customer support operations through Zendesk. Create and update tickets, manage users, track support metrics, and streamline your customer service workflows with AI-powered automation.


## Prerequisites

Before using the Zendesk integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* A Zendesk account with appropriate API permissions
* Connected your Zendesk account through the [Integrations page](https://app.crewai.com/integrations)


## Setting Up Zendesk Integration

### 1. Connect Your Zendesk Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Zendesk** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for ticket and user management
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

### **Ticket Management**

<AccordionGroup>
  <Accordion title="zendesk/create_ticket">
    **Description:** Create a new support ticket in Zendesk.

    **Parameters:**

    * `ticketSubject` (string, required): Ticket subject line (e.g., "Help, my printer is on fire!")
    * `ticketDescription` (string, required): First comment that appears on the ticket (e.g., "The smoke is very colorful.")
    * `requesterName` (string, required): Name of the user requesting support (e.g., "Jane Customer")
    * `requesterEmail` (string, required): Email of the user requesting support (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `assigneeId` (string, optional): Zendesk Agent ID assigned to this ticket - Use Connect Portal Workflow Settings to allow users to select an assignee
    * `ticketType` (string, optional): Ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Priority level - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Ticket status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Due date for task-type tickets (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Array of tags to apply (e.g., `["enterprise", "other_tag"]`)
    * `ticketExternalId` (string, optional): External ID to link tickets to local records
    * `ticketCustomFields` (object, optional): Custom field values in JSON format
  </Accordion>

  <Accordion title="zendesk/update_ticket">
    **Description:** Update an existing support ticket in Zendesk.

    **Parameters:**

    * `ticketId` (string, required): ID of the ticket to update (e.g., "35436")
    * `ticketSubject` (string, optional): Updated ticket subject
    * `requesterName` (string, required): Name of the user who requested this ticket
    * `requesterEmail` (string, required): Email of the user who requested this ticket
    * `assigneeId` (string, optional): Updated assignee ID - Use Connect Portal Workflow Settings
    * `ticketType` (string, optional): Updated ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Updated priority - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Updated status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Updated due date (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Updated tags array
    * `ticketExternalId` (string, optional): Updated external ID
    * `ticketCustomFields` (object, optional): Updated custom field values
  </Accordion>

  <Accordion title="zendesk/get_ticket_by_id">
    **Description:** Retrieve a specific ticket by its ID.

    **Parameters:**

    * `ticketId` (string, required): The ticket ID to retrieve (e.g., "35436")
  </Accordion>

  <Accordion title="zendesk/add_comment_to_ticket">
    **Description:** Add a comment or internal note to an existing ticket.

    **Parameters:**

    * `ticketId` (string, required): ID of the ticket to add comment to (e.g., "35436")
    * `commentBody` (string, required): Comment message (accepts plain text or HTML, e.g., "Thanks for your help!")
    * `isInternalNote` (boolean, optional): Set to true for internal notes instead of public replies (defaults to false)
    * `isPublic` (boolean, optional): True for public comments, false for internal notes
  </Accordion>

  <Accordion title="zendesk/search_tickets">
    **Description:** Search for tickets using various filters and criteria.

    **Parameters:**

    * `ticketSubject` (string, optional): Filter by text in ticket subject
    * `ticketDescription` (string, optional): Filter by text in ticket description and comments
    * `ticketStatus` (string, optional): Filter by status - Options: new, open, pending, hold, solved, closed
    * `ticketType` (string, optional): Filter by type - Options: problem, incident, question, task, no\_type
    * `ticketPriority` (string, optional): Filter by priority - Options: urgent, high, normal, low, no\_priority
    * `requesterId` (string, optional): Filter by requester user ID
    * `assigneeId` (string, optional): Filter by assigned agent ID
    * `recipientEmail` (string, optional): Filter by original recipient email address
    * `ticketTags` (string, optional): Filter by ticket tags
    * `ticketExternalId` (string, optional): Filter by external ID
    * `createdDate` (object, optional): Filter by creation date with operator (EQUALS, LESS\_THAN\_EQUALS, GREATER\_THAN\_EQUALS) and value
    * `updatedDate` (object, optional): Filter by update date with operator and value
    * `dueDate` (object, optional): Filter by due date with operator and value
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at, priority, status, ticket\_type
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **User Management**

<AccordionGroup>
  <Accordion title="zendesk/create_user">
    **Description:** Create a new user in Zendesk.

    **Parameters:**

    * `name` (string, required): User's full name
    * `email` (string, optional): User's email address (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `phone` (string, optional): User's phone number
    * `role` (string, optional): User role - Options: admin, agent, end-user
    * `externalId` (string, optional): Unique identifier from another system
    * `details` (string, optional): Additional user details
    * `notes` (string, optional): Internal notes about the user
  </Accordion>

  <Accordion title="zendesk/update_user">
    **Description:** Update an existing user's information.

    **Parameters:**

    * `userId` (string, required): ID of the user to update
    * `name` (string, optional): Updated user name
    * `email` (string, optional): Updated email (adds as secondary email on update)
    * `phone` (string, optional): Updated phone number
    * `role` (string, optional): Updated role - Options: admin, agent, end-user
    * `externalId` (string, optional): Updated external ID
    * `details` (string, optional): Updated user details
    * `notes` (string, optional): Updated internal notes
  </Accordion>

  <Accordion title="zendesk/get_user_by_id">
    **Description:** Retrieve a specific user by their ID.

    **Parameters:**

    * `userId` (string, required): The user ID to retrieve
  </Accordion>

  <Accordion title="zendesk/search_users">
    **Description:** Search for users using various criteria.

    **Parameters:**

    * `name` (string, optional): Filter by user name
    * `email` (string, optional): Filter by user email (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `role` (string, optional): Filter by role - Options: admin, agent, end-user
    * `externalId` (string, optional): Filter by external ID
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **Administrative Tools**

<AccordionGroup>
  <Accordion title="zendesk/get_ticket_fields">
    **Description:** Retrieve all standard and custom fields available for tickets.

    **Parameters:**

    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

  <Accordion title="zendesk/get_ticket_audits">
    **Description:** Get audit records (read-only history) for tickets.

    **Parameters:**

    * `ticketId` (string, optional): Get audits for specific ticket (if empty, retrieves audits for all non-archived tickets, e.g., "1234")
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>


## Custom Fields

Custom fields allow you to store additional information specific to your organization:

```json  theme={null}
[
  { "id": 27642, "value": "745" },
  { "id": 27648, "value": "yes" }
]
```


## Ticket Priority Levels

Understanding priority levels:

* **urgent** - Critical issues requiring immediate attention
* **high** - Important issues that should be addressed quickly
* **normal** - Standard priority for most tickets
* **low** - Minor issues that can be addressed when convenient


## Ticket Status Workflow

Standard ticket status progression:

* **new** - Recently created, not yet assigned
* **open** - Actively being worked on
* **pending** - Waiting for customer response or external action
* **hold** - Temporarily paused
* **solved** - Issue resolved, awaiting customer confirmation
* **closed** - Ticket completed and closed


## Usage Examples

### Basic Zendesk Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew


# Create an agent with Zendesk capabilities
zendesk_agent = Agent(
    role="Support Manager",
    goal="Manage customer support tickets and provide excellent customer service",
    backstory="An AI assistant specialized in customer support operations and ticket management.",
    apps=['zendesk']  # All Zendesk actions will be available
)


# Task to create a new support ticket
create_ticket_task = Task(
    description="Create a high-priority support ticket for John Smith who is unable to access his account after password reset",
    agent=zendesk_agent,
    expected_output="Support ticket created successfully with ticket ID"
)


# Run the task
crew = Crew(
    agents=[zendesk_agent],
    tasks=[create_ticket_task]
)

crew.kickoff()
```

### Filtering Specific Zendesk Tools

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with specific Zendesk actions only
support_agent = Agent(
    role="Customer Support Agent",
    goal="Handle customer inquiries and resolve support issues efficiently",
    backstory="An experienced support agent who specializes in ticket resolution and customer communication.",
    apps=['zendesk/create_ticket']  # Specific Zendesk actions
)


# Task to manage support workflow
support_task = Task(
    description="Create a ticket for login issues, add troubleshooting comments, and update status to resolved",
    agent=support_agent,
    expected_output="Support ticket managed through complete resolution workflow"
)

crew = Crew(
    agents=[support_agent],
    tasks=[support_task]
)

crew.kickoff()
```

### Advanced Ticket Management

```python  theme={null}
from crewai import Agent, Task, Crew

ticket_manager = Agent(
    role="Ticket Manager",
    goal="Manage support ticket workflows and ensure timely resolution",
    backstory="An AI assistant that specializes in support ticket triage and workflow optimization.",
    apps=['zendesk']
)


# Task to manage ticket lifecycle
ticket_workflow = Task(
    description="""
    1. Create a new support ticket for account access issues
    2. Add internal notes with troubleshooting steps
    3. Update ticket priority based on customer tier
    4. Add resolution comments and close the ticket
    """,
    agent=ticket_manager,
    expected_output="Complete ticket lifecycle managed from creation to resolution"
)

crew = Crew(
    agents=[ticket_manager],
    tasks=[ticket_workflow]
)

crew.kickoff()
```

### Support Analytics and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

support_analyst = Agent(
    role="Support Analyst",
    goal="Analyze support metrics and generate insights for team performance",
    backstory="An analytical AI that excels at extracting insights from support data and ticket patterns.",
    apps=['zendesk']
)


# Complex task involving analytics and reporting
analytics_task = Task(
    description="""
    1. Search for all open tickets from the last 30 days
    2. Analyze ticket resolution times and customer satisfaction
    3. Identify common issues and support patterns
    4. Generate weekly support performance report
    """,
    agent=support_analyst,
    expected_output="Comprehensive support analytics report with performance insights and recommendations"
)

crew = Crew(
    agents=[support_analyst],
    tasks=[analytics_task]
)

crew.kickoff()
```



# CrewAI AMP
Source: https://docs.crewai.com/en/enterprise/introduction

Deploy, monitor, and scale your AI agent workflows


## Introduction

CrewAI AMP(Agent Management Platform) provides a platform for deploying, monitoring, and scaling your crews and agents in a production environment.

<Frame>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f3c686c946a4843a9093f21c0d1a420f" alt="CrewAI AMP Dashboard" data-og-width="3648" width="3648" data-og-height="2248" height="2248" data-path="images/enterprise/crewai-enterprise-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a58dd6da8e1de0056bc26152476114c9 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3cbeb2e4972fe106a8fdf256539c965a 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c81d9773136e4d33a8853457690bc14d 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d5a21be80d159c6041ebfeb51f948b5e 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=326a6f4e11c1091dca20d98384eeb0ad 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2d799c4a99363505252df6a3553fc248 2500w" />
</Frame>

CrewAI AMP extends the power of the open-source framework with features designed for production deployments, collaboration, and scalability. Deploy your crews to a managed infrastructure and monitor their execution in real-time.


## Key Features

<CardGroup cols={2}>
  <Card title="Crew Deployments" icon="rocket">
    Deploy your crews to a managed infrastructure with a few clicks
  </Card>

  <Card title="API Access" icon="code">
    Access your deployed crews via REST API for integration with existing systems
  </Card>

  <Card title="Observability" icon="chart-line">
    Monitor your crews with detailed execution traces and logs
  </Card>

  <Card title="Tool Repository" icon="toolbox">
    Publish and install tools to enhance your crews' capabilities
  </Card>

  <Card title="Webhook Streaming" icon="webhook">
    Stream real-time events and updates to your systems
  </Card>

  <Card title="Crew Studio" icon="paintbrush">
    Create and customize crews using a no-code/low-code interface
  </Card>
</CardGroup>


## Deployment Options

<CardGroup cols={3}>
  <Card title="GitHub Integration" icon="github">
    Connect directly to your GitHub repositories to deploy code
  </Card>

  <Card title="Crew Studio" icon="palette">
    Deploy crews created through the no-code Crew Studio interface
  </Card>

  <Card title="CLI Deployment" icon="terminal">
    Use the CrewAI CLI for more advanced deployment workflows
  </Card>
</CardGroup>


## Getting Started

<Steps>
  <Step title="Sign up for an account">
    Create your account at [app.crewai.com](https://app.crewai.com)

    <Card title="Sign Up" icon="user" href="https://app.crewai.com/signup">
      Sign Up
    </Card>
  </Step>

  <Step title="Build your first crew">
    Use code or Crew Studio to build your crew

    <Card title="Build Crew" icon="paintbrush" href="/en/enterprise/guides/build-crew">
      Build Crew
    </Card>
  </Step>

  <Step title="Deploy your crew">
    Deploy your crew to the Enterprise platform

    <Card title="Deploy Crew" icon="rocket" href="/en/enterprise/guides/deploy-crew">
      Deploy Crew
    </Card>
  </Step>

  <Step title="Access your crew">
    Integrate with your crew via the generated API endpoints

    <Card title="API Access" icon="code" href="/en/enterprise/guides/kickoff-crew">
      Use the Crew API
    </Card>
  </Step>
</Steps>

For detailed instructions, check out our [deployment guide](/en/enterprise/guides/deploy-crew) or click the button below to get started.



# Coding Agents
Source: https://docs.crewai.com/en/learn/coding-agents

Learn how to enable your CrewAI Agents to write and execute code, and explore advanced features for enhanced functionality.


## Introduction

CrewAI Agents now have the powerful ability to write and execute code, significantly enhancing their problem-solving capabilities. This feature is particularly useful for tasks that require computational or programmatic solutions.


## Enabling Code Execution

To enable code execution for an agent, set the `allow_code_execution` parameter to `True` when creating the agent.

Here's an example:

```python Code theme={null}
from crewai import Agent

coding_agent = Agent(
    role="Senior Python Developer",
    goal="Craft well-designed and thought-out code",
    backstory="You are a senior Python developer with extensive experience in software architecture and best practices.",
    allow_code_execution=True
)
```

<Note>
  Note that `allow_code_execution` parameter defaults to `False`.
</Note>


## Important Considerations

1. **Model Selection**: It is strongly recommended to use more capable models like Claude 3.5 Sonnet and GPT-4 when enabling code execution.
   These models have a better understanding of programming concepts and are more likely to generate correct and efficient code.

2. **Error Handling**: The code execution feature includes error handling. If executed code raises an exception, the agent will receive the error message and can attempt to correct the code or
   provide alternative solutions. The `max_retry_limit` parameter, which defaults to 2, controls the maximum number of retries for a task.

3. **Dependencies**: To use the code execution feature, you need to install the `crewai_tools` package. If not installed, the agent will log an info message:
   "Coding tools not available. Install crewai\_tools."


## Code Execution Process

When an agent with code execution enabled encounters a task requiring programming:

<Steps>
  <Step title="Task Analysis">
    The agent analyzes the task and determines that code execution is necessary.
  </Step>

  <Step title="Code Formulation">
    It formulates the Python code needed to solve the problem.
  </Step>

  <Step title="Code Execution">
    The code is sent to the internal code execution tool (`CodeInterpreterTool`).
  </Step>

  <Step title="Result Interpretation">
    The agent interprets the result and incorporates it into its response or uses it for further problem-solving.
  </Step>
</Steps>


## Example Usage

Here's a detailed example of creating an agent with code execution capabilities and using it in a task:

```python Code theme={null}
from crewai import Agent, Task, Crew


# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)


# Create a task that requires code execution
data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants.",
    agent=coding_agent
)


# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task]
)


# Execute the crew
result = analysis_crew.kickoff()

print(result)
```

In this example, the `coding_agent` can write and execute Python code to perform data analysis tasks.



# Conditional Tasks
Source: https://docs.crewai.com/en/learn/conditional-tasks

Learn how to use conditional tasks in a crewAI kickoff


## Introduction

Conditional Tasks in crewAI allow for dynamic workflow adaptation based on the outcomes of previous tasks.
This powerful feature enables crews to make decisions and execute tasks selectively, enhancing the flexibility and efficiency of your AI-driven processes.


## Example Usage

```python Code theme={null}
from typing import List
from pydantic import BaseModel
from crewai import Agent, Crew
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput
from crewai.task import Task
from crewai_tools import SerperDevTool


# Define a condition function for the conditional task

# If false, the task will be skipped, if true, then execute the task.
def is_data_missing(output: TaskOutput) -> bool:
    return len(output.pydantic.events) < 10  # this will skip this task


# Define the agents
data_fetcher_agent = Agent(
    role="Data Fetcher",
    goal="Fetch data online using Serper tool",
    backstory="Backstory 1",
    verbose=True,
    tools=[SerperDevTool()]
)

data_processor_agent = Agent(
    role="Data Processor",
    goal="Process fetched data",
    backstory="Backstory 2",
    verbose=True
)

summary_generator_agent = Agent(
    role="Summary Generator",
    goal="Generate summary from fetched data",
    backstory="Backstory 3",
    verbose=True
)

class EventOutput(BaseModel):
    events: List[str]

task1 = Task(
    description="Fetch data about events in San Francisco using Serper tool",
    expected_output="List of 10 things to do in SF this week",
    agent=data_fetcher_agent,
    output_pydantic=EventOutput,
)

conditional_task = ConditionalTask(
    description="""
        Check if data is missing. If we have less than 10 events,
        fetch more events using Serper tool so that
        we have a total of 10 events in SF this week..
        """,
    expected_output="List of 10 Things to do in SF this week",
    condition=is_data_missing,
    agent=data_processor_agent,
)

task3 = Task(
    description="Generate summary of events in San Francisco from fetched data",
    expected_output="A complete report on the customer and their customers and competitors, including their demographics, preferences, market positioning and audience engagement.",
    agent=summary_generator_agent,
)


# Create a crew with the tasks
crew = Crew(
    agents=[data_fetcher_agent, data_processor_agent, summary_generator_agent],
    tasks=[task1, conditional_task, task3],
    verbose=True,
    planning=True
)


# Run the crew
result = crew.kickoff()
print("results", result)
```



# Create Custom Tools
Source: https://docs.crewai.com/en/learn/create-custom-tools

Comprehensive guide on crafting, using, and managing custom tools within the CrewAI framework, including new functionalities and error handling.


## Creating and Utilizing Tools in CrewAI

This guide provides detailed instructions on creating custom tools for the CrewAI framework and how to efficiently manage and utilize these tools,
incorporating the latest functionalities such as tool delegation, error handling, and dynamic tool calling. It also highlights the importance of collaboration tools,
enabling agents to perform a wide range of actions.

### Subclassing `BaseTool`

To create a personalized tool, inherit from `BaseTool` and define the necessary attributes, including the `args_schema` for input validation, and the `_run` method.

```python Code theme={null}
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"
```

### Using the `tool` Decorator

Alternatively, you can use the tool decorator `@tool`. This approach allows you to define the tool's attributes and functionality directly within a function,
offering a concise and efficient way to create specialized tools tailored to your needs.

```python Code theme={null}
from crewai.tools import tool

@tool("Tool Name")
def my_simple_tool(question: str) -> str:
    """Tool description for clarity."""
    # Tool logic here
    return "Tool output"
```

### Defining a Cache Function for the Tool

To optimize tool performance with caching, define custom caching strategies using the `cache_function` attribute.

```python Code theme={null}
@tool("Tool with Caching")
def cached_tool(argument: str) -> str:
    """Tool functionality description."""
    return "Cacheable result"

def my_cache_strategy(arguments: dict, result: str) -> bool:
    # Define custom caching logic
    return True if some_condition else False

cached_tool.cache_function = my_cache_strategy
```

By adhering to these guidelines and incorporating new functionalities and collaboration tools into your tool creation and management processes,
you can leverage the full capabilities of the CrewAI framework, enhancing both the development experience and the efficiency of your AI agents.



# Custom LLM Implementation
Source: https://docs.crewai.com/en/learn/custom-llm

Learn how to create custom LLM implementations in CrewAI.


## Overview

CrewAI supports custom LLM implementations through the `BaseLLM` abstract base class. This allows you to integrate any LLM provider that doesn't have built-in support in LiteLLM, or implement custom authentication mechanisms.


## Quick Start

Here's a minimal custom LLM implementation:

```python  theme={null}
from crewai import BaseLLM
from typing import Any, Dict, List, Optional, Union
import requests

class CustomLLM(BaseLLM):
    def __init__(self, model: str, api_key: str, endpoint: str, temperature: Optional[float] = None):
        # IMPORTANT: Call super().__init__() with required parameters
        super().__init__(model=model, temperature=temperature)
        
        self.api_key = api_key
        self.endpoint = endpoint
        
    def call(
        self,
        messages: Union[str, List[Dict[str, str]]],
        tools: Optional[List[dict]] = None,
        callbacks: Optional[List[Any]] = None,
        available_functions: Optional[Dict[str, Any]] = None,
    ) -> Union[str, Any]:
        """Call the LLM with the given messages."""
        # Convert string to message format if needed
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        
        # Prepare request
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
        }
        
        # Add tools if provided and supported
        if tools and self.supports_function_calling():
            payload["tools"] = tools
        
        # Make API call
        response = requests.post(
            self.endpoint,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
        
    def supports_function_calling(self) -> bool:
        """Override if your LLM supports function calling."""
        return True  # Change to False if your LLM doesn't support tools
        
    def get_context_window_size(self) -> int:
        """Return the context window size of your LLM."""
        return 8192  # Adjust based on your model's actual context window
```


## Using Your Custom LLM

```python  theme={null}
from crewai import Agent, Task, Crew


# Assuming you have the CustomLLM class defined above

# Create your custom LLM
custom_llm = CustomLLM(
    model="my-custom-model",
    api_key="your-api-key",
    endpoint="https://api.example.com/v1/chat/completions",
    temperature=0.7
)


# Use with an agent
agent = Agent(
    role="Research Assistant",
    goal="Find and analyze information",
    backstory="You are a research assistant.",
    llm=custom_llm
)


# Create and execute tasks
task = Task(
    description="Research the latest developments in AI",
    expected_output="A comprehensive summary",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```


## Required Methods

### Constructor: `__init__()`

**Critical**: You must call `super().__init__(model, temperature)` with the required parameters:

```python  theme={null}
def __init__(self, model: str, api_key: str, temperature: Optional[float] = None):
    # REQUIRED: Call parent constructor with model and temperature
    super().__init__(model=model, temperature=temperature)
    
    # Your custom initialization
    self.api_key = api_key
```

### Abstract Method: `call()`

The `call()` method is the heart of your LLM implementation. It must:

* Accept messages (string or list of dicts with 'role' and 'content')
* Return a string response
* Handle tools and function calling if supported
* Raise appropriate exceptions for errors

### Optional Methods

```python  theme={null}
def supports_function_calling(self) -> bool:
    """Return True if your LLM supports function calling."""
    return True  # Default is True

def supports_stop_words(self) -> bool:
    """Return True if your LLM supports stop sequences."""
    return True  # Default is True

def get_context_window_size(self) -> int:
    """Return the context window size."""
    return 4096  # Default is 4096
```


## Common Patterns

### Error Handling

```python  theme={null}
import requests

def call(self, messages, tools=None, callbacks=None, available_functions=None):
    try:
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
        
    except requests.Timeout:
        raise TimeoutError("LLM request timed out")
    except requests.RequestException as e:
        raise RuntimeError(f"LLM request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Invalid response format: {str(e)}")
```

### Custom Authentication

```python  theme={null}
from crewai import BaseLLM
from typing import Optional

class CustomAuthLLM(BaseLLM):
    def __init__(self, model: str, auth_token: str, endpoint: str, temperature: Optional[float] = None):
        super().__init__(model=model, temperature=temperature)
        self.auth_token = auth_token
        self.endpoint = endpoint
    
    def call(self, messages, tools=None, callbacks=None, available_functions=None):
        headers = {
            "Authorization": f"Custom {self.auth_token}",  # Custom auth format
            "Content-Type": "application/json"
        }
        # Rest of implementation...
```

### Stop Words Support

CrewAI automatically adds `"\nObservation:"` as a stop word to control agent behavior. If your LLM supports stop words:

```python  theme={null}
def call(self, messages, tools=None, callbacks=None, available_functions=None):
    payload = {
        "model": self.model,
        "messages": messages,
        "stop": self.stop  # Include stop words in API call
    }
    # Make API call...

def supports_stop_words(self) -> bool:
    return True  # Your LLM supports stop sequences
```

If your LLM doesn't support stop words natively:

```python  theme={null}
def call(self, messages, tools=None, callbacks=None, available_functions=None):
    response = self._make_api_call(messages, tools)
    content = response["choices"][0]["message"]["content"]
    
    # Manually truncate at stop words
    if self.stop:
        for stop_word in self.stop:
            if stop_word in content:
                content = content.split(stop_word)[0]
                break
    
    return content

def supports_stop_words(self) -> bool:
    return False  # Tell CrewAI we handle stop words manually
```


## Function Calling

If your LLM supports function calling, implement the complete flow:

```python  theme={null}
import json

def call(self, messages, tools=None, callbacks=None, available_functions=None):
    # Convert string to message format
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    
    # Make API call
    response = self._make_api_call(messages, tools)
    message = response["choices"][0]["message"]
    
    # Check for function calls
    if "tool_calls" in message and available_functions:
        return self._handle_function_calls(
            message["tool_calls"], messages, tools, available_functions
        )
    
    return message["content"]

def _handle_function_calls(self, tool_calls, messages, tools, available_functions):
    """Handle function calling with proper message flow."""
    for tool_call in tool_calls:
        function_name = tool_call["function"]["name"]
        
        if function_name in available_functions:
            # Parse and execute function
            function_args = json.loads(tool_call["function"]["arguments"])
            function_result = available_functions[function_name](**function_args)
            
            # Add function call and result to message history
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [tool_call]
            })
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "name": function_name,
                "content": str(function_result)
            })
            
            # Call LLM again with updated context
            return self.call(messages, tools, None, available_functions)
    
    return "Function call failed"
```


## Troubleshooting

### Common Issues

**Constructor Errors**

```python  theme={null}

# ❌ Wrong - missing required parameters
def __init__(self, api_key: str):
    super().__init__()


# ✅ Correct
def __init__(self, model: str, api_key: str, temperature: Optional[float] = None):
    super().__init__(model=model, temperature=temperature)
```

**Function Calling Not Working**

* Ensure `supports_function_calling()` returns `True`
* Check that you handle `tool_calls` in the response
* Verify `available_functions` parameter is used correctly

**Authentication Failures**

* Verify API key format and permissions
* Check authentication header format
* Ensure endpoint URLs are correct

**Response Parsing Errors**

* Validate response structure before accessing nested fields
* Handle cases where content might be None
* Add proper error handling for malformed responses


## Testing Your Custom LLM

```python  theme={null}
from crewai import Agent, Task, Crew

def test_custom_llm():
    llm = CustomLLM(
        model="test-model",
        api_key="test-key",
        endpoint="https://api.test.com"
    )
    
    # Test basic call
    result = llm.call("Hello, world!")
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Test with CrewAI agent
    agent = Agent(
        role="Test Agent",
        goal="Test custom LLM",
        backstory="A test agent.",
        llm=llm
    )
    
    task = Task(
        description="Say hello",
        expected_output="A greeting",
        agent=agent
    )
    
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    assert "hello" in result.raw.lower()
```

This guide covers the essentials of implementing custom LLMs in CrewAI.



# Custom Manager Agent
Source: https://docs.crewai.com/en/learn/custom-manager-agent

Learn how to set a custom agent as the manager in CrewAI, providing more control over task management and coordination.


# Setting a Specific Agent as Manager in CrewAI

CrewAI allows users to set a specific agent as the manager of the crew, providing more control over the management and coordination of tasks.
This feature enables the customization of the managerial role to better fit your project's requirements.


## Using the `manager_agent` Attribute

### Custom Manager Agent

The `manager_agent` attribute allows you to define a custom agent to manage the crew. This agent will oversee the entire process, ensuring that tasks are completed efficiently and to the highest standard.

### Example

```python Code theme={null}
import os
from crewai import Agent, Task, Crew, Process


# Define your agents
researcher = Agent(
    role="Researcher",
    goal="Conduct thorough research and analysis on AI and AI agents",
    backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
    allow_delegation=False,
)

writer = Agent(
    role="Senior Writer",
    goal="Create compelling content about AI and AI agents",
    backstory="You're a senior writer, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently writing content for a new client.",
    allow_delegation=False,
)


# Define your task
task = Task(
    description="Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes.",
    expected_output="5 bullet points, each with a paragraph and accompanying notes.",
)


# Define the manager agent
manager = Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion",
    backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
    allow_delegation=True,
)


# Instantiate your crew with a custom manager
crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    manager_agent=manager,
    process=Process.hierarchical,
)


# Start the crew's work
result = crew.kickoff()
```


## Benefits of a Custom Manager Agent

* **Enhanced Control**: Tailor the management approach to fit the specific needs of your project.
* **Improved Coordination**: Ensure efficient task coordination and management by an experienced agent.
* **Customizable Management**: Define managerial roles and responsibilities that align with your project's goals.


## Setting a Manager LLM

If you're using the hierarchical process and don't want to set a custom manager agent, you can specify the language model for the manager:

```python Code theme={null}
from crewai import LLM

manager_llm = LLM(model="gpt-4o")

crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    process=Process.hierarchical,
    manager_llm=manager_llm
)
```

<Note>
  Either `manager_agent` or `manager_llm` must be set when using the hierarchical process.
</Note>



# Customize Agents
Source: https://docs.crewai.com/en/learn/customizing-agents

A comprehensive guide to tailoring agents for specific roles, tasks, and advanced customizations within the CrewAI framework.


## Customizable Attributes

Crafting an efficient CrewAI team hinges on the ability to dynamically tailor your AI agents to meet the unique requirements of any project. This section covers the foundational attributes you can customize.

### Key Attributes for Customization

| Attribute                           | Description                                                                                                         |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **Role**                            | Specifies the agent's job within the crew, such as 'Analyst' or 'Customer Service Rep'.                             |
| **Goal**                            | Defines the agent’s objectives, aligned with its role and the crew’s overarching mission.                           |
| **Backstory**                       | Provides depth to the agent's persona, enhancing motivations and engagements within the crew.                       |
| **Tools** *(Optional)*              | Represents the capabilities or methods the agent uses for tasks, from simple functions to complex integrations.     |
| **Cache** *(Optional)*              | Determines if the agent should use a cache for tool usage.                                                          |
| **Max RPM**                         | Sets the maximum requests per minute (`max_rpm`). Can be set to `None` for unlimited requests to external services. |
| **Verbose** *(Optional)*            | Enables detailed logging for debugging and optimization, providing insights into execution processes.               |
| **Allow Delegation** *(Optional)*   | Controls task delegation to other agents, default is `False`.                                                       |
| **Max Iter** *(Optional)*           | Limits the maximum number of iterations (`max_iter`) for a task to prevent infinite loops, with a default of 25.    |
| **Max Execution Time** *(Optional)* | Sets the maximum time allowed for an agent to complete a task.                                                      |
| **System Template** *(Optional)*    | Defines the system format for the agent.                                                                            |
| **Prompt Template** *(Optional)*    | Defines the prompt format for the agent.                                                                            |
| **Response Template** *(Optional)*  | Defines the response format for the agent.                                                                          |
| **Use System Prompt** *(Optional)*  | Controls whether the agent will use a system prompt during task execution.                                          |
| **Respect Context Window**          | Enables a sliding context window by default, maintaining context size.                                              |
| **Max Retry Limit**                 | Sets the maximum number of retries (`max_retry_limit`) for an agent in case of errors.                              |


## Advanced Customization Options

Beyond the basic attributes, CrewAI allows for deeper customization to enhance an agent's behavior and capabilities significantly.

### Language Model Customization

Agents can be customized with specific language models (`llm`) and function-calling language models (`function_calling_llm`), offering advanced control over their processing and decision-making abilities.
It's important to note that setting the `function_calling_llm` allows for overriding the default crew function-calling language model, providing a greater degree of customization.


## Performance and Debugging Settings

Adjusting an agent's performance and monitoring its operations are crucial for efficient task execution.

### Verbose Mode and RPM Limit

* **Verbose Mode**: Enables detailed logging of an agent's actions, useful for debugging and optimization. Specifically, it provides insights into agent execution processes, aiding in the optimization of performance.
* **RPM Limit**: Sets the maximum number of requests per minute (`max_rpm`). This attribute is optional and can be set to `None` for no limit, allowing for unlimited queries to external services if needed.

### Maximum Iterations for Task Execution

The `max_iter` attribute allows users to define the maximum number of iterations an agent can perform for a single task, preventing infinite loops or excessively long executions.
The default value is set to 25, providing a balance between thoroughness and efficiency. Once the agent approaches this number, it will try its best to give a good answer.


## Customizing Agents and Tools

Agents are customized by defining their attributes and tools during initialization. Tools are critical for an agent's functionality, enabling them to perform specialized tasks.
The `tools` attribute should be an array of tools the agent can utilize, and it's initialized as an empty list by default. Tools can be added or modified post-agent initialization to adapt to new requirements.

```shell  theme={null}
pip install 'crewai[tools]'
```

### Example: Assigning Tools to an Agent

```python Code theme={null}
import os
from crewai import Agent
from crewai_tools import SerperDevTool


# Set API keys for tool initialization
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key"


# Initialize a search tool
search_tool = SerperDevTool()


# Initialize the agent with advanced options
agent = Agent(
  role='Research Analyst',
  goal='Provide up-to-date market analysis',
  backstory='An expert analyst with a keen eye for market trends.',
  tools=[search_tool],
  memory=True, # Enable memory
  verbose=True,
  max_rpm=None, # No limit on requests per minute
  max_iter=25, # Default value for maximum iterations
)
```


## Delegation and Autonomy

Controlling an agent's ability to delegate tasks or ask questions is vital for tailoring its autonomy and collaborative dynamics within the CrewAI framework. By default,
the `allow_delegation` attribute is now set to `False`, disabling agents to seek assistance or delegate tasks as needed. This default behavior can be changed to promote collaborative problem-solving and
efficiency within the CrewAI ecosystem. If needed, delegation can be enabled to suit specific operational requirements.

### Example: Disabling Delegation for an Agent

```python Code theme={null}
agent = Agent(
  role='Content Writer',
  goal='Write engaging content on market trends',
  backstory='A seasoned writer with expertise in market analysis.',
  allow_delegation=True # Enabling delegation
)
```


## Conclusion

Customizing agents in CrewAI by setting their roles, goals, backstories, and tools, alongside advanced options like language model customization, memory, performance settings, and delegation preferences,
equips a nuanced and capable AI team ready for complex challenges.



# Image Generation with DALL-E
Source: https://docs.crewai.com/en/learn/dalle-image-generation

Learn how to use DALL-E for AI-powered image generation in your CrewAI projects

CrewAI supports integration with OpenAI's DALL-E, allowing your AI agents to generate images as part of their tasks. This guide will walk you through how to set up and use the DALL-E tool in your CrewAI projects.


## Prerequisites

* crewAI installed (latest version)
* OpenAI API key with access to DALL-E


## Setting Up the DALL-E Tool

<Steps>
  <Step title="Import the DALL-E tool">
    ```python  theme={null}
    from crewai_tools import DallETool
    ```
  </Step>

  <Step title="Add the DALL-E tool to your agent configuration">
    ```python  theme={null}
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), DallETool()],  # Add DallETool to the list of tools
            allow_delegation=False,
            verbose=True
        )
    ```
  </Step>
</Steps>


## Using the DALL-E Tool

Once you've added the DALL-E tool to your agent, it can generate images based on text prompts. The tool will return a URL to the generated image, which can be used in the agent's output or passed to other agents for further processing.

### Example Agent Configuration

```yaml  theme={null}
role: >
    LinkedIn Profile Senior Data Researcher
goal: >
    Uncover detailed LinkedIn profiles based on provided name {name} and domain {domain}
    Generate a Dall-e image based on domain {domain}
backstory: >
    You're a seasoned researcher with a knack for uncovering the most relevant LinkedIn profiles.
    Known for your ability to navigate LinkedIn efficiently, you excel at gathering and presenting
    professional information clearly and concisely.
```

### Expected Output

The agent with the DALL-E tool will be able to generate the image and provide a URL in its response. You can then download the image.

<Frame>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7b6378a1ee0aad5d3941193c6802312c" alt="DALL-E Image" data-og-width="670" width="670" data-og-height="670" height="670" data-path="images/enterprise/dall-e-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=95b3ae8ec53f789746846831fa981b32 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f880f86fa3b648a257ac74fcc7838dce 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c98e8fd36d462d3806c398c1f074efb2 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=68af7edd51913d04723c0fbae774ea1d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=07c15be8399f83239d49e28f6667a28d 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=619edc0ffc57a1eddd3cd7f9715b6b0a 2500w" />
</Frame>


## Best Practices

1. **Be specific in your image generation prompts** to get the best results.
2. **Consider generation time** - Image generation can take some time, so factor this into your task planning.
3. **Follow usage policies** - Always comply with OpenAI's usage policies when generating images.


## Troubleshooting

1. **Check API access** - Ensure your OpenAI API key has access to DALL-E.
2. **Version compatibility** - Check that you're using the latest version of crewAI and crewai-tools.
3. **Tool configuration** - Verify that the DALL-E tool is correctly added to the agent's tool list.



# Force Tool Output as Result
Source: https://docs.crewai.com/en/learn/force-tool-output-as-result

Learn how to force tool output as the result in an Agent's task in CrewAI.


## Introduction

In CrewAI, you can force the output of a tool as the result of an agent's task.
This feature is useful when you want to ensure that the tool output is captured and returned as the task result, avoiding any agent modification during the task execution.


## Forcing Tool Output as Result

To force the tool output as the result of an agent's task, you need to set the `result_as_answer` parameter to `True` when adding a tool to the agent.
This parameter ensures that the tool output is captured and returned as the task result, without any modifications by the agent.

Here's an example of how to force the tool output as the result of an agent's task:

```python Code theme={null}
from crewai.agent import Agent
from my_tool import MyCustomTool


# Create a coding agent with the custom tool
coding_agent = Agent(
        role="Data Scientist",
        goal="Produce amazing reports on AI",
        backstory="You work with data and AI",
        tools=[MyCustomTool(result_as_answer=True)],
    )


# Assuming the tool's execution and result population occurs within the system
task_result = coding_agent.execute_task(task)
```


## Workflow in Action

<Steps>
  <Step title="Task Execution">
    The agent executes the task using the tool provided.
  </Step>

  <Step title="Tool Output">
    The tool generates the output, which is captured as the task result.
  </Step>

  <Step title="Agent Interaction">
    The agent may reflect and take learnings from the tool but the output is not modified.
  </Step>

  <Step title="Result Return">
    The tool output is returned as the task result without any modifications.
  </Step>
</Steps>



# Hierarchical Process
Source: https://docs.crewai.com/en/learn/hierarchical-process

A comprehensive guide to understanding and applying the hierarchical process within your CrewAI projects, updated to reflect the latest coding practices and functionalities.


## Introduction

The hierarchical process in CrewAI introduces a structured approach to task management, simulating traditional organizational hierarchies for efficient task delegation and execution.
This systematic workflow enhances project outcomes by ensuring tasks are handled with optimal efficiency and accuracy.

<Tip>
  The hierarchical process is designed to leverage advanced models like GPT-4, optimizing token usage while handling complex tasks with greater efficiency.
</Tip>


## Hierarchical Process Overview

By default, tasks in CrewAI are managed through a sequential process. However, adopting a hierarchical approach allows for a clear hierarchy in task management,
where a 'manager' agent coordinates the workflow, delegates tasks, and validates outcomes for streamlined and effective execution. This manager agent can now be either
automatically created by CrewAI or explicitly set by the user.

### Key Features

* **Task Delegation**: A manager agent allocates tasks among crew members based on their roles and capabilities.
* **Result Validation**: The manager evaluates outcomes to ensure they meet the required standards.
* **Efficient Workflow**: Emulates corporate structures, providing an organized approach to task management.
* **System Prompt Handling**: Optionally specify whether the system should use predefined prompts.
* **Stop Words Control**: Optionally specify whether stop words should be used, supporting various models including the o1 models.
* **Context Window Respect**: Prioritize important context by enabling respect of the context window, which is now the default behavior.
* **Delegation Control**: Delegation is now disabled by default to give users explicit control.
* **Max Requests Per Minute**: Configurable option to set the maximum number of requests per minute.
* **Max Iterations**: Limit the maximum number of iterations for obtaining a final answer.


## Implementing the Hierarchical Process

To utilize the hierarchical process, it's essential to explicitly set the process attribute to `Process.hierarchical`, as the default behavior is `Process.sequential`.
Define a crew with a designated manager and establish a clear chain of command.

<Tip>
  Assign tools at the agent level to facilitate task delegation and execution by the designated agents under the manager's guidance.
  Tools can also be specified at the task level for precise control over tool availability during task execution.
</Tip>

<Tip>
  Configuring the `manager_llm` parameter is crucial for the hierarchical process.
  The system requires a manager LLM to be set up for proper function, ensuring tailored decision-making.
</Tip>

```python Code theme={null}
from crewai import Crew, Process, Agent


# Agents are defined with attributes for backstory, cache, and verbose mode
researcher = Agent(
    role='Researcher',
    goal='Conduct in-depth analysis',
    backstory='Experienced data analyst with a knack for uncovering hidden trends.',
)
writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passionate about storytelling in technical domains.',
)


# Establishing the crew with a hierarchical process and additional configurations
project_crew = Crew(
    tasks=[...],  # Tasks to be delegated and executed under the manager's supervision
    agents=[researcher, writer],
    manager_llm="gpt-4o",  # Specify which LLM the manager should use
    process=Process.hierarchical,  
    planning=True, 
)
```

### Using a Custom Manager Agent

Alternatively, you can create a custom manager agent with specific attributes tailored to your project's management needs. This gives you more control over the manager's behavior and capabilities.

```python  theme={null}

# Define a custom manager agent
manager = Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion",
    backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success.",
    allow_delegation=True,
)


# Use the custom manager in your crew
project_crew = Crew(
    tasks=[...],
    agents=[researcher, writer],
    manager_agent=manager,  # Use your custom manager agent
    process=Process.hierarchical,
    planning=True,
)
```

<Tip>
  For more details on creating and customizing a manager agent, check out the [Custom Manager Agent documentation](https://docs.crewai.com/how-to/custom-manager-agent#custom-manager-agent).
</Tip>

### Workflow in Action

1. **Task Assignment**: The manager assigns tasks strategically, considering each agent's capabilities and available tools.
2. **Execution and Review**: Agents complete their tasks with the option for asynchronous execution and callback functions for streamlined workflows.
3. **Sequential Task Progression**: Despite being a hierarchical process, tasks follow a logical order for smooth progression, facilitated by the manager's oversight.


## Conclusion

Adopting the hierarchical process in CrewAI, with the correct configurations and understanding of the system's capabilities, facilitates an organized and efficient approach to project management.
Utilize the advanced features and customizations to tailor the workflow to your specific needs, ensuring optimal task execution and project success.



# Human-in-the-Loop (HITL) Workflows
Source: https://docs.crewai.com/en/learn/human-in-the-loop

Learn how to implement Human-in-the-Loop workflows in CrewAI for enhanced decision-making

Human-in-the-Loop (HITL) is a powerful approach that combines artificial intelligence with human expertise to enhance decision-making and improve task outcomes. This guide shows you how to implement HITL within CrewAI.


## Setting Up HITL Workflows

<Steps>
  <Step title="Configure Your Task">
    Set up your task with human input enabled:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cb2e2bab131e9eff86b0c51dceb16e11" alt="Crew Human Input" data-og-width="624" width="624" data-og-height="165" height="165" data-path="images/enterprise/crew-human-input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1bc2a85e5aa6e736a118fe2c91452dc6 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=137c8e9c09c9a93ba1b683ad3e247e0d 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79c8be91790b117c1498568ca48f4287 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4da8411c0c26ee98c0dcdde6117353fe 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1b24b707df7ec697db2652d80ed3ff8f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=39a7543043c397cf4ff84582216ddb65 2500w" />
    </Frame>
  </Step>

  <Step title="Provide Webhook URL">
    When kicking off your crew, include a webhook URL for human input:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f2d298c0b4c7b3a62e1dee4e2e6f1bb3" alt="Crew Webhook URL" data-og-width="624" width="624" data-og-height="259" height="259" data-path="images/enterprise/crew-webhook-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=80f52cbe2cd1c6a2a4cd3e2039c22971 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6496d6f5e1fe13fec8be8a406e635b26 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=27cfbbf1fecdab2540df4aeb7ddd15b6 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=57d3439e96917a0627189bfd188af4a0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cad1f034d8fd4113f08df6bf1a58f3fa 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fba10cd375c57bcd9b2a216067b5bd44 2500w" />
    </Frame>

    Example with Bearer authentication:

    ```bash  theme={null}
    curl -X POST {BASE_URL}/kickoff \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "inputs": {
          "topic": "AI Research"
        },
        "humanInputWebhook": {
          "url": "https://your-webhook.com/hitl",
          "authentication": {
            "strategy": "bearer",
            "token": "your-webhook-secret-token"
          }
        }
      }'
    ```

    Or with Basic authentication:

    ```bash  theme={null}
    curl -X POST {BASE_URL}/kickoff \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "inputs": {
          "topic": "AI Research"
        },
        "humanInputWebhook": {
          "url": "https://your-webhook.com/hitl",
          "authentication": {
            "strategy": "basic",
            "username": "your-username",
            "password": "your-password"
          }
        }
      }'
    ```
  </Step>

  <Step title="Receive Webhook Notification">
    Once the crew completes the task requiring human input, you'll receive a webhook notification containing:

    * Execution ID
    * Task ID
    * Task output
  </Step>

  <Step title="Review Task Output">
    The system will pause in the `Pending Human Input` state. Review the task output carefully.
  </Step>

  <Step title="Submit Human Feedback">
    Call the resume endpoint of your crew with the following information:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1e1c2ca22a2d674426f8e663fed33eca" alt="Crew Resume Endpoint" data-og-width="624" width="624" data-og-height="261" height="261" data-path="images/enterprise/crew-resume-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=09014207ae06e6522303b77e4648f0d4 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1ad53990ab04014e622b3acdb37ca604 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afb11308edffa03de969712505cf95ab 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bd69f0d75ec47ac2c6280f24a550bff 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f81e1ebcdc8a9348133503eb5eb4e37a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b12843fa2b80cc86580220766a1f4cc4 2500w" />
    </Frame>

    <Warning>
      **Critical: Webhook URLs Must Be Provided Again**:
      You **must** provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`) in the resume call that you used in the kickoff call. Webhook configurations are **NOT** automatically carried over from kickoff - they must be explicitly included in the resume request to continue receiving notifications for task completion, agent steps, and crew completion.
    </Warning>

    Example resume call with webhooks:

    ```bash  theme={null}
    curl -X POST {BASE_URL}/resume \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "execution_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
        "task_id": "research_task",
        "human_feedback": "Great work! Please add more details.",
        "is_approve": true,
        "taskWebhookUrl": "https://your-server.com/webhooks/task",
        "stepWebhookUrl": "https://your-server.com/webhooks/step",
        "crewWebhookUrl": "https://your-server.com/webhooks/crew"
      }'
    ```

    <Warning>
      **Feedback Impact on Task Execution**:
      It's crucial to exercise care when providing feedback, as the entire feedback content will be incorporated as additional context for further task executions.
    </Warning>

    This means:

    * All information in your feedback becomes part of the task's context.
    * Irrelevant details may negatively influence it.
    * Concise, relevant feedback helps maintain task focus and efficiency.
    * Always review your feedback carefully before submission to ensure it contains only pertinent information that will positively guide the task's execution.
  </Step>

  <Step title="Handle Negative Feedback">
    If you provide negative feedback:

    * The crew will retry the task with added context from your feedback.
    * You'll receive another webhook notification for further review.
    * Repeat steps 4-6 until satisfied.
  </Step>

  <Step title="Execution Continuation">
    When you submit positive feedback, the execution will proceed to the next steps.
  </Step>
</Steps>


## Best Practices

* **Be Specific**: Provide clear, actionable feedback that directly addresses the task at hand
* **Stay Relevant**: Only include information that will help improve the task execution
* **Be Timely**: Respond to HITL prompts promptly to avoid workflow delays
* **Review Carefully**: Double-check your feedback before submitting to ensure accuracy


## Common Use Cases

HITL workflows are particularly valuable for:

* Quality assurance and validation
* Complex decision-making scenarios
* Sensitive or high-stakes operations
* Creative tasks requiring human judgment
* Compliance and regulatory reviews



# Human Input on Execution
Source: https://docs.crewai.com/en/learn/human-input-on-execution

Integrating CrewAI with human input during execution in complex decision-making processes and leveraging the full capabilities of the agent's attributes and tools.


## Human input in agent execution

Human input is critical in several agent execution scenarios, allowing agents to request additional information or clarification when necessary.
This feature is especially useful in complex decision-making processes or when agents require more details to complete a task effectively.


## Using human input with CrewAI

To integrate human input into agent execution, set the `human_input` flag in the task definition. When enabled, the agent prompts the user for input before delivering its final answer.
This input can provide extra context, clarify ambiguities, or validate the agent's output.

### Example:

```shell  theme={null}
pip install crewai
```

```python Code theme={null}
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"


# Loading Tools
search_tool = SerperDevTool()


# Define your agents with roles, goals, tools, and additional attributes
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory=(
        "You are a Senior Research Analyst at a leading tech think tank. "
        "Your expertise lies in identifying emerging trends and technologies in AI and data science. "
        "You have a knack for dissecting complex data and presenting actionable insights."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)
writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory=(
        "You are a renowned Tech Content Strategist, known for your insightful and engaging articles on technology and innovation. "
        "With a deep understanding of the tech industry, you transform complex concepts into compelling narratives."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    cache=False,  # Disable cache for this agent
)


# Create tasks for your agents
task1 = Task(
    description=(
        "Conduct a comprehensive analysis of the latest advancements in AI in 2025. "
        "Identify key trends, breakthrough technologies, and potential industry impacts. "
        "Compile your findings in a detailed report. "
        "Make sure to check with a human if the draft is good before finalizing your answer."
    ),
    expected_output='A comprehensive full report on the latest AI advancements in 2025, leave nothing out',
    agent=researcher,
    human_input=True
)

task2 = Task(
    description=(
        "Using the insights from the researcher\'s report, develop an engaging blog post that highlights the most significant AI advancements. "
        "Your post should be informative yet accessible, catering to a tech-savvy audience. "
        "Aim for a narrative that captures the essence of these breakthroughs and their implications for the future."
    ),
    expected_output='A compelling 3 paragraphs blog post formatted as markdown about the latest AI advancements in 2025',
    agent=writer,
    human_input=True
)


# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    memory=True,
    planning=True  # Enable planning feature for the crew
)


# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
```



# Kickoff Crew Asynchronously
Source: https://docs.crewai.com/en/learn/kickoff-async

Kickoff a Crew Asynchronously


## Introduction

CrewAI provides the ability to kickoff a crew asynchronously, allowing you to start the crew execution in a non-blocking manner.
This feature is particularly useful when you want to run multiple crews concurrently or when you need to perform other tasks while the crew is executing.


## Asynchronous Crew Execution

To kickoff a crew asynchronously, use the `kickoff_async()` method. This method initiates the crew execution in a separate thread, allowing the main thread to continue executing other tasks.

### Method Signature

```python Code theme={null}
def kickoff_async(self, inputs: dict) -> CrewOutput:
```

### Parameters

* `inputs` (dict): A dictionary containing the input data required for the tasks.

### Returns

* `CrewOutput`: An object representing the result of the crew execution.


## Potential Use Cases

* **Parallel Content Generation**: Kickoff multiple independent crews asynchronously, each responsible for generating content on different topics. For example, one crew might research and draft an article on AI trends, while another crew generates social media posts about a new product launch. Each crew operates independently, allowing content production to scale efficiently.

* **Concurrent Market Research Tasks**: Launch multiple crews asynchronously to conduct market research in parallel. One crew might analyze industry trends, while another examines competitor strategies, and yet another evaluates consumer sentiment. Each crew independently completes its task, enabling faster and more comprehensive insights.

* **Independent Travel Planning Modules**: Execute separate crews to independently plan different aspects of a trip. One crew might handle flight options, another handles accommodation, and a third plans activities. Each crew works asynchronously, allowing various components of the trip to be planned simultaneously and independently for faster results.


## Example: Single Asynchronous Crew Execution

Here's an example of how to kickoff a crew asynchronously using asyncio and awaiting the result:

```python Code theme={null}
import asyncio
from crewai import Crew, Agent, Task


# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)


# Create a task that requires code execution
data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)


# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task]
)


# Async function to kickoff the crew asynchronously
async def async_crew_execution():
    result = await analysis_crew.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    print("Crew Result:", result)


# Run the async function
asyncio.run(async_crew_execution())
```


## Example: Multiple Asynchronous Crew Executions

In this example, we'll show how to kickoff multiple crews asynchronously and wait for all of them to complete using `asyncio.gather()`:

```python Code theme={null}
import asyncio
from crewai import Crew, Agent, Task


# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)


# Create tasks that require code execution
task_1 = Task(
    description="Analyze the first dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)

task_2 = Task(
    description="Analyze the second dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)


# Create two crews and add tasks
crew_1 = Crew(agents=[coding_agent], tasks=[task_1])
crew_2 = Crew(agents=[coding_agent], tasks=[task_2])


# Async function to kickoff multiple crews asynchronously and wait for all to finish
async def async_multiple_crews():
    # Create coroutines for concurrent execution
    result_1 = crew_1.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    result_2 = crew_2.kickoff_async(inputs={"ages": [20, 22, 24, 28, 30]})

    # Wait for both crews to finish
    results = await asyncio.gather(result_1, result_2)

    for i, result in enumerate(results, 1):
        print(f"Crew {i} Result:", result)


# Run the async function
asyncio.run(async_multiple_crews())
```



# Kickoff Crew for Each
Source: https://docs.crewai.com/en/learn/kickoff-for-each

Kickoff Crew for Each Item in a List


## Introduction

CrewAI provides the ability to kickoff a crew for each item in a list, allowing you to execute the crew for each item in the list.
This feature is particularly useful when you need to perform the same set of tasks for multiple items.


## Kicking Off a Crew for Each Item

To kickoff a crew for each item in a list, use the `kickoff_for_each()` method.
This method executes the crew for each item in the list, allowing you to process multiple items efficiently.

Here's an example of how to kickoff a crew for each item in a list:

```python Code theme={null}
from crewai import Crew, Agent, Task


# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    allow_code_execution=True
)


# Create a task that requires code execution
data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age calculated from the dataset"
)


# Create a crew and add the task
analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task],
    verbose=True,
    memory=False
)

datasets = [
  { "ages": [25, 30, 35, 40, 45] },
  { "ages": [20, 25, 30, 35, 40] },
  { "ages": [30, 35, 40, 45, 50] }
]


# Execute the crew
result = analysis_crew.kickoff_for_each(inputs=datasets)
```



# Connect to any LLM
Source: https://docs.crewai.com/en/learn/llm-connections

Comprehensive guide on integrating CrewAI with various Large Language Models (LLMs) using LiteLLM, including supported providers and configuration options.


## Connect CrewAI to LLMs

CrewAI uses LiteLLM to connect to a wide variety of Language Models (LLMs). This integration provides extensive versatility, allowing you to use models from numerous providers with a simple, unified interface.

<Note>
  By default, CrewAI uses the `gpt-4o-mini` model. This is determined by the `OPENAI_MODEL_NAME` environment variable, which defaults to "gpt-4o-mini" if not set.
  You can easily configure your agents to use a different model or provider as described in this guide.
</Note>


## Supported Providers

LiteLLM supports a wide range of providers, including but not limited to:

* OpenAI
* Anthropic
* Google (Vertex AI, Gemini)
* Azure OpenAI
* AWS (Bedrock, SageMaker)
* Cohere
* VoyageAI
* Hugging Face
* Ollama
* Mistral AI
* Replicate
* Together AI
* AI21
* Cloudflare Workers AI
* DeepInfra
* Groq
* SambaNova
* Nebius AI Studio
* [NVIDIA NIMs](https://docs.api.nvidia.com/nim/reference/models-1)
* And many more!

For a complete and up-to-date list of supported providers, please refer to the [LiteLLM Providers documentation](https://docs.litellm.ai/docs/providers).


## Changing the LLM

To use a different LLM with your CrewAI agents, you have several options:

<Tabs>
  <Tab title="Using a String Identifier">
    Pass the model name as a string when initializing the agent:

    <CodeGroup>
      ```python Code theme={null}
      from crewai import Agent

      # Using OpenAI's GPT-4
      openai_agent = Agent(
          role='OpenAI Expert',
          goal='Provide insights using GPT-4',
          backstory="An AI assistant powered by OpenAI's latest model.",
          llm='gpt-4'
      )

      # Using Anthropic's Claude
      claude_agent = Agent(
          role='Anthropic Expert',
          goal='Analyze data using Claude',
          backstory="An AI assistant leveraging Anthropic's language model.",
          llm='claude-2'
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Using the LLM Class">
    For more detailed configuration, use the LLM class:

    <CodeGroup>
      ```python Code theme={null}
      from crewai import Agent, LLM

      llm = LLM(
          model="gpt-4",
          temperature=0.7,
          base_url="https://api.openai.com/v1",
          api_key="your-api-key-here"
      )

      agent = Agent(
          role='Customized LLM Expert',
          goal='Provide tailored responses',
          backstory="An AI assistant with custom LLM settings.",
          llm=llm
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Configuration Options

When configuring an LLM for your agent, you have access to a wide range of parameters:

| Parameter              |        Type        | Description                                                      |
| :--------------------- | :----------------: | :--------------------------------------------------------------- |
| **model**              |        `str`       | The name of the model to use (e.g., "gpt-4", "claude-2")         |
| **temperature**        |       `float`      | Controls randomness in output (0.0 to 1.0)                       |
| **max\_tokens**        |        `int`       | Maximum number of tokens to generate                             |
| **top\_p**             |       `float`      | Controls diversity of output (0.0 to 1.0)                        |
| **frequency\_penalty** |       `float`      | Penalizes new tokens based on their frequency in the text so far |
| **presence\_penalty**  |       `float`      | Penalizes new tokens based on their presence in the text so far  |
| **stop**               | `str`, `List[str]` | Sequence(s) to stop generation                                   |
| **base\_url**          |        `str`       | The base URL for the API endpoint                                |
| **api\_key**           |        `str`       | Your API key for authentication                                  |

For a complete list of parameters and their descriptions, refer to the LLM class documentation.


## Connecting to OpenAI-Compatible LLMs

You can connect to OpenAI-compatible LLMs using either environment variables or by setting specific attributes on the LLM class:

<Tabs>
  <Tab title="Using Environment Variables">
    <CodeGroup>
      ```python Generic theme={null}
      import os

      os.environ["OPENAI_API_KEY"] = "your-api-key"
      os.environ["OPENAI_API_BASE"] = "https://api.your-provider.com/v1"
      os.environ["OPENAI_MODEL_NAME"] = "your-model-name"
      ```

      ```python Google theme={null}
      import os

      # Example using Gemini's OpenAI-compatible API.
      os.environ["OPENAI_API_KEY"] = "your-gemini-key"  # Should start with AIza...
      os.environ["OPENAI_API_BASE"] = "https://generativelanguage.googleapis.com/v1beta/openai/"
      os.environ["OPENAI_MODEL_NAME"] = "openai/gemini-2.0-flash"  # Add your Gemini model here, under openai/
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Using LLM Class Attributes">
    <CodeGroup>
      ```python Generic theme={null}
      llm = LLM(
          model="custom-model-name",
          api_key="your-api-key",
          base_url="https://api.your-provider.com/v1"
      )
      agent = Agent(llm=llm, ...)
      ```

      ```python Google theme={null}
      # Example using Gemini's OpenAI-compatible API
      llm = LLM(
          model="openai/gemini-2.0-flash",
          base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
          api_key="your-gemini-key",  # Should start with AIza...
      )
      agent = Agent(llm=llm, ...)
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Using Local Models with Ollama

For local models like those provided by Ollama:

<Steps>
  <Step title="Download and install Ollama">
    [Click here to download and install Ollama](https://ollama.com/download)
  </Step>

  <Step title="Pull the desired model">
    For example, run `ollama pull llama3.2` to download the model.
  </Step>

  <Step title="Configure your agent">
    <CodeGroup>
      ```python Code theme={null}
          agent = Agent(
              role='Local AI Expert',
              goal='Process information using a local model',
              backstory="An AI assistant running on local hardware.",
              llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
          )
      ```
    </CodeGroup>
  </Step>
</Steps>


## Changing the Base API URL

You can change the base API URL for any LLM provider by setting the `base_url` parameter:

```python Code theme={null}
llm = LLM(
    model="custom-model-name",
    base_url="https://api.your-provider.com/v1",
    api_key="your-api-key"
)
agent = Agent(llm=llm, ...)
```

This is particularly useful when working with OpenAI-compatible APIs or when you need to specify a different endpoint for your chosen provider.


## Conclusion

By leveraging LiteLLM, CrewAI offers seamless integration with a vast array of LLMs. This flexibility allows you to choose the most suitable model for your specific needs, whether you prioritize performance, cost-efficiency, or local deployment. Remember to consult the [LiteLLM documentation](https://docs.litellm.ai/docs/) for the most up-to-date information on supported models and configuration options.



# Strategic LLM Selection Guide
Source: https://docs.crewai.com/en/learn/llm-selection-guide

Strategic framework for choosing the right LLM for your CrewAI AI agents and writing effective task and agent definitions


## The CrewAI Approach to LLM Selection

Rather than prescriptive model recommendations, we advocate for a **thinking framework** that helps you make informed decisions based on your specific use case, constraints, and requirements. The LLM landscape evolves rapidly, with new models emerging regularly and existing ones being updated frequently. What matters most is developing a systematic approach to evaluation that remains relevant regardless of which specific models are available.

<Note>
  This guide focuses on strategic thinking rather than specific model recommendations, as the LLM landscape evolves rapidly.
</Note>


## Quick Decision Framework

<Steps>
  <Step title="Analyze Your Tasks">
    Begin by deeply understanding what your tasks actually require. Consider the cognitive complexity involved, the depth of reasoning needed, the format of expected outputs, and the amount of context the model will need to process. This foundational analysis will guide every subsequent decision.
  </Step>

  <Step title="Map Model Capabilities">
    Once you understand your requirements, map them to model strengths. Different model families excel at different types of work; some are optimized for reasoning and analysis, others for creativity and content generation, and others for speed and efficiency.
  </Step>

  <Step title="Consider Constraints">
    Factor in your real-world operational constraints including budget limitations, latency requirements, data privacy needs, and infrastructure capabilities. The theoretically best model may not be the practically best choice for your situation.
  </Step>

  <Step title="Test and Iterate">
    Start with reliable, well-understood models and optimize based on actual performance in your specific use case. Real-world results often differ from theoretical benchmarks, so empirical testing is crucial.
  </Step>
</Steps>


## Core Selection Framework

### a. Task-First Thinking

The most critical step in LLM selection is understanding what your task actually demands. Too often, teams select models based on general reputation or benchmark scores without carefully analyzing their specific requirements. This approach leads to either over-engineering simple tasks with expensive, complex models, or under-powering sophisticated work with models that lack the necessary capabilities.

<Tabs>
  <Tab title="Reasoning Complexity">
    * **Simple Tasks** represent the majority of everyday AI work and include basic instruction following, straightforward data processing, and simple formatting operations. These tasks typically have clear inputs and outputs with minimal ambiguity. The cognitive load is low, and the model primarily needs to follow explicit instructions rather than engage in complex reasoning.

    * **Complex Tasks** require multi-step reasoning, strategic thinking, and the ability to handle ambiguous or incomplete information. These might involve analyzing multiple data sources, developing comprehensive strategies, or solving problems that require breaking down into smaller components. The model needs to maintain context across multiple reasoning steps and often must make inferences that aren't explicitly stated.

    * **Creative Tasks** demand a different type of cognitive capability focused on generating novel, engaging, and contextually appropriate content. This includes storytelling, marketing copy creation, and creative problem-solving. The model needs to understand nuance, tone, and audience while producing content that feels authentic and engaging rather than formulaic.
  </Tab>

  <Tab title="Output Requirements">
    * **Structured Data** tasks require precision and consistency in format adherence. When working with JSON, XML, or database formats, the model must reliably produce syntactically correct output that can be programmatically processed. These tasks often have strict validation requirements and little tolerance for format errors, making reliability more important than creativity.

    * **Creative Content** outputs demand a balance of technical competence and creative flair. The model needs to understand audience, tone, and brand voice while producing content that engages readers and achieves specific communication goals. Quality here is often subjective and requires models that can adapt their writing style to different contexts and purposes.

    * **Technical Content** sits between structured data and creative content, requiring both precision and clarity. Documentation, code generation, and technical analysis need to be accurate and comprehensive while remaining accessible to the intended audience. The model must understand complex technical concepts and communicate them effectively.
  </Tab>

  <Tab title="Context Needs">
    * **Short Context** scenarios involve focused, immediate tasks where the model needs to process limited information quickly. These are often transactional interactions where speed and efficiency matter more than deep understanding. The model doesn't need to maintain extensive conversation history or process large documents.

    * **Long Context** requirements emerge when working with substantial documents, extended conversations, or complex multi-part tasks. The model needs to maintain coherence across thousands of tokens while referencing earlier information accurately. This capability becomes crucial for document analysis, comprehensive research, and sophisticated dialogue systems.

    * **Very Long Context** scenarios push the boundaries of what's currently possible, involving massive document processing, extensive research synthesis, or complex multi-session interactions. These use cases require models specifically designed for extended context handling and often involve trade-offs between context length and processing speed.
  </Tab>
</Tabs>

### b. Model Capability Mapping

Understanding model capabilities requires looking beyond marketing claims and benchmark scores to understand the fundamental strengths and limitations of different model architectures and training approaches.

<AccordionGroup>
  <Accordion title="Reasoning Models" icon="brain">
    Reasoning models represent a specialized category designed specifically for complex, multi-step thinking tasks. These models excel when problems require careful analysis, strategic planning, or systematic problem decomposition. They typically employ techniques like chain-of-thought reasoning or tree-of-thought processing to work through complex problems step by step.

    The strength of reasoning models lies in their ability to maintain logical consistency across extended reasoning chains and to break down complex problems into manageable components. They're particularly valuable for strategic planning, complex analysis, and situations where the quality of reasoning matters more than speed of response.

    However, reasoning models often come with trade-offs in terms of speed and cost. They may also be less suitable for creative tasks or simple operations where their sophisticated reasoning capabilities aren't needed. Consider these models when your tasks involve genuine complexity that benefits from systematic, step-by-step analysis.
  </Accordion>

  <Accordion title="General Purpose Models" icon="microchip">
    General purpose models offer the most balanced approach to LLM selection, providing solid performance across a wide range of tasks without extreme specialization in any particular area. These models are trained on diverse datasets and optimized for versatility rather than peak performance in specific domains.

    The primary advantage of general purpose models is their reliability and predictability across different types of work. They handle most standard business tasks competently, from research and analysis to content creation and data processing. This makes them excellent choices for teams that need consistent performance across varied workflows.

    While general purpose models may not achieve the peak performance of specialized alternatives in specific domains, they offer operational simplicity and reduced complexity in model management. They're often the best starting point for new projects, allowing teams to understand their specific needs before potentially optimizing with more specialized models.
  </Accordion>

  <Accordion title="Fast & Efficient Models" icon="bolt">
    Fast and efficient models prioritize speed, cost-effectiveness, and resource efficiency over sophisticated reasoning capabilities. These models are optimized for high-throughput scenarios where quick responses and low operational costs are more important than nuanced understanding or complex reasoning.

    These models excel in scenarios involving routine operations, simple data processing, function calling, and high-volume tasks where the cognitive requirements are relatively straightforward. They're particularly valuable for applications that need to process many requests quickly or operate within tight budget constraints.

    The key consideration with efficient models is ensuring that their capabilities align with your task requirements. While they can handle many routine operations effectively, they may struggle with tasks requiring nuanced understanding, complex reasoning, or sophisticated content generation. They're best used for well-defined, routine operations where speed and cost matter more than sophistication.
  </Accordion>

  <Accordion title="Creative Models" icon="pen">
    Creative models are specifically optimized for content generation, writing quality, and creative thinking tasks. These models typically excel at understanding nuance, tone, and style while producing engaging, contextually appropriate content that feels natural and authentic.

    The strength of creative models lies in their ability to adapt writing style to different audiences, maintain consistent voice and tone, and generate content that engages readers effectively. They often perform better on tasks involving storytelling, marketing copy, brand communications, and other content where creativity and engagement are primary goals.

    When selecting creative models, consider not just their ability to generate text, but their understanding of audience, context, and purpose. The best creative models can adapt their output to match specific brand voices, target different audience segments, and maintain consistency across extended content pieces.
  </Accordion>

  <Accordion title="Open Source Models" icon="code">
    Open source models offer unique advantages in terms of cost control, customization potential, data privacy, and deployment flexibility. These models can be run locally or on private infrastructure, providing complete control over data handling and model behavior.

    The primary benefits of open source models include elimination of per-token costs, ability to fine-tune for specific use cases, complete data privacy, and independence from external API providers. They're particularly valuable for organizations with strict data privacy requirements, budget constraints, or specific customization needs.

    However, open source models require more technical expertise to deploy and maintain effectively. Teams need to consider infrastructure costs, model management complexity, and the ongoing effort required to keep models updated and optimized. The total cost of ownership may be higher than cloud-based alternatives when factoring in technical overhead.
  </Accordion>
</AccordionGroup>


## Strategic Configuration Patterns

### a. Multi-Model Approach

<Tip>
  Use different models for different purposes within the same crew to optimize both performance and cost.
</Tip>

The most sophisticated CrewAI implementations often employ multiple models strategically, assigning different models to different agents based on their specific roles and requirements. This approach allows teams to optimize for both performance and cost by using the most appropriate model for each type of work.

Planning agents benefit from reasoning models that can handle complex strategic thinking and multi-step analysis. These agents often serve as the "brain" of the operation, developing strategies and coordinating other agents' work. Content agents, on the other hand, perform best with creative models that excel at writing quality and audience engagement. Processing agents handling routine operations can use efficient models that prioritize speed and cost-effectiveness.

**Example: Research and Analysis Crew**

```python  theme={null}
from crewai import Agent, Task, Crew, LLM


# High-capability reasoning model for strategic planning
manager_llm = LLM(model="gemini-2.5-flash-preview-05-20", temperature=0.1)


# Creative model for content generation
content_llm = LLM(model="claude-3-5-sonnet-20241022", temperature=0.7)


# Efficient model for data processing
processing_llm = LLM(model="gpt-4o-mini", temperature=0)

research_manager = Agent(
    role="Research Strategy Manager",
    goal="Develop comprehensive research strategies and coordinate team efforts",
    backstory="Expert research strategist with deep analytical capabilities",
    llm=manager_llm,  # High-capability model for complex reasoning
    verbose=True
)

content_writer = Agent(
    role="Research Content Writer",
    goal="Transform research findings into compelling, well-structured reports",
    backstory="Skilled writer who excels at making complex topics accessible",
    llm=content_llm,  # Creative model for engaging content
    verbose=True
)

data_processor = Agent(
    role="Data Analysis Specialist",
    goal="Extract and organize key data points from research sources",
    backstory="Detail-oriented analyst focused on accuracy and efficiency",
    llm=processing_llm,  # Fast, cost-effective model for routine tasks
    verbose=True
)

crew = Crew(
    agents=[research_manager, content_writer, data_processor],
    tasks=[...],  # Your specific tasks
    manager_llm=manager_llm,  # Manager uses the reasoning model
    verbose=True
)
```

The key to successful multi-model implementation is understanding how different agents interact and ensuring that model capabilities align with agent responsibilities. This requires careful planning but can result in significant improvements in both output quality and operational efficiency.

### b. Component-Specific Selection

<Tabs>
  <Tab title="Manager LLM">
    The manager LLM plays a crucial role in hierarchical CrewAI processes, serving as the coordination point for multiple agents and tasks. This model needs to excel at delegation, task prioritization, and maintaining context across multiple concurrent operations.

    Effective manager LLMs require strong reasoning capabilities to make good delegation decisions, consistent performance to ensure predictable coordination, and excellent context management to track the state of multiple agents simultaneously. The model needs to understand the capabilities and limitations of different agents while optimizing task allocation for efficiency and quality.

    Cost considerations are particularly important for manager LLMs since they're involved in every operation. The model needs to provide sufficient capability for effective coordination while remaining cost-effective for frequent use. This often means finding models that offer good reasoning capabilities without the premium pricing of the most sophisticated options.
  </Tab>

  <Tab title="Function Calling LLM">
    Function calling LLMs handle tool usage across all agents, making them critical for crews that rely heavily on external tools and APIs. These models need to excel at understanding tool capabilities, extracting parameters accurately, and handling tool responses effectively.

    The most important characteristics for function calling LLMs are precision and reliability rather than creativity or sophisticated reasoning. The model needs to consistently extract the correct parameters from natural language requests and handle tool responses appropriately. Speed is also important since tool usage often involves multiple round trips that can impact overall performance.

    Many teams find that specialized function calling models or general purpose models with strong tool support work better than creative or reasoning-focused models for this role. The key is ensuring that the model can reliably bridge the gap between natural language instructions and structured tool calls.
  </Tab>

  <Tab title="Agent-Specific Overrides">
    Individual agents can override crew-level LLM settings when their specific needs differ significantly from the general crew requirements. This capability allows for fine-tuned optimization while maintaining operational simplicity for most agents.

    Consider agent-specific overrides when an agent's role requires capabilities that differ substantially from other crew members. For example, a creative writing agent might benefit from a model optimized for content generation, while a data analysis agent might perform better with a reasoning-focused model.

    The challenge with agent-specific overrides is balancing optimization with operational complexity. Each additional model adds complexity to deployment, monitoring, and cost management. Teams should focus overrides on agents where the performance improvement justifies the additional complexity.
  </Tab>
</Tabs>


## Task Definition Framework

### a. Focus on Clarity Over Complexity

Effective task definition is often more important than model selection in determining the quality of CrewAI outputs. Well-defined tasks provide clear direction and context that enable even modest models to perform well, while poorly defined tasks can cause even sophisticated models to produce unsatisfactory results.

<AccordionGroup>
  <Accordion title="Effective Task Descriptions" icon="list-check">
    The best task descriptions strike a balance between providing sufficient detail and maintaining clarity. They should define the specific objective clearly enough that there's no ambiguity about what success looks like, while explaining the approach or methodology in enough detail that the agent understands how to proceed.

    Effective task descriptions include relevant context and constraints that help the agent understand the broader purpose and any limitations they need to work within. They break complex work into focused steps that can be executed systematically, rather than presenting overwhelming, multi-faceted objectives that are difficult to approach systematically.

    Common mistakes include being too vague about objectives, failing to provide necessary context, setting unclear success criteria, or combining multiple unrelated tasks into a single description. The goal is to provide enough information for the agent to succeed while maintaining focus on a single, clear objective.
  </Accordion>

  <Accordion title="Expected Output Guidelines" icon="bullseye">
    Expected output guidelines serve as a contract between the task definition and the agent, clearly specifying what the deliverable should look like and how it will be evaluated. These guidelines should describe both the format and structure needed, as well as the key elements that must be included for the output to be considered complete.

    The best output guidelines provide concrete examples of quality indicators and define completion criteria clearly enough that both the agent and human reviewers can assess whether the task has been completed successfully. This reduces ambiguity and helps ensure consistent results across multiple task executions.

    Avoid generic output descriptions that could apply to any task, missing format specifications that leave agents guessing about structure, unclear quality standards that make evaluation difficult, or failing to provide examples or templates that help agents understand expectations.
  </Accordion>
</AccordionGroup>

### b. Task Sequencing Strategy

<Tabs>
  <Tab title="Sequential Dependencies">
    Sequential task dependencies are essential when tasks build upon previous outputs, information flows from one task to another, or quality depends on the completion of prerequisite work. This approach ensures that each task has access to the information and context it needs to succeed.

    Implementing sequential dependencies effectively requires using the context parameter to chain related tasks, building complexity gradually through task progression, and ensuring that each task produces outputs that serve as meaningful inputs for subsequent tasks. The goal is to maintain logical flow between dependent tasks while avoiding unnecessary bottlenecks.

    Sequential dependencies work best when there's a clear logical progression from one task to another and when the output of one task genuinely improves the quality or feasibility of subsequent tasks. However, they can create bottlenecks if not managed carefully, so it's important to identify which dependencies are truly necessary versus those that are merely convenient.
  </Tab>

  <Tab title="Parallel Execution">
    Parallel execution becomes valuable when tasks are independent of each other, time efficiency is important, or different expertise areas are involved that don't require coordination. This approach can significantly reduce overall execution time while allowing specialized agents to work on their areas of strength simultaneously.

    Successful parallel execution requires identifying tasks that can truly run independently, grouping related but separate work streams effectively, and planning for result integration when parallel tasks need to be combined into a final deliverable. The key is ensuring that parallel tasks don't create conflicts or redundancies that reduce overall quality.

    Consider parallel execution when you have multiple independent research streams, different types of analysis that don't depend on each other, or content creation tasks that can be developed simultaneously. However, be mindful of resource allocation and ensure that parallel execution doesn't overwhelm your available model capacity or budget.
  </Tab>
</Tabs>


## Optimizing Agent Configuration for LLM Performance

### a. Role-Driven LLM Selection

<Warning>
  Generic agent roles make it impossible to select the right LLM. Specific roles enable targeted model optimization.
</Warning>

The specificity of your agent roles directly determines which LLM capabilities matter most for optimal performance. This creates a strategic opportunity to match precise model strengths with agent responsibilities.

**Generic vs. Specific Role Impact on LLM Choice:**

When defining roles, think about the specific domain knowledge, working style, and decision-making frameworks that would be most valuable for the tasks the agent will handle. The more specific and contextual the role definition, the better the model can embody that role effectively.

```python  theme={null}

# ✅ Specific role - clear LLM requirements
specific_agent = Agent(
    role="SaaS Revenue Operations Analyst",  # Clear domain expertise needed
    goal="Analyze recurring revenue metrics and identify growth opportunities",
    backstory="Specialist in SaaS business models with deep understanding of ARR, churn, and expansion revenue",
    llm=LLM(model="gpt-4o")  # Reasoning model justified for complex analysis
)
```

**Role-to-Model Mapping Strategy:**

* **"Research Analyst"** → Reasoning model (GPT-4o, Claude Sonnet) for complex analysis
* **"Content Editor"** → Creative model (Claude, GPT-4o) for writing quality
* **"Data Processor"** → Efficient model (GPT-4o-mini, Gemini Flash) for structured tasks
* **"API Coordinator"** → Function-calling optimized model (GPT-4o, Claude) for tool usage

### b. Backstory as Model Context Amplifier

<Info>
  Strategic backstories multiply your chosen LLM's effectiveness by providing domain-specific context that generic prompting cannot achieve.
</Info>

A well-crafted backstory transforms your LLM choice from generic capability to specialized expertise. This is especially crucial for cost optimization - a well-contextualized efficient model can outperform a premium model without proper context.

**Context-Driven Performance Example:**

```python  theme={null}

# Context amplifies model effectiveness
domain_expert = Agent(
    role="B2B SaaS Marketing Strategist",
    goal="Develop comprehensive go-to-market strategies for enterprise software",
    backstory="""
    You have 10+ years of experience scaling B2B SaaS companies from Series A to IPO.
    You understand the nuances of enterprise sales cycles, the importance of product-market
    fit in different verticals, and how to balance growth metrics with unit economics.
    You've worked with companies like Salesforce, HubSpot, and emerging unicorns, giving
    you perspective on both established and disruptive go-to-market strategies.
    """,
    llm=LLM(model="claude-3-5-sonnet", temperature=0.3)  # Balanced creativity with domain knowledge
)


# This context enables Claude to perform like a domain expert

# Without it, even it would produce generic marketing advice
```

**Backstory Elements That Enhance LLM Performance:**

* **Domain Experience**: "10+ years in enterprise SaaS sales"
* **Specific Expertise**: "Specializes in technical due diligence for Series B+ rounds"
* **Working Style**: "Prefers data-driven decisions with clear documentation"
* **Quality Standards**: "Insists on citing sources and showing analytical work"

### c. Holistic Agent-LLM Optimization

The most effective agent configurations create synergy between role specificity, backstory depth, and LLM selection. Each element reinforces the others to maximize model performance.

**Optimization Framework:**

```python  theme={null}

# Example: Technical Documentation Agent
tech_writer = Agent(
    role="API Documentation Specialist",  # Specific role for clear LLM requirements
    goal="Create comprehensive, developer-friendly API documentation",
    backstory="""
    You're a technical writer with 8+ years documenting REST APIs, GraphQL endpoints,
    and SDK integration guides. You've worked with developer tools companies and
    understand what developers need: clear examples, comprehensive error handling,
    and practical use cases. You prioritize accuracy and usability over marketing fluff.
    """,
    llm=LLM(
        model="claude-3-5-sonnet",  # Excellent for technical writing
        temperature=0.1  # Low temperature for accuracy
    ),
    tools=[code_analyzer_tool, api_scanner_tool],
    verbose=True
)
```

**Alignment Checklist:**

* ✅ **Role Specificity**: Clear domain and responsibilities
* ✅ **LLM Match**: Model strengths align with role requirements
* ✅ **Backstory Depth**: Provides domain context the LLM can leverage
* ✅ **Tool Integration**: Tools support the agent's specialized function
* ✅ **Parameter Tuning**: Temperature and settings optimize for role needs

The key is creating agents where every configuration choice reinforces your LLM selection strategy, maximizing performance while optimizing costs.


## Practical Implementation Checklist

Rather than repeating the strategic framework, here's a tactical checklist for implementing your LLM selection decisions in CrewAI:

<Steps>
  <Step title="Audit Your Current Setup" icon="clipboard-check">
    **What to Review:**

    * Are all agents using the same LLM by default?
    * Which agents handle the most complex reasoning tasks?
    * Which agents primarily do data processing or formatting?
    * Are any agents heavily tool-dependent?

    **Action**: Document current agent roles and identify optimization opportunities.
  </Step>

  <Step title="Implement Crew-Level Strategy" icon="users-gear">
    **Set Your Baseline:**

    ```python  theme={null}
    # Start with a reliable default for the crew
    default_crew_llm = LLM(model="gpt-4o-mini")  # Cost-effective baseline

    crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True
    )
    ```

    **Action**: Establish your crew's default LLM before optimizing individual agents.
  </Step>

  <Step title="Optimize High-Impact Agents" icon="star">
    **Identify and Upgrade Key Agents:**

    ```python  theme={null}
    # Manager or coordination agents
    manager_agent = Agent(
        role="Project Manager",
        llm=LLM(model="gemini-2.5-flash-preview-05-20"),  # Premium for coordination
        # ... rest of config
    )

    # Creative or customer-facing agents
    content_agent = Agent(
        role="Content Creator",
        llm=LLM(model="claude-3-5-sonnet"),  # Best for writing
        # ... rest of config
    )
    ```

    **Action**: Upgrade 20% of your agents that handle 80% of the complexity.
  </Step>

  <Step title="Validate with Enterprise Testing" icon="test-tube">
    **Once you deploy your agents to production:**

    * Use [CrewAI AMP platform](https://app.crewai.com) to A/B test your model selections
    * Run multiple iterations with real inputs to measure consistency and performance
    * Compare cost vs. performance across your optimized setup
    * Share results with your team for collaborative decision-making

    **Action**: Replace guesswork with data-driven validation using the testing platform.
  </Step>
</Steps>

### When to Use Different Model Types

<Tabs>
  <Tab title="Reasoning Models">
    Reasoning models become essential when tasks require genuine multi-step logical thinking, strategic planning, or high-level decision making that benefits from systematic analysis. These models excel when problems need to be broken down into components and analyzed systematically rather than handled through pattern matching or simple instruction following.

    Consider reasoning models for business strategy development, complex data analysis that requires drawing insights from multiple sources, multi-step problem solving where each step depends on previous analysis, and strategic planning tasks that require considering multiple variables and their interactions.

    However, reasoning models often come with higher costs and slower response times, so they're best reserved for tasks where their sophisticated capabilities provide genuine value rather than being used for simple operations that don't require complex reasoning.
  </Tab>

  <Tab title="Creative Models">
    Creative models become valuable when content generation is the primary output and the quality, style, and engagement level of that content directly impact success. These models excel when writing quality and style matter significantly, creative ideation or brainstorming is needed, or brand voice and tone are important considerations.

    Use creative models for blog post writing and article creation, marketing copy that needs to engage and persuade, creative storytelling and narrative development, and brand communications where voice and tone are crucial. These models often understand nuance and context better than general purpose alternatives.

    Creative models may be less suitable for technical or analytical tasks where precision and factual accuracy are more important than engagement and style. They're best used when the creative and communicative aspects of the output are primary success factors.
  </Tab>

  <Tab title="Efficient Models">
    Efficient models are ideal for high-frequency, routine operations where speed and cost optimization are priorities. These models work best when tasks have clear, well-defined parameters and don't require sophisticated reasoning or creative capabilities.

    Consider efficient models for data processing and transformation tasks, simple formatting and organization operations, function calling and tool usage where precision matters more than sophistication, and high-volume operations where cost per operation is a significant factor.

    The key with efficient models is ensuring that their capabilities align with task requirements. They can handle many routine operations effectively but may struggle with tasks requiring nuanced understanding, complex reasoning, or sophisticated content generation.
  </Tab>

  <Tab title="Open Source Models">
    Open source models become attractive when budget constraints are significant, data privacy requirements exist, customization needs are important, or local deployment is required for operational or compliance reasons.

    Consider open source models for internal company tools where data privacy is paramount, privacy-sensitive applications that can't use external APIs, cost-optimized deployments where per-token pricing is prohibitive, and situations requiring custom model modifications or fine-tuning.

    However, open source models require more technical expertise to deploy and maintain effectively. Consider the total cost of ownership including infrastructure, technical overhead, and ongoing maintenance when evaluating open source options.
  </Tab>
</Tabs>


## Common CrewAI Model Selection Pitfalls

<AccordionGroup>
  <Accordion title="The 'One Model Fits All' Trap" icon="triangle-exclamation">
    **The Problem**: Using the same LLM for all agents in a crew, regardless of their specific roles and responsibilities. This is often the default approach but rarely optimal.

    **Real Example**: Using GPT-4o for both a strategic planning manager and a data extraction agent. The manager needs reasoning capabilities worth the premium cost, but the data extractor could perform just as well with GPT-4o-mini at a fraction of the price.

    **CrewAI Solution**: Leverage agent-specific LLM configuration to match model capabilities with agent roles:

    ```python  theme={null}
    # Strategic agent gets premium model
    manager = Agent(role="Strategy Manager", llm=LLM(model="gpt-4o"))

    # Processing agent gets efficient model
    processor = Agent(role="Data Processor", llm=LLM(model="gpt-4o-mini"))
    ```
  </Accordion>

  <Accordion title="Ignoring Crew-Level vs Agent-Level LLM Hierarchy" icon="shuffle">
    **The Problem**: Not understanding how CrewAI's LLM hierarchy works - crew LLM, manager LLM, and agent LLM settings can conflict or be poorly coordinated.

    **Real Example**: Setting a crew to use Claude, but having agents configured with GPT models, creating inconsistent behavior and unnecessary model switching overhead.

    **CrewAI Solution**: Plan your LLM hierarchy strategically:

    ```python  theme={null}
    crew = Crew(
        agents=[agent1, agent2],
        tasks=[task1, task2],
        manager_llm=LLM(model="gpt-4o"),  # For crew coordination
        process=Process.hierarchical  # When using manager_llm
    )

    # Agents inherit crew LLM unless specifically overridden
    agent1 = Agent(llm=LLM(model="claude-3-5-sonnet"))  # Override for specific needs
    ```
  </Accordion>

  <Accordion title="Function Calling Model Mismatch" icon="screwdriver-wrench">
    **The Problem**: Choosing models based on general capabilities while ignoring function calling performance for tool-heavy CrewAI workflows.

    **Real Example**: Selecting a creative-focused model for an agent that primarily needs to call APIs, search tools, or process structured data. The agent struggles with tool parameter extraction and reliable function calls.

    **CrewAI Solution**: Prioritize function calling capabilities for tool-heavy agents:

    ```python  theme={null}
    # For agents that use many tools
    tool_agent = Agent(
        role="API Integration Specialist",
        tools=[search_tool, api_tool, data_tool],
        llm=LLM(model="gpt-4o"),  # Excellent function calling
        # OR
        llm=LLM(model="claude-3-5-sonnet")  # Also strong with tools
    )
    ```
  </Accordion>

  <Accordion title="Premature Optimization Without Testing" icon="gear">
    **The Problem**: Making complex model selection decisions based on theoretical performance without validating with actual CrewAI workflows and tasks.

    **Real Example**: Implementing elaborate model switching logic based on task types without testing if the performance gains justify the operational complexity.

    **CrewAI Solution**: Start simple, then optimize based on real performance data:

    ```python  theme={null}
    # Start with this
    crew = Crew(agents=[...], tasks=[...], llm=LLM(model="gpt-4o-mini"))

    # Test performance, then optimize specific agents as needed
    # Use Enterprise platform testing to validate improvements
    ```
  </Accordion>

  <Accordion title="Overlooking Context and Memory Limitations" icon="brain">
    **The Problem**: Not considering how model context windows interact with CrewAI's memory and context sharing between agents.

    **Real Example**: Using a short-context model for agents that need to maintain conversation history across multiple task iterations, or in crews with extensive agent-to-agent communication.

    **CrewAI Solution**: Match context capabilities to crew communication patterns.
  </Accordion>
</AccordionGroup>


## Testing and Iteration Strategy

<Steps>
  <Step title="Start Simple" icon="play">
    Begin with reliable, general-purpose models that are well-understood and widely supported. This provides a stable foundation for understanding your specific requirements and performance expectations before optimizing for specialized needs.
  </Step>

  <Step title="Measure What Matters" icon="chart-line">
    Develop metrics that align with your specific use case and business requirements rather than relying solely on general benchmarks. Focus on measuring outcomes that directly impact your success rather than theoretical performance indicators.
  </Step>

  <Step title="Iterate Based on Results" icon="arrows-rotate">
    Make model changes based on observed performance in your specific context rather than theoretical considerations or general recommendations. Real-world performance often differs significantly from benchmark results or general reputation.
  </Step>

  <Step title="Consider Total Cost" icon="calculator">
    Evaluate the complete cost of ownership including model costs, development time, maintenance overhead, and operational complexity. The cheapest model per token may not be the most cost-effective choice when considering all factors.
  </Step>
</Steps>

<Tip>
  Focus on understanding your requirements first, then select models that best match those needs. The best LLM choice is the one that consistently delivers the results you need within your operational constraints.
</Tip>

### Enterprise-Grade Model Validation

For teams serious about optimizing their LLM selection, the **CrewAI AMP platform** provides sophisticated testing capabilities that go far beyond basic CLI testing. The platform enables comprehensive model evaluation that helps you make data-driven decisions about your LLM strategy.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=08580e93186b6563adca8b75da805805" alt="Enterprise Testing Interface" data-og-width="2238" width="2238" data-og-height="1700" height="1700" data-path="images/enterprise/enterprise-testing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d7ced6158ec4dd0b5a9928edcfc4a38d 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=0bf0f3d7110c1ac4ae4139a80e28b9c2 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=27a38bf115431233bfb9849629dc125e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5d73aad5c4af3e62a82044f80add8ac1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a91a7198392462683371a28e799943a0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise-testing.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78aaf8869525c5633d5f06655cc46c5e 2500w" />
</Frame>

**Advanced Testing Features:**

* **Multi-Model Comparison**: Test multiple LLMs simultaneously across the same tasks and inputs. Compare performance between GPT-4o, Claude, Llama, Groq, Cerebras, and other leading models in parallel to identify the best fit for your specific use case.

* **Statistical Rigor**: Configure multiple iterations with consistent inputs to measure reliability and performance variance. This helps identify models that not only perform well but do so consistently across runs.

* **Real-World Validation**: Use your actual crew inputs and scenarios rather than synthetic benchmarks. The platform allows you to test with your specific industry context, company information, and real use cases for more accurate evaluation.

* **Comprehensive Analytics**: Access detailed performance metrics, execution times, and cost analysis across all tested models. This enables data-driven decision making rather than relying on general model reputation or theoretical capabilities.

* **Team Collaboration**: Share testing results and model performance data across your team, enabling collaborative decision-making and consistent model selection strategies across projects.

Go to [app.crewai.com](https://app.crewai.com) to get started!

<Info>
  The Enterprise platform transforms model selection from guesswork into a data-driven process, enabling you to validate the principles in this guide with your actual use cases and requirements.
</Info>


## Key Principles Summary

<CardGroup cols={2}>
  <Card title="Task-Driven Selection" icon="bullseye">
    Choose models based on what the task actually requires, not theoretical capabilities or general reputation.
  </Card>

  <Card title="Capability Matching" icon="puzzle-piece">
    Align model strengths with agent roles and responsibilities for optimal performance.
  </Card>

  <Card title="Strategic Consistency" icon="link">
    Maintain coherent model selection strategy across related components and workflows.
  </Card>

  <Card title="Practical Testing" icon="flask">
    Validate choices through real-world usage rather than benchmarks alone.
  </Card>

  <Card title="Iterative Improvement" icon="arrow-up">
    Start simple and optimize based on actual performance and needs.
  </Card>

  <Card title="Operational Balance" icon="scale-balanced">
    Balance performance requirements with cost and complexity constraints.
  </Card>
</CardGroup>

<Check>
  Remember: The best LLM choice is the one that consistently delivers the results you need within your operational constraints. Focus on understanding your requirements first, then select models that best match those needs.
</Check>


## Current Model Landscape (June 2025)

<Warning>
  **Snapshot in Time**: The following model rankings represent current leaderboard standings as of June 2025, compiled from [LMSys Arena](https://arena.lmsys.org/), [Artificial Analysis](https://artificialanalysis.ai/), and other leading benchmarks. LLM performance, availability, and pricing change rapidly. Always conduct your own evaluations with your specific use cases and data.
</Warning>

### Leading Models by Category

The tables below show a representative sample of current top-performing models across different categories, with guidance on their suitability for CrewAI agents:

<Note>
  These tables/metrics showcase selected leading models in each category and are not exhaustive. Many excellent models exist beyond those listed here. The goal is to illustrate the types of capabilities to look for rather than provide a complete catalog.
</Note>

<Tabs>
  <Tab title="Reasoning & Planning">
    **Best for Manager LLMs and Complex Analysis**

    | Model                      | Intelligence Score | Cost (\$/M tokens) | Speed    | Best Use in CrewAI                                  |
    | :------------------------- | :----------------- | :----------------- | :------- | :-------------------------------------------------- |
    | **o3**                     | 70                 | \$17.50            | Fast     | Manager LLM for complex multi-agent coordination    |
    | **Gemini 2.5 Pro**         | 69                 | \$3.44             | Fast     | Strategic planning agents, research coordination    |
    | **DeepSeek R1**            | 68                 | \$0.96             | Moderate | Cost-effective reasoning for budget-conscious crews |
    | **Claude 4 Sonnet**        | 53                 | \$6.00             | Fast     | Analysis agents requiring nuanced understanding     |
    | **Qwen3 235B (Reasoning)** | 62                 | \$2.63             | Moderate | Open-source alternative for reasoning tasks         |

    These models excel at multi-step reasoning and are ideal for agents that need to develop strategies, coordinate other agents, or analyze complex information.
  </Tab>

  <Tab title="Coding & Technical">
    **Best for Development and Tool-Heavy Workflows**

    | Model                 | Coding Performance | Tool Use Score | Cost (\$/M tokens) | Best Use in CrewAI                            |
    | :-------------------- | :----------------- | :------------- | :----------------- | :-------------------------------------------- |
    | **Claude 4 Sonnet**   | Excellent          | 72.7%          | \$6.00             | Primary coding agent, technical documentation |
    | **Claude 4 Opus**     | Excellent          | 72.5%          | \$30.00            | Complex software architecture, code review    |
    | **DeepSeek V3**       | Very Good          | High           | \$0.48             | Cost-effective coding for routine development |
    | **Qwen2.5 Coder 32B** | Very Good          | Medium         | \$0.15             | Budget-friendly coding agent                  |
    | **Llama 3.1 405B**    | Good               | 81.1%          | \$3.50             | Function calling LLM for tool-heavy workflows |

    These models are optimized for code generation, debugging, and technical problem-solving, making them ideal for development-focused crews.
  </Tab>

  <Tab title="Speed & Efficiency">
    **Best for High-Throughput and Real-Time Applications**

    | Model                   | Speed (tokens/s) | Latency (TTFT) | Cost (\$/M tokens) | Best Use in CrewAI                   |
    | :---------------------- | :--------------- | :------------- | :----------------- | :----------------------------------- |
    | **Llama 4 Scout**       | 2,600            | 0.33s          | \$0.27             | High-volume processing agents        |
    | **Gemini 2.5 Flash**    | 376              | 0.30s          | \$0.26             | Real-time response agents            |
    | **DeepSeek R1 Distill** | 383              | Variable       | \$0.04             | Cost-optimized high-speed processing |
    | **Llama 3.3 70B**       | 2,500            | 0.52s          | \$0.60             | Balanced speed and capability        |
    | **Nova Micro**          | High             | 0.30s          | \$0.04             | Simple, fast task execution          |

    These models prioritize speed and efficiency, perfect for agents handling routine operations or requiring quick responses. **Pro tip**: Pairing these models with fast inference providers like Groq can achieve even better performance, especially for open-source models like Llama.
  </Tab>

  <Tab title="Balanced Performance">
    **Best All-Around Models for General Crews**

    | Model                 | Overall Score | Versatility | Cost (\$/M tokens) | Best Use in CrewAI                |
    | :-------------------- | :------------ | :---------- | :----------------- | :-------------------------------- |
    | **GPT-4.1**           | 53            | Excellent   | \$3.50             | General-purpose crew LLM          |
    | **Claude 3.7 Sonnet** | 48            | Very Good   | \$6.00             | Balanced reasoning and creativity |
    | **Gemini 2.0 Flash**  | 48            | Good        | \$0.17             | Cost-effective general use        |
    | **Llama 4 Maverick**  | 51            | Good        | \$0.37             | Open-source general purpose       |
    | **Qwen3 32B**         | 44            | Good        | \$1.23             | Budget-friendly versatility       |

    These models offer good performance across multiple dimensions, suitable for crews with diverse task requirements.
  </Tab>
</Tabs>

### Selection Framework for Current Models

<AccordionGroup>
  <Accordion title="High-Performance Crews" icon="rocket">
    **When performance is the priority**: Use top-tier models like **o3**, **Gemini 2.5 Pro**, or **Claude 4 Sonnet** for manager LLMs and critical agents. These models excel at complex reasoning and coordination but come with higher costs.

    **Strategy**: Implement a multi-model approach where premium models handle strategic thinking while efficient models handle routine operations.
  </Accordion>

  <Accordion title="Cost-Conscious Crews" icon="dollar-sign">
    **When budget is a primary constraint**: Focus on models like **DeepSeek R1**, **Llama 4 Scout**, or **Gemini 2.0 Flash**. These provide strong performance at significantly lower costs.

    **Strategy**: Use cost-effective models for most agents, reserving premium models only for the most critical decision-making roles.
  </Accordion>

  <Accordion title="Specialized Workflows" icon="screwdriver-wrench">
    **For specific domain expertise**: Choose models optimized for your primary use case. **Claude 4** series for coding, **Gemini 2.5 Pro** for research, **Llama 405B** for function calling.

    **Strategy**: Select models based on your crew's primary function, ensuring the core capability aligns with model strengths.
  </Accordion>

  <Accordion title="Enterprise & Privacy" icon="shield">
    **For data-sensitive operations**: Consider open-source models like **Llama 4** series, **DeepSeek V3**, or **Qwen3** that can be deployed locally while maintaining competitive performance.

    **Strategy**: Deploy open-source models on private infrastructure, accepting potential performance trade-offs for data control.
  </Accordion>
</AccordionGroup>

### Key Considerations for Model Selection

* **Performance Trends**: The current landscape shows strong competition between reasoning-focused models (o3, Gemini 2.5 Pro) and balanced models (Claude 4, GPT-4.1). Specialized models like DeepSeek R1 offer excellent cost-performance ratios.

* **Speed vs. Intelligence Trade-offs**: Models like Llama 4 Scout prioritize speed (2,600 tokens/s) while maintaining reasonable intelligence, whereas models like o3 maximize reasoning capability at the cost of speed and price.

* **Open Source Viability**: The gap between open-source and proprietary models continues to narrow, with models like Llama 4 Maverick and DeepSeek V3 offering competitive performance at attractive price points. Fast inference providers particularly shine with open-source models, often delivering better speed-to-cost ratios than proprietary alternatives.

<Info>
  **Testing is Essential**: Leaderboard rankings provide general guidance, but your specific use case, prompting style, and evaluation criteria may produce different results. Always test candidate models with your actual tasks and data before making final decisions.
</Info>

### Practical Implementation Strategy

<Steps>
  <Step title="Start with Proven Models">
    Begin with well-established models like **GPT-4.1**, **Claude 3.7 Sonnet**, or **Gemini 2.0 Flash** that offer good performance across multiple dimensions and have extensive real-world validation.
  </Step>

  <Step title="Identify Specialized Needs">
    Determine if your crew has specific requirements (coding, reasoning, speed) that would benefit from specialized models like **Claude 4 Sonnet** for development or **o3** for complex analysis. For speed-critical applications, consider fast inference providers like **Groq** alongside model selection.
  </Step>

  <Step title="Implement Multi-Model Strategy">
    Use different models for different agents based on their roles. High-capability models for managers and complex tasks, efficient models for routine operations.
  </Step>

  <Step title="Monitor and Optimize">
    Track performance metrics relevant to your use case and be prepared to adjust model selections as new models are released or pricing changes.
  </Step>
</Steps>



# Using Multimodal Agents
Source: https://docs.crewai.com/en/learn/multimodal-agents

Learn how to enable and use multimodal capabilities in your agents for processing images and other non-text content within the CrewAI framework.


## Using Multimodal Agents

CrewAI supports multimodal agents that can process both text and non-text content like images. This guide will show you how to enable and use multimodal capabilities in your agents.

### Enabling Multimodal Capabilities

To create a multimodal agent, simply set the `multimodal` parameter to `True` when initializing your agent:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Image Analyst",
    goal="Analyze and extract insights from images",
    backstory="An expert in visual content interpretation with years of experience in image analysis",
    multimodal=True  # This enables multimodal capabilities
)
```

When you set `multimodal=True`, the agent is automatically configured with the necessary tools for handling non-text content, including the `AddImageTool`.

### Working with Images

The multimodal agent comes pre-configured with the `AddImageTool`, which allows it to process images. You don't need to manually add this tool - it's automatically included when you enable multimodal capabilities.

Here's a complete example showing how to use a multimodal agent to analyze an image:

```python  theme={null}
from crewai import Agent, Task, Crew


# Create a multimodal agent
image_analyst = Agent(
    role="Product Analyst",
    goal="Analyze product images and provide detailed descriptions",
    backstory="Expert in visual product analysis with deep knowledge of design and features",
    multimodal=True
)


# Create a task for image analysis
task = Task(
    description="Analyze the product image at https://example.com/product.jpg and provide a detailed description",
    expected_output="A detailed description of the product image",
    agent=image_analyst
)


# Create and run the crew
crew = Crew(
    agents=[image_analyst],
    tasks=[task]
)

result = crew.kickoff()
```

### Advanced Usage with Context

You can provide additional context or specific questions about the image when creating tasks for multimodal agents. The task description can include specific aspects you want the agent to focus on:

```python  theme={null}
from crewai import Agent, Task, Crew


# Create a multimodal agent for detailed analysis
expert_analyst = Agent(
    role="Visual Quality Inspector",
    goal="Perform detailed quality analysis of product images",
    backstory="Senior quality control expert with expertise in visual inspection",
    multimodal=True  # AddImageTool is automatically included
)


# Create a task with specific analysis requirements
inspection_task = Task(
    description="""
    Analyze the product image at https://example.com/product.jpg with focus on:
    1. Quality of materials
    2. Manufacturing defects
    3. Compliance with standards
    Provide a detailed report highlighting any issues found.
    """,
    expected_output="A detailed report highlighting any issues found",
    agent=expert_analyst
)


# Create and run the crew
crew = Crew(
    agents=[expert_analyst],
    tasks=[inspection_task]
)

result = crew.kickoff()
```

### Tool Details

When working with multimodal agents, the `AddImageTool` is automatically configured with the following schema:

```python  theme={null}
class AddImageToolSchema:
    image_url: str  # Required: The URL or path of the image to process
    action: Optional[str] = None  # Optional: Additional context or specific questions about the image
```

The multimodal agent will automatically handle the image processing through its built-in tools, allowing it to:

* Access images via URLs or local file paths
* Process image content with optional context or specific questions
* Provide analysis and insights based on the visual information and task requirements

### Best Practices

When working with multimodal agents, keep these best practices in mind:

1. **Image Access**
   * Ensure your images are accessible via URLs that the agent can reach
   * For local images, consider hosting them temporarily or using absolute file paths
   * Verify that image URLs are valid and accessible before running tasks

2. **Task Description**
   * Be specific about what aspects of the image you want the agent to analyze
   * Include clear questions or requirements in the task description
   * Consider using the optional `action` parameter for focused analysis

3. **Resource Management**
   * Image processing may require more computational resources than text-only tasks
   * Some language models may require base64 encoding for image data
   * Consider batch processing for multiple images to optimize performance

4. **Environment Setup**
   * Verify that your environment has the necessary dependencies for image processing
   * Ensure your language model supports multimodal capabilities
   * Test with small images first to validate your setup

5. **Error Handling**
   * Implement proper error handling for image loading failures
   * Have fallback strategies for when image processing fails
   * Monitor and log image processing operations for debugging



# Overview
Source: https://docs.crewai.com/en/learn/overview

Learn how to build, customize, and optimize your CrewAI applications with comprehensive guides and tutorials


## Learn CrewAI

This section provides comprehensive guides and tutorials to help you master CrewAI, from basic concepts to advanced techniques. Whether you're just getting started or looking to optimize your existing implementations, these resources will guide you through every aspect of building powerful AI agent workflows.


## Getting Started Guides

### Core Concepts

<CardGroup cols={2}>
  <Card title="Sequential Process" icon="list-ol" href="/en/learn/sequential-process">
    Learn how to execute tasks in a sequential order for structured workflows.
  </Card>

  <Card title="Hierarchical Process" icon="sitemap" href="/en/learn/hierarchical-process">
    Implement hierarchical task execution with manager agents overseeing workflows.
  </Card>

  <Card title="Conditional Tasks" icon="code-branch" href="/en/learn/conditional-tasks">
    Create dynamic workflows with conditional task execution based on outcomes.
  </Card>

  <Card title="Async Kickoff" icon="bolt" href="/en/learn/kickoff-async">
    Execute crews asynchronously for improved performance and concurrency.
  </Card>
</CardGroup>

### Agent Development

<CardGroup cols={2}>
  <Card title="Customizing Agents" icon="user-gear" href="/en/learn/customizing-agents">
    Learn how to customize agent behavior, roles, and capabilities.
  </Card>

  <Card title="Coding Agents" icon="code" href="/en/learn/coding-agents">
    Build agents that can write, execute, and debug code automatically.
  </Card>

  <Card title="Multimodal Agents" icon="images" href="/en/learn/multimodal-agents">
    Create agents that can process text, images, and other media types.
  </Card>

  <Card title="Custom Manager Agent" icon="user-tie" href="/en/learn/custom-manager-agent">
    Implement custom manager agents for complex hierarchical workflows.
  </Card>
</CardGroup>


## Advanced Features

### Workflow Control

<CardGroup cols={2}>
  <Card title="Human in the Loop" icon="user-check" href="/en/learn/human-in-the-loop">
    Integrate human oversight and intervention into agent workflows.
  </Card>

  <Card title="Human Input on Execution" icon="hand-paper" href="/en/learn/human-input-on-execution">
    Allow human input during task execution for dynamic decision making.
  </Card>

  <Card title="Replay Tasks" icon="rotate-left" href="/en/learn/replay-tasks-from-latest-crew-kickoff">
    Replay and resume tasks from previous crew executions.
  </Card>

  <Card title="Kickoff for Each" icon="repeat" href="/en/learn/kickoff-for-each">
    Execute crews multiple times with different inputs efficiently.
  </Card>
</CardGroup>

### Customization & Integration

<CardGroup cols={2}>
  <Card title="Custom LLM" icon="brain" href="/en/learn/custom-llm">
    Integrate custom language models and providers with CrewAI.
  </Card>

  <Card title="LLM Connections" icon="link" href="/en/learn/llm-connections">
    Configure and manage connections to various LLM providers.
  </Card>

  <Card title="Create Custom Tools" icon="wrench" href="/en/learn/create-custom-tools">
    Build custom tools to extend agent capabilities.
  </Card>

  <Card title="Using Annotations" icon="at" href="/en/learn/using-annotations">
    Use Python annotations for cleaner, more maintainable code.
  </Card>
</CardGroup>


## Specialized Applications

### Content & Media

<CardGroup cols={2}>
  <Card title="DALL-E Image Generation" icon="image" href="/en/learn/dalle-image-generation">
    Generate images using DALL-E integration with your agents.
  </Card>

  <Card title="Bring Your Own Agent" icon="user-plus" href="/en/learn/bring-your-own-agent">
    Integrate existing agents and models into CrewAI workflows.
  </Card>
</CardGroup>

### Tool Management

<CardGroup cols={2}>
  <Card title="Force Tool Output as Result" icon="hammer" href="/en/learn/force-tool-output-as-result">
    Configure tools to return their output directly as task results.
  </Card>
</CardGroup>


## Learning Path Recommendations

### For Beginners

1. Start with **Sequential Process** to understand basic workflow execution
2. Learn **Customizing Agents** to create effective agent configurations
3. Explore **Create Custom Tools** to extend functionality
4. Try **Human in the Loop** for interactive workflows

### For Intermediate Users

1. Master **Hierarchical Process** for complex multi-agent systems
2. Implement **Conditional Tasks** for dynamic workflows
3. Use **Async Kickoff** for performance optimization
4. Integrate **Custom LLM** for specialized models

### For Advanced Users

1. Build **Multimodal Agents** for complex media processing
2. Create **Custom Manager Agents** for sophisticated orchestration
3. Implement **Bring Your Own Agent** for hybrid systems
4. Use **Replay Tasks** for robust error recovery


## Best Practices

### Development

* **Start Simple**: Begin with basic sequential workflows before adding complexity
* **Test Incrementally**: Test each component before integrating into larger systems
* **Use Annotations**: Leverage Python annotations for cleaner, more maintainable code
* **Custom Tools**: Build reusable tools that can be shared across different agents

### Production

* **Error Handling**: Implement robust error handling and recovery mechanisms
* **Performance**: Use async execution and optimize LLM calls for better performance
* **Monitoring**: Integrate observability tools to track agent performance
* **Human Oversight**: Include human checkpoints for critical decisions

### Optimization

* **Resource Management**: Monitor and optimize token usage and API costs
* **Workflow Design**: Design workflows that minimize unnecessary LLM calls
* **Tool Efficiency**: Create efficient tools that provide maximum value with minimal overhead
* **Iterative Improvement**: Use feedback and metrics to continuously improve agent performance


## Getting Help

* **Documentation**: Each guide includes detailed examples and explanations
* **Community**: Join the [CrewAI Forum](https://community.crewai.com) for discussions and support
* **Examples**: Check the Examples section for complete working implementations
* **Support**: Contact [support@crewai.com](mailto:support@crewai.com) for technical assistance

Start with the guides that match your current needs and gradually explore more advanced topics as you become comfortable with the fundamentals.



---

**Navigation:** [← Previous](./09-task-using-schema-based-operations.md) | [Index](./index.md) | [Next →](./11-replay-tasks-from-latest-crew-kickoff.md)
