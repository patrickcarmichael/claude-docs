# Agents

**Navigation:** [Index](./index.md) | [Next →](./02-generalist-gets-crewknowledge-only.md)

---

# Agents
Source: https://docs.crewai.com/en/concepts/agents

Detailed guide on creating and managing agents within the CrewAI framework.


## Overview of an Agent

In the CrewAI framework, an `Agent` is an autonomous unit that can:

* Perform specific tasks
* Make decisions based on its role and goal
* Use tools to accomplish objectives
* Communicate and collaborate with other agents
* Maintain memory of interactions
* Delegate tasks when allowed

<Tip>
  Think of an agent as a specialized team member with specific skills, expertise, and responsibilities. For example, a `Researcher` agent might excel at gathering and analyzing information, while a `Writer` agent might be better at creating content.
</Tip>

<Note type="info" title="Enterprise Enhancement: Visual Agent Builder">
  CrewAI AMP includes a Visual Agent Builder that simplifies agent creation and configuration without writing code. Design your agents visually and test them in real-time.

    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Visual Agent Builder Screenshot" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />

  The Visual Agent Builder enables:

  * Intuitive agent configuration with form-based interfaces
  * Real-time testing and validation
  * Template library with pre-configured agent types
  * Easy customization of agent attributes and behaviors
</Note>


## Agent Attributes

| Attribute                               | Parameter                | Type                                  | Description                                                                                              |
| :-------------------------------------- | :----------------------- | :------------------------------------ | :------------------------------------------------------------------------------------------------------- |
| **Role**                                | `role`                   | `str`                                 | Defines the agent's function and expertise within the crew.                                              |
| **Goal**                                | `goal`                   | `str`                                 | The individual objective that guides the agent's decision-making.                                        |
| **Backstory**                           | `backstory`              | `str`                                 | Provides context and personality to the agent, enriching interactions.                                   |
| **LLM** *(optional)*                    | `llm`                    | `Union[str, LLM, Any]`                | Language model that powers the agent. Defaults to the model specified in `OPENAI_MODEL_NAME` or "gpt-4". |
| **Tools** *(optional)*                  | `tools`                  | `List[BaseTool]`                      | Capabilities or functions available to the agent. Defaults to an empty list.                             |
| **Function Calling LLM** *(optional)*   | `function_calling_llm`   | `Optional[Any]`                       | Language model for tool calling, overrides crew's LLM if specified.                                      |
| **Max Iterations** *(optional)*         | `max_iter`               | `int`                                 | Maximum iterations before the agent must provide its best answer. Default is 20.                         |
| **Max RPM** *(optional)*                | `max_rpm`                | `Optional[int]`                       | Maximum requests per minute to avoid rate limits.                                                        |
| **Max Execution Time** *(optional)*     | `max_execution_time`     | `Optional[int]`                       | Maximum time (in seconds) for task execution.                                                            |
| **Verbose** *(optional)*                | `verbose`                | `bool`                                | Enable detailed execution logs for debugging. Default is False.                                          |
| **Allow Delegation** *(optional)*       | `allow_delegation`       | `bool`                                | Allow the agent to delegate tasks to other agents. Default is False.                                     |
| **Step Callback** *(optional)*          | `step_callback`          | `Optional[Any]`                       | Function called after each agent step, overrides crew callback.                                          |
| **Cache** *(optional)*                  | `cache`                  | `bool`                                | Enable caching for tool usage. Default is True.                                                          |
| **System Template** *(optional)*        | `system_template`        | `Optional[str]`                       | Custom system prompt template for the agent.                                                             |
| **Prompt Template** *(optional)*        | `prompt_template`        | `Optional[str]`                       | Custom prompt template for the agent.                                                                    |
| **Response Template** *(optional)*      | `response_template`      | `Optional[str]`                       | Custom response template for the agent.                                                                  |
| **Allow Code Execution** *(optional)*   | `allow_code_execution`   | `Optional[bool]`                      | Enable code execution for the agent. Default is False.                                                   |
| **Max Retry Limit** *(optional)*        | `max_retry_limit`        | `int`                                 | Maximum number of retries when an error occurs. Default is 2.                                            |
| **Respect Context Window** *(optional)* | `respect_context_window` | `bool`                                | Keep messages under context window size by summarizing. Default is True.                                 |
| **Code Execution Mode** *(optional)*    | `code_execution_mode`    | `Literal["safe", "unsafe"]`           | Mode for code execution: 'safe' (using Docker) or 'unsafe' (direct). Default is 'safe'.                  |
| **Multimodal** *(optional)*             | `multimodal`             | `bool`                                | Whether the agent supports multimodal capabilities. Default is False.                                    |
| **Inject Date** *(optional)*            | `inject_date`            | `bool`                                | Whether to automatically inject the current date into tasks. Default is False.                           |
| **Date Format** *(optional)*            | `date_format`            | `str`                                 | Format string for date when inject\_date is enabled. Default is "%Y-%m-%d" (ISO format).                 |
| **Reasoning** *(optional)*              | `reasoning`              | `bool`                                | Whether the agent should reflect and create a plan before executing a task. Default is False.            |
| **Max Reasoning Attempts** *(optional)* | `max_reasoning_attempts` | `Optional[int]`                       | Maximum number of reasoning attempts before executing the task. If None, will try until ready.           |
| **Embedder** *(optional)*               | `embedder`               | `Optional[Dict[str, Any]]`            | Configuration for the embedder used by the agent.                                                        |
| **Knowledge Sources** *(optional)*      | `knowledge_sources`      | `Optional[List[BaseKnowledgeSource]]` | Knowledge sources available to the agent.                                                                |
| **Use System Prompt** *(optional)*      | `use_system_prompt`      | `Optional[bool]`                      | Whether to use system prompt (for o1 model support). Default is True.                                    |


## Creating Agents

There are two ways to create agents in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define agents. We strongly recommend using this approach in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/agents.yaml` file and modify the template to match your requirements.

<Note>
  Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

  ```python Code theme={null}
  crew.kickoff(inputs={'topic': 'AI Agents'})
  ```
</Note>

Here's an example of how to configure agents using YAML:

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

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

```python Code theme={null}

# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process
from crewai.project import CrewBase, agent, crew
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  agents_config = "config/agents.yaml"

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
```

<Note>
  The names you use in your YAML files (`agents.yaml`) should match the method names in your Python code.
</Note>

### Direct Code Definition

You can create agents directly in code by instantiating the `Agent` class. Here's a comprehensive example showing all available parameters:

```python Code theme={null}
from crewai import Agent
from crewai_tools import SerperDevTool


# Create an agent with all available parameters
agent = Agent(
    role="Senior Data Scientist",
    goal="Analyze and interpret complex datasets to provide actionable insights",
    backstory="With over 10 years of experience in data science and machine learning, "
              "you excel at finding patterns in complex datasets.",
    llm="gpt-4",  # Default: OPENAI_MODEL_NAME or "gpt-4"
    function_calling_llm=None,  # Optional: Separate LLM for tool calling
    verbose=False,  # Default: False
    allow_delegation=False,  # Default: False
    max_iter=20,  # Default: 20 iterations
    max_rpm=None,  # Optional: Rate limit for API calls
    max_execution_time=None,  # Optional: Maximum execution time in seconds
    max_retry_limit=2,  # Default: 2 retries on error
    allow_code_execution=False,  # Default: False
    code_execution_mode="safe",  # Default: "safe" (options: "safe", "unsafe")
    respect_context_window=True,  # Default: True
    use_system_prompt=True,  # Default: True
    multimodal=False,  # Default: False
    inject_date=False,  # Default: False
    date_format="%Y-%m-%d",  # Default: ISO format
    reasoning=False,  # Default: False
    max_reasoning_attempts=None,  # Default: None
    tools=[SerperDevTool()],  # Optional: List of tools
    knowledge_sources=None,  # Optional: List of knowledge sources
    embedder=None,  # Optional: Custom embedder configuration
    system_template=None,  # Optional: Custom system prompt template
    prompt_template=None,  # Optional: Custom prompt template
    response_template=None,  # Optional: Custom response template
    step_callback=None,  # Optional: Callback function for monitoring
)
```

Let's break down some key parameter combinations for common use cases:

#### Basic Research Agent

```python Code theme={null}
research_agent = Agent(
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="You are an experienced researcher with attention to detail",
    tools=[SerperDevTool()],
    verbose=True  # Enable logging for debugging
)
```

#### Code Development Agent

```python Code theme={null}
dev_agent = Agent(
    role="Senior Python Developer",
    goal="Write and debug Python code",
    backstory="Expert Python developer with 10 years of experience",
    allow_code_execution=True,
    code_execution_mode="safe",  # Uses Docker for safety
    max_execution_time=300,  # 5-minute timeout
    max_retry_limit=3  # More retries for complex code tasks
)
```

#### Long-Running Analysis Agent

```python Code theme={null}
analysis_agent = Agent(
    role="Data Analyst",
    goal="Perform deep analysis of large datasets",
    backstory="Specialized in big data analysis and pattern recognition",
    memory=True,
    respect_context_window=True,
    max_rpm=10,  # Limit API calls
    function_calling_llm="gpt-4o-mini"  # Cheaper model for tool calls
)
```

#### Custom Template Agent

```python Code theme={null}
custom_agent = Agent(
    role="Customer Service Representative",
    goal="Assist customers with their inquiries",
    backstory="Experienced in customer support with a focus on satisfaction",
    system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",
)
```

#### Date-Aware Agent with Reasoning

```python Code theme={null}
strategic_agent = Agent(
    role="Market Analyst",
    goal="Track market movements with precise date references and strategic planning",
    backstory="Expert in time-sensitive financial analysis and strategic reporting",
    inject_date=True,  # Automatically inject current date into tasks
    date_format="%B %d, %Y",  # Format as "May 21, 2025"
    reasoning=True,  # Enable strategic planning
    max_reasoning_attempts=2,  # Limit planning iterations
    verbose=True
)
```

#### Reasoning Agent

```python Code theme={null}
reasoning_agent = Agent(
    role="Strategic Planner",
    goal="Analyze complex problems and create detailed execution plans",
    backstory="Expert strategic planner who methodically breaks down complex challenges",
    reasoning=True,  # Enable reasoning and planning
    max_reasoning_attempts=3,  # Limit reasoning attempts
    max_iter=30,  # Allow more iterations for complex planning
    verbose=True
)
```

#### Multimodal Agent

```python Code theme={null}
multimodal_agent = Agent(
    role="Visual Content Analyst",
    goal="Analyze and process both text and visual content",
    backstory="Specialized in multimodal analysis combining text and image understanding",
    multimodal=True,  # Enable multimodal capabilities
    verbose=True
)
```

### Parameter Details

#### Critical Parameters

* `role`, `goal`, and `backstory` are required and shape the agent's behavior
* `llm` determines the language model used (default: OpenAI's GPT-4)

#### Memory and Context

* `memory`: Enable to maintain conversation history
* `respect_context_window`: Prevents token limit issues
* `knowledge_sources`: Add domain-specific knowledge bases

#### Execution Control

* `max_iter`: Maximum attempts before giving best answer
* `max_execution_time`: Timeout in seconds
* `max_rpm`: Rate limiting for API calls
* `max_retry_limit`: Retries on error

#### Code Execution

* `allow_code_execution`: Must be True to run code
* `code_execution_mode`:
  * `"safe"`: Uses Docker (recommended for production)
  * `"unsafe"`: Direct execution (use only in trusted environments)

<Note>
  This runs a default Docker image. If you want to configure the docker image, the checkout the Code Interpreter Tool in the tools section.
  Add the code interpreter tool as a tool in the agent as a tool parameter.
</Note>

#### Advanced Features

* `multimodal`: Enable multimodal capabilities for processing text and visual content
* `reasoning`: Enable agent to reflect and create plans before executing tasks
* `inject_date`: Automatically inject current date into task descriptions

#### Templates

* `system_template`: Defines agent's core behavior
* `prompt_template`: Structures input format
* `response_template`: Formats agent responses

<Note>
  When using custom templates, ensure that both `system_template` and `prompt_template` are defined. The `response_template` is optional but recommended for consistent output formatting.
</Note>

<Note>
  When using custom templates, you can use variables like `{role}`, `{goal}`, and `{backstory}` in your templates. These will be automatically populated during execution.
</Note>


## Agent Tools

Agents can be equipped with various tools to enhance their capabilities. CrewAI supports tools from:

* [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools)
* [LangChain Tools](https://python.langchain.com/docs/integrations/tools)

Here's how to add tools to an agent:

```python Code theme={null}
from crewai import Agent
from crewai_tools import SerperDevTool, WikipediaTools


# Create tools
search_tool = SerperDevTool()
wiki_tool = WikipediaTools()


# Add tools to agent
researcher = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    tools=[search_tool, wiki_tool],
    verbose=True
)
```


## Agent Memory and Context

Agents can maintain memory of their interactions and use context from previous tasks. This is particularly useful for complex workflows where information needs to be retained across multiple tasks.

```python Code theme={null}
from crewai import Agent

analyst = Agent(
    role="Data Analyst",
    goal="Analyze and remember complex data patterns",
    memory=True,  # Enable memory
    verbose=True
)
```

<Note>
  When `memory` is enabled, the agent will maintain context across multiple interactions, improving its ability to handle complex, multi-step tasks.
</Note>


## Context Window Management

CrewAI includes sophisticated automatic context window management to handle situations where conversations exceed the language model's token limits. This powerful feature is controlled by the `respect_context_window` parameter.

### How Context Window Management Works

When an agent's conversation history grows too large for the LLM's context window, CrewAI automatically detects this situation and can either:

1. **Automatically summarize content** (when `respect_context_window=True`)
2. **Stop execution with an error** (when `respect_context_window=False`)

### Automatic Context Handling (`respect_context_window=True`)

This is the **default and recommended setting** for most use cases. When enabled, CrewAI will:

```python Code theme={null}

