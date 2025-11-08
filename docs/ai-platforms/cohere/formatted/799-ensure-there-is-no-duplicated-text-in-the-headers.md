---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ensure there is no duplicated text in the headers

def remove_duplicates(text):
    return re.sub(
        r"((\b\w+\b.{1,2}\w+\b)+).+\1", r"\1", text, flags=re.I
    )


df["text"] = df["text"].apply(remove_duplicates)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
