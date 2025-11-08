---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```
```
"Hi, I'm [Your Name] and I'm thrilled to join the Co1t team today as a [Your Role], eager to contribute my skills and ideas to help drive innovation and success for our startup!"
```
Often, you’ll need to control the level of randomness of the output. You can control this using a few parameters.

The most commonly used parameter is `temperature`, which is a number used to tune the degree of randomness. You can enter values between 0.0 to 1.0.

A lower temperature gives more predictable outputs, and a higher temperature gives more "creative" outputs.

Here's an example of setting `temperature` to 0.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
