---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## QnA over Multiple Tables \[#qna\_over\_multiple\_tables]

We now make the task for the Agent more complicated by asking a question that can be only answered by retrieving relevant information from multiple tables:

* Q: What is the ratio of the largest stockholders equity to the smallest revenue?

As you will see below, this question can be obtained only by accessing both the balance sheet and the income statement.
```python PYTHON
question_dict ={
    'q1': ['what is the ratio of the largest stockholders equity to the smallest revenue'],
}
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
