---
title: "Crewai: Run the flow"
description: "Run the flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the flow

if __name__ == "__main__":
    asyncio.run(run_flow())
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c60457e1a2b9bc0ef957c373a88359b" alt="Flow Visual image" data-og-width="1933" width="1933" data-og-height="959" height="959" data-path="images/crewai-flow-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4e6a743b2b19cd86dadbbd015d0a0393 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=740f254bb03d60cd011911dab702ca77 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b93c5bde69019cdc34c143bcc0885743 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4eabe8d3536d6588a14157b60bc7a1e0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e76b5df7821722a59d3267f3a0eff3ed 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3a9775e3f5798ccb73e5feb7e53319fd 2500w" />

This example demonstrates several key features of using Agents in flows:

1. **Structured Output**: Using Pydantic models to define the expected output format (`MarketAnalysis`) ensures type safety and structured data throughout the flow.

2. **State Management**: The flow state (`MarketResearchState`) maintains context between steps and stores both inputs and outputs.

3. **Tool Integration**: Agents can use tools (like `WebsiteSearchTool`) to enhance their capabilities.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage example](./119-usage-example.md)

**Next:** [Adding Crews to Flows →](./121-adding-crews-to-flows.md)
