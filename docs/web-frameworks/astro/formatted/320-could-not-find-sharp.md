---
title: "Could not find Sharp."
section: 320
---

# Could not find Sharp.

> **MissingSharp**: Could not find Sharp. Please install Sharp (`sharp`) manually into your project or migrate to another image service.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Sharp is the default image service used for `astro:assets`. When using a [strict package manager](https://pnpm.io/pnpm-vs-npm#npms-flat-tree) like pnpm, Sharp must be installed manually into your project in order to use image processing.

If you are not using `astro:assets` for image processing, and do not wish to install Sharp, you can configure the following passthrough image service that does no processing:

```js
import { defineConfig, passthroughImageService } from "astro/config";
export default defineConfig({
 image: {
   service: passthroughImageService(),
 },
});
```jsx
**See Also:**

* [Default Image Service](/en/guides/images/#default-image-service)
* [Image Services API](/en/reference/image-service-reference/)

---

[← Previous](319-enabled-manual-internationalization-routing-without-having-a-middleware.md) | [Index](index.md) | [Next →](index.md)
