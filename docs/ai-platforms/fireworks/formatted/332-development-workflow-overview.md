---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Development Workflow Overview

The typical workflow involves:

1. **Dataset Configuration**: Defining how your data is loaded and prepared (see [Dataset Configuration Guide](/evaluators/developer_guide/dataset_configuration_guide)).
2. **Reward Function Implementation**: Writing the logic to evaluate model responses.
3. **Local Evaluation (using `reward-kit run`)**: Running evaluations locally using Hydra-based configurations to generate responses and score them.
4. **Previewing Results (using `reward-kit preview`)**: Inspecting or re-evaluating generated outputs.
5. **Deployment**: Making the reward function or evaluator available as a service.
6. **Integration**: Using the deployed evaluator in RLHF training or other workflows.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
