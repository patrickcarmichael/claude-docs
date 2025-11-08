---
title: "Value assigned to locals is not accepted."
section: 305
---

# Value assigned to locals is not accepted.

> **LocalsNotAnObject**: `locals` can only be assigned to an object. Other values like numbers, strings, etc. are not accepted.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when `locals` is overwritten with something that is not an object

For example:

```ts
import {defineMiddleware} from "astro:middleware";
export const onRequest = defineMiddleware((context, next) => {
  context.locals = 1541;
  return next();
});
```

---

[← Previous](304-local-images-must-be-imported.md) | [Index](index.md) | [Next →](index.md)
