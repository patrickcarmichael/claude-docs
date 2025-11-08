---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 3. Use LLM to Generate Natural Language Questions ---

nl_generation_prompt_template = """
You are an expert data analyst who is great at translating SQL queries into plain English.
Based on the database schema and the provided SQL query, what is a natural language question a business user would ask to get this information?
Ensure that the question is precise enough to accurately map to the corresponding SQL query.

**Database Schema:**
{schema_for_prompt}

**SQL Query:**
{query}

Provide only the user's question, without any preamble or explanation.
""".strip()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
