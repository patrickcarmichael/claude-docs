---
title: "Missing image dimensions"
section: 315
---

# Missing image dimensions

> Missing width and height attributes for `IMAGE_URL`. When using remote images, both dimensions are required in order to avoid cumulative layout shift (CLS).

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

For remote images, `width` and `height` cannot automatically be inferred from the original file. To avoid cumulative layout shift (CLS), either specify these two properties, or set [`inferSize`](/en/reference/modules/astro-assets/#infersize) to `true` to fetch a remote image’s original dimensions.

If your image is inside your `src` folder, you probably meant to import it instead. See [the Imports guide for more information](/en/guides/imports/#other-assets).

**See Also:**

* [Images](/en/guides/images/)
* [Image component#width-and-height-required](/en/reference/modules/astro-assets/#width-and-height-required-for-images-in-public)

---

[← Previous](314-the-middleware-returned-something-that-is-not-a-response-object.md) | [Index](index.md) | [Next →](index.md)
