---
title: "{frontmatter.title}"
section: 138
---

# {frontmatter.title}


Written by: {frontmatter.author}
```jsx
### Using Components in MDX

[Section titled “Using Components in MDX”](#using-components-in-mdx)

After installing the MDX integration, you can import and use both [Astro components](/en/basics/astro-components/) and [UI framework components](/en/guides/framework-components/#using-framework-components) in MDX (`.mdx`) files just as you would use them in any other Astro component.

Don’t forget to include a `client:directive` on your UI framework components, if necessary!

See more examples of using import and export statements in the [MDX docs](https://mdxjs.com/docs/what-is-mdx/#esm).

src/blog/post-1.mdx

```mdx
---
title: My first post
---
import ReactCounter from '../components/ReactCounter.jsx';


I just started my new Astro blog!


Here is my counter component, working in MDX:
<ReactCounter client:load />
```jsx
#### Assigning Custom Components to HTML elements

[Section titled “Assigning Custom Components to HTML elements”](#assigning-custom-components-to-html-elements)

With MDX, you can map Markdown syntax to custom components instead of their standard HTML elements. This allows you to write in standard Markdown syntax, but apply special component styling to selected elements.

For example, you can create a `Blockquote.astro` component to provide custom styling for `<blockquote>` content:

src/components/Blockquote.astro

```astro
---
const props = Astro.props;
---
<blockquote {...props} class="bg-blue-50 p-4">
  <span class="text-4xl text-blue-600 mb-2">“</span>
  <slot /> <!-- Be sure to add a `<slot/>` for child content! -->
</blockquote>
```jsx
Import your custom component into your `.mdx` file, then export a `components` object that maps the standard HTML element to your custom component:

src/blog/posts/post-1.mdx

```mdx
import Blockquote from '../components/Blockquote.astro';
export const components = {blockquote: Blockquote}


> This quote will be a custom Blockquote
```jsx
Visit the [MDX website](https://mdxjs.com/table-of-components/) for a full list of HTML elements that can be overwritten as custom components.

Note

Custom components defined and exported in an MDX file must always be imported and then passed back to the `<Content />` component via the `components` property.

#### Passing `components` to MDX content

[Section titled “Passing components to MDX content”](#passing-components-to-mdx-content)

When rendering imported MDX content with the `<Content />` component, including rendering MDX entries using content collections, custom components can be passed via the `components` prop. These components must first be imported to make them available to the `<Content />` component.

The `components` object maps HTML element names (`h1`, `h2`, `blockquote`, etc.) to your custom components. You can also include [all components exported from the MDX file itself](#assigning-custom-components-to-html-elements) using the spread operator (`...`), which must also be imported from your MDX file as `components`.

If you are importing MDX directly from a single file for use in an Astro component, import both the `Content` component and any exported components from your MDX file.

src/pages/page.astro

```astro
---
import { Content, components } from '../content.mdx';
import Heading from '../Heading.astro';
---
<!-- Creates a custom <h1> for the # syntax, _and_ applies any custom components defined in `content.mdx` -->
<Content components={{...components, h1: Heading }} />
```jsx
If your MDX file is a content collections entry, then use the `render()` function from `astro:content` to access the `<Content />` component.

The following example passes a custom heading to the `<Content />` component via the `components` prop to be used in place of all `<h1>` HTML elements:

src/pages/blog/post-1.astro

```astro
---
import { getEntry, render } from 'astro:content';
import CustomHeading from '../../components/CustomHeading.astro';
const entry = await getEntry('blog', 'post-1');
const { Content } = await render(entry);
---
<Content components={{ h1: CustomHeading }} />
```jsx
## Configuration

[Section titled “Configuration”](#configuration)

Once the MDX integration is installed, no configuration is necessary to use `.mdx` files in your Astro project.

You can configure how your MDX is rendered with the following options:

* [Options inherited from Markdown config](#options-inherited-from-markdown-config)
* [`extendMarkdownConfig`](#extendmarkdownconfig)
* [`recmaPlugins`](#recmaplugins)
* [`optimize`](#optimize)

### Options inherited from Markdown config

[Section titled “Options inherited from Markdown config”](#options-inherited-from-markdown-config)

All [`markdown` configuration options](/en/reference/configuration-reference/#markdown-options) can be configured separately in the MDX integration. This includes remark and rehype plugins, syntax highlighting, and more. Options will default to those in your Markdown config ([see the `extendMarkdownConfig` option](#extendmarkdownconfig) to modify this).

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import remarkToc from 'remark-toc';
import rehypePresetMinify from 'rehype-preset-minify';


export default defineConfig({
  // ...
  integrations: [
    mdx({
      syntaxHighlight: 'shiki',
      shikiConfig: { theme: 'dracula' },
      remarkPlugins: [remarkToc],
      rehypePlugins: [rehypePresetMinify],
      remarkRehype: { footnoteLabel: 'Footnotes' },
      gfm: false,
    }),
  ],
});
```jsx
Caution

