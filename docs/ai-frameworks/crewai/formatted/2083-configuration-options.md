---
title: "Crewai: Configuration Options"
description: "Configuration Options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Options


When configuring an LLM for your agent, you have access to a wide range of parameters:

| Parameter              |        Type        | Description                                                      |
| :--------------------- | :----------------: | :--------------------------------------------------------------- |
| **model**              |        `str`       | The name of the model to use (e.g., "gpt-4", "claude-2")         |
| **temperature**        |       `float`      | Controls randomness in output (0.0 to 1.0)                       |
| **max\_tokens**        |        `int`       | Maximum number of tokens to generate                             |
| **top\_p**             |       `float`      | Controls diversity of output (0.0 to 1.0)                        |
| **frequency\_penalty** |       `float`      | Penalizes new tokens based on their frequency in the text so far |
| **presence\_penalty**  |       `float`      | Penalizes new tokens based on their presence in the text so far  |
| **stop**               | `str`, `List[str]` | Sequence(s) to stop generation                                   |
| **base\_url**          |        `str`       | The base URL for the API endpoint                                |
| **api\_key**           |        `str`       | Your API key for authentication                                  |

For a complete list of parameters and their descriptions, refer to the LLM class documentation.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Changing the LLM](./2082-changing-the-llm.md)

**Next:** [Connecting to OpenAI-Compatible LLMs →](./2084-connecting-to-openai-compatible-llms.md)
