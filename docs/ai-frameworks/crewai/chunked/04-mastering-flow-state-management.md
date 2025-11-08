# Mastering Flow State Management

**Navigation:** [← Previous](./03-srclatestaidevelopmentcrewpy.md) | [Index](./index.md) | [Next →](./05-overview.md)

---

# Mastering Flow State Management
Source: https://docs.crewai.com/en/guides/flows/mastering-flow-state

A comprehensive guide to managing, persisting, and leveraging state in CrewAI Flows for building robust AI applications.


## Understanding the Power of State in Flows

State management is the backbone of any sophisticated AI workflow. In CrewAI Flows, the state system allows you to maintain context, share data between steps, and build complex application logic. Mastering state management is essential for creating reliable, maintainable, and powerful AI applications.

This guide will walk you through everything you need to know about managing state in CrewAI Flows, from basic concepts to advanced techniques, with practical code examples along the way.

### Why State Management Matters

Effective state management enables you to:

1. **Maintain context across execution steps** - Pass information seamlessly between different stages of your workflow
2. **Build complex conditional logic** - Make decisions based on accumulated data
3. **Create persistent applications** - Save and restore workflow progress
4. **Handle errors gracefully** - Implement recovery patterns for more robust applications
5. **Scale your applications** - Support complex workflows with proper data organization
6. **Enable conversational applications** - Store and access conversation history for context-aware AI interactions

Let's explore how to leverage these capabilities effectively.


## State Management Fundamentals

### The Flow State Lifecycle

In CrewAI Flows, the state follows a predictable lifecycle:

1. **Initialization** - When a flow is created, its state is initialized (either as an empty dictionary or a Pydantic model instance)
2. **Modification** - Flow methods access and modify the state as they execute
3. **Transmission** - State is passed automatically between flow methods
4. **Persistence** (optional) - State can be saved to storage and later retrieved
5. **Completion** - The final state reflects the cumulative changes from all executed methods

Understanding this lifecycle is crucial for designing effective flows.

### Two Approaches to State Management

CrewAI offers two ways to manage state in your flows:

1. **Unstructured State** - Using dictionary-like objects for flexibility
2. **Structured State** - Using Pydantic models for type safety and validation

Let's examine each approach in detail.


## Unstructured State Management

Unstructured state uses a dictionary-like approach, offering flexibility and simplicity for straightforward applications.

### How It Works

With unstructured state:

* You access state via `self.state` which behaves like a dictionary
* You can freely add, modify, or remove keys at any point
* All state is automatically available to all flow methods

### Basic Example

Here's a simple example of unstructured state management:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start

class UnstructuredStateFlow(Flow):
    @start()
    def initialize_data(self):
        print("Initializing flow data")
        # Add key-value pairs to state
        self.state["user_name"] = "Alex"
        self.state["preferences"] = {
            "theme": "dark",
            "language": "English"
        }
        self.state["items"] = []

        # The flow state automatically gets a unique ID
        print(f"Flow ID: {self.state['id']}")

        return "Initialized"

    @listen(initialize_data)
    def process_data(self, previous_result):
        print(f"Previous step returned: {previous_result}")

        # Access and modify state
        user = self.state["user_name"]
        print(f"Processing data for {user}")

        # Add items to a list in state
        self.state["items"].append("item1")
        self.state["items"].append("item2")

        # Add a new key-value pair
        self.state["processed"] = True

        return "Processed"

    @listen(process_data)
    def generate_summary(self, previous_result):
        # Access multiple state values
        user = self.state["user_name"]
        theme = self.state["preferences"]["theme"]
        items = self.state["items"]
        processed = self.state.get("processed", False)

        summary = f"User {user} has {len(items)} items with {theme} theme. "
        summary += "Data is processed." if processed else "Data is not processed."

        return summary


# Run the flow
flow = UnstructuredStateFlow()
result = flow.kickoff()
print(f"Final result: {result}")
print(f"Final state: {flow.state}")
```

### When to Use Unstructured State

Unstructured state is ideal for:

* Quick prototyping and simple flows
* Dynamically evolving state needs
* Cases where the structure may not be known in advance
* Flows with simple state requirements

While flexible, unstructured state lacks type checking and schema validation, which can lead to errors in complex applications.


## Structured State Management

Structured state uses Pydantic models to define a schema for your flow's state, providing type safety, validation, and better developer experience.

### How It Works

With structured state:

* You define a Pydantic model that represents your state structure
* You pass this model type to your Flow class as a type parameter
* You access state via `self.state`, which behaves like a Pydantic model instance
* All fields are validated according to their defined types
* You get IDE autocompletion and type checking support

### Basic Example

Here's how to implement structured state management:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# Define your state model
class UserPreferences(BaseModel):
    theme: str = "light"
    language: str = "English"

class AppState(BaseModel):
    user_name: str = ""
    preferences: UserPreferences = UserPreferences()
    items: List[str] = []
    processed: bool = False
    completion_percentage: float = 0.0


# Create a flow with typed state
class StructuredStateFlow(Flow[AppState]):
    @start()
    def initialize_data(self):
        print("Initializing flow data")
        # Set state values (type-checked)
        self.state.user_name = "Taylor"
        self.state.preferences.theme = "dark"

        # The ID field is automatically available
        print(f"Flow ID: {self.state.id}")

        return "Initialized"

    @listen(initialize_data)
    def process_data(self, previous_result):
        print(f"Processing data for {self.state.user_name}")

        # Modify state (with type checking)
        self.state.items.append("item1")
        self.state.items.append("item2")
        self.state.processed = True
        self.state.completion_percentage = 50.0

        return "Processed"

    @listen(process_data)
    def generate_summary(self, previous_result):
        # Access state (with autocompletion)
        summary = f"User {self.state.user_name} has {len(self.state.items)} items "
        summary += f"with {self.state.preferences.theme} theme. "
        summary += "Data is processed." if self.state.processed else "Data is not processed."
        summary += f" Completion: {self.state.completion_percentage}%"

        return summary


# Run the flow
flow = StructuredStateFlow()
result = flow.kickoff()
print(f"Final result: {result}")
print(f"Final state: {flow.state}")
```

### Benefits of Structured State

Using structured state provides several advantages:

1. **Type Safety** - Catch type errors at development time
2. **Self-Documentation** - The state model clearly documents what data is available
3. **Validation** - Automatic validation of data types and constraints
4. **IDE Support** - Get autocomplete and inline documentation
5. **Default Values** - Easily define fallbacks for missing data

### When to Use Structured State

Structured state is recommended for:

* Complex flows with well-defined data schemas
* Team projects where multiple developers work on the same code
* Applications where data validation is important
* Flows that need to enforce specific data types and constraints


## The Automatic State ID

Both unstructured and structured states automatically receive a unique identifier (UUID) to help track and manage state instances.

### How It Works

* For unstructured state, the ID is accessible as `self.state["id"]`
* For structured state, the ID is accessible as `self.state.id`
* This ID is generated automatically when the flow is created
* The ID remains the same throughout the flow's lifecycle
* The ID can be used for tracking, logging, and retrieving persisted states

This UUID is particularly valuable when implementing persistence or tracking multiple flow executions.


## Dynamic State Updates

Regardless of whether you're using structured or unstructured state, you can update state dynamically throughout your flow's execution.

### Passing Data Between Steps

Flow methods can return values that are then passed as arguments to listening methods:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start

class DataPassingFlow(Flow):
    @start()
    def generate_data(self):
        # This return value will be passed to listening methods
        return "Generated data"

    @listen(generate_data)
    def process_data(self, data_from_previous_step):
        print(f"Received: {data_from_previous_step}")
        # You can modify the data and pass it along
        processed_data = f"{data_from_previous_step} - processed"
        # Also update state
        self.state["last_processed"] = processed_data
        return processed_data

    @listen(process_data)
    def finalize_data(self, processed_data):
        print(f"Received processed data: {processed_data}")
        # Access both the passed data and state
        last_processed = self.state.get("last_processed", "")
        return f"Final: {processed_data} (from state: {last_processed})"
```

This pattern allows you to combine direct data passing with state updates for maximum flexibility.


## Persisting Flow State

One of CrewAI's most powerful features is the ability to persist flow state across executions. This enables workflows that can be paused, resumed, and even recovered after failures.

### The @persist() Decorator

The `@persist()` decorator automates state persistence, saving your flow's state at key points in execution.

#### Class-Level Persistence

When applied at the class level, `@persist()` saves state after every method execution:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from crewai.flow.persistence import persist
from pydantic import BaseModel

class CounterState(BaseModel):
    value: int = 0

@persist()  # Apply to the entire flow class
class PersistentCounterFlow(Flow[CounterState]):
    @start()
    def increment(self):
        self.state.value += 1
        print(f"Incremented to {self.state.value}")
        return self.state.value

    @listen(increment)
    def double(self, value):
        self.state.value = value * 2
        print(f"Doubled to {self.state.value}")
        return self.state.value


# First run
flow1 = PersistentCounterFlow()
result1 = flow1.kickoff()
print(f"First run result: {result1}")


# Second run - state is automatically loaded
flow2 = PersistentCounterFlow()
result2 = flow2.kickoff()
print(f"Second run result: {result2}")  # Will be higher due to persisted state
```

#### Method-Level Persistence

For more granular control, you can apply `@persist()` to specific methods:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from crewai.flow.persistence import persist

class SelectivePersistFlow(Flow):
    @start()
    def first_step(self):
        self.state["count"] = 1
        return "First step"

    @persist()  # Only persist after this method
    @listen(first_step)
    def important_step(self, prev_result):
        self.state["count"] += 1
        self.state["important_data"] = "This will be persisted"
        return "Important step completed"

    @listen(important_step)
    def final_step(self, prev_result):
        self.state["count"] += 1
        return f"Complete with count {self.state['count']}"
```


## Advanced State Patterns

### Conditional starts and resumable execution

Flows support conditional `@start()` and resumable execution for HITL/cyclic scenarios:

```python  theme={null}
from crewai.flow.flow import Flow, start, listen, and_, or_

class ResumableFlow(Flow):
    @start()  # unconditional start
    def init(self):
        ...

    # Conditional start: run after "init" or external trigger name
    @start("init")
    def maybe_begin(self):
        ...

    @listen(and_(init, maybe_begin))
    def proceed(self):
        ...
```

* Conditional `@start()` accepts a method name, a router label, or a callable condition.
* During resume, listeners continue from prior checkpoints; cycle/router branches honor resumption flags.

### State-Based Conditional Logic

You can use state to implement complex conditional logic in your flows:

```python  theme={null}
from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel

class PaymentState(BaseModel):
    amount: float = 0.0
    is_approved: bool = False
    retry_count: int = 0

class PaymentFlow(Flow[PaymentState]):
    @start()
    def process_payment(self):
        # Simulate payment processing
        self.state.amount = 100.0
        self.state.is_approved = self.state.amount < 1000
        return "Payment processed"

    @router(process_payment)
    def check_approval(self, previous_result):
        if self.state.is_approved:
            return "approved"
        elif self.state.retry_count < 3:
            return "retry"
        else:
            return "rejected"

    @listen("approved")
    def handle_approval(self):
        return f"Payment of ${self.state.amount} approved!"

    @listen("retry")
    def handle_retry(self):
        self.state.retry_count += 1
        print(f"Retrying payment (attempt {self.state.retry_count})...")
        # Could implement retry logic here
        return "Retry initiated"

    @listen("rejected")
    def handle_rejection(self):
        return f"Payment of ${self.state.amount} rejected after {self.state.retry_count} retries."
```

### Handling Complex State Transformations

For complex state transformations, you can create dedicated methods:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from typing import List, Dict

class UserData(BaseModel):
    name: str
    active: bool = True
    login_count: int = 0

class ComplexState(BaseModel):
    users: Dict[str, UserData] = {}
    active_user_count: int = 0

class TransformationFlow(Flow[ComplexState]):
    @start()
    def initialize(self):
        # Add some users
        self.add_user("alice", "Alice")
        self.add_user("bob", "Bob")
        self.add_user("charlie", "Charlie")
        return "Initialized"

    @listen(initialize)
    def process_users(self, _):
        # Increment login counts
        for user_id in self.state.users:
            self.increment_login(user_id)

        # Deactivate one user
        self.deactivate_user("bob")

        # Update active count
        self.update_active_count()

        return f"Processed {len(self.state.users)} users"

    # Helper methods for state transformations
    def add_user(self, user_id: str, name: str):
        self.state.users[user_id] = UserData(name=name)
        self.update_active_count()

    def increment_login(self, user_id: str):
        if user_id in self.state.users:
            self.state.users[user_id].login_count += 1

    def deactivate_user(self, user_id: str):
        if user_id in self.state.users:
            self.state.users[user_id].active = False
            self.update_active_count()

    def update_active_count(self):
        self.state.active_user_count = sum(
            1 for user in self.state.users.values() if user.active
        )
```

This pattern of creating helper methods keeps your flow methods clean while enabling complex state manipulations.


## State Management with Crews

One of the most powerful patterns in CrewAI is combining flow state management with crew execution.

### Passing State to Crews

You can use flow state to parameterize crews:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel

class ResearchState(BaseModel):
    topic: str = ""
    depth: str = "medium"
    results: str = ""

class ResearchFlow(Flow[ResearchState]):
    @start()
    def get_parameters(self):
        # In a real app, this might come from user input
        self.state.topic = "Artificial Intelligence Ethics"
        self.state.depth = "deep"
        return "Parameters set"

    @listen(get_parameters)
    def execute_research(self, _):
        # Create agents
        researcher = Agent(
            role="Research Specialist",
            goal=f"Research {self.state.topic} in {self.state.depth} detail",
            backstory="You are an expert researcher with a talent for finding accurate information."
        )

        writer = Agent(
            role="Content Writer",
            goal="Transform research into clear, engaging content",
            backstory="You excel at communicating complex ideas clearly and concisely."
        )

        # Create tasks
        research_task = Task(
            description=f"Research {self.state.topic} with {self.state.depth} analysis",
            expected_output="Comprehensive research notes in markdown format",
            agent=researcher
        )

        writing_task = Task(
            description=f"Create a summary on {self.state.topic} based on the research",
            expected_output="Well-written article in markdown format",
            agent=writer,
            context=[research_task]
        )

        # Create and run crew
        research_crew = Crew(
            agents=[researcher, writer],
            tasks=[research_task, writing_task],
            process=Process.sequential,
            verbose=True
        )

        # Run crew and store result in state
        result = research_crew.kickoff()
        self.state.results = result.raw

        return "Research completed"

    @listen(execute_research)
    def summarize_results(self, _):
        # Access the stored results
        result_length = len(self.state.results)
        return f"Research on {self.state.topic} completed with {result_length} characters of results."
```

### Handling Crew Outputs in State

When a crew completes, you can process its output and store it in your flow state:

```python  theme={null}
@listen(execute_crew)
def process_crew_results(self, _):
    # Parse the raw results (assuming JSON output)
    import json
    try:
        results_dict = json.loads(self.state.raw_results)
        self.state.processed_results = {
            "title": results_dict.get("title", ""),
            "main_points": results_dict.get("main_points", []),
            "conclusion": results_dict.get("conclusion", "")
        }
        return "Results processed successfully"
    except json.JSONDecodeError:
        self.state.error = "Failed to parse crew results as JSON"
        return "Error processing results"
