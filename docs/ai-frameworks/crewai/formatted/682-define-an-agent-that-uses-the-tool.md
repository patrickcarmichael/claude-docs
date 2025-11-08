---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

@agent
def researcher(self) -> Agent:
    '''
    This agent uses the LlamaIndexTool to search for information.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        tools=[tool]
    )
```

### From LlamaHub Tools

```python Code theme={null}
from crewai_tools import LlamaIndexTool
from llama_index.tools.wolfram_alpha import WolframAlphaToolSpec

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Wrap it with LlamaIndexTool](./681-wrap-it-with-llamaindextool.md)

**Next:** [Initialize from LlamaHub Tools →](./683-initialize-from-llamahub-tools.md)
