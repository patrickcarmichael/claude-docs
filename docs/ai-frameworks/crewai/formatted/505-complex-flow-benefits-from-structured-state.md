---
title: "Crewai: Complex flow benefits from structured state"
description: "Complex flow benefits from structured state section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex flow benefits from structured state

class UserRegistrationState(BaseModel):
    username: str
    email: str
    verification_status: bool = False
    registration_date: datetime = Field(default_factory=datetime.now)
    last_login: Optional[datetime] = None

class RegistrationFlow(Flow[UserRegistrationState]):
    # Methods with strongly-typed state access
```

### 3. Document State Transitions

For complex flows, document how state changes throughout the execution:

```python  theme={null}
@start()
def initialize_order(self):
    """
    Initialize order state with empty values.

    State before: {}
    State after: {order_id: str, items: [], status: 'new'}
    """
    self.state.order_id = str(uuid.uuid4())
    self.state.items = []
    self.state.status = "new"
    return "Order initialized"
```

### 4. Handle State Errors Gracefully

Implement error handling for state access:

```python  theme={null}
@listen(previous_step)
def process_data(self, _):
    try:
        # Try to access a value that might not exist
        user_preference = self.state.preferences.get("theme", "default")
    except (AttributeError, KeyError):
        # Handle the error gracefully
        self.state.errors = self.state.get("errors", [])
        self.state.errors.append("Failed to access preferences")
        user_preference = "default"

    return f"Used preference: {user_preference}"
```

### 5. Use State for Progress Tracking

Leverage state to track progress in long-running flows:

```python  theme={null}
class ProgressTrackingFlow(Flow):
    @start()
    def initialize(self):
        self.state["total_steps"] = 3
        self.state["current_step"] = 0
        self.state["progress"] = 0.0
        self.update_progress()
        return "Initialized"

    def update_progress(self):
        """Helper method to calculate and update progress"""
        if self.state.get("total_steps", 0) > 0:
            self.state["progress"] = (self.state.get("current_step", 0) /
                                    self.state["total_steps"]) * 100
            print(f"Progress: {self.state['progress']:.1f}%")

    @listen(initialize)
    def step_one(self, _):
        # Do work...
        self.state["current_step"] = 1
        self.update_progress()
        return "Step 1 complete"

    # Additional steps...
```

### 6. Use Immutable Operations When Possible

Especially with structured state, prefer immutable operations for clarity:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Simple flow can use unstructured state](./504-simple-flow-can-use-unstructured-state.md)

**Next:** [Instead of modifying lists in place: →](./506-instead-of-modifying-lists-in-place.md)
