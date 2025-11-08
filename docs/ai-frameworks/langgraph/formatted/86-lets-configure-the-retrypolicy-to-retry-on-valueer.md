---
title: "Langgraph: Let's configure the RetryPolicy to retry on ValueError."
description: "Let's configure the RetryPolicy to retry on ValueError. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Let's configure the RetryPolicy to retry on ValueError.

# The default RetryPolicy is optimized for retrying specific network errors.
retry_policy = RetryPolicy(retry_on=ValueError)

@task(retry_policy=retry_policy)
def get_info():
    global attempts
    attempts += 1

    if attempts < 2:
        raise ValueError('Failure')
    return "OK"

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def main(inputs, writer):
    return get_info().result()

config = {
    "configurable": {
        "thread_id": "1"
    }
}

main.invoke({'any_input': 'foobar'}, config=config)
```

```pycon
'OK'
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← This variable is just used for demonstration purposes to simulate a network failure.](./85-this-variable-is-just-used-for-demonstration-purpo.md)

**Next:** [Caching Tasks →](./87-caching-tasks.md)
