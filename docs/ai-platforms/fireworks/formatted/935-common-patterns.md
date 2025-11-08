---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common patterns

### Multi-turn conversations

Maintain conversation history by including all previous messages:
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What's its population?"}
]

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=messages
)

print(response.choices[0].message.content)
```
The model uses the full conversation history to provide contextually relevant responses.

### System prompts

Override the default system prompt by setting the first message with `role: "system"`:
```python
messages = [
    {"role": "system", "content": "You are a helpful Python expert who provides concise code examples."},
    {"role": "user", "content": "How do I read a CSV file?"}
]

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=messages
)
```
To completely omit the system prompt, set the first message's `content` to an empty string.

### Streaming responses

Stream tokens as they're generated for real time, interactive UX. Covered in detail in the [Serverless Quickstart](/getting-started/quickstart#streaming-responses).
```python
stream = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```
**Aborting streams:** Close the connection to stop generation and avoid billing for ungenerated tokens:
```python
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
    if some_condition:
        stream.close()
        break
```

### Async requests

Use async clients to make multiple concurrent requests for better throughput:

<Tabs>
  <Tab title="Python">
```python
    import asyncio
    from openai import AsyncOpenAI

    client = AsyncOpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    async def main():
        response = await client.chat.completions.create(
            model="accounts/fireworks/models/deepseek-v3p1",
            messages=[{"role": "user", "content": "Hello"}]
        )
        print(response.choices[0].message.content)

    asyncio.run(main())
```
  </Tab>

  <Tab title="JavaScript">
```javascript
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    async function main() {
      const response = await client.chat.completions.create({
        model: "accounts/fireworks/models/deepseek-v3p1",
        messages: [{ role: "user", content: "Hello" }],
      });
      console.log(response.choices[0].message.content);
    }

    main();
```
  </Tab>
</Tabs>

### Usage & performance tracking

Every response includes token usage information and performance metrics for debugging and observability. For aggregate metrics over time, see the [usage dashboard](https://app.fireworks.ai/account/usage).

**Token usage** (prompt, completion, total tokens) is included in the response body for all requests.

**Performance metrics** (latency, time-to-first-token, etc.) are included in response headers for non-streaming requests. For streaming requests, use the `perf_metrics_in_response` parameter to include all metrics in the response body.

<Tabs>
  <Tab title="Non-streaming">
```python
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}]
    )

    # Token usage (always included)

    print(response.usage.prompt_tokens)      # Tokens in your prompt

    print(response.usage.completion_tokens)  # Tokens generated

    print(response.usage.total_tokens)       # Total tokens billed

    # Performance metrics are in response headers:

    # fireworks-prompt-tokens, fireworks-server-time-to-first-token, etc.

```
  </Tab>

  <Tab title="Streaming (usage only)">
```python
    stream = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
        
        # Usage is included in the final chunk

        if chunk.usage:
            print(f"\n\nTokens used: {chunk.usage.total_tokens}")
            print(f"Prompt: {chunk.usage.prompt_tokens}, Completion: {chunk.usage.completion_tokens}")
```
  </Tab>

  <Tab title="Streaming (with performance metrics)">
```python
    stream = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello, world!"}],
        stream=True,
        extra_body={"perf_metrics_in_response": True}
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
        
        # Both usage and performance metrics are in the final chunk

        if chunk.choices[0].finish_reason:
            if chunk.usage:
                print(f"\n\nTokens: {chunk.usage.total_tokens}")
            if hasattr(chunk, 'perf_metrics'):
                print(f"Performance: {chunk.perf_metrics}")
```
  </Tab>
</Tabs>

>   **📝 Note**
>
> Usage information is automatically included in the final chunk for streaming responses (the chunk with `finish_reason` set). This is a Fireworks extension - OpenAI SDK doesn't return usage for streaming by default.

For all available metrics and details, see the [API reference documentation](/api-reference/post-chatcompletions#response-perf_metrics).

<Tip>
  If you encounter errors during inference, see [Inference Error Codes](/guides/inference-error-codes) for common issues and resolutions.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
