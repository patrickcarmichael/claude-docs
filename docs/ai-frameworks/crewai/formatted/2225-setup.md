---
title: "Crewai: Setup"
description: "Setup section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup


Comet provides a hosted version of the Opik platform, or you can run the platform locally.

To use the hosted version, simply [create a free Comet account](https://www.comet.com/signup?utm_medium=github\&utm_source=crewai_docs) and grab you API Key.

To run the Opik platform locally, see our [installation guide](https://www.comet.com/docs/opik/self-host/overview/) for more information.

For this guide we will use CrewAI’s quickstart example.

<Steps>
  <Step title="Install required packages">
    ```shell  theme={null}
    pip install crewai crewai-tools opik --upgrade
    ```
  </Step>

  <Step title="Configure Opik">
    ```python  theme={null}
    import opik
    opik.configure(use_local=False)
    ```
  </Step>

  <Step title="Prepare environment">
    First, we set up our API keys for our LLM-provider as environment variables:

    ```python  theme={null}
    import os
    import getpass

    if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
    ```
  </Step>

  <Step title="Using CrewAI">
    The first step is to create our project. We will use an example from CrewAI’s documentation:

    ```python  theme={null}
    from crewai import Agent, Crew, Task, Process

    class YourCrewName:
        def agent_one(self) -> Agent:
            return Agent(
                role="Data Analyst",
                goal="Analyze data trends in the market",
                backstory="An experienced data analyst with a background in economics",
                verbose=True,
            )

        def agent_two(self) -> Agent:
            return Agent(
                role="Market Researcher",
                goal="Gather information on market dynamics",
                backstory="A diligent researcher with a keen eye for detail",
                verbose=True,
            )

        def task_one(self) -> Task:
            return Task(
                name="Collect Data Task",
                description="Collect recent market data and identify trends.",
                expected_output="A report summarizing key trends in the market.",
                agent=self.agent_one(),
            )

        def task_two(self) -> Task:
            return Task(
                name="Market Research Task",
                description="Research factors affecting market dynamics.",
                expected_output="An analysis of factors influencing the market.",
                agent=self.agent_two(),
            )

        def crew(self) -> Crew:
            return Crew(
                agents=[self.agent_one(), self.agent_two()],
                tasks=[self.task_one(), self.task_two()],
                process=Process.sequential,
                verbose=True,
            )

    ```

    Now we can import Opik’s tracker and run our crew:

    ```python  theme={null}
    from opik.integrations.crewai import track_crewai

    track_crewai(project_name="crewai-integration-demo")

    my_crew = YourCrewName().crew()
    result = my_crew.kickoff()

    print(result)
    ```

    After running your CrewAI application, visit the Opik app to view:

    * LLM traces, spans, and their metadata
    * Agent interactions and task execution flow
    * Performance metrics like latency and token usage
    * Evaluation metrics (built-in or custom)
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Opik Overview](./2224-opik-overview.md)

**Next:** [Resources →](./2226-resources.md)
