---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-Metric Evaluation

Combine multiple evaluation criteria:
```python
from reward_kit import reward_function
from reward_kit.rewards import accuracy, length, format_compliance
import numpy as np

@reward_function
def multi_metric_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Advanced reward function combining accuracy, length, and format compliance.
    """
    # Base accuracy score

    acc_score = accuracy(response, expected_response)

    # Length appropriateness (prefer responses between 50-200 chars)

    len_score = length_appropriateness(response, min_len=50, max_len=200)

    # Format compliance (if response should follow a pattern)

    format_score = check_format_compliance(response)

    # Weighted combination

    weights = [0.6, 0.2, 0.2]  # accuracy, length, format

    scores = [acc_score, len_score, format_score]

    return np.average(scores, weights=weights)

def length_appropriateness(response: str, min_len: int, max_len: int) -> float:
    """Helper function to score length appropriateness."""
    length = len(response)
    if min_len <= length <= max_len:
        return 1.0
    elif length < min_len:
        return max(0.0, length / min_len)
    else:
        return max(0.0, 1.0 - (length - max_len) / max_len)

def check_format_compliance(response: str) -> float:
    """Helper function to check format compliance."""
    # Example: Check if response follows expected structure

    if response.startswith("Answer:") and response.endswith("."):
        return 1.0
    return 0.5
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
