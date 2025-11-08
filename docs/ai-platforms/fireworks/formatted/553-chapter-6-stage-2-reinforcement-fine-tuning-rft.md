---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chapter 6: Stage 2 - Reinforcement Fine-Tuning (RFT)

Now that our model consistently uses the `[WORK]` and `[RESULT]` format **automatically** (without being told), we can apply RFT to improve the accuracy of answers within that structure.

### Why Add Reinforcement Learning

**Beyond Imitation**: While SFT teaches the model to mimic the teacher's style, RFT optimizes for **correctness**. The model learns to:

* Prefer reasoning paths that lead to correct answers
* Self-correct when making mistakes
* Develop confidence in its mathematical reasoning

**How RFT Works**: Instead of just copying teacher responses, RFT gives the model a reward (+1) for correct answers and penalty (0) for wrong answers, encouraging the model to find its own path to the right solution.

**RFT Advantages with SFT Foundation**:

* Easy reward calculation from `[RESULT]` tags
* Maintains learned formatting while optimizing correctness

### Creating the RFT Dataset

**Strategy**: Reuse the same problems our teacher model solved correctly during SFT generation, but format them for reinforcement learning.
```python
def create_rft_dataset_from_sft(sft_training_data, max_samples=1000):
    """
    Create RFT dataset by extracting problems from existing SFT dataset
    """

    rft_data = []
    problems_processed = 0

    for sft_example in sft_training_data:
        if problems_processed >= max_samples:
            break

        user_question = None
        teacher_response = None

        # Extract user question and teacher response from messages

        for message in sft_example["messages"]:
            if message["role"] == "user":
                user_question = message["content"]
            elif message["role"] == "assistant":
                teacher_response = message["content"]

        if user_question and teacher_response:
            # Extract ground truth from teacher's [RESULT] tags

            ground_truth = extract_answer_from_result_tags(teacher_response)

            if ground_truth:
                rft_example = {
                    "messages": [
                        {"role": "user", "content": user_question}
                    ],
                    "ground_truth": ground_truth
                }
                rft_data.append(rft_example)
                problems_processed += 1
    return rft_data

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
