---
title: "Crewai: Set environment variables"
description: "Set environment variables section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Set environment variables

os.environ["PHOENIX_CLIENT_HEADERS"] = f"api_key={PHOENIX_API_KEY}"
os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "https://app.phoenix.arize.com" # Phoenix Cloud, change this to your own endpoint if you are using a self-hosted instance
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY
```

### Step 3: Initialize OpenTelemetry with Phoenix

Initialize the OpenInference OpenTelemetry instrumentation SDK to start capturing traces and send them to Phoenix.

```python  theme={null}
from phoenix.otel import register

tracer_provider = register(
    project_name="crewai-tracing-demo",
    auto_instrument=True,
)
```

### Step 4: Create a CrewAI Application

We'll create a CrewAI application where two agents collaborate to research and write a blog post about AI advancements.

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from openinference.instrumentation.crewai import CrewAIInstrumentor
from phoenix.otel import register

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Get API keys for services](./2147-get-api-keys-for-services.md)

**Next:** [setup monitoring for your crew →](./2149-setup-monitoring-for-your-crew.md)
