---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setting up a tool to interact with tabular data

Next, we define the `analyze_evaluation_results` tool. There are many ways we can set up a tool to work with CSV data, and in this example, we are using the tool description to provide the agent with the necessary context for working with the CSV file, such as:

* the name of the CSV file to load
* the columns of the CSV file
* additional instructions on what libraries to use (in this case, `pandas`)

The parameter of this tool is the `code` string containing the Python code that the agent writes to analyze the data.
```python PYTHON
analyze_evaluation_results_tool = {
    "type": "function",
    "function": {
        "name": "analyze_evaluation_results",
        "description": "Generate Python code using the pandas library to analyze evaluation results from a dataframe called `evaluation_results`. The dataframe has columns 'usecase','run','score','temperature','tokens', and 'latency'. You must start with `import pandas as pd` and read a CSV file called `evaluation_results.csv` into the `evaluation_results` dataframe.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Executable Python code",
                }
            },
            "required": ["code"],
        },
    },
}
```
```python PYTHON
tools = [analyze_evaluation_results_tool]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
