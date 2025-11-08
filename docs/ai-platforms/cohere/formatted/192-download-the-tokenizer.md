---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## download the tokenizer

tokenizer_url = (
    "https://..."  # use /models/<id> endpoint for latest URL

)

response = requests.get(tokenizer_url)
tokenizer = Tokenizer.from_str(response.text)

tokenizer.encode(sequence="...", add_special_tokens=False)
```
The URL for the tokenizer should be obtained dynamically by calling the [Models API](/reference/get-model). Here is a sample response for the Command R model:
```json JSON
{  
  "name": "command-a-03-2025",  
  ...
  "tokenizer_url": "https://storage.googleapis.com/cohere-public/tokenizers/command-a-03-2025.json"
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