```


## Best Practices for State Management

### 1. Keep State Focused

Design your state to contain only what's necessary:

```python  theme={null}

# Too broad
class BloatedState(BaseModel):
    user_data: Dict = {}
    system_settings: Dict = {}
    temporary_calculations: List = []
    debug_info: Dict = {}
    # ...many more fields


# Better: Focused state
class FocusedState(BaseModel):
    user_id: str
    preferences: Dict[str, str]
    completion_status: Dict[str, bool]
```

### 2. Use Structured State for Complex Flows

As your flows grow in complexity, structured state becomes increasingly valuable:

```python  theme={null}

# Simple flow can use unstructured state
class SimpleGreetingFlow(Flow):
    @start()
    def greet(self):
        self.state["name"] = "World"
        return f"Hello, {self.state['name']}!"


# Complex flow benefits from structured state
class UserRegistrationState(BaseModel):
    username: str
    email: str
    verification_status: bool = False
    registration_date: datetime = Field(default_factory=datetime.now)
    last_login: Optional[datetime] = None

class RegistrationFlow(Flow[UserRegistrationState]):
    # Methods with strongly-typed state access
```

### 3. Document State Transitions

For complex flows, document how state changes throughout the execution:

```python  theme={null}
@start()
def initialize_order(self):
    """
    Initialize order state with empty values.

    State before: {}
    State after: {order_id: str, items: [], status: 'new'}
    """
    self.state.order_id = str(uuid.uuid4())
    self.state.items = []
    self.state.status = "new"
    return "Order initialized"
```

### 4. Handle State Errors Gracefully

Implement error handling for state access:

```python  theme={null}
@listen(previous_step)
def process_data(self, _):
    try:
        # Try to access a value that might not exist
        user_preference = self.state.preferences.get("theme", "default")
    except (AttributeError, KeyError):
        # Handle the error gracefully
        self.state.errors = self.state.get("errors", [])
        self.state.errors.append("Failed to access preferences")
        user_preference = "default"

    return f"Used preference: {user_preference}"
```

### 5. Use State for Progress Tracking

Leverage state to track progress in long-running flows:

```python  theme={null}
class ProgressTrackingFlow(Flow):
    @start()
    def initialize(self):
        self.state["total_steps"] = 3
        self.state["current_step"] = 0
        self.state["progress"] = 0.0
        self.update_progress()
        return "Initialized"

    def update_progress(self):
        """Helper method to calculate and update progress"""
        if self.state.get("total_steps", 0) > 0:
            self.state["progress"] = (self.state.get("current_step", 0) /
                                    self.state["total_steps"]) * 100
            print(f"Progress: {self.state['progress']:.1f}%")

    @listen(initialize)
    def step_one(self, _):
        # Do work...
        self.state["current_step"] = 1
        self.update_progress()
        return "Step 1 complete"

    # Additional steps...
```

### 6. Use Immutable Operations When Possible

Especially with structured state, prefer immutable operations for clarity:

```python  theme={null}

# Instead of modifying lists in place:
self.state.items.append(new_item)  # Mutable operation


# Consider creating new state:
from pydantic import BaseModel
from typing import List

class ItemState(BaseModel):
    items: List[str] = []

class ImmutableFlow(Flow[ItemState]):
    @start()
    def add_item(self):
        # Create new list with the added item
        self.state.items = [*self.state.items, "new item"]
        return "Item added"
```


## Debugging Flow State

### Logging State Changes

When developing, add logging to track state changes:

```python  theme={null}
import logging
logging.basicConfig(level=logging.INFO)

class LoggingFlow(Flow):
    def log_state(self, step_name):
        logging.info(f"State after {step_name}: {self.state}")

    @start()
    def initialize(self):
        self.state["counter"] = 0
        self.log_state("initialize")
        return "Initialized"

    @listen(initialize)
    def increment(self, _):
        self.state["counter"] += 1
        self.log_state("increment")
        return f"Incremented to {self.state['counter']}"
```

### State Visualization

You can add methods to visualize your state for debugging:

```python  theme={null}
def visualize_state(self):
    """Create a simple visualization of the current state"""
    import json
    from rich.console import Console
    from rich.panel import Panel

    console = Console()

    if hasattr(self.state, "model_dump"):
        # Pydantic v2
        state_dict = self.state.model_dump()
    elif hasattr(self.state, "dict"):
        # Pydantic v1
        state_dict = self.state.dict()
    else:
        # Unstructured state
        state_dict = dict(self.state)

    # Remove id for cleaner output
    if "id" in state_dict:
        state_dict.pop("id")

    state_json = json.dumps(state_dict, indent=2, default=str)
    console.print(Panel(state_json, title="Current Flow State"))
```


## Conclusion

Mastering state management in CrewAI Flows gives you the power to build sophisticated, robust AI applications that maintain context, make complex decisions, and deliver consistent results.

Whether you choose unstructured or structured state, implementing proper state management practices will help you create flows that are maintainable, extensible, and effective at solving real-world problems.

As you develop more complex flows, remember that good state management is about finding the right balance between flexibility and structure, making your code both powerful and easy to understand.

<Check>
  You've now mastered the concepts and practices of state management in CrewAI Flows! With this knowledge, you can create robust AI workflows that effectively maintain context, share data between steps, and build sophisticated application logic.
</Check>


## Next Steps

* Experiment with both structured and unstructured state in your flows
* Try implementing state persistence for long-running workflows
* Explore [building your first crew](/en/guides/crews/first-crew) to see how crews and flows can work together
* Check out the [Flow reference documentation](/en/concepts/flows) for more advanced features



# Installation
Source: https://docs.crewai.com/en/installation

Get started with CrewAI - Install, configure, and build your first AI crew


## Video Tutorial

Watch this video tutorial for a step-by-step demonstration of the installation process:

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/-kSOTtYzgEw" title="CrewAI Installation Guide" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />


## Text Tutorial

<Note>
  **Python Version Requirements**

  CrewAI requires `Python >=3.10 and <3.14`. Here's how to check your version:

  ```bash  theme={null}
  python3 --version
  ```

  If you need to update Python, visit [python.org/downloads](https://python.org/downloads)
</Note>

<Note>
  **OpenAI SDK Requirement**

  CrewAI 0.175.0 requires `openai >= 1.13.3`. If you manage dependencies yourself, ensure your environment satisfies this constraint to avoid import/runtime issues.
</Note>

CrewAI uses the `uv` as its dependency management and package handling tool. It simplifies project setup and execution, offering a seamless experience.

If you haven't installed `uv` yet, follow **step 1** to quickly get it set up on your system, else you can skip to **step 2**.

<Steps>
  <Step title="Install uv">
    * **On macOS/Linux:**

      Use `curl` to download the script and execute it with `sh`:

      ```shell  theme={null}
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```

      If your system doesn't have `curl`, you can use `wget`:

      ```shell  theme={null}
      wget -qO- https://astral.sh/uv/install.sh | sh
      ```

    * **On Windows:**

      Use `irm` to download the script and `iex` to execute it:

      ```shell  theme={null}
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```

      If you run into any issues, refer to [UV's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.
  </Step>

  <Step title="Install CrewAI 🚀">
    * Run the following command to install `crewai` CLI:

      ```shell  theme={null}
      uv tool install crewai
      ```

      <Warning>
        If you encounter a `PATH` warning, run this command to update your shell:

        ```shell  theme={null}
        uv tool update-shell
        ```
      </Warning>

      <Warning>
        If you encounter the `chroma-hnswlib==0.7.6` build error (`fatal error C1083: Cannot open include file: 'float.h'`) on Windows, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) with *Desktop development with C++*.
      </Warning>

    * To verify that `crewai` is installed, run:
      ```shell  theme={null}
      uv tool list
      ```

    * You should see something like:
      ```shell  theme={null}
      crewai v0.102.0
      - crewai
      ```

    * If you need to update `crewai`, run:
      ```shell  theme={null}
      uv tool install crewai --upgrade
      ```

    <Check>Installation successful! You're ready to create your first crew! 🎉</Check>
  </Step>
</Steps>


# Creating a CrewAI Project

We recommend using the `YAML` template scaffolding for a structured approach to defining agents and tasks. Here's how to get started:

<Steps>
  <Step title="Generate Project Scaffolding">
    * Run the `crewai` CLI command:
      ```shell  theme={null}
      crewai create crew <your_project_name>
      ```

    * This creates a new project with the following structure:
      ```
      my_project/
      ├── .gitignore
      ├── knowledge/
      ├── pyproject.toml
      ├── README.md
      ├── .env
      └── src/
          └── my_project/
              ├── __init__.py
              ├── main.py
              ├── crew.py
              ├── tools/
              │   ├── custom_tool.py
              │   └── __init__.py
              └── config/
                  ├── agents.yaml
                  └── tasks.yaml
      ```
  </Step>

  <Step title="Customize Your Project">
    * Your project will contain these essential files:
      | File          | Purpose                                  |
      | ------------- | ---------------------------------------- |
      | `agents.yaml` | Define your AI agents and their roles    |
      | `tasks.yaml`  | Set up agent tasks and workflows         |
      | `.env`        | Store API keys and environment variables |
      | `main.py`     | Project entry point and execution flow   |
      | `crew.py`     | Crew orchestration and coordination      |
      | `tools/`      | Directory for custom agent tools         |
      | `knowledge/`  | Directory for knowledge base             |

    * Start by editing `agents.yaml` and `tasks.yaml` to define your crew's behavior.

    * Keep sensitive information like API keys in `.env`.
  </Step>

  <Step title="Run your Crew">
    * Before you run your crew, make sure to run:
      ```bash  theme={null}
      crewai install
      ```
    * If you need to install additional packages, use:
      ```shell  theme={null}
      uv add <package-name>
      ```
    * To run your crew, execute the following command in the root of your project:
      ```bash  theme={null}
      crewai run
      ```
  </Step>
</Steps>


## Enterprise Installation Options

<Note type="info">
  For teams and organizations, CrewAI offers enterprise deployment options that eliminate setup complexity:

  ### CrewAI AMP (SaaS)

  * Zero installation required - just sign up for free at [app.crewai.com](https://app.crewai.com)
  * Automatic updates and maintenance
  * Managed infrastructure and scaling
  * Build Crews with no Code

  ### CrewAI Factory (Self-hosted)

  * Containerized deployment for your infrastructure
  * Supports any hyperscaler including on prem deployments
  * Integration with your existing security systems

  <Card title="Explore Enterprise Options" icon="building" href="https://crewai.com/enterprise">
    Learn about CrewAI's enterprise offerings and schedule a demo
  </Card>
</Note>


## Next Steps

<CardGroup cols={2}>
  <Card title="Build Your First Agent" icon="code" href="/en/quickstart">
    Follow our quickstart guide to create your first CrewAI agent and get hands-on experience.
  </Card>

  <Card title="Join the Community" icon="comments" href="https://community.crewai.com">
    Connect with other developers, get help, and share your CrewAI experiences.
  </Card>
</CardGroup>



# Introduction
Source: https://docs.crewai.com/en/introduction

Build AI agent teams that work together to tackle complex tasks


# What is CrewAI?

**CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks.**

CrewAI empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario:

* **[CrewAI Crews](/en/guides/crews/first-crew)**: Optimize for autonomy and collaborative intelligence, enabling you to create AI teams where each agent has specific roles, tools, and goals.
* **[CrewAI Flows](/en/guides/flows/first-flow)**: Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively.

With over 100,000 developers certified through our community courses, CrewAI is rapidly becoming the standard for enterprise-ready AI automation.


## How Crews Work

<Note>
  Just like a company has departments (Sales, Engineering, Marketing) working together under leadership to achieve business goals, CrewAI helps you create an organization of AI agents with specialized roles collaborating to accomplish complex tasks.
</Note>

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975" alt="CrewAI Framework Overview" data-og-width="634" width="634" data-og-height="473" height="473" data-path="images/crews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=279c5c26c77fc9acc8411677716fa5ee 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ef573e6215967af1bb2975a58d0d859 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1af6e6a337b70ca2ce238d8e40f49218 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c5da01705f1373446f8582ac582ff244 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=96464aab7bb5efe4213a7b80f58038aa 2500w" />
</Frame>

| Component     |         Description        | Key Features                                                                                                                      |
| :------------ | :------------------------: | :-------------------------------------------------------------------------------------------------------------------------------- |
| **Crew**      | The top-level organization | • Manages AI agent teams<br />• Oversees workflows<br />• Ensures collaboration<br />• Delivers outcomes                          |
| **AI Agents** |  Specialized team members  | • Have specific roles (researcher, writer)<br />• Use designated tools<br />• Can delegate tasks<br />• Make autonomous decisions |
| **Process**   | Workflow management system | • Defines collaboration patterns<br />• Controls task assignments<br />• Manages interactions<br />• Ensures efficient execution  |
| **Tasks**     |   Individual assignments   | • Have clear objectives<br />• Use specific tools<br />• Feed into larger process<br />• Produce actionable results               |

### How It All Works Together

1. The **Crew** organizes the overall operation
2. **AI Agents** work on their specialized tasks
3. The **Process** ensures smooth collaboration
4. **Tasks** get completed to achieve the goal


## Key Features

<CardGroup cols={2}>
  <Card title="Role-Based Agents" icon="users">
    Create specialized agents with defined roles, expertise, and goals - from researchers to analysts to writers
  </Card>

  <Card title="Flexible Tools" icon="screwdriver-wrench">
    Equip agents with custom tools and APIs to interact with external services and data sources
  </Card>

  <Card title="Intelligent Collaboration" icon="people-arrows">
    Agents work together, sharing insights and coordinating tasks to achieve complex objectives
  </Card>

  <Card title="Task Management" icon="list-check">
    Define sequential or parallel workflows, with agents automatically handling task dependencies
  </Card>
</CardGroup>


## How Flows Work

<Note>
  While Crews excel at autonomous collaboration, Flows provide structured automations, offering granular control over workflow execution. Flows ensure tasks are executed reliably, securely, and efficiently, handling conditional logic, loops, and dynamic state management with precision. Flows integrate seamlessly with Crews, enabling you to balance high autonomy with exacting control.
</Note>

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a" alt="CrewAI Framework Overview" data-og-width="669" width="669" data-og-height="464" height="464" data-path="images/flows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4a6177acae3789dd8e4467b791c8966e 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a83fa78165e93bc1d988a30ebc33889a 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=04fbb8e23728b87efa78a0a776e2d194 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ff06d73f5d4aa911154c66becf14d732 2500w" />
</Frame>

| Component        |            Description            | Key Features                                                                                                                                                         |
| :--------------- | :-------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**         | Structured workflow orchestration | • Manages execution paths<br />• Handles state transitions<br />• Controls task sequencing<br />• Ensures reliable execution                                         |
| **Events**       |   Triggers for workflow actions   | • Initiate specific processes<br />• Enable dynamic responses<br />• Support conditional branching<br />• Allow for real-time adaptation                             |
| **States**       |    Workflow execution contexts    | • Maintain execution data<br />• Enable persistence<br />• Support resumability<br />• Ensure execution integrity                                                    |
| **Crew Support** |    Enhances workflow automation   | • Injects pockets of agency when needed<br />• Complements structured workflows<br />• Balances automation with intelligence<br />• Enables adaptive decision-making |

### Key Capabilities

<CardGroup cols={2}>
  <Card title="Event-Driven Orchestration" icon="bolt">
    Define precise execution paths responding dynamically to events
  </Card>

  <Card title="Fine-Grained Control" icon="sliders">
    Manage workflow states and conditional execution securely and efficiently
  </Card>

  <Card title="Native Crew Integration" icon="puzzle-piece">
    Effortlessly combine with Crews for enhanced autonomy and intelligence
  </Card>

  <Card title="Deterministic Execution" icon="route">
    Ensure predictable outcomes with explicit control flow and error handling
  </Card>
</CardGroup>


## When to Use Crews vs. Flows

<Note>
  Understanding when to use [Crews](/en/guides/crews/first-crew) versus [Flows](/en/guides/flows/first-flow) is key to maximizing the potential of CrewAI in your applications.
</Note>

| Use Case                | Recommended Approach                 | Why?                                                                                                                                        |
| :---------------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **Open-ended research** | [Crews](/en/guides/crews/first-crew) | When tasks require creative thinking, exploration, and adaptation                                                                           |
| **Content generation**  | [Crews](/en/guides/crews/first-crew) | For collaborative creation of articles, reports, or marketing materials                                                                     |
| **Decision workflows**  | [Flows](/en/guides/flows/first-flow) | When you need predictable, auditable decision paths with precise control                                                                    |
| **API orchestration**   | [Flows](/en/guides/flows/first-flow) | For reliable integration with multiple external services in a specific sequence                                                             |
| **Hybrid applications** | Combined approach                    | Use [Flows](/en/guides/flows/first-flow) to orchestrate overall process with [Crews](/en/guides/crews/first-crew) handling complex subtasks |

### Decision Framework

* **Choose [Crews](/en/guides/crews/first-crew) when:** You need autonomous problem-solving, creative collaboration, or exploratory tasks
* **Choose [Flows](/en/guides/flows/first-flow) when:** You require deterministic outcomes, auditability, or precise control over execution
* **Combine both when:** Your application needs both structured processes and pockets of autonomous intelligence


## Why Choose CrewAI?

* 🧠 **Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools
* 📝 **Natural Interaction**: Agents communicate and collaborate like human team members
* 🛠️ **Extensible Design**: Easy to add new tools, roles, and capabilities
* 🚀 **Production Ready**: Built for reliability and scalability in real-world applications
* 🔒 **Security-Focused**: Designed with enterprise security requirements in mind
* 💰 **Cost-Efficient**: Optimized to minimize token usage and API calls


## Ready to Start Building?

<CardGroup cols={2}>
  <Card title="Build Your First Crew" icon="users-gear" href="/en/guides/crews/first-crew">
    Step-by-step tutorial to create a collaborative AI team that works together to solve complex problems.
  </Card>

  <Card title="Build Your First Flow" icon="diagram-project" href="/en/guides/flows/first-flow">
    Learn how to create structured, event-driven workflows with precise control over execution.
  </Card>
</CardGroup>

<CardGroup cols={3}>
  <Card title="Install CrewAI" icon="wrench" href="/en/installation">
    Get started with CrewAI in your development environment.
  </Card>

  <Card title="Quick Start" icon="bolt" href="en/quickstart">
    Follow our quickstart guide to create your first CrewAI agent and get hands-on experience.
  </Card>

  <Card title="Join the Community" icon="comments" href="https://community.crewai.com">
    Connect with other developers, get help, and share your CrewAI experiences.
  </Card>
</CardGroup>



# MCP DSL Integration
Source: https://docs.crewai.com/en/mcp/dsl-integration

Learn how to use CrewAI's simple DSL syntax to integrate MCP servers directly with your agents using the mcps field.


## Overview

CrewAI's MCP DSL (Domain Specific Language) integration provides the **simplest way** to connect your agents to MCP (Model Context Protocol) servers. Just add an `mcps` field to your agent and CrewAI handles all the complexity automatically.

<Info>
  This is the **recommended approach** for most MCP use cases. For advanced scenarios requiring manual connection management, see [MCPServerAdapter](/en/mcp/overview#advanced-mcpserveradapter).
</Info>


## Basic Usage

Add MCP servers to your agent using the `mcps` field:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Research Assistant",
    goal="Help with research and analysis tasks",
    backstory="Expert assistant with access to advanced research tools",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key&profile=research"
    ]
)


# MCP tools are now automatically available!

# No need for manual connection management or tool configuration
```


