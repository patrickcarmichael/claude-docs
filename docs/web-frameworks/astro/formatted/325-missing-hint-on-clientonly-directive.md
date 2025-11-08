---
title: "Missing hint on client:only directive."
section: 325
---

# Missing hint on client:only directive.

> **NoClientOnlyHint**: Unable to render `COMPONENT_NAME`. When using the `client:only` hydration strategy, Astro needs a hint to use the correct renderer.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`client:only` components are not run on the server, as such Astro does not know (and cannot guess) which renderer to use and require a hint. Like such:

```astro
  <SomeReactComponent client:only="react" />
```jsx
**See Also:**

* [`client:only`](/en/reference/directives-reference/#clientonly)

---

[← Previous](324-no-client-entrypoint-specified-in-renderer.md) | [Index](index.md) | [Next →](index.md)
