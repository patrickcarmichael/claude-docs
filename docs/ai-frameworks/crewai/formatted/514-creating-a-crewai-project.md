---
title: "Crewai: Creating a CrewAI Project"
description: "Creating a CrewAI Project section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Creating a CrewAI Project


We recommend using the `YAML` template scaffolding for a structured approach to defining agents and tasks. Here's how to get started:

<Steps>
  <Step title="Generate Project Scaffolding">
    * Run the `crewai` CLI command:
      ```shell  theme={null}
      crewai create crew <your_project_name>
      ```

    * This creates a new project with the following structure:
      ```
      my_project/
      ├── .gitignore
      ├── knowledge/
      ├── pyproject.toml
      ├── README.md
      ├── .env
      └── src/
          └── my_project/
              ├── __init__.py
              ├── main.py
              ├── crew.py
              ├── tools/
              │   ├── custom_tool.py
              │   └── __init__.py
              └── config/
                  ├── agents.yaml
                  └── tasks.yaml
      ```
  </Step>

  <Step title="Customize Your Project">
    * Your project will contain these essential files:
      | File          | Purpose                                  |
      | ------------- | ---------------------------------------- |
      | `agents.yaml` | Define your AI agents and their roles    |
      | `tasks.yaml`  | Set up agent tasks and workflows         |
      | `.env`        | Store API keys and environment variables |
      | `main.py`     | Project entry point and execution flow   |
      | `crew.py`     | Crew orchestration and coordination      |
      | `tools/`      | Directory for custom agent tools         |
      | `knowledge/`  | Directory for knowledge base             |

    * Start by editing `agents.yaml` and `tasks.yaml` to define your crew's behavior.

    * Keep sensitive information like API keys in `.env`.
  </Step>

  <Step title="Run your Crew">
    * Before you run your crew, make sure to run:
      ```bash  theme={null}
      crewai install
      ```
    * If you need to install additional packages, use:
      ```shell  theme={null}
      uv add <package-name>
      ```
    * To run your crew, execute the following command in the root of your project:
      ```bash  theme={null}
      crewai run
      ```
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Text Tutorial](./513-text-tutorial.md)

**Next:** [Enterprise Installation Options →](./515-enterprise-installation-options.md)
