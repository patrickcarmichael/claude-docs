---
title: "{title}"
section: 137
---

# {title}
```jsx
Or you can use that exported `title` in your page using `import` and `import.meta.glob()` statements:

src/pages/index.astro

```astro
---
const matches = import.meta.glob('./posts/*.mdx', { eager: true });
const posts = Object.values(matches);
---


{posts.map(post => <p>{post.title}</p>)}
```jsx
#### Exported Properties

[Section titled “Exported Properties”](#exported-properties)

The following properties are available to a `.astro` component when using an `import` statement or `import.meta.glob()`:

* **`file`** - The absolute file path (e.g. `/home/user/projects/.../file.mdx`).
* **`url`** - The URL of the page (e.g. `/en/guides/markdown-content`).
* **`frontmatter`** - Contains any data specified in the file’s YAML/TOML frontmatter.
* **`getHeadings()`** - An async function that returns an array of all headings (`<h1>` to `<h6>`) in the file with the type: `{ depth: number; slug: string; text: string }[]`. Each heading’s `slug` corresponds to the generated ID for a given heading and can be used for anchor links.
* **`<Content />`** - A component that returns the full, rendered contents of the file.
* **(any `export` value)** - MDX files can also export data with an `export` statement.

### Using Frontmatter Variables in MDX

[Section titled “Using Frontmatter Variables in MDX”](#using-frontmatter-variables-in-mdx)

The Astro MDX integration includes support for using frontmatter in MDX by default. Add frontmatter properties just as you would in Markdown files, and these variables are available to use in the template, and as named properties when importing the file somewhere else.

/src/blog/posts/post-1.mdx

```mdx
---
title: 'My first MDX post'
author: 'Houston'
---

---

[← Previous](136-astrojsmdx.md) | [Index](index.md) | [Next →](index.md)
