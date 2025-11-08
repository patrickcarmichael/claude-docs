---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

### Basic Flight Task Evaluation

```bash
export MODEL_AGENT=openai/gpt-4o
reward-kit agent-eval --task-dir ./examples/flight_task
```

### Testing Without API Keys

```bash
reward-kit agent-eval --task-dir ./examples/flight_task --test-mode --mock-response
```

### Complex Task with Multiple Tool Registries

```bash
reward-kit agent-eval --task-dir ./examples/travel_task --registries flight=flight_tools,hotel=hotel_tools
```

### Running with Specific Task IDs

```bash
reward-kit agent-eval --task-dir ./examples/flight_task --task-ids flight.booking.001,flight.booking.002
```

### Using Debug Mode

```bash
reward-kit agent-eval --task-dir ./examples/flight_task --debug
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
