---
title: "Crewai: Example of using kickoff_for_each"
description: "Example of using kickoff_for_each section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of using kickoff_for_each

inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
results = my_crew.kickoff_for_each(inputs=inputs_array)
for result in results:
    print(result)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Start the crew's task execution](./84-start-the-crews-task-execution.md)

**Next:** [Example of using kickoff_async →](./86-example-of-using-kickoff_async.md)
