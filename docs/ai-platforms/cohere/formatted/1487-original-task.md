---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Original Task

{original_prompt}
'''
```
```python PYTHON
print(meta_prompt)
```
```txt title="Output"
Below is a task for an LLM delimited with ## Original Task. Your task is to split that task into two parts: (1) the context; and (2) the instructions.

The context should be split into several separate parts and returned as a JSON object where each part has a name describing its contents and the value is the contents itself.
Make sure to include all of the context contained in the original task description and do not change its meaning.
The instructions should be re-written so that they are very clear and concise. Do not change the meaning of the instructions or task, just make sure they are very direct and clear.
Return everything in a JSON object with the following structure:

{
    "context": [{"<description 1="" of="" part="">": "<content 1="" of="" part="">"}, ...],
    "instructions": "<the instructions="" re-written="">"
}

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
