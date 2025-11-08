---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the documents

emails = [
    {
        "from": "hr@co1t.com",
        "to": "david@co1t.com",
        "date": "2024-06-24",
        "subject": "A Warm Welcome to Co1t!",
        "text": "We are delighted to welcome you to the team! As you embark on your journey with us, you'll find attached an agenda to guide you through your first week.",
    },
    {
        "from": "it@co1t.com",
        "to": "david@co1t.com",
        "date": "2024-06-24",
        "subject": "Setting Up Your IT Needs",
        "text": "Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.",
    },
    {
        "from": "john@co1t.com",
        "to": "david@co1t.com",
        "date": "2024-06-24",
        "subject": "First Week Check-In",
        "text": "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!",
    },
]

yaml_emails = [yaml.dump(doc, sort_keys=False) for doc in emails]
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
