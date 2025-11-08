---
title: "Langgraph: Run creation, streaming, updates, etc."
description: "Run creation, streaming, updates, etc. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Run creation, streaming, updates, etc.

# This takes precedenceover the generic @auth.on handler and the @auth.on.threads handler
@auth.on.threads.create_run
async def on_run_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.create_run.value
):
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    # Inherit thread's access control
    return {"owner": ctx.user.identity}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler,](./362-reading-a-thread-since-this-is-also-more-specific-.md)

**Next:** [Assistant creation →](./364-assistant-creation.md)
