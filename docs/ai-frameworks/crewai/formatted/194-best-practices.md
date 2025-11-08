---
title: "Crewai: Best Practices"
description: "Best Practices section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Best Practices


<AccordionGroup>
  <Accordion title="Content Organization">
    * Keep chunk sizes appropriate for your content type
    * Consider content overlap for context preservation
    * Organize related information into separate knowledge sources
  </Accordion>

  <Accordion title="Performance Tips">
    * Adjust chunk sizes based on content complexity
    * Configure appropriate embedding models
    * Consider using local embedding providers for faster processing
  </Accordion>

  <Accordion title="One Time Knowledge">
    * With the typical file structure provided by CrewAI, knowledge sources are embedded every time the kickoff is triggered.
    * If the knowledge sources are large, this leads to inefficiency and increased latency, as the same data is embedded each time.
    * To resolve this, directly initialize the knowledge parameter instead of the knowledge\_sources parameter.
    * Link to the issue to get complete idea [Github Issue](https://github.com/crewAIInc/crewAI/issues/2755)
  </Accordion>

  <Accordion title="Knowledge Management">
    * Use agent-level knowledge for role-specific information
    * Use crew-level knowledge for shared information all agents need
    * Set embedders at agent level if you need different embedding strategies
    * Use consistent collection naming by keeping agent roles descriptive
    * Test knowledge initialization by checking agent.knowledge after kickoff
    * Monitor storage locations to understand where knowledge is stored
    * Reset knowledge appropriately using the correct command types
  </Accordion>

  <Accordion title="Production Best Practices">
    * Set `CREWAI_STORAGE_DIR` to a known location in production
    * Choose explicit embedding providers to match your LLM setup and avoid API key conflicts
    * Monitor knowledge storage size as it grows with document additions
    * Organize knowledge sources by domain or purpose using collection names
    * Include knowledge directories in your backup and deployment strategies
    * Set appropriate file permissions for knowledge files and storage directories
    * Use environment variables for API keys and sensitive configuration
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← crewai reset-memories --knowledge        # All knowledge](./193-crewai-reset-memories-knowledge-all-knowledge.md)

**Next:** [LLMs →](./195-llms.md)
