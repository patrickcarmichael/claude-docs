---
title: "Langgraph: Configuration File {#configuration-file-concepts}"
description: "Configuration File {#configuration-file-concepts} section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Configuration File {#configuration-file-concepts}


The `langgraph.json` file is a JSON file that specifies the dependencies, graphs, environment variables, and other settings required to deploy a LangGraph application.

See the [LangGraph configuration file reference](../cloud/reference/cli.md#configuration-file) for details on all supported keys in the JSON file.

!!! tip

    The [LangGraph CLI](./langgraph_cli.md) defaults to using the configuration file `langgraph.json` in the current directory.

### Examples

- The dependencies involve a custom local package and the `langchain_openai` package.
- A single graph will be loaded from the file `./your_package/your_file.py` with the variable `variable`.
- The environment variables are loaded from the `.env` file.

```json
{
  "dependencies": ["langchain_openai", "./your_package"],
  "graphs": {
    "my_agent": "./your_package/your_file.py:agent"
  },
  "env": "./.env"
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← File Structure](./457-file-structure.md)

**Next:** [Dependencies →](./459-dependencies.md)
