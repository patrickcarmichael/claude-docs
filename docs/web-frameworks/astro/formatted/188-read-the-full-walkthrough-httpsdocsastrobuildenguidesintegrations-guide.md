---
title: "(Read the full walkthrough: https://docs.astro.build/en/guides/integrations-guide)"
section: 188
---

# (Read the full walkthrough: https://docs.astro.build/en/guides/integrations-guide)
+npm install @astrojs/lit lit
+npm install @astrojs/react react react-dom
```jsx
```diff
// Then, update your `astro.config.mjs` file:
// (Read the full walkthrough: https://docs.astro.build/en/guides/integrations-guide)
+import lit from '@astrojs/lit';
+import react from '@astrojs/react';


export default {
-  renderers: ['@astrojs/renderer-lit', '@astrojs/renderer-react'],
+  integrations: [lit(), react()],
}
```jsx
| Deprecated Renderers on npm | v0.25+ Integrations on npm |
| --------------------------- | -------------------------- |
| @astrojs/renderer-react     | @astrojs/react             |
| @astrojs/renderer-preact    | @astrojs/preact            |
| @astrojs/renderer-solid     | @astrojs/solid-js          |
| @astrojs/renderer-vue       | @astrojs/vue               |
| @astrojs/renderer-svelte    | @astrojs/svelte            |

#### Handling Peer Dependencies

[Section titled “Handling Peer Dependencies”](#handling-peer-dependencies)

Note

Read this section if: You are on Node v14 **or** if you use any package manager other than npm.

Unlike the old renderers, integrations no longer mark the frameworks themselves (“react”, “svelte”, “vue”, etc.) as direct dependencies of the integration. Instead, you should now install your framework packages *in addition to* your integrations.

```shell

---

[← Previous](187-install-your-new-integrations-and-frameworks.md) | [Index](index.md) | [Next →](index.md)
