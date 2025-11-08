---
title: "Crewai: Use this LLM configuration with your agents"
description: "Use this LLM configuration with your agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Use this LLM configuration with your agents

```

This configuration will automatically try Claude if the GPT-4o request fails, ensuring your crew can continue operating.

<CardGroup cols="2">
  <Card title="Automatic Retries" icon="rotate" href="https://portkey.ai/docs/product/ai-gateway/automatic-retries">
    Handles temporary failures automatically. If an LLM call fails, Portkey will retry the same request for the specified number of times - perfect for rate limits or network blips.
  </Card>

  <Card title="Request Timeouts" icon="clock" href="https://portkey.ai/docs/product/ai-gateway/request-timeouts">
    Prevent your agents from hanging. Set timeouts to ensure you get responses (or can fail gracefully) within your required timeframes.
  </Card>

  <Card title="Conditional Routing" icon="route" href="https://portkey.ai/docs/product/ai-gateway/conditional-routing">
    Send different requests to different providers. Route complex reasoning to GPT-4, creative tasks to Claude, and quick responses to Gemini based on your needs.
  </Card>

  <Card title="Fallbacks" icon="shield" href="https://portkey.ai/docs/product/ai-gateway/fallbacks">
    Keep running even if your primary provider fails. Automatically switch to backup providers to maintain availability.
  </Card>

  <Card title="Load Balancing" icon="scale-balanced" href="https://portkey.ai/docs/product/ai-gateway/load-balancing">
    Spread requests across multiple API keys or providers. Great for high-volume crew operations and staying within rate limits.
  </Card>
</CardGroup>

### 3. Prompting in CrewAI

Portkey's Prompt Engineering Studio helps you create, manage, and optimize the prompts used in your CrewAI agents. Instead of hardcoding prompts or instructions, use Portkey's prompt rendering API to dynamically fetch and apply your versioned prompts.

<Frame caption="Manage prompts in Portkey's Prompt Library">
  ![Prompt Playground Interface](https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20Portkey%20Docs.webp)
</Frame>

<Tabs>
  <Tab title="Prompt Playground">
    Prompt Playground is a place to compare, test and deploy perfect prompts for your AI application. It's where you experiment with different models, test variables, compare outputs, and refine your prompt engineering strategy before deploying to production. It allows you to:

    1. Iteratively develop prompts before using them in your agents
    2. Test prompts with different variables and models
    3. Compare outputs between different prompt versions
    4. Collaborate with team members on prompt development

    This visual environment makes it easier to craft effective prompts for each step in your CrewAI agents' workflow.
  </Tab>

  <Tab title="Using Prompt Templates">
    The Prompt Render API retrieves your prompt templates with all parameters configured:

    ```python  theme={null}
    from crewai import Agent, LLM
    from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL, Portkey

    # Initialize Portkey admin client
    portkey_admin = Portkey(api_key="YOUR_PORTKEY_API_KEY")

    # Retrieve prompt using the render API
    prompt_data = portkey_client.prompts.render(
        prompt_id="YOUR_PROMPT_ID",
        variables={
            "agent_role": "Senior Research Scientist",
        }
    )

    backstory_agent_prompt=prompt_data.data.messages[0]["content"]

    # Set up LLM with Portkey integration
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_OPENAI_VIRTUAL_KEY"
        )
    )

    # Create agent using the rendered prompt
    researcher = Agent(
        role="Senior Research Scientist",
        goal="Discover groundbreaking insights about the assigned topic",
        backstory=backstory_agent,  # Use the rendered prompt
        verbose=True,
        llm=portkey_llm
    )
    ```
  </Tab>

  <Tab title="Prompt Versioning">
    You can:

    * Create multiple versions of the same prompt
    * Compare performance between versions
    * Roll back to previous versions if needed
    * Specify which version to use in your code:

    ```python  theme={null}
    # Use a specific prompt version
    prompt_data = portkey_admin.prompts.render(
        prompt_id="YOUR_PROMPT_ID@version_number",
        variables={
            "agent_role": "Senior Research Scientist",
            "agent_goal": "Discover groundbreaking insights"
        }
    )
    ```
  </Tab>

  <Tab title="Mustache Templating for variables">
    Portkey prompts use Mustache-style templating for easy variable substitution:

    ```
    You are a {{agent_role}} with expertise in {{domain}}.

    Your mission is to {{agent_goal}} by leveraging your knowledge
    and experience in the field.

    Always maintain a {{tone}} tone and focus on providing {{focus_area}}.
    ```

    When rendering, simply pass the variables:

    ```python  theme={null}
    prompt_data = portkey_admin.prompts.render(
        prompt_id="YOUR_PROMPT_ID",
        variables={
            "agent_role": "Senior Research Scientist",
            "domain": "artificial intelligence",
            "agent_goal": "discover groundbreaking insights",
            "tone": "professional",
            "focus_area": "practical applications"
        }
    )
    ```
  </Tab>
</Tabs>

<Card title="Prompt Engineering Studio" icon="wand-magic-sparkles" href="https://portkey.ai/docs/product/prompt-library">
  Learn more about Portkey's prompt management features
</Card>

### 4. Guardrails for Safe Crews

Guardrails ensure your CrewAI agents operate safely and respond appropriately in all situations.

**Why Use Guardrails?**

CrewAI agents can experience various failure modes:

* Generating harmful or inappropriate content
* Leaking sensitive information like PII
* Hallucinating incorrect information
* Generating outputs in incorrect formats

Portkey's guardrails add protections for both inputs and outputs.

**Implementing Guardrails**

```python  theme={null}
from crewai import Agent, LLM
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create LLM with fallback configuration](./2262-create-llm-with-fallback-configuration.md)

**Next:** [Create LLM with guardrails →](./2264-create-llm-with-guardrails.md)
