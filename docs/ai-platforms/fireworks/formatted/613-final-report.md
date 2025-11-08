---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Final report

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con_read:
    final_zero_indices = [i for i, q in enumerate(queries) if count_rows(con_read, q) == 0]
    final_zero_count = len(final_zero_indices)
    final_zero_percent = (final_zero_count / total_q * 100) if total_q else 0
    
    print(f"\n{'='*60}")
    print(f"AUGMENTATION COMPLETE")
    print(f"{'='*60}")
    print(f"Initial zero-result: {initial_zero_count}/{total_q} ({initial_zero_count/total_q*100:.1f}%)")
    print(f"Final zero-result:   {final_zero_count}/{total_q} ({final_zero_percent:.1f}%)")
    print(f"Improvement:         {initial_zero_count - final_zero_count} queries now return results")
    
    if final_zero_percent <= TARGET_MAX_ZERO_PERCENT:
        print(f"\n✅ SUCCESS: Achieved target of ≤{TARGET_MAX_ZERO_PERCENT}% zero-result queries")
    else:
        print(f"\n⚠️  Partial success. Consider running again or adjusting parameters.")
        
    # Show a few examples of remaining zero-result queries if any

    if final_zero_count > 0 and final_zero_count <= 5:
        print(f"\nRemaining zero-result queries:")
        for idx in final_zero_indices[:5]:
            print(f"  [{idx}]: {queries[idx][:100]}...")
```

### 7. 🎯 Execute Queries to Get Ground-Truth Answers

Now we will act as the "system" and run the queries we just generated against our synthetic sandbox. The output of each query is the **ground-truth result**. During Reinforcement Fine-Tuning, our model will be rewarded if the SQL it writes produces this exact same result.

#### Why RFT is a good choice for a text-to-SQL use-case

In RFT, the model explores the space of possible SQL queries during fine-tuning; the reward signal comes from comparing the result of executing the model's output SQL queries against the ground truth expected results. This is fundamentally different from SFT, where the model learns to mimic the exact SQL syntax. With RFT:

* Multiple SQL queries can be "correct" if they produce the same result
* The model learns to reason about the problem rather than memorize solutions
* Edge cases and query optimization patterns can emerge naturally

>   **Real World 🌍**: You would run your real historical queries against the synthetic database we previously created. The correctness of the data is not a concern here, as our aim is to see what a correct query would have generated, so we can compare it to our LLM's generations during the RFT process.
```python
import duckdb
import json
import pandas as pd

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
