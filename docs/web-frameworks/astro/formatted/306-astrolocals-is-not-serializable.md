---
title: "Astro.locals is not serializable"
section: 306
---

# Astro.locals is not serializable

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **LocalsNotSerializable**: The information stored in `Astro.locals` for the path “`HREF`” is not serializable. Make sure you store only serializable data. (E03034)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when a user attempts to store something that is not serializable in `locals`.

For example:

```ts
import {defineMiddleware} from "astro/middleware";
export const onRequest = defineMiddleware((context, next) => {
  context.locals = {
    foo() {
      alert("Hello world!")
    }
  };
  return next();
});
```

---

[← Previous](305-value-assigned-to-locals-is-not-accepted.md) | [Index](index.md) | [Next →](index.md)
