---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data Preparation

Your dataset should contain examples with:

* An `input` field with messages in in the [conversational format](/docs/fine-tuning-data-preparation#conversational-data).
* A `preferred_output` field with the ideal assistant response
* A `non_preferred_output` field with a suboptimal assistant response

Both outputs must contain exactly one message from the assistant role.

Format your data in `JSONL`, with each line structured as:
```json
  {
    "input": {
      "messages": [
        {
          "role": "assistant",
          "content": "Hello, how can I assist you today?"
        },
        {
          "role": "user",
          "content": "Can you tell me about the rise of the Roman Empire?"
        }
      ]
    },
    "preferred_output": [
      {
        "role": "assistant",
        "content": "The Roman Empire rose from a small city-state founded in 753 BCE. Through military conquests and strategic alliances, Rome expanded across the Italian peninsula. After the Punic Wars, it grew even stronger, and in 27 BCE, Augustus became the first emperor, marking the start of the Roman Empire. This led to a period of peace and prosperity known as the Pax Romana."
      }
    ],
    "non_preferred_output": [
      {
        "role": "assistant",
        "content": "The Roman Empire rose due to military strength and strategic alliances."
      }
    ]
  }
```

>   **📝 Note**
>
> Preference-tuning does not support pretokenized datasets. [Contact us](https://www.together.ai/contact) if you need to use them for preference training.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
