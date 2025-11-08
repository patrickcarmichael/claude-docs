---
title: "Glob patterns are not supported in the file loader"
section: 274
---

# Glob patterns are not supported in the file loader

> **FileGlobNotSupported**: Glob patterns are not supported in the `file` loader. Use the `glob` loader instead.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `file` loader must be passed a single local file. Glob patterns are not supported. Use the built-in `glob` loader to create entries from patterns of multiple local files.

**See Also:**

* [Astro’s built-in loaders](/en/guides/content-collections/#built-in-loaders)

---

[← Previous](273-could-not-import-file.md) | [Index](index.md) | [Next →](index.md)
