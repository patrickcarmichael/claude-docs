---
title: "Crewai: Setup Instructions"
description: "Setup Instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup Instructions


<Steps>
  <Step title="Install required packages">
    ```shell  theme={null}
    pip install crewai weave
    ```
  </Step>

  <Step title="Set up W&B Account">
    Sign up for a [Weights & Biases account](https://wandb.ai) if you haven't already. You'll need this to view your traces and metrics.
  </Step>

  <Step title="Initialize Weave in Your Application">
    Add the following code to your application:

    ```python  theme={null}
    import weave

    # Initialize Weave with your project name
    weave.init(project_name="crewai_demo")
    ```

    After initialization, Weave will provide a URL where you can view your traces and metrics.
  </Step>

  <Step title="Create your Crews/Flows">
    ```python  theme={null}
    from crewai import Agent, Task, Crew, LLM, Process

    # Create an LLM with a temperature of 0 to ensure deterministic outputs
    llm = LLM(model="gpt-4o", temperature=0)

    # Create agents
    researcher = Agent(
        role='Research Analyst',
        goal='Find and analyze the best investment opportunities',
        backstory='Expert in financial analysis and market research',
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role='Report Writer',
        goal='Write clear and concise investment reports',
        backstory='Experienced in creating detailed financial reports',
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    # Create tasks
    research_task = Task(
        description='Deep research on the {topic}',
        expected_output='Comprehensive market data including key players, market size, and growth trends.',
        agent=researcher
    )

    writing_task = Task(
        description='Write a detailed report based on the research',
        expected_output='The report should be easy to read and understand. Use bullet points where applicable.',
        agent=writer
    )

    # Create a crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True,
        process=Process.sequential,
    )

    # Run the crew
    result = crew.kickoff(inputs={"topic": "AI in material science"})
    print(result)
    ```
  </Step>

  <Step title="View Traces in Weave">
    After running your CrewAI application, visit the Weave URL provided during initialization to view:

    * LLM calls and their metadata
    * Agent interactions and task execution flow
    * Performance metrics like latency and token usage
    * Any errors or issues that occurred during execution

    <Frame caption="Weave Tracing Dashboard">
      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f59e556fcc0ac8fcca8eaeef4c0551ae" alt="Weave tracing example with CrewAI" data-og-width="3456" width="3456" data-og-height="1986" height="1986" data-path="images/weave-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=42efb320cedff3209765027d4f47e187 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=85318181f2afd6237c71cecedfda8104 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6124c3113060320d39847c47faa02ac4 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e04300ff38ddf3624acc078bacf6712e 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c0ba473c3fa41c2939df4e28bc1098b5 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6d860d735bc5a42fb68085fc4ef01b2c 2500w" />
    </Frame>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Weave Overview](./2292-weave-overview.md)

**Next:** [Features →](./2294-features.md)
