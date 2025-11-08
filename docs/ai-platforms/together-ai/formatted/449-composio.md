---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Composio

*Composio allows developers to integrate external tools and services into their AI applications.*

Install `composio-togetherai`
```bash
pip install together composio-togetherai
export TOGETHER_API_KEY=***
export COMPOSIO_API_KEY=***
```

Get Together AI models to use integrated tools
```python
from composio_togetherai import ComposioToolSet, App
from together import Together

client = Together()
toolset = ComposioToolSet()

request = toolset.initiate_connection(app=App.GITHUB)
print(f"Open this URL to authenticate: {request.redirectUrl}")

tools = toolset.get_tools(apps=[App.GITHUB])

response = client.chat.completions.create(
    tools=tools,
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": "Star the repo 'togethercomputer/together-cookbook'",
        }
    ],
)

res = toolset.handle_tool_calls(response)
print(res)
```

Learn more in our [Composio Guide](https://docs.together.ai/docs/composio) and explore our [Composio cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Composio/Agents_Composio.ipynb).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
