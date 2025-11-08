---
title: "Crewai: Quick Setup with CrewAI"
description: "Quick Setup with CrewAI section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Quick Setup with CrewAI


<Steps>
  <Step title="Sign Up & Get API Key">
    Visit [neatlogs.com](https://neatlogs.com/?utm_source=crewAI-docs), create a project, copy the API key.
  </Step>

  <Step title="Install SDK">
    ```bash  theme={null}
    pip install neatlogs
    ```

    (Latest version 0.8.0, Python 3.8+; MIT license)
  </Step>

  <Step title="Initialize Neatlogs">
    Before starting Crew agents, add:

    ```python  theme={null}
    import neatlogs
    neatlogs.init("YOUR_PROJECT_API_KEY")
    ```

    Agents run as usual. Neatlogs captures everything automatically.
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Core Features](./2214-core-features.md)

**Next:** [Under the Hood →](./2216-under-the-hood.md)
