---
title: "Crewai: Practical Implementation Checklist"
description: "Practical Implementation Checklist section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Practical Implementation Checklist


Rather than repeating the strategic framework, here's a tactical checklist for implementing your LLM selection decisions in CrewAI:

<Steps>
  <Step title="Audit Your Current Setup" icon="clipboard-check">
    **What to Review:**

    * Are all agents using the same LLM by default?
    * Which agents handle the most complex reasoning tasks?
    * Which agents primarily do data processing or formatting?
    * Are any agents heavily tool-dependent?

    **Action**: Document current agent roles and identify optimization opportunities.
  </Step>

  <Step title="Implement Crew-Level Strategy" icon="users-gear">
    **Set Your Baseline:**

    ```python  theme={null}
    # Start with a reliable default for the crew
    default_crew_llm = LLM(model="gpt-4o-mini")  # Cost-effective baseline

    crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True
    )
    ```

    **Action**: Establish your crew's default LLM before optimizing individual agents.
  </Step>

  <Step title="Optimize High-Impact Agents" icon="star">
    **Identify and Upgrade Key Agents:**

    ```python  theme={null}
    # Manager or coordination agents
    manager_agent = Agent(
        role="Project Manager",
        llm=LLM(model="gemini-2.5-flash-preview-05-20"),  # Premium for coordination
        # ... rest of config
    )

    # Creative or customer-facing agents
    content_agent = Agent(
        role="Content Creator",
        llm=LLM(model="claude-3-5-sonnet"),  # Best for writing
        # ... rest of config
    )
    ```

    **Action**: Upgrade 20% of your agents that handle 80% of the complexity.
  </Step>

  <Step title="Validate with Enterprise Testing" icon="test-tube">
    **Once you deploy your agents to production:**

    * Use [CrewAI AMP platform](https://app.crewai.com) to A/B test your model selections
    * Run multiple iterations with real inputs to measure consistency and performance
    * Compare cost vs. performance across your optimized setup
    * Share results with your team for collaborative decision-making

    **Action**: Replace guesswork with data-driven validation using the testing platform.
  </Step>
</Steps>

### When to Use Different Model Types

<Tabs>
  <Tab title="Reasoning Models">
    Reasoning models become essential when tasks require genuine multi-step logical thinking, strategic planning, or high-level decision making that benefits from systematic analysis. These models excel when problems need to be broken down into components and analyzed systematically rather than handled through pattern matching or simple instruction following.

    Consider reasoning models for business strategy development, complex data analysis that requires drawing insights from multiple sources, multi-step problem solving where each step depends on previous analysis, and strategic planning tasks that require considering multiple variables and their interactions.

    However, reasoning models often come with higher costs and slower response times, so they're best reserved for tasks where their sophisticated capabilities provide genuine value rather than being used for simple operations that don't require complex reasoning.
  </Tab>

  <Tab title="Creative Models">
    Creative models become valuable when content generation is the primary output and the quality, style, and engagement level of that content directly impact success. These models excel when writing quality and style matter significantly, creative ideation or brainstorming is needed, or brand voice and tone are important considerations.

    Use creative models for blog post writing and article creation, marketing copy that needs to engage and persuade, creative storytelling and narrative development, and brand communications where voice and tone are crucial. These models often understand nuance and context better than general purpose alternatives.

    Creative models may be less suitable for technical or analytical tasks where precision and factual accuracy are more important than engagement and style. They're best used when the creative and communicative aspects of the output are primary success factors.
  </Tab>

  <Tab title="Efficient Models">
    Efficient models are ideal for high-frequency, routine operations where speed and cost optimization are priorities. These models work best when tasks have clear, well-defined parameters and don't require sophisticated reasoning or creative capabilities.

    Consider efficient models for data processing and transformation tasks, simple formatting and organization operations, function calling and tool usage where precision matters more than sophistication, and high-volume operations where cost per operation is a significant factor.

    The key with efficient models is ensuring that their capabilities align with task requirements. They can handle many routine operations effectively but may struggle with tasks requiring nuanced understanding, complex reasoning, or sophisticated content generation.
  </Tab>

  <Tab title="Open Source Models">
    Open source models become attractive when budget constraints are significant, data privacy requirements exist, customization needs are important, or local deployment is required for operational or compliance reasons.

    Consider open source models for internal company tools where data privacy is paramount, privacy-sensitive applications that can't use external APIs, cost-optimized deployments where per-token pricing is prohibitive, and situations requiring custom model modifications or fine-tuning.

    However, open source models require more technical expertise to deploy and maintain effectively. Consider the total cost of ownership including infrastructure, technical overhead, and ongoing maintenance when evaluating open source options.
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example: Technical Documentation Agent](./2101-example-technical-documentation-agent.md)

**Next:** [Common CrewAI Model Selection Pitfalls →](./2103-common-crewai-model-selection-pitfalls.md)
