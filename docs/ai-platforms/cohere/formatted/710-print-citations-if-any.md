---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print citations (if any)

if response.message.citations:
    print("\nCITATIONS:")
    for citation in response.message.citations:
        print(citation, "\n")
```
```
Response:
Yes, there is an email from it@co1t.com with the subject 'Setting Up Your IT Needs'. It includes an attached guide to help you set up your work accounts.
==================================================

CITATIONS:
start=17 end=83 text="email from it@co1t.com with the subject 'Setting Up Your IT Needs'" sources=[ToolSource(type='tool', id='search_emails_wqs498sp2d07:0', tool_output={'date': '2024-06-24', 'from': 'it@co1t.com', 'subject': 'Setting Up Your IT Needs', 'text': 'Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.', 'to': 'david@co1t.com'})] 

start=100 end=153 text='attached guide to help you set up your work accounts.' sources=[ToolSource(type='tool', id='search_emails_wqs498sp2d07:0', tool_output={'date': '2024-06-24', 'from': 'it@co1t.com', 'subject': 'Setting Up Your IT Needs', 'text': 'Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.', 'to': 'david@co1t.com'})] 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
