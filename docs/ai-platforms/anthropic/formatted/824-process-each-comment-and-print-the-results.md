---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Process each comment and print the results

for comment in user_comments:
    print(f"\nComment: {comment}")
    violation, violated_categories, explanation = moderate_message_with_definitions(comment, unsafe_category_definitions)
    
    if violation:
        print(f"Violated Categories: {', '.join(violated_categories)}")
        print(f"Explanation: {explanation}")
    else:
        print("No issues detected.")
```
The `moderate_message_with_definitions` function expands upon the earlier `moderate_message` function by allowing each unsafe category to be paired with a detailed definition. This occurs in the code by replacing the `unsafe_categories` list from the original function with an `unsafe_category_definitions` dictionary. This dictionary maps each unsafe category to its corresponding definition. Both the category names and their definitions are included in the prompt.

Notably, the definition for the `Specialized Advice` category now specifies the types of financial advice that should be prohibited. As a result, the comment `It's a great time to invest in gold!`, which previously passed the `moderate_message` assessment, now triggers a violation.

### Consider batch processing

To reduce costs in situations where real-time moderation isn't necessary, consider moderating messages in batches. Include multiple messages within the prompt's context, and ask Claude to assess which messages should be moderated.
```python
import anthropic
import json

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
