---
title: "Expected image options."
section: 268
---

# Expected image options.

> **ExpectedImageOptions**: Expected getImage() parameter to be an object. Received `OPTIONS`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getImage()`’s first parameter should be an object with the different properties to apply to your image.

```ts
import { getImage } from "astro:assets";
import myImage from "../assets/my_image.png";


const optimizedImage = await getImage({src: myImage, width: 300, height: 300});
```jsx
In most cases, this error happens because parameters were passed directly instead of inside an object.

**See Also:**

* [Images](/en/guides/images/)

---

[← Previous](267-expected-src-to-be-an-image.md) | [Index](index.md) | [Next →](index.md)
