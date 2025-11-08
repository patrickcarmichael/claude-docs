---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

In this simple example we augment an LLM with a calculator tool!
```python
  import os
  from langchain_together import ChatTogether

  llm = ChatTogether(
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      api_key=os.getenv("TOGETHER_API_KEY"),
  )


  # Define a tool

  def multiply(a: int, b: int) -> int:
      return a * b


  # Augment the LLM with tools

  llm_with_tools = llm.bind_tools([multiply])

  # Invoke the LLM with input that triggers the tool call

  msg = llm_with_tools.invoke("What is 2 times 3?")

  # Get the tool call

  msg.tool_calls
```
```typescript
  import { ChatTogetherAI } from "@langchain/community/chat_models/togetherai";

  const llm = new ChatTogetherAI({
      model: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      apiKey: process.env.TOGETHER_API_KEY,
  });

  // Define a tool
  const multiply = {
      name: "multiply",
      description: "Multiply two numbers",
      schema: {
          type: "function",
          function: {
              name: "multiply",
              description: "Multiply two numbers",
              parameters: {
                  type: "object",
                  properties: {
                      a: { type: "number" },
                      b: { type: "number" },
                  },
                  required: ["a", "b"],
              },
          },
      },
  };

  // Augment the LLM with tools
  const llmWithTools = llm.bindTools([multiply]);

  // Invoke the LLM with input that triggers the tool call
  const msg = await llmWithTools.invoke("What is 2 times 3?");

  // Get the tool call
  console.log(msg.tool_calls);
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
