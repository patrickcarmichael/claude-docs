---
title: "The middleware didn't return a Response."
section: 313
---

# The middleware didn't return a Response.

> **MiddlewareNoDataOrNextCalled**: Make sure your middleware returns a `Response` object, either directly or by returning the `Response` from calling the `next` function.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when the middleware does not return any data or call the `next` function.

For example:

```ts
import {defineMiddleware} from "astro:middleware";
export const onRequest = defineMiddleware((context, _) => {
  // doesn't return anything or call `next`
  context.locals.someData = false;
});
```

---

[← Previous](312-cant-load-the-middleware.md) | [Index](index.md) | [Next →](index.md)
