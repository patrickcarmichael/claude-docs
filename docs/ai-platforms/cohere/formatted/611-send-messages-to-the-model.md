---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Send messages to the model

response = co.chat(
    model="command-a-03-2025",
    messages=[
        {"role": "system", "content": system_instruction},
        {
            "role": "user",
            "content": "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates.",
        },
    ],
)

print(response.message.content[0].text)
```
```
Sure, here's a rhyme to break the ice,
A warm welcome to the team, so nice,

Hi, I'm [Your Name], a new face,
Ready to join the Co1t space,

A journey begins, a path unknown,
But together we'll make our mark, a foundation stone,

Excited to learn and contribute my part,
Let's create, innovate, and leave a lasting art,

Looking forward to our adventures yet untold,
With teamwork and passion, let's achieve our goals!

Cheers to a great start!
Your enthusiastic new mate.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
