---
title: "Langgraph: it will take precedence for any "create" actions on the "threads" resources"
description: "it will take precedence for any "create" actions on the "threads" resources section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# it will take precedence for any "create" actions on the "threads" resources

@auth.on.threads.create
async def on_thread_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.create.value
):
    # Setting metadata on the thread being created
    # will ensure that the resource contains an "owner" field
    # Then any time a user tries to access this thread or runs within the thread,
    # we can filter by owner
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    return {"owner": ctx.user.identity}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Thread creation. This will match only on thread create actions](./360-thread-creation-this-will-match-only-on-thread-cre.md)

**Next:** [Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler, →](./362-reading-a-thread-since-this-is-also-more-specific-.md)
