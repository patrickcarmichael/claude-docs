---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Agent use case pricing examples

Understanding pricing for agent applications is crucial when building with Claude. These real-world examples can help you estimate costs for different agent patterns.

### Customer support agent example

When building a customer support agent, here's how costs might break down:

>   **📝 Note**
>
> Example calculation for processing 10,000 support tickets:

  * Average \~3,700 tokens per conversation
  * Using Claude Sonnet 4.5 at $3/MTok input, $15/MTok output
  * Total cost: \~\$22.20 per 10,000 tickets

For a detailed walkthrough of this calculation, see our [customer support agent guide](/en/docs/about-claude/use-case-guides/customer-support-chat).

### General agent workflow pricing

For more complex agent architectures with multiple steps:

1. **Initial request processing**
   * Typical input: 500-1,000 tokens
   * Processing cost: \~\$0.003 per request

2. **Memory and context retrieval**
   * Retrieved context: 2,000-5,000 tokens
   * Cost per retrieval: \~\$0.015 per operation

3. **Action planning and execution**
   * Planning tokens: 1,000-2,000
   * Execution feedback: 500-1,000
   * Combined cost: \~\$0.045 per action

For a comprehensive guide on agent pricing patterns, see our [agent use cases guide](/en/docs/about-claude/use-case-guides).

### Cost optimization strategies

When building agents with Claude:

1. **Use appropriate models**: Choose Haiku for simple tasks, Sonnet for complex reasoning
2. **Implement prompt caching**: Reduce costs for repeated context
3. **Batch operations**: Use the Batch API for non-time-sensitive tasks
4. **Monitor usage patterns**: Track token consumption to identify optimization opportunities

<Tip>
  For high-volume agent applications, consider contacting our [enterprise sales team](https://claude.com/contact-sales) for custom pricing arrangements.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
