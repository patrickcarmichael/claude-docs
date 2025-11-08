---
title: "Missing value for client:media directive."
section: 318
---

# Missing value for client:media directive.

> **MissingMediaQueryDirective**: Media query not provided for `client:media` directive. A media query similar to `client:media="(max-width: 600px)"` must be provided

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) parameter is required when using the `client:media` directive.

```astro
<Counter client:media="(max-width: 640px)" />
```jsx
**See Also:**

* [`client:media`](/en/reference/directives-reference/#clientmedia)

---

[← Previous](317-the-provided-locale-does-not-exist.md) | [Index](index.md) | [Next →](index.md)
