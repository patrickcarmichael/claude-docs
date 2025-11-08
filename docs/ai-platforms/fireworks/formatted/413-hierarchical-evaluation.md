---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hierarchical Evaluation

Create reward functions with hierarchical evaluation:
```python
@reward_function
def hierarchical_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Hierarchical evaluation with multiple levels of assessment.
    """
    # Level 1: Basic format validation

    if not basic_format_check(response):
        return 0.0

    # Level 2: Content relevance

    relevance_score = content_relevance(response, expected_response)
    if relevance_score < 0.3:
        return relevance_score * 0.5  # Cap low relevance scores

    # Level 3: Detailed accuracy

    accuracy_score = detailed_accuracy(response, expected_response)

    # Level 4: Style and presentation

    style_score = evaluate_style(response)

    # Weighted combination based on hierarchy

    final_score = (
        0.1 * 1.0 +  # Format passed

        0.3 * relevance_score +
        0.5 * accuracy_score +
        0.1 * style_score
    )

    return final_score

def basic_format_check(response: str) -> bool:
    """Basic format validation."""
    return len(response.strip()) > 0 and len(response) < 10000

def content_relevance(response: str, expected: str) -> float:
    """Evaluate content relevance."""
    # Placeholder for semantic similarity

    common_words = set(response.lower().split()) & set(expected.lower().split())
    return len(common_words) / max(len(set(expected.lower().split())), 1)

def detailed_accuracy(response: str, expected: str) -> float:
    """Detailed accuracy evaluation."""
    return accuracy(response, expected)

def evaluate_style(response: str) -> float:
    """Evaluate writing style and presentation."""
    score = 0.0
    if response[0].isupper():  # Starts with capital

        score += 0.3
    if response.endswith('.'):  # Ends with period

        score += 0.3
    if 10 <= len(response.split()) <= 100:  # Appropriate length

        score += 0.4
    return score
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
