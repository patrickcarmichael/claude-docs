---
title: "Invalid entry inside getStaticPath's return value"
section: 297
---

# Invalid entry inside getStaticPath's return value

> **InvalidGetStaticPathsEntry**: Invalid entry returned by getStaticPaths. Expected an object, got `ENTRY_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths`’s return value must be an array of objects. In most cases, this error happens because an array of array was returned. Using [`.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap) or a [`.flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat) call may be useful.

pages/blog/\[id].astro

```ts
export async function getStaticPaths() {
  return [ // <-- Array
    { params: { slug: "blog" } }, // <-- Object
    { params: { slug: "about" } }
  ];
}
```jsx
**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)

---

[← Previous](296-invalid-value-returned-by-a-getstaticpaths-path.md) | [Index](index.md) | [Next →](index.md)
