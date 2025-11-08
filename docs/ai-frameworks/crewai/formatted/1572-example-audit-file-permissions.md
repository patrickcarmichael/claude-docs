---
title: "Crewai: Example: Audit file permissions"
description: "Example: Audit file permissions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Audit file permissions


```python  theme={null}
from onedrive_file_crew import OneDriveFileTrigger

crew = OneDriveFileTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": onedrive_payload,
})
```

The crew inspects file metadata, user activity, and permission changes to produce a compliance-friendly summary.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling the OneDrive Trigger](./1571-enabling-the-onedrive-trigger.md)

**Next:** [Testing Locally →](./1573-testing-locally.md)
