---
title: "Content collection frontmatter invalid."
section: 308
---

# Content collection frontmatter invalid.

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **Example error message:**\
> Could not parse frontmatter in **blog** → **post.md**\
> “title” is required.\
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A Markdown document’s frontmatter in `src/content/` does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content/config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

---

[← Previous](307-locals-must-not-be-reassigned.md) | [Index](index.md) | [Next →](index.md)
