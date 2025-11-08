---
title: "Crewai: Defaults on initialization"
description: "Defaults on initialization section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Defaults on initialization


* `default_catalog`
* `default_schema`
* `default_warehouse_id`

### Error handling & tips

* Authentication errors: verify `DATABRICKS_HOST` begins with `https://` and token is valid.
* Permissions: ensure your SQL warehouse and schema are accessible by your token.
* Limits: long‑running queries should be avoided in agent loops; add filters/limits.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./1076-parameters.md)

**Next:** [EXA Search Web Loader →](./1078-exa-search-web-loader.md)
