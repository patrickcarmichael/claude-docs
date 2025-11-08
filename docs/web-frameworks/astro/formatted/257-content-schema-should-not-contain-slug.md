---
title: "Content Schema should not contain slug."
section: 257
---

# Content Schema should not contain slug.

> **ContentSchemaContainsSlugError**: A content collection schema should not contain `slug` since it is reserved for slug generation. Remove this from your COLLECTION\_NAME collection schema.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A legacy content collection schema should not contain the `slug` field. This is reserved by Astro for generating entry slugs. Remove `slug` from your schema. You can still use custom slugs in your frontmatter.

**See Also:**

* [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

---

[← Previous](256-content-loader-returned-an-entry-with-an-invalid-id.md) | [Index](index.md) | [Next →](index.md)
