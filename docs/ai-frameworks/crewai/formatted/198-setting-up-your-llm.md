---
title: "Crewai: Setting up your LLM"
description: "Setting up your LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setting up your LLM


There are different places in CrewAI code where you can specify the model to use. Once you specify the model you are using, you will need to provide the configuration (like an API key) for each of the model providers you use. See the [provider configuration examples](#provider-configuration-examples) section for your provider.

<Tabs>
  <Tab title="1. Environment Variables">
    The simplest way to get started. Set the model in your environment directly, through an `.env` file or in your app code. If you used `crewai create` to bootstrap your project, it will be set already.

    ```bash .env theme={null}
    MODEL=model-id  # e.g. gpt-4o, gemini-2.0-flash, claude-3-sonnet-...

    # Be sure to set your API keys here too. See the Provider
    # section below.
    ```

    <Warning>
      Never commit API keys to version control. Use environment files (.env) or your system's secret management.
    </Warning>
  </Tab>

  <Tab title="2. YAML Configuration">
    Create a YAML file to define your agent configurations. This method is great for version control and team collaboration:

    ```yaml agents.yaml {6} theme={null}
    researcher:
        role: Research Specialist
        goal: Conduct comprehensive research and analysis
        backstory: A dedicated research professional with years of experience
        verbose: true
        llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
        # (see provider configuration examples below for more)
    ```

    <Info>
      The YAML configuration allows you to:

      * Version control your agent settings
      * Easily switch between different models
      * Share configurations across team members
      * Document model choices and their purposes
    </Info>
  </Tab>

  <Tab title="3. Direct Code">
    For maximum flexibility, configure LLMs directly in your Python code:

    ```python {4,8} theme={null}
    from crewai import LLM

    # Basic configuration
    llm = LLM(model="model-id-here")  # gpt-4o, gemini-2.0-flash, anthropic/claude...

    # Advanced configuration with detailed parameters
    llm = LLM(
        model="model-id-here",  # gpt-4o, gemini-2.0-flash, anthropic/claude...
        temperature=0.7,        # Higher for more creative outputs
        timeout=120,            # Seconds to wait for response
        max_tokens=4000,        # Maximum length of response
        top_p=0.9,              # Nucleus sampling parameter
        frequency_penalty=0.1 , # Reduce repetition
        presence_penalty=0.1,   # Encourage topic diversity
        response_format={"type": "json"},  # For structured outputs
        seed=42                 # For reproducible results
    )
    ```

    <Info>
      Parameter explanations:

      * `temperature`: Controls randomness (0.0-1.0)
      * `timeout`: Maximum wait time for response
      * `max_tokens`: Limits response length
      * `top_p`: Alternative to temperature for sampling
      * `frequency_penalty`: Reduces word repetition
      * `presence_penalty`: Encourages new topics
      * `response_format`: Specifies output structure
      * `seed`: Ensures consistent outputs
    </Info>
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← What are LLMs?](./197-what-are-llms.md)

**Next:** [Provider Configuration Examples →](./199-provider-configuration-examples.md)
