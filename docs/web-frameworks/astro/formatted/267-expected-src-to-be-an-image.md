---
title: "Expected src to be an image."
section: 267
---

# Expected src to be an image.

> **ExpectedImage**: Expected `src` property for `getImage` or `<Image />` to be either an ESM imported image or a string with the path of a remote image. Received `SRC` (type: `TYPEOF_OPTIONS`).\
> \
> Full serialized options received: `FULL_OPTIONS`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An image’s `src` property is not valid. The Image component requires the `src` attribute to be either an image that has been ESM imported or a string. This is also true for the first parameter of `getImage()`.

```astro
---
import { Image } from "astro:assets";
import myImage from "../assets/my_image.png";
---


<Image src={myImage} alt="..." />
<Image src="https://example.com/logo.png" width={300} height={300} alt="..." />
```jsx
In most cases, this error happens when the value passed to `src` is undefined.

**See Also:**

* [Images](/en/guides/images/)

---

[← Previous](266-unsupported-astroenv-getsecret.md) | [Index](index.md) | [Next →](index.md)
