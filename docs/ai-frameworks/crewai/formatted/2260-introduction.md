---
title: "Crewai: Introduction"
description: "Introduction section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Introduction


Portkey enhances CrewAI with production-readiness features, turning your experimental agent crews into robust systems by providing:

* **Complete observability** of every agent step, tool use, and interaction
* **Built-in reliability** with fallbacks, retries, and load balancing
* **Cost tracking and optimization** to manage your AI spend
* **Access to 200+ LLMs** through a single integration
* **Guardrails** to keep agent behavior safe and compliant
* **Version-controlled prompts** for consistent agent performance

### Installation & Setup

<Steps>
  <Step title="Install the required packages">
    ```bash  theme={null}
    pip install -U crewai portkey-ai
    ```
  </Step>

  <Step title="Generate API Key" icon="lock">
    Create a Portkey API key with optional budget/rate limits from the [Portkey dashboard](https://app.portkey.ai/). You can also attach configurations for reliability, caching, and more to this key. More on this later.
  </Step>

  <Step title="Configure CrewAI with Portkey">
    The integration is simple - you just need to update the LLM configuration in your CrewAI setup:

    ```python  theme={null}
    from crewai import LLM
    from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

    # Create an LLM instance with Portkey integration
    gpt_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",  # We are using a Virtual key, so this is a placeholder
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_LLM_VIRTUAL_KEY",
            trace_id="unique-trace-id",               # Optional, for request tracing
        )
    )

    #Use them in your Crew Agents like this:

    	@agent
    	def lead_market_analyst(self) -> Agent:
    		return Agent(
    			config=self.agents_config['lead_market_analyst'],
    			verbose=True,
    			memory=False,
    			llm=gpt_llm
    		)

    ```

    <Info>
      **What are Virtual Keys?** Virtual keys in Portkey securely store your LLM provider API keys (OpenAI, Anthropic, etc.) in an encrypted vault. They allow for easier key rotation and budget management. [Learn more about virtual keys here](https://portkey.ai/docs/product/ai-gateway/virtual-keys).
    </Info>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Portkey Integration](./2259-portkey-integration.md)

**Next:** [Production Features →](./2261-production-features.md)
