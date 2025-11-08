---
title: "Crewai: Always include backup options"
description: "Always include backup options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Always include backup options

mcps=[
    "https://primary-api.com/mcp",       # Primary choice
    "https://backup-api.com/mcp",        # Backup option
    "crewai-amp:reliable-service"        # AMP fallback
]
```

### 4. Use Descriptive Agent Roles

```python  theme={null}
agent = Agent(
    role="Weather-Enhanced Market Analyst",
    goal="Analyze markets considering weather impacts",
    backstory="Financial analyst with access to weather data for agricultural market insights",
    mcps=[
        "https://weather.service.com/mcp#get_forecast",
        "crewai-amp:financial-data#stock_analysis"
    ]
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Store API keys in environment variables](./559-store-api-keys-in-environment-variables.md)

**Next:** [Troubleshooting →](./561-troubleshooting.md)
