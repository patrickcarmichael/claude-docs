---
title: "No static path found for requested path."
section: 329
---

# No static path found for requested path.

> **NoMatchingStaticPathFound**: A `getStaticPaths()` route pattern was matched, but no matching static path was found for requested path `PATH_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A [dynamic route](/en/guides/routing/#dynamic-routes) was matched, but no corresponding path was found for the requested parameters. This is often caused by a typo in either the generated or the requested path.

**See Also:**

* [getStaticPaths()](/en/reference/routing-reference/#getstaticpaths)

---

[← Previous](328-no-matching-renderer-found.md) | [Index](index.md) | [Next →](index.md)
