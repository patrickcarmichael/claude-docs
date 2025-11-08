---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Incorporating Tools into the Coding Agent

Now we can add all three of these tools into the simple looping chat function we made and call it!
```python
  def chat():
      messages_history = []

      while True:
          user_input = input("You: ")
          if user_input.lower() in ["exit", "quit", "q"]:
              break

          messages_history.append({"role": "user", "content": user_input})

          response = client.chat.completions.create(
              model="Qwen/Qwen2.5-7B-Instruct-Turbo",
              messages=messages_history,
              tools=tools,
          )

          tool_calls = response.choices[0].message.tool_calls
          if tool_calls:
              for tool_call in tool_calls:
                  function_name = tool_call.function.name
                  function_args = json.loads(tool_call.function.arguments)

                  if function_name == "read_file":
                      print(f"Tool call: read_file")
                      function_response = read_file(
                          path=function_args.get("path")
                      )
                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )
                  elif function_name == "list_files":
                      print(f"Tool call: list_files")
                      function_response = list_files(
                          path=function_args.get("path", ".")
                      )

                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )
                  elif function_name == "edit_file":
                      print(f"Tool call: edit_file")
                      function_response = edit_file(
                          path=function_args.get("path"),
                          old_str=function_args.get("old_str"),
                          new_str=function_args.get("new_str"),
                      )
                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )

                  function_enriched_response = client.chat.completions.create(
                      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
                      messages=messages_history,
                  )

                  messages_history.append(
                      {
                          "role": "assistant",
                          "content": function_enriched_response.choices[
                              0
                          ].message.content,
                      }
                  )
                  print(
                      f"LLM: {function_enriched_response.choices[0].message.content}"
                  )
          else:
              messages_history.append(
                  {
                      "role": "assistant",
                      "content": response.choices[0].message.content,
                  }
              )
              print(f"LLM: {response.choices[0].message.content}")


  # start the chat

  chat()
```

Output:
````
You: Create a congrats.py script that rot13-decodes the following string ‘Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!’ and prints it.

Tool call: edit_file

LLM: Sure, I'll create a `congrats.py` script that rot13-decodes the given string and prints it. Here's the script:
```python
def rot13_decode(s):
    result = ""
    for char in s:
        if "a" <= char <= "z":
            start = ord("a")
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        elif "A" <= char <= "Z":
            start = ord("A")
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        else:
            result += char
    return result


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
