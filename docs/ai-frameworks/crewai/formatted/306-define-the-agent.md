---
title: "Crewai: Define the agent"
description: "Define the agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define the agent

blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the Pydantic model for the blog](./305-define-the-pydantic-model-for-the-blog.md)

**Next:** [Define the task with output_json set to the Blog model →](./307-define-the-task-with-output_json-set-to-the-blog-m.md)
