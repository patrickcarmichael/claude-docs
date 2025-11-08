---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced: cache locality for Enterprise deployments

Dedicated deployments on an Enterprise plan allow you to pass an additional hint in the request to improve cache hit rates.

First, the deployment needs to be created or updated with an additional flag:
```bash
firectl create deployment ... --enable-session-affinity
```
Then the client can pass an opaque identifier representing a single user or
session in the `user` field of the body or in the `x-session-affinity` header. Fireworks
will try to route requests with the identifier to the same server, further reducing response times.

It's best to choose an identifier that groups requests with long shared prompt
prefixes. For example, it can be a chat session with the same user or an
assistant working with the same shared context.

### Migration and traffic management

When migrating between deployments that use prompt caching, it's crucial to implement proper traffic routing to maintain optimal cache hit rates. When gradually routing traffic to a new deployment, use consistent user/session-based sampling rather than random sampling.

Here's the recommended implementation for traffic routing:
```python
import hashlib

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
