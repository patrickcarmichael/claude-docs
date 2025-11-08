---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print the results for each detected violation

for violation in response_obj['violations']:
    print(f"""Comment: {user_comments[violation['id']]}
Violated Categories: {', '.join(violation['categories'])}
Explanation: {violation['explanation']}
""")
```
In this example, the `batch_moderate_messages` function handles the moderation of an entire batch of messages with a single Claude API call.
Inside the function, a prompt is created that includes the list of messages to evaluate, the defined unsafe content categories, and their descriptions. The prompt directs Claude to return a JSON object listing all messages that contain violations. Each message in the response is identified by its id, which corresponds to the message's position in the input list.
Keep in mind that finding the optimal batch size for your specific needs may require some experimentation. While larger batch sizes can lower costs, they might also lead to a slight decrease in quality. Additionally, you may need to increase the `max_tokens` parameter in the Claude API call to accommodate longer responses. For details on the maximum number of tokens your chosen model can output, refer to the [model comparison page](/en/docs/about-claude/models#model-comparison-table).

<CardGroup cols={2}>
  <Card title="Content moderation cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fmoderation%5Ffilter.ipynb">
    View a fully implemented code-based example of how to use Claude for content moderation.
  </Card>

  <Card title="Guardrails guide" icon="link" href="/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations">
    Explore our guardrails guide for techniques to moderate interactions with Claude.
  </Card>
</CardGroup>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
