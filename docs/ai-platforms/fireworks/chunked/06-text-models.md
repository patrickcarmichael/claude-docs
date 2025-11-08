**Navigation:** [← Previous](./05-svg-drawing-agent.md) | [Index](./index.md) | [Next →](./07-firectl-list-secret.md)

---

# Text Models
Source: https://docs.fireworks.ai/guides/querying-text-models

Query, track and manage inference for text models

<Info>
  New to Fireworks? Start with the [Serverless Quickstart](/getting-started/quickstart) for a step-by-step guide to making your first API call.
</Info>

Fireworks provides fast, cost-effective access to leading open-source text models through OpenAI-compatible APIs. Query models via serverless inference or dedicated deployments using the chat completions API (recommended), completions API, or responses API. [Browse 100+ available models →](https://fireworks.ai/models)

## Chat Completions API

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{
            "role": "user",
            "content": "Explain quantum computing in simple terms"
        }]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [
        {
          role: "user",
          content: "Explain quantum computing in simple terms",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
          {
            "role": "user",
            "content": "Explain quantum computing in simple terms"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

<Tip>
  Most models automatically format your messages with the correct template. To verify the exact prompt used, enable the [`echo`](#debugging--advanced-options) parameter.
</Tip>

## Alternative query methods

Fireworks also supports [Completions API](/guides/completions-api) and [Responses API](/guides/response-api).

## Querying dedicated deployments

For consistent performance, guaranteed capacity, or higher throughput, you can query [on-demand deployments](/guides/ondemand-deployments) instead of serverless models. Deployments use the same APIs with a deployment-specific model identifier:

```
<MODEL_NAME>#<DEPLOYMENT_NAME>
```

For example:

```python  theme={null}
response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Common patterns

### Multi-turn conversations

Maintain conversation history by including all previous messages:

```python  theme={null}
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

```python  theme={null}
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

```python  theme={null}
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

```python  theme={null}
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
    ```python  theme={null}
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
    ```javascript  theme={null}
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
    ```python  theme={null}
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
    ```python  theme={null}
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
    ```python  theme={null}
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

<Note>
  Usage information is automatically included in the final chunk for streaming responses (the chunk with `finish_reason` set). This is a Fireworks extension - OpenAI SDK doesn't return usage for streaming by default.
</Note>

For all available metrics and details, see the [API reference documentation](/api-reference/post-chatcompletions#response-perf_metrics).

<Tip>
  If you encounter errors during inference, see [Inference Error Codes](/guides/inference-error-codes) for common issues and resolutions.
</Tip>

## Advanced capabilities

Extend text models with additional features for structured outputs, tool integration, and performance optimization:

<CardGroup cols={3}>
  <Card title="Tool calling" href="/guides/function-calling" icon="function">
    Connect models to external tools and APIs with type-safe parameters
  </Card>

  <Card title="Structured outputs" href="/structured-responses/structured-response-formatting" icon="brackets-curly">
    Enforce JSON schemas for reliable data extraction
  </Card>

  <Card title="Responses API" href="/guides/response-api" icon="brain">
    Multi-step reasoning for complex problem-solving
  </Card>

  <Card title="Predicted outputs" href="/guides/predicted-outputs" icon="bolt">
    Speed up edits by predicting unchanged sections
  </Card>

  <Card title="Prompt caching" href="/guides/prompt-caching" icon="database">
    Cache common prompts to reduce latency and cost
  </Card>

  <Card title="Batch inference" href="/guides/batch-inference" icon="list-check">
    Process large volumes of requests asynchronously
  </Card>
</CardGroup>

## Configuration & debugging

<AccordionGroup>
  <Accordion title="Sampling parameters">
    Control how the model generates text. Fireworks automatically uses recommended sampling parameters from each model's HuggingFace `generation_config.json` when you don't specify them explicitly, ensuring optimal performance out-of-the-box.

    We pull `temperature`, `top_k`, `top_p`, `min_p`, and `typical_p` from the model's configuration when not explicitly provided.

    ### Temperature

    Adjust randomness (0 = deterministic, higher = more creative):

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Write a poem"}],
        temperature=0.7  # Override model default
    )
    ```

    ### Max tokens

    Control the maximum number of tokens in the generated completion:

    ```python  theme={null}
    max_tokens=100  # Generate at most 100 tokens
    ```

    **Important notes:**

    * Default value is 2048 tokens if not specified
    * Most models support up to their full context window (e.g., 128K for DeepSeek R1)
    * When the limit is reached, you'll see `"finish_reason": "length"` in the response

    <Tip>
      Set `max_tokens` appropriately for your use case to avoid truncated responses. Check the model's context window in the [Model Library](https://fireworks.ai/models).
    </Tip>

    ### Top-p (nucleus sampling)

    Consider only the most probable tokens summing to `top_p` probability mass:

    ```python  theme={null}
    top_p=0.9  # Consider top 90% probability mass
    ```

    ### Top-k

    Consider only the k most probable tokens:

    ```python  theme={null}
    top_k=50  # Consider top 50 tokens
    ```

    ### Min-p

    Exclude tokens below a probability threshold:

    ```python  theme={null}
    min_p=0.05  # Exclude tokens with <5% probability
    ```

    ### Typical-p

    Use typical sampling to select tokens with probability close to the entropy of the distribution:

    ```python  theme={null}
    typical_p=0.95  # Consider tokens with typical probability
    ```

    ### Repetition penalties

    Reduce repetitive text with `frequency_penalty`, `presence_penalty`, or `repetition_penalty`:

    ```python  theme={null}
    frequency_penalty=0.5,   # Penalize frequent tokens (OpenAI compatible)
    presence_penalty=0.5,    # Penalize any repeated token (OpenAI compatible)
    repetition_penalty=1.1   # Exponential penalty from prompt + output
    ```

    ### Sampling options header

    The `fireworks-sampling-options` header contains the actual default sampling parameters used for the model, including values from the model's HuggingFace `generation_config.json`:

    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        import os
        from openai import OpenAI

        client = OpenAI(
            api_key=os.environ.get("FIREWORKS_API_KEY"),
            base_url="https://api.fireworks.ai/inference/v1"
        )

        response = client.chat.completions.with_raw_response.create(
            model="accounts/fireworks/models/deepseek-v3p1",
            messages=[{"role": "user", "content": "Hello"}]
        )

        # Access headers from the raw response
        sampling_options = response.headers.get('fireworks-sampling-options')
        print(sampling_options)  # e.g., '{"temperature": 0.7, "top_p": 0.9}'

        completion = response.parse()  # get the parsed response object
        print(completion.choices[0].message.content)
        ```
      </Tab>

      <Tab title="JavaScript">
        ```javascript  theme={null}
        import OpenAI from "openai";

        const client = new OpenAI({
          apiKey: process.env.FIREWORKS_API_KEY,
          baseURL: "https://api.fireworks.ai/inference/v1",
        });

        const response = await client.chat.completions.with_raw_response.create({
          model: "accounts/fireworks/models/deepseek-v3p1",
          messages: [{ role: "user", content: "Hello" }],
        });

        // Access headers from the raw response
        const samplingOptions = response.headers.get('fireworks-sampling-options');
        console.log(samplingOptions); // e.g., '{"temperature": 0.7, "top_p": 0.9}'

        const completion = response.parse(); // get the parsed response object
        console.log(completion.choices[0].message.content);
        ```
      </Tab>
    </Tabs>

    See the [API reference](/api-reference/post-chatcompletions) for detailed parameter descriptions.
  </Accordion>

  <Accordion title="Multiple generations">
    Generate multiple completions in one request:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Tell me a joke"}],
        n=3  # Generate 3 different jokes
    )

    for choice in response.choices:
        print(choice.message.content)
    ```
  </Accordion>

  <Accordion title="Token probabilities (logprobs)">
    Inspect token probabilities for debugging or analysis:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        logprobs=True,
        top_logprobs=5  # Show top 5 alternatives per token
    )

    for content in response.choices[0].logprobs.content:
        print(f"Token: {content.token}, Logprob: {content.logprob}")
    ```
  </Accordion>

  <Accordion title="Prompt inspection (echo & raw_output)">
    Verify how your prompt was formatted:

    **Echo:** Return the prompt along with the generation:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        echo=True
    )
    ```

    **Raw output:** See raw token IDs and prompt fragments:

    <Warning>
      Experimental API - may change without notice.
    </Warning>

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        raw_output=True
    )

    print(response.raw_output.prompt_token_ids)  # Token IDs
    print(response.raw_output.completion)        # Raw completion
    ```
  </Accordion>

  <Accordion title="Ignore EOS token">
    Force generation to continue past the end-of-sequence token (useful for benchmarking):

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        ignore_eos=True,
        max_tokens=100  # Will always generate exactly 100 tokens
    )
    ```

    <Note>
      Output quality may degrade when ignoring EOS. This API is experimental and should not be relied upon for production use cases.
    </Note>
  </Accordion>

  <Accordion title="Logit bias">
    Modify token probabilities to encourage or discourage specific tokens:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        logit_bias={
            123: 10.0,   # Strongly encourage token ID 123
            456: -50.0   # Strongly discourage token ID 456
        }
    )
    ```
  </Accordion>

  <Accordion title="Mirostat sampling">
    Control perplexity dynamically using the [Mirostat algorithm](https://arxiv.org/abs/2007.14966):

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        mirostat_target=5.0,  # Target perplexity
        mirostat_lr=0.1       # Learning rate for adjustments
    )
    ```
  </Accordion>
</AccordionGroup>

## Understanding tokens

Language models process text in chunks called **tokens**. In English, a token can be as short as one character or as long as one word. Different model families use different **tokenizers**, so the same text may translate to different token counts depending on the model.

**Why tokens matter:**

* Models have maximum context lengths measured in tokens
* Pricing is based on token usage (prompt + completion)
* Token count affects response time

For Llama models, use [this tokenizer tool](https://belladoreai.github.io/llama-tokenizer-js/example-demo/build/) to estimate token counts. Actual usage is returned in the `usage` field of every API response.

## OpenAI SDK Migration

<Accordion title="OpenAI SDK compatibility notes">
  Fireworks provides an OpenAI-compatible API, making migration straightforward. However, there are some minor differences to be aware of:

  ### Behavioral differences

  **`stop` parameter:**

  * **Fireworks**: Returns text including the stop word
  * **OpenAI**: Omits the stop word
  * *You can easily truncate it client-side if needed*

  **`max_tokens` with context limits:**

  * **Fireworks**: Automatically adjusts `max_tokens` lower if `prompt + max_tokens` exceeds the model's context window
  * **OpenAI**: Returns an invalid request error
  * *Control this behavior with the `context_length_exceeded_behavior` parameter*

  **Streaming usage stats:**

  * **Fireworks**: Returns `usage` field in the final chunk (where `finish_reason` is set) for both streaming and non-streaming
  * **OpenAI**: Only returns usage for non-streaming responses

  Example accessing streaming usage:

  ```python  theme={null}
  for chunk in client.chat.completions.create(stream=True, ...):
      if chunk.usage:  # Available in final chunk
          print(f"Tokens: {chunk.usage.total_tokens}")
  ```

  ### Unsupported parameters

  The following OpenAI parameters are not yet supported:

  * `presence_penalty`
  * `frequency_penalty`
  * `best_of` (use `n` instead)
  * `logit_bias`
  * `functions` (deprecated - use [Tool Calling](/guides/function-calling) with the `tools` parameter instead)

  Have a use case requiring one of these? [Join our Discord](https://discord.gg/fireworks-ai) to discuss.
</Accordion>

## Next steps

<CardGroup cols={3}>
  <Card title="Vision models" href="/guides/querying-vision-language-models" icon="image">
    Process images alongside text
  </Card>

  <Card title="Audio models" href="/guides/querying-asr-models" icon="microphone">
    Transcribe and translate audio
  </Card>

  <Card title="Embeddings" href="/guides/querying-embeddings-models" icon="database">
    Generate vector representations for search
  </Card>

  <Card title="On-demand deployments" href="/guides/ondemand-deployments" icon="server">
    Deploy models on dedicated GPUs
  </Card>

  <Card title="Fine-tuning" href="/fine-tuning/finetuning-intro" icon="sliders">
    Customize models for your use case
  </Card>

  <Card title="Error codes" href="/guides/inference-error-codes" icon="circle-exclamation">
    Troubleshoot common inference errors
  </Card>

  <Card title="API Reference" href="/api-reference/post-chatcompletions" icon="code">
    Complete API documentation
  </Card>
</CardGroup>


# Vision Models
Source: https://docs.fireworks.ai/guides/querying-vision-language-models

Query vision-language models to analyze images and visual content

<Info>
  New to Fireworks? Start with the [Serverless Quickstart](/getting-started/quickstart#vision-models) to see a vision model example, then return here for more details.
</Info>

Vision-language models (VLMs) process both text and images in a single request, enabling image captioning, visual question answering, document analysis, chart interpretation, OCR, and content moderation. Use VLMs via serverless inference or [dedicated deployments](/getting-started/ondemand-quickstart). [Browse available vision models →](https://app.fireworks.ai/models?filter=Vision)

## Chat Completions API

Provide images via URL or base64 encoding:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Can you describe this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
                        }
                    }
                ]
            }
        ]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Can you describe this image?" },
            {
              type: "image_url",
              image_url: {
                url: "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
              }
            }
          ]
        }
      ]
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "Can you describe this image?"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
                }
              }
            ]
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

<Accordion title="Using base64-encoded images">
  Instead of URLs, you can provide base64-encoded images prefixed with MIME types:

  ```python  theme={null}
  import os
  import base64
  from openai import OpenAI

  # Helper function to encode the image
  def encode_image(image_path):
      with open(image_path, "rb") as image_file:
          return base64.b64encode(image_file.read()).decode('utf-8')

  # Encode your image
  image_base64 = encode_image("your_image.jpg")

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  response = client.chat.completions.create(
      model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Can you describe this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": f"data:image/jpeg;base64,{image_base64}"
                      }
                  }
              ]
          }
      ]
  )

  print(response.choices[0].message.content)
  ```
</Accordion>

## Working with images

Vision-language models support [prompt caching](/guides/prompt-caching) to improve performance for requests with repeated content. Both text and image portions can benefit from caching to reduce time to first token by up to 80%.

**Tips for optimal performance:**

* **Use URLs for long conversations** – Reduces latency compared to base64 encoding
* **Downsize images** – Smaller images use fewer tokens and process faster
* **Structure prompts for caching** – Place static instructions at the beginning, variable content at the end
* **Include metadata in prompts** – Add context about the image directly in your text prompt

## Advanced capabilities

<CardGroup cols={3}>
  <Card title="Vision fine-tuning" href="/fine-tuning/fine-tuning-vlm" icon="sliders">
    Fine-tune VLMs for specialized visual tasks
  </Card>

  <Card title="LoRA adapters" href="/models/uploading-custom-models" icon="layer-group">
    Deploy custom LoRA adapters for vision models
  </Card>

  <Card title="Dedicated deployments" href="/getting-started/ondemand-quickstart" icon="server">
    Deploy VLMs on dedicated GPUs for better performance
  </Card>
</CardGroup>

## Alternative query methods

<Accordion title="Completions API (advanced)">
  For the Completions API, manually insert the image token `<image>` in your prompt and supply images as an ordered list:

  ```python  theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  response = client.completions.create(
      model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      prompt="SYSTEM: Hello\n\nUSER:<image>\ntell me about the image\n\nASSISTANT:",
      extra_body={
          "images": ["https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"]
      }
  )

  print(response.choices[0].text)
  ```
</Accordion>

## Known limitations

1. **Maximum images per request**: 30 images maximum, regardless of format (base64 or URL)
2. **Base64 size limit**: Total base64-encoded images must be less than 10MB
3. **URL size and timeout**: Each image URL must be smaller than 5MB and download within 1.5 seconds
4. **Supported formats**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.ppm`
5. **Llama 3.2 Vision models**: Pass images before text in the content field to avoid refusals (temporary limitation)


