---
title: "Crewai: Setup Instructions"
description: "Setup Instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup Instructions


<Steps>
  <Step title="Install LangDB">
    Install the LangDB client with CrewAI feature flag:

    ```bash  theme={null}
    pip install 'pylangdb[crewai]'
    ```
  </Step>

  <Step title="Set Environment Variables">
    Configure your LangDB credentials:

    ```bash  theme={null}
    export LANGDB_API_KEY="<your_langdb_api_key>"
    export LANGDB_PROJECT_ID="<your_langdb_project_id>"
    export LANGDB_API_BASE_URL='https://api.us-east-1.langdb.ai'
    ```
  </Step>

  <Step title="Initialize Tracing">
    Import and initialize LangDB before configuring your CrewAI code:

    ```python  theme={null}
    from pylangdb.crewai import init
    # Initialize LangDB
    init()
    ```
  </Step>

  <Step title="Configure CrewAI with LangDB">
    Set up your LLM with LangDB headers:

    ```python  theme={null}
    from crewai import Agent, Task, Crew, LLM
    import os

    # Configure LLM with LangDB headers
    llm = LLM(
        model="openai/gpt-4o", # Replace with the model you want to use
        api_key=os.getenv("LANGDB_API_KEY"),
        base_url=os.getenv("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.getenv("LANGDB_PROJECT_ID")}
    )
    ```
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Features](./2170-features.md)

**Next:** [Quick Start Example →](./2172-quick-start-example.md)
