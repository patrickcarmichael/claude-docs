---
title: "Crewai: Create an instance of your listener"
description: "Create an instance of your listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an instance of your listener

my_listener = MyCustomListener()

class MyCustomFlow(Flow):
    # Your flow implementation...

    @start()
    def first_step(self):
        # ...
```

This ensures that your listener is loaded and active when your Crew or Flow is executed.

### Option 2: Create a Package for Your Listeners

For a more structured approach, especially if you have multiple listeners:

1. Create a package for your listeners:

```
my_project/
  ├── listeners/
  │   ├── __init__.py
  │   ├── my_custom_listener.py
  │   └── another_listener.py
```

2. In `my_custom_listener.py`, define your listener class and create an instance:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← In your main.py or flow.py file](./95-in-your-mainpy-or-flowpy-file.md)

**Next:** [my_custom_listener.py →](./97-my_custom_listenerpy.md)
