---
title: "The path doesn't contain any locale"
section: 284
---

# The path doesn't contain any locale

> **i18nNoLocaleFoundInPath**: You tried to use an i18n utility on a path that doesn’t contain any locale. You can use `pathHasLocale` first to determine if the path has a locale.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An i18n utility tried to use the locale from a URL path that does not contain one. You can prevent this error by using pathHasLocale to check URLs for a locale first before using i18n utilities.

---

[← Previous](283-getstaticpaths-function-required-for-dynamic-routes.md) | [Index](index.md) | [Next →](index.md)
