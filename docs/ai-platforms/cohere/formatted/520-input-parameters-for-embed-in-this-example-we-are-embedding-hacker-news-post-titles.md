---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Input parameters for embed. In this example we are embedding hacker news post titles.

texts = [
    "Interesting (Non software) books?",
    "Non-tech books that have helped you grow professionally?",
    "I sold my company last month for $5m. What do I do with the money?",
    "How are you getting through (and back from) burning out?",
    "I made $24k over the last month. Now what?",
    "What kind of personal financial investment do you do?",
    "Should I quit the field of software development?",
]
input_type = "clustering"
truncate = "NONE"  # optional

model_id = "<YOUR ENDPOINT NAME>"  # On SageMaker, you create a model name that you'll pass here.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
