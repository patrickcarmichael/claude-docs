---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Output: [ChatCompletionMessageToolCall(id='call_abc123', function=Function(arguments='{"location":"San Francisco"}', name='get_weather'), type='function')]

```
<Tip>
  For best results with tool calling, use a low temperature (0.0-0.3) to reduce hallucinated parameter values and ensure more deterministic tool selection.
</Tip>

<AccordionGroup>
  <Accordion title="Complete workflow: Execute tools and get final response">
```python
    import os
    from openai import OpenAI
    import json

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    # Step 1: Define your tools

    tools = [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }]

    # Step 2: Send initial request

    messages = [{"role": "user", "content": "What's the weather in San Francisco?"}]
    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2-instruct-0905",
        messages=messages,
        tools=tools,
        temperature=0.1
    )

    # Step 3: Check if model wants to call a tool

    if response.choices[0].message.tool_calls:
        # Step 4: Execute the tool

        tool_call = response.choices[0].message.tool_calls[0]
        
        # Your actual tool implementation

        def get_weather(location, unit="celsius"):
            # In production, call your weather API here

            return {"temperature": 72, "condition": "sunny", "unit": unit}
        
        # Parse arguments and call your function

        function_args = json.loads(tool_call.function.arguments)
        function_response = get_weather(**function_args)
        
        # Step 5: Send tool response back to model

        messages.append(response.choices[0].message)  # Add assistant's tool call

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(function_response)
        })
        
        # Step 6: Get final response

        final_response = client.chat.completions.create(
            model="accounts/fireworks/models/kimi-k2-instruct-0905",
            messages=messages,
            tools=tools,
            temperature=0.1
        )
        
        print(final_response.choices[0].message.content)
        # Output: "It's currently 72°F and sunny in San Francisco."

```
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
