---
title: "Crewai: Connecting to OpenAI-Compatible LLMs"
description: "Connecting to OpenAI-Compatible LLMs section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Connecting to OpenAI-Compatible LLMs


You can connect to OpenAI-compatible LLMs using either environment variables or by setting specific attributes on the LLM class:

<Tabs>
  <Tab title="Using Environment Variables">
    <CodeGroup>
      ```python Generic theme={null}
      import os

      os.environ["OPENAI_API_KEY"] = "your-api-key"
      os.environ["OPENAI_API_BASE"] = "https://api.your-provider.com/v1"
      os.environ["OPENAI_MODEL_NAME"] = "your-model-name"
      ```

      ```python Google theme={null}
      import os

      # Example using Gemini's OpenAI-compatible API.
      os.environ["OPENAI_API_KEY"] = "your-gemini-key"  # Should start with AIza...
      os.environ["OPENAI_API_BASE"] = "https://generativelanguage.googleapis.com/v1beta/openai/"
      os.environ["OPENAI_MODEL_NAME"] = "openai/gemini-2.0-flash"  # Add your Gemini model here, under openai/
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Using LLM Class Attributes">
    <CodeGroup>
      ```python Generic theme={null}
      llm = LLM(
          model="custom-model-name",
          api_key="your-api-key",
          base_url="https://api.your-provider.com/v1"
      )
      agent = Agent(llm=llm, ...)
      ```

      ```python Google theme={null}
      # Example using Gemini's OpenAI-compatible API
      llm = LLM(
          model="openai/gemini-2.0-flash",
          base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
          api_key="your-gemini-key",  # Should start with AIza...
      )
      agent = Agent(llm=llm, ...)
      ```
    </CodeGroup>
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configuration Options](./2083-configuration-options.md)

**Next:** [Using Local Models with Ollama →](./2085-using-local-models-with-ollama.md)
