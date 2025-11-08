---
title: "Crewai: How Flows Work"
description: "How Flows Work section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## How Flows Work


<Note>
  While Crews excel at autonomous collaboration, Flows provide structured automations, offering granular control over workflow execution. Flows ensure tasks are executed reliably, securely, and efficiently, handling conditional logic, loops, and dynamic state management with precision. Flows integrate seamlessly with Crews, enabling you to balance high autonomy with exacting control.
</Note>

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a" alt="CrewAI Framework Overview" data-og-width="669" width="669" data-og-height="464" height="464" data-path="images/flows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4a6177acae3789dd8e4467b791c8966e 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a83fa78165e93bc1d988a30ebc33889a 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=04fbb8e23728b87efa78a0a776e2d194 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ff06d73f5d4aa911154c66becf14d732 2500w" />
</Frame>

| Component        |            Description            | Key Features                                                                                                                                                         |
| :--------------- | :-------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**         | Structured workflow orchestration | • Manages execution paths<br />• Handles state transitions<br />• Controls task sequencing<br />• Ensures reliable execution                                         |
| **Events**       |   Triggers for workflow actions   | • Initiate specific processes<br />• Enable dynamic responses<br />• Support conditional branching<br />• Allow for real-time adaptation                             |
| **States**       |    Workflow execution contexts    | • Maintain execution data<br />• Enable persistence<br />• Support resumability<br />• Ensure execution integrity                                                    |
| **Crew Support** |    Enhances workflow automation   | • Injects pockets of agency when needed<br />• Complements structured workflows<br />• Balances automation with intelligence<br />• Enables adaptive decision-making |

### Key Capabilities

<CardGroup cols={2}>
  <Card title="Event-Driven Orchestration" icon="bolt">
    Define precise execution paths responding dynamically to events
  </Card>

  <Card title="Fine-Grained Control" icon="sliders">
    Manage workflow states and conditional execution securely and efficiently
  </Card>

  <Card title="Native Crew Integration" icon="puzzle-piece">
    Effortlessly combine with Crews for enhanced autonomy and intelligence
  </Card>

  <Card title="Deterministic Execution" icon="route">
    Ensure predictable outcomes with explicit control flow and error handling
  </Card>
</CardGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Key Features](./520-key-features.md)

**Next:** [When to Use Crews vs. Flows →](./522-when-to-use-crews-vs-flows.md)
