---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 6. REPORT RESULTS ---

if dataset:
    total = len(dataset)
    base_accuracy = (base_model_score / total) * 100
    large_base_accuracy = (large_base_model_score / total) * 100
    tuned_accuracy = (fine_tuned_model_score / total) * 100

    print("\n" + "="*25)
    print("  EVALUATION COMPLETE")
    print("="*25)
    print(f"Total Examples: {total}\n")
    print("--- BASE MODEL ---")
    print(f"Model ID: {BASE_MODEL_ID}")
    print(f"Correct: {base_model_score}/{total}")
    print(f"Accuracy: {base_accuracy:.2f}%\n")

    print("--- LARGE BASE MODEL ---")
    print(f"Model ID: {LARGE_BASE_MODEL_ID}")
    print(f"Correct: {large_base_model_score}/{total}")
    print(f"Accuracy: {large_base_accuracy:.2f}%\n")

    print("--- FINE-TUNED MODEL ---")
    print(f"Model ID: {FINE_TUNED_MODEL_ID}")
    print(f"Correct: {fine_tuned_model_score}/{total}")
    print(f"Accuracy: {tuned_accuracy:.2f}%\n")
    
    print("="*25)
    print("  PERFORMANCE LIFT")
    print("="*25)
    print(f"Fine-Tuned vs. Base: {tuned_accuracy - base_accuracy:+.2f}%")
    print(f"Fine-Tuned vs. Large Base: {tuned_accuracy - large_base_accuracy:+.2f}%")

else:
    print("Evaluation skipped because the dataset or LLM objects could not be loaded.")
```
```text
    LLM objects for all three models created successfully.
    Loaded 92 evaluation examples from 'data/final_rft_sql_test_data.jsonl'.
    
    Starting evaluation...


    Evaluating models:   0%|          | 0/92 [00:00<?, ?it/s]
      result = func(*args, **kwargs)
    Evaluating models: 100%|██████████| 92/92 [14:41<00:00,  9.59s/it]  

    
    =========================
      EVALUATION COMPLETE
    =========================
    Total Examples: 92
    
    --- BASE MODEL ---
    Model ID: accounts/fireworks/models/qwen2p5-7b
    Correct: 22/92
    Accuracy: 23.91%
    
    --- LARGE BASE MODEL ---
    Model ID: accounts/fireworks/models/qwen3-coder-480b-a35b-instruct
    Correct: 32/92
    Accuracy: 34.78%
    
    --- FINE-TUNED MODEL ---
    Model ID: accounts/<account-id>/models/<base-model-id>
    Correct: 52/92
    Accuracy: 56.52%
    
    =========================
      PERFORMANCE LIFT
    =========================
    Fine-Tuned vs. Base: +32.61%
    Fine-Tuned vs. Large Base: +21.74%
```

### 16. ✨ Cleanup & Conclusion

Congratulations! You've successfully completed the entire Reinforcement Fine-Tuning loop. You started with just a database schema and ended with a highly specialized, performant, and data-aware AI model.

#### Cleanup

Cloud resources and model deployments can incur costs, so it's good practice to clean up any resources you no longer need.

* **Check your Deployments:** Navigate to the [Deployments tab](https://app.fireworks.ai/dashboard/deployments) in your Fireworks AI dashboard. Here you can monitor and manage all your deployed models.
* **Delete Unneeded Models:** Feel free to delete any deployments you no longer need. For example, you might have deployed the base or large-base models during the evaluation step to compare against your fine-tuned model. These can now be safely removed to save costs.
* **Delete Cloud Run service and container image:** Feel free to delete your MCP server Cloud Run service and container image to avoid stray storage costs.

You can, of course, continue using your new fine-tuned SQL generation model for any application you see fit!

#### Conclusions

The evaluation results from the previous step highlight the power of this approach.

* **Performance on par with massive models:** Our fine-tuned 7B parameter model performs better than a much larger model like `qwen3-coder-480b-a35b-instruct` on this specific dataset. This is because it has been fine-tuned to understand the data schema via real query generation and execution.
* **Efficiency Gains:** A 7B model is significantly faster and cheaper to run than a 480B one, offering production-grade performance at a fraction of the cost and latency.
* **High-Level Capability on Complex Tasks:** The queries in this dataset are relatively complex, which is reflected in the final accuracy score of around 57%. This is a strong result, demonstrating that for a specialized domain, a smaller model can be tuned to achieve a level of performance that exceeds larger models like `qwen3-coder-480b-a35b-instruct`. Specifically, the final accuracy scores we measured for this dataset were:
  * Qwen2.5 7B (base): **23.91%** accuracy (**22/92** correct on the held-out test set)
  * Qwen3 Coder 480B A35B Instruct (base): **34.78%** accuracy (**32/92** correct on the held-out test set)
  * Qwen2.5 7B (RFT tuned): **56.52%** accuracy (**52/92** correct on the held-out test set)

***

Throughout this tutorial, we demonstrated a complete, end-to-end workflow for creating a fine-tuned text-to-SQL model. We began with the absolute minimum requirement, a database schema, and used a series of LLM-driven steps to generate a safe, synthetic data sandbox. From there, we generated a rich dataset of queries and answers, which we used to fine-tune a model using the Fireworks RFT platform. The final result is a small, efficient model that can accurately query data it has never seen, a task that was previously only possible with vastly larger and more expensive models.

This pattern of **schema → synthetic data → RFT** is a secure, effective, and repeatable methodology for teaching language models to become expert users of your private data and custom APIs, without ever exposing the underlying sensitive information.

### Appendix

#### Testing more open models on Fireworks

```python
import requests
import json
import os
import time
import datetime
from fireworks import LLM
from tqdm.auto import tqdm
from dotenv import load_dotenv

load_dotenv()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
