---
title: "Crewai: Frequently Asked Questions"
description: "Frequently Asked Questions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Frequently Asked Questions


<AccordionGroup>
  <Accordion title="How does Portkey enhance CrewAI?">
    Portkey adds production-readiness to CrewAI through comprehensive observability (traces, logs, metrics), reliability features (fallbacks, retries, caching), and access to 200+ LLMs through a unified interface. This makes it easier to debug, optimize, and scale your agent applications.
  </Accordion>

  <Accordion title="Can I use Portkey with existing CrewAI applications?">
    Yes! Portkey integrates seamlessly with existing CrewAI applications. You just need to update your LLM configuration code with the Portkey-enabled version. The rest of your agent and crew code remains unchanged.
  </Accordion>

  <Accordion title="Does Portkey work with all CrewAI features?">
    Portkey supports all CrewAI features, including agents, tools, human-in-the-loop workflows, and all task process types (sequential, hierarchical, etc.). It adds observability and reliability without limiting any of the framework's functionality.
  </Accordion>

  <Accordion title="Can I track usage across multiple agents in a crew?">
    Yes, Portkey allows you to use a consistent `trace_id` across multiple agents in a crew to track the entire workflow. This is especially useful for complex crews where you want to understand the full execution path across multiple agents.
  </Accordion>

  <Accordion title="How do I filter logs and traces for specific crew runs?">
    Portkey allows you to add custom metadata to your LLM configuration, which you can then use for filtering. Add fields like `crew_name`, `crew_type`, or `session_id` to easily find and analyze specific crew executions.
  </Accordion>

  <Accordion title="Can I use my own API keys with Portkey?">
    Yes! Portkey uses your own API keys for the various LLM providers. It securely stores them as virtual keys, allowing you to easily manage and rotate keys without changing your code.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set Up Enterprise Governance for CrewAI](./2270-set-up-enterprise-governance-for-crewai.md)

**Next:** [Resources →](./2272-resources.md)
