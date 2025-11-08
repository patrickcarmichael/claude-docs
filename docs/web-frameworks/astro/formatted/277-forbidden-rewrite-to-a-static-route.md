---
title: "Forbidden rewrite to a static route."
section: 277
---

# Forbidden rewrite to a static route.

> **ForbiddenRewrite**: You tried to rewrite the on-demand route ‘FROM’ with the static route ‘TO’, when using the ‘server’ output.\
> \
> The static route ‘TO’ is rendered by the component ‘COMPONENT’, which is marked as prerendered. This is a forbidden operation because during the build the component ‘COMPONENT’ is compiled to an HTML file, which can’t be retrieved at runtime by Astro.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.rewrite()` can’t be used to rewrite an on-demand route with a static route when using the `"server"` output.

---

[← Previous](276-font-family-not-found.md) | [Index](index.md) | [Next →](index.md)
