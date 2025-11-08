---
title: "Crewai: Create agent with guardrailed LLM"
description: "Create agent with guardrailed LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with guardrailed LLM

researcher = Agent(
    role="Senior Research Scientist",
    goal="Discover groundbreaking insights about the assigned topic",
    backstory="You are an expert researcher with deep domain knowledge.",
    verbose=True,
    llm=portkey_llm
)
```

Portkey's guardrails can:

* Detect and redact PII in both inputs and outputs
* Filter harmful or inappropriate content
* Validate response formats against schemas
* Check for hallucinations against ground truth
* Apply custom business logic and rules

<Card title="Learn More About Guardrails" icon="shield-check" href="https://portkey.ai/docs/product/guardrails">
  Explore Portkey's guardrail features to enhance agent safety
</Card>

### 5. User Tracking with Metadata

Track individual users through your CrewAI agents using Portkey's metadata system.

**What is Metadata in Portkey?**

Metadata allows you to associate custom data with each request, enabling filtering, segmentation, and analytics. The special `_user` field is specifically designed for user tracking.

```python  theme={null}
from crewai import Agent, LLM
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create LLM with guardrails](./2264-create-llm-with-guardrails.md)

**Next:** [Configure LLM with user tracking →](./2266-configure-llm-with-user-tracking.md)
