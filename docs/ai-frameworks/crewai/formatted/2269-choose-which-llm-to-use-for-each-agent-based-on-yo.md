---
title: "Crewai: Choose which LLM to use for each agent based on your needs"
description: "Choose which LLM to use for each agent based on your needs section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Choose which LLM to use for each agent based on your needs

researcher = Agent(
    role="Senior Research Scientist",
    goal="Discover groundbreaking insights about the assigned topic",
    backstory="You are an expert researcher with deep domain knowledge.",
    verbose=True,
    llm=openai_llm  # Use anthropic_llm for Anthropic
)
```

Portkey provides access to LLMs from providers including:

* OpenAI (GPT-4o, GPT-4 Turbo, etc.)
* Anthropic (Claude 3.5 Sonnet, Claude 3 Opus, etc.)
* Mistral AI (Mistral Large, Mistral Medium, etc.)
* Google Vertex AI (Gemini 1.5 Pro, etc.)
* Cohere (Command, Command-R, etc.)
* AWS Bedrock (Claude, Titan, etc.)
* Local/Private Models

<Card title="Supported Providers" icon="server" href="https://portkey.ai/docs/integrations/llms">
  See the full list of LLM providers supported by Portkey
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set up LLMs with different providers](./2268-set-up-llms-with-different-providers.md)

**Next:** [Set Up Enterprise Governance for CrewAI →](./2270-set-up-enterprise-governance-for-crewai.md)
