---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building strong criteria

Good success criteria are:

* **Specific**: Clearly define what you want to achieve. Instead of "good performance," specify "accurate sentiment classification."
* **Measurable**: Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied *along* with quantitative measures.

  * Even "hazy" topics such as ethics and safety can be quantified:
    |      | Safety criteria                                                                            |
    | ---- | ------------------------------------------------------------------------------------------ |
    | Bad  | Safe outputs                                                                               |
    | Good | Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter. |

  <Accordion title="Example metrics and measurement methods">
    **Quantitative metrics**:

    * Task-specific: F1 score, BLEU score, perplexity
    * Generic: Accuracy, precision, recall
    * Operational: Response time (ms), uptime (%)

    **Quantitative methods**:

    * A/B testing: Compare performance against a baseline model or earlier version.
    * User feedback: Implicit measures like task completion rates.
    * Edge case analysis: Percentage of edge cases handled without errors.

    **Qualitative scales**:

    * Likert scales: "Rate coherence from 1 (nonsensical) to 5 (perfectly logical)"
    * Expert rubrics: Linguists rating translation quality on defined criteria
  </Accordion>
* **Achievable**: Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.
* **Relevant**: Align your criteria with your application's purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.

<Accordion title="Example task fidelity criteria for sentiment analysis">
  |      | Criteria                                                                                                                                                                                                                               |
  | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Bad  | The model should classify sentiments well                                                                                                                                                                                              |
  | Good | Our sentiment analysis model should achieve an F1 score of at least 0.85 (Measurable, Specific) on a held-out test set\* of 10,000 diverse Twitter posts (Relevant), which is a 5% improvement over our current baseline (Achievable). |

  \**More on held-out test sets in the next section*
</Accordion>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
