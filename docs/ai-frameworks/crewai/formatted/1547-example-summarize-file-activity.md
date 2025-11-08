---
title: "Crewai: Example: Summarize file activity"
description: "Example: Summarize file activity section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Summarize file activity


The drive example crews parse the payload to extract file metadata, evaluate permissions, and publish a summary.

```python  theme={null}
from drive_file_crew import GoogleDriveFileTrigger

crew = GoogleDriveFileTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": drive_payload,
})
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling the Google Drive Trigger](./1546-enabling-the-google-drive-trigger.md)

**Next:** [Testing Locally →](./1548-testing-locally.md)
