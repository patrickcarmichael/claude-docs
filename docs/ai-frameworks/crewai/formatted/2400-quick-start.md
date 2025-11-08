---
title: "Crewai: Quick Start"
description: "Quick Start section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Quick Start


<Steps>
  <Step title="Get Your API Credentials">
    Navigate to your crew's detail page in the CrewAI AMP dashboard and copy your Bearer Token from the Status tab.
  </Step>

  <Step title="Discover Required Inputs">
    Use the `GET /inputs` endpoint to see what parameters your crew expects.
  </Step>

  <Step title="Start a Crew Execution">
    Call `POST /kickoff` with your inputs to start the crew execution and receive a `kickoff_id`.
  </Step>

  <Step title="Monitor Progress">
    Use `GET /status/{kickoff_id}` to check execution status and retrieve results.
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← CrewAI AMP API](./2399-crewai-amp-api.md)

**Next:** [Authentication →](./2401-authentication.md)
