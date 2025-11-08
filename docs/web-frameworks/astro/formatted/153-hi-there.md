---
title: "Hi there!"
section: 153
---

# Hi there!


This Markdown file creates a page at `your-domain.com/page-1/`


It probably isn't styled much, but Markdown does support:
- **bold** and _italics._
- lists
- [links](https://astro.build)
- <p>HTML elements</p>
- and more!
```jsx
### Frontmatter `layout` property

[Section titled “Frontmatter layout property”](#frontmatter-layout-property)

To help with the limited functionality of individual Markdown pages, Astro provides a special frontmatter `layout` property which is a relative path to an Astro [Markdown layout component](/en/basics/layouts/#markdown-layouts). `layout` is not a special property when using [content collections](/en/guides/content-collections/) to query and render your Markdown content, and is not guaranteed to be supported outside of its intended use case.

If your Markdown file is located within `src/pages/`, create a layout component and add it in this layout property to provide a page shell around your Markdown content.

src/pages/posts/post-1.md

```markdown
---
layout: ../../layouts/BlogPostLayout.astro
title: Astro in brief
author: Himanshu
description: Find out what makes Astro awesome!
---
This is a post written in Markdown.
```jsx
This layout component is a regular Astro component with [specific properties automatically available](/en/basics/layouts/#markdown-layout-props) through `Astro.props` for your Astro template. For example, you can access your Markdown file’s frontmatter properties through `Astro.props.frontmatter`:

src/layouts/BlogPostLayout.astro

```astro
---
const {frontmatter} = Astro.props;
---
<html>
  <head>
    <!-- ... -->
    <meta charset="utf-8"> // no longer added by default
  </head>
  <!-- ... -->
  <h1>{frontmatter.title}</h1>
  <h2>Post author: {frontmatter.author}</h2>
  <p>{frontmatter.description}</p>
  <slot /> <!-- Markdown content is injected here -->
  <!-- ... -->
</html>
```jsx
When using the frontmatter `layout` property, you must include the `<meta charset="utf-8">` tag in your layout as Astro will no longer add it automatically. You can now also [style your Markdown](/en/guides/styling/#markdown-styling) in your layout component.

Learn more about [Markdown Layouts](/en/basics/layouts/#markdown-layouts).

## Fetching Remote Markdown

[Section titled “Fetching Remote Markdown”](#fetching-remote-markdown)

Astro’s internal Markdown processor is not available for processing remote Markdown.

To fetch remote Markdown for use in [content collections](/en/guides/content-collections/), you can [build a custom loader](/en/guides/content-collections/#building-a-custom-loader) with access to a [`renderMarkdown()` function](/en/reference/content-loader-reference/#rendermarkdown).

To fetch remote Markdown directly and render it to HTML, you will need to install and configure your own Markdown parser from NPM. This will not inherit from any of Astro’s built-in Markdown settings that you have configured.

Be sure that you understand these limitations before implementing this in your project, and consider fetching your remote Markdown using a content collections loader instead.

src/pages/remote-example.astro

```astro
---
// Example: Fetch Markdown from a remote API
// and render it to HTML, at runtime.
// Using "marked" (https://github.com/markedjs/marked)
import { marked } from 'marked';
const response = await fetch('https://raw.githubusercontent.com/wiki/adam-p/markdown-here/Markdown-Cheatsheet.md');
const markdown = await response.text();
const content = marked.parse(markdown);
---
<article set:html={content} />
```

---

[← Previous](152-markdown-in-astro.md) | [Index](index.md) | [Next →](index.md)
