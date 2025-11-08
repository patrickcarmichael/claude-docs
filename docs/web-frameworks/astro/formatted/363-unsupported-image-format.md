---
title: "Unsupported image format"
section: 363
---

# Unsupported image format

> **UnsupportedImageFormat**: Received unsupported format `FORMAT` from `IMAGE_PATH`. Currently only SUPPORTED\_FORMATS.JOIN(’, ’) are supported by our image services.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The built-in image services do not currently support optimizing all image formats.

For unsupported formats such as GIFs, you may be able to use an `img` tag directly:

```astro
---
import rocket from '../assets/images/rocket.gif';
---


<img src={rocket.src} width={rocket.width} height={rocket.height} alt="A rocketship in space." />
```

---

[← Previous](362-unsupported-image-conversion.md) | [Index](index.md) | [Next →](index.md)
