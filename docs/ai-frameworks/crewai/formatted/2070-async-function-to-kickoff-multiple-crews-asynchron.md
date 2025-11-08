---
title: "Crewai: Async function to kickoff multiple crews asynchronously and wait for all to finish"
description: "Async function to kickoff multiple crews asynchronously and wait for all to finish section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Async function to kickoff multiple crews asynchronously and wait for all to finish

async def async_multiple_crews():
    # Create coroutines for concurrent execution
    result_1 = crew_1.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    result_2 = crew_2.kickoff_async(inputs={"ages": [20, 22, 24, 28, 30]})

    # Wait for both crews to finish
    results = await asyncio.gather(result_1, result_2)

    for i, result in enumerate(results, 1):
        print(f"Crew {i} Result:", result)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create two crews and add tasks](./2069-create-two-crews-and-add-tasks.md)

**Next:** [Run the async function →](./2071-run-the-async-function.md)
