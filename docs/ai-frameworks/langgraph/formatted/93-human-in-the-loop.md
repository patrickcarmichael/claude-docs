---
title: "Langgraph: Human-in-the-loop"
description: "Human-in-the-loop section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Human-in-the-loop


The functional API supports [human-in-the-loop](../concepts/human_in_the_loop.md) workflows using the `interrupt` function and the `Command` primitive.

### Basic human-in-the-loop workflow

We will create three [tasks](../concepts/functional_api.md#task):

1. Append `"bar"`.
2. Pause for human input. When resuming, append human input.
3. Append `"qux"`.

```python
from langgraph.func import entrypoint, task
from langgraph.types import Command, interrupt

@task
def step_1(input_query):
    """Append bar."""
    return f"{input_query} bar"

@task
def human_feedback(input_query):
    """Append user input."""
    feedback = interrupt(f"Please provide feedback: {input_query}")
    return f"{input_query} {feedback}"

@task
def step_3(input_query):
    """Append qux."""
    return f"{input_query} qux"
```

We can now compose these tasks in an [entrypoint](../concepts/functional_api.md#entrypoint):

```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def graph(input_query):
    result_1 = step_1(input_query).result()
    result_2 = human_feedback(result_1).result()
    result_3 = step_3(result_2).result()

    return result_3
```

[interrupt()](../how-tos/human_in_the_loop/add-human-in-the-loop.md#pause-using-interrupt) is called inside a task, enabling a human to review and edit the output of the previous task. The results of prior tasks-- in this case `step_1`-- are persisted, so that they are not run again following the `interrupt`.

Let's send in a query string:

```python
config = {"configurable": {"thread_id": "1"}}

for event in graph.stream("foo", config):
    print(event)
    print("\n")
```

Note that we've paused with an `interrupt` after `step_1`. The interrupt provides instructions to resume the run. To resume, we issue a [Command](../how-tos/human_in_the_loop/add-human-in-the-loop.md#resume-using-the-command-primitive) containing the data expected by the `human_feedback` task.

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← This invocation will take ~1 second due to the slow_task execution](./92-this-invocation-will-take-1-second-due-to-the-slow.md)

**Next:** [Continue execution →](./94-continue-execution.md)