## Supported Reference Formats

### External MCP Remote Servers

```python  theme={null}

# Basic HTTPS server
"https://api.example.com/mcp"


# Server with authentication
"https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile"


# Server with custom path
"https://services.company.com/api/v1/mcp"
```

### Specific Tool Selection

Use the `#` syntax to select specific tools from a server:

```python  theme={null}

# Get only the forecast tool from weather server
"https://weather.api.com/mcp#get_forecast"


# Get only the search tool from Exa
"https://mcp.exa.ai/mcp?api_key=your_key#web_search_exa"
```

### CrewAI AMP Marketplace

Access tools from the CrewAI AMP marketplace:

```python  theme={null}

# Full service with all tools
"crewai-amp:financial-data"


# Specific tool from AMP service
"crewai-amp:research-tools#pubmed_search"


# Multiple AMP services
mcps=[
    "crewai-amp:weather-insights",
    "crewai-amp:market-analysis",
    "crewai-amp:social-media-monitoring"
]
```


## Complete Example

Here's a complete example using multiple MCP servers:

```python  theme={null}
from crewai import Agent, Task, Crew, Process


# Create agent with multiple MCP sources
multi_source_agent = Agent(
    role="Multi-Source Research Analyst",
    goal="Conduct comprehensive research using multiple data sources",
    backstory="""Expert researcher with access to web search, weather data,
    financial information, and academic research tools""",
    mcps=[
        # External MCP servers
        "https://mcp.exa.ai/mcp?api_key=your_exa_key&profile=research",
        "https://weather.api.com/mcp#get_current_conditions",

        # CrewAI AMP marketplace
        "crewai-amp:financial-insights",
        "crewai-amp:academic-research#pubmed_search",
        "crewai-amp:market-intelligence#competitor_analysis"
    ]
)


# Create comprehensive research task
research_task = Task(
    description="""Research the impact of AI agents on business productivity.
    Include current weather impacts on remote work, financial market trends,
    and recent academic publications on AI agent frameworks.""",
    expected_output="""Comprehensive report covering:
    1. AI agent business impact analysis
    2. Weather considerations for remote work
    3. Financial market trends related to AI
    4. Academic research citations and insights
    5. Competitive landscape analysis""",
    agent=multi_source_agent
)


# Create and execute crew
research_crew = Crew(
    agents=[multi_source_agent],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)

result = research_crew.kickoff()
print(f"Research completed with {len(multi_source_agent.mcps)} MCP data sources")
```


## Tool Naming and Organization

CrewAI automatically handles tool naming to prevent conflicts:

```python  theme={null}

# Original MCP server has tools: "search", "analyze"

# CrewAI creates tools: "mcp_exa_ai_search", "mcp_exa_ai_analyze"

agent = Agent(
    role="Tool Organization Demo",
    goal="Show how tool naming works",
    backstory="Demonstrates automatic tool organization",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=key",      # Tools: mcp_exa_ai_*
        "https://weather.service.com/mcp",         # Tools: weather_service_com_*
        "crewai-amp:financial-data"                # Tools: financial_data_*
    ]
)


# Each server's tools get unique prefixes based on the server name

# This prevents naming conflicts between different MCP servers
```


## Error Handling and Resilience

The MCP DSL is designed to be robust and user-friendly:

### Graceful Server Failures

```python  theme={null}
agent = Agent(
    role="Resilient Researcher",
    goal="Research despite server issues",
    backstory="Experienced researcher who adapts to available tools",
    mcps=[
        "https://primary-server.com/mcp",         # Primary data source
        "https://backup-server.com/mcp",          # Backup if primary fails
        "https://unreachable-server.com/mcp",     # Will be skipped with warning
        "crewai-amp:reliable-service"             # Reliable AMP service
    ]
)


# Agent will:

# 1. Successfully connect to working servers

# 2. Log warnings for failing servers

# 3. Continue with available tools

# 4. Not crash or hang on server failures
```

### Timeout Protection

All MCP operations have built-in timeouts:

* **Connection timeout**: 10 seconds
* **Tool execution timeout**: 30 seconds
* **Discovery timeout**: 15 seconds

```python  theme={null}

# These servers will timeout gracefully if unresponsive
mcps=[
    "https://slow-server.com/mcp",        # Will timeout after 10s if unresponsive
    "https://overloaded-api.com/mcp"      # Will timeout if discovery takes > 15s
]
```


## Performance Features

### Automatic Caching

Tool schemas are cached for 5 minutes to improve performance:

```python  theme={null}

# First agent creation - discovers tools from server
agent1 = Agent(role="First", goal="Test", backstory="Test",
               mcps=["https://api.example.com/mcp"])


# Second agent creation (within 5 minutes) - uses cached tool schemas
agent2 = Agent(role="Second", goal="Test", backstory="Test",
               mcps=["https://api.example.com/mcp"])  # Much faster!
```

### On-Demand Connections

Tool connections are established only when tools are actually used:

```python  theme={null}

# Agent creation is fast - no MCP connections made yet
agent = Agent(
    role="On-Demand Agent",
    goal="Use tools efficiently",
    backstory="Efficient agent that connects only when needed",
    mcps=["https://api.example.com/mcp"]
)


# MCP connection is made only when a tool is actually executed

# This minimizes connection overhead and improves startup performance
```


## Integration with Existing Features

MCP tools work seamlessly with other CrewAI features:

```python  theme={null}
from crewai.tools import BaseTool

class CustomTool(BaseTool):
    name: str = "custom_analysis"
    description: str = "Custom analysis tool"

    def _run(self, **kwargs):
        return "Custom analysis result"

agent = Agent(
    role="Full-Featured Agent",
    goal="Use all available tool types",
    backstory="Agent with comprehensive tool access",

    # All tool types work together
    tools=[CustomTool()],                          # Custom tools
    apps=["gmail", "slack"],                       # Platform integrations
    mcps=[                                         # MCP servers
        "https://mcp.exa.ai/mcp?api_key=key",
        "crewai-amp:research-tools"
    ],

    verbose=True,
    max_iter=15
)
```


## Best Practices

### 1. Use Specific Tools When Possible

```python  theme={null}

# Good - only get the tools you need
mcps=["https://weather.api.com/mcp#get_forecast"]


# Less efficient - gets all tools from server
mcps=["https://weather.api.com/mcp"]
```

### 2. Handle Authentication Securely

```python  theme={null}
import os


# Store API keys in environment variables
exa_key = os.getenv("EXA_API_KEY")
exa_profile = os.getenv("EXA_PROFILE")

agent = Agent(
    role="Secure Agent",
    goal="Use MCP tools securely",
    backstory="Security-conscious agent",
    mcps=[f"https://mcp.exa.ai/mcp?api_key={exa_key}&profile={exa_profile}"]
)
```

### 3. Plan for Server Failures

```python  theme={null}

# Always include backup options
mcps=[
    "https://primary-api.com/mcp",       # Primary choice
    "https://backup-api.com/mcp",        # Backup option
    "crewai-amp:reliable-service"        # AMP fallback
]
```

### 4. Use Descriptive Agent Roles

```python  theme={null}
agent = Agent(
    role="Weather-Enhanced Market Analyst",
    goal="Analyze markets considering weather impacts",
    backstory="Financial analyst with access to weather data for agricultural market insights",
    mcps=[
        "https://weather.service.com/mcp#get_forecast",
        "crewai-amp:financial-data#stock_analysis"
    ]
)
```


## Troubleshooting

### Common Issues

**No tools discovered:**

```python  theme={null}

# Check your MCP server URL and authentication

# Verify the server is running and accessible
mcps=["https://mcp.example.com/mcp?api_key=valid_key"]
```

**Connection timeouts:**

```python  theme={null}

# Server may be slow or overloaded

# CrewAI will log warnings and continue with other servers

# Check server status or try backup servers
```

**Authentication failures:**

```python  theme={null}

# Verify API keys and credentials

# Check server documentation for required parameters

# Ensure query parameters are properly URL encoded
```


## Advanced: MCPServerAdapter

For complex scenarios requiring manual connection management, use the `MCPServerAdapter` class from `crewai-tools`. Using a Python context manager (`with` statement) is the recommended approach as it automatically handles starting and stopping the connection to the MCP server.



# Connecting to Multiple MCP Servers
Source: https://docs.crewai.com/en/mcp/multiple-servers

Learn how to use MCPServerAdapter in CrewAI to connect to multiple MCP servers simultaneously and aggregate their tools.


## Overview

`MCPServerAdapter` in `crewai-tools` allows you to connect to multiple MCP servers concurrently. This is useful when your agents need to access tools distributed across different services or environments. The adapter aggregates tools from all specified servers, making them available to your CrewAI agents.


## Configuration

To connect to multiple servers, you provide a list of server parameter dictionaries to `MCPServerAdapter`. Each dictionary in the list should define the parameters for one MCP server.

Supported transport types for each server in the list include `stdio`, `sse`, and `streamable-http`.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters # Needed for Stdio example


# Define parameters for multiple MCP servers
server_params_list = [
    # Streamable HTTP Server
    {
        "url": "http://localhost:8001/mcp", 
        "transport": "streamable-http"
    },
    # SSE Server
    {
        "url": "http://localhost:8000/sse",
        "transport": "sse"
    },
    # StdIO Server
    StdioServerParameters(
        command="python3",
        args=["servers/your_stdio_server.py"],
        env={"UV_PYTHON": "3.12", **os.environ},
    )
]

try:
    with MCPServerAdapter(server_params_list) as aggregated_tools:
        print(f"Available aggregated tools: {[tool.name for tool in aggregated_tools]}")

        multi_server_agent = Agent(
            role="Versatile Assistant",
            goal="Utilize tools from local Stdio, remote SSE, and remote HTTP MCP servers.",
            backstory="An AI agent capable of leveraging a diverse set of tools from multiple sources.",
            tools=aggregated_tools, # All tools are available here
            verbose=True,
        )

        ... # Your other agent, tasks, and crew code here

except Exception as e:
    print(f"Error connecting to or using multiple MCP servers (Managed): {e}")
    print("Ensure all MCP servers are running and accessible with correct configurations.")

