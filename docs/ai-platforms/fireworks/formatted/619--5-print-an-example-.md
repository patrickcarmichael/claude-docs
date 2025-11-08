---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 5. Print an Example ---

if ground_truth_results:
    print("\n--- Example ground_truth_results dataset entry ---")
    print(json.dumps(ground_truth_results[0], indent=2))
```

### 8. 💬 Generate Natural Language Questions for Final RFT Training Data

We now have pairs of `(SQL Query, Ground-Truth Result)`. The final piece missing from our training data is the user's input: a question in natural language. This is because our final goal is to use RFT to tune an LLM to map from a natural language question to a SQL query, having the reward signal be the actual result of the query, rather than just the query itself. This is important because there are many ways to write the same SQL query that yield the same, correct result.

#### Thus, the complete training loop will look like this:

1. User asks: *"Which countries have the most airlines?"*
2. Model generates: *SQL query*
3. System executes: *Query against database*
4. Reward calculation: *Does result match ground truth?*
5. Model update: *Reinforce successful strategies*

Thus, we will use an LLM once again to translate our "historical" SQL queries into plausible questions a business user might ask, corresponding to that query. This will yield our final training dataset in the format: `(Natural Language Question, SQL Query, Ground-Truth Result)`. Note that the SQL queries themselves will not be used as part of the RFT job itself, but are useful for debugging our evaluation function (more details in a later section).

>   **Real World 🌍**: You might not need this step! If you have logs that already link user questions to the queries they ran (e.g., from a BI tool's search bar), you can use those directly. If not, this LLM-based translation is a powerful technique to bootstrap your training data.
```python
import json
import time
import jsonlines
from typing import List
import random
from fireworks import LLM
import os

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
