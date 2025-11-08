---
title: "Missing params property on getStaticPaths route."
section: 280
---

# Missing params property on getStaticPaths route.

> **GetStaticPathsExpectedParams**: Missing or empty required `params` property on `getStaticPaths` route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Every route specified by `getStaticPaths` require a `params` property specifying the path parameters needed to match the route.

For instance, the following code:

pages/blog/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: '1' } }
  ];
}
---
```jsx
Will create the following route: `site.com/blog/1`.

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

---

[← Previous](279-invalid-use-of-getdataentrybyid-or-getentrybyslug-function.md) | [Index](index.md) | [Next →](index.md)
