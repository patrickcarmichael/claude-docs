---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get first 10 rows as a new dataset

first_10_dataset = dataset.head(10, as_dataset=True)
```

### `create_evaluation_job(reward_function: Callable, samples: Optional[int] = None)`

Creates an evaluation job using a reward function for this dataset.

**Arguments:**

* `reward_function` *Callable* - A callable decorated with @reward\_function
* `samples` *int, optional* - Optional number of samples to evaluate (creates a subset dataset)

**Returns:**

* *EvaluationJob* - The created evaluation job
```python
from fireworks import reward_function

@reward_function
def my_reward_function(response, context):
    # Your reward logic here

    return 1.0

evaluation_job = dataset.create_evaluation_job(my_reward_function, samples=100)
```

### `preview_evaluator(reward_function: Callable, samples: Optional[int] = None)`

Previews the evaluator for the dataset.

**Arguments:**

* `reward_function` *Callable* - A callable decorated with @reward\_function
* `samples` *int, optional* - Optional number of samples to preview

**Returns:**

* *SyncPreviewEvaluatorResponse* - Preview response from the evaluator
```python
preview_response = dataset.preview_evaluator(my_reward_function, samples=10)
```

### Data Format

The Dataset class expects data in OpenAI's chat completion format. Each training example should be a JSON object with a `messages` array containing message objects. Each message object should have:

* `role`: One of `"system"`, `"user"`, or `"assistant"`
* `content`: The message content as a string

Example format:
```json
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris."}
    ]
}
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
