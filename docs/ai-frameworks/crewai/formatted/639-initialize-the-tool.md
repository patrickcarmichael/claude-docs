---
title: "Crewai: Initialize the tool"
description: "Initialize the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool

aimind_tool = AIMindTool(
    datasources=[
        {
            "description": "sales data",
            "engine": "postgres",
            "connection_data": {
                "user": "your_user",
                "password": "your_password",
                "host": "your_host",
                "port": 5432,
                "database": "your_db",
                "schema": "your_schema"
            },
            "tables": ["sales"]
        }
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent Integration Example](./638-agent-integration-example.md)

**Next:** [Define an agent with the AIMindTool →](./640-define-an-agent-with-the-aimindtool.md)