MDX does not support passing remark and rehype plugins as a string. You should install, import, and apply the plugin function instead.

See the [Markdown Options reference](/en/reference/configuration-reference/#markdown-options) for a complete list of options.

### `extendMarkdownConfig`

[Section titled “extendMarkdownConfig”](#extendmarkdownconfig)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `@astrojs/mdx@0.15.0`

MDX will extend [your project’s existing Markdown configuration](/en/reference/configuration-reference/#markdown-options) by default. To override individual options, you can specify their equivalent in your MDX configuration.

For example, say you need to disable GitHub-Flavored Markdown and apply a different set of remark plugins for MDX files. You can apply these options like so, with `extendMarkdownConfig` enabled by default:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  // ...
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
    }),
  ],
});
```jsx
You may also need to disable `markdown` config extension in MDX. For this, set `extendMarkdownConfig` to `false`:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  // ...
  markdown: {
    remarkPlugins: [remarkPlugin1],
  },
  integrations: [
    mdx({
      // Markdown config now ignored
      extendMarkdownConfig: false,
      // No `remarkPlugins` applied
    }),
  ],
});
```jsx
### `recmaPlugins`

[Section titled “recmaPlugins”](#recmaplugins)

**Type:** `PluggableList`\
**Default:** `[]`

**Added in:** `@astrojs/mdx@0.11.5`

These are plugins that modify the output [estree](https://github.com/estree/estree) directly. This is useful for modifying or injecting JavaScript variables in your MDX files.

We suggest [using AST Explorer](https://astexplorer.net/) to play with estree outputs, and trying [`estree-util-visit`](https://unifiedjs.com/explore/package/estree-util-visit/) for searching across JavaScript nodes.

### `optimize`

[Section titled “optimize”](#optimize)

**Type:** `boolean | { ignoreElementNames?: string[] }`\
**Default:** `false`

**Added in:** `@astrojs/mdx@0.19.5`

This is an optional configuration setting to optimize the MDX output for faster builds and rendering via an internal rehype plugin. This may be useful if you have many MDX files and notice slow builds. However, this option may generate some unescaped HTML, so make sure your site’s interactive parts still work correctly after enabling it.

This is disabled by default. To enable MDX optimization, add the following to your MDX integration configuration:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  // ...
  integrations: [
    mdx({
      optimize: true,
    }),
  ],
});
```jsx
#### `ignoreElementNames`

[Section titled “ignoreElementNames”](#ignoreelementnames)

**Type:** `string[]`

**Added in:** `@astrojs/mdx@3.0.0`

Previously known as `customComponentNames`.

An optional property of `optimize` to prevent the MDX optimizer from handling certain element names, like [custom components passed to imported MDX content via the components prop](#passing-components-to-mdx-content).

You will need to exclude these components from optimization as the optimizer eagerly converts content into a static string, which will break custom components that needs to be dynamically rendered.

For example, the intended MDX output of the following is `<Heading>...</Heading>` in place of every `"<h1>...</h1>"`:

```astro
---
import { Content, components } from '../content.mdx';
import Heading from '../Heading.astro';
---


<Content components={{ ...components, h1: Heading }} />
```jsx
To configure optimization for this using the `ignoreElementNames` property, specify an array of HTML element names that should be treated as custom components:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  // ...
  integrations: [
    mdx({
      optimize: {
        // Prevent the optimizer from handling `h1` elements
        ignoreElementNames: ['h1'],
      },
    }),
  ],
});
```jsx
Note that if your MDX file [configures custom components using `export const components = { ... }`](/en/guides/integrations-guide/mdx/#assigning-custom-components-to-html-elements), then you do not need to manually configure this option. The optimizer will automatically detect them.

## Examples

[Section titled “Examples”](#examples)

* The [Astro MDX starter template](https://github.com/withastro/astro/tree/latest/examples/with-mdx) shows how to use MDX files in your Astro project.

---

[← Previous](137-title.md) | [Index](index.md) | [Next →](index.md)
