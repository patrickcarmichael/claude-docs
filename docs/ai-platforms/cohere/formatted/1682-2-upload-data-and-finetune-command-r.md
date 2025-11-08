---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Upload data and finetune Command-R

Select a path on S3 to store the training and evaluation datasets and update the **s3\_data\_dir** below:
```python
s3_data_dir = "s3://..."  # Do not add a trailing slash otherwise the upload will not work

```
Upload sample training data to S3:

### Note:

You'll need your data in a .jsonl file that contains chat-formatted data. [Doc](https://docs.cohere.com/docs/chat-preparing-the-data#data-requirements)

### Example:

JSONL:
```
{
  "messages": [
    {
      "role": "System",
      "content": "You are a chatbot trained to answer to my every question."
    },
    {
      "role": "User",
      "content": "Hello"
    },
    {
      "role": "Chatbot",
      "content": "Greetings! How can I help you?"
    },
    {
      "role": "User",
      "content": "What makes a good running route?"
    },
    {
      "role": "Chatbot",
      "content": "A sidewalk-lined road is ideal so that you\u2019re up and off the road away from vehicular traffic."
    }
  ]
}
```
```python
sess = sage.Session()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
