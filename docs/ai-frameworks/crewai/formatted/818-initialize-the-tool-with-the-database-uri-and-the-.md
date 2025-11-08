---
title: "Crewai: Initialize the tool with the database URI and the target table name"
description: "Initialize the tool with the database URI and the target table name section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool with the database URI and the target table name

tool = PGSearchTool(
    db_uri='postgresql://user:password@localhost:5432/mydatabase', 
    table_name='employees'
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example Usage](./817-example-usage.md)

**Next:** [Arguments →](./819-arguments.md)
