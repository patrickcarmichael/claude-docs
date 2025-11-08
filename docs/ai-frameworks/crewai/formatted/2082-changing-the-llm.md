---
title: "Crewai: Changing the LLM"
description: "Changing the LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Changing the LLM


To use a different LLM with your CrewAI agents, you have several options:

<Tabs>
  <Tab title="Using a String Identifier">
    Pass the model name as a string when initializing the agent:

    <CodeGroup>
      ```python Code theme={null}
      from crewai import Agent

      # Using OpenAI's GPT-4
      openai_agent = Agent(
          role='OpenAI Expert',
          goal='Provide insights using GPT-4',
          backstory="An AI assistant powered by OpenAI's latest model.",
          llm='gpt-4'
      )

      # Using Anthropic's Claude
      claude_agent = Agent(
          role='Anthropic Expert',
          goal='Analyze data using Claude',
          backstory="An AI assistant leveraging Anthropic's language model.",
          llm='claude-2'
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Using the LLM Class">
    For more detailed configuration, use the LLM class:

    <CodeGroup>
      ```python Code theme={null}
      from crewai import Agent, LLM

      llm = LLM(
          model="gpt-4",
          temperature=0.7,
          base_url="https://api.openai.com/v1",
          api_key="your-api-key-here"
      )

      agent = Agent(
          role='Customized LLM Expert',
          goal='Provide tailored responses',
          backstory="An AI assistant with custom LLM settings.",
          llm=llm
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Supported Providers](./2081-supported-providers.md)

**Next:** [Configuration Options →](./2083-configuration-options.md)
