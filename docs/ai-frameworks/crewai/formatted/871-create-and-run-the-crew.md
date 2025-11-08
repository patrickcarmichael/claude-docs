---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(agents=[data_analyst_agent], 
            tasks=[query_task])
result = crew.kickoff()
```

You can also customize the tool with additional parameters:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to query sales data](./870-example-task-to-query-sales-data.md)

**Next:** [Initialize the tool with custom parameters →](./872-initialize-the-tool-with-custom-parameters.md)
