---
title: "Crewai: Advanced State Patterns"
description: "Advanced State Patterns section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced State Patterns


### Conditional starts and resumable execution

Flows support conditional `@start()` and resumable execution for HITL/cyclic scenarios:

```python  theme={null}
from crewai.flow.flow import Flow, start, listen, and_, or_

class ResumableFlow(Flow):
    @start()  # unconditional start
    def init(self):
        ...

    # Conditional start: run after "init" or external trigger name
    @start("init")
    def maybe_begin(self):
        ...

    @listen(and_(init, maybe_begin))
    def proceed(self):
        ...
```

* Conditional `@start()` accepts a method name, a router label, or a callable condition.
* During resume, listeners continue from prior checkpoints; cycle/router branches honor resumption flags.

### State-Based Conditional Logic

You can use state to implement complex conditional logic in your flows:

```python  theme={null}
from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel

class PaymentState(BaseModel):
    amount: float = 0.0
    is_approved: bool = False
    retry_count: int = 0

class PaymentFlow(Flow[PaymentState]):
    @start()
    def process_payment(self):
        # Simulate payment processing
        self.state.amount = 100.0
        self.state.is_approved = self.state.amount < 1000
        return "Payment processed"

    @router(process_payment)
    def check_approval(self, previous_result):
        if self.state.is_approved:
            return "approved"
        elif self.state.retry_count < 3:
            return "retry"
        else:
            return "rejected"

    @listen("approved")
    def handle_approval(self):
        return f"Payment of ${self.state.amount} approved!"

    @listen("retry")
    def handle_retry(self):
        self.state.retry_count += 1
        print(f"Retrying payment (attempt {self.state.retry_count})...")
        # Could implement retry logic here
        return "Retry initiated"

    @listen("rejected")
    def handle_rejection(self):
        return f"Payment of ${self.state.amount} rejected after {self.state.retry_count} retries."
```

### Handling Complex State Transformations

For complex state transformations, you can create dedicated methods:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from typing import List, Dict

class UserData(BaseModel):
    name: str
    active: bool = True
    login_count: int = 0

class ComplexState(BaseModel):
    users: Dict[str, UserData] = {}
    active_user_count: int = 0

class TransformationFlow(Flow[ComplexState]):
    @start()
    def initialize(self):
        # Add some users
        self.add_user("alice", "Alice")
        self.add_user("bob", "Bob")
        self.add_user("charlie", "Charlie")
        return "Initialized"

    @listen(initialize)
    def process_users(self, _):
        # Increment login counts
        for user_id in self.state.users:
            self.increment_login(user_id)

        # Deactivate one user
        self.deactivate_user("bob")

        # Update active count
        self.update_active_count()

        return f"Processed {len(self.state.users)} users"

    # Helper methods for state transformations
    def add_user(self, user_id: str, name: str):
        self.state.users[user_id] = UserData(name=name)
        self.update_active_count()

    def increment_login(self, user_id: str):
        if user_id in self.state.users:
            self.state.users[user_id].login_count += 1

    def deactivate_user(self, user_id: str):
        if user_id in self.state.users:
            self.state.users[user_id].active = False
            self.update_active_count()

    def update_active_count(self):
        self.state.active_user_count = sum(
            1 for user in self.state.users.values() if user.active
        )
```

This pattern of creating helper methods keeps your flow methods clean while enabling complex state manipulations.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Second run - state is automatically loaded](./498-second-run-state-is-automatically-loaded.md)

**Next:** [State Management with Crews →](./500-state-management-with-crews.md)
