---
title: "You can't use the current function with the current strategy"
section: 289
---

# You can't use the current function with the current strategy

> **IncorrectStrategyForI18n**: The function `FUNCTION_NAME` can only be used when the `i18n.routing.strategy` is set to `"manual"`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Some internationalization functions are only available when Astro’s own i18n routing is disabled by the configuration setting `i18n.routing: "manual"`.

**See Also:**

* [`i18n` routing](/en/guides/internationalization/#routing)

---

[← Previous](288-cannot-set-both-densities-and-widths.md) | [Index](index.md) | [Next →](index.md)
