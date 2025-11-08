---
title: "Images"
section: 121
---

# Images

> Learn how to use images in Astro.

Astro provides several ways for you to use images on your site, whether they are stored locally inside your project, linked to from an external URL, or managed in a CMS or CDN.

Astro provides built-in [`<Image />`](#image-) and [`<Picture />`](#picture-) Astro components, [Markdown image syntax](#images-in-markdown-files) (`![]()`) processing, [SVG components](#svg-components), and [an image generating function](#generating-images-with-getimage) to optimize and/or transform your images. Additionally, you can configure [automatically resizing responsive images](#responsive-image-behavior) by default, or set responsive properties on individual image and picture components.

You can always choose to use images and SVG files using native HTML elements in `.astro` or Markdown files, or the standard way for your file type (e.g. `<img />` in MDX and JSX). However, Astro does not perform any processing or optimization of these images.

There is also no native video support in Astro, and we recommend choosing a [hosted video service](/en/guides/media/) to handle the demands of optimizing and streaming video content.

See the full API reference for the [`<Image />`](/en/reference/modules/astro-assets/#image-) and [`<Picture />`](/en/reference/modules/astro-assets/#picture-) components.

## Where to store images

[Section titled “Where to store images”](#where-to-store-images)

### `src/` vs `public/`

[Section titled “src/ vs public/”](#src-vs-public)

We recommend that local images are kept in `src/` when possible so that Astro can transform, optimize, and bundle them. Files in the `public/` directory are always served or copied into the build folder as-is, with no processing.

Your local images stored in `src/` can be used by all files in your project: `.astro`, `.md`, `.mdx`, `.mdoc`, and other UI frameworks as file imports. Images can be stored in any folder, including alongside your content.

Store your images in the `public/` folder if you want to avoid any processing. These images are available to your project files as URL paths on your domain and allow you to have a direct public link to them. For example, your site favicon will commonly be placed in the root of this folder where browsers can identify it.

### Remote images

[Section titled “Remote images”](#remote-images)

You can also choose to store your images remotely, in a [content management system (CMS)](/en/guides/cms/) or [digital asset management (DAM)](/en/guides/media/) platform. Astro can fetch your data remotely using APIs or display images from their full URL path.

For extra protection when dealing with external sources, Astro’s image components and helper function will only process (e.g. optimize, transform) images from [authorized image sources specified in your configuration](#authorizing-remote-images). Remote images from other sources will be displayed with no processing.

## Images in `.astro` files

[Section titled “Images in .astro files”](#images-in-astro-files)

**Options:** `<Image />`, `<Picture />`, `<img>`, `<svg>`, SVG components

Astro’s templating language allows you to render optimized images with the Astro [`<Image />`](/en/reference/modules/astro-assets/#image-) component and generate multiple sizes and formats with the Astro [`<Picture />`](/en/reference/modules/astro-assets/#picture-) component. Both components also accept [responsive image properties](#responsive-image-behavior) for resizing based on container size and responding to device screen size and resolution.

Additionally, you can import and use [SVG files as Astro components](#svg-components) in `.astro` components.

All native HTML tags, including `<img>` and `<svg>`, are also available in `.astro` components. [Images rendered with HTML tags](#display-unprocessed-images-with-the-html-img-tag) will not be processed (e.g. optimized, transformed) and will be copied into your build folder as-is.

For all images in `.astro` files, **the value of the image `src` attribute is determined by the location of your image file**:

* A local image from your project `src/` folder uses an import from the file’s relative path.

  The image and picture components use the named import directly (e.g. `src={rocket}`), while the `<img>` tag uses the `src` object property of the import (e.g. `src={rocket.src}`).

* Remote and `public/` images use a URL path.

  Provide a full URL for remote images (e.g. `src="https://www.example.com/images/my-remote-image.jpg"`), or a relative URL path on your site that corresponds to your file’s location in your `public/` folder (e.g. `src="/images/my-public-image.jpg"` for an image located in `public/images/my-public-image.jpg`).

src/pages/blog/my-images.astro

```astro
---
import { Image } from 'astro:assets';
import localBirdImage from '../../images/subfolder/localBirdImage.png';
---
<Image src={localBirdImage} alt="A bird sitting on a nest of eggs." />
<Image src="/images/bird-in-public-folder.jpg" alt="A bird." width="50" height="50" />
<Image src="https://example.com/remote-bird.jpg" alt="A bird." width="50" height="50" />


<img src={localBirdImage.src} alt="A bird sitting on a nest of eggs.">
<img src="/images/bird-in-public-folder.jpg" alt="A bird.">
<img src="https://example.com/remote-bird.jpg" alt="A bird.">
```jsx
See the full API reference for the [`<Image />`](/en/reference/modules/astro-assets/#image-) and [`<Picture />`](/en/reference/modules/astro-assets/#picture-) components including required and optional properties.

![](/houston_chef.webp) **Related recipe:** [Dynamically import images](/en/recipes/dynamically-importing-images/)

## Images in Markdown files

[Section titled “Images in Markdown files”](#images-in-markdown-files)

**Options:** `![]()`, `<img>` (with public or remote images)

Use standard Markdown `![alt](src)` syntax in your `.md` files. Your local images stored in `src/` and remote images will be processed and optimized. When you [configure responsive images globally](/en/reference/configuration-reference/#imagelayout), these images will also be [responsive](#responsive-image-behavior).

Images stored in the `public/` folder are never optimized.

src/pages/post-1.md

```md

---

[← Previous](120-front-end-frameworks.md) | [Index](index.md) | [Next →](index.md)
