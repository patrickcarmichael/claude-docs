---
title: "Crewai: Create LLM with fallback configuration"
description: "Create LLM with fallback configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create LLM with fallback configuration

portkey_llm = LLM(
    model="gpt-4o",
    max_tokens=1000,
    base_url=PORTKEY_GATEWAY_URL,
    api_key="dummy",
    extra_headers=createHeaders(
        api_key="YOUR_PORTKEY_API_KEY",
        config={
            "strategy": {
                "mode": "fallback"
            },
            "targets": [
                {
                    "provider": "openai",
                    "api_key": "YOUR_OPENAI_API_KEY",
                    "override_params": {"model": "gpt-4o"}
                },
                {
                    "provider": "anthropic",
                    "api_key": "YOUR_ANTHROPIC_API_KEY",
                    "override_params": {"model": "claude-3-opus-20240229"}
                }
            ]
        }
    )
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Production Features](./2261-production-features.md)

**Next:** [Use this LLM configuration with your agents →](./2263-use-this-llm-configuration-with-your-agents.md)
