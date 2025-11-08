---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implementation: Cost Tracking System

Here's a complete example of implementing a cost tracking system:
```typescript
  import { query } from "@anthropic-ai/claude-agent-sdk";

  class CostTracker {
    private processedMessageIds = new Set<string>();
    private stepUsages: Array<any> = [];
    
    async trackConversation(prompt: string) {
      const result = await query({
        prompt,
        options: {
          onMessage: (message) => {
            this.processMessage(message);
          }
        }
      });
      
      return {
        result,
        stepUsages: this.stepUsages,
        totalCost: result.usage?.total_cost_usd || 0
      };
    }
    
    private processMessage(message: any) {
      // Only process assistant messages with usage
      if (message.type !== 'assistant' || !message.usage) {
        return;
      }
      
      // Skip if we've already processed this message ID
      if (this.processedMessageIds.has(message.id)) {
        return;
      }
      
      // Mark as processed and record usage
      this.processedMessageIds.add(message.id);
      this.stepUsages.push({
        messageId: message.id,
        timestamp: new Date().toISOString(),
        usage: message.usage,
        costUSD: this.calculateCost(message.usage)
      });
    }
    
    private calculateCost(usage: any): number {
      // Implement your pricing calculation here
      // This is a simplified example
      const inputCost = usage.input_tokens * 0.00003;
      const outputCost = usage.output_tokens * 0.00015;
      const cacheReadCost = (usage.cache_read_input_tokens || 0) * 0.0000075;
      
      return inputCost + outputCost + cacheReadCost;
    }
  }

  // Usage
  const tracker = new CostTracker();
  const { result, stepUsages, totalCost } = await tracker.trackConversation(
    "Analyze and refactor this code"
  );

  console.log(`Steps processed: ${stepUsages.length}`);
  console.log(`Total cost: $${totalCost.toFixed(4)}`);
```
```python
  from claude_agent_sdk import query, AssistantMessage, ResultMessage
  from datetime import datetime
  import asyncio

  class CostTracker:
      def __init__(self):
          self.processed_message_ids = set()
          self.step_usages = []

      async def track_conversation(self, prompt):
          result = None

          # Process messages as they arrive

          async for message in query(prompt=prompt):
              self.process_message(message)

              # Capture the final result message

              if isinstance(message, ResultMessage):
                  result = message

          return {
              "result": result,
              "step_usages": self.step_usages,
              "total_cost": result.total_cost_usd if result else 0
          }

      def process_message(self, message):
          # Only process assistant messages with usage

          if not isinstance(message, AssistantMessage) or not hasattr(message, 'usage'):
              return

          # Skip if already processed this message ID

          message_id = getattr(message, 'id', None)
          if not message_id or message_id in self.processed_message_ids:
              return

          # Mark as processed and record usage

          self.processed_message_ids.add(message_id)
          self.step_usages.append({
              "message_id": message_id,
              "timestamp": datetime.now().isoformat(),
              "usage": message.usage,
              "cost_usd": self.calculate_cost(message.usage)
          })

      def calculate_cost(self, usage):
          # Implement your pricing calculation

          input_cost = usage.get("input_tokens", 0) * 0.00003
          output_cost = usage.get("output_tokens", 0) * 0.00015
          cache_read_cost = usage.get("cache_read_input_tokens", 0) * 0.0000075

          return input_cost + output_cost + cache_read_cost

  # Usage

  async def main():
      tracker = CostTracker()
      result = await tracker.track_conversation("Analyze and refactor this code")

      print(f"Steps processed: {len(result['step_usages'])}")
      print(f"Total cost: ${result['total_cost']:.4f}")

  asyncio.run(main())
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
