---
title: "Crewai: No crew-level knowledge required"
description: "No crew-level knowledge required section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# No crew-level knowledge required

crew = Crew(
    agents=[specialist_agent],
    tasks=[task]
)

result = crew.kickoff()  # Agent knowledge works independently
```

#### What Happens During `crew.kickoff()`

When you call `crew.kickoff()`, here's the exact sequence:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent with its own knowledge - NO crew knowledge needed](./140-agent-with-its-own-knowledge-no-crew-knowledge-nee.md)

**Next:** [During kickoff →](./142-during-kickoff.md)
