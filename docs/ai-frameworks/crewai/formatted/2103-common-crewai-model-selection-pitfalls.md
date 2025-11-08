---
title: "Crewai: Common CrewAI Model Selection Pitfalls"
description: "Common CrewAI Model Selection Pitfalls section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Common CrewAI Model Selection Pitfalls


<AccordionGroup>
  <Accordion title="The 'One Model Fits All' Trap" icon="triangle-exclamation">
    **The Problem**: Using the same LLM for all agents in a crew, regardless of their specific roles and responsibilities. This is often the default approach but rarely optimal.

    **Real Example**: Using GPT-4o for both a strategic planning manager and a data extraction agent. The manager needs reasoning capabilities worth the premium cost, but the data extractor could perform just as well with GPT-4o-mini at a fraction of the price.

    **CrewAI Solution**: Leverage agent-specific LLM configuration to match model capabilities with agent roles:

    ```python  theme={null}
    # Strategic agent gets premium model
    manager = Agent(role="Strategy Manager", llm=LLM(model="gpt-4o"))

    # Processing agent gets efficient model
    processor = Agent(role="Data Processor", llm=LLM(model="gpt-4o-mini"))
    ```
  </Accordion>

  <Accordion title="Ignoring Crew-Level vs Agent-Level LLM Hierarchy" icon="shuffle">
    **The Problem**: Not understanding how CrewAI's LLM hierarchy works - crew LLM, manager LLM, and agent LLM settings can conflict or be poorly coordinated.

    **Real Example**: Setting a crew to use Claude, but having agents configured with GPT models, creating inconsistent behavior and unnecessary model switching overhead.

    **CrewAI Solution**: Plan your LLM hierarchy strategically:

    ```python  theme={null}
    crew = Crew(
        agents=[agent1, agent2],
        tasks=[task1, task2],
        manager_llm=LLM(model="gpt-4o"),  # For crew coordination
        process=Process.hierarchical  # When using manager_llm
    )

    # Agents inherit crew LLM unless specifically overridden
    agent1 = Agent(llm=LLM(model="claude-3-5-sonnet"))  # Override for specific needs
    ```
  </Accordion>

  <Accordion title="Function Calling Model Mismatch" icon="screwdriver-wrench">
    **The Problem**: Choosing models based on general capabilities while ignoring function calling performance for tool-heavy CrewAI workflows.

    **Real Example**: Selecting a creative-focused model for an agent that primarily needs to call APIs, search tools, or process structured data. The agent struggles with tool parameter extraction and reliable function calls.

    **CrewAI Solution**: Prioritize function calling capabilities for tool-heavy agents:

    ```python  theme={null}
    # For agents that use many tools
    tool_agent = Agent(
        role="API Integration Specialist",
        tools=[search_tool, api_tool, data_tool],
        llm=LLM(model="gpt-4o"),  # Excellent function calling
        # OR
        llm=LLM(model="claude-3-5-sonnet")  # Also strong with tools
    )
    ```
  </Accordion>

  <Accordion title="Premature Optimization Without Testing" icon="gear">
    **The Problem**: Making complex model selection decisions based on theoretical performance without validating with actual CrewAI workflows and tasks.

    **Real Example**: Implementing elaborate model switching logic based on task types without testing if the performance gains justify the operational complexity.

    **CrewAI Solution**: Start simple, then optimize based on real performance data:

    ```python  theme={null}
    # Start with this
    crew = Crew(agents=[...], tasks=[...], llm=LLM(model="gpt-4o-mini"))

    # Test performance, then optimize specific agents as needed
    # Use Enterprise platform testing to validate improvements
    ```
  </Accordion>

  <Accordion title="Overlooking Context and Memory Limitations" icon="brain">
    **The Problem**: Not considering how model context windows interact with CrewAI's memory and context sharing between agents.

    **Real Example**: Using a short-context model for agents that need to maintain conversation history across multiple task iterations, or in crews with extensive agent-to-agent communication.

    **CrewAI Solution**: Match context capabilities to crew communication patterns.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Practical Implementation Checklist](./2102-practical-implementation-checklist.md)

**Next:** [Testing and Iteration Strategy →](./2104-testing-and-iteration-strategy.md)
