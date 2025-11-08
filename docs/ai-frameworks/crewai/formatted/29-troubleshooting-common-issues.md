---
title: "Crewai: Troubleshooting Common Issues"
description: "Troubleshooting Common Issues section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting Common Issues


1. **Rate Limiting**: If you're hitting API rate limits:
   * Implement appropriate `max_rpm`
   * Use caching for repetitive operations
   * Consider batching requests

2. **Context Window Errors**: If you're exceeding context limits:
   * Enable `respect_context_window`
   * Use more efficient prompts
   * Clear agent memory periodically

3. **Code Execution Issues**: If code execution fails:
   * Verify Docker is installed for safe mode
   * Check execution permissions
   * Review code sandbox settings

4. **Memory Issues**: If agent responses seem inconsistent:
   * Check knowledge source configuration
   * Review conversation history management

Remember that agents are most effective when configured according to their specific use case. Take time to understand your requirements and adjust these parameters accordingly.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Important Considerations and Best Practices](./28-important-considerations-and-best-practices.md)

**Next:** [CLI →](./30-cli.md)
