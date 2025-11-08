---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


When using the `SnowflakeSearchTool`, you need to provide the following parameters:

* **query**: Required. The SQL query to execute.
* **database**: Optional. Override the default database specified in the config.
* **snowflake\_schema**: Optional. Override the default schema specified in the config.
* **timeout**: Optional. Query timeout in seconds. Default is 300.

The tool will return the query results as a list of dictionaries, where each dictionary represents a row with column names as keys.

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./873-parameters.md)

**Next:** [Example of using the tool with an agent →](./875-example-of-using-the-tool-with-an-agent.md)
