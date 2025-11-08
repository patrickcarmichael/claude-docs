---
title: "Crewai: Efficient model for data processing"
description: "Efficient model for data processing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Efficient model for data processing

processing_llm = LLM(model="gpt-4o-mini", temperature=0)

research_manager = Agent(
    role="Research Strategy Manager",
    goal="Develop comprehensive research strategies and coordinate team efforts",
    backstory="Expert research strategist with deep analytical capabilities",
    llm=manager_llm,  # High-capability model for complex reasoning
    verbose=True
)

content_writer = Agent(
    role="Research Content Writer",
    goal="Transform research findings into compelling, well-structured reports",
    backstory="Skilled writer who excels at making complex topics accessible",
    llm=content_llm,  # Creative model for engaging content
    verbose=True
)

data_processor = Agent(
    role="Data Analysis Specialist",
    goal="Extract and organize key data points from research sources",
    backstory="Detail-oriented analyst focused on accuracy and efficiency",
    llm=processing_llm,  # Fast, cost-effective model for routine tasks
    verbose=True
)

crew = Crew(
    agents=[research_manager, content_writer, data_processor],
    tasks=[...],  # Your specific tasks
    manager_llm=manager_llm,  # Manager uses the reasoning model
    verbose=True
)
```

The key to successful multi-model implementation is understanding how different agents interact and ensuring that model capabilities align with agent responsibilities. This requires careful planning but can result in significant improvements in both output quality and operational efficiency.

### b. Component-Specific Selection

<Tabs>
  <Tab title="Manager LLM">
    The manager LLM plays a crucial role in hierarchical CrewAI processes, serving as the coordination point for multiple agents and tasks. This model needs to excel at delegation, task prioritization, and maintaining context across multiple concurrent operations.

    Effective manager LLMs require strong reasoning capabilities to make good delegation decisions, consistent performance to ensure predictable coordination, and excellent context management to track the state of multiple agents simultaneously. The model needs to understand the capabilities and limitations of different agents while optimizing task allocation for efficiency and quality.

    Cost considerations are particularly important for manager LLMs since they're involved in every operation. The model needs to provide sufficient capability for effective coordination while remaining cost-effective for frequent use. This often means finding models that offer good reasoning capabilities without the premium pricing of the most sophisticated options.
  </Tab>

  <Tab title="Function Calling LLM">
    Function calling LLMs handle tool usage across all agents, making them critical for crews that rely heavily on external tools and APIs. These models need to excel at understanding tool capabilities, extracting parameters accurately, and handling tool responses effectively.

    The most important characteristics for function calling LLMs are precision and reliability rather than creativity or sophisticated reasoning. The model needs to consistently extract the correct parameters from natural language requests and handle tool responses appropriately. Speed is also important since tool usage often involves multiple round trips that can impact overall performance.

    Many teams find that specialized function calling models or general purpose models with strong tool support work better than creative or reasoning-focused models for this role. The key is ensuring that the model can reliably bridge the gap between natural language instructions and structured tool calls.
  </Tab>

  <Tab title="Agent-Specific Overrides">
    Individual agents can override crew-level LLM settings when their specific needs differ significantly from the general crew requirements. This capability allows for fine-tuned optimization while maintaining operational simplicity for most agents.

    Consider agent-specific overrides when an agent's role requires capabilities that differ substantially from other crew members. For example, a creative writing agent might benefit from a model optimized for content generation, while a data analysis agent might perform better with a reasoning-focused model.

    The challenge with agent-specific overrides is balancing optimization with operational complexity. Each additional model adds complexity to deployment, monitoring, and cost management. Teams should focus overrides on agents where the performance improvement justifies the additional complexity.
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Creative model for content generation](./2094-creative-model-for-content-generation.md)

**Next:** [Task Definition Framework →](./2096-task-definition-framework.md)
