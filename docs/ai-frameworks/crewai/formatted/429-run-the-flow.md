---
title: "Crewai: Run the flow"
description: "Run the flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the flow

support_flow = CustomerSupportFlow()
result = support_flow.kickoff()
```

### When to Combine Crews and Flows

The most sophisticated applications often benefit from combining Crews and Flows:

1. **Complex multi-stage processes** - Use Flows to orchestrate the overall process and Crews for complex subtasks
2. **Applications requiring both creativity and structure** - Use Crews for creative tasks and Flows for structured processing
3. **Enterprise-grade AI applications** - Use Flows to manage state and process flow while leveraging Crews for specialized work

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define structured state](./428-define-structured-state.md)

**Next:** [Example: Content Production Pipeline combining Crews and Flows →](./430-example-content-production-pipeline-combining-crew.md)
