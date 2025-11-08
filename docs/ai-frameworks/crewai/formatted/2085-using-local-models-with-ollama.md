---
title: "Crewai: Using Local Models with Ollama"
description: "Using Local Models with Ollama section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Using Local Models with Ollama


For local models like those provided by Ollama:

<Steps>
  <Step title="Download and install Ollama">
    [Click here to download and install Ollama](https://ollama.com/download)
  </Step>

  <Step title="Pull the desired model">
    For example, run `ollama pull llama3.2` to download the model.
  </Step>

  <Step title="Configure your agent">
    <CodeGroup>
      ```python Code theme={null}
          agent = Agent(
              role='Local AI Expert',
              goal='Process information using a local model',
              backstory="An AI assistant running on local hardware.",
              llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
          )
      ```
    </CodeGroup>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connecting to OpenAI-Compatible LLMs](./2084-connecting-to-openai-compatible-llms.md)

**Next:** [Changing the Base API URL →](./2086-changing-the-base-api-url.md)
