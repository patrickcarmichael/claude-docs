---
title: "Image missing required "alt" property."
section: 286
---

# Image missing required "alt" property.

> **ImageMissingAlt**: Image missing “alt” property. “alt” text is required to describe important images on the page.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `alt` property allows you to provide descriptive alt text to users of screen readers and other assistive technologies. In order to ensure your images are accessible, the `Image` component requires that an `alt` be specified.

If the image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers know to ignore the image.

**See Also:**

* [Images](/en/guides/images/)
* [Image component](/en/reference/modules/astro-assets/#image-)
*  [Image component#alt](/en/reference/modules/astro-assets/#alt-required)

---

[← Previous](285-i18n-not-enabled.md) | [Index](index.md) | [Next →](index.md)
