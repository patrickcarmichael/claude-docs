---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating the template

Create a new folder in your project and add the files you want to have available inside your Sandbox. For example set up a Vite project:
```text
npx create-vite@latest my-template
```
Now we need to configure the template with tasks so that it will install dependencies and start the dev server. Create a my-template/.codesandbox/tasks.json file with the following content:
```json
{  
    "setupTasks": [  
        "npm install"  
    ],  
    "tasks": {  
        "dev-server": {  
            "name": "Dev Server",  
            "command": "npm run dev",  
            "runAtStart": true  
        }  
    }  
}
```
The `setupTasks` will run after the Sandbox has started, before any other tasks.

Now we are ready to deploy the template to our clusters, run:
```text
$ CSB_API_KEY=your-api-key npx @codesandbox/sdk build ./my-template --ports 5173
```
<br />

<Tip>
  ### Note

  The template will by default be built with Micro VM Tier unless you pass --vmTier to the build command.
</Tip>

This will start the process of creating Sandboxes for each of our clusters, write files, restart, wait for port 5173 to be available and then hibernate. This generates the snapshot that allows you to quickly create Sandboxes already running a dev server from the template.

When all clusters are updated successfully you will get a "Template Tag" back which you can use when you create your sandboxes.
```javascript
const sandbox = await sdk.sandboxes.create({  
    source: 'template',  
    id: 'some-template-tag'  
})
```
<br />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
