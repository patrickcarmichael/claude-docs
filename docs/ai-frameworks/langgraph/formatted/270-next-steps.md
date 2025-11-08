---
title: "Langgraph: Next Steps"
description: "Next Steps section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Next Steps


Review the `README.md` file in the root of your new LangGraph app for more information about the template and how to customize it.

After configuring the app properly and adding your API keys, you can start the app using the LangGraph CLI:

```bash
langgraph dev
```

Or via [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (recommended):

```bash
uvx --from "langgraph-cli[inmem]" --with-editable . langgraph dev
```

!!! info "Missing Local Package?"

    If you are not using `uv` and run into a "`ModuleNotFoundError`" or "`ImportError`", even after installing the local package (`pip install -e .`), it is likely the case that you need to install the CLI into your local virtual environment to make the CLI "aware" of the local package. You can do this by running `python -m pip install "langgraph-cli[inmem]"` and re-activating your virtual environment before running `langgraph dev`.

See the following guides for more information on how to deploy your app:

- **[Launch Local LangGraph Server](../tutorials/langgraph-platform/local-server.md)**: This quick start guide shows how to start a LangGraph Server locally for the **ReAct Agent** template. The steps are similar for other templates.
- **[Deploy to LangGraph Platform](../cloud/quick_start.md)**: Deploy your LangGraph app using LangGraph Platform.

---

concepts/tools.md

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 🌱 Create a LangGraph App](./269-create-a-langgraph-app.md)

**Next:** [Tools →](./271-tools.md)
