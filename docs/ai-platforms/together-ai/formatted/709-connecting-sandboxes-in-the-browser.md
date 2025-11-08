---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Connecting Sandboxes in the browser

In addition to running your Sandbox in the server, you can also connect it to the browser. This requires some collaboration with the server.
```javascript
app.post('/api/sandboxes', async (req, res) => {
  const sandbox = await sdk.sandboxes.create();
  const session = await sandbox.createBrowserSession({
    // Create isolated sessions by using a unique reference to the user
    id: req.session.username,
  });
 
  res.json(session)
})
 
app.get('/api/sandboxes/:sandboxId', async (req, res) => {
  const sandbox = await sdk.sandboxes.resume(req.params.sandboxId);
  const session = await sandbox.createBrowserSession({
    // Resume any existing session by using the same user reference
    id: req.session.username,
  });
 
  res.json(session)
})
```
Then in the browser:
```javascript
import { connectToSandbox } from '@codesandbox/sdk/browser';
 
const sandbox = await connectToSandbox({
  // The session object you either passed on page load or fetched from the server
  session: initialSessionFromServer,
  // When reconnecting to the sandbox, fetch the session from the server
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`)
});
 
await sandbox.fs.writeTextFile('test.txt', 'Hello World');
```
The browser session automatically manages the connection and will reconnect if the connection is lost. This is controlled by an option called `onFocusChange` and by default it will reconnect when the page is visible.
```javascript
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
  onFocusChange: (notify) => {
    const onVisibilityChange = () => {
      notify(document.visibilityState === 'visible');
    }
 
    document.addEventListener('visibilitychange', onVisibilityChange);
 
    return () => {
      document.removeEventListener('visibilitychange', onVisibilityChange);
    }
  }
});
```
If you tell the browser session when it is in focus it will automatically reconnect when hibernated. Unless you explicitly disconnect the session.

While the `connectToSandbox` promise is resolving you can also listen to initialization events to show a loading state:
```javascript
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
  onInitCb: (event) => {}
});
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
