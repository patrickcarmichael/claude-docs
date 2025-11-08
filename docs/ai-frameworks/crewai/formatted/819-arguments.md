---
title: "Crewai: Arguments"
description: "Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Arguments


The PGSearchTool is designed to require the following arguments for its operation:

| Argument        | Type     | Description                                                                                                                                                                                                    |
| :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **db\_uri**     | `string` | **Mandatory**. A string representing the URI of the PostgreSQL database to be queried. This argument will be mandatory and must include the necessary authentication details and the location of the database. |
| **table\_name** | `string` | **Mandatory**. A string specifying the name of the table within the database on which the semantic search will be performed. This argument will also be mandatory.                                             |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with the database URI and the target table name](./818-initialize-the-tool-with-the-database-uri-and-the-.md)

**Next:** [Custom Model and Embeddings →](./820-custom-model-and-embeddings.md)
