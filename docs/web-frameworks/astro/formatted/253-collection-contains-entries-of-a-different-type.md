---
title: "Collection contains entries of a different type."
section: 253
---

# Collection contains entries of a different type.

> **ContentCollectionTypeMismatchError**: COLLECTION contains EXPECTED\_TYPE entries, but is configured as a ACTUAL\_TYPE collection.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Legacy content collections must contain entries of the type configured. Collections are `type: 'content'` by default. Try adding `type: 'data'` to your collection config for data collections.

**See Also:**

* [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

---

[← Previous](252-specified-configuration-file-not-found.md) | [Index](index.md) | [Next →](index.md)
