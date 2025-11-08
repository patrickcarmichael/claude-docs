---
title: "Crewai: Get Started"
description: "Get Started section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Get Started


We'll walk through a simple example of using CrewAI and integrating it with Langfuse via OpenTelemetry using OpenLit.

### Step 1: Install Dependencies

```python  theme={null}
%pip install langfuse openlit crewai crewai_tools
```

### Step 2: Set Up Environment Variables

Set your Langfuse API keys and configure OpenTelemetry export settings to send traces to Langfuse. Please refer to the [Langfuse OpenTelemetry Docs](https://langfuse.com/docs/opentelemetry/get-started) for more information on the Langfuse OpenTelemetry endpoint `/api/public/otel` and authentication.

```python  theme={null}
import os

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Integrate Langfuse with CrewAI](./2185-integrate-langfuse-with-crewai.md)

**Next:** [Get keys for your project from the project settings page: https://cloud.langfuse.com →](./2187-get-keys-for-your-project-from-the-project-setting.md)
