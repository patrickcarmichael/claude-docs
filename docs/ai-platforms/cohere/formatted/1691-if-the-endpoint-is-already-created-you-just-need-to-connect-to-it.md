---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## If the endpoint is already created, you just need to connect to it

co.connect_to_endpoint(endpoint_name=endpoint_name)
```

### B. Perform real-time inference

Now, you can access all models deployed on the endpoint for inference:
```python
message = "Classify the following text as either very negative, negative, neutral, positive or very positive: mr. deeds is , as comedy goes , very silly -- and in the best way."

result = co.sagemaker_finetuning.chat(message=message)
print(result)
```

#### \[Optional] Now let's evaluate our finetuned model using the evaluation dataset.

```python
import json
from tqdm import tqdm

total = 0
correct = 0
for line in tqdm(
    open("./sample_finetune_scienceQA_eval.jsonl").readlines()
):
    total += 1
    question_answer_json = json.loads(line)
    question = question_answer_json["messages"][0]["content"]
    answer = question_answer_json["messages"][1]["content"]
    model_ans = co.sagemaker_finetuning.chat(
        message=question, temperature=0
    ).text
    if model_ans == answer:
        correct += 1

print(f"Accuracy of finetuned model is %.3f" % (correct / total))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
