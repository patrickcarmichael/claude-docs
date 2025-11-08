---
title: "Crewai: Set up LLMs with different providers"
description: "Set up LLMs with different providers section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Set up LLMs with different providers

openai_llm = LLM(
    model="gpt-4o",
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_OPENAI_VIRTUAL_KEY"
    )
)

anthropic_llm = LLM(
    model="claude-3-5-sonnet-latest",
    max_tokens=1000,
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_ANTHROPIC_VIRTUAL_KEY"
    )
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with tracked LLM](./2267-create-agent-with-tracked-llm.md)

**Next:** [Choose which LLM to use for each agent based on your needs →](./2269-choose-which-llm-to-use-for-each-agent-based-on-yo.md)
