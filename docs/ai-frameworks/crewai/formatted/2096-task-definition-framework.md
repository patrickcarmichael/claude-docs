---
title: "Crewai: Task Definition Framework"
description: "Task Definition Framework section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Task Definition Framework


### a. Focus on Clarity Over Complexity

Effective task definition is often more important than model selection in determining the quality of CrewAI outputs. Well-defined tasks provide clear direction and context that enable even modest models to perform well, while poorly defined tasks can cause even sophisticated models to produce unsatisfactory results.

<AccordionGroup>
  <Accordion title="Effective Task Descriptions" icon="list-check">
    The best task descriptions strike a balance between providing sufficient detail and maintaining clarity. They should define the specific objective clearly enough that there's no ambiguity about what success looks like, while explaining the approach or methodology in enough detail that the agent understands how to proceed.

    Effective task descriptions include relevant context and constraints that help the agent understand the broader purpose and any limitations they need to work within. They break complex work into focused steps that can be executed systematically, rather than presenting overwhelming, multi-faceted objectives that are difficult to approach systematically.

    Common mistakes include being too vague about objectives, failing to provide necessary context, setting unclear success criteria, or combining multiple unrelated tasks into a single description. The goal is to provide enough information for the agent to succeed while maintaining focus on a single, clear objective.
  </Accordion>

  <Accordion title="Expected Output Guidelines" icon="bullseye">
    Expected output guidelines serve as a contract between the task definition and the agent, clearly specifying what the deliverable should look like and how it will be evaluated. These guidelines should describe both the format and structure needed, as well as the key elements that must be included for the output to be considered complete.

    The best output guidelines provide concrete examples of quality indicators and define completion criteria clearly enough that both the agent and human reviewers can assess whether the task has been completed successfully. This reduces ambiguity and helps ensure consistent results across multiple task executions.

    Avoid generic output descriptions that could apply to any task, missing format specifications that leave agents guessing about structure, unclear quality standards that make evaluation difficult, or failing to provide examples or templates that help agents understand expectations.
  </Accordion>
</AccordionGroup>

### b. Task Sequencing Strategy

<Tabs>
  <Tab title="Sequential Dependencies">
    Sequential task dependencies are essential when tasks build upon previous outputs, information flows from one task to another, or quality depends on the completion of prerequisite work. This approach ensures that each task has access to the information and context it needs to succeed.

    Implementing sequential dependencies effectively requires using the context parameter to chain related tasks, building complexity gradually through task progression, and ensuring that each task produces outputs that serve as meaningful inputs for subsequent tasks. The goal is to maintain logical flow between dependent tasks while avoiding unnecessary bottlenecks.

    Sequential dependencies work best when there's a clear logical progression from one task to another and when the output of one task genuinely improves the quality or feasibility of subsequent tasks. However, they can create bottlenecks if not managed carefully, so it's important to identify which dependencies are truly necessary versus those that are merely convenient.
  </Tab>

  <Tab title="Parallel Execution">
    Parallel execution becomes valuable when tasks are independent of each other, time efficiency is important, or different expertise areas are involved that don't require coordination. This approach can significantly reduce overall execution time while allowing specialized agents to work on their areas of strength simultaneously.

    Successful parallel execution requires identifying tasks that can truly run independently, grouping related but separate work streams effectively, and planning for result integration when parallel tasks need to be combined into a final deliverable. The key is ensuring that parallel tasks don't create conflicts or redundancies that reduce overall quality.

    Consider parallel execution when you have multiple independent research streams, different types of analysis that don't depend on each other, or content creation tasks that can be developed simultaneously. However, be mindful of resource allocation and ensure that parallel execution doesn't overwhelm your available model capacity or budget.
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Efficient model for data processing](./2095-efficient-model-for-data-processing.md)

**Next:** [Optimizing Agent Configuration for LLM Performance →](./2097-optimizing-agent-configuration-for-llm-performance.md)
