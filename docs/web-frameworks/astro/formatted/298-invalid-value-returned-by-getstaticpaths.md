---
title: "Invalid value returned by getStaticPaths."
section: 298
---

# Invalid value returned by getStaticPaths.

> **InvalidGetStaticPathsReturn**: Invalid type returned by `getStaticPaths`. Expected an `array`, got `RETURN_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths`’s return value must be an array of objects.

pages/blog/\[id].astro

```ts
export async function getStaticPaths() {
  return [ // <-- Array
    { params: { slug: "blog" } },
    { params: { slug: "about" } }
  ];
}
```jsx
**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

---

[← Previous](297-invalid-entry-inside-getstaticpaths-return-value.md) | [Index](index.md) | [Next →](index.md)
