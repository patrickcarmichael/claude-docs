---
title: "Expected image options, not an ESM-imported image."
section: 269
---

# Expected image options, not an ESM-imported image.

> **ExpectedNotESMImage**: An ESM-imported image cannot be passed directly to `getImage()`. Instead, pass an object with the image in the `src` property.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An ESM-imported image cannot be passed directly to `getImage()`. Instead, pass an object with the image in the `src` property.

```diff
import { getImage } from "astro:assets";
import myImage from "../assets/my_image.png";
 const optimizedImage = await getImage( myImage );
 const optimizedImage = await getImage({ src: myImage });
```jsx
**See Also:**

* [Images](/en/guides/images/)

---

[← Previous](268-expected-image-options.md) | [Index](index.md) | [Next →](index.md)
