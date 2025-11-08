---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define whether to use Claude for ticket routing

Here are some key indicators that you should use an LLM like Claude  instead of traditional ML approaches for your classification task:

<AccordionGroup>
  <Accordion title="You have limited labeled training data available">
    Traditional ML processes require massive labeled datasets. Claude's pre-trained model can effectively classify tickets with just a few dozen labeled examples, significantly reducing data preparation time and costs.
  </Accordion>

  <Accordion title="Your classification categories are likely to change or evolve over time">
    Once a traditional ML approach has been established, changing it is a laborious and data-intensive undertaking. On the other hand, as your product or customer needs evolve, Claude can easily adapt to changes in class definitions or new classes without extensive relabeling of training data.
  </Accordion>

  <Accordion title="You need to handle complex, unstructured text inputs">
    Traditional ML models often struggle with unstructured data and require extensive feature engineering. Claude's advanced language understanding allows for accurate classification based on content and context, rather than relying on strict ontological structures.
  </Accordion>

  <Accordion title="Your classification rules are based on semantic understanding">
    Traditional ML approaches often rely on bag-of-words models or simple pattern matching. Claude excels at understanding and applying underlying rules when classes are defined by conditions rather than examples.
  </Accordion>

  <Accordion title="You require interpretable reasoning for classification decisions">
    Many traditional ML models provide little insight into their decision-making process. Claude can provide human-readable explanations for its classification decisions, building trust in the automation system and facilitating easy adaptation if needed.
  </Accordion>

  <Accordion title="You want to handle edge cases and ambiguous tickets more effectively">
    Traditional ML systems often struggle with outliers and ambiguous inputs, frequently misclassifying them or defaulting to a catch-all category. Claude's natural language processing capabilities allow it to better interpret context and nuance in support tickets, potentially reducing the number of misrouted or unclassified tickets that require manual intervention.
  </Accordion>

  <Accordion title="You need multilingual support without maintaining separate models">
    Traditional ML approaches typically require separate models or extensive translation processes for each supported language. Claude's multilingual capabilities allow it to classify tickets in various languages without the need for separate models or extensive translation processes, streamlining support for global customer bases.
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
