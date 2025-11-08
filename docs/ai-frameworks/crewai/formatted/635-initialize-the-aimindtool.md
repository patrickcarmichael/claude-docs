---
title: "Crewai: Initialize the AIMindTool"
description: "Initialize the AIMindTool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the AIMindTool

aimind_tool = AIMindTool(
    datasources=[
        {
            "description": "house sales data",
            "engine": "postgres",
            "connection_data": {
                "user": "demo_user",
                "password": "demo_password",
                "host": "samples.mindsdb.com",
                "port": 5432,
                "database": "demo",
                "schema": "demo_data"
            },
            "tables": ["house_sales"]
        }
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example](./634-example.md)

**Next:** [Run a natural language query →](./636-run-a-natural-language-query.md)
