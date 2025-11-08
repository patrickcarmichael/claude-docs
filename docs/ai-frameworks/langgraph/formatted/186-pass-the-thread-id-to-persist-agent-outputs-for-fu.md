---
title: "Langgraph: pass the thread ID to persist agent outputs for future interactions"
description: "pass the thread ID to persist agent outputs for future interactions section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# pass the thread ID to persist agent outputs for future interactions

config = {"configurable": {"thread_id": "1"}}

for chunk in workflow.stream(
    [
        {
            "role": "user",
            "content": "Find numbers between 10 and 30 in fibonacci sequence",
        }
    ],
    config,
):
    print(chunk)
```
```output
user_proxy (to assistant):

Find numbers between 10 and 30 in fibonacci sequence

--------------------------------------------------------------------------------
assistant (to user_proxy):

To find numbers between 10 and 30 in the Fibonacci sequence, we can generate the Fibonacci sequence and check which numbers fall within this range. Here's a plan:

1. Generate Fibonacci numbers starting from 0.
2. Continue generating until the numbers exceed 30.
3. Collect and print the numbers that are between 10 and 30.

Let's implement this in Python:

\`\`\`python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the graph](./185-run-the-graph.md)

**Next:** [filename: fibonacci_range.py →](./187-filename-fibonacci_rangepy.md)
