---
title: "Sessions cannot be used with an adapter that doesn't support server output."
section: 348
---

# Sessions cannot be used with an adapter that doesn't support server output.

Deprecated

This error was removed in Astro 5.7, when the Sessions feature stopped being experimental.

> **SessionWithoutSupportedAdapterOutputError**: Sessions require an adapter that supports server output. The adapter must set `"server"` in the `buildOutput` adapter feature.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Your adapter must support server output to use sessions.

**See Also:**

* [Sessions](/en/guides/sessions/)

---

[← Previous](347-session-data-could-not-be-saved.md) | [Index](index.md) | [Next →](index.md)
