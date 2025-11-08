---
title: "Langgraph: Dependencies"
description: "Dependencies section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Dependencies


A LangGraph application may depend on other Python packages.

You will generally need to specify the following information for dependencies to be set up correctly:

1. A file in the directory that specifies the dependencies (e.g. `requirements.txt`, `pyproject.toml`, or `package.json`).

2. A `dependencies` key in the [LangGraph configuration file](#configuration-file-concepts) that specifies the dependencies required to run the LangGraph application.
3. Any additional binaries or system libraries can be specified using `dockerfile_lines` key in the [LangGraph configuration file](#configuration-file-concepts).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configuration File {#configuration-file-concepts}](./458-configuration-file-configuration-file-concepts.md)

**Next:** [Graphs →](./460-graphs.md)
