---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response multiple times by specifying a low temperature value

for idx in range(3):
    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": message}],
        temperature=1,
    )

    print(f"{idx+1}: {response.message.content[0].text}\n")
```
```
1: Here is a suggestion: 

"Revolution Enthusiast. History Fan." 

This introduction highlights your passion for the industrial revolution and its impact on history while keeping within the word limit.

2: "Revolution fan."

3: "IR enthusiast."
```
Further reading:

* [Available models for the Chat endpoint](https://docs.cohere.com/docs/models#command)
* [Documentation on predictable outputs](https://docs.cohere.com/v2/docs/predictable-outputs)
* [Documentation on advanced generation parameters](https://docs.cohere.com/docs/advanced-generation-hyperparameters)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