# Rate Limits & Quotas
Source: https://docs.fireworks.ai/guides/quotas_usage/rate-limits

Understand and manage your rate limits, spend limits and quotas

## Check your current limits

View your account's current quotas and limits:

```bash  theme={null}
firectl list quotas
```

This shows your rate limits, GPU quotas, spend limits, and usage across serverless and on-demand deployments.

## Spending tiers

Your account tier determines the maximum budget you can set:

| Tier      | Criteria                                              | Max Monthly Budget |
| --------- | ----------------------------------------------------- | ------------------ |
| Tier 1    | [Valid payment method](https://fireworks.ai/billing)  | \$50               |
| Tier 2    | Spend or add \$50 in credits                          | \$500              |
| Tier 3    | Spend or add \$500 in credits                         | \$5,000            |
| Tier 4    | Spend or add \$5,000 in credits                       | \$50,000           |
| Unlimited | [Contact us](https://fireworks.ai/company/contact-us) | Unlimited          |

<Tip>
  Add prepaid credits to unlock a higher tier. For example, adding \$100 moves you from Tier 1 to Tier 2. Your new tier activates within minutes.
</Tip>

## Manage your quotas

<AccordionGroup>
  <Accordion title="Budget control">
    Control your monthly spending with flexible budget limits. Set a limit that fits your needs and adjust it anytime.

    ### View and adjust your spend limit

    Check your current spend limit:

    ```bash  theme={null}
    firectl list quotas
    ```

    Set a custom monthly budget:

    ```bash  theme={null}
    firectl update quota monthly-spend-usd --value <AMOUNT>
    ```

    For example, to set a \$200 monthly budget:

    ```bash  theme={null}
    firectl update quota monthly-spend-usd --value 200
    ```

    ### When you reach your budget

    When you reach your spending limit, all API requests pause automatically across serverless inference, deployments, and fine-tuning. To resume, [add credits](https://fireworks.ai/billing) to increase your tier and set a higher budget.
  </Accordion>

  <Accordion title="On-demand deployment quotas">
    On-demand deployments have GPU quotas instead of rate limits:

    | GPU Type                         | Default Quota |
    | -------------------------------- | ------------- |
    | Nvidia A100                      | 8 GPUs        |
    | Nvidia H100                      | 8 GPUs        |
    | Nvidia H200                      | 8 GPUs        |
    | GPU hours/month                  | 2,000         |
    | LoRAs (on-demand and serverless) | 100           |

    <Tip>
      Need more GPUs? [Contact us](https://fireworks.ai/company/contact-us) to request a quota increase.
    </Tip>
  </Accordion>

  <Accordion title="Serverless rate limits">
    ### Default limits

    All accounts with a payment method get these limits:

    | Limit                                    | Value |
    | ---------------------------------------- | ----- |
    | Requests per minute (RPM)                | 6,000 |
    | Audio min per minute, Whisper-v3-large   | 200   |
    | Audio min per minute, Whisper-v3-turbo   | 400   |
    | Concurrent connections, streaming speech | 10    |
    | LoRAs (on-demand and serverless)         | 100   |

    <Tip>
      Make sure to add a [payment method](https://fireworks.ai/billing) to access higher rate limits up to 6,000 RPM. Without a payment method, you're limited to 10 RPM. Your rate limits will increase automatically once the payment method is added.
    </Tip>

    <Tip>
      During periods of high load, RPM limit may be lower.
    </Tip>

    ### How rate limiting works

    Dynamic rate limits support high RPM limits in a fair manner, while limiting spiky traffic from impacting other users:

    * **Gradual scaling**: Your minimum limits increase as you sustain consistent high usage
    * **Typical scale-up**: Traffic can typically double within an hour without issues
    * **Burst handling**: Short traffic spikes are accommodated during autoscaling

    **Monitoring your limits:**

    * Check response headers to see your current limits and remaining capacity
    * `x-ratelimit-limit-requests`: Your current minimum limit
    * `x-ratelimit-remaining-requests`: Remaining capacity
    * `x-ratelimit-over-limit: yes`: Your request was processed but you're near capacity

    <Tip>
      For production workloads requiring consistent performance and higher limits, use [on-demand deployments](/guides/ondemand-deployments). They provide dedicated GPUs with no rate limits and SLA guarantees.
    </Tip>
  </Accordion>

  <Accordion title="Account recovery">
    If your account is suspended due to failed payment:

    1. Go to [Billing → Invoices](https://fireworks.ai/billing)
    2. Pay any outstanding invoices
    3. Your account reactivates automatically within an hour

    <Tip>
      Still suspended after resolving payment issues? Contact support via [Discord](https://discord.gg/fireworks-ai) or email [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).
    </Tip>
  </Accordion>
</AccordionGroup>


# Which model should I use?
Source: https://docs.fireworks.ai/guides/recommended-models

A list of recommended open models for common use cases

Users often ask us, which open models should I use? There's no single right answer! Here's a curated list based on **Fireworks internal testing**, **community feedback**, and **external benchmarks**. We recommend using it as a starting point, and we will update it regularly as new models emerge.

<Tip>
  Model sizes are marked as *Small*, *Medium*, or *Large*. For best quality, use large models or fine-tune medium/small models. For best speeds, use small models.
</Tip>

| **Category**            | **Use Case**                          | **Recommended Models**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Code & Development**  | **Code generation & reasoning**       | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) *(Medium)*<br />[Qwen3 Coder 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct) *(Small)*                                                                                                                                                  |
|                         | **Code completion & bug fixing**      | [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) *(Medium)*<br />[Qwen3 Coder 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct), [Qwen3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(Small)*                                                                                                                                                                         |
| **AI Applications**     | **AI Agents with tool use**           | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[Qwen 3 Family Models](https://app.fireworks.ai/models?filter=Provider\&provider=Qwen) *(Large/Medium/Small)*                                                                                                                                                                        |
|                         | **General reasoning & planning**      | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [Qwen3 235B Thinking 2507](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-thinking-2507), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b), [Qwen2.5-72B-Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-72b-instruct), [Llama 3.3 70B](https://app.fireworks.ai/models/fireworks/llama-v3p3-70b-instruct) *(Medium)* |
|                         | **Long context & summarization**      | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905) *(Large)*<br />[GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(Medium)*                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                         | **Fast semantic search & extraction** | [GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(Medium)*<br />[Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [Llama 3.1 8B](https://app.fireworks.ai/models/fireworks/llama-v3p1-8b-instruct), [Llama 3.2 3B](https://app.fireworks.ai/models/fireworks/llama-v3p2-3b-instruct), [Llama 3.2 1B](https://app.fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) *(Small)*                                                                                                                                                                                     |
| **Vision & Multimodal** | **Vision & document understanding**   | [Qwen3 VL 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-vl-235b-a22b), [Qwen2.5-VL 72B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-72b-instruct), [Qwen2.5-VL 32B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-32b-instruct) *(Medium)*<br />[Qwen3 VL 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-vl-30b-a3b), [Qwen2.5-VL 3-7B](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-7b-instruct) *(Small)*                                                                                                                              |

<Tip>
  You can explore all models in the [Fireworks Model Library](https://app.fireworks.ai/models)
</Tip>

*Last updated: Oct 25, 2025*


# Responses API
Source: https://docs.fireworks.ai/guides/response-api



Fireworks.ai offers a powerful Responses API that allows for more complex and stateful interactions with models. This guide will walk you through the key features and how to use them.

<Warning title="Data Retention Policy">
  The Responses API has a different data retention policy than the chat completions endpoint. See [Data Privacy & security](/guides/security_compliance/data_handling#response-api-data-retention).
</Warning>

## Overview

The Responses API is designed for building conversational applications and complex workflows. It allows you to:

* **Continue conversations**: Maintain context across multiple turns without resending the entire history.
* **Use external tools**: Integrate with external services and data sources through the Model Context Protocol (MCP).
* **Stream responses**: Receive results as they are generated, enabling real-time applications.
* **Control tool usage**: Set limits on tool calls with `max_tool_calls` parameter.
* **Manage data retention**: Choose whether to store conversations (default) or opt-out with `store=false`.

## Basic Usage

You can interact with the Response API using the Fireworks Python SDK or by making direct HTTP requests.

### Creating a Response

To start a new conversation, you use the `client.responses.create` method. For a complete example, see the [getting started notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb).

<CodeGroup>
  ```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  response = llm.responses.create(
      input="What is reward-kit and what are its 2 main features? Keep it short Please analyze the fw-ai-external/reward-kit repository.",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(response.output[-1].content[0].text.split("</think>")[-1])
  ```

  ```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="What is reward-kit and what are its 2 main features? Keep it short Please analyze the fw-ai-external/reward-kit repository.",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(response.output[-1].content[0].text.split("</think>")[-1])
  ```
</CodeGroup>

### Continuing a Conversation with `previous_response_id`

To continue a conversation, you can use the `previous_response_id` parameter. This tells the API to use the context from a previous response, so you don't have to send the entire conversation history again. For a complete example, see the [previous response ID notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb).

<CodeGroup>
  ```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  # First, create an initial response
  initial_response = llm.responses.create(
      input="What are the key features of reward-kit?",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )
  initial_response_id = initial_response.id

  # Now, continue the conversation
  continuation_response = llm.responses.create(
      input="How do I install it?",
      previous_response_id=initial_response_id,
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(continuation_response.output[-1].content[0].text.split("</think>")[-1])
  ```

  ```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  # First, create an initial response
  initial_response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="What are the key features of reward-kit?",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )
  initial_response_id = initial_response.id

  # Now, continue the conversation
  continuation_response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="How do I install it?",
      previous_response_id=initial_response_id,
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(continuation_response.output[-1].content[0].text.split("</think>")[-1])
  ```
</CodeGroup>

## Streaming Responses

For real-time applications, you can stream the response as it's being generated. For a complete example, see the [streaming example notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb).

<CodeGroup>
  ```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  stream = llm.responses.create(
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      stream=True,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  for chunk in stream:
      print(chunk)
  ```

  ```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  stream = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      stream=True,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  for chunk in stream:
      print(chunk)
  ```
</CodeGroup>

## Cookbook Examples

For more in-depth examples, check out the following notebooks:

* [General MCP Examples](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb)
* [Using `previous_response_id`](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb)
* [Streaming Responses](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb)
* [Using `store=False`](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb)
* [MCP with Streaming](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_with_streaming.ipynb)

## Storing Responses

By default, responses are stored and can be referenced by their ID. You can disable this by setting `store=False`. If you do this, you will not be able to use the `previous_response_id` to continue the conversation. For a complete example, see the [store=False notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb).

<CodeGroup>
  ```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  response = llm.responses.create(
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      store=False,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  # This will fail because the previous response was not stored
  try:
      continuation_response = llm.responses.create(
          input="Explain the second fact in more detail.",
          previous_response_id=response.id
      )
  except Exception as e:
      print(e)
  ```

  ```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      store=False,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  # This will fail because the previous response was not stored
  try:
      continuation_response = client.responses.create(
          model="accounts/fireworks/models/qwen3-235b-a22b",
          input="Explain the second fact in more detail.",
          previous_response_id=response.id
      )
  except Exception as e:
      print(e)
  ```
</CodeGroup>

## Deleting Stored Responses

When responses are stored (the default behavior with `store=True`), you can immediately delete them from storage using the DELETE endpoint. This permanently removes the conversation data.

<CodeGroup>
  ```python Python (Fireworks) theme={null}
  from fireworks import LLM
  import requests
  import os

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  # Create a response
  response = llm.responses.create(
      input="What is the capital of France?",
      store=True  # This is the default
  )

  response_id = response.id
  print(f"Created response with ID: {response_id}")

  # Delete the response immediately
  headers = {
      "Authorization": f"Bearer {os.getenv('FIREWORKS_API_KEY')}",
      "x-fireworks-account-id": "your-account-id"
  }
  delete_response = requests.delete(
      f"https://api.fireworks.ai/inference/v1/responses/{response_id}",
      headers=headers
  )

  if delete_response.status_code == 200:
      print("Response deleted successfully")
  else:
      print(f"Failed to delete response: {delete_response.status_code}")
  ```

  ```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI
  import requests

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  # Create a response
  response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="What is the capital of France?",
      store=True  # This is the default
  )

  response_id = response.id
  print(f"Created response with ID: {response_id}")

  # Delete the response immediately
  headers = {
      "Authorization": f"Bearer {os.getenv('FIREWORKS_API_KEY')}",
      "x-fireworks-account-id": "your-account-id"
  }
  delete_response = requests.delete(
      f"https://api.fireworks.ai/inference/v1/responses/{response_id}",
      headers=headers
  )

  if delete_response.status_code == 200:
      print("Response deleted successfully")
  else:
      print(f"Failed to delete response: {delete_response.status_code}")
  ```

  ```bash cURL theme={null}
  # First create a response and capture the ID
  RESPONSE=$(curl -X POST https://api.fireworks.ai/inference/v1/responses \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "accounts/fireworks/models/qwen3-235b-a22b",
      "input": "What is the capital of France?",
      "store": true
    }')

  # Extract the response ID (using jq or similar JSON parser)
  RESPONSE_ID=$(echo $RESPONSE | jq -r '.id')

  # Delete the response
  curl -X DELETE "https://api.fireworks.ai/inference/v1/responses/$RESPONSE_ID" \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "x-fireworks-account-id: your-account-id"
  ```
</CodeGroup>

<Warning>
  Once a response is deleted, it cannot be recovered.
</Warning>

## Response Structure

All response objects include the following fields:

* `id`: Unique identifier for the response (e.g., `resp_abc123...`)
* `created_at`: Unix timestamp when the response was created
* `status`: Status of the response (typically `"completed"`)
* `model`: The model used to generate the response
* `output`: Array of message objects, tool calls, and tool outputs
* `usage`: Token usage information:
  * `prompt_tokens`: Number of tokens in the prompt
  * `completion_tokens`: Number of tokens in the completion
  * `total_tokens`: Total tokens used
* `previous_response_id`: ID of the previous response in the conversation (if any)
* `store`: Whether the response was stored (boolean)
* `max_tool_calls`: Maximum number of tool calls allowed (if set)

### Example Response

```json  theme={null}
{
  "id": "resp_abc123...",
  "created_at": 1735000000,
  "status": "completed",
  "model": "accounts/fireworks/models/qwen3-235b-a22b",
  "output": [
    {
      "id": "msg_xyz789...",
      "role": "user",
      "content": [{"type": "input_text", "text": "What is 2+2?"}],
      "status": "completed"
    },
    {
      "id": "msg_def456...",
      "role": "assistant",
      "content": [{"type": "output_text", "text": "2 + 2 equals 4."}],
      "status": "completed"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 8,
    "total_tokens": 23
  },
  "previous_response_id": null,
  "store": true,
  "max_tool_calls": null
}
```


# Audit & Access Logs
Source: https://docs.fireworks.ai/guides/security_compliance/audit_logs

Monitor and track account activities with audit logging for Enterprise accounts

Audit logs are available for Enterprise accounts. This feature enhances security visibility, incident investigation, and compliance reporting.

Audit logs include data access logs. All read, write, and delete operations on storage are logged, normalized, and enriched with account context for complete visibility.

## View audit logs

You can view audit logs, including data access logs, using the Fireworks CLI:

```bash  theme={null}
firectl ls audit-logs
```

<Frame caption="Audit logs showing data access activities with timestamps, principals, and resource paths">
  <img src="https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=5aaa79c36dbd45b72c0ed6da84d3f1c1" alt="Audit logs table showing data access activities with columns for timestamp, principal, response code, resource path, and message" data-og-width="2110" width="2110" data-og-height="258" height="258" data-path="images/audit-logs-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?w=280&fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=18af189a09152586b09b6382971d43e0 280w, https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?w=560&fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=77c913fcd6a6adce3f4607679ca7317e 560w, https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?w=840&fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=945986ab1108cd2eca5ec6bb9fa4d383 840w, https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?w=1100&fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=942a772dc0e7a4692707235afc50d97d 1100w, https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?w=1650&fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=c80a83bad6f3ab4882f7ed945237ef70 1650w, https://mintcdn.com/fireworksai/2J3dYvs4OJ-_-alw/images/audit-logs-example.png?w=2500&fit=max&auto=format&n=2J3dYvs4OJ-_-alw&q=85&s=9c47f023f9dced9345b3ec6c41cca053 2500w" />
</Frame>


# Zero Data Retention
Source: https://docs.fireworks.ai/guides/security_compliance/data_handling

Data retention policies at Fireworks

## Zero data retention

Fireworks has Zero Data Retention by default. Specifically, this means

* Fireworks does not log or store prompt or generation data for any open models, without explicit user opt-in.
  * More technically: prompt and generation data exist only in volatile memory for the duration of the request. If [prompt caching](https://docs.fireworks.ai/guides/prompt-caching#data-privacy) is active, some prompt data (and associated KV caches) can be stored in volatile memory for several minutes. In either case, prompt and generation data are not logged into any persistent storage.
* Fireworks logs metadata (e.g. number of tokens in a request) as required to deliver the service.
* Users can explicitly opt-in to log prompt and generation data for certain advanced features (e.g. FireOptimizer).
* For proprietary Fireworks models (e.g. f1, FireFunction), prompt and generation data may be logged to enable bulk analytics to improve the model.
  * In this case, the model description will contain an explicit message about logging.

## Response API data retention

For the Response API specifically, Fireworks retains conversation data with the following policy when the API request has `store=True` (the default):

* **What is stored**: Conversation messages include the complete conversation data:
  * User prompts
  * Model responses
  * Tools called by the model
* **Opt-out option**: You can disable data storage by setting `store=False` in your API requests to prevent any conversation data from being retained.
* **Retention period**: All stored conversation data is automatically deleted after 30 days.
* **Immediate deletion**: You can immediately delete stored conversation data using the DELETE API endpoint by providing the `response_id`. This will permanently remove the record.

This retention policy is designed to be consistent with the OpenAI API while providing users control over their data storage preferences.

<Note>
  The Response API retention policy only applies to conversation data when using the Response API endpoints. All other Fireworks services follow the zero data retention policy described above.
</Note>


# Data Security
Source: https://docs.fireworks.ai/guides/security_compliance/data_security

How we secure and handle your data for inference and training

At Fireworks, protecting customer data is at the core of our platform. We design all of our systems, infrastructure, and business processes to ensure customer trust through verifiable security & compliance.

This page provides an overview of our key security measures. For documentation and audit reports, see our [Trust Center](https://trust.fireworks.ai/).

## Zero Data Retention

Fireworks does not log or store prompt or generation data for open models, without explicit user opt-in. See our [Zero Data Retention Policy](https://docs.fireworks.ai/guides/security_compliance/data_handling).

## Secure Data Handling

**Data Ownership & Control:** Customers maintain ownership of their data. Customer data stored as part of an active workflow can be permanently deleted with auditable confirmation, and secure wipe processes ensure deleted assets cannot be reconstructed.

**Encryption**: Data is encrypted in transit (TLS 1.2+) and at rest (AES-256).

**Bring Your Own Bucket:** Customers may integrate their own cloud storage to retain governance and apply their own compliance frameworks.

* Datasets: [GCS Bucket Integration](/fine-tuning/secure-fine-tuning#gcs-bucket-integration) (AWS S3 coming soon)
* Models: [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model)
* (Coming soon) Encryption Keys: Customers may choose to use their own encryption keys and policies for end-to-end control.

**Access Logging:** All customer data access is logged, monitored, and protected against tampering. See [Audit & Access Logs](https://docs.fireworks.ai/guides/security_compliance/audit_logs).

## Workload Isolation

Dedicated workloads run in logically isolated environments, preventing cross-customer access or data leakage.

## Secure Training

Fireworks enables secure model training, including fine-tuning and reinforcement learning, while maintaining customer control over sensitive components and data. This approach builds on our [Zero Data Retention](#zero-data-retention) policy to ensure sensitive training data never persists on our platform.

**Customer-Controlled Architecture:** For advanced training workflows like reinforcement learning, critical components remain under customer control:

* Reward models and reward functions are kept proprietary and not shared
* Rollout servers and training metrics are built and managed by customers
* Model checkpoints are managed through secure cloud storage registries

**Minimal Data Sharing:** Training data is shared via controlled bucket access with minimal sharing and step-wise retention, limiting data exposure while enabling effective training workflows.

**API-Based Integration:** Customers leverage Fireworks' training APIs while maintaining full control over sensitive components, ensuring no cross-component data leakage.

<Tip>
  For detailed guidance on secure reinforcement fine-tuning and using your own cloud storage, see [Secure Fine Tuning](/fine-tuning/secure-fine-tuning).
</Tip>

## Technical Safeguards

* **Device Trust**: Only approved, secured devices with strong authentication can access sensitive Fireworks systems.
* **Identity & Access Management**: Fine-grained access controls are enforced across all Fireworks environments, following the principle of least privilege.
* **Network Security**
  * Private network isolation for customer workloads.
  * Firewalls and security groups prevent unauthorized inbound/outbound traffic.
  * DDoS protection is in place across core services.
* **Monitoring & Detection**: Real-time monitoring and anomaly detection systems alert on suspicious activity
* **Vulnerability Management**: Continuous scanning and patching processes keep infrastructure up to date against known threats.

## Operational Security

* **Security Reviews & Testing**: Regular penetration testing validates controls.
* **Incident Response**: A formal incident response plan ensures swift containment, customer notification, and remediation if an issue arises.
* **Employee Access**: Only a minimal subset of Fireworks personnel have access to production systems, and all access is logged and periodically reviewed.
* **Third-Party Risk Management**: Vendors and subprocessors undergo rigorous due diligence and contractual security obligations.

## Compliance & Certifications

Fireworks aligns with leading industry standards to support customer compliance obligations:

* **SOC 2 Type II** (certified)
* **ISO 27001 / ISO 27701 / ISO 42001** (in progress)
* **HIPAA Support**: Firework is HIPAA compliant and supports healthcare and life sciences organizations in leveraging our rapid inference capabilities with confidence.
* **Regulatory Alignment**: Controls are mapped to GDPR, CCPA, and other international data protection frameworks

<Note>
  Documentation and audit reports are available in our [Trust Center](https://trust.fireworks.ai/).
</Note>


# Quantization
Source: https://docs.fireworks.ai/models/quantization

Reduce model precision to improve performance and lower costs

Quantization reduces the number of bits used to serve a model, improving performance and reducing cost by 30-50%. However, this can change model numerics which may introduce small changes to the output.

<Tip>
  Read our [blog post](https://fireworks.ai/blog/fireworks-quantization) for a detailed treatment of how quantization affects model quality.
</Tip>

## Checking available precisions

Models may support different numerical precisions like FP16, FP8, BF16, or INT8, which affect memory usage and inference speed.

**Check default precision:**

```bash  theme={null}
firectl get model accounts/fireworks/models/llama-v3p1-8b-instruct | grep "Default Precision"
```

**Check supported precisions:**

```bash  theme={null}
firectl get model accounts/fireworks/models/llama-v3p1-8b-instruct | grep -E "(Supported Precisions|Supported Precisions With Calibration)"
```

The `Precisions` field indicates what precisions the model has been prepared for.

## Quantizing a model

A model can be quantized to 8-bit floating-point (FP8) precision.

<Tabs>
  <Tab title="firectl">
    ```bash  theme={null}
    firectl prepare-model <MODEL_ID>
    ```
  </Tab>

  <Tab title="Python (REST API)">
    ```python  theme={null}
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to prepare

    response = requests.post(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}:prepare",
      headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
      },
      json={
        "precision": "FP8"
      }
    )

    print(response.json())
    ```
  </Tab>
</Tabs>

<Note>This is an additive process that enables creating deployments with additional precisions. The original FP16 checkpoint is still available for use.</Note>

You can check on the status of preparation by running:

<Tabs>
  <Tab title="firectl">
    ```bash  theme={null}
    firectl get model <MODEL_ID>
    ```
  </Tab>

  <Tab title="Python (REST API)">
    ```python  theme={null}
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to get

    response = requests.get(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}",
      headers={
        "Authorization": f"Bearer {API_KEY}"
      }
    )

    print(response.json())
    ```
  </Tab>
</Tabs>

and checking if the state is still in `PREPARING`. A successfully prepared model will have the desired precision added
to the `Precisions` list.

## Creating an FP8 deployment

By default, creating a deployment uses the FP16 checkpoint. To use a quantized FP8 checkpoint, first ensure the model has been prepared for FP8 (see [Checking available precisions](#checking-available-precisions) above), then pass the `--precision` flag when creating your deployment:

<Tabs>
  <Tab title="firectl">
    ```bash  theme={null}
    firectl create deployment <MODEL> --accelerator-type NVIDIA_H100_80GB --precision FP8
    ```
  </Tab>

  <Tab title="Python (REST API)">
    ```python  theme={null}
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    # The ID of the model you want to deploy.
    # The model must be prepared for FP8 precision.
    MODEL_ID = "<YOUR_MODEL_ID>"
    DEPLOYMENT_NAME = "My FP8 Deployment"

    response = requests.post(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/deployments",
      headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
      },
      json={
        "displayName": DEPLOYMENT_NAME,
        "baseModel": MODEL_ID,
        "acceleratorType": "NVIDIA_H100_80GB",
        "precision": "FP8",
      }
    )

    print(response.json())
    ```
  </Tab>
</Tabs>

<Note>Quantized deployments can only be served using H100 GPUs.</Note>


# Custom Models
Source: https://docs.fireworks.ai/models/uploading-custom-models

Upload, verify, and deploy your own models from Hugging Face or elsewhere

Upload your own models from Hugging Face or elsewhere to deploy fine-tuned or custom-trained models optimized for your use case.

* **Multiple upload options** – Upload from local files or directly from S3 buckets
* **Secure uploads** – All uploads are encrypted and models remain private to your account by default

## Requirements

### Supported architectures

Fireworks supports most popular model architectures, including:

* [DeepSeek V1, V2 & V3](https://huggingface.co/deepseek-ai)
* [Qwen, Qwen2, Qwen2.5, Qwen2.5-VL, Qwen3](https://huggingface.co/Qwen)
* [Kimi K2 family](https://huggingface.co/moonshotai)
* [GLM 4.X family](https://huggingface.co/zai-org)
* [Llama 1, 2, 3, 3.1, 4](https://huggingface.co/docs/transformers/en/model_doc/llama2)
* [Mistral & Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mistral)
* [Gemma](https://huggingface.co/docs/transformers/en/model_doc/gemma)
* [GPT-OSS 120B and 20B](https://huggingface.co/openai/gpt-oss-120b)

<Accordion title="View all supported architectures">
  - [DBRX](https://huggingface.co/docs/transformers/en/model_doc/dbrx)
  - [DeepSeek V1, V2 & V3](https://huggingface.co/deepseek-ai)
  - [Falcon](https://huggingface.co/docs/transformers/en/model_doc/falcon)
  - [Gemma](https://huggingface.co/docs/transformers/en/model_doc/gemma)
  - [GPT NeoX](https://huggingface.co/docs/transformers/en/model_doc/gpt_neox)
  - [Idefics3](https://huggingface.co/docs/transformers/en/model_doc/idefics3)
  - [Llama 1, 2, 3, 3.1, 4](https://huggingface.co/docs/transformers/en/model_doc/llama2)
  - [LLaVA](https://huggingface.co/docs/transformers/main/en/model_doc/llava)
  - [Mistral](https://huggingface.co/docs/transformers/en/model_doc/mistral) & [Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mixtral)
  - [Phi, Phi-3, Phi-3V, Phi-4](https://huggingface.co/docs/transformers/en/model_doc/phi)
  - [Pythia](https://huggingface.co/docs/transformers/en/model_doc/gpt_neox)
  - [Qwen](https://huggingface.co/docs/transformers/en/model_doc/qwen), [Qwen2](https://huggingface.co/docs/transformers/en/model_doc/qwen2), [Qwen2.5](https://huggingface.co/collections/Qwen/qwen25-66e81a666513e518adb90d9e), [Qwen2.5-VL](https://huggingface.co/collections/Qwen/qwen25-vl-6795ffac22b334a837c0f9a5), [Qwen3](https://huggingface.co/Qwen)
  - [Solar](https://huggingface.co/upstage/SOLAR-10.7B-v1.0)
  - [StableLM](https://huggingface.co/docs/transformers/main/en/model_doc/stablelm)
  - [Starcoder (GPTBigCode)](https://huggingface.co/docs/transformers/en/model_doc/gpt_bigcode) & [Starcoder2](https://huggingface.co/docs/transformers/main/en/model_doc/starcoder2)
  - [Vision Llama](https://huggingface.co/docs/transformers/en/model_doc/llama2)
</Accordion>

### Required files

You'll need standard Hugging Face model files: `config.json`, model weights (`.safetensors` or `.bin`), and tokenizer files.

<Accordion title="View detailed file requirements">
  The model files you will need to provide depend on the model architecture. In general, you will need:

  * **Model configuration**: `config.json`

    <Note>
      Fireworks does not support the `quantization_config` option in `config.json`.
    </Note>
  * **Model weights** in one of the following formats:
    * `*.safetensors`
    * `*.bin`
  * **Weights index**: `*.index.json`
  * **Tokenizer file(s)**, e.g.:
    * `tokenizer.model`
    * `tokenizer.json`
    * `tokenizer_config.json`

  If the requisite files are not present, model deployment may fail.

  **Enabling chat completions**: To enable the chat completions API for your custom base model, ensure your `tokenizer_config.json` contains a `chat_template` field. See the Hugging Face guide on [Templates for Chat Models](https://huggingface.co/docs/transformers/main/en/chat_templating) for details.
</Accordion>

## Uploading your model

<Tabs>
  <Tab title="Local files (CLI)">
    Upload from your local machine:

    ```bash  theme={null}
    firectl create model <MODEL_ID> /path/to/files/
    ```
  </Tab>

  <Tab title="S3 bucket (CLI)">
    For larger models, upload directly from an Amazon S3 bucket for faster transfer:

    ```bash  theme={null}
    firectl create model <MODEL_ID> s3://<BUCKET_NAME>/<PATH_TO_MODEL>/ \
      --aws-access-key-id <ACCESS_KEY_ID> \
      --aws-secret-access-key <SECRET_ACCESS_KEY>
    ```

    See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) for how to generate an access key ID and secret access key pair.

    <Note>
      Ensure the IAM user has read access to the S3 bucket containing the model.
    </Note>
  </Tab>

  <Tab title="REST API">
    For programmatic uploads (automation, CI/CD pipelines), use the Fireworks REST API with a 4-step process: create model → get upload URLs → upload files → validate.

    See the [REST API upload guide](/models/uploading-custom-models-api) for a complete Python example.
  </Tab>
</Tabs>

## Verifying your upload

After uploading, verify your model is ready to deploy:

```bash  theme={null}
firectl get model accounts/<ACCOUNT_ID>/models/<MODEL_NAME>
```

Look for `State: READY` in the output. Once ready, you can create a deployment.

## Deploying your model

Once your model shows `State: READY`, create a deployment:

```bash  theme={null}
firectl create deployment accounts/<ACCOUNT_ID>/models/<MODEL_NAME> --wait
```

See the [On-demand deployments guide](/guides/ondemand-deployments) for configuration options like GPU types, autoscaling, and quantization.

## Publishing your model

By default, models are private to your account. Publish a model to make it available to other Fireworks users.

**When published:**

* Listed in the public model catalog
* Deployable by anyone with a Fireworks account
* Still hosted and controlled by your account

**Publish a model:**

```bash  theme={null}
firectl update model <MODEL_ID> --public
```

**Unpublish a model:**

```bash  theme={null}
firectl update model <MODEL_ID> --public=false
```

## Importing fine-tuned models

In addition to models you fine-tune on the Fireworks platform, you can also upload your own custom fine-tuned models as LoRA adapters.

### Requirements

Your custom LoRA addon must contain the following files:

* `adapter_config.json` - The Hugging Face adapter configuration file
* `adapter_model.bin` or `adapter_model.safetensors` - The saved addon file

The `adapter_config.json` must contain the following fields:

* `r` - The number of LoRA ranks. Must be an integer between 4 and 64, inclusive
* `target_modules` - A list of target modules. Currently the following target modules are supported:
  * `q_proj`
  * `k_proj`
  * `v_proj`
  * `o_proj`
  * `up_proj` or `w1`
  * `down_proj` or `w2`
  * `gate_proj` or `w3`
  * `block_sparse_moe.gate`

Additional fields may be specified but are ignored.

### Enabling chat completions

To enable the chat completions API for your LoRA addon, add a `fireworks.json` file to the directory containing:

```json  theme={null}
{
  "conversation_config": {
    "style": "jinja",
    "args": {
      "template": "<YOUR_JINJA_TEMPLATE>"
    }
  }
}
```

### Uploading the LoRA adapter

To upload a LoRA addon, run the following command. The MODEL\_ID is an arbitrary [resource ID](/getting-started/concepts#resource-names-and-ids) to refer to the model within Fireworks.

<Note>
  Only some base models support LoRA addons.
</Note>

```bash  theme={null}
firectl create model <MODEL_ID> /path/to/files/ --base-model "accounts/fireworks/models/<BASE_MODEL_ID>"
```

## Next steps

<CardGroup cols={3}>
  <Card title="Deploy your model" icon="rocket" href="/guides/ondemand-deployments">
    Configure GPU types, autoscaling, and optimization
  </Card>

  <Card title="Quantization" icon="compress" href="/models/quantization">
    Reduce serving costs with model quantization
  </Card>

  <Card title="Fine-tuning" icon="wand-magic-sparkles" href="/fine-tuning/finetuning-intro">
    Fine-tune models before deploying them
  </Card>
</CardGroup>


# Structured Outputs
Source: https://docs.fireworks.ai/structured-responses/structured-response-formatting

Enforce output formats using JSON schemas or custom grammars

Structured outputs ensure model responses conform to your specified format, making them easy to parse and integrate into your application. Fireworks supports two methods: **JSON mode** (using JSON schemas) and **Grammar mode** (using custom BNF grammars).

<Info>
  New to structured outputs? Check out the [Serverless Quickstart](/getting-started/quickstart#structured-outputs) for a quick introduction.
</Info>

## Quick Start

Force model output to conform to a [JSON schema](https://json-schema.org/):

```python  theme={null}
import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

# Define your schema
class Result(BaseModel):
    winner: str

# Make the request
response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "Result",
            "schema": Result.model_json_schema()
        }
    },
    messages=[{
        "role": "user",
        "content": "Who won the US presidential election in 2012? Reply in JSON format."
    }]
)

print(response.choices[0].message.content)
# Output: {"winner": "Barack Obama"}
```

<Tip>
  Include the schema in **both** your prompt and the `response_format` for best results. The model doesn't automatically "see" the schema—it's enforced during generation.
</Tip>

## Response Format Options

Fireworks supports two JSON mode variants:

* **`json_object`** – Force any valid JSON output (no specific schema)
* **`json_schema`** – Enforce a specific JSON schema (recommended)

<Warning>
  Always instruct the model to produce JSON in your prompt. Without this, the model may generate whitespace indefinitely until hitting token limits.
</Warning>

<AccordionGroup>
  <Accordion title="Using arbitrary JSON mode">
    To force JSON output without a specific schema:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        response_format={"type": "json_object"},
        messages=[{
            "role": "user",
            "content": "List the top 3 programming languages in JSON format."
        }]
    )
    ```

    This is similar to [OpenAI's JSON mode](https://platform.openai.com/docs/guides/text-generation/json-mode).
  </Accordion>

  <Accordion title="Important notes and limitations">
    **Token limits:** If `finish_reason="length"`, the response may be truncated and invalid JSON. Increase `max_tokens` if needed.

    **Completions API:** JSON mode works with both Chat Completions and Completions APIs.

    **Function calling:** When using [Tool Calling](/guides/function-calling), JSON mode is enabled automatically—these guidelines don't apply.
  </Accordion>
</AccordionGroup>

## JSON Schema Support

Fireworks supports most [JSON schema specification](https://json-schema.org/specification) constructs:

**Supported:**

* Types: `string`, `number`, `integer`, `boolean`, `object`, `array`, `null`
* Object constraints: `properties`, `required`
* Array constraints: `items`
* Nested schemas: `anyOf`, `$ref`

**Not yet supported:**

* `oneOf` composition
* Length/size constraints (`minLength`, `maxLength`, `minItems`, `maxItems`)
* Regular expressions (`pattern`)

<Tip>
  Fireworks automatically prevents hallucinated fields by treating schemas with `properties` as if `"unevaluatedProperties": false` is set.
</Tip>

<Accordion title="Advanced: Reasoning Model JSON Mode">
  Some models support generating structured JSON outputs with visible reasoning. In this mode, the model's response includes a `<think>...</think>` section showing its reasoning process, followed by the JSON output.

  #### Example Usage

  ```python  theme={null}
  import os
  import re
  from openai import OpenAI
  from pydantic import BaseModel

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  # Define the output schema
  class QAResult(BaseModel):
      question: str
      answer: str

  # Make the request
  response = client.chat.completions.create(
      model="accounts/fireworks/models/deepseek-v3p1",
      messages=[{"role": "user", "content": "Who wrote 'Pride and Prejudice'?"}],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "QAResult",
              "schema": QAResult.model_json_schema()
          }
      },
      max_tokens=1000
  )

  # Extract the response content
  response_content = response.choices[0].message.content

  # Extract reasoning (if present)
  reasoning_match = re.search(r"<think>(.*?)</think>", response_content, re.DOTALL)
  reasoning = reasoning_match.group(1).strip() if reasoning_match else None

  # Extract JSON
  json_match = re.search(r"</think>\s*(\{.*\})", response_content, re.DOTALL) if reasoning else re.search(r"(\{.*\})", response_content, re.DOTALL)
  json_str = json_match.group(1).strip() if json_match else "{}"

  # Parse into Pydantic model
  qa_result = QAResult.model_validate_json(json_str)

  if reasoning:
      print("Reasoning:", reasoning)
  print("Result:", qa_result.model_dump_json(indent=2))
  ```

  #### Use Cases

  Reasoning mode is useful for:

  * **Debugging**: Understanding why the model generated specific outputs
  * **Auditing**: Documenting the decision-making process
  * **Complex tasks**: Scenarios where the reasoning is as valuable as the final answer

  #### Additional Examples

  <CardGroup cols={2}>
    <Card title="Computer Specs with Reasoning" icon="square-1" href="https://colab.research.google.com/drive/1zBK1nDITDNOx7oRWxh19C5_sNSh64PKM?usp=sharing">
      Generate structured PC specifications with reasoning
    </Card>

    <Card title="Healthcare Records with Reasoning" icon="square-2" href="https://colab.research.google.com/drive/1njzOgHWgguSuA732RYROJDiCua3hGO_R?usp=sharing">
      Structure patient records with AI-generated reasoning
    </Card>
  </CardGroup>
</Accordion>

## Grammar Mode

For advanced use cases where JSON isn't sufficient, use [Grammar mode](/structured-responses/structured-output-grammar-based) to constrain outputs using custom BNF grammars. Grammar mode is ideal for:

* **Classification tasks** – Limit output to a predefined list of options
* **Language-specific output** – Force output in specific languages or character sets
* **Custom formats** – Define arbitrary output structures beyond JSON

[Learn more about Grammar mode →](/structured-responses/structured-output-grammar-based)

## Related features

Check out [Tool Calling](/guides/function-calling) for multi-turn capabilities and routing across multiple schemas.


# Authentication
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/authentication

Authentication for access to your account

### Signing in

Users using Google SSO can run:

```
firectl signin
```

If you are using [custom SSO](/accounts/sso), also specify the account ID:

```
firectl signin my-enterprise-account
```

### Authenticate with API Key

To authenticate with an API key, append `--api-key` to any firectl command.

```
firectl --api-key API_KEY <command>
```

To persist the API key for all subsequent commands, run:

```
firectl set-api-key API_KEY
```


# firectl create api-key
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-api-key

Creates an API key for the signed in user or a specified service account user.

```
firectl create api-key [flags]
```

### Examples

```
firectl create api-key
firectl create api-key --service-account=my-service-account
firectl create api-key --key-name="Production Key" --service-account=ci-bot
firectl create api-key --key-name="Temporary Key" --expire-time="2025-12-31 23:59:59"
```

### Flags

```
      --expire-time string       If specified, the time at which the API key will automatically expire. Specified in YYYY-MM-DD[ HH:MM:SS] format.
  -h, --help                     help for api-key
      --key-name string          The name of the key to be created. Defaults to "default"
      --service-account string   Admin only: Create API key for the specified service account user
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create batch-inference-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-batch-inference-job

Creates a batch inference job.

```
firectl create batch-inference-job [flags]
```

### Examples

```
firectl create batch-inference-job --input-dataset-id my-dataset --output-dataset-id my-output-dataset --model my-model \
			--job-id my-job --max-tokens 1024 --temperature 0.7 --top-p 0.9 --top-k 50 --n 2 --precision FP16 \
			--extra-body '{"stop": ["\n"], "presence_penalty": 0.5}'
```

### Flags

```
      --job-id string              The ID of the batch inference job. If not set, it will be autogenerated.
      --display-name string        The display name of the batch inference job.
  -m, --model string               The model to use for inference.
  -d, --input-dataset-id string    The input dataset ID.
  -x, --output-dataset-id string   The output dataset ID. If not provided, a default one will be generated.
      --continue-from string       Continue from an existing batch inference job (by job ID or resource name).
      --max-tokens int32           Maximum number of tokens to generate per response.
      --temperature float32        Sampling temperature (typically between 0 and 2).
      --top-p float32              Top-p sampling parameter (typically between 0 and 1).
      --top-k int32                Top-k sampling parameter, limits the token selection to the top k tokens.
      --n int32                    Number of response candidates to generate per input.
      --extra-body string          Additional inference parameters as a JSON string (e.g., '{"stop": ["\n"]}').
      --precision string           The precision with which the model should be served. If not specified, a suitable default will be chosen based on the model.
      --quiet                      If set, only errors will be printed.
  -h, --help                       help for batch-inference-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create dataset
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset

Creates and uploads a dataset.

```
firectl create dataset [flags]
```

### Examples

```
firectl create dataset my-dataset /path/to/dataset.jsonl
firectl create dataset --trace-from-model-id model_abc --format chat --date 2024-01-10 my-dataset
firectl create dataset my-dataset --external-url gs://bucket-name/object-name
```

### Flags

```
      --display-name string    The display name of the dataset.
      --end-time string        The end time for which to trace data (format: YYYY-MM-DD). Only specify for traced dataset.
      --eval-protocol-output   If true, the dataset is in eval protocol output format.
      --external-url string    The GCS URI that points to the dataset file.
      --filter string          Filter condition to apply to the source dataset.
  -h, --help                   help for dataset
      --quiet                  If true, does not print the upload progress bar.
      --source string          Source dataset ID to filter from.
      --start-time string      The start time for which to trace data (format: YYYY-MM-DD). Only specify for traced dataset.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create deployment
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-deployment

Creates a new deployment.

```
firectl create deployment [flags]
```

### Examples

```
firectl create deployment falcon-7b
firectl create deployment accounts/fireworks/models/falcon-7b
firectl create deployment falcon-7b --file=/path/to/deployment-config.json
firectl create deployment falcon-7b --deployment-shape=falcon-7b-shape
```

### Flags

```
      --accelerator-count int32             The number of accelerators to use per replica.
      --accelerator-type string             The type of accelerator to use. Must be one of {NVIDIA_A100_80GB, NVIDIA_H100_80GB, NVIDIA_H200_141GB, AMD_MI300X_192GB}
  -c, --cluster-id string                   The Fireworks cluster ID. If not specified, reads cluster_id from ~/.fireworks/settings.ini.
      --deployment-id string                The ID of the deployment. If not specified, a random ID will be generated.
      --deployment-shape string             The deployment shape to use for this deployment.
      --deployment-template string          The deployment template to use.
      --description string                  Description of the deployment.
      --direct-route-api-keys stringArray   The API keys for the direct route. Only available to enterprise accounts.
      --direct-route-type string            If set, this deployment will expose an endpoint that bypasses our API gateway. Must be one of {INTERNET, GCP_PRIVATE_SERVICE_CONNECT, AWS_PRIVATELINK}. Only available to enterprise accounts.
      --disable-speculative-decoding        If true, speculative decoding is disabled.
      --display-name string                 Human-readable name of the deployment. Must be fewer than 64 characters long.
      --draft-model string                  The draft model to use for speculative decoding. If the model is under your account, you can specify the model ID. If the model is under another account, you can specify the full resource name (e.g. accounts/other-account/models/falcon-7b).
      --draft-token-count int32             The number of tokens to generate per step for speculative decoding.
      --enable-addons                       If true, enable addons for this deployment.
      --enable-mtp                          If true, enable multi-token prediction for this deployment.
      --enable-session-affinity             If true, does sticky routing based on the 'user' field. Only available to enterprise accounts.
      --expire-time string                  If specified, the time at which the deployment will automatically be deleted. Specified in YYYY-MM-DD[ HH:MM:SS] format.
      --file string                         Path to a JSON configuration file containing deployment settings.
  -h, --help                                help for deployment
      --load-targets Map                    Map of autoscaling load metric names to their target utilization factors. Only available to enterprise accounts.
      --long-prompt                         Whether this deployment is optimized for long prompts.
      --max-context-length int32            The maximum context length supported by the model (context window). If not specified, the model's default maximum context length will be used.
      --max-replica-count int32             Maximum number of replicas for the deployment. If min-replica-count > 0 defaults to 0, otherwise defaults to 1.
      --min-replica-count int32             Minimum number of replicas for the deployment. If min-replica-count < max-replica-count the deployment will automatically scale between the two replica counts based on load.
      --multi-region string                 The multi-region where the deployment must be placed.
      --ngram-speculation-length int32      The length of previous input sequence to be considered for N-gram speculation.
      --precision string                    The precision with which the model is served. If specified, must be one of {FP8, FP16, FP8_MM, FP8_AR, FP8_MM_KV_ATTN, FP8_KV, FP8_MM_V2, FP8_V2, FP8_MM_KV_ATTN_V2, FP4, BF16, FP4_BLOCKSCALED_MM, FP4_MX_MOE}.
      --region string                       The region where the deployment must be placed.
      --scale-down-window duration          The duration the autoscaler will wait before scaling down a deployment after observing decreased load. Default is 10m.
      --scale-to-zero-window duration       The duration after which there are no requests that the deployment will be scaled down to zero replicas, if min-replica-count is 0. Default 1h.
      --scale-up-window duration            The duration the autoscaler will wait before scaling up a deployment after observing increased load. Default is 30s.
      --validate-only                       If true, this will not create the deployment, but will return the deployment that would be created.
      --wait                                Wait until the deployment is ready.
      --wait-timeout duration               Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create dpo-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dpo-job

Creates a dpo job.

```
firectl create dpo-job [flags]
```

### Examples

```
firectl create dpoj \
	--base-model llama-v3-8b-instruct \
	--dataset sample-dataset \
	--output-model name-of-the-trained-model

# Create from source job:
firectl create dpoj \
	--source-job my-previous-job \
	--output-model new-model

```

### Flags

```
      --base-model string                   The base model for the dpo job. Only one of base-model or warm-start-from should be specified.
      --dataset string                      The dataset for the dpo job. (Required)
      --output-model string                 The output model for the dpo job.
      --job-id string                       The ID of the dpo job. If not set, it will be autogenerated.
      --warm-start-from string              The model to warm start from. If set, base-model must not be set.
      --source-job string                   The source dpo job to copy configuration from. If other flags are set, they will override the source job's configuration.
      --epochs int32                        The number of epochs for the dpo job.
      --learning-rate float32               The learning rate for the dpo job.
      --max-context-length int32            Maximum token length for sequences within each training batch. Shorter sequences are concatenated; longer sequences are truncated. (default 8192)
      --batch-size int32                    The maximum number of tokens packed into each training batch in the dpo job. (default 32768)
      --gradient-accumulation-steps int32   The number of gradient accumulation steps for the dpo job. (default 1)
      --learning-rate-warmup-steps int32    The number of learning rate warmup steps for the dpo job.
      --lora-rank int32                     The rank of the LoRA layers for the dpo job. (default 8)
      --accelerator-count int32             The number of accelerators to use for the dpo job.
                                             (default 1)
      --wandb-api-key string                [WANDB_API_KEY] WandB API Key. (Required if any WandB flag is set)
      --wandb-project string                [WANDB_PROJECT] WandB Project. (Required if any WandB flag is set)
      --wandb-entity string                 [WANDB_ENTITY] WandB Entity. (Required if any WandB flag is set)
      --wandb                               Enable WandB
                                            
      --display-name string                 The display name of the dpo job.
      --early-stop                          Enable early stopping for the dpo job.
      --quiet                               If set, only errors will be printed.
  -h, --help                                help for dpo-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create identity-provider
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-identity-provider

Creates a new identity provider.

```
firectl create identity-provider [flags]
```

### Examples

```
# Create SAML identity provider
firectl create identity-provider --display-name="Company SAML" \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata"

# Create OIDC identity provider
firectl create identity-provider --display-name="Company OIDC" \
  --oidc-issuer="https://auth.company.com" \
  --oidc-client-id="abc123" \
  --oidc-client-secret="secret456"

# Create OIDC identity provider with multiple domains
firectl create identity-provider --display-name="Example OIDC" \
  --oidc-issuer="https://accounts.google.com" \
  --oidc-client-id="client123" \
  --oidc-client-secret="secret456" \
  --tenant-domains="example.com,example.co.uk"
```

### Flags

```
      --display-name string         The display name of the identity provider (required)
  -h, --help                        help for identity-provider
      --oidc-client-id string       The OIDC client ID for OIDC providers
      --oidc-client-secret string   The OIDC client secret for OIDC providers
      --oidc-issuer string          The OIDC issuer URL for OIDC providers
      --saml-metadata-url string    The SAML metadata URL for SAML providers
      --tenant-domains string       Comma-separated list of allowed domains for the organization (e.g., 'example.com,example.co.uk'). If not provided, domain will be derived from account email.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-model

Creates and uploads a model.

```
firectl create model [flags]
```

### Examples

```
firectl create model my-model /path/to/checkpoint/
firectl create model my-model s3://bucket/path
```

### Flags

```
      --base-model string                 If specified, then the model will be considered a PEFT addon with the given base model.
      --default-draft-model string        The default speculative draft model to use when creating a deployment.
      --default-draft-token-count int32   The default speculative draft token count when creating a deployment.
      --description string                The description of the model.
      --display-name string               The display name of the model.
      --embedding                         If true, sets the model kind to an embeddings base model.
      --enable-resumable-upload           If true, uses resumable upload for the model.
      --github-url string                 The GitHub URL of the model.
  -h, --help                              help for model
      --hugging-face-url string           The Hugging Face URL of the model.
      --poll-duration duration            The duration to poll for model import operation completion. Default is 2 hours. (default 2h0m0s)
      --public                            Whether the model is publicly accessible.
      --quiet                             If true, does not print the upload progress bar.
      --supports-image-input              Whether the model supports image inputs.
      --supports-tools                    Whether the model supports function calling.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create reinforcement-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-reinforcement-fine-tuning-job

Creates a reinforcement fine-tuning job.

```
firectl create reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl create reinforcement-fine-tuning-job \
	--base-model llama-v3-8b-instruct \
	--dataset sample-dataset \
	--epochs 5 \
	--output-model name-of-the-trained-model
	--evaluator accounts/my-account/evaluators/abc123

```

### Flags

```
      --base-model string                   The base model for the reinforcement fine-tuning job. Only one of base-model or warm-start-from should be specified.
      --dataset string                      The dataset for the reinforcement fine-tuning job. (Required)
      --output-model string                 The output model for the reinforcement fine-tuning job.
      --job-id string                       The ID of the reinforcement fine-tuning job. If not set, it will be autogenerated.
      --warm-start-from string              The model to warm start from. If set, base-model must not be set.
      --evaluator string                    The evaluator resource name to use for the reinforcement fine-tuning job. (Required)
      --mcp-server string                   The MCP server resource name to use for the reinforcement fine-tuning job. (Optional)
      --epochs int32                        The number of epochs for the reinforcement fine-tuning job. (default 5)
      --learning-rate float32               The learning rate for the reinforcement fine-tuning job. (default 0.0001)
      --max-context-length int32            Maximum token length for sequences within each training batch. Shorter sequences are concatenated; longer sequences are truncated. (default 8192)
      --batch-size int32                    The maximum number of tokens packed into each training batch in the reinforcement fine-tuning. (default 32768)
      --gradient-accumulation-steps int32   The number of gradient accumulation steps for the reinforcement fine-tuning job. (default 1)
      --learning-rate-warmup-steps int32    The number of learning rate warmup steps for the reinforcement fine-tuning job.
      --lora-rank int32                     The rank of the LoRA layers for the reinforcement fine-tuning job.
                                             (default 8)
      --wandb-api-key string                [WANDB_API_KEY] WandB API Key. (Required if any WandB flag is set)
      --wandb-project string                [WANDB_PROJECT] WandB Project. (Required if any WandB flag is set)
      --wandb-entity string                 [WANDB_ENTITY] WandB Entity. (Required if any WandB flag is set)
      --wandb                               Enable WandB
                                            
      --temperature float32                 The randomness of the model's word or token selection during text generation. (default 1)
      --top-p float32                       Top-p sampling, selecting the smallest set of candidate words whose cumulative probability exceeds the top-p. (default 1)
      --response-candidates-count int32     The number of response candidates to generate per input. (default 4)
      --max-output-tokens int32             The maximum number of tokens to generate in the response. If 0, the model's default will be used.
      --top-k int32                         Top-k sampling parameter, limits the token selection to the top k tokens.
      --extra-body string                   Additional parameters for the inference request as a JSON string. For example: '{"stop": ["\n"]}'
      --quiet                               If set, only errors will be printed.
      --eval-auto-carveout                  If set, the evaluation dataset will be auto-carved.
  -h, --help                                help for reinforcement-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create secret
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-secret

Creates a secret for the signed in user.

```
firectl create secret [flags]
```

### Examples

```
firectl create secret --name MY_SECRET --value mysecretvalue
```

### Flags

```
  -h, --help           help for secret
      --name string    The name of the secret to be created
      --value string   The value of the secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create supervised-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-supervised-fine-tuning-job

Creates a supervised fine-tuning job.

```
firectl create supervised-fine-tuning-job [flags]
```

### Examples

```
firectl create sftj \
	--base-model llama-v3-8b-instruct \
	--dataset sample-dataset \
	--output-model name-of-the-trained-model

# Create from source job:
firectl create sftj \
	--source-job my-previous-job \
	--output-model new-model

```

### Flags

```
      --base-model string                   The base model for the supervised fine-tuning job. Only one of base-model or warm-start-from should be specified.
      --dataset string                      The dataset for the supervised fine-tuning job. (Required)
      --output-model string                 The output model for the supervised fine-tuning job.
      --job-id string                       The ID of the supervised fine-tuning job. If not set, it will be autogenerated.
      --warm-start-from string              The model to warm start from. If set, base-model must not be set.
      --source-job string                   The source supervised fine-tuning job to copy configuration from. If other flags are set, they will override the source job's configuration.
      --evaluation-dataset string           The evaluation dataset for the supervised fine-tuning job.
      --epochs int32                        The number of epochs for the supervised fine-tuning job.
      --learning-rate float32               The learning rate for the supervised fine-tuning job.
      --max-context-length int32            Maximum token length for sequences within each training batch. Shorter sequences are concatenated; longer sequences are truncated. (default 8192)
      --batch-size int32                    The maximum number of tokens packed into each training batch. (default 32768)
      --gradient-accumulation-steps int32   The number of gradient accumulation steps for the supervised fine-tuning job. (default 1)
      --learning-rate-warmup-steps int32    The number of learning rate warmup steps for the supervised fine-tuning job.
      --lora-rank int32                     The rank of the LoRA layers for the supervised fine-tuning job.
                                             (default 8)
      --wandb-api-key string                [WANDB_API_KEY] WandB API Key. (Required if any WandB flag is set)
      --wandb-project string                [WANDB_PROJECT] WandB Project. (Required if any WandB flag is set)
      --wandb-entity string                 [WANDB_ENTITY] WandB Entity. (Required if any WandB flag is set)
      --wandb                               Enable WandB
                                            
      --display-name string                 The display name of the supervised fine-tuning job.
      --early-stop                          Enable early stopping for the supervised fine-tuning job.
      --quiet                               If set, only errors will be printed.
      --eval-auto-carveout                  If set, the evaluation dataset will be auto-carved.
      --mtp-enable                          If set, enables MTP (Multi-Token-Prediction) layer (only available for Deepseek finetuning).
      --mtp-num-draft-tokens int32          Number of draft tokens in MTP. Needs to be between 1 and 3. Default is 1.
      --mtp-freeze-base-model               If set, freezes the base model parameters during MTP training.
  -h, --help                                help for supervised-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl create user
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-user

Creates a new user.

```
firectl create user [flags]
```

### Examples

```
firectl create user --email="alice.cullen@gmail.com"
firectl create user --service-account --user-id="my-bot"
```

### Flags

```
      --display-name string   The display name of the user.
      --email string          The email address of the user (not required for service accounts).
  -h, --help                  help for user
      --role string           The user's role, must be one of "user" or "admin" (default "user")
      --service-account       Admin only: Create as a service account (email will be auto-generated)
      --user-id string        The ID of the user (required for service accounts).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete api-key
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-api-key

Deletes an API key.

```
firectl delete api-key [flags]
```

### Examples

```
firectl delete api-key key-id
```

### Flags

```
  -h, --help   help for api-key
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete batch-inference-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-batch-inference-job

Deletes a batch inference job.

```
firectl delete batch-inference-job [flags]
```

### Examples

```
firectl delete batch-inference-job my-batch-job
firectl delete batch-inference-job accounts/my-account/batch-inference-jobs/my-batch-job
```

### Flags

```
  -h, --help                    help for batch-inference-job
      --wait                    Wait until the batch inference job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete dataset
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-dataset

Deletes a dataset.

```
firectl delete dataset [flags]
```

### Examples

```
firectl delete dataset my-dataset
firectl delete dataset accounts/my-account/datasets/my-dataset
```

### Flags

```
  -h, --help                    help for dataset
      --wait                    Wait until the dataset is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete deployment
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment

Deletes a deployment.

```
firectl delete deployment [flags]
```

### Examples

```
firectl delete deployment my-deployment
firectl delete deployment accounts/my-account/deployments/my-deployment
```

### Flags

```
      --hard                    Hard delete the deployment
  -h, --help                    help for deployment
      --ignore-checks           Skip checking if the deployment is in use before deleting
      --wait                    Wait until the deployment is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete dpo-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-dpo-job

Deletes a dpo job.

```
firectl delete dpo-job [flags]
```

### Examples

```
firectl delete dpo-job my-dpo-job
firectl delete dpo-job accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
  -h, --help                    help for dpo-job
      --wait                    Wait until the dpo job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-model

Deletes a model.

```
firectl delete model [flags]
```

### Examples

```
firectl delete model my-model
firectl delete model accounts/my-account/models/my-model
```

### Flags

```
  -h, --help   help for model
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete reinforcement-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-reinforcement-fine-tuning-job

Deletes a reinforcement fine-tuning job.

```
firectl delete reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl delete reinforcement-fine-tuning-job my-rftj
firectl delete reinforcement-fine-tuning-job accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help                    help for reinforcement-fine-tuning-job
      --wait                    Wait until the reinforcement fine-tuning job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete secret
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-secret

Deletes a secret.

```
firectl delete secret [flags]
```

### Examples

```
firectl delete secret MY_SECRET
```

### Flags

```
  -h, --help   help for secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete supervised-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-supervised-fine-tuning-job

Deletes a supervised fine-tuning job.

```
firectl delete supervised-fine-tuning-job [flags]
```

### Examples

```
firectl delete supervised-fine-tuning-job my-sft-job
firectl delete supervised-fine-tuning-job accounts/my-account/supervised-fine-tuning-jobs/my-sft-job
```

### Flags

```
  -h, --help                    help for supervised-fine-tuning-job
      --wait                    Wait until the supervised fine-tuning job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl delete user
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-user

Deletes a user.

```
firectl delete user [flags]
```

### Examples

```
firectl delete user my-user
firectl delete user accounts/my-account/users/my-user
```

### Flags

```
  -h, --help   help for user
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl download billing-metrics
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-billing-metrics

Exports billing metrics

```
firectl download billing-metrics [flags]
```

### Examples

```
firectl export billing-metrics
```

### Flags

```
      --end-time string     The end time (exclusive).
      --filename string     The file name to export to. (default "billing_metrics.csv")
  -h, --help                help for billing-metrics
      --start-time string   The start time (inclusive).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl download dataset
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-dataset

Downloads a dataset to a local directory.

```
firectl download dataset [flags]
```

### Examples

```
# Download a single dataset
firectl download dataset my-dataset --output-dir /path/to/download

# Download entire lineage chain
firectl download dataset my-dataset --download-lineage --output-dir /path/to/download
```

### Flags

```
      --download-lineage    If true, downloads entire lineage chain (all related datasets)
  -h, --help                help for dataset
      --output-dir string   Directory to download dataset files to (default ".")
      --quiet               If true, does not show download progress
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl download dpo-job-metrics
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-dpo-job-metrics

Retrieves metrics for a dpo job.

```
firectl download dpo-job-metrics [flags]
```

### Examples

```
firectl download dpoj-metrics my-dpo-job
firectl download dpoj-metrics accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
      --filename string   The file name to export to. (default "metrics.jsonl")
  -h, --help              help for dpo-job-metrics
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl download model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-model

Download a model.

```
firectl download model [flags]
```

### Examples

```
firectl download model my-model /path/to/checkpoint/
```

### Flags

```
  -h, --help    help for model
      --quiet   If true, does not print the upload progress bar.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get account
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-account

Prints information about an account.

```
firectl get account [flags]
```

### Examples

```
firectl get account
firectl get account my-account
firectl get account accounts/my-account
```

### Flags

```
  -h, --help   help for account
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get batch-inference-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-batch-inference-job

Retrieves information about a batch inference job.

```
firectl get batch-inference-job [flags]
```

### Examples

```
firectl get batch-inference-job my-batch-job
firectl get batch-inference-job accounts/my-account/batch-inference-jobs/my-batch-job
```

### Flags

```
  -h, --help   help for batch-inference-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get dataset
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-dataset

Prints information about a dataset.

```
firectl get dataset [flags]
```

### Examples

```
firectl get dataset my-dataset
firectl get dataset accounts/my-account/datasets/my-dataset
```

### Flags

```
  -h, --help   help for dataset
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get deployed-model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployed-model

Prints information about a deployed model.

```
firectl get deployed-model [flags]
```

### Examples

```
firectl get deployed-model my-deployed-model
firectl get deployed-model accounts/my-account/deployed-models/my-deployed-model
```

### Flags

```
  -h, --help   help for deployed-model
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get deployment
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment

Prints information about a deployment.

```
firectl get deployment [flags]
```

### Examples

```
firectl get deployment my-deployment
firectl get deployment accounts/my-account/deployments/my-deployment
```

### Flags

```
  -h, --help   help for deployment
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get deployment-shape-version
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment-shape-version

Prints information about a deployment shape version.

```
firectl get deployment-shape-version [flags]
```

### Examples

```
firectl get deployment-shape-version accounts/my-account/deploymentShapes/my-deployment-shape/versions/my-version
		firectl get deployment-shape-version accounts/my-account/deploymentShapes/my-deployment-shape/versions/latest
```

### Flags

```
  -h, --help   help for deployment-shape-version
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get dpo-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-dpo-job

Retrieves information about a dpo job.

```
firectl get dpo-job [flags]
```

### Examples

```
firectl get dpo-job my-dpo-job
firectl get dpo-job accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
  -h, --help   help for dpo-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get feature-flag
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-feature-flag

Gets a feature flag.

```
firectl get feature-flag [flags]
```

### Examples

```
firectl get feature-flag my-account my-feature-flag
```

### Flags

```
  -h, --help   help for feature-flag
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get identity-provider
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-identity-provider

Prints information about an identity provider.

```
firectl get identity-provider [flags]
```

### Examples

```
firectl get identity-provider my-provider
```

### Flags

```
  -h, --help   help for identity-provider
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-model

Prints information about a model.

```
firectl get model [flags]
```

### Examples

```
firectl get model my-model
firectl get model accounts/fireworks/models/my-model
```

### Flags

```
  -h, --help   help for model
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get quota
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-quota

Prints information about a quota.

```
firectl get quota [flags]
```

### Examples

```
firectl get quota serverless-inference-rpm
firectl get quota accounts/my-account/quotas/serverless-inference-rpm
```

### Flags

```
  -h, --help   help for quota
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get reinforcement-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-reinforcement-fine-tuning-job

Retrieves information about a reinforcement fine-tuning job.

```
firectl get reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl get reinforcement-fine-tuning-job my-rftj
firectl get reinforcement-fine-tuning-job accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for reinforcement-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get reservation
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-reservation

Prints information about a reservation.

```
firectl get reservation [flags]
```

### Examples

```
firectl get reservation abcdef
firectl get reservation accounts/my-account/reservations/abcdef
```

### Flags

```
  -h, --help   help for reservation
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get secret
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-secret

Retrieves a secret by name.

```
firectl get secret [flags]
```

### Examples

```
firectl get secret MY_SECRET
```

### Flags

```
  -h, --help   help for secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get supervised-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-supervised-fine-tuning-job

Retrieves information about a supervised fine-tuning job.

```
firectl get supervised-fine-tuning-job [flags]
```

### Examples

```
firectl get supervised-fine-tuning-job my-sft-job
firectl get supervised-fine-tuning-job accounts/my-account/supervised-fine-tuning-jobs/my-sft-job
```

### Flags

```
  -h, --help   help for supervised-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl get user
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-user

Prints information about a user.

```
firectl get user [flags]
```

### Examples

```
firectl get user my-user
firectl get user accounts/my-account/users/my-user
```

### Flags

```
  -h, --help   help for user
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list accounts
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-accounts

Prints all accounts the current signed-in user has access to.

```
firectl list accounts [flags]
```

### Examples

```
firectl list accounts
```

### Flags

```
  -h, --help   help for accounts
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list api-key
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-api-key

Prints all API keys for the signed in user.

```
firectl list api-key [flags]
```

### Examples

```
firectl list api-keys
```

### Flags

```
      --all-users   Admin only: list API keys for all users in the account
  -h, --help        help for api-key
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list batch-inference-jobs
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-batch-inference-jobs

Lists all batch inference jobs in an account.

```
firectl list batch-inference-jobs [flags]
```

### Examples

```
firectl list batch-inference-jobs
```

### Flags

```
  -h, --help   help for batch-inference-jobs
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list datasets
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-datasets

Prints all datasets in an account.

```
firectl list datasets [flags]
```

### Examples

```
firectl list datasets
```

### Flags

```
  -h, --help   help for datasets
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list deployed-models
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-deployed-models

Prints all deployed models in the account.

```
firectl list deployed-models [flags]
```

### Examples

```
firectl list deployed-models
```

### Flags

```
  -h, --help   help for deployed-models
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list deployment-shape-versions
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-deployment-shape-versions

Prints all deployment shape versions of this deployment shape.

```
firectl list deployment-shape-versions [flags]
```

### Examples

```
firectl list deployment-shape-versions my-deployment-shape
firectl list deployment-shape-versions accounts/my-account/deploymentShapes/my-deployment-shape
firectl list deployment-shape-versions
```

### Flags

```
      --base-model string   If specified, will filter out versions not matching the given base model.
  -h, --help                help for deployment-shape-versions
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list deployments
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-deployments

Prints all deployments in the account.

```
firectl list deployments [flags]
```

### Examples

```
firectl list deployments
```

### Flags

```
  -h, --help           help for deployments
      --show-deleted   If true, DELETED deployments will be included.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list dpo-jobs
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-dpo-jobs

Lists all dpo jobs in an account.

```
firectl list dpo-jobs [flags]
```

### Examples

```
firectl list dpo-jobs
```

### Flags

```
  -h, --help   help for dpo-jobs
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list identity-providers
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-identity-providers

List identity providers for an account

```
firectl list identity-providers [flags]
```

### Examples

```
firectl list identity-providers
```

### Flags

```
  -h, --help   help for identity-providers
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list invoices
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-invoices

Prints information about invoices.

```
firectl list invoices [flags]
```

### Examples

```
firectl list invoices
```

### Flags

```
  -h, --help           help for invoices
      --show-pending   If true, only pending invoices are shown.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list models
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-models

Prints all models in an account.

```
firectl list models [flags]
```

### Examples

```
firectl list models
```

### Flags

```
  -h, --help   help for models
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list quotas
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-quotas

Prints all quotas.

```
firectl list quotas [flags]
```

### Examples

```
firectl list quotas
```

### Flags

```
  -h, --help   help for quotas
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list reinforcement-fine-tuning-jobs
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-reinforcement-fine-tuning-jobs

Lists all reinforcement fine-tuning jobs in an account.

```
firectl list reinforcement-fine-tuning-jobs [flags]
```

### Examples

```
firectl list reinforcement-fine-tuning-jobs
```

### Flags

```
  -h, --help   help for reinforcement-fine-tuning-jobs
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list reservations
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-reservations

Prints active reservations.

```
firectl list reservations [flags]
```

### Examples

```
firectl list reservations
```

### Flags

```
  -h, --help            help for reservations
      --show-inactive   Show all reservations
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```



---

**Navigation:** [← Previous](./05-svg-drawing-agent.md) | [Index](./index.md) | [Next →](./07-firectl-list-secret.md)
