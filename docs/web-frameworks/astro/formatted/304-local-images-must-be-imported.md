---
title: "Local images must be imported."
section: 304
---

# Local images must be imported.

> **LocalImageUsedWrongly**: `Image`’s and `getImage`’s `src` parameter must be an imported image or an URL, it cannot be a string filepath. Received `IMAGE_FILE_PATH`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

When using the default image services, `Image`’s and `getImage`’s `src` parameter must be either an imported image or an URL, it cannot be a string of a filepath.

For local images from content collections, you can use the [image() schema helper](/en/guides/images/#images-in-content-collections) to resolve the images.

```astro
---
import { Image } from "astro:assets";
import myImage from "../my_image.png";
---


<!-- GOOD: `src` is the full imported image. -->
<Image src={myImage} alt="Cool image" />


<!-- GOOD: `src` is a URL. -->
<Image src="https://example.com/my_image.png" alt="Cool image" />


<!-- BAD: `src` is an image's `src` path instead of the full image object. -->
<Image src={myImage.src} alt="Cool image" />


<!-- BAD: `src` is a string filepath. -->
<Image src="../my_image.png" alt="Cool image" />
```jsx
**See Also:**

* [Images](/en/guides/images/)

---

[← Previous](303-error-in-live-content-config.md) | [Index](index.md) | [Next →](index.md)
