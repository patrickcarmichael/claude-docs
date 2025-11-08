---
title: "Crewai: Using Crew Studio"
description: "Using Crew Studio section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Using Crew Studio


Now that you've configured your LLM connection and default settings, you're ready to start using Crew Studio!

<Steps>
  <Step title="Access Studio">
    Navigate to the **Studio** section in your CrewAI AMP dashboard.
  </Step>

  <Step title="Start a Conversation">
    Start a conversation with the Crew Assistant by describing the problem you want to solve:

    ```md  theme={null}
    I need a crew that can research the latest AI developments and create a summary report.
    ```

    The Crew Assistant will ask clarifying questions to better understand your requirements.
  </Step>

  <Step title="Review Generated Crew">
    Review the generated crew configuration, including:

    * Agents and their roles
    * Tasks to be performed
    * Required inputs
    * Tools to be used

    This is your opportunity to refine the configuration before proceeding.
  </Step>

  <Step title="Deploy or Download">
    Once you're satisfied with the configuration, you can:

    * Download the generated code for local customization
    * Deploy the crew directly to the CrewAI AMP platform
    * Modify the configuration and regenerate the crew
  </Step>

  <Step title="Test Your Crew">
    After deployment, test your crew with sample inputs to ensure it performs as expected.
  </Step>
</Steps>

<Tip>
  For best results, provide clear, detailed descriptions of what you want your crew to accomplish. Include specific inputs and expected outputs in your description.
</Tip>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configuration Steps](./1524-configuration-steps.md)

**Next:** [Example Workflow →](./1526-example-workflow.md)
