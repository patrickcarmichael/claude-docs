---
title: "Crewai: Step 4: Configure the Content Writer Crew"
description: "Step 4: Configure the Content Writer Crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Step 4: Configure the Content Writer Crew


Now, let's modify the generated files for the content writer crew. We'll set up two specialized agents - a writer and a reviewer - that will collaborate to create high-quality content for our guide.

1. First, update the agents configuration file to define our content creation team:

   Remember to set `llm` to the provider you are using.

```yaml  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Step 3: Add a Content Writer Crew](./466-step-3-add-a-content-writer-crew.md)

**Next:** [src/guide_creator_flow/crews/content_crew/config/agents.yaml →](./468-srcguide_creator_flowcrewscontent_crewconfigagents.md)
