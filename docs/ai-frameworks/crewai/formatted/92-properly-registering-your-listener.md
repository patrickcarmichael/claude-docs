---
title: "Crewai: Properly Registering Your Listener"
description: "Properly Registering Your Listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Properly Registering Your Listener


Simply defining your listener class isn't enough. You need to create an instance of it and ensure it's imported in your application. This ensures that:

1. The event handlers are registered with the event bus
2. The listener instance remains in memory (not garbage collected)
3. The listener is active when events are emitted

### Option 1: Import and Instantiate in Your Crew or Flow Implementation

The most important thing is to create an instance of your listener in the file where your Crew or Flow is defined and executed:

#### For Crew-based Applications

Create and import your listener at the top of your Crew implementation file:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Creating a Custom Event Listener](./91-creating-a-custom-event-listener.md)

**Next:** [In your crew.py file →](./93-in-your-crewpy-file.md)