```


## Connection Management

When using the context manager (`with` statement), `MCPServerAdapter` handles the lifecycle (start and stop) of all connections to the configured MCP servers. This simplifies resource management and ensures that all connections are properly closed when the context is exited.



# MCP Servers as Tools in CrewAI
Source: https://docs.crewai.com/en/mcp/overview

Learn how to integrate MCP servers as tools in your CrewAI agents using the `crewai-tools` library.


## Overview

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) provides a standardized way for AI agents to provide context to LLMs by communicating with external services, known as MCP Servers.

CrewAI offers **two approaches** for MCP integration:

### 🚀 **Simple DSL Integration** (Recommended)

Use the `mcps` field directly on agents for seamless MCP tool integration. The DSL supports both **string references** (for quick setup) and **structured configurations** (for full control).

#### String-Based References (Quick Setup)

Perfect for remote HTTPS servers and CrewAI AMP marketplace:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Research Analyst",
    goal="Research and analyze information",
    backstory="Expert researcher with access to external tools",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key",           # External MCP server
        "https://api.weather.com/mcp#get_forecast",          # Specific tool from server
        "crewai-amp:financial-data",                         # CrewAI AMP marketplace
        "crewai-amp:research-tools#pubmed_search"            # Specific AMP tool
    ]
)

# MCP tools are now automatically available to your agent!
```

#### Structured Configurations (Full Control)

For complete control over connection settings, tool filtering, and all transport types:

```python  theme={null}
from crewai import Agent
from crewai.mcp import MCPServerStdio, MCPServerHTTP, MCPServerSSE
from crewai.mcp.filters import create_static_tool_filter

agent = Agent(
    role="Advanced Research Analyst",
    goal="Research with full control over MCP connections",
    backstory="Expert researcher with advanced tool access",
    mcps=[
        # Stdio transport for local servers
        MCPServerStdio(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem"],
            env={"API_KEY": "your_key"},
            tool_filter=create_static_tool_filter(
                allowed_tool_names=["read_file", "list_directory"]
            ),
            cache_tools_list=True,
        ),
        # HTTP/Streamable HTTP transport for remote servers
        MCPServerHTTP(
            url="https://api.example.com/mcp",
            headers={"Authorization": "Bearer your_token"},
            streamable=True,
            cache_tools_list=True,
        ),
        # SSE transport for real-time streaming
        MCPServerSSE(
            url="https://stream.example.com/mcp/sse",
            headers={"Authorization": "Bearer your_token"},
        ),
    ]
)
```

### 🔧 **Advanced: MCPServerAdapter** (For Complex Scenarios)

For advanced use cases requiring manual connection management, the `crewai-tools` library provides the `MCPServerAdapter` class.

We currently support the following transport mechanisms:

* **Stdio**: for local servers (communication via standard input/output between processes on the same machine)
* **Server-Sent Events (SSE)**: for remote servers (unidirectional, real-time data streaming from server to client over HTTP)
* **Streamable HTTPS**: for remote servers (flexible, potentially bi-directional communication over HTTPS, often utilizing SSE for server-to-client streams)


## Video Tutorial

Watch this video tutorial for a comprehensive guide on MCP integration with CrewAI:

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/TpQ45lAZh48" title="CrewAI MCP Integration Guide" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />


## Installation

CrewAI MCP integration requires the `mcp` library:

```shell  theme={null}

# For Simple DSL Integration (Recommended)
uv add mcp


# For Advanced MCPServerAdapter usage
uv pip install 'crewai-tools[mcp]'
```


## Quick Start: Simple DSL Integration

The easiest way to integrate MCP servers is using the `mcps` field on your agents. You can use either string references or structured configurations.

### Quick Start with String References

```python  theme={null}
from crewai import Agent, Task, Crew


# Create agent with MCP tools using string references
research_agent = Agent(
    role="Research Analyst",
    goal="Find and analyze information using advanced search tools",
    backstory="Expert researcher with access to multiple data sources",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile",
        "crewai-amp:weather-service#current_conditions"
    ]
)


# Create task
research_task = Task(
    description="Research the latest developments in AI agent frameworks",
    expected_output="Comprehensive research report with citations",
    agent=research_agent
)


# Create and run crew
crew = Crew(agents=[research_agent], tasks=[research_task])
result = crew.kickoff()
```

### Quick Start with Structured Configurations

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai.mcp import MCPServerStdio, MCPServerHTTP, MCPServerSSE


# Create agent with structured MCP configurations
research_agent = Agent(
    role="Research Analyst",
    goal="Find and analyze information using advanced search tools",
    backstory="Expert researcher with access to multiple data sources",
    mcps=[
        # Local stdio server
        MCPServerStdio(
            command="python",
            args=["local_server.py"],
            env={"API_KEY": "your_key"},
        ),
        # Remote HTTP server
        MCPServerHTTP(
            url="https://api.research.com/mcp",
            headers={"Authorization": "Bearer your_token"},
        ),
    ]
)


# Create task
research_task = Task(
    description="Research the latest developments in AI agent frameworks",
    expected_output="Comprehensive research report with citations",
    agent=research_agent
)


# Create and run crew
crew = Crew(agents=[research_agent], tasks=[research_task])
result = crew.kickoff()
```

That's it! The MCP tools are automatically discovered and available to your agent.


## MCP Reference Formats

The `mcps` field supports both **string references** (for quick setup) and **structured configurations** (for full control). You can mix both formats in the same list.

### String-Based References

#### External MCP Servers

```python  theme={null}
mcps=[
    # Full server - get all available tools
    "https://mcp.example.com/api",

    # Specific tool from server using # syntax
    "https://api.weather.com/mcp#get_current_weather",

    # Server with authentication parameters
    "https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile"
]
```

#### CrewAI AMP Marketplace

```python  theme={null}
mcps=[
    # Full AMP MCP service - get all available tools
    "crewai-amp:financial-data",

    # Specific tool from AMP service using # syntax
    "crewai-amp:research-tools#pubmed_search",

    # Multiple AMP services
    "crewai-amp:weather-service",
    "crewai-amp:market-analysis"
]
```

### Structured Configurations

#### Stdio Transport (Local Servers)

Perfect for local MCP servers that run as processes:

```python  theme={null}
from crewai.mcp import MCPServerStdio
from crewai.mcp.filters import create_static_tool_filter

mcps=[
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
        env={"API_KEY": "your_key"},
        tool_filter=create_static_tool_filter(
            allowed_tool_names=["read_file", "write_file"]
        ),
        cache_tools_list=True,
    ),
    # Python-based server
    MCPServerStdio(
        command="python",
        args=["path/to/server.py"],
        env={"UV_PYTHON": "3.12", "API_KEY": "your_key"},
    ),
]
```

#### HTTP/Streamable HTTP Transport (Remote Servers)

For remote MCP servers over HTTP/HTTPS:

```python  theme={null}
from crewai.mcp import MCPServerHTTP

mcps=[
    # Streamable HTTP (default)
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer your_token"},
        streamable=True,
        cache_tools_list=True,
    ),
    # Standard HTTP
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer your_token"},
        streamable=False,
    ),
]
```

#### SSE Transport (Real-Time Streaming)

For remote servers using Server-Sent Events:

```python  theme={null}
from crewai.mcp import MCPServerSSE

mcps=[
    MCPServerSSE(
        url="https://stream.example.com/mcp/sse",
        headers={"Authorization": "Bearer your_token"},
        cache_tools_list=True,
    ),
]
```

### Mixed References

You can combine string references and structured configurations:

```python  theme={null}
from crewai.mcp import MCPServerStdio, MCPServerHTTP

mcps=[
    # String references
    "https://external-api.com/mcp",              # External server
    "crewai-amp:financial-insights",             # AMP service

    # Structured configurations
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
    ),
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer token"},
    ),
]
```

### Tool Filtering

Structured configurations support advanced tool filtering:

```python  theme={null}
from crewai.mcp import MCPServerStdio
from crewai.mcp.filters import create_static_tool_filter, create_dynamic_tool_filter, ToolFilterContext


# Static filtering (allow/block lists)
static_filter = create_static_tool_filter(
    allowed_tool_names=["read_file", "write_file"],
    blocked_tool_names=["delete_file"],
)


# Dynamic filtering (context-aware)
def dynamic_filter(context: ToolFilterContext, tool: dict) -> bool:
    # Block dangerous tools for certain agent roles
    if context.agent.role == "Code Reviewer":
        if "delete" in tool.get("name", "").lower():
            return False
    return True

mcps=[
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
        tool_filter=static_filter,  # or dynamic_filter
    ),
]
```


## Configuration Parameters

Each transport type supports specific configuration options:

### MCPServerStdio Parameters

* **`command`** (required): Command to execute (e.g., `"python"`, `"node"`, `"npx"`, `"uvx"`)
* **`args`** (optional): List of command arguments (e.g., `["server.py"]` or `["-y", "@mcp/server"]`)
* **`env`** (optional): Dictionary of environment variables to pass to the process
* **`tool_filter`** (optional): Tool filter function for filtering available tools
* **`cache_tools_list`** (optional): Whether to cache the tool list for faster subsequent access (default: `False`)

### MCPServerHTTP Parameters

* **`url`** (required): Server URL (e.g., `"https://api.example.com/mcp"`)
* **`headers`** (optional): Dictionary of HTTP headers for authentication or other purposes
* **`streamable`** (optional): Whether to use streamable HTTP transport (default: `True`)
* **`tool_filter`** (optional): Tool filter function for filtering available tools
* **`cache_tools_list`** (optional): Whether to cache the tool list for faster subsequent access (default: `False`)

### MCPServerSSE Parameters

* **`url`** (required): Server URL (e.g., `"https://api.example.com/mcp/sse"`)
* **`headers`** (optional): Dictionary of HTTP headers for authentication or other purposes
* **`tool_filter`** (optional): Tool filter function for filtering available tools
* **`cache_tools_list`** (optional): Whether to cache the tool list for faster subsequent access (default: `False`)

### Common Parameters

All transport types support:

* **`tool_filter`**: Filter function to control which tools are available. Can be:
  * `None` (default): All tools are available
  * Static filter: Created with `create_static_tool_filter()` for allow/block lists
  * Dynamic filter: Created with `create_dynamic_tool_filter()` for context-aware filtering
* **`cache_tools_list`**: When `True`, caches the tool list after first discovery to improve performance on subsequent connections


## Key Features

* 🔄 **Automatic Tool Discovery**: Tools are automatically discovered and integrated
* 🏷️ **Name Collision Prevention**: Server names are prefixed to tool names
* ⚡ **Performance Optimized**: On-demand connections with schema caching
* 🛡️ **Error Resilience**: Graceful handling of unavailable servers
* ⏱️ **Timeout Protection**: Built-in timeouts prevent hanging connections
* 📊 **Transparent Integration**: Works seamlessly with existing CrewAI features
* 🔧 **Full Transport Support**: Stdio, HTTP/Streamable HTTP, and SSE transports
* 🎯 **Advanced Filtering**: Static and dynamic tool filtering capabilities
* 🔐 **Flexible Authentication**: Support for headers, environment variables, and query parameters


## Error Handling

The MCP DSL integration is designed to be resilient and handles failures gracefully:

```python  theme={null}
from crewai import Agent
from crewai.mcp import MCPServerStdio, MCPServerHTTP

agent = Agent(
    role="Resilient Agent",
    goal="Continue working despite server issues",
    backstory="Agent that handles failures gracefully",
    mcps=[
        # String references
        "https://reliable-server.com/mcp",        # Will work
        "https://unreachable-server.com/mcp",     # Will be skipped gracefully
        "crewai-amp:working-service",             # Will work

        # Structured configs
        MCPServerStdio(
            command="python",
            args=["reliable_server.py"],          # Will work
        ),
        MCPServerHTTP(
            url="https://slow-server.com/mcp",     # Will timeout gracefully
        ),
    ]
)

# Agent will use tools from working servers and log warnings for failing ones
```

All connection errors are handled gracefully:

* **Connection failures**: Logged as warnings, agent continues with available tools
* **Timeout errors**: Connections timeout after 30 seconds (configurable)
* **Authentication errors**: Logged clearly for debugging
* **Invalid configurations**: Validation errors are raised at agent creation time


## Advanced: MCPServerAdapter

For complex scenarios requiring manual connection management, use the `MCPServerAdapter` class from `crewai-tools`. Using a Python context manager (`with` statement) is the recommended approach as it automatically handles starting and stopping the connection to the MCP server.


## Connection Configuration

The `MCPServerAdapter` supports several configuration options to customize the connection behavior:

* **`connect_timeout`** (optional): Maximum time in seconds to wait for establishing a connection to the MCP server. Defaults to 30 seconds if not specified. This is particularly useful for remote servers that may have variable response times.

```python  theme={null}

# Example with custom connection timeout
with MCPServerAdapter(server_params, connect_timeout=60) as tools:
    # Connection will timeout after 60 seconds if not established
    pass
```

```python  theme={null}
from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters # For Stdio Server


# Example server_params (choose one based on your server type):

# 1. Stdio Server:
server_params=StdioServerParameters(
    command="python3",
    args=["servers/your_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)


# 2. SSE Server:
server_params = {
    "url": "http://localhost:8000/sse",
    "transport": "sse"
}


# 3. Streamable HTTP Server:
server_params = {
    "url": "http://localhost:8001/mcp",
    "transport": "streamable-http"
}


# Example usage (uncomment and adapt once server_params is set):
with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")

    my_agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server.",
        backstory="I can connect to MCP servers and use their tools.",
        tools=mcp_tools, # Pass the loaded tools to your agent
        reasoning=True,
        verbose=True
    )
    # ... rest of your crew setup ...
```

This general pattern shows how to integrate tools. For specific examples tailored to each transport, refer to the detailed guides below.


## Filtering Tools

There are two ways to filter tools:

1. Accessing a specific tool using dictionary-style indexing.
2. Pass a list of tool names to the `MCPServerAdapter` constructor.

### Accessing a specific tool using dictionary-style indexing.

```python  theme={null}
with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")

    my_agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server.",
        backstory="I can connect to MCP servers and use their tools.",
        tools=[mcp_tools["tool_name"]], # Pass the loaded tools to your agent
        reasoning=True,
        verbose=True
    )
    # ... rest of your crew setup ...
```

### Pass a list of tool names to the `MCPServerAdapter` constructor.

```python  theme={null}
with MCPServerAdapter(server_params, "tool_name", connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")

    my_agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server.",
        backstory="I can connect to MCP servers and use their tools.",
        tools=mcp_tools, # Pass the loaded tools to your agent
        reasoning=True,
        verbose=True
    )
    # ... rest of your crew setup ...
```


## Using with CrewBase

To use MCPServer tools within a CrewBase class, use the `get_mcp_tools` method. Server configurations should be provided via the `mcp_server_params` attribute. You can pass either a single configuration or a list of multiple server configurations.

```python  theme={null}
@CrewBase
class CrewWithMCP:
  # ... define your agents and tasks config file ...

  mcp_server_params = [
    # Streamable HTTP Server
    {
        "url": "http://localhost:8001/mcp",
        "transport": "streamable-http"
    },
    # SSE Server
    {
        "url": "http://localhost:8000/sse",
        "transport": "sse"
    },
    # StdIO Server
    StdioServerParameters(
        command="python3",
        args=["servers/your_stdio_server.py"],
        env={"UV_PYTHON": "3.12", **os.environ},
    )
  ]

  @agent
  def your_agent(self):
      return Agent(config=self.agents_config["your_agent"], tools=self.get_mcp_tools()) # get all available tools

    # ... rest of your crew setup ...
