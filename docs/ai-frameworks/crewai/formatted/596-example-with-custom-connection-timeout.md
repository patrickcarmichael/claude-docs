---
title: "Crewai: Example with custom connection timeout"
description: "Example with custom connection timeout section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example with custom connection timeout

with MCPServerAdapter(server_params, connect_timeout=60) as tools:
    # Connection will timeout after 60 seconds if not established
    pass
```

```python  theme={null}
from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters # For Stdio Server

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connection Configuration](./595-connection-configuration.md)

**Next:** [Example server_params (choose one based on your server type): →](./597-example-server_params-choose-one-based-on-your-ser.md)
