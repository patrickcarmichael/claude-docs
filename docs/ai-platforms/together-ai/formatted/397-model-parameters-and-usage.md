---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Model Parameters and Usage

### What is the maximum context window supported by Together models?

The maximum context window varies significantly by model. Refer to the specific model's documentation or the inference models [page](https://docs.together.ai/docs/serverless-models) for the exact context length supported by each model.

### Where can I find default parameter values for a model?

Default parameter values for a model can be found in the `generation_config.json` file on Hugging Face. For example, the configuration for Llama 3.3 70B Instruct shows defaults like temperature: 0.6 and top\_p: 0.9. If not defined, no value is passed for that parameter.

### How do I send a request to an inference endpoint?

You can use the OpenAI-compatible API. Example using curl:
```bash
curl https://api.together.xyz/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
         "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
         "messages": [{"role": "user", "content": "Hello!"}]
       }'
```

More examples in Python and TypeScript are available [here](https://docs.together.ai/docs/openai-api-compatibility).

### Do you support function calling or tool use?

Function calling is natively supported for some models (see [here](https://docs.together.ai/docs/function-calling#function-calling)) but structured prompting can simulate function-like behavior.

### Function Calls Not Returned in Response "message.content"

Models that support Function Calling return any tool calls in a separate part of the model response, not inside of `message.content`. Some models will return "None" for this if any function calls are made.

Any tool calls instead will be found in:

`message.tool_calls[0].function.name`

For example, when making a function call, `message.content` may be None, but the function name will be in `message.tool_calls[0].function.name`.

### Do you support structured outputs or JSON mode?

Yes, you can use JSON mode to get structured outputs from LLMs like DeepSeek V3 & Llama 3.3. See more [here](https://docs.together.ai/docs/json-mode).

#### Troubleshooting Structured Output Generation

When working with structured outputs, you may encounter issues where your generated JSON gets cut off or contains errors. Here are key considerations:

* **Token Limits**: Check the maximum token limit of your model and ensure you're under it. Model specifications are available in our [serverless models documentation](https://docs.together.ai/docs/serverless-models).

* **Malformed JSON**: Validate your example JSON before using it in prompts. The model follows your example exactly, including syntax errors. Common symptoms include unterminated strings, repeated newlines, incomplete structures, or truncated output with 'stop' finish reason.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
