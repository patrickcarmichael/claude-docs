---
title: "Crewai: Set environment variables"
description: "Set environment variables section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Set environment variables

os.environ["BRAINTRUST_API_KEY"] = BRAINTRUST_API_KEY
os.environ["BRAINTRUST_PARENT"] = "project_name:crewai-demo"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```

### Step 3: Initialize OpenTelemetry with Braintrust

Initialize the Braintrust OpenTelemetry instrumentation to start capturing traces and send them to Braintrust.

```python  theme={null}
import os
from typing import Any, Dict

from braintrust.otel import BraintrustSpanProcessor
from crewai import Agent, Crew, Task
from crewai.llm import LLM
from opentelemetry import trace
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.sdk.trace import TracerProvider

def setup_tracing() -> None:
    """Setup OpenTelemetry tracing with Braintrust."""
    current_provider = trace.get_tracer_provider()
    if isinstance(current_provider, TracerProvider):
        provider = current_provider
    else:
        provider = TracerProvider()
        trace.set_tracer_provider(provider)

    provider.add_span_processor(BraintrustSpanProcessor())
    CrewAIInstrumentor().instrument(tracer_provider=provider)
    OpenAIInstrumentor().instrument(tracer_provider=provider)

setup_tracing()
```

### Step 4: Create a CrewAI Application

We'll create a CrewAI application where two agents collaborate to research and write a blog post about AI advancements, with comprehensive tracing enabled.

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool

def create_crew() -> Crew:
    """Create a crew with multiple agents for comprehensive tracing."""
    llm = LLM(model="gpt-4o-mini")
    search_tool = SerperDevTool()

    # Define agents with specific roles
    researcher = Agent(
        role="Senior Research Analyst",
        goal="Uncover cutting-edge developments in AI and data science",
        backstory="""You work at a leading tech think tank.
        Your expertise lies in identifying emerging trends.
        You have a knack for dissecting complex data and presenting actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[search_tool],
    )

    writer = Agent(
        role="Tech Content Strategist",
        goal="Craft compelling content on tech advancements",
        backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
        You transform complex concepts into compelling narratives.""",
        verbose=True,
        allow_delegation=True,
        llm=llm,
    )

    # Create tasks for your agents
    research_task = Task(
        description="""Conduct a comprehensive analysis of the latest advancements in {topic}.
        Identify key trends, breakthrough technologies, and potential industry impacts.""",
        expected_output="Full analysis report in bullet points",
        agent=researcher,
    )

    writing_task = Task(
        description="""Using the insights provided, develop an engaging blog
        post that highlights the most significant {topic} advancements.
        Your post should be informative yet accessible, catering to a tech-savvy audience.
        Make it sound cool, avoid complex words so it doesn't sound like AI.""",
        expected_output="Full blog post of at least 4 paragraphs",
        agent=writer,
        context=[research_task],
    )

    # Instantiate your crew with a sequential process
    crew = Crew(
        agents=[researcher, writer], 
        tasks=[research_task, writing_task], 
        verbose=True, 
        process=Process.sequential
    )

    return crew

def run_crew():
    """Run the crew and return results."""
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": "AI developments"})
    return result

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Get API keys for services](./2158-get-api-keys-for-services.md)

**Next:** [Run your crew →](./2160-run-your-crew.md)
