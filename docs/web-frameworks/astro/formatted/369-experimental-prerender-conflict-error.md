---
title: "Experimental prerender conflict error"
section: 369
---

# Experimental prerender conflict error

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.14.0`

Turns prerender conflict warnings into errors during the build process.

Astro currently warns you during the build about any conflicts between multiple dynamic routes that can result in the same output path. For example `/blog/[slug]` and `/blog/[...all]` both could try to prerender the `/blog/post-1` path. In such cases, Astro renders only the [highest priority route](/en/guides/routing/#route-priority-order) for the conflicting path. This allows your site to build successfully, although you may discover that some pages are rendered by unexpected routes.

With this experimental flag set, the build will instead fail immediately with an error. This will require you to resolve any routing conflicts immediately, and will ensure that Astro is building your routes as you intend.

To enable this behavior, add the `experimental.failOnPrerenderConflict` feature flag to your Astro config:

astro.config.mjs

```diff
import { defineConfig } from "astro/config"


defineConfig({
+  experimental: {
+    failOnPrerenderConflict: true,
+  },
});
```jsx
## Usage

[Section titled “Usage”](#usage)

After enabling this flag, you may encounter errors about conflicting prerendered routes when you attempt to build your project. If this happens, you will need to update one or more of your [dynamic routes](/en/guides/routing/#dynamic-routes) to avoid ambiguous routing.

---

[← Previous](368-experimental-content-security-policy-csp.md) | [Index](index.md) | [Next →](index.md)
