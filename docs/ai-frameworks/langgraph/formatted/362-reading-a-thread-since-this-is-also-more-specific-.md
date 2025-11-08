---
title: "Langgraph: Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler,"
description: "Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler, section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler,

# it will take precedence for any "read" actions on the "threads" resource
@auth.on.threads.read
async def on_thread_read(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.read.value
):
    # Since we are reading (and not creating) a thread,
    # we don't need to set metadata. We just need to
    # return a filter to ensure users can only see their own threads
    return {"owner": ctx.user.identity}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← it will take precedence for any "create" actions on the "threads" resources](./361-it-will-take-precedence-for-any-create-actions-on-.md)

**Next:** [Run creation, streaming, updates, etc. →](./363-run-creation-streaming-updates-etc.md)
