---
title: "Crewai: Step 2: Understanding the Project Structure"
description: "Step 2: Understanding the Project Structure section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Step 2: Understanding the Project Structure


The generated project has the following structure. Take a moment to familiarize yourself with it, as understanding this structure will help you create more complex flows in the future.

```
guide_creator_flow/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
├── main.py
├── crews/
│   └── poem_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── poem_crew.py
└── tools/
    └── custom_tool.py
```

This structure provides a clear separation between different components of your flow:

* The main flow logic in the `main.py` file
* Specialized crews in the `crews` directory
* Custom tools in the `tools` directory

We'll modify this structure to create our guide creator flow, which will orchestrate the process of generating comprehensive learning guides.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Step 1: Create a New CrewAI Flow Project](./464-step-1-create-a-new-crewai-flow-project.md)

**Next:** [Step 3: Add a Content Writer Crew →](./466-step-3-add-a-content-writer-crew.md)
