---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Style Guide

Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""
    model = 'command-a-03-2025'
    temp = 0.2


    response = co.chat(
      message=query,
      documents=documents,
      preamble=preamble,
      model=model,
      temperature=temp
    )

    final_answer_docs="""The final answer is from the documents below:

    {docs}""".format(docs=str(response.documents))

    final_answer = response.text
    return final_answer, final_answer_docs
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
