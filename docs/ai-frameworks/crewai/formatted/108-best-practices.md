---
title: "Crewai: Best Practices"
description: "Best Practices section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Best Practices


1. **Keep Handlers Light**: Event handlers should be lightweight and avoid blocking operations
2. **Error Handling**: Include proper error handling in your event handlers to prevent exceptions from affecting the main execution
3. **Cleanup**: If your listener allocates resources, ensure they're properly cleaned up
4. **Selective Listening**: Only listen for events you actually need to handle
5. **Testing**: Test your event listeners in isolation to ensure they behave as expected

By leveraging CrewAI's event system, you can extend its functionality and integrate it seamlessly with your existing infrastructure.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use Cases](./107-use-cases.md)

**Next:** [Flows →](./109-flows.md)