# Agent with automatic context management (default)
smart_agent = Agent(
    role="Research Analyst",
    goal="Analyze large documents and datasets",
    backstory="Expert at processing extensive information",
    respect_context_window=True,  # 🔑 Default: auto-handle context limits
    verbose=True
)
```

**What happens when context limits are exceeded:**

* ⚠️ **Warning message**: `"Context length exceeded. Summarizing content to fit the model context window."`
* 🔄 **Automatic summarization**: CrewAI intelligently summarizes the conversation history
* ✅ **Continued execution**: Task execution continues seamlessly with the summarized context
* 📝 **Preserved information**: Key information is retained while reducing token count

### Strict Context Limits (`respect_context_window=False`)

When you need precise control and prefer execution to stop rather than lose any information:

```python Code theme={null}

# Agent with strict context limits
strict_agent = Agent(
    role="Legal Document Reviewer",
    goal="Provide precise legal analysis without information loss",
    backstory="Legal expert requiring complete context for accurate analysis",
    respect_context_window=False,  # ❌ Stop execution on context limit
    verbose=True
)
```

**What happens when context limits are exceeded:**

* ❌ **Error message**: `"Context length exceeded. Consider using smaller text or RAG tools from crewai_tools."`
* 🛑 **Execution stops**: Task execution halts immediately
* 🔧 **Manual intervention required**: You need to modify your approach

### Choosing the Right Setting

#### Use `respect_context_window=True` (Default) when:

* **Processing large documents** that might exceed context limits
* **Long-running conversations** where some summarization is acceptable
* **Research tasks** where general context is more important than exact details
* **Prototyping and development** where you want robust execution

```python Code theme={null}

# Perfect for document processing
document_processor = Agent(
    role="Document Analyst",
    goal="Extract insights from large research papers",
    backstory="Expert at analyzing extensive documentation",
    respect_context_window=True,  # Handle large documents gracefully
    max_iter=50,  # Allow more iterations for complex analysis
    verbose=True
)
```

#### Use `respect_context_window=False` when:

* **Precision is critical** and information loss is unacceptable
* **Legal or medical tasks** requiring complete context
* **Code review** where missing details could introduce bugs
* **Financial analysis** where accuracy is paramount

```python Code theme={null}

# Perfect for precision tasks
precision_agent = Agent(
    role="Code Security Auditor",
    goal="Identify security vulnerabilities in code",
    backstory="Security expert requiring complete code context",
    respect_context_window=False,  # Prefer failure over incomplete analysis
    max_retry_limit=1,  # Fail fast on context issues
    verbose=True
)
```

### Alternative Approaches for Large Data

When dealing with very large datasets, consider these strategies:

#### 1. Use RAG Tools

```python Code theme={null}
from crewai_tools import RagTool


# Create RAG tool for large document processing
rag_tool = RagTool()

rag_agent = Agent(
    role="Research Assistant",
    goal="Query large knowledge bases efficiently",
    backstory="Expert at using RAG tools for information retrieval",
    tools=[rag_tool],  # Use RAG instead of large context windows
    respect_context_window=True,
    verbose=True
)
```

#### 2. Use Knowledge Sources

```python Code theme={null}

# Use knowledge sources instead of large prompts
knowledge_agent = Agent(
    role="Knowledge Expert",
    goal="Answer questions using curated knowledge",
    backstory="Expert at leveraging structured knowledge sources",
    knowledge_sources=[your_knowledge_sources],  # Pre-processed knowledge
    respect_context_window=True,
    verbose=True
)
```

### Context Window Best Practices

1. **Monitor Context Usage**: Enable `verbose=True` to see context management in action
2. **Design for Efficiency**: Structure tasks to minimize context accumulation
3. **Use Appropriate Models**: Choose LLMs with context windows suitable for your tasks
4. **Test Both Settings**: Try both `True` and `False` to see which works better for your use case
5. **Combine with RAG**: Use RAG tools for very large datasets instead of relying solely on context windows

### Troubleshooting Context Issues

**If you're getting context limit errors:**

```python Code theme={null}

# Quick fix: Enable automatic handling
agent.respect_context_window = True


# Better solution: Use RAG tools for large data
from crewai_tools import RagTool
agent.tools = [RagTool()]


# Alternative: Break tasks into smaller pieces

# Or use knowledge sources instead of large prompts
```

**If automatic summarization loses important information:**

```python Code theme={null}

# Disable auto-summarization and use RAG instead
agent = Agent(
    role="Detailed Analyst",
    goal="Maintain complete information accuracy",
    backstory="Expert requiring full context",
    respect_context_window=False,  # No summarization
    tools=[RagTool()],  # Use RAG for large data
    verbose=True
)
```

<Note>
  The context window management feature works automatically in the background. You don't need to call any special functions - just set `respect_context_window` to your preferred behavior and CrewAI handles the rest!
</Note>


## Direct Agent Interaction with `kickoff()`

Agents can be used directly without going through a task or crew workflow using the `kickoff()` method. This provides a simpler way to interact with an agent when you don't need the full crew orchestration capabilities.

### How `kickoff()` Works

The `kickoff()` method allows you to send messages directly to an agent and get a response, similar to how you would interact with an LLM but with all the agent's capabilities (tools, reasoning, etc.).

```python Code theme={null}
from crewai import Agent
from crewai_tools import SerperDevTool


# Create an agent
researcher = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    tools=[SerperDevTool()],
    verbose=True
)


# Use kickoff() to interact directly with the agent
result = researcher.kickoff("What are the latest developments in language models?")


# Access the raw response
print(result.raw)
```

### Parameters and Return Values

| Parameter         | Type                               | Description                                                               |
| :---------------- | :--------------------------------- | :------------------------------------------------------------------------ |
| `messages`        | `Union[str, List[Dict[str, str]]]` | Either a string query or a list of message dictionaries with role/content |
| `response_format` | `Optional[Type[Any]]`              | Optional Pydantic model for structured output                             |

The method returns a `LiteAgentOutput` object with the following properties:

* `raw`: String containing the raw output text
* `pydantic`: Parsed Pydantic model (if a `response_format` was provided)
* `agent_role`: Role of the agent that produced the output
* `usage_metrics`: Token usage metrics for the execution

### Structured Output

You can get structured output by providing a Pydantic model as the `response_format`:

```python Code theme={null}
from pydantic import BaseModel
from typing import List

class ResearchFindings(BaseModel):
    main_points: List[str]
    key_technologies: List[str]
    future_predictions: str


# Get structured output
result = researcher.kickoff(
    "Summarize the latest developments in AI for 2025",
    response_format=ResearchFindings
)


# Access structured data
print(result.pydantic.main_points)
print(result.pydantic.future_predictions)
```

### Multiple Messages

You can also provide a conversation history as a list of message dictionaries:

```python Code theme={null}
messages = [
    {"role": "user", "content": "I need information about large language models"},
    {"role": "assistant", "content": "I'd be happy to help with that! What specifically would you like to know?"},
    {"role": "user", "content": "What are the latest developments in 2025?"}
]

result = researcher.kickoff(messages)
```

### Async Support

An asynchronous version is available via `kickoff_async()` with the same parameters:

```python Code theme={null}
import asyncio

async def main():
    result = await researcher.kickoff_async("What are the latest developments in AI?")
    print(result.raw)

