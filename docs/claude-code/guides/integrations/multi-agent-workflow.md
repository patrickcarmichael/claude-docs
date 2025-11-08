# Multi-Agent Workflow Orchestration Guide

> Build sophisticated AI systems with multiple specialized agents working together using CrewAI or LangGraph

## Overview

This guide demonstrates how to create multi-agent systems where agents with different roles collaborate to solve complex problems. You'll learn to:

- Define specialized agents with specific roles
- Create tasks that agents execute independently or collaboratively
- Orchestrate workflows with sequential and parallel execution
- Implement agent memory and communication
- Monitor and debug multi-agent systems

## Architecture Comparison

### CrewAI: Role-Based Agent Teams

CrewAI treats agents as team members with defined roles, goals, and backstories:

```
┌──────────────────────────────────────────────┐
│            Crew (Team Manager)               │
├──────────────────────────────────────────────┤
│                                              │
│  ┌──────────────┐  ┌──────────────┐         │
│  │   Researcher │  │   Analyst    │         │
│  │    Agent     │  │    Agent     │         │
│  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                  │
│         └────────┬────────┘                  │
│                  │                           │
│         ┌────────▼────────┐                  │
│         │  Writer Agent   │                  │
│         └─────────────────┘                  │
│                                              │
└──────────────────────────────────────────────┘
```

### LangGraph: State-Based Agent Orchestration

LangGraph uses a graph-based approach with explicit state management:

```
Query → [Researcher Node] → [Analysis Node] → [Decision Node] → Response
           ↓                  ↓                  ↓
         State           State Updates       State
         Mgmt            & Validation        Output
```

## Option 1: CrewAI Implementation

### Prerequisites

```bash
pip install crewai langchain anthropic
```

### Step 1: Install CrewAI

```bash
pip install crewai[tools]
```

Create `crew_config.py`:

```python
from crewai import Agent, Task, Crew
from crewai_tools import tool
from anthropic import Anthropic
import json

# Initialize Anthropic client
client = Anthropic()

@tool
def search_information(query: str) -> str:
    """Search for information about a topic"""
    # In production, integrate with real search APIs
    return f"Search results for: {query}"

@tool
def analyze_content(content: str) -> str:
    """Analyze and summarize content"""
    return f"Analysis of content (length: {len(content)} chars)"

@tool
def generate_report(data: dict) -> str:
    """Generate a formatted report from data"""
    return json.dumps(data, indent=2)
```

### Step 2: Define Specialized Agents

```python
# agents.py
from crewai import Agent
from crewai_tools import tool
from anthropic import Anthropic

class AgentFactory:
    """Factory for creating specialized agents"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = Anthropic()

    def create_researcher_agent(self):
        """Create a research agent"""
        return Agent(
            role="Research Analyst",
            goal="Find and synthesize information on given topics",
            backstory="""You are a meticulous research analyst with expertise in
            finding reliable sources and extracting key information. You excel at
            breaking down complex topics into understandable components.""",
            tools=[search_information()],
            verbose=True,
        )

    def create_analyst_agent(self):
        """Create an analysis agent"""
        return Agent(
            role="Data Analyst",
            goal="Analyze information and identify patterns and insights",
            backstory="""You are an experienced data analyst with a sharp eye for
            patterns and trends. You excel at synthesizing information and drawing
            meaningful conclusions from complex datasets.""",
            tools=[analyze_content()],
            verbose=True,
        )

    def create_writer_agent(self):
        """Create a writing agent"""
        return Agent(
            role="Technical Writer",
            goal="Create clear, comprehensive reports based on analysis",
            backstory="""You are a skilled technical writer known for transforming
            complex information into clear, engaging narratives. You excel at
            structuring information logically and presenting it accessibly.""",
            tools=[generate_report()],
            verbose=True,
        )

    def create_quality_agent(self):
        """Create a quality assurance agent"""
        return Agent(
            role="Quality Assurance",
            goal="Verify accuracy and completeness of outputs",
            backstory="""You are a detail-oriented QA specialist who ensures all
            work meets high standards of accuracy and completeness. You excel at
            identifying gaps and suggesting improvements.""",
            verbose=True,
        )
```

### Step 3: Create Tasks

