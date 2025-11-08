---
title: "My Markdown Page"
section: 122
---

# My Markdown Page


<!-- Local image stored in src/assets/ -->
<!-- Use a relative file path or import alias -->
![A starry night sky.](../assets/stars.png)


<!-- Image stored in public/images/ -->
<!-- Use the file path relative to public/ -->
![A starry night sky.](/images/stars.png)


<!-- Remote image on another server -->
<!-- Use the full URL of the image -->
![Astro](https://example.com/images/remote-image.png)
```jsx
The HTML `<img>` tag can also be used to display images stored in `public/` or remote images without any image optimization or processing. However, `<img>` is not supported for your local images in `src`.

The `<Image />` and `<Picture />` components are unavailable in `.md` files. If you require more control over your image attributes, we recommend using [Astro’s MDX integration](/en/guides/integrations-guide/mdx/) to add support for `.mdx` file format. MDX allows additional [image options available in MDX](#images-in-mdx-files), including combining components with Markdown syntax.

## Images in MDX files

[Section titled “Images in MDX files”](#images-in-mdx-files)

**Options:** `<Image />`, `<Picture />`, `<img />`, `![]()`, SVG components

You can use Astro’s `<Image />` and `<Picture />` components in your `.mdx` files by importing both the component and your image. Use them just as they are [used in `.astro` files](#images-in-astro-files). The JSX `<img />` tag is also supported for unprocessed images and [uses the same image import as the HTML `<img>` tag](#display-unprocessed-images-with-the-html-img-tag).

Additionally, there is support for [standard Markdown `![alt](src)` syntax](#images-in-markdown-files) with no import required.

src/pages/post-1.mdx

```mdx
---
title: My Page title
---
import { Image } from 'astro:assets';
import rocket from '../assets/rocket.png';

---

[← Previous](121-images.md) | [Index](index.md) | [Next →](index.md)
