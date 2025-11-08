---
title: "Mcp: Behavior Requirements"
description: "Behavior Requirements section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Behavior Requirements


1. Progress notifications **MUST** only reference tokens that:
   * Were provided in an active request
   * Are associated with an in-progress operation

2. Receivers of progress requests **MAY**:
   * Choose not to send any progress notifications
   * Send notifications at whatever frequency they deem appropriate
   * Omit the total value if unknown

```mermaid  theme={null}
sequenceDiagram
    participant Sender
    participant Receiver

    Note over Sender,Receiver: Request with progress token
    Sender->>Receiver: Method request with progressToken

    Note over Sender,Receiver: Progress updates
    Receiver-->>Sender: Progress notification (0.2/1.0)
    Receiver-->>Sender: Progress notification (0.6/1.0)
    Receiver-->>Sender: Progress notification (1.0/1.0)

    Note over Sender,Receiver: Operation complete
    Receiver->>Sender: Method response
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Progress Flow](./125-progress-flow.md)

**Next:** [Implementation Notes →](./127-implementation-notes.md)
