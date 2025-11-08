---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## List of categories considered unsafe for content moderation

unsafe_categories = [
    'Child Exploitation',
    'Conspiracy Theories',
    'Hate',
    'Indiscriminate Weapons', 
    'Intellectual Property',
    'Non-Violent Crimes', 
    'Privacy',
    'Self-Harm',
    'Sex Crimes',
    'Sexual Content',
    'Specialized Advice',
    'Violent Crimes'
]
```
Effectively moderating these examples requires a nuanced understanding of language. In the comment, `This movie was great, I really enjoyed it. The main actor really killed it!`, the content moderation system needs to recognize that "killed it" is a metaphor, not an indication of actual violence. Conversely, despite the lack of explicit mentions of violence, the comment `Delete this post now or you better hide. I am coming after you and your family.` should be flagged by the content moderation system.

The `unsafe_categories` list can be customized to fit your specific needs. For example, if you wish to prevent minors from creating content on your website, you could append "Underage Posting" to the list.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
