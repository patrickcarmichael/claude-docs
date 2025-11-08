---
title: "Crewai: Return Format"
description: "Return Format section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Return Format


The tool returns results in the following format:

```json  theme={null}
{
  "success": true,
  "results": [
    {
      "name": "Result Title",
      "url": "https://example.com/result",
      "content": "Content of the result..."
    },
    // Additional results...
  ]
}
```

If an error occurs, the response will be:

```json  theme={null}
{
  "success": false,
  "error": "Error message"
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Perform a search with custom parameters](./1106-perform-a-search-with-custom-parameters.md)

**Next:** [Error Handling →](./1108-error-handling.md)
