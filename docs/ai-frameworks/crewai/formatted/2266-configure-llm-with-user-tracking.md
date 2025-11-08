---
title: "Crewai: Configure LLM with user tracking"
description: "Configure LLM with user tracking section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Configure LLM with user tracking

portkey_llm = LLM(
    model="gpt-4o",
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        virtual_key="YOUR_OPENAI_VIRTUAL_KEY",
        metadata={
            "_user": "user_123",  # Special _user field for user analytics
            "user_tier": "premium",
            "user_company": "Acme Corp",
            "session_id": "abc-123"
        }
    )
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with guardrailed LLM](./2265-create-agent-with-guardrailed-llm.md)

**Next:** [Create agent with tracked LLM →](./2267-create-agent-with-tracked-llm.md)