```python
# tasks.py
from crewai import Task

class TaskFactory:
    """Factory for creating specialized tasks"""

    @staticmethod
    def create_research_task(agent, topic: str):
        return Task(
            description=f"""Research the topic: {topic}
            Find at least 3 credible sources and key information points.
            Provide a comprehensive summary of findings.""",
            agent=agent,
            expected_output="Detailed research findings with source citations"
        )

    @staticmethod
    def create_analysis_task(agent, research_output: str):
        return Task(
            description=f"""Analyze the following research findings:
            {research_output}

            Identify patterns, trends, and key insights.
            Evaluate the reliability of information.
            Highlight any gaps or contradictions.""",
            agent=agent,
            expected_output="Analysis report with identified patterns and insights"
        )

    @staticmethod
    def create_writing_task(agent, analysis: str, topic: str):
        return Task(
            description=f"""Create a comprehensive report about {topic}
            Based on this analysis:
            {analysis}

            Structure the report with:
            - Executive Summary
            - Key Findings
            - Analysis & Insights
            - Recommendations
            - Conclusion""",
            agent=agent,
            expected_output="Well-structured technical report"
        )

    @staticmethod
    def create_qa_task(agent, report: str):
        return Task(
            description=f"""Review and quality check this report:
            {report}

            Verify:
            - Accuracy of information
            - Logical structure and flow
            - Completeness of analysis
            - Professional presentation""",
            agent=agent,
            expected_output="QA review with feedback and approval status"
        )
```

### Step 4: Orchestrate the Crew

```python
# main.py
from crewai import Crew, Process
from agents import AgentFactory
from tasks import TaskFactory
from anthropic import Anthropic

def create_research_crew(topic: str):
    """Create a crew for research and report generation"""

    agent_factory = AgentFactory(api_key="sk-ant-...")
    task_factory = TaskFactory()

    # Create agents
    researcher = agent_factory.create_researcher_agent()
    analyst = agent_factory.create_analyst_agent()
    writer = agent_factory.create_writer_agent()
    qa_agent = agent_factory.create_quality_agent()

    # Create tasks
    research_task = task_factory.create_research_task(researcher, topic)
    analysis_task = task_factory.create_analysis_task(analyst, "{research_output}")
    writing_task = task_factory.create_writing_task(writer, "{analysis_output}", topic)
    qa_task = task_factory.create_qa_task(qa_agent, "{writing_output}")

    # Create crew with sequential process
    crew = Crew(
        agents=[researcher, analyst, writer, qa_agent],
        tasks=[research_task, analysis_task, writing_task, qa_task],
        process=Process.sequential,  # Execute tasks in order
        verbose=True,
        memory=True,  # Enable crew memory
    )

    return crew

def main():
    topic = "Impact of AI on Modern Software Development"

    crew = create_research_crew(topic)
    result = crew.kickoff()

    print("=" * 80)
    print("CREW EXECUTION COMPLETED")
    print("=" * 80)
    print(result)

if __name__ == "__main__":
    main()
```

### Advanced: Hierarchical Crew

For complex workflows, use a manager agent:

```python
# hierarchical_crew.py
from crewai import Crew, Process

def create_hierarchical_crew(topic: str):
    """Create a hierarchical crew with a manager"""

    agent_factory = AgentFactory(api_key="sk-ant-...")

    # Create specialized agents
    researcher = agent_factory.create_researcher_agent()
    analyst = agent_factory.create_analyst_agent()
    writer = agent_factory.create_writer_agent()

    # Create manager agent
    manager = Agent(
        role="Project Manager",
        goal="Oversee research project and ensure quality outcomes",
        backstory="""You are an experienced project manager who coordinates
        teams efficiently and ensures project goals are met.""",
        verbose=True,
    )

    # Create crew with hierarchical process
    crew = Crew(
        agents=[manager, researcher, analyst, writer],
        tasks=[...],  # Define tasks here
        process=Process.hierarchical,
        manager_agent=manager,
        verbose=True,
    )

    return crew
```

## Option 2: LangGraph Implementation

### Setup

```bash
pip install langgraph langchain anthropic
```

### Step 1: Define State Schema

```python
# state.py
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import operator

class ResearchState(TypedDict):
    """State for research workflow"""
    query: str
    research_findings: list[str]
    analysis: str
    final_report: str
    messages: Annotated[Sequence[BaseMessage], operator.add]
    iteration: int
```

### Step 2: Create Node Functions

