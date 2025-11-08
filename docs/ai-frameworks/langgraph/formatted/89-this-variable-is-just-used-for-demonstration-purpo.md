---
title: "Langgraph: This variable is just used for demonstration purposes to simulate a network failure."
description: "This variable is just used for demonstration purposes to simulate a network failure. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# This variable is just used for demonstration purposes to simulate a network failure.

# It's not something you will have in your actual code.
attempts = 0

@task()
def get_info():
    """
    Simulates a task that fails once before succeeding.
    Raises an exception on the first attempt, then returns "OK" on subsequent tries.
    """
    global attempts
    attempts += 1

    if attempts < 2:
        raise ValueError("Failure")  # Simulate a failure on the first attempt
    return "OK"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Resuming after an error](./88-resuming-after-an-error.md)

**Next:** [Initialize an in-memory checkpointer for persistence →](./90-initialize-an-in-memory-checkpointer-for-persisten.md)
