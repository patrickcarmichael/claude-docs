---
title: "Crewai: Response Format"
description: "Response Format section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Response Format


The tool returns results in JSON format:

```json  theme={null}
{
  "results": [
    {
      "content": "Retrieved text content",
      "content_type": "text",
      "source_type": "S3",
      "source_uri": "s3://bucket/document.pdf",
      "score": 0.95,
      "metadata": {
        "additional": "metadata"
      }
    }
  ],
  "nextToken": "pagination-token",
  "guardrailAction": "NONE"
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Environment Variables](./734-environment-variables.md)

**Next:** [Advanced Usage →](./736-advanced-usage.md)