```python
# nodes.py
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from state import ResearchState

model = ChatAnthropic(
    model_name="claude-3-sonnet-20240229",
    api_key="sk-ant-..."
)

def research_node(state: ResearchState) -> dict:
    """Research node: gather information"""
    prompt = ChatPromptTemplate.from_template("""
    Research the following query: {query}

    Provide 3-5 key findings with details.
    Format as a bulleted list.""")

    chain = prompt | model
    result = chain.invoke({"query": state["query"]})

    return {
        "research_findings": [result.content],
        "messages": [result],
    }

def analysis_node(state: ResearchState) -> dict:
    """Analysis node: analyze findings"""
    findings = "\n".join(state["research_findings"])

    prompt = ChatPromptTemplate.from_template("""
    Analyze these research findings:
    {findings}

    Identify patterns, implications, and insights.""")

    chain = prompt | model
    result = chain.invoke({"findings": findings})

    return {
        "analysis": result.content,
        "messages": [result],
    }

def synthesis_node(state: ResearchState) -> dict:
    """Synthesis node: create final report"""
    prompt = ChatPromptTemplate.from_template("""
    Query: {query}

    Research Findings:
    {findings}

    Analysis:
    {analysis}

    Create a comprehensive report synthesizing all information.""")

    findings = "\n".join(state["research_findings"])
    chain = prompt | model

    result = chain.invoke({
        "query": state["query"],
        "findings": findings,
        "analysis": state["analysis"],
    })

    return {
        "final_report": result.content,
        "messages": [result],
    }

def quality_check_node(state: ResearchState) -> dict:
    """Quality check node"""
    prompt = ChatPromptTemplate.from_template("""
    Review this report for quality:
    {report}

    Provide feedback on:
    - Completeness
    - Accuracy
    - Clarity
    - Structure""")

    chain = prompt | model
    result = chain.invoke({"report": state["final_report"]})

    return {
        "messages": [result],
        "iteration": state["iteration"] + 1,
    }
```

### Step 3: Define Graph Edges

```python
# graph.py
from langgraph.graph import StateGraph, END
from state import ResearchState
from nodes import (
    research_node,
    analysis_node,
    synthesis_node,
    quality_check_node,
)

def create_research_graph():
    """Create the research workflow graph"""

    graph = StateGraph(ResearchState)

    # Add nodes
    graph.add_node("research", research_node)
    graph.add_node("analysis", analysis_node)
    graph.add_node("synthesis", synthesis_node)
    graph.add_node("quality_check", quality_check_node)

    # Define edges (workflow sequence)
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "synthesis")
    graph.add_edge("synthesis", "quality_check")
    graph.add_edge("quality_check", END)

    # Set entry point
    graph.set_entry_point("research")

    # Compile graph
    return graph.compile()

def run_research_workflow(query: str):
    """Execute the research workflow"""

    workflow = create_research_graph()

    initial_state = {
        "query": query,
        "research_findings": [],
        "analysis": "",
        "final_report": "",
        "messages": [],
        "iteration": 0,
    }

    # Execute workflow
    result = workflow.invoke(initial_state)

    return result
```

### Advanced: Conditional Routing

Add conditional logic based on state:

```python
# advanced_graph.py
from langgraph.graph import StateGraph
from state import ResearchState

def should_revise(state: ResearchState) -> str:
    """Determine if revision is needed"""
    if state["iteration"] < 2:
        return "revise"
    return "done"

def create_iterative_graph():
    """Create a graph with conditional routing"""

    graph = StateGraph(ResearchState)

    # Add nodes
    graph.add_node("research", research_node)
    graph.add_node("analysis", analysis_node)
    graph.add_node("synthesis", synthesis_node)
    graph.add_node("quality_check", quality_check_node)
    graph.add_node("revise", revise_node)

    # Add conditional edge
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "synthesis")
    graph.add_edge("synthesis", "quality_check")

    # Conditional routing after quality check
    graph.add_conditional_edges(
        "quality_check",
        should_revise,
        {
            "revise": "revise",
            "done": END,
        }
    )

    # Revision path
    graph.add_edge("revise", "analysis")

    graph.set_entry_point("research")
    return graph.compile()
```

## Comparison: CrewAI vs LangGraph

| Aspect | CrewAI | LangGraph |
|--------|--------|-----------|
| **Learning Curve** | Easy, agent-first | Moderate, graph-first |
| **Flexibility** | Good for standard workflows | Excellent for complex logic |
| **State Management** | Implicit, agent-based | Explicit, type-safe |
| **Conditional Routing** | Limited | Advanced |
| **Memory Management** | Built-in | Manual |
| **Debugging** | Tool-based | Graph visualization |
| **Best For** | Role-based teams | Complex state machines |

## Advanced Patterns

