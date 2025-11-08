---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Process each comment and print the results

for comment in user_comments:
    print(f"\nComment: {comment}")
    risk_level, violated_categories, explanation = assess_risk_level(comment, unsafe_categories)
    
    print(f"Risk Level: {risk_level}")
    if violated_categories:
        print(f"Violated Categories: {', '.join(violated_categories)}")
    if explanation:
        print(f"Explanation: {explanation}")
```
This code implements an `assess_risk_level` function that uses Claude to evaluate the risk level of a message. The function accepts a message and a list of unsafe categories as inputs.

Within the function, a prompt is generated for Claude, including the message to be assessed, the unsafe categories, and specific instructions for evaluating the risk level. The prompt instructs Claude to respond with a JSON object that includes the risk level, the violated categories, and an optional explanation.

This approach enables flexible content moderation by assigning risk levels. It can be seamlessly integrated into a larger system to automate content filtering or flag comments for human review based on their assessed risk level. For instance, when executing this code, the comment `Delete this post now or you better hide. I am coming after you and your family.` is identified as high risk due to its dangerous threat. Conversely, the comment `Stay away from the 5G cellphones!! They are using 5G to control you.` is categorized as medium risk.

### Deploy your prompt

Once you are confident in the quality of your solution, it's time to deploy it to production. Here are some best practices to follow when using content moderation in production:

1. **Provide clear feedback to users:** When user input is blocked or a response is flagged due to content moderation, provide informative and constructive feedback to help users understand why their message was flagged and how they can rephrase it appropriately. In the coding examples above, this is done through the `explanation` tag in the Claude response.

2. **Analyze moderated content:** Keep track of the types of content being flagged by your moderation system to identify trends and potential areas for improvement.

3. **Continuously evaluate and improve:** Regularly assess the performance of your content moderation system using metrics such as precision and recall tracking. Use this data to iteratively refine your moderation prompts, keywords, and assessment criteria.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