asyncio.run(main())
```

<Note>
  The `kickoff()` method uses a `LiteAgent` internally, which provides a simpler execution flow while preserving all of the agent's configuration (role, goal, backstory, tools, etc.).
</Note>


## Important Considerations and Best Practices

### Security and Code Execution

* When using `allow_code_execution`, be cautious with user input and always validate it
* Use `code_execution_mode: "safe"` (Docker) in production environments
* Consider setting appropriate `max_execution_time` limits to prevent infinite loops

### Performance Optimization

* Use `respect_context_window: true` to prevent token limit issues
* Set appropriate `max_rpm` to avoid rate limiting
* Enable `cache: true` to improve performance for repetitive tasks
* Adjust `max_iter` and `max_retry_limit` based on task complexity

### Memory and Context Management

* Leverage `knowledge_sources` for domain-specific information
* Configure `embedder` when using custom embedding models
* Use custom templates (`system_template`, `prompt_template`, `response_template`) for fine-grained control over agent behavior

### Advanced Features

* Enable `reasoning: true` for agents that need to plan and reflect before executing complex tasks
* Set appropriate `max_reasoning_attempts` to control planning iterations (None for unlimited attempts)
* Use `inject_date: true` to provide agents with current date awareness for time-sensitive tasks
* Customize the date format with `date_format` using standard Python datetime format codes
* Enable `multimodal: true` for agents that need to process both text and visual content

### Agent Collaboration

* Enable `allow_delegation: true` when agents need to work together
* Use `step_callback` to monitor and log agent interactions
* Consider using different LLMs for different purposes:
  * Main `llm` for complex reasoning
  * `function_calling_llm` for efficient tool usage

### Date Awareness and Reasoning

* Use `inject_date: true` to provide agents with current date awareness for time-sensitive tasks
* Customize the date format with `date_format` using standard Python datetime format codes
* Valid format codes include: %Y (year), %m (month), %d (day), %B (full month name), etc.
* Invalid date formats will be logged as warnings and will not modify the task description
* Enable `reasoning: true` for complex tasks that benefit from upfront planning and reflection

### Model Compatibility

* Set `use_system_prompt: false` for older models that don't support system messages
* Ensure your chosen `llm` supports the features you need (like function calling)


## Troubleshooting Common Issues

1. **Rate Limiting**: If you're hitting API rate limits:
   * Implement appropriate `max_rpm`
   * Use caching for repetitive operations
   * Consider batching requests

2. **Context Window Errors**: If you're exceeding context limits:
   * Enable `respect_context_window`
   * Use more efficient prompts
   * Clear agent memory periodically

3. **Code Execution Issues**: If code execution fails:
   * Verify Docker is installed for safe mode
   * Check execution permissions
   * Review code sandbox settings

4. **Memory Issues**: If agent responses seem inconsistent:
   * Check knowledge source configuration
   * Review conversation history management

Remember that agents are most effective when configured according to their specific use case. Take time to understand your requirements and adjust these parameters accordingly.



# CLI
Source: https://docs.crewai.com/en/concepts/cli

Learn how to use the CrewAI CLI to interact with CrewAI.

<Warning>Since release 0.140.0, CrewAI AMP started a process of migrating their login provider. As such, the authentication flow via CLI was updated. Users that use Google to login, or that created their account after July 3rd, 2025 will be unable to log in with older versions of the `crewai` library.</Warning>


## Overview

The CrewAI CLI provides a set of commands to interact with CrewAI, allowing you to create, train, run, and manage crews & flows.


## Installation

To use the CrewAI CLI, make sure you have CrewAI installed:

```shell Terminal theme={null}
pip install crewai
```


## Basic Usage

The basic structure of a CrewAI CLI command is:

```shell Terminal theme={null}
crewai [COMMAND] [OPTIONS] [ARGUMENTS]
```


## Available Commands

### 1. Create

Create a new crew or flow.

```shell Terminal theme={null}
crewai create [OPTIONS] TYPE NAME
```

* `TYPE`: Choose between "crew" or "flow"
* `NAME`: Name of the crew or flow

Example:

```shell Terminal theme={null}
crewai create crew my_new_crew
crewai create flow my_new_flow
```

### 2. Version

Show the installed version of CrewAI.

```shell Terminal theme={null}
crewai version [OPTIONS]
```

* `--tools`: (Optional) Show the installed version of CrewAI tools

Example:

```shell Terminal theme={null}
crewai version
crewai version --tools
```

### 3. Train

Train the crew for a specified number of iterations.

```shell Terminal theme={null}
crewai train [OPTIONS]
```

* `-n, --n_iterations INTEGER`: Number of iterations to train the crew (default: 5)
* `-f, --filename TEXT`: Path to a custom file for training (default: "trained\_agents\_data.pkl")

Example:

```shell Terminal theme={null}
crewai train -n 10 -f my_training_data.pkl
```

### 4. Replay

Replay the crew execution from a specific task.

```shell Terminal theme={null}
crewai replay [OPTIONS]
```

* `-t, --task_id TEXT`: Replay the crew from this task ID, including all subsequent tasks

Example:

```shell Terminal theme={null}
crewai replay -t task_123456
```

### 5. Log-tasks-outputs

Retrieve your latest crew\.kickoff() task outputs.

```shell Terminal theme={null}
crewai log-tasks-outputs
```

### 6. Reset-memories

Reset the crew memories (long, short, entity, latest\_crew\_kickoff\_outputs).

```shell Terminal theme={null}
crewai reset-memories [OPTIONS]
```

* `-l, --long`: Reset LONG TERM memory
* `-s, --short`: Reset SHORT TERM memory
* `-e, --entities`: Reset ENTITIES memory
* `-k, --kickoff-outputs`: Reset LATEST KICKOFF TASK OUTPUTS
* `-kn, --knowledge`: Reset KNOWLEDGE storage
* `-akn, --agent-knowledge`: Reset AGENT KNOWLEDGE storage
* `-a, --all`: Reset ALL memories

Example:

```shell Terminal theme={null}
crewai reset-memories --long --short
crewai reset-memories --all
```

### 7. Test

Test the crew and evaluate the results.

```shell Terminal theme={null}
crewai test [OPTIONS]
```

* `-n, --n_iterations INTEGER`: Number of iterations to test the crew (default: 3)
* `-m, --model TEXT`: LLM Model to run the tests on the Crew (default: "gpt-4o-mini")

Example:

```shell Terminal theme={null}
crewai test -n 5 -m gpt-3.5-turbo
```

### 8. Run

Run the crew or flow.

```shell Terminal theme={null}
crewai run
```

<Note>
  Starting from version 0.103.0, the `crewai run` command can be used to run both standard crews and flows. For flows, it automatically detects the type from pyproject.toml and runs the appropriate command. This is now the recommended way to run both crews and flows.
</Note>

<Note>
  Make sure to run these commands from the directory where your CrewAI project is set up.
  Some commands may require additional configuration or setup within your project structure.
</Note>

### 9. Chat

Starting in version `0.98.0`, when you run the `crewai chat` command, you start an interactive session with your crew. The AI assistant will guide you by asking for necessary inputs to execute the crew. Once all inputs are provided, the crew will execute its tasks.

After receiving the results, you can continue interacting with the assistant for further instructions or questions.

```shell Terminal theme={null}
crewai chat
```

<Note>
  Ensure you execute these commands from your CrewAI project's root directory.
</Note>

<Note>
  IMPORTANT: Set the `chat_llm` property in your `crew.py` file to enable this command.

  ```python  theme={null}
  @crew
  def crew(self) -> Crew:
      return Crew(
          agents=self.agents,
          tasks=self.tasks,
          process=Process.sequential,
          verbose=True,
          chat_llm="gpt-4o",  # LLM for chat orchestration
      )
  ```
</Note>

### 10. Deploy

Deploy the crew or flow to [CrewAI AMP](https://app.crewai.com).

* **Authentication**: You need to be authenticated to deploy to CrewAI AMP.
  You can login or create an account with:
  ```shell Terminal theme={null}
  crewai login
  ```

* **Create a deployment**: Once you are authenticated, you can create a deployment for your crew or flow from the root of your localproject.
  ```shell Terminal theme={null}
  crewai deploy create
  ```
  * Reads your local project configuration.
  * Prompts you to confirm the environment variables (like `OPENAI_API_KEY`, `SERPER_API_KEY`) found locally. These will be securely stored with the deployment on the Enterprise platform. Ensure your sensitive keys are correctly configured locally (e.g., in a `.env` file) before running this.

### 11. Organization Management

Manage your CrewAI AMP organizations.

```shell Terminal theme={null}
crewai org [COMMAND] [OPTIONS]
```

#### Commands:

* `list`: List all organizations you belong to

```shell Terminal theme={null}
crewai org list
```

* `current`: Display your currently active organization

```shell Terminal theme={null}
crewai org current
```

* `switch`: Switch to a specific organization

```shell Terminal theme={null}
crewai org switch <organization_id>
```

<Note>
  You must be authenticated to CrewAI AMP to use these organization management commands.
</Note>

* **Create a deployment** (continued):
  * Links the deployment to the corresponding remote GitHub repository (it usually detects this automatically).

* **Deploy the Crew**: Once you are authenticated, you can deploy your crew or flow to CrewAI AMP.
  ```shell Terminal theme={null}
  crewai deploy push
  ```
  * Initiates the deployment process on the CrewAI AMP platform.
  * Upon successful initiation, it will output the Deployment created successfully! message along with the Deployment Name and a unique Deployment ID (UUID).

* **Deployment Status**: You can check the status of your deployment with:
  ```shell Terminal theme={null}
  crewai deploy status
  ```
  This fetches the latest deployment status of your most recent deployment attempt (e.g., `Building Images for Crew`, `Deploy Enqueued`, `Online`).

* **Deployment Logs**: You can check the logs of your deployment with:
  ```shell Terminal theme={null}
  crewai deploy logs
  ```
  This streams the deployment logs to your terminal.

* **List deployments**: You can list all your deployments with:
  ```shell Terminal theme={null}
  crewai deploy list
  ```
  This lists all your deployments.

* **Delete a deployment**: You can delete a deployment with:
  ```shell Terminal theme={null}
  crewai deploy remove
  ```
  This deletes the deployment from the CrewAI AMP platform.

* **Help Command**: You can get help with the CLI with:
  ```shell Terminal theme={null}
  crewai deploy --help
  ```
  This shows the help message for the CrewAI Deploy CLI.

Watch this video tutorial for a step-by-step demonstration of deploying your crew to [CrewAI AMP](http://app.crewai.com) using the CLI.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/3EqSV-CYDZA" title="CrewAI Deployment Guide" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### 11. Login

Authenticate with CrewAI AMP using a secure device code flow (no email entry required).

```shell Terminal theme={null}
crewai login
```

What happens:

* A verification URL and short code are displayed in your terminal
* Your browser opens to the verification URL
* Enter/confirm the code to complete authentication

Notes:

* The OAuth2 provider and domain are configured via `crewai config` (defaults use `login.crewai.com`)
* After successful login, the CLI also attempts to authenticate to the Tool Repository automatically
* If you reset your configuration, run `crewai login` again to re-authenticate

### 12. API Keys

When running `crewai create crew` command, the CLI will show you a list of available LLM providers to choose from, followed by model selection for your chosen provider.

Once you've selected an LLM provider and model, you will be prompted for API keys.

#### Available LLM Providers

Here's a list of the most popular LLM providers suggested by the CLI:

* OpenAI
* Groq
* Anthropic
* Google Gemini
* SambaNova

When you select a provider, the CLI will then show you available models for that provider and prompt you to enter your API key.

#### Other Options

If you select "other", you will be able to select from a list of LiteLLM supported providers.

When you select a provider, the CLI will prompt you to enter the Key name and the API key.

See the following link for each provider's key name:

* [LiteLLM Providers](https://docs.litellm.ai/docs/providers)

### 13. Configuration Management

Manage CLI configuration settings for CrewAI.

```shell Terminal theme={null}
crewai config [COMMAND] [OPTIONS]
```

#### Commands:

* `list`: Display all CLI configuration parameters

```shell Terminal theme={null}
crewai config list
```

* `set`: Set a CLI configuration parameter

```shell Terminal theme={null}
crewai config set <key> <value>
```

* `reset`: Reset all CLI configuration parameters to default values

```shell Terminal theme={null}
crewai config reset
```

#### Available Configuration Parameters

* `enterprise_base_url`: Base URL of the CrewAI AMP instance
* `oauth2_provider`: OAuth2 provider used for authentication (e.g., workos, okta, auth0)
* `oauth2_audience`: OAuth2 audience value, typically used to identify the target API or resource
* `oauth2_client_id`: OAuth2 client ID issued by the provider, used during authentication requests
* `oauth2_domain`: OAuth2 provider's domain (e.g., your-org.auth0.com) used for issuing tokens

#### Examples

Display current configuration:

```shell Terminal theme={null}
crewai config list
```

Example output:

| Setting               | Value                                            | Description                                  |
| :-------------------- | :----------------------------------------------- | :------------------------------------------- |
| enterprise\_base\_url | [https://app.crewai.com](https://app.crewai.com) | Base URL of the CrewAI AMP instance          |
| org\_name             | Not set                                          | Name of the currently active organization    |
| org\_uuid             | Not set                                          | UUID of the currently active organization    |
| oauth2\_provider      | workos                                           | OAuth2 provider (e.g., workos, okta, auth0)  |
| oauth2\_audience      | client\_01YYY                                    | Audience identifying the target API/resource |
| oauth2\_client\_id    | client\_01XXX                                    | OAuth2 client ID issued by the provider      |
| oauth2\_domain        | login.crewai.com                                 | Provider domain (e.g., your-org.auth0.com)   |

Set the enterprise base URL:

```shell Terminal theme={null}
crewai config set enterprise_base_url https://my-enterprise.crewai.com
```

Set OAuth2 provider:

```shell Terminal theme={null}
crewai config set oauth2_provider auth0
```

Set OAuth2 domain:

```shell Terminal theme={null}
crewai config set oauth2_domain my-company.auth0.com
```

Reset all configuration to defaults:

```shell Terminal theme={null}
crewai config reset
```

<Tip>
  After resetting configuration, re-run `crewai login` to authenticate again.
</Tip>

<Tip>
  CrewAI CLI handles authentication to the Tool Repository automatically when adding packages to your project. Just append `crewai` before any `uv` command to use it. E.g. `crewai uv add requests`. For more information, see [Tool Repository](https://docs.crewai.com/enterprise/features/tool-repository) docs.
</Tip>

<Note>
  Configuration settings are stored in `~/.config/crewai/settings.json`. Some settings like organization name and UUID are read-only and managed through authentication and organization commands. Tool repository related settings are hidden and cannot be set directly by users.
</Note>



# Collaboration
Source: https://docs.crewai.com/en/concepts/collaboration

How to enable agents to work together, delegate tasks, and communicate effectively within CrewAI teams.


## Overview

Collaboration in CrewAI enables agents to work together as a team by delegating tasks and asking questions to leverage each other's expertise. When `allow_delegation=True`, agents automatically gain access to powerful collaboration tools.


## Quick Start: Enable Collaboration

```python  theme={null}
from crewai import Agent, Crew, Task


# Enable collaboration for agents
researcher = Agent(
    role="Research Specialist",
    goal="Conduct thorough research on any topic",
    backstory="Expert researcher with access to various sources",
    allow_delegation=True,  # 🔑 Key setting for collaboration
    verbose=True
)

writer = Agent(
    role="Content Writer", 
    goal="Create engaging content based on research",
    backstory="Skilled writer who transforms research into compelling content",
    allow_delegation=True,  # 🔑 Enables asking questions to other agents
    verbose=True
)


# Agents can now collaborate automatically
crew = Crew(
    agents=[researcher, writer],
    tasks=[...],
    verbose=True
)
```


## How Agent Collaboration Works

When `allow_delegation=True`, CrewAI automatically provides agents with two powerful tools:

### 1. **Delegate Work Tool**

Allows agents to assign tasks to teammates with specific expertise.

```python  theme={null}

# Agent automatically gets this tool:

# Delegate work to coworker(task: str, context: str, coworker: str)
```

### 2. **Ask Question Tool**

Enables agents to ask specific questions to gather information from colleagues.

```python  theme={null}

# Agent automatically gets this tool:

# Ask question to coworker(question: str, context: str, coworker: str)
```


## Collaboration in Action

Here's a complete example showing agents collaborating on a content creation task:

```python  theme={null}
from crewai import Agent, Crew, Task, Process


# Create collaborative agents
researcher = Agent(
    role="Research Specialist",
    goal="Find accurate, up-to-date information on any topic",
    backstory="""You're a meticulous researcher with expertise in finding 
    reliable sources and fact-checking information across various domains.""",
    allow_delegation=True,
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Create engaging, well-structured content",
    backstory="""You're a skilled content writer who excels at transforming 
    research into compelling, readable content for different audiences.""",
    allow_delegation=True,
    verbose=True
)

editor = Agent(
    role="Content Editor",
    goal="Ensure content quality and consistency",
    backstory="""You're an experienced editor with an eye for detail, 
    ensuring content meets high standards for clarity and accuracy.""",
    allow_delegation=True,
    verbose=True
)


# Create a task that encourages collaboration
article_task = Task(
    description="""Write a comprehensive 1000-word article about 'The Future of AI in Healthcare'.
    
    The article should include:
    - Current AI applications in healthcare
    - Emerging trends and technologies  
    - Potential challenges and ethical considerations
    - Expert predictions for the next 5 years
    
    Collaborate with your teammates to ensure accuracy and quality.""",
    expected_output="A well-researched, engaging 1000-word article with proper structure and citations",
    agent=writer  # Writer leads, but can delegate research to researcher
)


# Create collaborative crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[article_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
```


## Collaboration Patterns

### Pattern 1: Research → Write → Edit

```python  theme={null}
research_task = Task(
    description="Research the latest developments in quantum computing",
    expected_output="Comprehensive research summary with key findings and sources",
    agent=researcher
)

writing_task = Task(
    description="Write an article based on the research findings",
    expected_output="Engaging 800-word article about quantum computing",
    agent=writer,
    context=[research_task]  # Gets research output as context
)

editing_task = Task(
    description="Edit and polish the article for publication",
    expected_output="Publication-ready article with improved clarity and flow",
    agent=editor,
    context=[writing_task]  # Gets article draft as context
)
```

### Pattern 2: Collaborative Single Task

```python  theme={null}
collaborative_task = Task(
    description="""Create a marketing strategy for a new AI product.
    
    Writer: Focus on messaging and content strategy
    Researcher: Provide market analysis and competitor insights
    
    Work together to create a comprehensive strategy.""",
    expected_output="Complete marketing strategy with research backing",
    agent=writer  # Lead agent, but can delegate to researcher
)
```


## Hierarchical Collaboration

For complex projects, use a hierarchical process with a manager agent:

```python  theme={null}
from crewai import Agent, Crew, Task, Process


# Manager agent coordinates the team
manager = Agent(
    role="Project Manager",
    goal="Coordinate team efforts and ensure project success",
    backstory="Experienced project manager skilled at delegation and quality control",
    allow_delegation=True,
    verbose=True
)


# Specialist agents
researcher = Agent(
    role="Researcher",
    goal="Provide accurate research and analysis",
    backstory="Expert researcher with deep analytical skills",
    allow_delegation=False,  # Specialists focus on their expertise
    verbose=True
)

