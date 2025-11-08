---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

To get started, install the SDK:
```text
npm install @codesandbox/sdk
```
Then, create an API token by going to [https://codesandbox.io/t/api](https://codesandbox.io/t/api), and clicking on the "Create API Token" button. You can then use this token to authenticate with the SDK:
```typescript
import { CodeSandbox } from "@codesandbox/sdk";
 
const sdk = new CodeSandbox(process.env.CSB_API_KEY!);
 
const sandbox = await sdk.sandboxes.create();
 
const session = await sandbox.connect();
 
const output = await session.commands.run("echo 'Hello World'");
 
console.log(output) // Hello World
```
<br />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
