# Multi-Agent System with CrewAI

This example demonstrates building a sophisticated multi-agent system using:
- **CrewAI**: Multi-agent orchestration framework
- **Anthropic Claude**: Advanced reasoning model for agent decisions
- **Tool Integration**: Custom tools for agents to use
- **Task Management**: Coordinating complex workflows

## Overview

A multi-agent system coordinates multiple specialized agents to solve complex problems. Each agent:
- Has specific roles and expertise
- Can use tools to gather information
- Collaborates with other agents
- Produces outputs for downstream agents

### Use Cases

- Content Creation: Research → Writing → Editing agents
- Customer Support: Classification → Resolution → Feedback agents
- Data Analysis: Collection → Processing → Reporting agents
- Software Development: Design → Implementation → Testing agents

## Features

- Define custom agents with specific roles and goals
- Create tools that agents can use
- Implement multi-step workflows and task dependencies
- Use Claude's advanced reasoning for agent decisions
- Integrate with external APIs and services
- Add memory and context sharing between agents

## Architecture

```
User Input/Task
    ↓
CrewAI Manager
    ↓
┌─────────────────────────────────┐
│  Agent 1 (Researcher)          │
│  - Search the web              │
│  - Read documents              │
│  - Summarize findings          │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│  Agent 2 (Writer)              │
│  - Write content               │
│  - Format output               │
│  - Add references              │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│  Agent 3 (Editor)              │
│  - Review content              │
│  - Check quality               │
│  - Provide feedback            │
└─────────────────────────────────┘
    ↓
Final Output
```

## Requirements

### System Requirements
- Python 3.9+
- pip or conda
- API keys: Anthropic, (optional: OpenAI, Serper for web search)

### Dependencies

```
crewai>=0.1.0
crewai-tools>=0.1.0
langchain>=0.1.0
langchain-anthropic>=0.1.0
anthropic>=0.7.0
```

See `requirements.txt` for complete list.

## Installation

### 1. Clone and Setup

```bash
cd examples/multi-agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file:

```env
# Anthropic API
ANTHROPIC_API_KEY=sk-ant-...

# Optional: Web search capability
SERPER_API_KEY=your_key_here

# Optional: ElevenLabs for voice
ELEVENLABS_API_KEY=your_key_here
```

## Usage

### Quick Start

```bash
# Run content creation workflow
python content_crew.py --topic "Claude Code Fundamentals"

# Run research and analysis workflow
python research_crew.py --query "How to build RAG applications"

# Interactive agent chat
python agent_chat.py
```

### Advanced Usage

```bash
# Use specific model
CLAUDE_MODEL=claude-3-5-sonnet-20241022 python content_crew.py --topic "AI Trends"

# Enable verbose output
python research_crew.py --query "AI Safety" --verbose

# Process batch of topics
python batch_process.py --input topics.txt --output results.json
```

## File Structure

```
multi-agent/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── config.py                # Configuration
├── content_crew.py          # Content creation workflow
├── research_crew.py         # Research and analysis workflow
├── agent_chat.py            # Interactive agent chat
├── batch_process.py         # Batch processing
├── agents/
│   ├── __init__.py
│   ├── researcher.py        # Research agent definitions
│   ├── writer.py            # Writer agent definitions
│   └── editor.py            # Editor agent definitions
├── tools/
│   ├── __init__.py
│   ├── search.py            # Web search tools
│   ├── document.py          # Document tools
│   └── custom_tools.py      # Custom tools
└── workflows/
    ├── __init__.py
    ├── content_workflow.py   # Content creation workflow
    └── research_workflow.py  # Research workflow
```

## Key Components

### 1. Agent Definition (`agents/researcher.py`)

```python
from crewai import Agent
from langchain_anthropic import ChatAnthropic

researcher = Agent(
    role="Research Analyst",
    goal="Find accurate, detailed information",
    backstory="Expert researcher with deep knowledge...",
    tools=[search_tool, read_file_tool],
    llm=ChatAnthropic(model="claude-3-5-sonnet-20241022"),
)
```

### 2. Tool Definition (`tools/search.py`)

```python
from crewai_tools import tool

@tool
def search_web(query: str) -> str:
    """Search the web for information"""
    # Implementation
    return results
```

### 3. Task Definition

```python
from crewai import Task

research_task = Task(
    description="Research the topic: {topic}",
    expected_output="Comprehensive research document",
    agent=researcher,
    tools=[search_tool],
)
```

### 4. Crew/Workflow Orchestration

```python
from crewai import Crew

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    verbose=True,
)

