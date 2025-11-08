---
title: "Crewai: Create an agent with Stripe capabilities"
description: "Create an agent with Stripe capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Stripe capabilities

stripe_agent = Agent(
    role="Payment Manager",
    goal="Manage customer payments, subscriptions, and billing operations efficiently",
    backstory="An AI assistant specialized in payment processing and subscription management.",
    apps=['stripe']  # All Stripe actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1940-usage-examples.md)

**Next:** [Task to create a new customer →](./1942-task-to-create-a-new-customer.md)
