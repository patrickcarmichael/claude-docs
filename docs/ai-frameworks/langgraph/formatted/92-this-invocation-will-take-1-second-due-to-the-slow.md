---
title: "Langgraph: This invocation will take ~1 second due to the slow_task execution"
description: "This invocation will take ~1 second due to the slow_task execution section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# This invocation will take ~1 second due to the slow_task execution

try:
    # First invocation will raise an exception due to the `get_info` task failing
    main.invoke({'any_input': 'foobar'}, config=config)
except ValueError:
    pass  # Handle the failure gracefully
```

When we resume execution, we won't need to re-run the `slow_task` as its result is already saved in the checkpoint.

```python
main.invoke(None, config=config)
```

```pycon
'Ran slow task.'
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Workflow execution configuration with a unique thread identifier](./91-workflow-execution-configuration-with-a-unique-thr.md)

**Next:** [Human-in-the-loop →](./93-human-in-the-loop.md)
