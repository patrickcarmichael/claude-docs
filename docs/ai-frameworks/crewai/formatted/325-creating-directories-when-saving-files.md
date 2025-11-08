---
title: "Crewai: Creating Directories when Saving Files"
description: "Creating Directories when Saving Files section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Creating Directories when Saving Files


The `create_directory` parameter controls whether CrewAI should automatically create directories when saving task outputs to files. This feature is particularly useful for organizing outputs and ensuring that file paths are correctly structured, especially when working with complex project hierarchies.

### Default Behavior

By default, `create_directory=True`, which means CrewAI will automatically create any missing directories in the output file path:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling and Validation Mechanisms](./324-error-handling-and-validation-mechanisms.md)

**Next:** [Default behavior - directories are created automatically →](./326-default-behavior-directories-are-created-automatic.md)
