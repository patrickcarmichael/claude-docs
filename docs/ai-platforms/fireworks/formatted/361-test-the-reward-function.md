---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Test the reward function

result = word_count_reward(messages=test_messages)
print(f"Score: {result.score}")
print(f"Explanation: {result.metrics['word_count'].reason}")
```

### Local Evaluation with `reward-kit run` (Recommended for datasets/examples)

For evaluating datasets or running complete examples, the primary method is the `reward-kit run` CLI command. This uses [Hydra for configuration](/evaluators/developer_guide/hydra_configuration), allowing you to define your dataset, model, and reward logic in YAML files.

1. **Explore Examples**: Check out the examples in the `examples/` directory at the root of the repository. The [main Examples README](https://github.com/fw-ai-external/reward-kit/blob/main/examples/README.md) provides an overview and guidance on their structure. Each example (e.g., `examples/math_example/`) has its own README explaining how to run it.

2. **Run an Example**:
```bash
   # Example: Running the math_example

   python -m reward_kit.cli run \
     --config-path examples/math_example/conf \
     --config-name run_math_eval.yaml
```
   This command processes the dataset, generates model responses, applies reward functions, and saves detailed results.

### Previewing Evaluation Outputs with `reward-kit preview`

After running an evaluation with `reward-kit run`, a `preview_input_output_pairs.jsonl` file is typically generated in the output directory. You can use `reward-kit preview` to inspect these pairs or re-evaluate them with different metrics:
```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