writer = Agent(
    role="Writer", 
    goal="Create compelling content",
    backstory="Skilled writer who creates engaging content",
    allow_delegation=False,
    verbose=True
)


# Manager-led task
project_task = Task(
    description="Create a comprehensive market analysis report with recommendations",
    expected_output="Executive summary, detailed analysis, and strategic recommendations",
    agent=manager  # Manager will delegate to specialists
)


# Hierarchical crew
crew = Crew(
    agents=[manager, researcher, writer],
    tasks=[project_task],
    process=Process.hierarchical,  # Manager coordinates everything
    manager_llm="gpt-4o",  # Specify LLM for manager
    verbose=True
)
```


## Best Practices for Collaboration

### 1. **Clear Role Definition**

```python  theme={null}

# ✅ Good: Specific, complementary roles
researcher = Agent(role="Market Research Analyst", ...)
writer = Agent(role="Technical Content Writer", ...)


# ❌ Avoid: Overlapping or vague roles  
agent1 = Agent(role="General Assistant", ...)
agent2 = Agent(role="Helper", ...)
```

### 2. **Strategic Delegation Enabling**

```python  theme={null}

# ✅ Enable delegation for coordinators and generalists
lead_agent = Agent(
    role="Content Lead",
    allow_delegation=True,  # Can delegate to specialists
    ...
)


# ✅ Disable for focused specialists (optional)
specialist_agent = Agent(
    role="Data Analyst", 
    allow_delegation=False,  # Focuses on core expertise
    ...
)
```

### 3. **Context Sharing**

```python  theme={null}

# ✅ Use context parameter for task dependencies
writing_task = Task(
    description="Write article based on research",
    agent=writer,
    context=[research_task],  # Shares research results
    ...
)
```

### 4. **Clear Task Descriptions**

```python  theme={null}

# ✅ Specific, actionable descriptions
Task(
    description="""Research competitors in the AI chatbot space.
    Focus on: pricing models, key features, target markets.
    Provide data in a structured format.""",
    ...
)


# ❌ Vague descriptions that don't guide collaboration
Task(description="Do some research about chatbots", ...)
```


## Troubleshooting Collaboration

### Issue: Agents Not Collaborating

**Symptoms:** Agents work in isolation, no delegation occurs

```python  theme={null}

# ✅ Solution: Ensure delegation is enabled
agent = Agent(
    role="...",
    allow_delegation=True,  # This is required!
    ...
)
```

### Issue: Too Much Back-and-Forth

**Symptoms:** Agents ask excessive questions, slow progress

```python  theme={null}

# ✅ Solution: Provide better context and specific roles
Task(
    description="""Write a technical blog post about machine learning.
    
    Context: Target audience is software developers with basic ML knowledge.
    Length: 1200 words
    Include: code examples, practical applications, best practices
    
    If you need specific technical details, delegate research to the researcher.""",
    ...
)
```

### Issue: Delegation Loops

**Symptoms:** Agents delegate back and forth indefinitely

```python  theme={null}

# ✅ Solution: Clear hierarchy and responsibilities
manager = Agent(role="Manager", allow_delegation=True)
specialist1 = Agent(role="Specialist A", allow_delegation=False)  # No re-delegation
specialist2 = Agent(role="Specialist B", allow_delegation=False)
```


## Advanced Collaboration Features

### Custom Collaboration Rules

```python  theme={null}

# Set specific collaboration guidelines in agent backstory
agent = Agent(
    role="Senior Developer",
    backstory="""You lead development projects and coordinate with team members.
    
    Collaboration guidelines:
    - Delegate research tasks to the Research Analyst
    - Ask the Designer for UI/UX guidance  
    - Consult the QA Engineer for testing strategies
    - Only escalate blocking issues to the Project Manager""",
    allow_delegation=True
)
```

### Monitoring Collaboration

```python  theme={null}
def track_collaboration(output):
    """Track collaboration patterns"""
    if "Delegate work to coworker" in output.raw:
        print("🤝 Delegation occurred")
    if "Ask question to coworker" in output.raw:
        print("❓ Question asked")

crew = Crew(
    agents=[...],
    tasks=[...],
    step_callback=track_collaboration,  # Monitor collaboration
    verbose=True
)
```


## Memory and Learning

Enable agents to remember past collaborations:

```python  theme={null}
agent = Agent(
    role="Content Lead",
    memory=True,  # Remembers past interactions
    allow_delegation=True,
    verbose=True
)
```

With memory enabled, agents learn from previous collaborations and improve their delegation decisions over time.


## Next Steps

* **Try the examples**: Start with the basic collaboration example
* **Experiment with roles**: Test different agent role combinations
* **Monitor interactions**: Use `verbose=True` to see collaboration in action
* **Optimize task descriptions**: Clear tasks lead to better collaboration
* **Scale up**: Try hierarchical processes for complex projects

Collaboration transforms individual AI agents into powerful teams that can tackle complex, multi-faceted challenges together.



# Crews
Source: https://docs.crewai.com/en/concepts/crews

Understanding and utilizing crews in the crewAI framework with comprehensive attributes and functionalities.


## Overview

A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.


## Crew Attributes

| Attribute                             | Parameters             | Description                                                                                                                                                                                           |   |
| :------------------------------------ | :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| **Tasks**                             | `tasks`                | A list of tasks assigned to the crew.                                                                                                                                                                 |   |
| **Agents**                            | `agents`               | A list of agents that are part of the crew.                                                                                                                                                           |   |
| **Process** *(optional)*              | `process`              | The process flow (e.g., sequential, hierarchical) the crew follows. Default is `sequential`.                                                                                                          |   |
| **Verbose** *(optional)*              | `verbose`              | The verbosity level for logging during execution. Defaults to `False`.                                                                                                                                |   |
| **Manager LLM** *(optional)*          | `manager_llm`          | The language model used by the manager agent in a hierarchical process. **Required when using a hierarchical process.**                                                                               |   |
| **Function Calling LLM** *(optional)* | `function_calling_llm` | If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew's LLM for function calling.              |   |
| **Config** *(optional)*               | `config`               | Optional configuration settings for the crew, in `Json` or `Dict[str, Any]` format.                                                                                                                   |   |
| **Max RPM** *(optional)*              | `max_rpm`              | Maximum requests per minute the crew adheres to during execution. Defaults to `None`.                                                                                                                 |   |
| **Memory** *(optional)*               | `memory`               | Utilized for storing execution memories (short-term, long-term, entity memory).                                                                                                                       |   |
| **Cache** *(optional)*                | `cache`                | Specifies whether to use a cache for storing the results of tools' execution. Defaults to `True`.                                                                                                     |   |
| **Embedder** *(optional)*             | `embedder`             | Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`.                                                                            |   |
| **Step Callback** *(optional)*        | `step_callback`        | A function that is called after each step of every agent. This can be used to log the agent's actions or to perform other operations; it won't override the agent-specific `step_callback`.           |   |
| **Task Callback** *(optional)*        | `task_callback`        | A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.                                                                      |   |
| **Share Crew** *(optional)*           | `share_crew`           | Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models.                                                  |   |
| **Output Log File** *(optional)*      | `output_log_file`      | Set to True to save logs as logs.txt in the current directory or provide a file path. Logs will be in JSON format if the filename ends in .json, otherwise .txt. Defaults to `None`.                  |   |
| **Manager Agent** *(optional)*        | `manager_agent`        | `manager` sets a custom agent that will be used as a manager.                                                                                                                                         |   |
| **Prompt File** *(optional)*          | `prompt_file`          | Path to the prompt JSON file to be used for the crew.                                                                                                                                                 |   |
| **Planning** *(optional)*             | `planning`             | Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks and this plan will be added to each task description. |   |
| **Planning LLM** *(optional)*         | `planning_llm`         | The language model used by the AgentPlanner in a planning process.                                                                                                                                    |   |
| **Knowledge Sources** *(optional)*    | `knowledge_sources`    | Knowledge sources available at the crew level, accessible to all the agents.                                                                                                                          |   |

<Tip>
  **Crew Max RPM**: The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents' `max_rpm` settings if you set it.
</Tip>


## Creating Crews

There are two ways to create crews in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define crews and is consistent with how agents and tasks are defined in CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, you can define your crew in a class that inherits from `CrewBase` and uses decorators to define agents, tasks, and the crew itself.

#### Example Crew Class with Decorators

```python code theme={null}
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class YourCrewName:
    """Description of your crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Paths to your YAML configuration files
    # To see an example agent and task defined in YAML, checkout the following:
    # - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    # - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def prepare_inputs(self, inputs):
        # Modify inputs before the crew starts
        inputs['additional_data'] = "Some extra information"
        return inputs

    @after_kickoff
    def process_output(self, output):
        # Modify output after the crew finishes
        output.raw += "\nProcessed after kickoff."
        return output

    @agent
    def agent_one(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_one'], # type: ignore[index]
            verbose=True
        )

    @agent
    def agent_two(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_two'], # type: ignore[index]
            verbose=True
        )

    @task
    def task_one(self) -> Task:
        return Task(
            config=self.tasks_config['task_one'] # type: ignore[index]
        )

    @task
    def task_two(self) -> Task:
        return Task(
            config=self.tasks_config['task_two'] # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically collected by the @agent decorator
            tasks=self.tasks,    # Automatically collected by the @task decorator.
            process=Process.sequential,
            verbose=True,
        )
```

How to run the above code:

```python code theme={null}
YourCrewName().crew().kickoff(inputs={"any": "input here"})
```

<Note>
  Tasks will be executed in the order they are defined.
</Note>

The `CrewBase` class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.

#### Decorators overview from `annotations.py`

CrewAI provides several decorators in the `annotations.py` file that are used to mark methods within your crew class for special handling:

* `@CrewBase`: Marks the class as a crew base class.
* `@agent`: Denotes a method that returns an `Agent` object.
* `@task`: Denotes a method that returns a `Task` object.
* `@crew`: Denotes the method that returns the `Crew` object.
* `@before_kickoff`: (Optional) Marks a method to be executed before the crew starts.
* `@after_kickoff`: (Optional) Marks a method to be executed after the crew finishes.

These decorators help in organizing your crew's structure and automatically collecting agents and tasks without manually listing them.

### Direct Code Definition (Alternative)

Alternatively, you can define the crew directly in code without using YAML configuration files.

```python code theme={null}
from crewai import Agent, Crew, Task, Process
from crewai_tools import YourCustomTool

class YourCrewName:
    def agent_one(self) -> Agent:
        return Agent(
            role="Data Analyst",
            goal="Analyze data trends in the market",
            backstory="An experienced data analyst with a background in economics",
            verbose=True,
            tools=[YourCustomTool()]
        )

    def agent_two(self) -> Agent:
        return Agent(
            role="Market Researcher",
            goal="Gather information on market dynamics",
            backstory="A diligent researcher with a keen eye for detail",
            verbose=True
        )

    def task_one(self) -> Task:
        return Task(
            description="Collect recent market data and identify trends.",
            expected_output="A report summarizing key trends in the market.",
            agent=self.agent_one()
        )

    def task_two(self) -> Task:
        return Task(
            description="Research factors affecting market dynamics.",
            expected_output="An analysis of factors influencing the market.",
            agent=self.agent_two()
        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.agent_one(), self.agent_two()],
            tasks=[self.task_one(), self.task_two()],
            process=Process.sequential,
            verbose=True
        )
```

How to run the above code:

```python code theme={null}
YourCrewName().crew().kickoff(inputs={})
```

In this example:

* Agents and tasks are defined directly within the class without decorators.
* We manually create and manage the list of agents and tasks.
* This approach provides more control but can be less maintainable for larger projects.


## Crew Output

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class.
This class provides a structured way to access results of the crew's execution, including various formats such as raw strings, JSON, and Pydantic models.
The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

### Crew Output Attributes

| Attribute        | Parameters     | Type                       | Description                                                                                          |
| :--------------- | :------------- | :------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Raw**          | `raw`          | `str`                      | The raw output of the crew. This is the default format for the output.                               |
| **Pydantic**     | `pydantic`     | `Optional[BaseModel]`      | A Pydantic model object representing the structured output of the crew.                              |
| **JSON Dict**    | `json_dict`    | `Optional[Dict[str, Any]]` | A dictionary representing the JSON output of the crew.                                               |
| **Tasks Output** | `tasks_output` | `List[TaskOutput]`         | A list of `TaskOutput` objects, each representing the output of a task in the crew.                  |
| **Token Usage**  | `token_usage`  | `Dict[str, Any]`           | A summary of token usage, providing insights into the language model's performance during execution. |

### Crew Output Methods and Properties

| Method/Property | Description                                                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------ |
| **json**        | Returns the JSON string representation of the crew output if the output format is JSON.           |
| **to\_dict**    | Converts the JSON and Pydantic outputs to a dictionary.                                           |
| \***\*str\*\*** | Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw. |

### Accessing Crew Outputs

Once a crew has been executed, its output can be accessed through the `output` attribute of the `Crew` object. The `CrewOutput` class provides various ways to interact with and present this output.

#### Example

```python Code theme={null}

# Example crew execution
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_article_task],
    verbose=True
)

crew_output = crew.kickoff()


# Accessing the crew output
print(f"Raw Output: {crew_output.raw}")
if crew_output.json_dict:
    print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
if crew_output.pydantic:
    print(f"Pydantic Output: {crew_output.pydantic}")
print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")
```


## Accessing Crew Logs

You can see real time log of the crew execution, by setting `output_log_file` as a `True(Boolean)` or a `file_name(str)`. Supports logging of events as both `file_name.txt` and `file_name.json`.
In case of `True(Boolean)` will save as `logs.txt`.

