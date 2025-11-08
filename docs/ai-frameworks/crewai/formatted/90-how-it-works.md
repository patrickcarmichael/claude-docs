---
title: "Crewai: How It Works"
description: "How It Works section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## How It Works


CrewAI uses an event bus architecture to emit events throughout the execution lifecycle. The event system is built on the following components:

1. **CrewAIEventsBus**: A singleton event bus that manages event registration and emission
2. **BaseEvent**: Base class for all events in the system
3. **BaseEventListener**: Abstract base class for creating custom event listeners

When specific actions occur in CrewAI (like a Crew starting execution, an Agent completing a task, or a tool being used), the system emits corresponding events. You can register handlers for these events to execute custom code when they occur.

<Note type="info" title="Enterprise Enhancement: Prompt Tracing">
  CrewAI AMP provides a built-in Prompt Tracing feature that leverages the event system to track, store, and visualize all prompts, completions, and associated metadata. This provides powerful debugging capabilities and transparency into your agent operations.

    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c02d5b7306bf7adaeadd77a018f8fea" alt="Prompt Tracing Dashboard" data-og-width="2244" width="2244" data-og-height="1422" height="1422" data-path="images/enterprise/traces-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e66e7c56a8848b69266563ea8cddfc4e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f590b3901aaa5994042c79426d78bd6c 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0ecb9dcb307e8f130f53393bd3abc12d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fc6fcfc51c4e8f4ce16d237228043d6 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=253eaed4ec34a35798dad42e9a388859 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec818e09bc20b3f72b1bcf1970804d13 2500w" />

  With Prompt Tracing you can:

  * View the complete history of all prompts sent to your LLM
  * Track token usage and costs
  * Debug agent reasoning failures
  * Share prompt sequences with your team
  * Compare different prompt strategies
  * Export traces for compliance and auditing
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./89-overview.md)

**Next:** [Creating a Custom Event Listener →](./91-creating-a-custom-event-listener.md)
