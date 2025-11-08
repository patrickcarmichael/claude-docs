---
title: "Astro.glob() used outside of an Astro file."
section: 241
---

# Astro.glob() used outside of an Astro file.

> **AstroGlobUsedOutside**: `Astro.glob(GLOB_STR)` can only be used in `.astro` files. `import.meta.glob(GLOB_STR)` can be used instead to achieve a similar result.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.glob()` can only be used in `.astro` files. You can use [`import.meta.glob()`](https://vite.dev/guide/features.html#glob-import) instead to achieve the same result.

**See Also:**

* [Astro.glob](/en/reference/api-reference/#astroglob)

---

[← Previous](240-astroglob-did-not-match-any-files.md) | [Index](index.md) | [Next →](index.md)
