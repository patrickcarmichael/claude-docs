---
title: "Langgraph: Initialize an in-memory checkpointer for persistence"
description: "Initialize an in-memory checkpointer for persistence section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Initialize an in-memory checkpointer for persistence

checkpointer = InMemorySaver()

@task
def slow_task():
    """
    Simulates a slow-running task by introducing a 1-second delay.
    """
    time.sleep(1)
    return "Ran slow task."

@entrypoint(checkpointer=checkpointer)
def main(inputs, writer: StreamWriter):
    """
    Main workflow function that runs the slow_task and get_info tasks sequentially.

    Parameters:
    - inputs: Dictionary containing workflow input values.
    - writer: StreamWriter for streaming custom data.

    The workflow first executes `slow_task` and then attempts to execute `get_info`,
    which will fail on the first invocation.
    """
    slow_task_result = slow_task().result()  # Blocking call to slow_task
    get_info().result()  # Exception will be raised here on the first attempt
    return slow_task_result

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← This variable is just used for demonstration purposes to simulate a network failure.](./89-this-variable-is-just-used-for-demonstration-purpo.md)

**Next:** [Workflow execution configuration with a unique thread identifier →](./91-workflow-execution-configuration-with-a-unique-thr.md)
