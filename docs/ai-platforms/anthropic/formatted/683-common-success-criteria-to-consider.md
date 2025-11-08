---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common success criteria to consider

Here are some criteria that might be important for your use case. This list is non-exhaustive.

<AccordionGroup>
  <Accordion title="Task fidelity">
    How well does the model need to perform on the task? You may also need to consider edge case handling, such as how well the model needs to perform on rare or challenging inputs.
  </Accordion>

  <Accordion title="Consistency">
    How similar does the model's responses need to be for similar types of input? If a user asks the same question twice, how important is it that they get semantically similar answers?
  </Accordion>

  <Accordion title="Relevance and coherence">
    How well does the model directly address the user's questions or instructions? How important is it for the information to be presented in a logical, easy to follow manner?
  </Accordion>

  <Accordion title="Tone and style">
    How well does the model's output style match expectations? How appropriate is its language for the target audience?
  </Accordion>

  <Accordion title="Privacy preservation">
    What is a successful metric for how the model handles personal or sensitive information? Can it follow instructions not to use or share certain details?
  </Accordion>

  <Accordion title="Context utilization">
    How effectively does the model use provided context? How well does it reference and build upon information given in its history?
  </Accordion>

  <Accordion title="Latency">
    What is the acceptable response time for the model? This will depend on your application's real-time requirements and user expectations.
  </Accordion>

  <Accordion title="Price">
    What is your budget for running the model? Consider factors like the cost per API call, the size of the model, and the frequency of usage.
  </Accordion>
</AccordionGroup>

Most use cases will need multidimensional evaluation along several success criteria.

<Accordion title="Example multidimensional criteria for sentiment analysis">
  |      | Criteria                                                                                                                                                                                                                                                                                   |
  | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | Bad  | The model should classify sentiments well                                                                                                                                                                                                                                                  |
  | Good | On a held-out test set of 10,000 diverse Twitter posts, our sentiment analysis model should achieve:<br />- an F1 score of at least 0.85<br />- 99.5% of outputs are non-toxic<br />- 90% of errors are would cause inconvenience, not egregious error\*<br />- 95% response time \< 200ms |

  \**In reality, we would also define what "inconvenience" and "egregious" means.*
</Accordion>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
