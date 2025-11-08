---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Asynchronous usage

async def main():
    response = await llm.completions.acreate(
        prompt="Hello, world!"
    )
    print(response.choices[0].text)

    # Async streaming

    async for chunk in llm.completions.acreate(
        prompt="Tell me a story",
        stream=True
    ):
        if chunk.choices[0].text:
            print(chunk.choices[0].text, end="")

asyncio.run(main())
```typescript

### `chat.completions.create()` and `chat.completions.acreate()`

Creates a chat completion using the LLM. These methods are OpenAI compatible and follow the same interface as described in the [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create). Use `create()` for synchronous calls and `acreate()` for asynchronous calls.

**Note:** The Fireworks chat completions API includes additional request and response fields beyond the standard OpenAI API. See the [Fireworks Chat Completions API reference](/api-reference/post-chatcompletions) for the complete set of available parameters and response fields.

**Arguments:**

* `messages` *list* - A list of messages comprising the conversation so far
* `stream` *bool, optional* - Whether to stream the response. Defaults to False
* `response_format` *dict, optional* - An object specifying the format that the model must output
* `reasoning_effort` *str, optional* - How much effort the model should put into reasoning
* `max_tokens` *int, optional* - The maximum number of tokens to generate
* `temperature` *float, optional* - Sampling temperature between 0 and 2. If not provided, uses the LLM's default temperature. Note that temperature can also be set once during LLM instantiation if preferred
* `tools` *list, optional* - A list of tools the model may call
* `extra_headers` *dict, optional* - Additional headers to include in the request
* `**kwargs` - Additional parameters supported by the OpenAI API

**Returns:**

* `ChatCompletion` when `stream=False` (default)
* `Generator[ChatCompletionChunk, None, None]` when `stream=True` (sync version)
* `AsyncGenerator[ChatCompletionChunk, None]` when `stream=True` (async version)

For details on the `ChatCompletion` object structure, see the [OpenAI Chat Completion Object documentation](https://platform.openai.com/docs/api-reference/chat/object). For the `ChatCompletionChunk` object structure used in streaming, see the [OpenAI Chat Streaming documentation](https://platform.openai.com/docs/api-reference/chat-streaming/streaming).
```python
import asyncio
from fireworks import LLM

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
