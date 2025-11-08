---
title: "Crewai: Best Practices"
description: "Best Practices section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Best Practices


### Context Guidelines

<Steps>
  <Step title="Provide Comprehensive Context">
    Include all relevant factual information that the AI should base its output on:

    ```python  theme={null}
    context = """
    Company XYZ was founded in 2020 and specializes in renewable energy solutions.
    They have 150 employees and generated $50M revenue in 2023.
    Their main products include solar panels and wind turbines.
    """
    ```
  </Step>

  <Step title="Keep Context Relevant">
    Only include information directly related to the task to avoid confusion:

    ```python  theme={null}
    # Good: Focused context
    context = "The current weather in New York is 18°C with light rain."

    # Avoid: Unrelated information
    context = "The weather is 18°C. The city has 8 million people. Traffic is heavy."
    ```
  </Step>

  <Step title="Update Context Regularly">
    Ensure your reference context reflects current, accurate information.
  </Step>
</Steps>

### Threshold Selection

<Steps>
  <Step title="Start with Default Validation">
    Begin without custom thresholds to understand baseline performance.
  </Step>

  <Step title="Adjust Based on Requirements">
    * **High-stakes content**: Use threshold 8-10 for maximum accuracy
    * **General content**: Use threshold 6-7 for balanced validation
    * **Creative content**: Use threshold 4-5 or default verdict-based validation
  </Step>

  <Step title="Monitor and Iterate">
    Track validation results and adjust thresholds based on false positives/negatives.
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task output validation flow](./1464-task-output-validation-flow.md)

**Next:** [Performance Considerations →](./1466-performance-considerations.md)
