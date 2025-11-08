---
title: "Crewai: Get Started"
description: "Get Started section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Get Started


We'll walk through a simple example of using CrewAI and integrating it with Braintrust via OpenTelemetry for comprehensive observability and evaluation.

### Step 1: Install Dependencies

```bash  theme={null}
uv add braintrust[otel] crewai crewai-tools opentelemetry-instrumentation-openai opentelemetry-instrumentation-crewai python-dotenv
```

### Step 2: Set Up Environment Variables

Setup Braintrust API keys and configure OpenTelemetry to send traces to Braintrust. You'll need a Braintrust API key and your OpenAI API key.

```python  theme={null}
import os
from getpass import getpass

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Braintrust Integration](./2155-braintrust-integration.md)

**Next:** [Get your Braintrust credentials →](./2157-get-your-braintrust-credentials.md)
