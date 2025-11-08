---
title: "Routing"
section: 176
---

# Routing

> An intro to routing with Astro.

Astro uses **file-based routing** to generate your build URLs based on the file layout of your project `src/pages/` directory.

## Navigating between pages

[Section titled “Navigating between pages”](#navigating-between-pages)

Astro uses standard HTML [`<a>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) to navigate between routes. There is no framework-specific `<Link>` component provided.

src/pages/index.astro

```astro
<p>Read more <a href="/about/">about</a> Astro!</p>


<!-- With `base: "/docs"` configured -->
<p>Learn more in our <a href="/docs/reference/">reference</a> section!</p>
```jsx
## Static routes

[Section titled “Static routes”](#static-routes)

`.astro` [page components](/en/basics/astro-pages/) as well as Markdown and MDX Files (`.md`, `.mdx`) within the `src/pages/` directory **automatically become pages on your website**. Each page’s route corresponds to its path and filename within the `src/pages/` directory.

```diff

---

[← Previous](175-prefetch.md) | [Index](index.md) | [Next →](index.md)
