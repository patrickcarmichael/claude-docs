---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response

<ResponseField name="id" type="string" required>
  Task id for retrieving result
</ResponseField>

<ResponseField name="status" type="enum<string>" required>
  Available options: Task not found, Pending, Request Moderated, Content Moderated, Ready, Error
</ResponseField>

<ResponseField name="result" type="any" />

<ResponseField name="progress" type="number | null" />

<ResponseField name="details" type="object | null" />


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
