---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Style Guide

Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling
"""  # noqa E501

```

### Define tools necessary for the agent

The below cell introduces a suite of tools that are provided to the csv agent. These tools allow the agent to fcilitate meaningful interactions with uploaded files and providing Python code execution functionality. The toolkit comprises three main components:

**File Peek Tool**: Offers a convenient way to inspect a CSV file by providing a quick preview of the first few rows in a Markdown format, making it easy to get a glimpse of the data.

**File Read Tool**: Allows for a comprehensive exploration of the CSV file by reading and presenting its full contents in a user-friendly Markdown format.

**Python Interpreter Tool**: Enables secure execution of Python code within a sandboxed environment, providing users with the output of the code execution.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
