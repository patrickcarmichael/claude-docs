---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

* **Dataset**: A sample from `codeparrot/apps`, a dataset of programming problems and solutions. The specific dataset configuration used is `apps_full_prompts` (defined in `conf/dataset/apps_full_prompts.yaml`), which typically points to a pre-generated JSONL file.
* **Task**: Given a problem description (question), the model should generate a Python code solution.
* **Reward Function**: The evaluation uses `reward_kit.rewards.apps_coding_reward.evaluate_apps_solution`.
  * **Functionality**: In its current form for this example, this reward function performs a basic check to see if the generated Python code is parsable by Python's `ast.parse` module. It scores `1.0` if the code is parsable and `0.0` otherwise.
  * It does *not* execute the code or check for functional correctness against test cases in this simplified setup.
  * The `ground_truth_for_eval` field (derived from APPS' `input_output` field) is available to the reward function but not utilized by this initial parsability check.
* **System Prompt**: A default system prompt is provided in the configuration to guide the model:
```
  Please write a Python script that solves the following problem. Structure your solution within a main() function. Please read from stdin directly and make sure the code is not interactive. The main() function should print the final result(s) to standard output as required by the problem statement.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
