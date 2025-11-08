---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Convenience function for formatting documents

def format_for_cohere_client(nodes_):
    return [
        {
            "text": node.node.text,
            "llamaindex_id": node.node.id_,
        }
        for node
        in nodes_
    ]


documents = []

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
