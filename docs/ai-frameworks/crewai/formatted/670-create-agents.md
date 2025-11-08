---
title: "Crewai: Create Agents"
description: "Create Agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create Agents

researcher = Agent(
    role='Research Analyst',
    goal='Gather current market data and trends',
    backstory="""You are an expert research analyst with years of experience in
    gathering market intelligence. You're known for your ability to find
    relevant and up-to-date market information and present it in a clear,
    actionable format.""",
    tools=[SearchTool()],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set up your SERPER_API_KEY key in an .env file, eg:](./669-set-up-your-serper_api_key-key-in-an-env-file-eg.md)

**Next:** [rest of the code ... →](./671-rest-of-the-code.md)