```

<Tip>
  When a crew class is decorated with `@CrewBase`, the adapter lifecycle is managed for you:

  * The first call to `get_mcp_tools()` lazily creates a shared `MCPServerAdapter` that is reused by every agent in the crew.
  * The adapter automatically shuts down after `.kickoff()` completes thanks to an implicit after-kickoff hook injected by `@CrewBase`, so no manual cleanup is required.
  * If `mcp_server_params` is not defined, `get_mcp_tools()` simply returns an empty list, allowing the same code paths to run with or without MCP configured.

  This makes it safe to call `get_mcp_tools()` from multiple agent methods or selectively enable MCP per environment.
</Tip>

### Connection Timeout Configuration

You can configure the connection timeout for MCP servers by setting the `mcp_connect_timeout` class attribute. If no timeout is specified, it defaults to 30 seconds.

```python  theme={null}
@CrewBase
class CrewWithMCP:
  mcp_server_params = [...]
  mcp_connect_timeout = 60  # 60 seconds timeout for all MCP connections

  @agent
  def your_agent(self):
      return Agent(config=self.agents_config["your_agent"], tools=self.get_mcp_tools())
```

```python  theme={null}
@CrewBase
class CrewWithDefaultTimeout:
  mcp_server_params = [...]
  # No mcp_connect_timeout specified - uses default 30 seconds

  @agent
  def your_agent(self):
      return Agent(config=self.agents_config["your_agent"], tools=self.get_mcp_tools())
```

### Filtering Tools

You can filter which tools are available to your agent by passing a list of tool names to the `get_mcp_tools` method.

```python  theme={null}
@agent
def another_agent(self):
    return Agent(
      config=self.agents_config["your_agent"],
      tools=self.get_mcp_tools("tool_1", "tool_2") # get specific tools
    )
```

The timeout configuration applies to all MCP tool calls within the crew:

```python  theme={null}
@CrewBase
class CrewWithCustomTimeout:
  mcp_server_params = [...]
  mcp_connect_timeout = 90  # 90 seconds timeout for all MCP connections

  @agent
  def filtered_agent(self):
      return Agent(
        config=self.agents_config["your_agent"],
        tools=self.get_mcp_tools("tool_1", "tool_2") # specific tools with custom timeout
      )
```


## Explore MCP Integrations

<CardGroup cols={2}>
  <Card title="Simple DSL Integration" icon="code" href="/en/mcp/dsl-integration" color="#3B82F6">
    **Recommended**: Use the simple `mcps=[]` field syntax for effortless MCP integration.
  </Card>

  <Card title="Stdio Transport" icon="server" href="/en/mcp/stdio" color="#10B981">
    Connect to local MCP servers via standard input/output. Ideal for scripts and local executables.
  </Card>

  <Card title="SSE Transport" icon="wifi" href="/en/mcp/sse" color="#F59E0B">
    Integrate with remote MCP servers using Server-Sent Events for real-time data streaming.
  </Card>

  <Card title="Streamable HTTP Transport" icon="globe" href="/en/mcp/streamable-http" color="#8B5CF6">
    Utilize flexible Streamable HTTP for robust communication with remote MCP servers.
  </Card>

  <Card title="Connecting to Multiple Servers" icon="layer-group" href="/en/mcp/multiple-servers" color="#EF4444">
    Aggregate tools from several MCP servers simultaneously using a single adapter.
  </Card>

  <Card title="Security Considerations" icon="lock" href="/en/mcp/security" color="#DC2626">
    Review important security best practices for MCP integration to keep your agents safe.
  </Card>
</CardGroup>

Checkout this repository for full demos and examples of MCP integration with CrewAI! 👇

<Card title="GitHub Repository" icon="github" href="https://github.com/tonykipkemboi/crewai-mcp-demo" target="_blank">
  CrewAI MCP Demo
</Card>


## Staying Safe with MCP

<Warning>
  Always ensure that you trust an MCP Server before using it.
</Warning>

#### Security Warning: DNS Rebinding Attacks

SSE transports can be vulnerable to DNS rebinding attacks if not properly secured.
To prevent this:

1. **Always validate Origin headers** on incoming SSE connections to ensure they come from expected sources
2. **Avoid binding servers to all network interfaces** (0.0.0.0) when running locally - bind only to localhost (127.0.0.1) instead
3. **Implement proper authentication** for all SSE connections

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.

For more details, see the [Anthropic's MCP Transport Security docs](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations).

### Limitations

* **Supported Primitives**: Currently, `MCPServerAdapter` primarily supports adapting MCP `tools`.
  Other MCP primitives like `prompts` or `resources` are not directly integrated as CrewAI components through this adapter at this time.
* **Output Handling**: The adapter typically processes the primary text output from an MCP tool (e.g., `.content[0].text`). Complex or multi-modal outputs might require custom handling if not fitting this pattern.



# MCP Security Considerations
Source: https://docs.crewai.com/en/mcp/security

Learn about important security best practices when integrating MCP servers with your CrewAI agents.


## Overview

<Warning>
  The most critical aspect of MCP security is **trust**. You should **only** connect your CrewAI agents to MCP servers that you fully trust.
</Warning>

When integrating external services like MCP (Model Context Protocol) servers into your CrewAI agents, security is paramount.
MCP servers can execute code, access data, or interact with other systems based on the tools they expose.
It's crucial to understand the implications and follow best practices to protect your applications and data.

### Risks

* Execute arbitrary code on the machine where the agent is running (especially with `Stdio` transport if the server can control the command executed).
* Expose sensitive data from your agent or its environment.
* Manipulate your agent's behavior in unintended ways, including making unauthorized API calls on your behalf.
* Hijack your agent's reasoning process through sophisticated prompt injection techniques (see below).

### 1. Trusting MCP Servers

<Warning>
  **Only connect to MCP servers that you trust.**
</Warning>

Before configuring `MCPServerAdapter` to connect to an MCP server, ensure you know:

* **Who operates the server?** Is it a known, reputable service, or an internal server under your control?
* **What tools does it expose?** Understand the capabilities of the tools. Could they be misused if an attacker gained control or if the server itself is malicious?
* **What data does it access or process?** Be aware of any sensitive information that might be sent to or handled by the MCP server.

Avoid connecting to unknown or unverified MCP servers, especially if your agents handle sensitive tasks or data.

### 2. Secure Prompt Injection via Tool Metadata: The "Model Control Protocol" Risk

A significant and subtle risk is the potential for prompt injection through tool metadata. Here's how it works:

1. When your CrewAI agent connects to an MCP server, it typically requests a list of available tools.
2. The MCP server responds with metadata for each tool, including its name, description, and parameter descriptions.
3. Your agent's underlying Language Model (LLM) uses this metadata to understand how and when to use the tools. This metadata is often incorporated into the LLM's system prompt or context.
4. A malicious MCP server can craft its tool metadata (names, descriptions) to include hidden or overt instructions. These instructions can act as a prompt injection, effectively telling your LLM to behave in a certain way, reveal sensitive information, or perform malicious actions.

**Crucially, this attack can occur simply by connecting to a malicious server and listing its tools, even if your agent never explicitly decides to *use* any of those tools.** The mere exposure to the malicious metadata can be enough to compromise the agent's behavior.

**Mitigation:**

* **Extreme Caution with Untrusted Servers:** Reiterate: *Do not connect to MCP servers you do not fully trust.* The risk of metadata injection makes this paramount.

### Stdio Transport Security

Stdio (Standard Input/Output) transport is typically used for local MCP servers running on the same machine as your CrewAI application.

* **Process Isolation**: While generally safer as it doesn't involve network exposure by default, ensure the script or command run by `StdioServerParameters` is from a trusted source and has appropriate file system permissions. A malicious Stdio server script could still harm your local system.
* **Input Sanitization**: If your Stdio server script takes complex inputs derived from agent interactions, ensure the script itself sanitizes these inputs to prevent command injection or other vulnerabilities within the script's logic.
* **Resource Limits**: Be mindful that a local Stdio server process consumes local resources (CPU, memory). Ensure it's well-behaved and won't exhaust system resources.

### Confused Deputy Attacks

The [Confused Deputy Problem](https://en.wikipedia.org/wiki/Confused_deputy_problem) is a classic security vulnerability that can manifest in MCP integrations, especially when an MCP server acts as a proxy to other third-party services (e.g., Google Calendar, GitHub) that use OAuth 2.0 for authorization.

**Scenario:**

1. An MCP server (let's call it `MCP-Proxy`) allows your agent to interact with `ThirdPartyAPI`.
2. `MCP-Proxy` uses its own single, static `client_id` when talking to `ThirdPartyAPI`'s authorization server.
3. You, as the user, legitimately authorize `MCP-Proxy` to access `ThirdPartyAPI` on your behalf. During this, `ThirdPartyAPI`'s auth server might set a cookie in your browser indicating your consent for `MCP-Proxy`'s `client_id`.
4. An attacker crafts a malicious link. This link initiates an OAuth flow with `MCP-Proxy`, but is designed to trick `ThirdPartyAPI`'s auth server.
5. If you click this link, and `ThirdPartyAPI`'s auth server sees your existing consent cookie for `MCP-Proxy`'s `client_id`, it might *skip* asking for your consent again.
6. `MCP-Proxy` might then be tricked into forwarding an authorization code (for `ThirdPartyAPI`) to the attacker, or an MCP authorization code that the attacker can use to impersonate you to `MCP-Proxy`.

**Mitigation (Primarily for MCP Server Developers):**

* MCP proxy servers using static client IDs for downstream services **must** obtain explicit user consent for *each client application or agent* connecting to them *before* initiating an OAuth flow with the third-party service. This means `MCP-Proxy` itself should show a consent screen.

**CrewAI User Implication:**

* Be cautious if an MCP server redirects you for multiple OAuth authentications, especially if it seems unexpected or if the permissions requested are overly broad.
* Prefer MCP servers that clearly delineate their own identity versus the third-party services they might proxy.

### Remote Transport Security (SSE & Streamable HTTP)

When connecting to remote MCP servers via Server-Sent Events (SSE) or Streamable HTTP, standard web security practices are essential.

### SSE Security Considerations

### a. DNS Rebinding Attacks (Especially for SSE)

<Critical>
  **Protect against DNS Rebinding Attacks.**
</Critical>

DNS rebinding allows an attacker-controlled website to bypass the same-origin policy and make requests to servers on the user's local network (e.g., `localhost`) or intranet. This is particularly risky if you run an MCP server locally (e.g., for development) and an agent in a browser-like environment (though less common for typical CrewAI backend setups) or if the MCP server is on an internal network.

**Mitigation Strategies for MCP Server Implementers:**

* **Validate `Origin` and `Host` Headers**: MCP servers (especially SSE ones) should validate the `Origin` and/or `Host` HTTP headers to ensure requests are coming from expected domains/clients.
* **Bind to `localhost` (127.0.0.1)**: When running MCP servers locally for development, bind them to `127.0.0.1` instead of `0.0.0.0`. This prevents them from being accessible from other machines on the network.
* **Authentication**: Require authentication for all connections to your MCP server if it's not intended for public anonymous access.

### b. Use HTTPS

* **Encrypt Data in Transit**: Always use HTTPS (HTTP Secure) for the URLs of remote MCP servers. This encrypts the communication between your CrewAI application and the MCP server, protecting against eavesdropping and man-in-the-middle attacks. `MCPServerAdapter` will respect the scheme (`http` or `https`) provided in the URL.

### c. Token Passthrough (Anti-Pattern)

This is primarily a concern for MCP server developers but understanding it helps in choosing secure servers.

"Token passthrough" is when an MCP server accepts an access token from your CrewAI agent (which might be a token for a *different* service, say `ServiceA`) and simply passes it through to another downstream API (`ServiceB`) without proper validation. Specifically, `ServiceB` (or the MCP server itself) should only accept tokens that were explicitly issued *for them* (i.e., the 'audience' claim in the token matches the server/service).

**Risks:**

* Bypasses security controls (like rate limiting or fine-grained permissions) on the MCP server or the downstream API.
* Breaks audit trails and accountability.
* Allows misuse of stolen tokens.

**Mitigation (For MCP Server Developers):**

* MCP servers **MUST NOT** accept tokens that were not explicitly issued for them. They must validate the token's audience claim.

**CrewAI User Implication:**

* While not directly controllable by the user, this highlights the importance of connecting to well-designed MCP servers that adhere to security best practices.

#### Authentication and Authorization

* **Verify Identity**: If the MCP server provides sensitive tools or access to private data, it MUST implement strong authentication mechanisms to verify the identity of the client (your CrewAI application). This could involve API keys, OAuth tokens, or other standard methods.
* **Principle of Least Privilege**: Ensure the credentials used by `MCPServerAdapter` (if any) have only the necessary permissions to access the required tools.

### d. Input Validation and Sanitization

* **Input Validation is Critical**: MCP servers **must** rigorously validate all inputs received from agents *before* processing them or passing them to tools. This is a primary defense against many common vulnerabilities:
  * **Command Injection:** If a tool constructs shell commands, SQL queries, or other interpreted language statements based on input, the server must meticulously sanitize this input to prevent malicious commands from being injected and executed.
  * **Path Traversal:** If a tool accesses files based on input parameters, the server must validate and sanitize these paths to prevent access to unauthorized files or directories (e.g., by blocking `../` sequences).
  * **Data Type & Range Checks:** Servers must ensure that input data conforms to the expected data types (e.g., string, number, boolean) and falls within acceptable ranges or adheres to defined formats (e.g., regex for URLs).
  * **JSON Schema Validation:** All tool parameters should be strictly validated against their defined JSON schema. This helps catch malformed requests early.
* **Client-Side Awareness**: While server-side validation is paramount, as a CrewAI user, be mindful of the data your agents are constructed to send to MCP tools, especially if interacting with less-trusted or new MCP servers.

### e. Rate Limiting and Resource Management

* **Prevent Abuse**: MCP servers should implement rate limiting to prevent abuse, whether intentional (Denial of Service attacks) or unintentional (e.g., a misconfigured agent making too many requests).
* **Client-Side Retries**: Implement sensible retry logic in your CrewAI tasks if transient network issues or server rate limits are expected, but avoid aggressive retries that could exacerbate server load.


## 4. Secure MCP Server Implementation Advice (For Developers)

If you are developing an MCP server that CrewAI agents might connect to, consider these best practices in addition to the points above:

* **Follow Secure Coding Practices**: Adhere to standard secure coding principles for your chosen language and framework (e.g., OWASP Top 10).
* **Principle of Least Privilege**: Ensure the process running the MCP server (especially for `Stdio`) has only the minimum necessary permissions. Tools themselves should also operate with the least privilege required to perform their function.
* **Dependency Management**: Keep all server-side dependencies, including operating system packages, language runtimes, and third-party libraries, up-to-date to patch known vulnerabilities. Use tools to scan for vulnerable dependencies.
* **Secure Defaults**: Design your server and its tools to be secure by default. For example, features that could be risky should be off by default or require explicit opt-in with clear warnings.
* **Access Control for Tools**: Implement robust mechanisms to control which authenticated and authorized agents or users can access specific tools, especially those that are powerful, sensitive, or incur costs.
* **Secure Error Handling**: Servers should not expose detailed internal error messages, stack traces, or debugging information to the client, as these can reveal internal workings or potential vulnerabilities. Log errors comprehensively on the server-side for diagnostics.
* **Comprehensive Logging and Monitoring**: Implement detailed logging of security-relevant events (e.g., authentication attempts, tool invocations, errors, authorization changes). Monitor these logs for suspicious activity or abuse patterns.
* **Adherence to MCP Authorization Spec**: If implementing authentication and authorization, strictly follow the [MCP Authorization specification](https://modelcontextprotocol.io/specification/draft/basic/authorization) and relevant [OAuth 2.0 security best practices](https://datatracker.ietf.org/doc/html/rfc9700).
* **Regular Security Audits**: If your MCP server handles sensitive data, performs critical operations, or is publicly exposed, consider periodic security audits by qualified professionals.


## 5. Further Reading

For more detailed information on MCP security, refer to the official documentation:

* **[MCP Transport Security](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations)**

By understanding these security considerations and implementing best practices, you can safely leverage the power of MCP servers in your CrewAI projects.
These are by no means exhaustive, but they cover the most common and critical security concerns.
The threats will continue to evolve, so it's important to stay informed and adapt your security measures accordingly.



# SSE Transport
Source: https://docs.crewai.com/en/mcp/sse

Learn how to connect CrewAI to remote MCP servers using Server-Sent Events (SSE) for real-time communication.


## Overview

Server-Sent Events (SSE) provide a standard way for a web server to send updates to a client over a single, long-lived HTTP connection. In the context of MCP, SSE is used for remote servers to stream data (like tool responses) to your CrewAI application in real-time.


## Key Concepts

* **Remote Servers**: SSE is suitable for MCP servers hosted remotely.
* **Unidirectional Stream**: Typically, SSE is a one-way communication channel from server to client.
* **`MCPServerAdapter` Configuration**: For SSE, you'll provide the server's URL and specify the transport type.


## Connecting via SSE

You can connect to an SSE-based MCP server using two main approaches for managing the connection lifecycle:

### 1. Fully Managed Connection (Recommended)

Using a Python context manager (`with` statement) is the recommended approach. It automatically handles establishing and closing the connection to the SSE MCP server.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8000/sse", # Replace with your actual SSE server URL
    "transport": "sse" 
}


# Using MCPServerAdapter with a context manager
try:
    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools from SSE MCP server: {[tool.name for tool in tools]}")

        # Example: Using a tool from the SSE MCP server
        sse_agent = Agent(
            role="Remote Service User",
            goal="Utilize a tool provided by a remote SSE MCP server.",
            backstory="An AI agent that connects to external services via SSE.",
            tools=tools,
            reasoning=True,
            verbose=True,
        )

        sse_task = Task(
            description="Fetch real-time stock updates for 'AAPL' using an SSE tool.",
            expected_output="The latest stock price for AAPL.",
            agent=sse_agent,
            markdown=True
        )

        sse_crew = Crew(
            agents=[sse_agent],
            tasks=[sse_task],
            verbose=True,
            process=Process.sequential
        )
        
        if tools: # Only kickoff if tools were loaded
            result = sse_crew.kickoff() # Add inputs={'stock_symbol': 'AAPL'} if tool requires it
            print("\nCrew Task Result (SSE - Managed):\n", result)
        else:
            print("Skipping crew kickoff as tools were not loaded (check server connection).")

except Exception as e:
    print(f"Error connecting to or using SSE MCP server (Managed): {e}")
    print("Ensure the SSE MCP server is running and accessible at the specified URL.")

```

