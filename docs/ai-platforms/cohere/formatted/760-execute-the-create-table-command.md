---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Execute the CREATE TABLE command

cursor.execute(
    """
CREATE TABLE evaluation_results (
    usecase TEXT,
    run TEXT,
    score FLOAT,
    temperature FLOAT,
    tokens INTEGER,
    latency FLOAT
)
"""
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
