---
title: "Crewai: Advanced Features"
description: "Advanced Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Features


### Connection Pooling

The `SnowflakeSearchTool` implements connection pooling to improve performance by reusing database connections. You can control the pool size with the `pool_size` parameter.

### Automatic Retries

The tool automatically retries failed queries with exponential backoff. You can configure the retry behavior with the `max_retries` and `retry_delay` parameters.

### Query Result Caching

To improve performance for repeated queries, the tool can cache query results. This feature is enabled by default but can be disabled by setting `enable_caching=False`.

### Key-Pair Authentication

In addition to password authentication, the tool supports key-pair authentication for enhanced security:

```python Code theme={null}
config = SnowflakeConfig(
    account="your_account",
    user="your_username",
    private_key_path="/path/to/your/private/key.p8",
    warehouse="COMPUTE_WH",
    database="your_database",
    snowflake_schema="your_schema"
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./879-run-the-task.md)

**Next:** [Error Handling →](./881-error-handling.md)
