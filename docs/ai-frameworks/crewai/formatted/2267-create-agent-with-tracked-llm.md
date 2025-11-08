---
title: "Crewai: Create agent with tracked LLM"
description: "Create agent with tracked LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with tracked LLM

researcher = Agent(
    role="Senior Research Scientist",
    goal="Discover groundbreaking insights about the assigned topic",
    backstory="You are an expert researcher with deep domain knowledge.",
    verbose=True,
    llm=portkey_llm
)
```

**Filter Analytics by User**

With metadata in place, you can filter analytics by user and analyze performance metrics on a per-user basis:

<Frame caption="Filter analytics by user">
  <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/Metadata%20Filters%20from%20CrewAI.png" />
</Frame>

This enables:

* Per-user cost tracking and budgeting
* Personalized user analytics
* Team or organization-level metrics
* Environment-specific monitoring (staging vs. production)

<Card title="Learn More About Metadata" icon="tags" href="https://portkey.ai/docs/product/observability/metadata">
  Explore how to use custom metadata to enhance your analytics
</Card>

### 6. Caching for Efficient Crews

Implement caching to make your CrewAI agents more efficient and cost-effective:

<Tabs>
  <Tab title="Simple Caching">
    ```python  theme={null}
    from crewai import Agent, LLM
    from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

    # Configure LLM with simple caching
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_OPENAI_VIRTUAL_KEY",
            config={
                "cache": {
                    "mode": "simple"
                }
            }
        )
    )

    # Create agent with cached LLM
    researcher = Agent(
        role="Senior Research Scientist",
        goal="Discover groundbreaking insights about the assigned topic",
        backstory="You are an expert researcher with deep domain knowledge.",
        verbose=True,
        llm=portkey_llm
    )
    ```

    Simple caching performs exact matches on input prompts, caching identical requests to avoid redundant model executions.
  </Tab>

  <Tab title="Semantic Caching">
    ```python  theme={null}
    from crewai import Agent, LLM
    from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

    # Configure LLM with semantic caching
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_OPENAI_VIRTUAL_KEY",
            config={
                "cache": {
                    "mode": "semantic"
                }
            }
        )
    )

    # Create agent with semantically cached LLM
    researcher = Agent(
        role="Senior Research Scientist",
        goal="Discover groundbreaking insights about the assigned topic",
        backstory="You are an expert researcher with deep domain knowledge.",
        verbose=True,
        llm=portkey_llm
    )
    ```

    Semantic caching considers the contextual similarity between input requests, caching responses for semantically similar inputs.
  </Tab>
</Tabs>

### 7. Model Interoperability

CrewAI supports multiple LLM providers, and Portkey extends this capability by providing access to over 200 LLMs through a unified interface. You can easily switch between different models without changing your core agent logic:

```python  theme={null}
from crewai import Agent, LLM
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configure LLM with user tracking](./2266-configure-llm-with-user-tracking.md)

**Next:** [Set up LLMs with different providers →](./2268-set-up-llms-with-different-providers.md)
