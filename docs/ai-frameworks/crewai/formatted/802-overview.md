---
title: "Crewai: Overview"
description: "Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Overview


This tool is used to convert natural language to SQL queries. When passed to the agent it will generate queries and then use them to interact with the database.

This enables multiple workflows like having an Agent to access the database fetch information based on the goal and then use the information to generate a response, report or any other output.
Along with that provides the ability for the Agent to update the database based on its goal.

**Attention**: Make sure that the Agent has access to a Read-Replica or that is okay for the Agent to run insert/update queries on the database.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← NL2SQL Tool](./801-nl2sql-tool.md)

**Next:** [Requirements →](./803-requirements.md)
