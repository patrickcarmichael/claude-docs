---
title: "Crewai: Step 1: Create a New CrewAI Project"
description: "Step 1: Create a New CrewAI Project section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Step 1: Create a New CrewAI Project


First, let's create a new CrewAI project using the CLI. This command will set up a complete project structure with all the necessary files, allowing you to focus on defining your agents and their tasks rather than setting up boilerplate code.

```bash  theme={null}
crewai create crew research_crew
cd research_crew
```

This will generate a project with the basic structure needed for your crew. The CLI automatically creates:

* A project directory with the necessary files
* Configuration files for agents and tasks
* A basic crew implementation
* A main script to run the crew

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975" alt="CrewAI Framework Overview" data-og-width="634" width="634" data-og-height="473" height="473" data-path="images/crews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=279c5c26c77fc9acc8411677716fa5ee 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ef573e6215967af1bb2975a58d0d859 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1af6e6a337b70ca2ce238d8e40f49218 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c5da01705f1373446f8582ac582ff244 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=96464aab7bb5efe4213a7b80f58038aa 2500w" />
</Frame>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Unleashing the Power of Collaborative AI](./436-unleashing-the-power-of-collaborative-ai.md)

**Next:** [Step 2: Explore the Project Structure →](./438-step-2-explore-the-project-structure.md)
