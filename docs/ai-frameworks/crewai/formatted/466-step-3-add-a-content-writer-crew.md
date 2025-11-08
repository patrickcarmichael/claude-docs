---
title: "Crewai: Step 3: Add a Content Writer Crew"
description: "Step 3: Add a Content Writer Crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Step 3: Add a Content Writer Crew


Our flow will need a specialized crew to handle the content creation process. Let's use the CrewAI CLI to add a content writer crew:

```bash  theme={null}
crewai flow add-crew content-crew
```

This command automatically creates the necessary directories and template files for your crew. The content writer crew will be responsible for writing and reviewing sections of our guide, working within the overall flow orchestrated by our main application.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Step 2: Understanding the Project Structure](./465-step-2-understanding-the-project-structure.md)

**Next:** [Step 4: Configure the Content Writer Crew →](./467-step-4-configure-the-content-writer-crew.md)