<Note>
  Replace `"http://localhost:8000/sse"` with the actual URL of your SSE MCP server.
</Note>

### 2. Manual Connection Lifecycle

If you need finer-grained control, you can manage the `MCPServerAdapter` connection lifecycle manually.

<Info>
  You **MUST** call `mcp_server_adapter.stop()` to ensure the connection is closed and resources are released. Using a `try...finally` block is highly recommended.
</Info>

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8000/sse", # Replace with your actual SSE server URL
    "transport": "sse"
}

mcp_server_adapter = None 
try:
    mcp_server_adapter = MCPServerAdapter(server_params)
    mcp_server_adapter.start()
    tools = mcp_server_adapter.tools
    print(f"Available tools (manual SSE): {[tool.name for tool in tools]}")

    manual_sse_agent = Agent(
        role="Remote Data Analyst",
        goal="Analyze data fetched from a remote SSE MCP server using manual connection management.",
        backstory="An AI skilled in handling SSE connections explicitly.",
        tools=tools,
        verbose=True
    )
    
    analysis_task = Task(
        description="Fetch and analyze the latest user activity trends from the SSE server.",
        expected_output="A summary report of user activity trends.",
        agent=manual_sse_agent
    )
    
    analysis_crew = Crew(
        agents=[manual_sse_agent],
        tasks=[analysis_task],
        verbose=True,
        process=Process.sequential
    )
    
    result = analysis_crew.kickoff()
    print("\nCrew Task Result (SSE - Manual):\n", result)

except Exception as e:
    print(f"An error occurred during manual SSE MCP integration: {e}")
    print("Ensure the SSE MCP server is running and accessible.")
finally:
    if mcp_server_adapter and mcp_server_adapter.is_connected:
        print("Stopping SSE MCP server connection (manual)...")
        mcp_server_adapter.stop()  # **Crucial: Ensure stop is called**
    elif mcp_server_adapter:
        print("SSE MCP server adapter was not connected. No stop needed or start failed.")

```


## Security Considerations for SSE

<Warning>
  **DNS Rebinding Attacks**: SSE transports can be vulnerable to DNS rebinding attacks if the MCP server is not properly secured. This could allow malicious websites to interact with local or intranet-based MCP servers.
</Warning>

To mitigate this risk:

* MCP server implementations should **validate `Origin` headers** on incoming SSE connections.
* When running local SSE MCP servers for development, **bind only to `localhost` (`127.0.0.1`)** rather than all network interfaces (`0.0.0.0`).
* Implement **proper authentication** for all SSE connections if they expose sensitive tools or data.

For a comprehensive overview of security best practices, please refer to our [Security Considerations](./security.mdx) page and the official [MCP Transport Security documentation](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations).



# Stdio Transport
Source: https://docs.crewai.com/en/mcp/stdio

Learn how to connect CrewAI to local MCP servers using the Stdio (Standard Input/Output) transport mechanism.


## Overview

The Stdio (Standard Input/Output) transport is designed for connecting `MCPServerAdapter` to local MCP servers that communicate over their standard input and output streams. This is typically used when the MCP server is a script or executable running on the same machine as your CrewAI application.


## Key Concepts

* **Local Execution**: Stdio transport manages a locally running process for the MCP server.
* **`StdioServerParameters`**: This class from the `mcp` library is used to configure the command, arguments, and environment variables for launching the Stdio server.


## Connecting via Stdio

You can connect to an Stdio-based MCP server using two main approaches for managing the connection lifecycle:

### 1. Fully Managed Connection (Recommended)

Using a Python context manager (`with` statement) is the recommended approach. It automatically handles starting the MCP server process and stopping it when the context is exited.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os


# Create a StdioServerParameters object
server_params=StdioServerParameters(
    command="python3", 
    args=["servers/your_stdio_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with MCPServerAdapter(server_params) as tools:
    print(f"Available tools from Stdio MCP server: {[tool.name for tool in tools]}")

    # Example: Using the tools from the Stdio MCP server in a CrewAI Agent
    research_agent = Agent(
        role="Local Data Processor",
        goal="Process data using a local Stdio-based tool.",
        backstory="An AI that leverages local scripts via MCP for specialized tasks.",
        tools=tools,
        reasoning=True,
        verbose=True,
    )
    
    processing_task = Task(
        description="Process the input data file 'data.txt' and summarize its contents.",
        expected_output="A summary of the processed data.",
        agent=research_agent,
        markdown=True
    )
    
    data_crew = Crew(
        agents=[research_agent],
        tasks=[processing_task],
        verbose=True,
        process=Process.sequential 
    )
   
    result = data_crew.kickoff()
    print("\nCrew Task Result (Stdio - Managed):\n", result)

```

### 2. Manual Connection Lifecycle

If you need finer-grained control over when the Stdio MCP server process is started and stopped, you can manage the `MCPServerAdapter` lifecycle manually.

<Info>
  You **MUST** call `mcp_server_adapter.stop()` to ensure the server process is terminated and resources are released. Using a `try...finally` block is highly recommended.
</Info>

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os


