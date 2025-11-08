---
title: "Langgraph: Streaming"
description: "Streaming section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Streaming


The **Functional API** uses the same streaming mechanism as the **Graph API**. Please
read the [**streaming guide**](../concepts/streaming.md) section for more details.

Example of using the streaming API to stream both updates and custom data.

```python hl_lines="17"
from langgraph.func import entrypoint
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer # (1)!

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def main(inputs: dict) -> int:
    writer = get_stream_writer() # (2)!
    writer("Started processing") # (3)!
    result = inputs["x"] * 2
    writer(f"Result is {result}") # (4)!
    return result

config = {"configurable": {"thread_id": "abc"}}

for mode, chunk in main.stream( # (5)!
    {"x": 5},
    stream_mode=["custom", "updates"], # (6)!
    config=config
):
    print(f"{mode}: {chunk}")
```

1. Import `get_stream_writer` from `langgraph.config`.
2. Obtain a stream writer instance within the entrypoint.
3. Emit custom data before computation begins.
4. Emit another custom message after computing the result.
5. Use `.stream()` to process streamed output.
6. Specify which streaming modes to use.

```pycon
('updates', {'add_one': 2})
('updates', {'add_two': 3})
('custom', 'hello')
('custom', 'world')
('updates', {'main': 5})
```

!!! important "Async with Python < 3.11"

    If using Python < 3.11 and writing async code, using `get_stream_writer()` will not work. Instead please
    use the `StreamWriter` class directly. See [Async with Python < 3.11](../how-tos/streaming.md#async) for more details.

    ```python hl_lines="4"
    from langgraph.types import StreamWriter

    @entrypoint(checkpointer=checkpointer)
    async def main(inputs: dict, writer: StreamWriter) -> int:
        ...
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Call other entrypoints](./82-call-other-entrypoints.md)

**Next:** [Retry policy →](./84-retry-policy.md)
