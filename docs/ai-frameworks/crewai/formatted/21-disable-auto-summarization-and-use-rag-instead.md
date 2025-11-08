---
title: "Crewai: Disable auto-summarization and use RAG instead"
description: "Disable auto-summarization and use RAG instead section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Disable auto-summarization and use RAG instead

agent = Agent(
    role="Detailed Analyst",
    goal="Maintain complete information accuracy",
    backstory="Expert requiring full context",
    respect_context_window=False,  # No summarization
    tools=[RagTool()],  # Use RAG for large data
    verbose=True
)
```

<Note>
  The context window management feature works automatically in the background. You don't need to call any special functions - just set `respect_context_window` to your preferred behavior and CrewAI handles the rest!
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Alternative: Break tasks into smaller pieces](./20-alternative-break-tasks-into-smaller-pieces.md)

**Next:** [Direct Agent Interaction with `kickoff()` →](./22-direct-agent-interaction-with-kickoff.md)