### Pattern 1: Agent Communication

```python
# agent_communication.py
from crewai import Agent, Task, Crew

class CommunicativeAgent(Agent):
    """Agent that can send messages to other agents"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_queue = []

    def send_message(self, recipient: str, message: str):
        """Send message to another agent"""
        self.message_queue.append({
            "to": recipient,
            "message": message,
            "timestamp": datetime.now()
        })

    def get_messages(self) -> list:
        """Retrieve messages for this agent"""
        messages = self.message_queue
        self.message_queue = []
        return messages
```

### Pattern 2: Dynamic Task Assignment

```python
# dynamic_tasks.py
from crewai import Crew

class DynamicCrew(Crew):
    """Crew that can dynamically assign tasks"""

    def assign_task(self, agent, task_description: str):
        """Dynamically assign a task to an agent"""
        from crewai import Task

        task = Task(
            description=task_description,
            agent=agent,
            expected_output="Task completion report"
        )

        self.tasks.append(task)

    def remove_task(self, task_id: str):
        """Remove a task from the crew"""
        self.tasks = [t for t in self.tasks if t.id != task_id]
```

### Pattern 3: Monitoring & Logging

```python
# monitoring.py
import logging
from typing import Any
from datetime import datetime

class WorkflowMonitor:
    """Monitor multi-agent workflow execution"""

    def __init__(self):
        self.logger = logging.getLogger("workflow")
        self.events = []

    def log_agent_start(self, agent_name: str, task: str):
        """Log when agent starts task"""
        event = {
            "timestamp": datetime.now(),
            "type": "agent_start",
            "agent": agent_name,
            "task": task
        }
        self.events.append(event)
        self.logger.info(f"Agent {agent_name} started: {task}")

    def log_agent_completion(self, agent_name: str, result: str):
        """Log when agent completes task"""
        event = {
            "timestamp": datetime.now(),
            "type": "agent_complete",
            "agent": agent_name,
            "result_length": len(result)
        }
        self.events.append(event)
        self.logger.info(f"Agent {agent_name} completed")

    def get_timeline(self) -> list:
        """Get execution timeline"""
        return sorted(self.events, key=lambda x: x["timestamp"])
```

## Production Deployment

### Docker Configuration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

CMD ["python", "main.py"]
```

### Requirements

```txt
# requirements.txt
crewai[tools]>=0.1.0
langgraph>=0.0.1
langchain>=0.1.0
anthropic>=0.7.0
python-dotenv>=1.0.0
pydantic>=2.0.0
```

## Testing & Validation

### Unit Tests

```python
# test_agents.py
import pytest
from agents import AgentFactory

@pytest.fixture
def agent_factory():
    return AgentFactory(api_key="test-key")

def test_researcher_agent_creation(agent_factory):
    agent = agent_factory.create_researcher_agent()
    assert agent.role == "Research Analyst"
    assert len(agent.tools) > 0

def test_analyst_agent_creation(agent_factory):
    agent = agent_factory.create_analyst_agent()
    assert agent.role == "Data Analyst"
```

### Integration Tests

```python
# test_workflow.py
import pytest
from main import create_research_crew

@pytest.mark.asyncio
async def test_complete_workflow():
    crew = create_research_crew("Test Topic")
    result = crew.kickoff()

    assert result is not None
    assert len(result) > 0
```

## Related Resources

- [CrewAI Documentation](../../ai-frameworks/crewai/)
- [LangGraph Documentation](../../ai-frameworks/langgraph/)
- [LangChain Integration](../../ai-frameworks/langchain/)
- [Claude Code Sub-Agents](../../features/sub-agents.md)
- [RAG Application Guide](./rag-app-complete.md)
- [Production Deployment](./production-deployment.md)

## Troubleshooting

### Issue: Agent Hallucinations
- Provide clear, specific role descriptions
- Include concrete examples in prompts
- Implement validation tasks

### Issue: Slow Execution
- Use parallel process instead of sequential
- Reduce number of agents
- Optimize tool implementations
- Consider caching for repeated queries

### Issue: Token Limits
- Break large tasks into smaller sub-tasks
- Implement summarization nodes
- Use appropriate model sizes
- Monitor token usage in logging

## Next Steps

1. Start with simple CrewAI workflow
2. Add specialized agents for your domain
3. Implement monitoring and logging
4. Deploy using containerization
5. Scale with load balancing
6. Integrate with RAG systems (see [RAG Guide](./rag-app-complete.md))
