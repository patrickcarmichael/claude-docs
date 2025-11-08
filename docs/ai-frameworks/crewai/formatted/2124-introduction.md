---
title: "Crewai: Introduction"
description: "Introduction section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Introduction


CrewAI provides the ability to replay from a task specified from the latest crew kickoff. This feature is particularly useful when you've finished a kickoff and may want to retry certain tasks or don't need to refetch data over and your agents already have the context saved from the kickoff execution so you just need to replay the tasks you want to.

<Note>
  You must run `crew.kickoff()` before you can replay a task.
  Currently, only the latest kickoff is supported, so if you use `kickoff_for_each`, it will only allow you to replay from the most recent crew run.
</Note>

Here's an example of how to replay from a task:

### Replaying from Specific Task Using the CLI

To use the replay feature, follow these steps:

<Steps>
  <Step title="Open your terminal or command prompt." />

  <Step title="Navigate to the directory where your CrewAI project is located." />

  <Step title="Run the following commands:">
    To view the latest kickoff task\_ids use:

    ```shell  theme={null}
    crewai log-tasks-outputs
    ```

    Once you have your `task_id` to replay, use:

    ```shell  theme={null}
    crewai replay -t <task_id>
    ```
  </Step>
</Steps>

<Note>
  Ensure `crewai` is installed and configured correctly in your development environment.
</Note>

### Replaying from a Task Programmatically

To replay from a task programmatically, use the following steps:

<Steps>
  <Step title="Specify the `task_id` and input parameters for the replay process.">
    Specify the `task_id` and input parameters for the replay process.
  </Step>

  <Step title="Execute the replay command within a try-except block to handle potential errors.">
    Execute the replay command within a try-except block to handle potential errors.

    <CodeGroup>
      ```python Code theme={null}
        def replay():
        """
        Replay the crew execution from a specific task.
        """
        task_id = '<task_id>'
        inputs = {"topic": "CrewAI Training"}  # This is optional; you can pass in the inputs you want to replay; otherwise, it uses the previous kickoff's inputs.
        try:
            YourCrewName_Crew().crew().replay(task_id=task_id, inputs=inputs)

        except subprocess.CalledProcessError as e:
            raise Exception(f"An error occurred while replaying the crew: {e}")

        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")
      ```
    </CodeGroup>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Replay Tasks from Latest Crew Kickoff](./2123-replay-tasks-from-latest-crew-kickoff.md)

**Next:** [Conclusion →](./2125-conclusion.md)
