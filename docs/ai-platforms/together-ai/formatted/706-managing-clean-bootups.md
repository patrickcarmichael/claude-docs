---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Managing CLEAN bootups

Whenever we boot a sandbox from scratch, we'll:

1. Start the Firecracker VM
2. Create a default user (called pitcher-host)
3. (optional) Build the Docker image specified in the .devcontainer/devcontainer.json file
4. Start the Docker container
5. Mount the /project/sandbox directory as a volume inside the Docker container

You will be able to connect to the Sandbox during this process and track its progress.
```javascript
const sandbox = await sdk.sandboxes.create()
 
const setupSteps = sandbox.setup.getSteps()
 
for (const step of setupSteps) {
  console.log(`Step: ${step.name}`);
  console.log(`Command: ${step.command}`);
  console.log(`Status: ${step.status}`);
 
  const output = await step.open()
 
  output.onOutput((output) => {
    console.log(output)
  })
 
  await step.waitUntilComplete()
}
```
<br />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