In case of `output_log_file` is set as `False(Boolean)` or `None`, the logs will not be populated.

```python Code theme={null}

# Save crew logs
crew = Crew(output_log_file = True)  # Logs will be saved as logs.txt
crew = Crew(output_log_file = file_name)  # Logs will be saved as file_name.txt
crew = Crew(output_log_file = file_name.txt)  # Logs will be saved as file_name.txt
crew = Crew(output_log_file = file_name.json)  # Logs will be saved as file_name.json
```


## Memory Utilization

Crews can utilize memory (short-term, long-term, and entity memory) to enhance their execution and learning over time. This feature allows crews to store and recall execution memories, aiding in decision-making and task execution strategies.


## Cache Utilization

Caches can be employed to store the results of tools' execution, making the process more efficient by reducing the need to re-execute identical tasks.


## Crew Usage Metrics

After the crew execution, you can access the `usage_metrics` attribute to view the language model (LLM) usage metrics for all tasks executed by the crew. This provides insights into operational efficiency and areas for improvement.

```python Code theme={null}

# Access the crew's usage metrics
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()
print(crew.usage_metrics)
```


## Crew Execution Process

* **Sequential Process**: Tasks are executed one after another, allowing for a linear flow of work.
* **Hierarchical Process**: A manager agent coordinates the crew, delegating tasks and validating outcomes before proceeding. **Note**: A `manager_llm` or `manager_agent` is required for this process and it's essential for validating the process flow.

### Kicking Off a Crew

Once your crew is assembled, initiate the workflow with the `kickoff()` method. This starts the execution process according to the defined process flow.

```python Code theme={null}

# Start the crew's task execution
result = my_crew.kickoff()
print(result)
```

### Different Ways to Kick Off a Crew

Once your crew is assembled, initiate the workflow with the appropriate kickoff method. CrewAI provides several methods for better control over the kickoff process: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.

* `kickoff()`: Starts the execution process according to the defined process flow.
* `kickoff_for_each()`: Executes tasks sequentially for each provided input event or item in the collection.
* `kickoff_async()`: Initiates the workflow asynchronously.
* `kickoff_for_each_async()`: Executes tasks concurrently for each provided input event or item, leveraging asynchronous processing.

```python Code theme={null}

# Start the crew's task execution
result = my_crew.kickoff()
print(result)


# Example of using kickoff_for_each
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
results = my_crew.kickoff_for_each(inputs=inputs_array)
for result in results:
    print(result)


# Example of using kickoff_async
inputs = {'topic': 'AI in healthcare'}
async_result = await my_crew.kickoff_async(inputs=inputs)
print(async_result)


# Example of using kickoff_for_each_async
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
async_results = await my_crew.kickoff_for_each_async(inputs=inputs_array)
for async_result in async_results:
    print(async_result)
```

These methods provide flexibility in how you manage and execute tasks within your crew, allowing for both synchronous and asynchronous workflows tailored to your needs.

### Replaying from a Specific Task

You can now replay from a specific task using our CLI command `replay`.

The replay feature in CrewAI allows you to replay from a specific task using the command-line interface (CLI). By running the command `crewai replay -t <task_id>`, you can specify the `task_id` for the replay process.

Kickoffs will now save the latest kickoffs returned task outputs locally for you to be able to replay from.

### Replaying from a Specific Task Using the CLI

To use the replay feature, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your CrewAI project is located.
3. Run the following command:

To view the latest kickoff task IDs, use:

```shell  theme={null}
crewai log-tasks-outputs
```

Then, to replay from a specific task, use:

```shell  theme={null}
crewai replay -t <task_id>
```

These commands let you replay from your latest kickoff tasks, still retaining context from previously executed tasks.



# Event Listeners
Source: https://docs.crewai.com/en/concepts/event-listener

Tap into CrewAI events to build custom integrations and monitoring


## Overview

CrewAI provides a powerful event system that allows you to listen for and react to various events that occur during the execution of your Crew. This feature enables you to build custom integrations, monitoring solutions, logging systems, or any other functionality that needs to be triggered based on CrewAI's internal events.


## How It Works

CrewAI uses an event bus architecture to emit events throughout the execution lifecycle. The event system is built on the following components:

1. **CrewAIEventsBus**: A singleton event bus that manages event registration and emission
2. **BaseEvent**: Base class for all events in the system
3. **BaseEventListener**: Abstract base class for creating custom event listeners

When specific actions occur in CrewAI (like a Crew starting execution, an Agent completing a task, or a tool being used), the system emits corresponding events. You can register handlers for these events to execute custom code when they occur.

<Note type="info" title="Enterprise Enhancement: Prompt Tracing">
  CrewAI AMP provides a built-in Prompt Tracing feature that leverages the event system to track, store, and visualize all prompts, completions, and associated metadata. This provides powerful debugging capabilities and transparency into your agent operations.

    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c02d5b7306bf7adaeadd77a018f8fea" alt="Prompt Tracing Dashboard" data-og-width="2244" width="2244" data-og-height="1422" height="1422" data-path="images/enterprise/traces-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e66e7c56a8848b69266563ea8cddfc4e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f590b3901aaa5994042c79426d78bd6c 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0ecb9dcb307e8f130f53393bd3abc12d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fc6fcfc51c4e8f4ce16d237228043d6 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=253eaed4ec34a35798dad42e9a388859 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec818e09bc20b3f72b1bcf1970804d13 2500w" />

  With Prompt Tracing you can:

  * View the complete history of all prompts sent to your LLM
  * Track token usage and costs
  * Debug agent reasoning failures
  * Share prompt sequences with your team
  * Compare different prompt strategies
  * Export traces for compliance and auditing
</Note>


## Creating a Custom Event Listener

To create a custom event listener, you need to:

1. Create a class that inherits from `BaseEventListener`
2. Implement the `setup_listeners` method
3. Register handlers for the events you're interested in
4. Create an instance of your listener in the appropriate file

Here's a simple example of a custom event listener class:

```python  theme={null}
from crewai.events import (
    CrewKickoffStartedEvent,
    CrewKickoffCompletedEvent,
    AgentExecutionCompletedEvent,
)
from crewai.events import BaseEventListener

class MyCustomListener(BaseEventListener):
    def __init__(self):
        super().__init__()

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(CrewKickoffStartedEvent)
        def on_crew_started(source, event):
            print(f"Crew '{event.crew_name}' has started execution!")

        @crewai_event_bus.on(CrewKickoffCompletedEvent)
        def on_crew_completed(source, event):
            print(f"Crew '{event.crew_name}' has completed execution!")
            print(f"Output: {event.output}")

        @crewai_event_bus.on(AgentExecutionCompletedEvent)
        def on_agent_execution_completed(source, event):
            print(f"Agent '{event.agent.role}' completed task")
            print(f"Output: {event.output}")
```


## Properly Registering Your Listener

Simply defining your listener class isn't enough. You need to create an instance of it and ensure it's imported in your application. This ensures that:

1. The event handlers are registered with the event bus
2. The listener instance remains in memory (not garbage collected)
3. The listener is active when events are emitted

### Option 1: Import and Instantiate in Your Crew or Flow Implementation

The most important thing is to create an instance of your listener in the file where your Crew or Flow is defined and executed:

#### For Crew-based Applications

Create and import your listener at the top of your Crew implementation file:

```python  theme={null}

# In your crew.py file
from crewai import Agent, Crew, Task
from my_listeners import MyCustomListener


# Create an instance of your listener
my_listener = MyCustomListener()

class MyCustomCrew:
    # Your crew implementation...

    def crew(self):
        return Crew(
            agents=[...],
            tasks=[...],
            # ...
        )
```

#### For Flow-based Applications

Create and import your listener at the top of your Flow implementation file:

```python  theme={null}

# In your main.py or flow.py file
from crewai.flow import Flow, listen, start
from my_listeners import MyCustomListener


# Create an instance of your listener
my_listener = MyCustomListener()

class MyCustomFlow(Flow):
    # Your flow implementation...

    @start()
    def first_step(self):
        # ...
```

This ensures that your listener is loaded and active when your Crew or Flow is executed.

### Option 2: Create a Package for Your Listeners

For a more structured approach, especially if you have multiple listeners:

1. Create a package for your listeners:

```
my_project/
  ├── listeners/
  │   ├── __init__.py
  │   ├── my_custom_listener.py
  │   └── another_listener.py
```

2. In `my_custom_listener.py`, define your listener class and create an instance:

```python  theme={null}

# my_custom_listener.py
from crewai.events import BaseEventListener

# ... import events ...

class MyCustomListener(BaseEventListener):
    # ... implementation ...


# Create an instance of your listener
my_custom_listener = MyCustomListener()
```

3. In `__init__.py`, import the listener instances to ensure they're loaded:

```python  theme={null}

# __init__.py
from .my_custom_listener import my_custom_listener
from .another_listener import another_listener


# Optionally export them if you need to access them elsewhere
__all__ = ['my_custom_listener', 'another_listener']
```

4. Import your listeners package in your Crew or Flow file:

```python  theme={null}

# In your crew.py or flow.py file
import my_project.listeners  # This loads all your listeners

class MyCustomCrew:
    # Your crew implementation...
```

This is how third-party event listeners are registered in the CrewAI codebase.


## Available Event Types

CrewAI provides a wide range of events that you can listen for:

### Crew Events

* **CrewKickoffStartedEvent**: Emitted when a Crew starts execution
* **CrewKickoffCompletedEvent**: Emitted when a Crew completes execution
* **CrewKickoffFailedEvent**: Emitted when a Crew fails to complete execution
* **CrewTestStartedEvent**: Emitted when a Crew starts testing
* **CrewTestCompletedEvent**: Emitted when a Crew completes testing
* **CrewTestFailedEvent**: Emitted when a Crew fails to complete testing
* **CrewTrainStartedEvent**: Emitted when a Crew starts training
* **CrewTrainCompletedEvent**: Emitted when a Crew completes training
* **CrewTrainFailedEvent**: Emitted when a Crew fails to complete training

### Agent Events

* **AgentExecutionStartedEvent**: Emitted when an Agent starts executing a task
* **AgentExecutionCompletedEvent**: Emitted when an Agent completes executing a task
* **AgentExecutionErrorEvent**: Emitted when an Agent encounters an error during execution

### Task Events

* **TaskStartedEvent**: Emitted when a Task starts execution
* **TaskCompletedEvent**: Emitted when a Task completes execution
* **TaskFailedEvent**: Emitted when a Task fails to complete execution
* **TaskEvaluationEvent**: Emitted when a Task is evaluated

### Tool Usage Events

* **ToolUsageStartedEvent**: Emitted when a tool execution is started
* **ToolUsageFinishedEvent**: Emitted when a tool execution is completed
* **ToolUsageErrorEvent**: Emitted when a tool execution encounters an error
* **ToolValidateInputErrorEvent**: Emitted when a tool input validation encounters an error
* **ToolExecutionErrorEvent**: Emitted when a tool execution encounters an error
* **ToolSelectionErrorEvent**: Emitted when there's an error selecting a tool

### Knowledge Events

* **KnowledgeRetrievalStartedEvent**: Emitted when a knowledge retrieval is started
* **KnowledgeRetrievalCompletedEvent**: Emitted when a knowledge retrieval is completed
* **KnowledgeQueryStartedEvent**: Emitted when a knowledge query is started
* **KnowledgeQueryCompletedEvent**: Emitted when a knowledge query is completed
* **KnowledgeQueryFailedEvent**: Emitted when a knowledge query fails
* **KnowledgeSearchQueryFailedEvent**: Emitted when a knowledge search query fails

### LLM Guardrail Events

* **LLMGuardrailStartedEvent**: Emitted when a guardrail validation starts. Contains details about the guardrail being applied and retry count.
* **LLMGuardrailCompletedEvent**: Emitted when a guardrail validation completes. Contains details about validation success/failure, results, and error messages if any.

### Flow Events

* **FlowCreatedEvent**: Emitted when a Flow is created
* **FlowStartedEvent**: Emitted when a Flow starts execution
* **FlowFinishedEvent**: Emitted when a Flow completes execution
* **FlowPlotEvent**: Emitted when a Flow is plotted
* **MethodExecutionStartedEvent**: Emitted when a Flow method starts execution
* **MethodExecutionFinishedEvent**: Emitted when a Flow method completes execution
* **MethodExecutionFailedEvent**: Emitted when a Flow method fails to complete execution

### LLM Events

* **LLMCallStartedEvent**: Emitted when an LLM call starts
* **LLMCallCompletedEvent**: Emitted when an LLM call completes
* **LLMCallFailedEvent**: Emitted when an LLM call fails
* **LLMStreamChunkEvent**: Emitted for each chunk received during streaming LLM responses

### Memory Events

* **MemoryQueryStartedEvent**: Emitted when a memory query is started. Contains the query, limit, and optional score threshold.
* **MemoryQueryCompletedEvent**: Emitted when a memory query is completed successfully. Contains the query, results, limit, score threshold, and query execution time.
* **MemoryQueryFailedEvent**: Emitted when a memory query fails. Contains the query, limit, score threshold, and error message.
* **MemorySaveStartedEvent**: Emitted when a memory save operation is started. Contains the value to be saved, metadata, and optional agent role.
* **MemorySaveCompletedEvent**: Emitted when a memory save operation is completed successfully. Contains the saved value, metadata, agent role, and save execution time.
* **MemorySaveFailedEvent**: Emitted when a memory save operation fails. Contains the value, metadata, agent role, and error message.
* **MemoryRetrievalStartedEvent**: Emitted when memory retrieval for a task prompt starts. Contains the optional task ID.
* **MemoryRetrievalCompletedEvent**: Emitted when memory retrieval for a task prompt completes successfully. Contains the task ID, memory content, and retrieval execution time.


