---
title: "Crewai: State Management with Crews"
description: "State Management with Crews section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced State Patterns](./499-advanced-state-patterns.md)

**Next:** [Best Practices for State Management →](./501-best-practices-for-state-management.md)
