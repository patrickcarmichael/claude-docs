---
title: "Astro.redirect is not available in static mode."
section: 350
---

# Astro.redirect is not available in static mode.

Deprecated

Deprecated since version 2.6.

> **StaticRedirectNotAvailable**: Redirects are only available when using `output: 'server'` or `output: 'hybrid'`. Update your Astro config if you need SSR features.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.redirect` function is only available when [Server-side rendering](/en/guides/on-demand-rendering/) is enabled.

To redirect on a static website, the [meta refresh attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) can be used. Certain hosts also provide config-based redirects (ex: [Netlify redirects](https://docs.netlify.com/routing/redirects/)).

**See Also:**

* [Enabling SSR in Your Project](/en/guides/on-demand-rendering/)
* [Astro.redirect](/en/reference/api-reference/#redirect)

---

[← Previous](349-astroclientaddress-is-not-available-in-prerendered-pages.md) | [Index](index.md) | [Next →](index.md)
