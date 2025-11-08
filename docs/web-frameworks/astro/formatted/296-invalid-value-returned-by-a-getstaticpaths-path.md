---
title: "Invalid value returned by a getStaticPaths path."
section: 296
---

# Invalid value returned by a getStaticPaths path.

> **InvalidGetStaticPathParam**: Invalid params given to `getStaticPaths` path. Expected an `object`, got `PARAM_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `params` property in `getStaticPaths`’s return value (an array of objects) should also be an object.

pages/blog/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { slug: "blog" } },
    { params: { slug: "about" } }
  ];
}
---
```jsx
**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

---

[← Previous](295-invalid-frontmatter-injection.md) | [Index](index.md) | [Next →](index.md)
