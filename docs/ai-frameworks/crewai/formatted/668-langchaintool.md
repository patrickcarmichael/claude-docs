---
title: "Crewai: `LangChainTool`"
description: "`LangChainTool` section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## `LangChainTool`


<Info>
  CrewAI seamlessly integrates with LangChain's comprehensive [list of tools](https://python.langchain.com/docs/integrations/tools/), all of which can be used with CrewAI.
</Info>

```python Code theme={null}
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← LangChain Tool](./667-langchain-tool.md)

**Next:** [Set up your SERPER_API_KEY key in an .env file, eg: →](./669-set-up-your-serper_api_key-key-in-an-env-file-eg.md)
