---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Motivation

Enterprise customers often store and handle information in relational databases but querying such databases effectively requires bespoke knowledge of the underlying database structure as well as strong SQL coding skills. One way to address these challenges is to build an LLM agent capable of generating and executing SQL queries based on natural language. For example, if a user asks: `what are the top 4 rows in table X`, the agent should be able to generate `SELECT * FROM X LIMIT 4`, execute this query and return the output to the user.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
