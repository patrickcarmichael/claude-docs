---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best Practices

### Give Detailed Context

Talk to OpenCode like you're talking to a junior developer:
```
When a user deletes a note, flag it as deleted in the database instead of removing it. 
Then create a "Recently Deleted" screen where users can restore or permanently delete notes.
Use the same design patterns as our existing settings page.
```

### Use Examples and References

Provide plenty of context and examples:
```
Add error handling to the API similar to how it's done in @src/utils/errorHandler.js
```

### Iterate on Plans

In Plan Mode, review and refine the approach before implementation:
```
That looks good, but let's also add input validation and rate limiting
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
