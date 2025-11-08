---
title: "Crewai: Creating and Publishing Tools"
description: "Creating and Publishing Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Creating and Publishing Tools


To create a new tool project:

```bash  theme={null}
crewai tool create <tool-name>
```

This generates a scaffolded tool project locally.

After making changes, initialize a Git repository and commit the code:

```bash  theme={null}
git init
git add .
git commit -m "Initial version"
```

To publish the tool:

```bash  theme={null}
crewai tool publish
```

By default, tools are published as private. To make a tool public:

```bash  theme={null}
crewai tool publish --public
```

For more details on how to build tools, see [Creating your own tools](https://docs.crewai.com/concepts/tools#creating-your-own-tools).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Adding other packages after installing a tool](./2428-adding-other-packages-after-installing-a-tool.md)

**Next:** [Updating Tools →](./2430-updating-tools.md)
