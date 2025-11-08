---
title: "Crewai: Store API keys in environment variables"
description: "Store API keys in environment variables section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Store API keys in environment variables

exa_key = os.getenv("EXA_API_KEY")
exa_profile = os.getenv("EXA_PROFILE")

agent = Agent(
    role="Secure Agent",
    goal="Use MCP tools securely",
    backstory="Security-conscious agent",
    mcps=[f"https://mcp.exa.ai/mcp?api_key={exa_key}&profile={exa_profile}"]
)
```

### 3. Plan for Server Failures

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Less efficient - gets all tools from server](./558-less-efficient-gets-all-tools-from-server.md)

**Next:** [Always include backup options →](./560-always-include-backup-options.md)
