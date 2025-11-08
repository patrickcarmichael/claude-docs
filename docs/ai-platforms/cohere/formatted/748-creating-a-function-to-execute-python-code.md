---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating a function to execute Python code

Here, we introduce a new tool that allows the agent to execute Python code and return the result. The agent will use this tool to generate pandas code for querying the data.

To create this tool, we'll use the `PythonREPL` class from the `langchain_experimental.utilities` module. This class provides a sandboxed environment for executing Python code and returns the result.

First, we define a `python_tool` that uses the `PythonREPL` class to execute Python code and return the result.

Next, we define a `ToolInput` class to handle the input for the `python_tool`.

Finally, we create a function `analyze_evaluation_results` that takes a string of Python code as input, executes the code using the Python tool we created, and returns the result.

**IMPORTANT:**

The source code for tool definitions can be [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py). Make sure to have the `tool_def.py` file in the same directory as this notebook for the imports to work correctly.
```python PYTHON
from tool_def import (
    analyze_evaluation_results,
    analyze_evaluation_results_tool,
)
```
```python PYTHON
functions_map = {
    "analyze_evaluation_results": analyze_evaluation_results
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
