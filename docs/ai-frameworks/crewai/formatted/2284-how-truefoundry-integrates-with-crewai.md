---
title: "Crewai: How TrueFoundry Integrates with CrewAI"
description: "How TrueFoundry Integrates with CrewAI section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## How TrueFoundry Integrates with CrewAI


### Installation & Setup

<Steps>
  <Step title="Install CrewAI">
    ```bash  theme={null}
    pip install crewai
    ```
  </Step>

  <Step title="Get TrueFoundry Access Token">
    1. Sign up for a [TrueFoundry account](https://www.truefoundry.com/register)
    2. Follow the steps here in [Quick start](https://docs.truefoundry.com/gateway/quick-start)
  </Step>

  <Step title="Configure CrewAI with TrueFoundry">
        <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=746c0bd23a77535f35b0b2bcf3320bf5" alt="TrueFoundry Code Configuration" data-og-width="2940" width="2940" data-og-height="1664" height="1664" data-path="images/new-code-snippet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1d7f4e8883760766aa1ae1274fba2ffe 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4604432c1e1121d24c3fa6ad93bc0bd9 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=8dd95282de37aa70090ac61a00b6e1bb 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=920a67bee38e979c770d775195b60864 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4173b6e99ed12b00b54bf3f222589863 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=176dd84222c8c1a6f40af3e0adb88e37 2500w" />

    ```python  theme={null}
    from crewai import LLM

    # Create an LLM instance with TrueFoundry AI Gateway
    truefoundry_llm = LLM(
        model="openai-main/gpt-4o",  # Similarly, you can call any model from any provider
        base_url="your_truefoundry_gateway_base_url",
        api_key="your_truefoundry_api_key"
    )

    # Use in your CrewAI agents
    from crewai import Agent

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=truefoundry_llm,
            verbose=True
        )
    ```
  </Step>
</Steps>

### Complete CrewAI Example

```python  theme={null}
from crewai import Agent, Task, Crew, LLM

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← TrueFoundry Integration](./2283-truefoundry-integration.md)

**Next:** [Configure LLM with TrueFoundry →](./2285-configure-llm-with-truefoundry.md)
