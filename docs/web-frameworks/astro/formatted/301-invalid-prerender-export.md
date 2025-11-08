---
title: "Invalid prerender export."
section: 301
---

# Invalid prerender export.

> **Example error messages:**\
> InvalidPrerenderExport: A `prerender` export has been detected, but its value cannot be statically analyzed.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `prerender` feature only supports a subset of valid JavaScript — be sure to use exactly `export const prerender = true` so that our compiler can detect this directive at build time. Variables, `let`, and `var` declarations are not supported.

---

[← Previous](300-error-while-loading-image-service.md) | [Index](index.md) | [Next →](index.md)
