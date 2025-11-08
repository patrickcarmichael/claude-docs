---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Objective

Generally, users are limited to text inputs when using large language models (LLMs), but agents enable the model to do more than ingest or output text information. Using tools, LLMs can call other APIs, save data, and much more. In this notebook, we will explore how we can leverage agents to extract information from PDFs. We will mimic an application where the user uploads PDF files and the agent extracts useful information. This can be useful when the text information has varying formats and you need to extract various types of information.

In the directory, we have a simple\_invoice.pdf file. Everytime a user uploads the document, the agent will extract key information total\_amount and invoice\_number and then save it as CSV which then can be used in another application. We only extract two pieces of information in this demo, but users can extend the example and extract a lot more information.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