## Event Handler Structure

Each event handler receives two parameters:

1. **source**: The object that emitted the event
2. **event**: The event instance, containing event-specific data

The structure of the event object depends on the event type, but all events inherit from `BaseEvent` and include:

* **timestamp**: The time when the event was emitted
* **type**: A string identifier for the event type

Additional fields vary by event type. For example, `CrewKickoffCompletedEvent` includes `crew_name` and `output` fields.


## Advanced Usage: Scoped Handlers

For temporary event handling (useful for testing or specific operations), you can use the `scoped_handlers` context manager:

```python  theme={null}
from crewai.events import crewai_event_bus, CrewKickoffStartedEvent

with crewai_event_bus.scoped_handlers():
    @crewai_event_bus.on(CrewKickoffStartedEvent)
    def temp_handler(source, event):
        print("This handler only exists within this context")

    # Do something that emits events


# Outside the context, the temporary handler is removed
```


## Use Cases

Event listeners can be used for a variety of purposes:

1. **Logging and Monitoring**: Track the execution of your Crew and log important events
2. **Analytics**: Collect data about your Crew's performance and behavior
3. **Debugging**: Set up temporary listeners to debug specific issues
4. **Integration**: Connect CrewAI with external systems like monitoring platforms, databases, or notification services
5. **Custom Behavior**: Trigger custom actions based on specific events


## Best Practices

1. **Keep Handlers Light**: Event handlers should be lightweight and avoid blocking operations
2. **Error Handling**: Include proper error handling in your event handlers to prevent exceptions from affecting the main execution
3. **Cleanup**: If your listener allocates resources, ensure they're properly cleaned up
4. **Selective Listening**: Only listen for events you actually need to handle
5. **Testing**: Test your event listeners in isolation to ensure they behave as expected

By leveraging CrewAI's event system, you can extend its functionality and integrate it seamlessly with your existing infrastructure.



# Flows
Source: https://docs.crewai.com/en/concepts/flows

Learn how to create and manage AI workflows using CrewAI Flows.


## Overview

CrewAI Flows is a powerful feature designed to streamline the creation and management of AI workflows. Flows allow developers to combine and coordinate coding tasks and Crews efficiently, providing a robust framework for building sophisticated AI automations.

Flows allow you to create structured, event-driven workflows. They provide a seamless way to connect multiple tasks, manage state, and control the flow of execution in your AI applications. With Flows, you can easily design and implement multi-step processes that leverage the full potential of CrewAI's capabilities.

1. **Simplified Workflow Creation**: Easily chain together multiple Crews and tasks to create complex AI workflows.

2. **State Management**: Flows make it super easy to manage and share state between different tasks in your workflow.

3. **Event-Driven Architecture**: Built on an event-driven model, allowing for dynamic and responsive workflows.

4. **Flexible Control Flow**: Implement conditional logic, loops, and branching within your workflows.


## Getting Started

Let's create a simple Flow where you will use OpenAI to generate a random city in one task and then use that city to generate a fun fact in another task.

```python Code theme={null}

from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion


class ExampleFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    def generate_city(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        print(f"Flow State ID: {self.state['id']}")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        # Store the city in our state
        self.state["city"] = random_city
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact



flow = ExampleFlow()
flow.plot()
result = flow.kickoff()

print(f"Generated fun fact: {result}")
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=18b381277b7b017abf7cb19bc5e03923" alt="Flow Visual image" data-og-width="1913" width="1913" data-og-height="989" height="989" data-path="images/crewai-flow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78864d97e0fc7f225a5313c9fb650900 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d87938c680e7aa201798075fe19dcf8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=36448790f7ca45e69ffdd3ceb2b2e713 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d10a3f4f9ea1c9b0428fbb66f0fca17 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=928a75232235b73e9308d4d9cfeaf0e8 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fa7022034285d0022ff07f97f6b675f7 2500w" />
In the above example, we have created a simple Flow that generates a random city using OpenAI and then generates a fun fact about that city. The Flow consists of two tasks: `generate_city` and `generate_fun_fact`. The `generate_city` task is the starting point of the Flow, and the `generate_fun_fact` task listens for the output of the `generate_city` task.

Each Flow instance automatically receives a unique identifier (UUID) in its state, which helps track and manage flow executions. The state can also store additional data (like the generated city and fun fact) that persists throughout the flow's execution.

When you run the Flow, it will:

1. Generate a unique ID for the flow state
2. Generate a random city and store it in the state
3. Generate a fun fact about that city and store it in the state
4. Print the results to the console

The state's unique ID and stored data can be useful for tracking flow executions and maintaining context between tasks.

**Note:** Ensure you have set up your `.env` file to store your `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

### @start()

The `@start()` decorator marks entry points for a Flow. You can:

* Declare multiple unconditional starts: `@start()`
* Gate a start on a prior method or router label: `@start("method_or_label")`
* Provide a callable condition to control when a start should fire

All satisfied `@start()` methods will execute (often in parallel) when the Flow begins or resumes.

### @listen()

The `@listen()` decorator is used to mark a method as a listener for the output of another task in the Flow. The method decorated with `@listen()` will be executed when the specified task emits an output. The method can access the output of the task it is listening to as an argument.

#### Usage

The `@listen()` decorator can be used in several ways:

1. **Listening to a Method by Name**: You can pass the name of the method you want to listen to as a string. When that method completes, the listener method will be triggered.

   ```python Code theme={null}
   @listen("generate_city")
   def generate_fun_fact(self, random_city):
       # Implementation
   ```

2. **Listening to a Method Directly**: You can pass the method itself. When that method completes, the listener method will be triggered.
   ```python Code theme={null}
   @listen(generate_city)
   def generate_fun_fact(self, random_city):
       # Implementation
   ```

### Flow Output

Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow.

#### Retrieving the Final Output

When you run a Flow, the final output is determined by the last method that completes. The `kickoff()` method returns the output of this final method.

Here's how you can access the final output:

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, listen, start

  class OutputExampleFlow(Flow):
      @start()
      def first_method(self):
          return "Output from first_method"

      @listen(first_method)
      def second_method(self, first_output):
          return f"Second method received: {first_output}"


  flow = OutputExampleFlow()
  flow.plot("my_flow_plot")
  final_output = flow.kickoff()

  print("---- Final Output ----")
  print(final_output)
  ```

  ```text Output theme={null}
  ---- Final Output ----
  Second method received: Output from first_method
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5" alt="Flow Visual image" data-og-width="2015" width="2015" data-og-height="1040" height="1040" data-path="images/crewai-flow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e6b4e913cd2d4bf4dc67bdcb2e59cceb 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=32155410f336267e29c64407e22ae57e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc414bc338e0475ae40aa3eedea0bd8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cfdf47937eb1f0a1f7e9ffdaab866e5a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ef7d71c39b8ea4ad865c514420df28d1 2500w" />

In this example, the `second_method` is the last method to complete, so its output will be the final output of the Flow.
The `kickoff()` method will return the final output, which is then printed to the console. The `plot()` method will generate the HTML file, which will help you understand the flow.

#### Accessing and Updating State

In addition to retrieving the final output, you can also access and update the state within your Flow. The state can be used to store and share data between different methods in the Flow. After the Flow has run, you can access the state to retrieve any information that was added or updated during the execution.

Here's an example of how to update and access the state:

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, listen, start
  from pydantic import BaseModel

  class ExampleState(BaseModel):
      counter: int = 0
      message: str = ""

  class StateExampleFlow(Flow[ExampleState]):

      @start()
      def first_method(self):
          self.state.message = "Hello from first_method"
          self.state.counter += 1

      @listen(first_method)
      def second_method(self):
          self.state.message += " - updated by second_method"
          self.state.counter += 1
          return self.state.message

  flow = StateExampleFlow()
  flow.plot("my_flow_plot")
  final_output = flow.kickoff()
  print(f"Final Output: {final_output}")
  print("Final State:")
  print(flow.state)
  ```

  ```text Output theme={null}
  Final Output: Hello from first_method - updated by second_method
  Final State:
  counter=2 message='Hello from first_method - updated by second_method'
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5" alt="Flow Visual image" data-og-width="2015" width="2015" data-og-height="1040" height="1040" data-path="images/crewai-flow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e6b4e913cd2d4bf4dc67bdcb2e59cceb 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=32155410f336267e29c64407e22ae57e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc414bc338e0475ae40aa3eedea0bd8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cfdf47937eb1f0a1f7e9ffdaab866e5a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ef7d71c39b8ea4ad865c514420df28d1 2500w" />

In this example, the state is updated by both `first_method` and `second_method`.
After the Flow has run, you can access the final state to see the updates made by these methods.

By ensuring that the final method's output is returned and providing access to the state, CrewAI Flows make it easy to integrate the results of your AI workflows into larger applications or systems,
while also maintaining and accessing the state throughout the Flow's execution.


## Flow State Management

Managing state effectively is crucial for building reliable and maintainable AI workflows. CrewAI Flows provides robust mechanisms for both unstructured and structured state management,
allowing developers to choose the approach that best fits their application's needs.

### Unstructured State Management

In unstructured state management, all state is stored in the `state` attribute of the `Flow` class.
This approach offers flexibility, enabling developers to add or modify state attributes on the fly without defining a strict schema.
Even with unstructured states, CrewAI Flows automatically generates and maintains a unique identifier (UUID) for each state instance.

```python Code theme={null}
from crewai.flow.flow import Flow, listen, start

class UnstructuredExampleFlow(Flow):

    @start()
    def first_method(self):
        # The state automatically includes an 'id' field
        print(f"State ID: {self.state['id']}")
        self.state['counter'] = 0
        self.state['message'] = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated again"

        print(f"State after third_method: {self.state}")


flow = UnstructuredExampleFlow()
flow.plot("my_flow_plot")
flow.kickoff()
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4" alt="Flow Visual image" data-og-width="1974" width="1974" data-og-height="1058" height="1058" data-path="images/crewai-flow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=192f7a8605d3a5c12b6b61aa4a23917f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d2315a6e69d8125e7e144f04180529f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=02eb5ffde3ef5936b2cf172160c72f72 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3fc5bb51802a4a5d641834e19d24e565 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=85414106ada4d15dcb7bccc086194b84 2500w" />

**Note:** The `id` field is automatically generated and preserved throughout the flow's execution. You don't need to manage or set it manually, and it will be maintained even when updating the state with new data.

**Key Points:**

* **Flexibility:** You can dynamically add attributes to `self.state` without predefined constraints.
* **Simplicity:** Ideal for straightforward workflows where state structure is minimal or varies significantly.

### Structured State Management

Structured state management leverages predefined schemas to ensure consistency and type safety across the workflow.
By using models like Pydantic's `BaseModel`, developers can define the exact shape of the state, enabling better validation and auto-completion in development environments.

Each state in CrewAI Flows automatically receives a unique identifier (UUID) to help track and manage state instances. This ID is automatically generated and managed by the Flow system.

```python Code theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel


class ExampleState(BaseModel):
    # Note: 'id' field is automatically added to all states
    counter: int = 0
    message: str = ""


class StructuredExampleFlow(Flow[ExampleState]):

    @start()
    def first_method(self):
        # Access the auto-generated ID if needed
        print(f"State ID: {self.state.id}")
        self.state.message = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state.counter += 1
        self.state.message += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state.counter += 1
        self.state.message += " - updated again"

        print(f"State after third_method: {self.state}")


flow = StructuredExampleFlow()
flow.kickoff()
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4" alt="Flow Visual image" data-og-width="1974" width="1974" data-og-height="1058" height="1058" data-path="images/crewai-flow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=192f7a8605d3a5c12b6b61aa4a23917f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d2315a6e69d8125e7e144f04180529f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=02eb5ffde3ef5936b2cf172160c72f72 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3fc5bb51802a4a5d641834e19d24e565 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=85414106ada4d15dcb7bccc086194b84 2500w" />

**Key Points:**

* **Defined Schema:** `ExampleState` clearly outlines the state structure, enhancing code readability and maintainability.
* **Type Safety:** Leveraging Pydantic ensures that state attributes adhere to the specified types, reducing runtime errors.
* **Auto-Completion:** IDEs can provide better auto-completion and error checking based on the defined state model.

### Choosing Between Unstructured and Structured State Management

* **Use Unstructured State Management when:**

  * The workflow's state is simple or highly dynamic.
  * Flexibility is prioritized over strict state definitions.
  * Rapid prototyping is required without the overhead of defining schemas.

* **Use Structured State Management when:**
  * The workflow requires a well-defined and consistent state structure.
  * Type safety and validation are important for your application's reliability.
  * You want to leverage IDE features like auto-completion and type checking for better developer experience.

By providing both unstructured and structured state management options, CrewAI Flows empowers developers to build AI workflows that are both flexible and robust, catering to a wide range of application requirements.


## Flow Persistence

The @persist decorator enables automatic state persistence in CrewAI Flows, allowing you to maintain flow state across restarts or different workflow executions. This decorator can be applied at either the class level or method level, providing flexibility in how you manage state persistence.

### Class-Level Persistence

When applied at the class level, the @persist decorator automatically persists all flow method states:

```python  theme={null}
@persist  # Using SQLiteFlowPersistence by default
class MyFlow(Flow[MyState]):
    @start()
    def initialize_flow(self):
        # This method will automatically have its state persisted
        self.state.counter = 1
        print("Initialized flow. State ID:", self.state.id)

    @listen(initialize_flow)
    def next_step(self):
        # The state (including self.state.id) is automatically reloaded
        self.state.counter += 1
        print("Flow state is persisted. Counter:", self.state.counter)
```

### Method-Level Persistence

For more granular control, you can apply @persist to specific methods:

```python  theme={null}
class AnotherFlow(Flow[dict]):
    @persist  # Persists only this method's state
    @start()
    def begin(self):
        if "runs" not in self.state:
            self.state["runs"] = 0
        self.state["runs"] += 1
        print("Method-level persisted runs:", self.state["runs"])
```

### How It Works

1. **Unique State Identification**
   * Each flow state automatically receives a unique UUID
   * The ID is preserved across state updates and method calls
   * Supports both structured (Pydantic BaseModel) and unstructured (dictionary) states

2. **Default SQLite Backend**
   * SQLiteFlowPersistence is the default storage backend
   * States are automatically saved to a local SQLite database
   * Robust error handling ensures clear messages if database operations fail

3. **Error Handling**
   * Comprehensive error messages for database operations
   * Automatic state validation during save and load
   * Clear feedback when persistence operations encounter issues

### Important Considerations

* **State Types**: Both structured (Pydantic BaseModel) and unstructured (dictionary) states are supported
* **Automatic ID**: The `id` field is automatically added if not present
* **State Recovery**: Failed or restarted flows can automatically reload their previous state
* **Custom Implementation**: You can provide your own FlowPersistence implementation for specialized storage needs

### Technical Advantages

1. **Precise Control Through Low-Level Access**
   * Direct access to persistence operations for advanced use cases
   * Fine-grained control via method-level persistence decorators
   * Built-in state inspection and debugging capabilities
   * Full visibility into state changes and persistence operations

2. **Enhanced Reliability**
   * Automatic state recovery after system failures or restarts
   * Transaction-based state updates for data integrity
   * Comprehensive error handling with clear error messages
   * Robust validation during state save and load operations

3. **Extensible Architecture**
   * Customizable persistence backend through FlowPersistence interface
   * Support for specialized storage solutions beyond SQLite
   * Compatible with both structured (Pydantic) and unstructured (dict) states
   * Seamless integration with existing CrewAI flow patterns

The persistence system's architecture emphasizes technical precision and customization options, allowing developers to maintain full control over state management while benefiting from built-in reliability features.


## Flow Control

### Conditional Logic: `or`

The `or_` function in Flows allows you to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, listen, or_, start

  class OrExampleFlow(Flow):

      @start()
      def start_method(self):
          return "Hello from the start method"

      @listen(start_method)
      def second_method(self):
          return "Hello from the second method"

      @listen(or_(start_method, second_method))
      def logger(self, result):
          print(f"Logger: {result}")



  flow = OrExampleFlow()
  flow.plot("my_flow_plot")
  flow.kickoff()
  ```

  ```text Output theme={null}
  Logger: Hello from the start method
  Logger: Hello from the second method
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=88ce9c9f10781b835f170847bc541a13" alt="Flow Visual image" data-og-width="2026" width="2026" data-og-height="1016" height="1016" data-path="images/crewai-flow-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=796ce622251faa461b481eb5d7cdcf70 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=260fcd89a5b3a6a42a25dd4f41e7c5c6 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b9268adb3abef93c7cce693a424a78ba 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=75f3ad392bfd6b72bd29d701675899d6 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dd771250338648e1f22c1463cb8e2ff0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b8e6fd63ec2ba23d9fa4f1dc2fd87143 2500w" />

When you run this Flow, the `logger` method will be triggered by the output of either the `start_method` or the `second_method`.
The `or_` function is used to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

### Conditional Logic: `and`

The `and_` function in Flows allows you to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, and_, listen, start

  class AndExampleFlow(Flow):

      @start()
      def start_method(self):
          self.state["greeting"] = "Hello from the start method"

      @listen(start_method)
      def second_method(self):
          self.state["joke"] = "What do computers eat? Microchips."

      @listen(and_(start_method, second_method))
      def logger(self):
          print("---- Logger ----")
          print(self.state)

  flow = AndExampleFlow()
  flow.plot()
  flow.kickoff()
  ```

  ```text Output theme={null}
  ---- Logger ----
  {'greeting': 'Hello from the start method', 'joke': 'What do computers eat? Microchips.'}
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=104318219be9d3502ac57ebb513aded7" alt="Flow Visual image" data-og-width="2062" width="2062" data-og-height="987" height="987" data-path="images/crewai-flow-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6e9cb9d2b1ec2cb2aee2df008d3696c9 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=07cbcc6de6e8c8ae5da6c02a6fe4b457 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afc6aad8f7276be4918527e553b5aa81 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e026919d9dff7ce0b0e592f4f2c0c4fd 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=03ea50c8681de2b8ea8cada6c0150e2c 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=61f9c7b0aceb69df6346ab2af321b779 2500w" />

When you run this Flow, the `logger` method will be triggered only when both the `start_method` and the `second_method` emit an output.
The `and_` function is used to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

### Router

The `@router()` decorator in Flows allows you to define conditional routing logic based on the output of a method.
You can specify different routes based on the output of the method, allowing you to control the flow of execution dynamically.

<CodeGroup>
  ```python Code theme={null}
  import random
  from crewai.flow.flow import Flow, listen, router, start
  from pydantic import BaseModel

  class ExampleState(BaseModel):
      success_flag: bool = False

  class RouterFlow(Flow[ExampleState]):

      @start()
      def start_method(self):
          print("Starting the structured flow")
          random_boolean = random.choice([True, False])
          self.state.success_flag = random_boolean

      @router(start_method)
      def second_method(self):
          if self.state.success_flag:
              return "success"
          else:
              return "failed"

      @listen("success")
      def third_method(self):
          print("Third method running")

      @listen("failed")
      def fourth_method(self):
          print("Fourth method running")


  flow = RouterFlow()
  flow.plot("my_flow_plot")
  flow.kickoff()
  ```

  ```text Output theme={null}
  Starting the structured flow
  Third method running
  Fourth method running
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f8cad73f073b4e936ef68d88545f1777" alt="Flow Visual image" data-og-width="1951" width="1951" data-og-height="1101" height="1101" data-path="images/crewai-flow-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9a8462f42a9d9e14748d35312553ec6c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78e66eabae15099e2ef1d0c314d3cb04 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a144377de810ed24f1d1aed1ba54d2d7 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2b17ebb2dd4eee4d086a8d0126a36c0d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4536b83aa7ff7e897f1193709ace944f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3b89cff817f7b4d05338f4a3a028f974 2500w" />

In the above example, the `start_method` generates a random boolean value and sets it in the state.
The `second_method` uses the `@router()` decorator to define conditional routing logic based on the value of the boolean.
If the boolean is `True`, the method returns `"success"`, and if it is `False`, the method returns `"failed"`.
The `third_method` and `fourth_method` listen to the output of the `second_method` and execute based on the returned value.

When you run this Flow, the output will change based on the random boolean value generated by the `start_method`.


## Adding Agents to Flows

Agents can be seamlessly integrated into your flows, providing a lightweight alternative to full Crews when you need simpler, focused task execution. Here's an example of how to use an Agent within a flow to perform market research:

```python  theme={null}
import asyncio
from typing import Any, Dict, List

from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

from crewai.agent import Agent
from crewai.flow.flow import Flow, listen, start



# Define a structured output format
class MarketAnalysis(BaseModel):
    key_trends: List[str] = Field(description="List of identified market trends")
    market_size: str = Field(description="Estimated market size")
    competitors: List[str] = Field(description="Major competitors in the space")



# Define flow state
class MarketResearchState(BaseModel):
    product: str = ""
    analysis: MarketAnalysis | None = None



# Create a flow class
class MarketResearchFlow(Flow[MarketResearchState]):
    @start()
    def initialize_research(self) -> Dict[str, Any]:
        print(f"Starting market research for {self.state.product}")
        return {"product": self.state.product}

    @listen(initialize_research)
    async def analyze_market(self) -> Dict[str, Any]:
        # Create an Agent for market research
        analyst = Agent(
            role="Market Research Analyst",
            goal=f"Analyze the market for {self.state.product}",
            backstory="You are an experienced market analyst with expertise in "
            "identifying market trends and opportunities.",
            tools=[SerperDevTool()],
            verbose=True,
        )

        # Define the research query
        query = f"""
        Research the market for {self.state.product}. Include:
        1. Key market trends
        2. Market size
        3. Major competitors

        Format your response according to the specified structure.
        """

        # Execute the analysis with structured output format
        result = await analyst.kickoff_async(query, response_format=MarketAnalysis)
        if result.pydantic:
            print("result", result.pydantic)
        else:
            print("result", result)

        # Return the analysis to update the state
        return {"analysis": result.pydantic}

    @listen(analyze_market)
    def present_results(self, analysis) -> None:
        print("\nMarket Analysis Results")
        print("=====================")

        if isinstance(analysis, dict):
            # If we got a dict with 'analysis' key, extract the actual analysis object
            market_analysis = analysis.get("analysis")
        else:
            market_analysis = analysis

        if market_analysis and isinstance(market_analysis, MarketAnalysis):
            print("\nKey Market Trends:")
            for trend in market_analysis.key_trends:
                print(f"- {trend}")

            print(f"\nMarket Size: {market_analysis.market_size}")

            print("\nMajor Competitors:")
            for competitor in market_analysis.competitors:
                print(f"- {competitor}")
        else:
            print("No structured analysis data available.")
            print("Raw analysis:", analysis)



# Usage example
async def run_flow():
    flow = MarketResearchFlow()
    flow.plot("MarketResearchFlowPlot")
    result = await flow.kickoff_async(inputs={"product": "AI-powered chatbots"})
    return result



# Run the flow
if __name__ == "__main__":
    asyncio.run(run_flow())
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c60457e1a2b9bc0ef957c373a88359b" alt="Flow Visual image" data-og-width="1933" width="1933" data-og-height="959" height="959" data-path="images/crewai-flow-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4e6a743b2b19cd86dadbbd015d0a0393 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=740f254bb03d60cd011911dab702ca77 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b93c5bde69019cdc34c143bcc0885743 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4eabe8d3536d6588a14157b60bc7a1e0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e76b5df7821722a59d3267f3a0eff3ed 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3a9775e3f5798ccb73e5feb7e53319fd 2500w" />

This example demonstrates several key features of using Agents in flows:

1. **Structured Output**: Using Pydantic models to define the expected output format (`MarketAnalysis`) ensures type safety and structured data throughout the flow.

2. **State Management**: The flow state (`MarketResearchState`) maintains context between steps and stores both inputs and outputs.

3. **Tool Integration**: Agents can use tools (like `WebsiteSearchTool`) to enhance their capabilities.


## Adding Crews to Flows

Creating a flow with multiple crews in CrewAI is straightforward.

You can generate a new CrewAI project that includes all the scaffolding needed to create a flow with multiple crews by running the following command:

```bash  theme={null}
crewai create flow name_of_flow
```

This command will generate a new CrewAI project with the necessary folder structure. The generated project includes a prebuilt crew called `poem_crew` that is already working. You can use this crew as a template by copying, pasting, and editing it to create other crews.

### Folder Structure

After running the `crewai create flow name_of_flow` command, you will see a folder structure similar to the following:

| Directory/File         | Description                                                         |
| :--------------------- | :------------------------------------------------------------------ |
| `name_of_flow/`        | Root directory for the flow.                                        |
| ├── `crews/`           | Contains directories for specific crews.                            |
| │ └── `poem_crew/`     | Directory for the "poem\_crew" with its configurations and scripts. |
| │ ├── `config/`        | Configuration files directory for the "poem\_crew".                 |
| │ │ ├── `agents.yaml`  | YAML file defining the agents for "poem\_crew".                     |
| │ │ └── `tasks.yaml`   | YAML file defining the tasks for "poem\_crew".                      |
| │ ├── `poem_crew.py`   | Script for "poem\_crew" functionality.                              |
| ├── `tools/`           | Directory for additional tools used in the flow.                    |
| │ └── `custom_tool.py` | Custom tool implementation.                                         |
| ├── `main.py`          | Main script for running the flow.                                   |
| ├── `README.md`        | Project description and instructions.                               |
| ├── `pyproject.toml`   | Configuration file for project dependencies and settings.           |
| └── `.gitignore`       | Specifies files and directories to ignore in version control.       |

### Building Your Crews

In the `crews` folder, you can define multiple crews. Each crew will have its own folder containing configuration files and the crew definition file. For example, the `poem_crew` folder contains:

* `config/agents.yaml`: Defines the agents for the crew.
* `config/tasks.yaml`: Defines the tasks for the crew.
* `poem_crew.py`: Contains the crew definition, including agents, tasks, and the crew itself.

You can copy, paste, and edit the `poem_crew` to create other crews.

### Connecting Crews in `main.py`

The `main.py` file is where you create your flow and connect the crews together. You can define your flow by using the `Flow` class and the decorators `@start` and `@listen` to specify the flow of execution.

Here's an example of how you can connect the `poem_crew` in the `main.py` file:

```python Code theme={null}
#!/usr/bin/env python
from random import randint

from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from .crews.poem_crew.poem_crew import PoemCrew

class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""

class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = PoemCrew().crew().kickoff(inputs={"sentence_count": self.state.sentence_count})

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)

def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot("PoemFlowPlot")

if __name__ == "__main__":
    kickoff()
    plot()
```

