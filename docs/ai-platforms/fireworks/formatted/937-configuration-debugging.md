---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Configuration & debugging

<AccordionGroup>
  <Accordion title="Sampling parameters">
    Control how the model generates text. Fireworks automatically uses recommended sampling parameters from each model's HuggingFace `generation_config.json` when you don't specify them explicitly, ensuring optimal performance out-of-the-box.

    We pull `temperature`, `top_k`, `top_p`, `min_p`, and `typical_p` from the model's configuration when not explicitly provided.

    ### Temperature

    Adjust randomness (0 = deterministic, higher = more creative):
```python
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Write a poem"}],
        temperature=0.7  # Override model default

    )
```
    ### Max tokens

    Control the maximum number of tokens in the generated completion:
```python
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
```python
    top_p=0.9  # Consider top 90% probability mass

```
    ### Top-k

    Consider only the k most probable tokens:
```python
    top_k=50  # Consider top 50 tokens

```
    ### Min-p

    Exclude tokens below a probability threshold:
```python
    min_p=0.05  # Exclude tokens with <5% probability

```
    ### Typical-p

    Use typical sampling to select tokens with probability close to the entropy of the distribution:
```python
    typical_p=0.95  # Consider tokens with typical probability

```
    ### Repetition penalties

    Reduce repetitive text with `frequency_penalty`, `presence_penalty`, or `repetition_penalty`:
```python
    frequency_penalty=0.5,   # Penalize frequent tokens (OpenAI compatible)

    presence_penalty=0.5,    # Penalize any repeated token (OpenAI compatible)

    repetition_penalty=1.1   # Exponential penalty from prompt + output

```
    ### Sampling options header

    The `fireworks-sampling-options` header contains the actual default sampling parameters used for the model, including values from the model's HuggingFace `generation_config.json`:

    <Tabs>
      <Tab title="Python">
```python
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
```javascript
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
```python
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
```python
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
```python
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        echo=True
    )
```
    **Raw output:** See raw token IDs and prompt fragments:

    >   **⚠️ Warning**
>
> Experimental API - may change without notice.
```python
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
```python
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        ignore_eos=True,
        max_tokens=100  # Will always generate exactly 100 tokens

    )
```
    >   **📝 Note**
>
> Output quality may degrade when ignoring EOS. This API is experimental and should not be relied upon for production use cases.
  </Accordion>

  <Accordion title="Logit bias">
    Modify token probabilities to encourage or discourage specific tokens:
```python
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
```python
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}],
        mirostat_target=5.0,  # Target perplexity

        mirostat_lr=0.1       # Learning rate for adjustments

    )
```
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
