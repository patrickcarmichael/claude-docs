---
title: "Crewai: Agent with automatic context management (default)"
description: "Agent with automatic context management (default) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Agent with automatic context management (default)

smart_agent = Agent(
    role="Research Analyst",
    goal="Analyze large documents and datasets",
    backstory="Expert at processing extensive information",
    respect_context_window=True,  # 🔑 Default: auto-handle context limits
    verbose=True
)
```

**What happens when context limits are exceeded:**

* ⚠️ **Warning message**: `"Context length exceeded. Summarizing content to fit the model context window."`
* 🔄 **Automatic summarization**: CrewAI intelligently summarizes the conversation history
* ✅ **Continued execution**: Task execution continues seamlessly with the summarized context
* 📝 **Preserved information**: Key information is retained while reducing token count

### Strict Context Limits (`respect_context_window=False`)

When you need precise control and prefer execution to stop rather than lose any information:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Context Window Management](./11-context-window-management.md)

**Next:** [Agent with strict context limits →](./13-agent-with-strict-context-limits.md)
