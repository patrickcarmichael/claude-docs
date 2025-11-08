---
title: "Crewai: src/guide_creator_flow/crews/content_crew/config/tasks.yaml"
description: "src/guide_creator_flow/crews/content_crew/config/tasks.yaml section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# src/guide_creator_flow/crews/content_crew/config/tasks.yaml

write_section_task:
  description: >
    Write a comprehensive section on the topic: "{section_title}"

    Section description: {section_description}
    Target audience: {audience_level} level learners

    Your content should:
    1. Begin with a brief introduction to the section topic
    2. Explain all key concepts clearly with examples
    3. Include practical applications or exercises where appropriate
    4. End with a summary of key points
    5. Be approximately 500-800 words in length

    Format your content in Markdown with appropriate headings, lists, and emphasis.

    Previously written sections:
    {previous_sections}

    Make sure your content maintains consistency with previously written sections
    and builds upon concepts that have already been explained.
  expected_output: >
    A well-structured, comprehensive section in Markdown format that thoroughly
    explains the topic and is appropriate for the target audience.
  agent: content_writer

review_section_task:
  description: >
    Review and improve the following section on "{section_title}":

    {draft_content}

    Target audience: {audience_level} level learners

    Previously written sections:
    {previous_sections}

    Your review should:
    1. Fix any grammatical or spelling errors
    2. Improve clarity and readability
    3. Ensure content is comprehensive and accurate
    4. Verify consistency with previously written sections
    5. Enhance the structure and flow
    6. Add any missing key information

    Provide the improved version of the section in Markdown format.
  expected_output: >
    An improved, polished version of the section that maintains the original
    structure but enhances clarity, accuracy, and consistency.
  agent: content_reviewer
  context:
    - write_section_task
```

These task definitions provide detailed instructions to our agents, ensuring they produce content that meets our quality standards. Note how the `context` parameter in the review task creates a workflow where the reviewer has access to the writer's output.

3. Now, update the crew implementation file to define how our agents and tasks work together:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← src/guide_creator_flow/crews/content_crew/config/agents.yaml](./468-srcguide_creator_flowcrewscontent_crewconfigagents.md)

**Next:** [src/guide_creator_flow/crews/content_crew/content_crew.py →](./470-srcguide_creator_flowcrewscontent_crewcontent_crew.md)
