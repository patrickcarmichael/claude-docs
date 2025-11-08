---
title: "Crewai: Create LLM with guardrails"
description: "Create LLM with guardrails section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create LLM with guardrails

portkey_llm = LLM(
    model="gpt-4o",
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_OPENAI_VIRTUAL_KEY",
        config={
            "input_guardrails": ["guardrails-id-xxx", "guardrails-id-yyy"],
            "output_guardrails": ["guardrails-id-zzz"]
        }
    )
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use this LLM configuration with your agents](./2263-use-this-llm-configuration-with-your-agents.md)

**Next:** [Create agent with guardrailed LLM →](./2265-create-agent-with-guardrailed-llm.md)
