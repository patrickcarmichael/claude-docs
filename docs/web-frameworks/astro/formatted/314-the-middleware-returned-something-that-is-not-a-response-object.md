---
title: "The middleware returned something that is not a Response object."
section: 314
---

# The middleware returned something that is not a Response object.

> **MiddlewareNotAResponse**: Any data returned from middleware must be a valid `Response` object.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when middleware returns something that is not a `Response` object.

For example:

```ts
import {defineMiddleware} from "astro:middleware";
export const onRequest = defineMiddleware(() => {
  return "string"
});
```

---

[← Previous](313-the-middleware-didnt-return-a-response.md) | [Index](index.md) | [Next →](index.md)
