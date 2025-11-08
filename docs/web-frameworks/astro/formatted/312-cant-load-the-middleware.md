---
title: "Can't load the middleware."
section: 312
---

# Can't load the middleware.

> **MiddlewareCantBeLoaded**: An unknown error was thrown while loading your middleware.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when middleware throws an error while attempting to loading it.

For example:

```ts
import {defineMiddleware} from "astro:middleware";
throw new Error("Error thrown while loading the middleware.")
export const onRequest = defineMiddleware(() => {
  return "string"
});
```

---

[← Previous](311-mdx-integration-missing.md) | [Index](index.md) | [Next →](index.md)
