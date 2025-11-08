---
title: "Adapter does not support server output."
section: 239
---

# Adapter does not support server output.

> **AdapterSupportOutputMismatch**: The `ADAPTER_NAME` adapter is configured to output a static website, but the project contains server-rendered pages. Please install and configure the appropriate server adapter for your final deployment.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The currently configured adapter does not support server-side rendering, which is required for the current project setup.

Depending on your adapter, there may be a different entrypoint to use for server-side rendering. For example, the `@astrojs/vercel` adapter has a `@astrojs/vercel/static` entrypoint for static rendering, and a `@astrojs/vercel/serverless` entrypoint for server-side rendering.

**See Also:**

* [Server-side Rendering](/en/guides/on-demand-rendering/)

---

[← Previous](238-actions-must-be-used-with-server-output.md) | [Index](index.md) | [Next →](index.md)
