---
title: "getStaticPaths() function required for dynamic routes."
section: 283
---

# getStaticPaths() function required for dynamic routes.

> **GetStaticPathsRequired**: `getStaticPaths()` function is required for dynamic routes. Make sure that you `export` a `getStaticPaths` function from your dynamic route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

In [Static Mode](/en/guides/routing/#static-ssg-mode), all routes must be determined at build time. As such, dynamic routes must `export` a `getStaticPaths` function returning the different paths to generate.

**See Also:**

* [Dynamic Routes](/en/guides/routing/#dynamic-routes)
* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [Server-side Rendering](/en/guides/on-demand-rendering/)

---

[← Previous](282-getstaticpaths-rss-helper-is-not-available-anymore.md) | [Index](index.md) | [Next →](index.md)
