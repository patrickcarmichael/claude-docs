---
title: "@astrojs/mdx"
section: 136
---

# @astrojs/mdx

> Learn how to use the @astrojs/mdx integration in your Astro project.

This **[Astro integration](/en/guides/integrations-guide/)** enables the usage of [MDX](https://mdxjs.com/) components and allows you to create pages as `.mdx` files.

## Why MDX?

[Section titled “Why MDX?”](#why-mdx)

MDX allows you to use variables, JSX expressions and components within Markdown content in Astro. If you have existing content authored in MDX, this integration allows you to bring those files to your Astro project.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

Run one of the following commands in a new terminal window.

* npm

  ```sh
  npx astro add mdx
  ```jsx
* pnpm

  ```sh
  pnpm astro add mdx
  ```jsx
* Yarn

  ```sh
  yarn astro add mdx
  ```jsx
If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/mdx` package:

* npm

  ```sh
  npm install @astrojs/mdx
  ```jsx
* pnpm

  ```sh
  pnpm add @astrojs/mdx
  ```jsx
* Yarn

  ```sh
  yarn add @astrojs/mdx
  ```jsx
Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import mdx from '@astrojs/mdx';


export default defineConfig({
  // ...
  integrations: [mdx()],
});
```jsx
### Editor Integration

[Section titled “Editor Integration”](#editor-integration)

For editor support in [VS Code](https://code.visualstudio.com/), install the [official MDX extension](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx).

For other editors, use the [MDX language server](https://github.com/mdx-js/mdx-analyzer/tree/main/packages/language-server).

## Usage

[Section titled “Usage”](#usage)

Visit the [MDX docs](https://mdxjs.com/docs/what-is-mdx/) to learn about using standard MDX features.

## MDX in Astro

[Section titled “MDX in Astro”](#mdx-in-astro)

Adding the MDX integration enhances your Markdown authoring with JSX variables, expressions and components.

It also adds extra features to standard MDX, including support for Markdown-style frontmatter in MDX. This allows you to use most of [Astro’s built-in Markdown features](/en/guides/markdown-content/).

`.mdx` files must be written in [MDX syntax](https://mdxjs.com/docs/what-is-mdx/#mdx-syntax) rather than Astro’s HTML-like syntax.

### Using MDX with content collections

[Section titled “Using MDX with content collections”](#using-mdx-with-content-collections)

To include MDX files in a content collection, make sure that your [collection loader](/en/guides/content-collections/#defining-the-collection-loader) is configured to load content from `.mdx` files:

src/content.config.ts

```js
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';


const blog = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
  })
});


export const collections = { blog };
```jsx
### Using Exported Variables in MDX

[Section titled “Using Exported Variables in MDX”](#using-exported-variables-in-mdx)

MDX supports using `export` statements to add variables to your MDX content or to export data to a component that imports it.

For example, you can export a `title` field from an MDX page or component to use as a heading with `{JSX expressions}`:

/src/blog/posts/post-1.mdx

```mdx
export const title = 'My first MDX post'

---

[← Previous](135-note-can-use-either-spaces-or-tabs-for-indentation.md) | [Index](index.md) | [Next →](index.md)
