---
title: "Crewai: Create an instance of your listener"
description: "Create an instance of your listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an instance of your listener

my_listener = MyCustomListener()

class MyCustomCrew:
    # Your crew implementation...

    def crew(self):
        return Crew(
            agents=[...],
            tasks=[...],
            # ...
        )
```

#### For Flow-based Applications

Create and import your listener at the top of your Flow implementation file:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← In your crew.py file](./93-in-your-crewpy-file.md)

**Next:** [In your main.py or flow.py file →](./95-in-your-mainpy-or-flowpy-file.md)
