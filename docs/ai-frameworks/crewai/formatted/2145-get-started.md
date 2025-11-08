---
title: "Crewai: Get Started"
description: "Get Started section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Get Started


We'll walk through a simple example of using CrewAI and integrating it with Arize Phoenix via OpenTelemetry using OpenInference.

You can also access this guide on [Google Colab](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/tracing/crewai_tracing_tutorial.ipynb).

### Step 1: Install Dependencies

```bash  theme={null}
pip install openinference-instrumentation-crewai crewai crewai-tools arize-phoenix-otel
```

### Step 2: Set Up Environment Variables

Setup Phoenix Cloud API keys and configure OpenTelemetry to send traces to Phoenix. Phoenix Cloud is a hosted version of Arize Phoenix, but it is not required to use this integration.

You can get your free Serper API key [here](https://serper.dev/).

```python  theme={null}
import os
from getpass import getpass

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Arize Phoenix Integration](./2144-arize-phoenix-integration.md)

**Next:** [Get your Phoenix Cloud credentials →](./2146-get-your-phoenix-cloud-credentials.md)
