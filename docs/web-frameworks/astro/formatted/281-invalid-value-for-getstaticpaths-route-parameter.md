---
title: "Invalid value for getStaticPaths route parameter."
section: 281
---

# Invalid value for getStaticPaths route parameter.

> **GetStaticPathsInvalidRouteParam**: Invalid getStaticPaths route parameter for `KEY`. Expected undefined, a string or a number, received `VALUE_TYPE` (`VALUE`)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Since `params` are encoded into the URL, only certain types are supported as values.

/route/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: '1' } } // Works
    { params: { id: 2 } } // Works
    { params: { id: false } } // Does not work
  ];
}
---
```jsx
In routes using [rest parameters](/en/guides/routing/#rest-parameters), `undefined` can be used to represent a path with no parameters passed in the URL:

/route/\[...id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: 1 } } // /route/1
    { params: { id: 2 } } // /route/2
    { params: { id: undefined } } // /route/
  ];
}
---
```jsx
**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

---

[← Previous](280-missing-params-property-on-getstaticpaths-route.md) | [Index](index.md) | [Next →](index.md)
