---
title: "Pages"
section: 09
---

# Pages

> An introduction to Astro pages.

**Pages** are files that live in the `src/pages/` subdirectory of your Astro project. They are responsible for handling routing, data loading, and overall page layout for every page in your website.

## Supported page files

[Section titled “Supported page files”](#supported-page-files)

Astro supports the following file types in the `src/pages/` directory:

* [`.astro`](#astro-pages)
* [`.md`](#markdownmdx-pages)
* `.mdx` (with the [MDX Integration installed](/en/guides/integrations-guide/mdx/#installation))
* [`.html`](#html-pages)
* `.js`/`.ts` (as [endpoints](/en/guides/endpoints/))

## File-based routing

[Section titled “File-based routing”](#file-based-routing)

Astro leverages a routing strategy called **file-based routing**. Each file in your `src/pages/` directory becomes an endpoint on your site based on its file path.

A single file can also generate multiple pages using [dynamic routing](/en/guides/routing/#dynamic-routes). This allows you to create pages even if your content lives outside of the special `/pages/` directory, such as in a [content collection](/en/guides/content-collections/) or a [CMS](/en/guides/cms/).

Read more about [Routing in Astro](/en/guides/routing/).

### Link between pages

[Section titled “Link between pages”](#link-between-pages)

Write standard HTML [`<a>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) in your Astro pages to link to other pages on your site. Use a **URL path relative to your root domain** as your link, not a relative file path.

For example, to link to `https://example.com/authors/sonali/` from any other page on `example.com`:

src/pages/index.astro

```astro
Read more <a href="/authors/sonali/">about Sonali</a>.
```jsx
## Astro Pages

[Section titled “Astro Pages”](#astro-pages)

Astro pages use the `.astro` file extension and support the same features as [Astro components](/en/basics/astro-components/).

src/pages/index.astro

```astro
---
---
<html lang="en">
  <head>
    <title>My Homepage</title>
  </head>
  <body>
    <h1>Welcome to my website!</h1>
  </body>
</html>
```jsx
A page must produce a full HTML document. If not explicitly included, Astro will add the necessary `<!DOCTYPE html>` declaration and `<head>` content to any `.astro` component located within `src/pages/` by default. You can opt-out of this behavior on a per-component basis by marking it as a [partial](#page-partials) page.

To avoid repeating the same HTML elements on every page, you can move common `<head>` and `<body>` elements into your own [layout components](/en/basics/layouts/). You can use as many or as few layout components as you’d like.

src/pages/index.astro

```astro
---
import MySiteLayout from "../layouts/MySiteLayout.astro";
---
<MySiteLayout>
  <p>My page content, wrapped in a layout!</p>
</MySiteLayout>
```jsx
Read more about [layout components](/en/basics/layouts/) in Astro.

## Markdown/MDX Pages

[Section titled “Markdown/MDX Pages”](#markdownmdx-pages)

Astro also treats any Markdown (`.md`) files inside of `src/pages/` as pages in your final website. If you have the [MDX Integration installed](/en/guides/integrations-guide/mdx/#installation), it also treats MDX (`.mdx`) files the same way.

Tip

Consider creating [content collections](/en/guides/content-collections/) instead of pages for directories of related Markdown files that share a similar structure, such as blog posts or product items.

Markdown files can use the special `layout` frontmatter property to specify a [layout component](/en/basics/layouts/) that will wrap their Markdown content in a full `<html>...</html>` page document.

src/pages/page.md

```md
---
layout: ../layouts/MySiteLayout.astro
title: My Markdown page
---

---

[← Previous](08-components.md) | [Index](index.md) | [Next →](index.md)
