---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

### Basic Usage with Reasoning Tokens

<Template
  data={{
  API_KEY_REF,
  MODEL: "openai/o3-mini"
}}
>
```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const response = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: "How would you build the world's tallest skyscraper?",
        },
      ],
      reasoning: {
        effort: 'high',
      },
      stream: false,
    });

    console.log('REASONING:', response.choices[0].message.reasoning);
    console.log('CONTENT:', response.choices[0].message.content);
```
```python title="Python (OpenAI SDK)"
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "How would you build the world's tallest skyscraper?"}
        ],
        extra_body={
            "reasoning": {
                "effort": "high"
            }
        },
    )

    msg = response.choices[0].message
    print(getattr(msg, "reasoning", None))
```
```typescript title="TypeScript (OpenAI SDK)"
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithReasoning() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "How would you build the world's tallest skyscraper?",
          },
        ],
        reasoning: {
          effort: 'high',
        },
      });

      type ORChatMessage = (typeof response)['choices'][number]['message'] & {
        reasoning?: string;
        reasoning_details?: unknown;
      };

      const msg = response.choices[0].message as ORChatMessage;
      console.log('REASONING:', msg.reasoning);
      console.log('CONTENT:', msg.content);
    }

    getResponseWithReasoning();
```
</Template>

### Using Max Tokens for Reasoning

For models that support direct token allocation (like Anthropic models), you can specify the exact number of tokens to use for reasoning:

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3.7-sonnet"
}}
>
```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What's the most efficient algorithm for sorting a large dataset?"}
        ],
        extra_body={
            "reasoning": {
                "max_tokens": 2000
            }
        },
    )

    msg = response.choices[0].message
    print(getattr(msg, "reasoning", None))
    print(getattr(msg, "content", None))
```
```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithReasoning() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "How would you build the world's tallest skyscraper?",
          },
        ],
        reasoning: {
          max_tokens: 2000,
        },
      });

      type ORChatMessage = (typeof response)['choices'][number]['message'] & {
        reasoning?: string;
      };
      const msg = response.choices[0].message as ORChatMessage;

      console.log('REASONING:', msg.reasoning);
      console.log('CONTENT:', msg.content);
    }

    getResponseWithReasoning();
```
</Template>

### Excluding Reasoning Tokens from Response

If you want the model to use reasoning internally but not include it in the response:

<Template
  data={{
  API_KEY_REF,
  MODEL: "deepseek/deepseek-r1"
}}
>
```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "Explain quantum computing in simple terms."}
        ],
        extra_body={
            "reasoning": {
                "effort": "high",
                "exclude": True
            }
        },
    )

    msg = response.choices[0].message
    print(getattr(msg, "content", None))
```
```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithReasoning() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "How would you build the world's tallest skyscraper?",
          },
        ],
        reasoning: {
          effort: 'high',
          exclude: true,
        },
      });

      const msg = response.choices[0].message as {
        content?: string | null;
      };
      console.log('CONTENT:', msg.content);
    }

    getResponseWithReasoning();
```
</Template>

### Advanced Usage: Reasoning Chain-of-Thought

This example shows how to use reasoning tokens in a more complex workflow. It injects one model's reasoning into another model to improve its response quality:

<Template
  data={{
  API_KEY_REF,
}}
>
```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    question = "Which is bigger: 9.11 or 9.9?"

    def do_req(model: str, content: str, reasoning_config: dict | None = None):
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": content}],
            "stop": "</think>",
        }
        if reasoning_config:
            payload.update(reasoning_config)
        return client.chat.completions.create(**payload)

    # Get reasoning from a capable model

    content = f"{question} Please think this through, but don't output an answer"
    reasoning_response = do_req("deepseek/deepseek-r1", content)
    reasoning = getattr(reasoning_response.choices[0].message, "reasoning", "")

    # Let's test! Here's the naive response:

    simple_response = do_req("openai/gpt-4o-mini", question)
    print(getattr(simple_response.choices[0].message, "content", None))

    # Here's the response with the reasoning token injected:

    content = f"{question}. Here is some context to help you: {reasoning}"
    smart_response = do_req("openai/gpt-4o-mini", content)
    print(getattr(smart_response.choices[0].message, "content", None))
```
```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function doReq(model, content, reasoningConfig) {
      const payload = {
        model,
        messages: [{ role: 'user', content }],
        stop: '</think>',
        ...reasoningConfig,
      };

      return openai.chat.completions.create(payload);
    }

    async function getResponseWithReasoning() {
      const question = 'Which is bigger: 9.11 or 9.9?';
      const reasoningResponse = await doReq(
        'deepseek/deepseek-r1',
        `${question} Please think this through, but don't output an answer`,
      );
      const reasoning = reasoningResponse.choices[0].message.reasoning;

      // Let's test! Here's the naive response:
      const simpleResponse = await doReq('openai/gpt-4o-mini', question);
      console.log(simpleResponse.choices[0].message.content);

      // Here's the response with the reasoning token injected:
      const content = `${question}. Here is some context to help you: ${reasoning}`;
      const smartResponse = await doReq('openai/gpt-4o-mini', content);
      console.log(smartResponse.choices[0].message.content);
    }

    getResponseWithReasoning();
```
</Template>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