In this example, the `PoemFlow` class defines a flow that generates a sentence count, uses the `PoemCrew` to generate a poem, and then saves the poem to a file. The flow is kicked off by calling the `kickoff()` method. The PoemFlowPlot will be generated by `plot()` method.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5321ca5d1f3c662dc7cff6950ba46000" alt="Flow Visual image" data-og-width="1901" width="1901" data-og-height="1032" height="1032" data-path="images/crewai-flow-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5179beeb8c5b02eafdc1fce722004529 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=994b487041be812c1df343b23b5da9f2 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=244859a74e398490fa313beb91a3b9a7 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7ab59d8b176f60f2ba882eca41100ce1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c817c66b2d016c0b1bc203c32413d08e 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f5936902cb8e9e405a65ab3e1adbbd43 2500w" />

### Running the Flow

(Optional) Before running the flow, you can install the dependencies by running:

```bash  theme={null}
crewai install
```

Once all of the dependencies are installed, you need to activate the virtual environment by running:

```bash  theme={null}
source .venv/bin/activate
```

After activating the virtual environment, you can run the flow by executing one of the following commands:

```bash  theme={null}
crewai flow kickoff
```

or

```bash  theme={null}
uv run kickoff
```

The flow will execute, and you should see the output in the console.


## Plot Flows

Visualizing your AI workflows can provide valuable insights into the structure and execution paths of your flows. CrewAI offers a powerful visualization tool that allows you to generate interactive plots of your flows, making it easier to understand and optimize your AI workflows.

### What are Plots?

Plots in CrewAI are graphical representations of your AI workflows. They display the various tasks, their connections, and the flow of data between them. This visualization helps in understanding the sequence of operations, identifying bottlenecks, and ensuring that the workflow logic aligns with your expectations.

### How to Generate a Plot

CrewAI provides two convenient methods to generate plots of your flows:

#### Option 1: Using the `plot()` Method

If you are working directly with a flow instance, you can generate a plot by calling the `plot()` method on your flow object. This method will create an HTML file containing the interactive plot of your flow.

```python Code theme={null}

# Assuming you have a flow instance
flow.plot("my_flow_plot")
```

This will generate a file named `my_flow_plot.html` in your current directory. You can open this file in a web browser to view the interactive plot.

#### Option 2: Using the Command Line

If you are working within a structured CrewAI project, you can generate a plot using the command line. This is particularly useful for larger projects where you want to visualize the entire flow setup.

```bash  theme={null}
crewai flow plot
```

This command will generate an HTML file with the plot of your flow, similar to the `plot()` method. The file will be saved in your project directory, and you can open it in a web browser to explore the flow.

### Understanding the Plot

The generated plot will display nodes representing the tasks in your flow, with directed edges indicating the flow of execution. The plot is interactive, allowing you to zoom in and out, and hover over nodes to see additional details.

By visualizing your flows, you can gain a clearer understanding of the workflow's structure, making it easier to debug, optimize, and communicate your AI processes to others.

### Conclusion

Plotting your flows is a powerful feature of CrewAI that enhances your ability to design and manage complex AI workflows. Whether you choose to use the `plot()` method or the command line, generating plots will provide you with a visual representation of your workflows, aiding in both development and presentation.


## Next Steps

If you're interested in exploring additional examples of flows, we have a variety of recommendations in our examples repository. Here are four specific flow examples, each showcasing unique use cases to help you match your current problem type to a specific example:

1. **Email Auto Responder Flow**: This example demonstrates an infinite loop where a background job continually runs to automate email responses. It's a great use case for tasks that need to be performed repeatedly without manual intervention. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/email_auto_responder_flow)

2. **Lead Score Flow**: This flow showcases adding human-in-the-loop feedback and handling different conditional branches using the router. It's an excellent example of how to incorporate dynamic decision-making and human oversight into your workflows. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/lead-score-flow)

3. **Write a Book Flow**: This example excels at chaining multiple crews together, where the output of one crew is used by another. Specifically, one crew outlines an entire book, and another crew generates chapters based on the outline. Eventually, everything is connected to produce a complete book. This flow is perfect for complex, multi-step processes that require coordination between different tasks. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/write_a_book_with_flows)

4. **Meeting Assistant Flow**: This flow demonstrates how to broadcast one event to trigger multiple follow-up actions. For instance, after a meeting is completed, the flow can update a Trello board, send a Slack message, and save the results. It's a great example of handling multiple outcomes from a single event, making it ideal for comprehensive task management and notification systems. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/meeting_assistant_flow)

By exploring these examples, you can gain insights into how to leverage CrewAI Flows for various use cases, from automating repetitive tasks to managing complex, multi-step processes with dynamic decision-making and human feedback.

Also, check out our YouTube video on how to use flows in CrewAI below!

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/MTb5my6VOT8" title="CrewAI Flows overview" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />


## Running Flows

There are two ways to run a flow:

### Using the Flow API

You can run a flow programmatically by creating an instance of your flow class and calling the `kickoff()` method:

```python  theme={null}
flow = ExampleFlow()
result = flow.kickoff()
```

### Using the CLI

Starting from version 0.103.0, you can run flows using the `crewai run` command:

```shell  theme={null}
crewai run
```

This command automatically detects if your project is a flow (based on the `type = "flow"` setting in your pyproject.toml) and runs it accordingly. This is the recommended way to run flows from the command line.

For backward compatibility, you can also use:

```shell  theme={null}
crewai flow kickoff
```

However, the `crewai run` command is now the preferred method as it works for both crews and flows.



# Knowledge
Source: https://docs.crewai.com/en/concepts/knowledge

What is knowledge in CrewAI and how to use it.


## Overview

Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks.
Think of it as giving your agents a reference library they can consult while working.

<Info>
  Key benefits of using Knowledge:

  * Enhance agents with domain-specific information
  * Support decisions with real-world data
  * Maintain context across conversations
  * Ground responses in factual information
</Info>


## Quickstart Examples

<Tip>
  For file-based Knowledge Sources, make sure to place your files in a `knowledge` directory at the root of your project.
  Also, use relative paths from the `knowledge` directory when creating the source.
</Tip>

### Vector store (RAG) client configuration

CrewAI exposes a provider-neutral RAG client abstraction for vector stores. The default provider is ChromaDB, and Qdrant is supported as well. You can switch providers using configuration utilities.

Supported today:

* ChromaDB (default)
* Qdrant

```python Code theme={null}
from crewai.rag.config.utils import set_rag_config, get_rag_client, clear_rag_config


# ChromaDB (default)
from crewai.rag.chromadb.config import ChromaDBConfig
set_rag_config(ChromaDBConfig())
chromadb_client = get_rag_client()


# Qdrant
from crewai.rag.qdrant.config import QdrantConfig
set_rag_config(QdrantConfig())
qdrant_client = get_rag_client()


# Example operations (same API for any provider)
client = qdrant_client  # or chromadb_client
client.create_collection(collection_name="docs")
client.add_documents(
    collection_name="docs",
    documents=[{"id": "1", "content": "CrewAI enables collaborative AI agents."}],
)
results = client.search(collection_name="docs", query="collaborative agents", limit=3)

clear_rag_config()  # optional reset
```

This RAG client is separate from Knowledge’s built-in storage. Use it when you need direct vector-store control or custom retrieval pipelines.

### Basic String Knowledge Example

```python Code theme={null}
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


# Create a knowledge source
content = "Users name is John. He is 30 years old and lives in San Francisco."
string_source = StringKnowledgeSource(content=content)


# Create an LLM with a temperature of 0 to ensure deterministic outputs
llm = LLM(model="gpt-4o-mini", temperature=0)


# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="You are a master at understanding people and their preferences.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source], # Enable knowledge by adding the sources here
)

result = crew.kickoff(inputs={"question": "What city does John live in and how old is he?"})
```

### Web Content Knowledge Example

<Note>
  You need to install `docling` for the following example to work: `uv add docling`
</Note>

```python Code theme={null}
from crewai import LLM, Agent, Crew, Process, Task
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource


# Create a knowledge source from web content
content_source = CrewDoclingSource(
    file_paths=[
        "https://lilianweng.github.io/posts/2024-11-28-reward-hacking",
        "https://lilianweng.github.io/posts/2024-07-07-hallucination",
    ],
)


# Create an LLM with a temperature of 0 to ensure deterministic outputs
llm = LLM(model="gpt-4o-mini", temperature=0)


# Create an agent with the knowledge store
agent = Agent(
    role="About papers",
    goal="You know everything about the papers.",
    backstory="You are a master at understanding papers and their content.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Answer the following questions about the papers: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[content_source],
)

result = crew.kickoff(
    inputs={"question": "What is the reward hacking paper about? Be sure to provide sources."}
)
```


## Supported Knowledge Sources

CrewAI supports various types of knowledge sources out of the box:

<CardGroup cols={2}>
  <Card title="Text Sources" icon="text">
    * Raw strings
    * Text files (.txt)
    * PDF documents
  </Card>

  <Card title="Structured Data" icon="table">
    * CSV files
    * Excel spreadsheets
    * JSON documents
  </Card>
</CardGroup>

### Text File Knowledge Source

```python  theme={null}
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

text_source = TextFileKnowledgeSource(
    file_paths=["document.txt", "another.txt"]
)
```

### PDF Knowledge Source

```python  theme={null}
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_source = PDFKnowledgeSource(
    file_paths=["document.pdf", "another.pdf"]
)
```

### CSV Knowledge Source

```python  theme={null}
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource

csv_source = CSVKnowledgeSource(
    file_paths=["data.csv"]
)
```

### Excel Knowledge Source

```python  theme={null}
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource

excel_source = ExcelKnowledgeSource(
    file_paths=["spreadsheet.xlsx"]
)
```

### JSON Knowledge Source

```python  theme={null}
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

json_source = JSONKnowledgeSource(
    file_paths=["data.json"]
)
```

<Note>
  Please ensure that you create the ./knowledge folder. All source files (e.g., .txt, .pdf, .xlsx, .json) should be placed in this folder for centralized management.
</Note>


## Agent vs Crew Knowledge: Complete Guide

<Info>
  **Understanding Knowledge Levels**: CrewAI supports knowledge at both agent and crew levels. This section clarifies exactly how each works, when they're initialized, and addresses common misconceptions about dependencies.
</Info>

### How Knowledge Initialization Actually Works

Here's exactly what happens when you use knowledge:

#### Agent-Level Knowledge (Independent)

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


# Agent with its own knowledge - NO crew knowledge needed
specialist_knowledge = StringKnowledgeSource(
    content="Specialized technical information for this agent only"
)

specialist_agent = Agent(
    role="Technical Specialist",
    goal="Provide technical expertise",
    backstory="Expert in specialized technical domains",
    knowledge_sources=[specialist_knowledge]  # Agent-specific knowledge
)

task = Task(
    description="Answer technical questions",
    agent=specialist_agent,
    expected_output="Technical answer"
)


# No crew-level knowledge required
crew = Crew(
    agents=[specialist_agent],
    tasks=[task]
)

result = crew.kickoff()  # Agent knowledge works independently
```

#### What Happens During `crew.kickoff()`

When you call `crew.kickoff()`, here's the exact sequence:

```python  theme={null}

# During kickoff
for agent in self.agents:
    agent.crew = self  # Agent gets reference to crew
    agent.set_knowledge(crew_embedder=self.embedder)  # Agent knowledge initialized
    agent.create_agent_executor()
```

#### Storage Independence

Each knowledge level uses independent storage collections:

```python  theme={null}

# Agent knowledge storage
agent_collection_name = agent.role  # e.g., "Technical Specialist"


# Crew knowledge storage  
crew_collection_name = "crew"


# Both stored in same ChromaDB instance but different collections

# Path: ~/.local/share/CrewAI/{project}/knowledge/

#   ├── crew/                    # Crew knowledge collection

#   ├── Technical Specialist/    # Agent knowledge collection

#   └── Another Agent Role/      # Another agent's collection
```

### Complete Working Examples

#### Example 1: Agent-Only Knowledge

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


# Agent-specific knowledge
agent_knowledge = StringKnowledgeSource(
    content="Agent-specific information that only this agent needs"
)

agent = Agent(
    role="Specialist",
    goal="Use specialized knowledge",
    backstory="Expert with specific knowledge",
    knowledge_sources=[agent_knowledge],
    embedder={  # Agent can have its own embedder
        "provider": "openai",
        "config": {"model": "text-embedding-3-small"}
    }
)

task = Task(
    description="Answer using your specialized knowledge",
    agent=agent,
    expected_output="Answer based on agent knowledge"
)


# No crew knowledge needed
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()  # Works perfectly
```

#### Example 2: Both Agent and Crew Knowledge

```python  theme={null}

# Crew-wide knowledge (shared by all agents)
crew_knowledge = StringKnowledgeSource(
    content="Company policies and general information for all agents"
)


# Agent-specific knowledge
specialist_knowledge = StringKnowledgeSource(
    content="Technical specifications only the specialist needs"
)

specialist = Agent(
    role="Technical Specialist",
    goal="Provide technical expertise",
    backstory="Technical expert",
    knowledge_sources=[specialist_knowledge]  # Agent-specific
)

generalist = Agent(
    role="General Assistant", 
    goal="Provide general assistance",
    backstory="General helper"
    # No agent-specific knowledge
)

crew = Crew(
    agents=[specialist, generalist],
    tasks=[...],
    knowledge_sources=[crew_knowledge]  # Crew-wide knowledge
)


# Result:

# - specialist gets: crew_knowledge + specialist_knowledge

---

**Navigation:** [Index](./index.md) | [Next →](./02-generalist-gets-crewknowledge-only.md)
