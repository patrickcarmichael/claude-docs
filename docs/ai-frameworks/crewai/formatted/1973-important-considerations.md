---
title: "Crewai: Important Considerations"
description: "Important Considerations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Important Considerations


1. **Model Selection**: It is strongly recommended to use more capable models like Claude 3.5 Sonnet and GPT-4 when enabling code execution.
   These models have a better understanding of programming concepts and are more likely to generate correct and efficient code.

2. **Error Handling**: The code execution feature includes error handling. If executed code raises an exception, the agent will receive the error message and can attempt to correct the code or
   provide alternative solutions. The `max_retry_limit` parameter, which defaults to 2, controls the maximum number of retries for a task.

3. **Dependencies**: To use the code execution feature, you need to install the `crewai_tools` package. If not installed, the agent will log an info message:
   "Coding tools not available. Install crewai\_tools."

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling Code Execution](./1972-enabling-code-execution.md)

**Next:** [Code Execution Process →](./1974-code-execution-process.md)
