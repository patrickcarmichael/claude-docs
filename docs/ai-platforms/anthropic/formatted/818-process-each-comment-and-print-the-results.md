---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Process each comment and print the results

for comment in user_comments:
    print(f"\nComment: {comment}")
    violation, violated_categories, explanation = moderate_message(comment, unsafe_categories)
    
    if violation:
        print(f"Violated Categories: {', '.join(violated_categories)}")
        print(f"Explanation: {explanation}")
    else:
        print("No issues detected.")
```
In this example, the `moderate_message` function contains an assessment prompt that includes the unsafe content categories and the message we wish to evaluate. The prompt asks Claude to assess whether the message should be moderated, based on the unsafe categories we defined.

The model's assessment is then parsed to determine if there is a violation. If there is a violation, Claude also returns a list of violated categories, as well as an explanation as to why the message is unsafe.

### Evaluate your prompt

Content moderation is a classification problem. Thus, you can use the same techniques outlined in our [classification cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb) to determine the accuracy of your content moderation system.

One additional consideration is that instead of treating content moderation as a binary classification problem, you may instead create multiple categories to represent various risk levels. Creating multiple risk levels allows you to adjust the aggressiveness of your moderation. For example, you might want to automatically block user queries that are deemed high risk, while users with many medium risk queries are flagged for human review.
```python
import anthropic
import json

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
