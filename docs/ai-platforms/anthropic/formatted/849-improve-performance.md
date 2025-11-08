---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/en/docs/build-with-claude/prompt-engineering/overview) & [guardrail implementation strategies](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). Here are some common scenarios:

### Use a taxonomic hierarchy for cases with 20+ intent categories

As the number of classes grows, the number of examples required also expands, potentially making the prompt unwieldy. As an alternative, you can consider implementing a hierarchical classification system using a mixture of classifiers.

1. Organize your intents in a taxonomic tree structure.
2. Create a series of classifiers at every level of the tree, enabling a cascading routing approach.

For example, you might have a top-level classifier that broadly categorizes tickets into "Technical Issues," "Billing Questions," and "General Inquiries." Each of these categories can then have its own sub-classifier to further refine the classification.

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=5289a8c92716a132311081bc9efed4fc" alt="" data-og-width="2998" width="2998" data-og-height="430" height="430" data-path="images/ticket-hierarchy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=6e2d5e710d722b23f00f43e14a9aa94c 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a6184c7df444a8c4bfbdbd7f5b46bb3e 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=31536d5d35e186e5cadf58d5b3657ce8 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=efc29d26d9808a8003c0bc66e7ac9ddb 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=4694bf9a36805541f14c2d33221a82ad 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=2ac2109b054a21342ae533e6098789d0 2500w" />

* **Pros - greater nuance and accuracy:** You can create different prompts for each parent path, allowing for more targeted and context-specific classification. This can lead to improved accuracy and more nuanced handling of customer requests.

* **Cons - increased latency:** Be advised that multiple classifiers can lead to increased latency, and we recommend implementing this approach with our fastest model, Haiku.

### Use vector databases and similarity search retrieval to handle highly variable tickets

Despite providing examples being the most effective way to improve performance, if support requests are highly variable, it can be hard to include enough examples in a single prompt.

In this scenario, you could employ a vector database to do similarity searches from a dataset of examples and retrieve the most relevant examples for a given query.

This approach, outlined in detail in our [classification recipe](https://github.com/anthropics/anthropic-cookbook/blob/82675c124e1344639b2a875aa9d3ae854709cd83/skills/classification/guide.ipynb), has been shown to improve performance from 71% accuracy to 93% accuracy.

### Account specifically for expected edge cases

Here are some scenarios where Claude may misclassify tickets (there may be others that are unique to your situation). In these scenarios,consider providing explicit instructions or examples in the prompt of how Claude should handle the edge case:

<AccordionGroup>
  <Accordion title="Customers make implicit requests">
    Customers often express needs indirectly. For example, "I've been waiting for my package for over two weeks now" may be an indirect request for order status.

    * **Solution:** Provide Claude with some real customer examples of these kinds of requests, along with what the underlying intent is. You can get even better results if you include a classification rationale for particularly nuanced ticket intents, so that Claude can better generalize the logic to other tickets.
  </Accordion>

  <Accordion title="Claude prioritizes emotion over intent">
    When customers express dissatisfaction, Claude may prioritize addressing the emotion over solving the underlying problem.

    * **Solution:** Provide Claude with directions on when to prioritize customer sentiment or not. It can be something as simple as “Ignore all customer emotions. Focus only on analyzing the intent of the customer’s request and what information the customer might be asking for.”
  </Accordion>

  <Accordion title="Multiple issues cause issue prioritization confusion">
    When customers present multiple issues in a single interaction, Claude may have difficulty identifying the primary concern.

    * **Solution:** Clarify the prioritization of intents so thatClaude can better rank the extracted intents and identify the primary concern.
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
