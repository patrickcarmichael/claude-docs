---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## If the endpoint is already deployed, you can directly connect to it

co.sagemaker_finetuning.connect_to_endpoint(
    endpoint_name=endpoint_name
)

message = "Classify the following text as either very negative, negative, neutral, positive or very positive: mr. deeds is , as comedy goes , very silly -- and in the best way."
result = co.sagemaker_finetuning.chat(message=message)
print(result)
```
You can also evaluate your finetuned model using a evaluation dataset. The following is an example with the [ScienceQA](https://scienceqa.github.io/) evaluation data at [here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/data/scienceQA_eval.jsonl).
```python
import json
from tqdm import tqdm

eval_data_path = "<path_to_scienceQA_eval.jsonl>"

total = 0
correct = 0
for line in tqdm(open(eval_data_path).readlines()):
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
<a name="delete" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
