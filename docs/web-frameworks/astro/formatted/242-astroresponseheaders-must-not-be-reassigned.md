---
title: "Astro.response.headers must not be reassigned."
section: 242
---

# Astro.response.headers must not be reassigned.

> **AstroResponseHeadersReassigned**: Individual headers can be added to and removed from `Astro.response.headers`, but it must not be replaced with another instance of `Headers` altogether.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when a value is being set as the `headers` field on the `ResponseInit` object available as `Astro.response`.

---

[← Previous](241-astroglob-used-outside-of-an-astro-file.md) | [Index](index.md) | [Next →](index.md)
