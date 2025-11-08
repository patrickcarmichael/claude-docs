---
title: "Cannot use Astro.rewrite after the request body has been read"
section: 341
---

# Cannot use Astro.rewrite after the request body has been read

> **RewriteWithBodyUsed**: Astro.rewrite() cannot be used if the request body has already been read. If you need to read the body, first clone the request.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.rewrite()` cannot be used if the request body has already been read. If you need to read the body, first clone the request. For example:

```js
const data = await Astro.request.clone().formData();


Astro.rewrite("/target")
```jsx
**See Also:**

* [Request.clone()](https://developer.mozilla.org/en-US/docs/Web/API/Request/clone)
* [Astro.rewrite](/en/reference/api-reference/#rewrite)

---

[← Previous](340-astro-couldnt-find-the-route-to-rewrite-or-if-was-found-but-it-emitted-an-error-during-the-rendering-phase.md) | [Index](index.md) | [Next →](index.md)
