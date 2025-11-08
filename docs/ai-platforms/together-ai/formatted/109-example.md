---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

In this example, we will use Together AI to star a repository on GitHub using Composio Tools.
```python
  from composio_togetherai import ComposioToolSet, App
  from together import Together

  client = Together()
  toolset = ComposioToolSet()
```
```typescript
  /*
  We use the Vercel AI SDK with the Together provider to 
  enable type checking to work correctly for tools and 
  to simplify the Composio integration. 
  This flow enables us to directly execute tool calls
  without having to use composio.provider.handleToolCalls.
  */

  import { Composio } from "@composio/core";
  import { VercelProvider } from "@composio/vercel";
  import { createTogetherAI } from "@ai-sdk/togetherai";
  import { generateText } from "ai";

  export const together = createTogetherAI({
    apiKey: process.env.TOGETHER_API_KEY ?? "",
  });

  const composio = new Composio({
    apiKey: process.env.COMPOSIO_API_KEY ?? "",
    provider: new VercelProvider(),
  });
```

### Connect Your GitHub Account

You need to have an active GitHub Integration in Composio. Learn how to do this [here](https://www.youtube.com/watch?v=LmyWy4LiedQ)
```py
  request = toolset.initiate_connection(app=App.GITHUB)
  print(f"Open this URL to authenticate: {request.redirectUrl}")
```
```sh
  composio login
  composio add github
```

### Get All Github Tools

You can get all the tools for a given app as shown below, but you can get specific actions and filter actions using usecase & tags.
```python
  tools = toolset.get_tools(apps=[App.GITHUB])
```
```typescript
  const userId = "default"; // replace with user id from composio
  const tools = await composio.tools.get(userId, {
    toolkits: ['github'],
  });
```

### Create a Chat Completion with Tools

```python
  response = client.chat.completions.create(
      tools=tools,
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "Star the repo 'togethercomputer/together-cookbook'",
          }
      ],
  )

  res = toolset.handle_tool_calls(response)
  print(res)
```
```typescript
  const responseGithub = await generateText({
      model: together("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      messages: [
        {
          role: "user",
          content: "Star the repo 'togethercomputer/together-cookbook'",
        },
      ],
      tools,
      toolChoice: "required",
  });

  console.log(responseGithub);
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
