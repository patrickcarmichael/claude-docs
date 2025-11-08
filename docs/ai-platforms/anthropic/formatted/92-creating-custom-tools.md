---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating Custom Tools

Use the `createSdkMcpServer` and `tool` helper functions to define type-safe custom tools:
```typescript
  import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
  import { z } from "zod";

  // Create an SDK MCP server with custom tools
  const customServer = createSdkMcpServer({
    name: "my-custom-tools",
    version: "1.0.0",
    tools: [
      tool(
        "get_weather",
        "Get current temperature for a location using coordinates",
        {
          latitude: z.number().describe("Latitude coordinate"),
          longitude: z.number().describe("Longitude coordinate")
        },
        async (args) => {
          const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&current=temperature_2m&temperature_unit=fahrenheit`);
          const data = await response.json();

          return {
            content: [{
              type: "text",
              text: `Temperature: ${data.current.temperature_2m}°F`
            }]
          };
        }
      )
    ]
  });
```
```python
  from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeSDKClient, ClaudeAgentOptions
  from typing import Any
  import aiohttp

  # Define a custom tool using the @tool decorator

  @tool("get_weather", "Get current temperature for a location using coordinates", {"latitude": float, "longitude": float})
  async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
      # Call weather API

      async with aiohttp.ClientSession() as session:
          async with session.get(
              f"https://api.open-meteo.com/v1/forecast?latitude={args['latitude']}&longitude={args['longitude']}&current=temperature_2m&temperature_unit=fahrenheit"
          ) as response:
              data = await response.json()

      return {
          "content": [{
              "type": "text",
              "text": f"Temperature: {data['current']['temperature_2m']}°F"
          }]
      }

  # Create an SDK MCP server with the custom tool

  custom_server = create_sdk_mcp_server(
      name="my-custom-tools",
      version="1.0.0",
      tools=[get_weather]  # Pass the decorated function

  )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
