---
title: "Langgraph: Common Access Patterns"
description: "Common Access Patterns section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Common Access Patterns


Here are some typical authorization patterns:

### Single-Owner Resources

This common pattern lets you scope all threads, assistants, crons, and runs to a single user. It's useful for common single-user use cases like regular chatbot-style apps.

```python
@auth.on
async def owner_only(ctx: Auth.types.AuthContext, value: dict):
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    return {"owner": ctx.user.identity}
```

### Permission-based Access

This pattern lets you control access based on **permissions**. It's useful if you want certain roles to have broader or more restricted access to resources.

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Assistant creation](./364-assistant-creation.md)

**Next:** [In your auth handler: →](./366-in-your-auth-handler.md)
