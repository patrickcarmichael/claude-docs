---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display the citations and source documents

if response.message.citations:
    print("\nCITATIONS:")
    for citation in response.message.citations:
        print(citation, "\n")
```
```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.

CITATIONS:
start=14 end=88 text='gym memberships, on-site yoga classes, and comprehensive health insurance.' sources=[DocumentSource(type='document', id='doc:2', document={'id': 'doc:2', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
