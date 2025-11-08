---
title: "Crewai: Updating Tools"
description: "Updating Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Updating Tools


To update a published tool:

1. Modify the tool locally
2. Update the version in `pyproject.toml` (e.g., from `0.1.0` to `0.1.1`)
3. Commit the changes and publish

```bash  theme={null}
git commit -m "Update version to 0.1.1"
crewai tool publish
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Creating and Publishing Tools](./2429-creating-and-publishing-tools.md)

**Next:** [Deleting Tools →](./2431-deleting-tools.md)
