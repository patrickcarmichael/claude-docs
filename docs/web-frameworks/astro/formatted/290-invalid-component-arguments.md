---
title: "Invalid component arguments."
section: 290
---

# Invalid component arguments.

> **Example error messages:**\
> InvalidComponentArgs: Invalid arguments passed to `<MyAstroComponent>` component.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro components cannot be rendered manually via a function call, such as `Component()` or `{items.map(Component)}`. Prefer the component syntax `<Component />` or `{items.map(item => <Component {...item} />)}`.

---

[← Previous](289-you-cant-use-the-current-function-with-the-current-strategy.md) | [Index](index.md) | [Next →](index.md)
