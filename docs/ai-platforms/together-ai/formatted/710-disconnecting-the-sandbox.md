---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Disconnecting the Sandbox

Disconnecting the session will end the session and automatically hibernate the sandbox after a timeout. You can also hibernate the sandbox explicitly from the server.
```javascript
import { connectToSandbox } from '@codesandbox/sdk/browser'
 
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
})
 
// Disconnect returns a promise that resolves when the session is disconnected
sandbox.disconnect();
 
// Optionally hibernate the sandbox explicitly by creating an endpoint on your server
fetch('/api/sandboxes/' + sandbox.id + '/hibernate', {
  method: 'POST'
})
 
// You can reconnect explicitly from the browser by
sandbox.reconnect()
```
<br />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