result = crew.kickoff(inputs={"topic": "AI Safety"})
```

## Example: Content Creation Workflow

A complete workflow with 3 agents:

1. **Researcher Agent**: Searches for information and gathers sources
2. **Writer Agent**: Creates compelling content based on research
3. **Editor Agent**: Reviews and refines the content

```bash
python content_crew.py --topic "Claude Code Advanced Features"
```

## Customization

### Create Custom Agent

```python
# In agents/custom.py
from crewai import Agent
from langchain_anthropic import ChatAnthropic

my_agent = Agent(
    role="Your Role",
    goal="Your specific goal",
    backstory="Detailed background...",
    tools=[your_tools],
    llm=ChatAnthropic(model="claude-3-5-sonnet-20241022"),
    allow_delegation=True,  # Can delegate to other agents
    verbose=True
)
```

### Create Custom Tool

```python
# In tools/custom_tools.py
from crewai_tools import tool
import requests

@tool
def my_tool(input: str) -> str:
    """
    Tool description for the agent to understand its purpose.
    """
    # Implementation
    return result
```

### Implement Custom Workflow

```python
# In workflows/my_workflow.py
from crewai import Crew, Task
from agents import agent1, agent2, agent3

task1 = Task(
    description="Do something",
    agent=agent1,
    expected_output="Result 1"
)

task2 = Task(
    description="Process {task1_result}",
    agent=agent2,
    expected_output="Result 2"
)

crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2],
    verbose=True
)
```

## Performance Tips

1. **Agent Specialization**: Give each agent a clear, focused role
2. **Tool Selection**: Provide only relevant tools to avoid confusion
3. **Context Sharing**: Use sequential task dependencies to pass context
4. **Model Selection**: Use appropriate Claude models for different tasks
5. **Timeout Settings**: Set reasonable timeouts for long-running tasks
6. **Memory**: Enable memory for complex multi-turn interactions

## Best Practices

### 1. Clear Agent Definitions

```python
# Good: Specific role and goal
agent = Agent(
    role="Technical Writer",
    goal="Create clear, accurate documentation",
    backstory="Expert technical writer with 10+ years experience..."
)

# Avoid: Vague definitions
agent = Agent(
    role="Helper",
    goal="Do things"
)
```

### 2. Appropriate Tool Sets

```python
# Good: Relevant tools for the task
researcher = Agent(
    role="Researcher",
    tools=[web_search_tool, document_reader_tool]
)

# Avoid: Too many tools causing confusion
researcher = Agent(
    role="Researcher",
    tools=[all_available_tools]  # Too many!
)
```

### 3. Clear Task Sequencing

```python
# Good: Clear dependencies and outputs
task1 = Task(description="Research...", agent=researcher)
task2 = Task(description="Write based on research...", agent=writer)
task3 = Task(description="Review the article...", agent=editor)

# Tasks are executed in order with outputs passed through
crew = Crew(agents=[researcher, writer, editor], tasks=[task1, task2, task3])
```

## Troubleshooting

### "Tool not found" Error
Ensure tools are properly imported and defined:
```python
from tools import search_tool
agent = Agent(tools=[search_tool])  # Make sure tool is passed
```

### Agent Loops/Repetition
Set max iterations and clear instructions:
```python
task = Task(
    description="...",
    agent=agent,
    max_iter=3  # Prevent infinite loops
)
```

### Memory Issues
Use conversation buffer memory with size limits:
```python
agent = Agent(
    role="...",
    memory_buffer_size=10  # Keep recent messages only
)
```

## Next Steps

1. **Extend with More Agents**: Add specialized agents for different domains
2. **Integrate Real Tools**: Connect to APIs, databases, services
3. **Add Error Handling**: Implement fallbacks and retry logic
4. **Performance Optimization**: Use caching and batching
5. **Deploy to Production**: Containerize and deploy as microservice

## Related Examples

- [RAG Application](../rag-app/) - Use RAG as a tool in multi-agent system
- [Chat Interface](../chat-interface/) - Build UI for agent interactions
- [Claude Code Automation](../claude-code-automation/) - Automate workflow setup

## Resources

- CrewAI Documentation: https://docs.crewai.com/
- CrewAI GitHub: https://github.com/joaomdmoura/crewai
- Anthropic Claude API: https://docs.anthropic.com/
- LangChain Tools: https://python.langchain.com/docs/integrations/tools/

---

*Example demonstrates the power of multi-agent systems for complex, collaborative problem-solving with CrewAI and Anthropic Claude.*
