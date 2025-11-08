---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Calling Tools

Now we need to run the function that the model has asked for and feed the response back to the model, this can be done by simply checking if the model asked for a tool call and executing the corresponding function and sending the response to the model:
```python
  tool_calls = response.choices[0].message.tool_calls

  # check is a tool was called by the first model call

  if tool_calls:
      for tool_call in tool_calls:
          function_name = tool_call.function.name
          function_args = json.loads(tool_call.function.arguments)

          if function_name == "read_file":
              # manually call the function

              function_response = read_file(path=function_args.get("path"))

              # add the response to messages to be sent back to the model

              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )
      # re-call the model now with the response of the tool!

      function_enriched_response = client.chat.completions.create(
          model="Qwen/Qwen2.5-7B-Instruct-Turbo",
          messages=messages,
      )
      print(
          json.dumps(
              function_enriched_response.choices[0].message.model_dump(),
              indent=2,
          )
      )
```

Output:
```json
  {
    "role": "assistant",
    "content": "The secret from the file secret.txt is \"my favourite colour is cyan sanguine\".",
    "tool_calls": []
  }
```

Above, we simply did the following:

1. See if the model wanted us to use a tool.
2. If so, we used the tool for it.
3. We appended the output from the tool back into `messages` and called the model again to make sense of the function response.

Now let's make our coding agent more interesting by creating two more tools!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
