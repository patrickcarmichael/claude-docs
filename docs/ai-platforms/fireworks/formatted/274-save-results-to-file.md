---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Save results to file

reward-kit preview --metrics-folders "clarity=./my_metrics/clarity" --samples ./samples.jsonl --output ./results.json
```

### Sample File Format

The samples file should be a JSONL (JSON Lines) file. If it's the output from `reward-kit run` (`preview_input_output_pairs.jsonl`), each line typically contains a "messages" list (including system, user, and assistant turns) and optionally a "ground\_truth" field. If creating manually, a common format is:
```json
{"messages": [{"role": "user", "content": "What is machine learning?"}, {"role": "assistant", "content": "Machine learning is a method of data analysis..."}]}
```
Or, if you have ground truth for comparison:
```json
{"messages": [{"role": "user", "content": "Question..."}, {"role": "assistant", "content": "Model answer..."}], "ground_truth": "Reference answer..."}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
