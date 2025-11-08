---
title: "Crewai: Initialize tools with session management"
description: "Initialize tools with session management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize tools with session management

initial_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id"
)

followup_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id"
)

final_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id",
    end_session=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Usage](./2357-advanced-usage.md)

**Next:** [Create agents for different stages →](./2359-create-agents-for-different-stages.md)
