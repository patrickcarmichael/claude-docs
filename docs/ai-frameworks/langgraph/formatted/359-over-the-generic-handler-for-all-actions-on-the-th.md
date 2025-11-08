---
title: "Langgraph: over the generic handler for all actions on the "threads" resource"
description: "over the generic handler for all actions on the "threads" resource section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# over the generic handler for all actions on the "threads" resource

@auth.on.threads
async def on_thread_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.create.value
):
    if "write" not in ctx.permissions:
        raise Auth.exceptions.HTTPException(
            status_code=403,
            detail="User lacks the required permissions."
        )
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

**Previous:** [← Matches the "thread" resource and all actions - create, read, update, delete, search](./358-matches-the-thread-resource-and-all-actions-create.md)

**Next:** [Thread creation. This will match only on thread create actions →](./360-thread-creation-this-will-match-only-on-thread-cre.md)
