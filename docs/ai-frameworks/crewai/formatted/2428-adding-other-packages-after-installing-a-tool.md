---
title: "Crewai: Adding other packages after installing a tool"
description: "Adding other packages after installing a tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Adding other packages after installing a tool


After installing a tool from the CrewAI AMP Tool Repository, you need to use the `crewai uv` command to add other packages to your project.
Using pure `uv` commands will fail due to authentication to tool repository being handled by the CLI. By using the `crewai uv` command, you can add other packages to your project without having to worry about authentication.
Any `uv` command can be used with the `crewai uv` command, making it a powerful tool for managing your project's dependencies without the hassle of managing authentication through environment variables or other methods.

Say that you have installed a custom tool from the CrewAI AMP Tool Repository called "my-tool":

```bash  theme={null}
crewai tool install my-tool
```

And now you want to add another package to your project, you can use the following command:

```bash  theme={null}
crewai uv add requests
```

Other commands like `uv sync` or `uv remove` can also be used with the `crewai uv` command:

```bash  theme={null}
crewai uv sync
```

```bash  theme={null}
crewai uv remove requests
```

This will add the package to your project and update `pyproject.toml` accordingly.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Installing Tools](./2427-installing-tools.md)

**Next:** [Creating and Publishing Tools →](./2429-creating-and-publishing-tools.md)
