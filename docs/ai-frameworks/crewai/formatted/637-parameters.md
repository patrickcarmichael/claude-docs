---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `AIMindTool` accepts the following parameters:

* **api\_key**: Optional. Your Minds API key. If not provided, it will be read from the `MINDS_API_KEY` environment variable.
* **datasources**: A list of dictionaries, each containing the following keys:
  * **description**: A description of the data contained in the datasource.
  * **engine**: The engine (or type) of the datasource.
  * **connection\_data**: A dictionary containing the connection parameters for the datasource.
  * **tables**: A list of tables that the data source will use. This is optional and can be omitted if all tables in the data source are to be used.

A list of supported data sources and their connection parameters can be found [here](https://docs.mdb.ai/docs/data_sources).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run a natural language query](./636-run-a-natural-language-query.md)

**Next:** [Agent Integration Example →](./638-agent-integration-example.md)
