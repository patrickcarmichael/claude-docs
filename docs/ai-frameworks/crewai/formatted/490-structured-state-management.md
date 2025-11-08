---
title: "Crewai: Structured State Management"
description: "Structured State Management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Structured State Management


Structured state uses Pydantic models to define a schema for your flow's state, providing type safety, validation, and better developer experience.

### How It Works

With structured state:

* You define a Pydantic model that represents your state structure
* You pass this model type to your Flow class as a type parameter
* You access state via `self.state`, which behaves like a Pydantic model instance
* All fields are validated according to their defined types
* You get IDE autocompletion and type checking support

### Basic Example

Here's how to implement structured state management:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the flow](./489-run-the-flow.md)

**Next:** [Define your state model →](./491-define-your-state-model.md)
