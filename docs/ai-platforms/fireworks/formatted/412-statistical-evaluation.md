---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Statistical Evaluation

Use statistical methods for more robust evaluation:
```python
from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

@reward_function
def statistical_similarity_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Uses statistical methods to evaluate response similarity.
    """
    # Convert to numerical representations (e.g., using embeddings)

    response_embedding = get_text_embedding(response)
    expected_embedding = get_text_embedding(expected_response)

    # Cosine similarity

    cos_sim = cosine_similarity([response_embedding], [expected_embedding])[0][0]

    # Pearson correlation (if applicable)

    if len(response_embedding) == len(expected_embedding):
        corr, _ = pearsonr(response_embedding, expected_embedding)
        corr = max(0, corr)  # Only positive correlations

    else:
        corr = 0

    # Combine metrics

    final_score = 0.7 * cos_sim + 0.3 * corr

    return max(0.0, min(1.0, final_score))

def get_text_embedding(text: str) -> np.ndarray:
    """Placeholder for text embedding function."""
    # In practice, use a real embedding model

    return np.random.rand(100)  # Placeholder

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
