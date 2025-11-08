---
title: "Crewai: Async function to kickoff the crew asynchronously"
description: "Async function to kickoff the crew asynchronously section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Async function to kickoff the crew asynchronously

async def async_crew_execution():
    result = await analysis_crew.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    print("Crew Result:", result)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a crew and add the task](./2063-create-a-crew-and-add-the-task.md)

**Next:** [Run the async function →](./2065-run-the-async-function.md)
