---
title: "Crewai: Error Handling"
description: "Error Handling section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Error Handling


The `S3WriterTool` includes error handling for common S3 issues:

* Invalid S3 path format
* Permission issues (e.g., no write access to the bucket)
* AWS credential problems
* Bucket does not exist

When an error occurs, the tool will return an error message that includes details about the issue.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./778-run-the-task.md)

**Next:** [Implementation Details →](./780-implementation-details.md)
