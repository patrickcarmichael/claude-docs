---
title: "Langgraph: Generic / global handler catches calls that aren't handled by more specific handlers"
description: "Generic / global handler catches calls that aren't handled by more specific handlers section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Generic / global handler catches calls that aren't handled by more specific handlers

@auth.on
async def reject_unhandled_requests(ctx: Auth.types.AuthContext, value: Any) -> False:
    print(f"Request to {ctx.path} by {ctx.user.identity}")
    raise Auth.exceptions.HTTPException(
        status_code=403,
        detail="Forbidden"
    )

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Authorization](./356-authorization.md)

**Next:** [Matches the "thread" resource and all actions - create, read, update, delete, search →](./358-matches-the-thread-resource-and-all-actions-create.md)
