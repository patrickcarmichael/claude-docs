---
title: "Markdown in Astro"
section: 152
---

# Markdown in Astro

> Learn about Astro's built-in support for Markdown.

[Markdown](https://daringfireball.net/projects/markdown/) is commonly used to author text-heavy content like blog posts and documentation. Astro includes built-in support for Markdown files that can also include [frontmatter YAML](https://dev.to/paulasantamaria/introduction-to-yaml-125f) (or [TOML](https://toml.io)) to define custom properties such as a title, description, and tags.

In Astro, you can author content in [GitHub Flavored Markdown](https://github.github.com/gfm/), then render it in `.astro` components. This combines a familiar writing format designed for content with the flexibility of Astro’s component syntax and architecture.

Tip

For additional functionality, such as including components and JSX expressions in Markdown, add the [`@astrojs/mdx` integration](/en/guides/integrations-guide/mdx/) to write your Markdown content using [MDX](https://mdxjs.com/).

## Organizing Markdown files

[Section titled “Organizing Markdown files”](#organizing-markdown-files)

Your local Markdown files can be kept anywhere within your `src/` directory. Markdown files located within `src/pages/` will automatically generate [Markdown pages on your site](#individual-markdown-pages).

Your Markdown content and frontmatter properties are available to use in components through [local file imports](#importing-markdown) or when [queried and rendered from data fetched by a content collections helper function](#markdown-from-content-collections-queries).

### File imports vs content collections queries

[Section titled “File imports vs content collections queries”](#file-imports-vs-content-collections-queries)

Local Markdown can be imported into `.astro` components using an `import` statement for a single file and [Vite’s `import.meta.glob()`](/en/guides/imports/#importmetaglob) to query multiple files at once. The [exported data from these Markdown files](#importing-markdown) can then be used in the `.astro` component.

If you have groups of related Markdown files, consider [defining them as collections](/en/guides/content-collections/). This gives you several advantages, including the ability to store Markdown files anywhere on your filesystem or remotely.

Collections use content-specific, optimized APIs for [querying and rendering your Markdown content](#markdown-from-content-collections-queries) instead of file imports. Collections are intended for sets of data that share the same structure, such as blog posts or product items. When you define that shape in a schema, you additionally get validation, type safety, and Intellisense in your editor.

See more about [when to use content collections](/en/guides/content-collections/#when-to-create-a-collection) instead of file imports.

## Dynamic JSX-like expressions

[Section titled “Dynamic JSX-like expressions”](#dynamic-jsx-like-expressions)

After importing or querying Markdown files, you can write dynamic HTML templates in your `.astro` components that include frontmatter data and body content.

src/pages/posts/great-post.md

```md
---
title: 'The greatest post of all time'
author: 'Ben'
---


Here is my _great_ post!
```jsx
src/pages/my-posts.astro

```astro
---
import * as greatPost from './posts/great-post.md';
const posts = Object.values(import.meta.glob('./posts/*.md', { eager: true }));
---


<p>{greatPost.frontmatter.title}</p>
<p>Written by: {greatPost.frontmatter.author}</p>


<p>Post Archive:</p>
<ul>
  {posts.map(post => <li><a href={post.url}>{post.frontmatter.title}</a></li>)}
</ul>
```jsx
### Available Properties

[Section titled “Available Properties”](#available-properties)

#### Markdown from content collections queries

[Section titled “Markdown from content collections queries”](#markdown-from-content-collections-queries)

When fetching data from your collections with the helper functions `getCollection()` or `getEntry()`, your Markdown’s frontmatter properties are available on a `data` object (e.g. `post.data.title`). Additionally, `body` contains the raw, uncompiled body content as a string.

The [`render()`](/en/reference/modules/astro-content/#render) function returns your Markdown body content, a generated list of headings, as well as a modified frontmatter object after any remark or rehype plugins have been applied.

Read more about [using content returned by a collections query](/en/guides/content-collections/#using-content-in-astro-templates).

#### Importing Markdown

[Section titled “Importing Markdown”](#importing-markdown)

The following exported properties are available in your `.astro` component when importing Markdown using `import` or `import.meta.glob()`:

* **`file`** - The absolute file path (e.g. `/home/user/projects/.../file.md`).
* **`url`** - The URL of the page (e.g. `/en/guides/markdown-content`).
* **`frontmatter`** - Contains any data specified in the file’s YAML (or TOML) frontmatter.
* **`<Content />`** - A component that returns the full, rendered contents of the file.
* **`rawContent()`** - A function that returns the raw Markdown document as a string.
* **`compiledContent()`** - An async function that returns the Markdown document compiled to an HTML string.
* **`getHeadings()`** - An async function that returns an array of all headings (`<h1>` to `<h6>`) in the file with the type: `{ depth: number; slug: string; text: string }[]`. Each heading’s `slug` corresponds to the generated ID for a given heading and can be used for anchor links.

An example Markdown blog post may pass the following `Astro.props` object:

```js
Astro.props = {
  file: "/home/user/projects/.../file.md",
  url: "/en/guides/markdown-content/",
  frontmatter: {
    /** Frontmatter from a blog post */
    title: "Astro 0.18 Release",
    date: "Tuesday, July 27 2021",
    author: "Matthew Phillips",
    description: "Astro 0.18 is our biggest release since Astro launch.",
  },
  getHeadings: () => [
    {"depth": 1, "text": "Astro 0.18 Release", "slug": "astro-018-release"},
    {"depth": 2, "text": "Responsive partial hydration", "slug": "responsive-partial-hydration"}
    /* ... */
  ],
  rawContent: () => "# Astro 0.18 Release\nA little over a month ago, the first public beta [...]",
  compiledContent: () => "<h1>Astro 0.18 Release</h1>\n<p>A little over a month ago, the first public beta [...]</p>",
}
```jsx
## The `<Content />` Component

[Section titled “The \<Content /> Component”](#the-content--component)

The `<Content />` component is available by importing `Content` from a Markdown file. This component returns the file’s full body content, rendered to HTML. You can optionally rename `Content` to any component name you prefer.

You can similarly [render the HTML content of a Markdown collection entry](/en/guides/content-collections/#rendering-body-content) by rendering a `<Content />` component.

src/pages/content.astro

```astro
---
// Import statement
import {Content as PromoBanner} from '../components/promoBanner.md';


// Collections query
import { getEntry, render } from 'astro:content';


const product = await getEntry('products', 'shirt');
const { Content } = await render(product);
---
<h2>Today's promo</h2>
<PromoBanner />


<p>Sale Ends: {product.data.saleEndDate.toDateString()}</p>
<Content />
```jsx
## Heading IDs

[Section titled “Heading IDs”](#heading-ids)

Writing headings in Markdown will automatically give you anchor links so you can link directly to certain sections of your page.

src/pages/page-1.md

```markdown
---
title: My page of content
---
## Introduction


I can link internally to [my conclusion](#conclusion) on the same page when writing Markdown.


## Conclusion


I can visit `https://example.com/page-1/#introduction` in a browser to navigate directly to my Introduction.
```jsx
Astro generates heading `id`s based on `github-slugger`. You can find more examples in [the github-slugger documentation](https://github.com/Flet/github-slugger#usage).

### Heading IDs and plugins

[Section titled “Heading IDs and plugins”](#heading-ids-and-plugins)

Astro injects an `id` attribute into all heading elements (`<h1>` to `<h6>`) in Markdown and MDX files. You can retrieve this data from the `getHeadings()` utility available as a [Markdown exported property](#available-properties) from an imported file, or from the `render()` function when [using Markdown returned from a content collections query](#markdown-from-content-collections-queries).

You can customize these heading IDs by adding a rehype plugin that injects `id` attributes (e.g. `rehype-slug`). Your custom IDs, instead of Astro’s defaults, will be reflected in the HTML output and the items returned by `getHeadings()`.

By default, Astro injects `id` attributes after your rehype plugins have run. If one of your custom rehype plugins needs to access the IDs injected by Astro, you can import and use Astro’s `rehypeHeadingIds` plugin directly. Be sure to add `rehypeHeadingIds` before any plugins that rely on it:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import { rehypeHeadingIds } from '@astrojs/markdown-remark';
import { otherPluginThatReliesOnHeadingIDs } from 'some/plugin/source';


export default defineConfig({
  markdown: {
    rehypePlugins: [
+      rehypeHeadingIds,
      otherPluginThatReliesOnHeadingIDs,
    ],
  },
});
```jsx
## Markdown Plugins

[Section titled “Markdown Plugins”](#markdown-plugins)

Markdown support in Astro is powered by [remark](https://remark.js.org/), a powerful parsing and processing tool with an active ecosystem. Other Markdown parsers like Pandoc and markdown-it are not currently supported.

Astro applies the [GitHub-flavored Markdown](https://github.com/remarkjs/remark-gfm) and [SmartyPants](https://github.com/silvenon/remark-smartypants) plugins by default. This brings some niceties like generating clickable links from text, and formatting for [quotations and em-dashes](https://daringfireball.net/projects/smartypants/).

You can customize how remark parses your Markdown in `astro.config.mjs`. See the full list of [Markdown configuration options](/en/reference/configuration-reference/#markdown-options).

### Adding remark and rehype plugins

[Section titled “Adding remark and rehype plugins”](#adding-remark-and-rehype-plugins)

Astro supports adding third-party [remark](https://github.com/remarkjs/remark) and [rehype](https://github.com/rehypejs/rehype) plugins for Markdown. These plugins allow you to extend your Markdown with new capabilities, like [auto-generating a table of contents](https://github.com/remarkjs/remark-toc), [applying accessible emoji labels](https://github.com/florianeckerstorfer/remark-a11y-emoji), and [styling your Markdown](/en/guides/styling/#markdown-styling).

We encourage you to browse [awesome-remark](https://github.com/remarkjs/awesome-remark) and [awesome-rehype](https://github.com/rehypejs/awesome-rehype) for popular plugins! See each plugin’s own README for specific installation instructions.

This example applies [`remark-toc`](https://github.com/remarkjs/remark-toc) and [`rehype-accessible-emojis`](https://www.npmjs.com/package/rehype-accessible-emojis) to Markdown files:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import remarkToc from 'remark-toc';
import { rehypeAccessibleEmojis } from 'rehype-accessible-emojis';


export default defineConfig({
  markdown: {
    remarkPlugins: [ [remarkToc, { heading: 'toc', maxDepth: 3 } ] ],
    rehypePlugins: [rehypeAccessibleEmojis],
  },
});
```jsx
### Customizing a plugin

[Section titled “Customizing a plugin”](#customizing-a-plugin)

In order to customize a plugin, provide an options object after it in a nested array.

The example below adds the [heading option to the `remarkToc` plugin](https://github.com/remarkjs/remark-toc#options) to change where the table of contents is placed, and the [`behavior` option to the `rehype-autolink-headings` plugin](https://github.com/rehypejs/rehype-autolink-headings#options) in order to add the anchor tag after the headline text.

astro.config.mjs

```js
import remarkToc from 'remark-toc';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';


export default {
  markdown: {
    remarkPlugins: [ [remarkToc, { heading: "contents"} ] ],
    rehypePlugins: [rehypeSlug, [rehypeAutolinkHeadings, { behavior: 'append' }]],
  },
}
```jsx
### Modifying frontmatter programmatically

[Section titled “Modifying frontmatter programmatically”](#modifying-frontmatter-programmatically)

You can add frontmatter properties to all of your Markdown and MDX files by using a [remark or rehype plugin](#markdown-plugins).

1. Append a `customProperty` to the `data.astro.frontmatter` property from your plugin’s `file` argument:

   example-remark-plugin.mjs

   ```js
   export function exampleRemarkPlugin() {
     // All remark and rehype plugins return a separate function
     return function (tree, file) {
       file.data.astro.frontmatter.customProperty = 'Generated property';
     }
   }
   ```jsx
   Tip

   **Added in:** `astro@2.0.0`

   `data.astro.frontmatter` contains all properties from a given Markdown or MDX document. This allows you to modify existing frontmatter properties, or compute new properties from this existing frontmatter.

2. Apply this plugin to your `markdown` or `mdx` integration config:

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { exampleRemarkPlugin } from './example-remark-plugin.mjs';


   export default defineConfig({
     markdown: {
       remarkPlugins: [exampleRemarkPlugin]
     },
   });
   ```jsx
   or

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { exampleRemarkPlugin } from './example-remark-plugin.mjs';


   export default defineConfig({
     integrations: [
       mdx({
         remarkPlugins: [exampleRemarkPlugin],
       }),
     ],
   });
   ```jsx
Now, every Markdown or MDX file will have `customProperty` in its frontmatter, making it available when [importing your markdown](#importing-markdown) and from [the `Astro.props.frontmatter` property in your layouts](#frontmatter-layout-property).

![](/houston_chef.webp) **Related recipe:** [Add reading time](/en/recipes/reading-time/)

### Extending Markdown config from MDX

[Section titled “Extending Markdown config from MDX”](#extending-markdown-config-from-mdx)

Astro’s MDX integration will extend [your project’s existing Markdown configuration](/en/reference/configuration-reference/#markdown-options) by default. To override individual options, you can specify their equivalent in your MDX configuration.

The following example disables GitHub-Flavored Markdown and applies a different set of remark plugins for MDX files:

astro.config.mjs

```ts
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  markdown: {
    syntaxHighlight: 'prism',
    remarkPlugins: [remarkPlugin1],
    gfm: true,
  },
  integrations: [
    mdx({
      // `syntaxHighlight` inherited from Markdown


      // Markdown `remarkPlugins` ignored,
      // only `remarkPlugin2` applied.
      remarkPlugins: [remarkPlugin2],
      // `gfm` overridden to `false`
      gfm: false,
    })
  ]
});
```jsx
To avoid extending your Markdown config from MDX, set [the `extendMarkdownConfig` option](/en/guides/integrations-guide/mdx/#extendmarkdownconfig) (enabled by default) to `false`:

astro.config.mjs

```ts
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  markdown: {
    remarkPlugins: [remarkPlugin],
  },
  integrations: [
    mdx({
      // Markdown config now ignored
      extendMarkdownConfig: false,
      // No `remarkPlugins` applied
    })
  ]
});
```jsx
## Individual Markdown pages

[Section titled “Individual Markdown pages”](#individual-markdown-pages)

Tip

[Content collections](/en/guides/content-collections/) and [importing Markdown into `.astro` components](#dynamic-jsx-like-expressions) provide more features for rendering your Markdown and are the recommended way to handle most of your content. However, there may be times when you want the convenience of just adding a file to `src/pages/` and having a simple page automatically created for you.

Astro treats [any supported file inside of the `/src/pages/` directory](/en/basics/astro-pages/#supported-page-files) as a page, including `.md` and other Markdown file types.

Placing a file in this directory, or any sub-directory, will automatically build a page route using the pathname of the file and display the Markdown content rendered to HTML. Astro will automatically add a `<meta charset="utf-8">` tag to your page to allow easier authoring of non-ASCII content.

src/pages/page-1.md

```markdown
---
title: Hello, World
---

---

[← Previous](151-internationalization-i18n-routing.md) | [Index](index.md) | [Next →](index.md)