# Create a StdioServerParameters object
stdio_params=StdioServerParameters(
    command="python3", 
    args=["servers/your_stdio_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

mcp_server_adapter = MCPServerAdapter(server_params=stdio_params)
try:
    mcp_server_adapter.start()  # Manually start the connection and server process
    tools = mcp_server_adapter.tools
    print(f"Available tools (manual Stdio): {[tool.name for tool in tools]}")

    # Example: Using the tools with your Agent, Task, Crew setup
    manual_agent = Agent(
        role="Local Task Executor",
        goal="Execute a specific local task using a manually managed Stdio tool.",
        backstory="An AI proficient in controlling local processes via MCP.",
        tools=tools,
        verbose=True
    )
    
    manual_task = Task(
        description="Execute the 'perform_analysis' command via the Stdio tool.",
        expected_output="Results of the analysis.",
        agent=manual_agent
    )
    
    manual_crew = Crew(
        agents=[manual_agent],
        tasks=[manual_task],
        verbose=True,
        process=Process.sequential
    )
        
       
    result = manual_crew.kickoff() # Actual inputs depend on your tool
    print("\nCrew Task Result (Stdio - Manual):\n", result)
            
except Exception as e:
    print(f"An error occurred during manual Stdio MCP integration: {e}")
finally:
    if mcp_server_adapter and mcp_server_adapter.is_connected: # Check if connected before stopping
        print("Stopping Stdio MCP server connection (manual)...")
        mcp_server_adapter.stop()  # **Crucial: Ensure stop is called**
    elif mcp_server_adapter: # If adapter exists but not connected (e.g. start failed)
        print("Stdio MCP server adapter was not connected. No stop needed or start failed.")

```

Remember to replace placeholder paths and commands with your actual Stdio server details. The `env` parameter in `StdioServerParameters` can
be used to set environment variables for the server process, which can be useful for configuring its behavior or providing necessary paths (like `PYTHONPATH`).



# Streamable HTTP Transport
Source: https://docs.crewai.com/en/mcp/streamable-http

Learn how to connect CrewAI to remote MCP servers using the flexible Streamable HTTP transport.


## Overview

Streamable HTTP transport provides a flexible way to connect to remote MCP servers. It's often built upon HTTP and can support various communication patterns, including request-response and streaming, sometimes utilizing Server-Sent Events (SSE) for server-to-client streams within a broader HTTP interaction.


## Key Concepts

* **Remote Servers**: Designed for MCP servers hosted remotely.
* **Flexibility**: Can support more complex interaction patterns than plain SSE, potentially including bi-directional communication if the server implements it.
* **`MCPServerAdapter` Configuration**: You'll need to provide the server's base URL for MCP communication and specify `"streamable-http"` as the transport type.


## Connecting via Streamable HTTP

You have two primary methods for managing the connection lifecycle with a Streamable HTTP MCP server:

### 1. Fully Managed Connection (Recommended)

The recommended approach is to use a Python context manager (`with` statement), which handles the connection's setup and teardown automatically.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8001/mcp", # Replace with your actual Streamable HTTP server URL
    "transport": "streamable-http"
}

try:
    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools from Streamable HTTP MCP server: {[tool.name for tool in tools]}")

        http_agent = Agent(
            role="HTTP Service Integrator",
            goal="Utilize tools from a remote MCP server via Streamable HTTP.",
            backstory="An AI agent adept at interacting with complex web services.",
            tools=tools,
            verbose=True,
        )

        http_task = Task(
            description="Perform a complex data query using a tool from the Streamable HTTP server.",
            expected_output="The result of the complex data query.",
            agent=http_agent,
        )

        http_crew = Crew(
            agents=[http_agent],
            tasks=[http_task],
            verbose=True,
            process=Process.sequential
        )
        
        result = http_crew.kickoff() 
        print("\nCrew Task Result (Streamable HTTP - Managed):\n", result)

except Exception as e:
    print(f"Error connecting to or using Streamable HTTP MCP server (Managed): {e}")
    print("Ensure the Streamable HTTP MCP server is running and accessible at the specified URL.")

```

**Note:** Replace `"http://localhost:8001/mcp"` with the actual URL of your Streamable HTTP MCP server.

### 2. Manual Connection Lifecycle

For scenarios requiring more explicit control, you can manage the `MCPServerAdapter` connection manually.

<Info>
  It is **critical** to call `mcp_server_adapter.stop()` when you are done to close the connection and free up resources. A `try...finally` block is the safest way to ensure this.
</Info>

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8001/mcp", # Replace with your actual Streamable HTTP server URL
    "transport": "streamable-http"
}

mcp_server_adapter = None 
try:
    mcp_server_adapter = MCPServerAdapter(server_params)
    mcp_server_adapter.start()
    tools = mcp_server_adapter.tools
    print(f"Available tools (manual Streamable HTTP): {[tool.name for tool in tools]}")

    manual_http_agent = Agent(
        role="Advanced Web Service User",
        goal="Interact with an MCP server using manually managed Streamable HTTP connections.",
        backstory="An AI specialist in fine-tuning HTTP-based service integrations.",
        tools=tools,
        verbose=True
    )
    
    data_processing_task = Task(
        description="Submit data for processing and retrieve results via Streamable HTTP.",
        expected_output="Processed data or confirmation.",
        agent=manual_http_agent
    )
    
    data_crew = Crew(
        agents=[manual_http_agent],
        tasks=[data_processing_task],
        verbose=True,
        process=Process.sequential
    )
    
    result = data_crew.kickoff()
    print("\nCrew Task Result (Streamable HTTP - Manual):\n", result)

except Exception as e:
    print(f"An error occurred during manual Streamable HTTP MCP integration: {e}")
    print("Ensure the Streamable HTTP MCP server is running and accessible.")
finally:
    if mcp_server_adapter and mcp_server_adapter.is_connected:
        print("Stopping Streamable HTTP MCP server connection (manual)...")
        mcp_server_adapter.stop()  # **Crucial: Ensure stop is called**
    elif mcp_server_adapter:
        print("Streamable HTTP MCP server adapter was not connected. No stop needed or start failed.")
```


## Security Considerations

When using Streamable HTTP transport, general web security best practices are paramount:

* **Use HTTPS**: Always prefer HTTPS (HTTP Secure) for your MCP server URLs to encrypt data in transit.
* **Authentication**: Implement robust authentication mechanisms if your MCP server exposes sensitive tools or data.
* **Input Validation**: Ensure your MCP server validates all incoming requests and parameters.

For a comprehensive guide on securing your MCP integrations, please refer to our [Security Considerations](./security.mdx) page and the official [MCP Transport Security documentation](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations).



# Quickstart
Source: https://docs.crewai.com/en/quickstart

Build your first AI agent with CrewAI in under 5 minutes.


## Build your first CrewAI Agent

Let's create a simple crew that will help us `research` and `report` on the `latest AI developments` for a given topic or subject.

Before we proceed, make sure you have finished installing CrewAI.
If you haven't installed them yet, you can do so by following the [installation guide](/en/installation).

Follow the steps below to get Crewing! 🚣‍♂️

<Steps>
  <Step title="Create your crew">
    Create a new crew project by running the following command in your terminal.
    This will create a new directory called `latest-ai-development` with the basic structure for your crew.

    <CodeGroup>
      ```shell Terminal theme={null}
      crewai create crew latest-ai-development
      ```
    </CodeGroup>
  </Step>

  <Step title="Navigate to your new crew project">
    <CodeGroup>
      ```shell Terminal theme={null}
      cd latest_ai_development
      ```
    </CodeGroup>
  </Step>

  <Step title="Modify your `agents.yaml` file">
    <Tip>
      You can also modify the agents as needed to fit your use case or copy and paste as is to your project.
      Any variable interpolated in your `agents.yaml` and `tasks.yaml` files like `{topic}` will be replaced by the value of the variable in the `main.py` file.
    </Tip>

    ```yaml agents.yaml theme={null}
    # src/latest_ai_development/config/agents.yaml
    researcher:
      role: >
        {topic} Senior Data Researcher
      goal: >
        Uncover cutting-edge developments in {topic}
      backstory: >
        You're a seasoned researcher with a knack for uncovering the latest
        developments in {topic}. Known for your ability to find the most relevant
        information and present it in a clear and concise manner.

    reporting_analyst:
      role: >
        {topic} Reporting Analyst
      goal: >
        Create detailed reports based on {topic} data analysis and research findings
      backstory: >
        You're a meticulous analyst with a keen eye for detail. You're known for
        your ability to turn complex data into clear and concise reports, making
        it easy for others to understand and act on the information you provide.
    ```
  </Step>

  <Step title="Modify your `tasks.yaml` file">
    ````yaml tasks.yaml theme={null}
    # src/latest_ai_development/config/tasks.yaml
    research_task:
      description: >
        Conduct a thorough research about {topic}
        Make sure you find any interesting and relevant information given
        the current year is 2025.
      expected_output: >
        A list with 10 bullet points of the most relevant information about {topic}
      agent: researcher

    reporting_task:
      description: >
        Review the context you got and expand each topic into a full section for a report.
        Make sure the report is detailed and contains any and all relevant information.
      expected_output: >
        A fully fledge reports with the mains topics, each with a full section of information.
        Formatted as markdown without '```'
      agent: reporting_analyst
      output_file: report.md
    ````
  </Step>

  <Step title="Modify your `crew.py` file">
    ```python crew.py theme={null}
    # src/latest_ai_development/crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task
    from crewai_tools import SerperDevTool
    from crewai.agents.agent_builder.base_agent import BaseAgent
    from typing import List

    @CrewBase
    class LatestAiDevelopmentCrew():
      """LatestAiDevelopment crew"""

      agents: List[BaseAgent]
      tasks: List[Task]

      @agent
      def researcher(self) -> Agent:
        return Agent(
          config=self.agents_config['researcher'], # type: ignore[index]
          verbose=True,
          tools=[SerperDevTool()]
        )

      @agent
      def reporting_analyst(self) -> Agent:
        return Agent(
          config=self.agents_config['reporting_analyst'], # type: ignore[index]
          verbose=True
        )

      @task
      def research_task(self) -> Task:
        return Task(
          config=self.tasks_config['research_task'], # type: ignore[index]
        )

      @task
      def reporting_task(self) -> Task:
        return Task(
          config=self.tasks_config['reporting_task'], # type: ignore[index]
          output_file='output/report.md' # This is the file that will be contain the final report.
        )

      @crew
      def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
          agents=self.agents, # Automatically created by the @agent decorator
          tasks=self.tasks, # Automatically created by the @task decorator
          process=Process.sequential,
          verbose=True,
        )
    ```
  </Step>

  <Step title="[Optional] Add before and after crew functions">
    ```python crew.py theme={null}
    # src/latest_ai_development/crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
    from crewai_tools import SerperDevTool

    @CrewBase
    class LatestAiDevelopmentCrew():
      """LatestAiDevelopment crew"""

      @before_kickoff
      def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs # You can return the inputs or modify them as needed

      @after_kickoff
      def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result # You can return the result or modify it as needed

      # ... remaining code
    ```
  </Step>

  <Step title="Feel free to pass custom inputs to your crew">
    For example, you can pass the `topic` input to your crew to customize the research and reporting.

    ```python main.py theme={null}
    #!/usr/bin/env python
    # src/latest_ai_development/main.py
    import sys
    from latest_ai_development.crew import LatestAiDevelopmentCrew

    def run():
      """
      Run the crew.
      """
      inputs = {
        'topic': 'AI Agents'
      }
      LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
    ```
  </Step>

  <Step title="Set your environment variables">
    Before running your crew, make sure you have the following keys set as environment variables in your `.env` file:

    * A [Serper.dev](https://serper.dev/) API key: `SERPER_API_KEY=YOUR_KEY_HERE`
    * The configuration for your choice of model, such as an API key. See the
      [LLM setup guide](/en/concepts/llms#setting-up-your-llm) to learn how to configure models from any provider.
  </Step>

  <Step title="Lock and install the dependencies">
    * Lock the dependencies and install them by using the CLI command:
      <CodeGroup>
        ```shell Terminal theme={null}
        crewai install
        ```
      </CodeGroup>
    * If you have additional packages that you want to install, you can do so by running:
      <CodeGroup>
        ```shell Terminal theme={null}
        uv add <package-name>
        ```
      </CodeGroup>
  </Step>

  <Step title="Run your crew">
    * To run your crew, execute the following command in the root of your project:
      <CodeGroup>
        ```bash Terminal theme={null}
        crewai run
        ```
      </CodeGroup>
  </Step>

  <Step title="Enterprise Alternative: Create in Crew Studio">
    For CrewAI AMP users, you can create the same crew without writing code:

    1. Log in to your CrewAI AMP account (create a free account at [app.crewai.com](https://app.crewai.com))
    2. Open Crew Studio
    3. Type what is the automation you're trying to build
    4. Create your tasks visually and connect them in sequence
    5. Configure your inputs and click "Download Code" or "Deploy"

        <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Crew Studio Quickstart" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />

    <Card title="Try CrewAI AMP" icon="rocket" href="https://app.crewai.com">
      Start your free account at CrewAI AMP
    </Card>
  </Step>

  <Step title="View your final report">
    You should see the output in the console and the `report.md` file should be created in the root of your project with the final report.

    Here's an example of what the report should look like:

    <CodeGroup>
      ```markdown output/report.md theme={null}
      # Comprehensive Report on the Rise and Impact of AI Agents in 2025

      ## 1. Introduction to AI Agents
      In 2025, Artificial Intelligence (AI) agents are at the forefront of innovation across various industries. As intelligent systems that can perform tasks typically requiring human cognition, AI agents are paving the way for significant advancements in operational efficiency, decision-making, and overall productivity within sectors like Human Resources (HR) and Finance. This report aims to detail the rise of AI agents, their frameworks, applications, and potential implications on the workforce.

      ## 2. Benefits of AI Agents
      AI agents bring numerous advantages that are transforming traditional work environments. Key benefits include:

      - **Task Automation**: AI agents can carry out repetitive tasks such as data entry, scheduling, and payroll processing without human intervention, greatly reducing the time and resources spent on these activities.
      - **Improved Efficiency**: By quickly processing large datasets and performing analyses that would take humans significantly longer, AI agents enhance operational efficiency. This allows teams to focus on strategic tasks that require higher-level thinking.
      - **Enhanced Decision-Making**: AI agents can analyze trends and patterns in data, provide insights, and even suggest actions, helping stakeholders make informed decisions based on factual data rather than intuition alone.

      ## 3. Popular AI Agent Frameworks
      Several frameworks have emerged to facilitate the development of AI agents, each with its own unique features and capabilities. Some of the most popular frameworks include:

      - **Autogen**: A framework designed to streamline the development of AI agents through automation of code generation.
      - **Semantic Kernel**: Focuses on natural language processing and understanding, enabling agents to comprehend user intentions better.
      - **Promptflow**: Provides tools for developers to create conversational agents that can navigate complex interactions seamlessly.
      - **Langchain**: Specializes in leveraging various APIs to ensure agents can access and utilize external data effectively.
      - **CrewAI**: Aimed at collaborative environments, CrewAI strengthens teamwork by facilitating communication through AI-driven insights.
      - **MemGPT**: Combines memory-optimized architectures with generative capabilities, allowing for more personalized interactions with users.

      These frameworks empower developers to build versatile and intelligent agents that can engage users, perform advanced analytics, and execute various tasks aligned with organizational goals.

      ## 4. AI Agents in Human Resources
      AI agents are revolutionizing HR practices by automating and optimizing key functions:

      - **Recruiting**: AI agents can screen resumes, schedule interviews, and even conduct initial assessments, thus accelerating the hiring process while minimizing biases.
      - **Succession Planning**: AI systems analyze employee performance data and potential, helping organizations identify future leaders and plan appropriate training.
      - **Employee Engagement**: Chatbots powered by AI can facilitate feedback loops between employees and management, promoting an open culture and addressing concerns promptly.

      As AI continues to evolve, HR departments leveraging these agents can realize substantial improvements in both efficiency and employee satisfaction.

      ## 5. AI Agents in Finance
      The finance sector is seeing extensive integration of AI agents that enhance financial practices:

      - **Expense Tracking**: Automated systems manage and monitor expenses, flagging anomalies and offering recommendations based on spending patterns.
      - **Risk Assessment**: AI models assess credit risk and uncover potential fraud by analyzing transaction data and behavioral patterns.
      - **Investment Decisions**: AI agents provide stock predictions and analytics based on historical data and current market conditions, empowering investors with informative insights.

      The incorporation of AI agents into finance is fostering a more responsive and risk-aware financial landscape.

      ## 6. Market Trends and Investments
      The growth of AI agents has attracted significant investment, especially amidst the rising popularity of chatbots and generative AI technologies. Companies and entrepreneurs are eager to explore the potential of these systems, recognizing their ability to streamline operations and improve customer engagement.

      Conversely, corporations like Microsoft are taking strides to integrate AI agents into their product offerings, with enhancements to their Copilot 365 applications. This strategic move emphasizes the importance of AI literacy in the modern workplace and indicates the stabilizing of AI agents as essential business tools.

      ## 7. Future Predictions and Implications
      Experts predict that AI agents will transform essential aspects of work life. As we look toward the future, several anticipated changes include:

      - Enhanced integration of AI agents across all business functions, creating interconnected systems that leverage data from various departmental silos for comprehensive decision-making.
      - Continued advancement of AI technologies, resulting in smarter, more adaptable agents capable of learning and evolving from user interactions.
      - Increased regulatory scrutiny to ensure ethical use, especially concerning data privacy and employee surveillance as AI agents become more prevalent.

      To stay competitive and harness the full potential of AI agents, organizations must remain vigilant about latest developments in AI technology and consider continuous learning and adaptation in their strategic planning.

      ## 8. Conclusion
      The emergence of AI agents is undeniably reshaping the workplace landscape in 5. With their ability to automate tasks, enhance efficiency, and improve decision-making, AI agents are critical in driving operational success. Organizations must embrace and adapt to AI developments to thrive in an increasingly digital business environment.
      ```
    </CodeGroup>
  </Step>
</Steps>

<Check>
  Congratulations!

  You have successfully set up your crew project and are ready to start building your own agentic workflows!
</Check>

### Note on Consistency in Naming

The names you use in your YAML files (`agents.yaml` and `tasks.yaml`) should match the method names in your Python code.
For example, you can reference the agent for specific tasks from `tasks.yaml` file.
This naming consistency allows CrewAI to automatically link your configurations with your code; otherwise, your task won't recognize the reference properly.

#### Example References

<Tip>
  Note how we use the same name for the agent in the `agents.yaml` (`email_summarizer`) file as the method name in the `crew.py` (`email_summarizer`) file.
</Tip>

```yaml agents.yaml theme={null}
email_summarizer:
    role: >
      Email Summarizer
    goal: >
      Summarize emails into a concise and clear summary
    backstory: >
      You will create a 5 bullet point summary of the report
    llm: provider/model-id  # Add your choice of model here
```

<Tip>
  Note how we use the same name for the task in the `tasks.yaml` (`email_summarizer_task`) file as the method name in the `crew.py` (`email_summarizer_task`) file.
</Tip>

```yaml tasks.yaml theme={null}
email_summarizer_task:
    description: >
      Summarize the email into a 5 bullet point summary
    expected_output: >
      A 5 bullet point summary of the email
    agent: email_summarizer
    context:
      - reporting_task
      - research_task
```


## Deploying Your Crew

The easiest way to deploy your crew to production is through [CrewAI AMP](http://app.crewai.com).

Watch this video tutorial for a step-by-step demonstration of deploying your crew to [CrewAI AMP](http://app.crewai.com) using the CLI.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/3EqSV-CYDZA" title="CrewAI Deployment Guide" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<CardGroup cols={2}>
  <Card title="Deploy on Enterprise" icon="rocket" href="http://app.crewai.com">
    Get started with CrewAI AMP and deploy your crew in a production environment with just a few clicks.
  </Card>

  <Card title="Join the Community" icon="comments" href="https://community.crewai.com">
    Join our open source community to discuss ideas, share your projects, and connect with other CrewAI developers.
  </Card>
</CardGroup>



# AI Mind Tool
Source: https://docs.crewai.com/en/tools/ai-ml/aimindtool

The `AIMindTool` is designed to query data sources in natural language.


# `AIMindTool`


## Description

The `AIMindTool` is a wrapper around [AI-Minds](https://mindsdb.com/minds) provided by [MindsDB](https://mindsdb.com/). It allows you to query data sources in natural language by simply configuring their connection parameters. This tool is useful when you need answers to questions from your data stored in various data sources including PostgreSQL, MySQL, MariaDB, ClickHouse, Snowflake, and Google BigQuery.

Minds are AI systems that work similarly to large language models (LLMs) but go beyond by answering any question from any data. This is accomplished by:

* Selecting the most relevant data for an answer using parametric search
* Understanding the meaning and providing responses within the correct context through semantic search
* Delivering precise answers by analyzing data and using machine learning (ML) models


## Installation

To incorporate this tool into your project, you need to install the Minds SDK:

```shell  theme={null}
uv add minds-sdk
```


## Steps to Get Started

To effectively use the `AIMindTool`, follow these steps:

1. **Package Installation**: Confirm that the `crewai[tools]` and `minds-sdk` packages are installed in your Python environment.
2. **API Key Acquisition**: Sign up for a Minds account [here](https://mdb.ai/register), and obtain an API key.
3. **Environment Configuration**: Store your obtained API key in an environment variable named `MINDS_API_KEY` to facilitate its use by the tool.


## Example

The following example demonstrates how to initialize the tool and execute a query:

```python Code theme={null}
from crewai_tools import AIMindTool


# Initialize the AIMindTool
aimind_tool = AIMindTool(
    datasources=[
        {
            "description": "house sales data",
            "engine": "postgres",
            "connection_data": {
                "user": "demo_user",
                "password": "demo_password",
                "host": "samples.mindsdb.com",
                "port": 5432,
                "database": "demo",
                "schema": "demo_data"
            },
            "tables": ["house_sales"]
        }
    ]
)


# Run a natural language query
result = aimind_tool.run("How many 3 bedroom houses were sold in 2008?")
print(result)
```


## Parameters

The `AIMindTool` accepts the following parameters:

* **api\_key**: Optional. Your Minds API key. If not provided, it will be read from the `MINDS_API_KEY` environment variable.
* **datasources**: A list of dictionaries, each containing the following keys:
  * **description**: A description of the data contained in the datasource.
  * **engine**: The engine (or type) of the datasource.
  * **connection\_data**: A dictionary containing the connection parameters for the datasource.
  * **tables**: A list of tables that the data source will use. This is optional and can be omitted if all tables in the data source are to be used.

A list of supported data sources and their connection parameters can be found [here](https://docs.mdb.ai/docs/data_sources).


## Agent Integration Example

Here's how to integrate the `AIMindTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent
from crewai.project import agent
from crewai_tools import AIMindTool


# Initialize the tool
aimind_tool = AIMindTool(
    datasources=[
        {
            "description": "sales data",
            "engine": "postgres",
            "connection_data": {
                "user": "your_user",
                "password": "your_password",
                "host": "your_host",
                "port": 5432,
                "database": "your_db",
                "schema": "your_schema"
            },
            "tables": ["sales"]
        }
    ]
)


# Define an agent with the AIMindTool
@agent
def data_analyst(self) -> Agent:
    return Agent(
        config=self.agents_config["data_analyst"],
        allow_delegation=False,
        tools=[aimind_tool]
    )
```


## Conclusion

The `AIMindTool` provides a powerful way to query your data sources using natural language, making it easier to extract insights without writing complex SQL queries. By connecting to various data sources and leveraging AI-Minds technology, this tool enables agents to access and analyze data efficiently.



# Code Interpreter
Source: https://docs.crewai.com/en/tools/ai-ml/codeinterpretertool

The `CodeInterpreterTool` is a powerful tool designed for executing Python 3 code within a secure, isolated environment.


# `CodeInterpreterTool`


## Description

The `CodeInterpreterTool` enables CrewAI agents to execute Python 3 code that they generate autonomously. This functionality is particularly valuable as it allows agents to create code, execute it, obtain the results, and utilize that information to inform subsequent decisions and actions.

There are several ways to use this tool:

### Docker Container (Recommended)

This is the primary option. The code runs in a secure, isolated Docker container, ensuring safety regardless of its content.
Make sure Docker is installed and running on your system. If you don’t have it, you can install it from [here](https://docs.docker.com/get-docker/).

### Sandbox environment

If Docker is unavailable — either not installed or not accessible for any reason — the code will be executed in a restricted Python environment - called sandbox.
This environment is very limited, with strict restrictions on many modules and built-in functions.

### Unsafe Execution

**NOT RECOMMENDED FOR PRODUCTION**
This mode allows execution of any Python code, including dangerous calls to `sys, os..` and similar modules. [Check out](/en/tools/ai-ml/codeinterpretertool#enabling-unsafe-mode) how to enable this mode


## Logging

The `CodeInterpreterTool` logs the selected execution strategy to STDOUT


## Installation

To use this tool, you need to install the CrewAI tools package:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

The following example demonstrates how to use the `CodeInterpreterTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import CodeInterpreterTool


# Initialize the tool
code_interpreter = CodeInterpreterTool()


# Define an agent that uses the tool
programmer_agent = Agent(
    role="Python Programmer",
    goal="Write and execute Python code to solve problems",
    backstory="An expert Python programmer who can write efficient code to solve complex problems.",
    tools=[code_interpreter],
    verbose=True,
)


# Example task to generate and execute code
coding_task = Task(
    description="Write a Python function to calculate the Fibonacci sequence up to the 10th number and print the result.",
    expected_output="The Fibonacci sequence up to the 10th number.",
    agent=programmer_agent,
)


# Create and run the crew
crew = Crew(
    agents=[programmer_agent],
    tasks=[coding_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff()
```

You can also enable code execution directly when creating an agent:

```python Code theme={null}
from crewai import Agent


# Create an agent with code execution enabled
programmer_agent = Agent(
    role="Python Programmer",
    goal="Write and execute Python code to solve problems",
    backstory="An expert Python programmer who can write efficient code to solve complex problems.",
    allow_code_execution=True,  # This automatically adds the CodeInterpreterTool
    verbose=True,
)
```

### Enabling `unsafe_mode`

```python Code theme={null}
from crewai_tools import CodeInterpreterTool

code = """
import os
os.system("ls -la")
"""

CodeInterpreterTool(unsafe_mode=True).run(code=code)
```


## Parameters

The `CodeInterpreterTool` accepts the following parameters during initialization:

* **user\_dockerfile\_path**: Optional. Path to a custom Dockerfile to use for the code interpreter container.
* **user\_docker\_base\_url**: Optional. URL to the Docker daemon to use for running the container.
* **unsafe\_mode**: Optional. Whether to run code directly on the host machine instead of in a Docker container or sandbox. Default is `False`. Use with caution!
* **default\_image\_tag**: Optional. Default Docker image tag. Default is `code-interpreter:latest`

When using the tool with an agent, the agent will need to provide:

* **code**: Required. The Python 3 code to execute.
* **libraries\_used**: Optional. A list of libraries used in the code that need to be installed. Default is `[]`


## Agent Integration Example

Here's a more detailed example of how to integrate the `CodeInterpreterTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import CodeInterpreterTool


# Initialize the tool
code_interpreter = CodeInterpreterTool()


# Define an agent that uses the tool
data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze data using Python code",
    backstory="""You are an expert data analyst who specializes in using Python
    to analyze and visualize data. You can write efficient code to process
    large datasets and extract meaningful insights.""",
    tools=[code_interpreter],
    verbose=True,
)


# Create a task for the agent
analysis_task = Task(
    description="""
    Write Python code to:
    1. Generate a random dataset of 100 points with x and y coordinates
    2. Calculate the correlation coefficient between x and y
    3. Create a scatter plot of the data
    4. Print the correlation coefficient and save the plot as 'scatter.png'

    Make sure to handle any necessary imports and print the results.
    """,
    expected_output="The correlation coefficient and confirmation that the scatter plot has been saved.",
    agent=data_analyst,
)


# Run the task
crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff()
```


## Implementation Details

The `CodeInterpreterTool` uses Docker to create a secure environment for code execution:

```python Code theme={null}
class CodeInterpreterTool(BaseTool):
    name: str = "Code Interpreter"
    description: str = "Interprets Python3 code strings with a final print statement."
    args_schema: Type[BaseModel] = CodeInterpreterSchema
    default_image_tag: str = "code-interpreter:latest"

    def _run(self, **kwargs) -> str:
        code = kwargs.get("code", self.code)
        libraries_used = kwargs.get("libraries_used", [])

        if self.unsafe_mode:
            return self.run_code_unsafe(code, libraries_used)
        else:
            return self.run_code_safety(code, libraries_used)
```

The tool performs the following steps:

1. Verifies that the Docker image exists or builds it if necessary
2. Creates a Docker container with the current working directory mounted
3. Installs any required libraries specified by the agent
4. Executes the Python code in the container
5. Returns the output of the code execution
6. Cleans up by stopping and removing the container


## Security Considerations

By default, the `CodeInterpreterTool` runs code in an isolated Docker container, which provides a layer of security. However, there are still some security considerations to keep in mind:

1. The Docker container has access to the current working directory, so sensitive files could potentially be accessed.
2. If the Docker container is unavailable and the code needs to run safely, it will be executed in a sandbox environment. For security reasons, installing arbitrary libraries is not allowed
3. The `unsafe_mode` parameter allows code to be executed directly on the host machine, which should only be used in trusted environments.
4. Be cautious when allowing agents to install arbitrary libraries, as they could potentially include malicious code.


## Conclusion

The `CodeInterpreterTool` provides a powerful way for CrewAI agents to execute Python code in a relatively secure environment. By enabling agents to write and run code, it significantly expands their problem-solving capabilities, especially for tasks involving data analysis, calculations, or other computational work. This tool is particularly useful for agents that need to perform complex operations that are more efficiently expressed in code than in natural language.



# DALL-E Tool
Source: https://docs.crewai.com/en/tools/ai-ml/dalletool

The `DallETool` is a powerful tool designed for generating images from textual descriptions.


# `DallETool`


## Description

This tool is used to give the Agent the ability to generate images using the DALL-E model. It is a transformer-based model that generates images from textual descriptions.
This tool allows the Agent to generate images based on the text input provided by the user.


## Installation

Install the crewai\_tools package

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

Remember that when using this tool, the text must be generated by the Agent itself. The text must be a description of the image you want to generate.

```python Code theme={null}
from crewai_tools import DallETool

Agent(
    ...
    tools=[DallETool()],
)
```

If needed you can also tweak the parameters of the DALL-E model by passing them as arguments to the `DallETool` class. For example:

```python Code theme={null}
from crewai_tools import DallETool

dalle_tool = DallETool(model="dall-e-3",
                       size="1024x1024",
                       quality="standard",
                       n=1)

Agent(
    ...
    tools=[dalle_tool]
)
```

The parameters are based on the `client.images.generate` method from the OpenAI API. For more information on the parameters,
please refer to the [OpenAI API documentation](https://platform.openai.com/docs/guides/images/introduction?lang=python).



# LangChain Tool
Source: https://docs.crewai.com/en/tools/ai-ml/langchaintool

The `LangChainTool` is a wrapper for LangChain tools and query engines.


## `LangChainTool`

<Info>
  CrewAI seamlessly integrates with LangChain's comprehensive [list of tools](https://python.langchain.com/docs/integrations/tools/), all of which can be used with CrewAI.
</Info>

```python Code theme={null}
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper


# Set up your SERPER_API_KEY key in an .env file, eg:

# SERPER_API_KEY=<your api key>
load_dotenv()

search = GoogleSerperAPIWrapper()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about markets, companies, and trends."
    search: GoogleSerperAPIWrapper = Field(default_factory=GoogleSerperAPIWrapper)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"


# Create Agents
researcher = Agent(
    role='Research Analyst',
    goal='Gather current market data and trends',
    backstory="""You are an expert research analyst with years of experience in
    gathering market intelligence. You're known for your ability to find
    relevant and up-to-date market information and present it in a clear,
    actionable format.""",
    tools=[SearchTool()],
    verbose=True
)


# rest of the code ...
```


## Conclusion

Tools are pivotal in extending the capabilities of CrewAI agents, enabling them to undertake a broad spectrum of tasks and collaborate effectively.
When building solutions with CrewAI, leverage both custom and existing tools to empower your agents and enhance the AI ecosystem. Consider utilizing error handling, caching mechanisms,
and the flexibility of tool arguments to optimize your agents' performance and capabilities.



# LlamaIndex Tool
Source: https://docs.crewai.com/en/tools/ai-ml/llamaindextool

The `LlamaIndexTool` is a wrapper for LlamaIndex tools and query engines.


# `LlamaIndexTool`


## Description

The `LlamaIndexTool` is designed to be a general wrapper around LlamaIndex tools and query engines, enabling you to leverage LlamaIndex resources in terms of RAG/agentic pipelines as tools to plug into CrewAI agents. This tool allows you to seamlessly integrate LlamaIndex's powerful data processing and retrieval capabilities into your CrewAI workflows.


## Installation

To use this tool, you need to install LlamaIndex:

```shell  theme={null}
uv add llama-index
```


## Steps to Get Started

To effectively use the `LlamaIndexTool`, follow these steps:

1. **Install LlamaIndex**: Install the LlamaIndex package using the command above.
2. **Set Up LlamaIndex**: Follow the [LlamaIndex documentation](https://docs.llamaindex.ai/) to set up a RAG/agent pipeline.
3. **Create a Tool or Query Engine**: Create a LlamaIndex tool or query engine that you want to use with CrewAI.


## Example

The following examples demonstrate how to initialize the tool from different LlamaIndex components:

### From a LlamaIndex Tool

```python Code theme={null}
from crewai_tools import LlamaIndexTool
from crewai import Agent
from llama_index.core.tools import FunctionTool


# Example 1: Initialize from FunctionTool
def search_data(query: str) -> str:
    """Search for information in the data."""
    # Your implementation here
    return f"Results for: {query}"


# Create a LlamaIndex FunctionTool
og_tool = FunctionTool.from_defaults(
    search_data, 
    name="DataSearchTool",
    description="Search for information in the data"
)


# Wrap it with LlamaIndexTool
tool = LlamaIndexTool.from_tool(og_tool)


# Define an agent that uses the tool
@agent
def researcher(self) -> Agent:
    '''
    This agent uses the LlamaIndexTool to search for information.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        tools=[tool]
    )
```

### From LlamaHub Tools

```python Code theme={null}
from crewai_tools import LlamaIndexTool
from llama_index.tools.wolfram_alpha import WolframAlphaToolSpec


# Initialize from LlamaHub Tools
wolfram_spec = WolframAlphaToolSpec(app_id="your_app_id")
wolfram_tools = wolfram_spec.to_tool_list()
tools = [LlamaIndexTool.from_tool(t) for t in wolfram_tools]
```

### From a LlamaIndex Query Engine

```python Code theme={null}
from crewai_tools import LlamaIndexTool
from llama_index.core import VectorStoreIndex
from llama_index.core.readers import SimpleDirectoryReader


# Load documents
documents = SimpleDirectoryReader("./data").load_data()


# Create an index
index = VectorStoreIndex.from_documents(documents)


# Create a query engine
query_engine = index.as_query_engine()


# Create a LlamaIndexTool from the query engine
query_tool = LlamaIndexTool.from_query_engine(
    query_engine,
    name="Company Data Query Tool",
    description="Use this tool to lookup information in company documents"
)
```


## Class Methods

The `LlamaIndexTool` provides two main class methods for creating instances:

### from\_tool

Creates a `LlamaIndexTool` from a LlamaIndex tool.

```python Code theme={null}
@classmethod
def from_tool(cls, tool: Any, **kwargs: Any) -> "LlamaIndexTool":
    # Implementation details
```

### from\_query\_engine

Creates a `LlamaIndexTool` from a LlamaIndex query engine.

```python Code theme={null}
@classmethod
def from_query_engine(
    cls,
    query_engine: Any,
    name: Optional[str] = None,
    description: Optional[str] = None,
    return_direct: bool = False,
    **kwargs: Any,
) -> "LlamaIndexTool":
    # Implementation details
```


## Parameters

The `from_query_engine` method accepts the following parameters:

* **query\_engine**: Required. The LlamaIndex query engine to wrap.
* **name**: Optional. The name of the tool.
* **description**: Optional. The description of the tool.
* **return\_direct**: Optional. Whether to return the response directly. Default is `False`.


## Conclusion

The `LlamaIndexTool` provides a powerful way to integrate LlamaIndex's capabilities into CrewAI agents. By wrapping LlamaIndex tools and query engines, it enables agents to leverage sophisticated data retrieval and processing functionalities, enhancing their ability to work with complex information sources.



---

**Navigation:** [← Previous](./03-srclatestaidevelopmentcrewpy.md) | [Index](./index.md) | [Next →](./05-overview.md)
