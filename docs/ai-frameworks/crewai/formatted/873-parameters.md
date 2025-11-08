---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


### SnowflakeConfig Parameters

The `SnowflakeConfig` class accepts the following parameters:

* **account**: Required. Snowflake account identifier.
* **user**: Required. Snowflake username.
* **password**: Optional\*. Snowflake password.
* **private\_key\_path**: Optional\*. Path to private key file (alternative to password).
* **warehouse**: Required. Snowflake warehouse name.
* **database**: Required. Default database.
* **snowflake\_schema**: Required. Default schema.
* **role**: Optional. Snowflake role.
* **session\_parameters**: Optional. Custom session parameters as a dictionary.

\*Either `password` or `private_key_path` must be provided.

### SnowflakeSearchTool Parameters

The `SnowflakeSearchTool` accepts the following parameters during initialization:

* **config**: Required. A `SnowflakeConfig` object containing connection details.
* **pool\_size**: Optional. Number of connections in the pool. Default is 5.
* **max\_retries**: Optional. Maximum retry attempts for failed queries. Default is 3.
* **retry\_delay**: Optional. Delay between retries in seconds. Default is 1.0.
* **enable\_caching**: Optional. Whether to enable query result caching. Default is True.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with custom parameters](./872-initialize-the-tool-with-custom-parameters.md)

**Next:** [Usage →](./874-usage.md)
