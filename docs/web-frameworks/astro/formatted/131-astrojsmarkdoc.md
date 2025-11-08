---
title: "@astrojs/markdoc"
section: 131
---

# @astrojs/markdoc

> Learn how to use the @astrojs/markdoc integration in your Astro project.

This **[Astro integration](/en/guides/integrations-guide/)** enables the usage of [Markdoc](https://markdoc.dev/) to create components, pages, and content collection entries.

## Why Markdoc?

[Section titled “Why Markdoc?”](#why-markdoc)

Markdoc allows you to enhance your Markdown with [Astro components](/en/basics/astro-components/). If you have existing content authored in Markdoc, this integration allows you to bring those files to your Astro project using content collections.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

Run one of the following commands in a new terminal window.

* npm

  ```sh
  npx astro add markdoc
  ```jsx
* pnpm

  ```sh
  pnpm astro add markdoc
  ```jsx
* Yarn

  ```sh
  yarn astro add markdoc
  ```jsx
If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/markdoc` package:

* npm

  ```sh
  npm install @astrojs/markdoc
  ```jsx
* pnpm

  ```sh
  pnpm add @astrojs/markdoc
  ```jsx
* Yarn

  ```sh
  yarn add @astrojs/markdoc
  ```jsx
Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import markdoc from '@astrojs/markdoc';
export default defineConfig({
  // ...
  integrations: [markdoc()],
});
```jsx
### VS Code Editor Integration

[Section titled “VS Code Editor Integration”](#vs-code-editor-integration)

If you are using VS Code, there is an official [Markdoc language extension](https://marketplace.visualstudio.com/items?itemName=Stripe.markdoc-language-support) that includes syntax highlighting and autocomplete for configured tags. [See the language server on GitHub](https://github.com/markdoc/language-server.git) for more information.

To set up the extension, create a `markdoc.config.json` file in the project root with following content:

markdoc.config.json

```json
[
  {
    "id": "my-site",
    "path": "src/content",
    "schema": {
      "path": "markdoc.config.mjs",
      "type": "esm",
      "property": "default",
      "watch": true
    }
  }
]
```jsx
Set `markdoc.config.mjs` as your configuration file with the `schema` object, and define where your Markdoc files are stored using the `path` property. Since Markdoc is specific to content collections, you can use `src/content`.

## Usage

[Section titled “Usage”](#usage)

Markdoc files can only be used within content collections. Add entries to any content collection using the `.mdoc` extension:

* src/

  * content/

    * docs/

      * why-markdoc.mdoc
      * quick-start.mdoc

Then, query your collection using the [Content Collection APIs](/en/guides/content-collections/#querying-collections):

src/pages/why-markdoc.astro

```astro
---
import { getEntry, render } from 'astro:content';


const entry = await getEntry('docs', 'why-markdoc');
const { Content } = await render(entry);
---


<!--Access frontmatter properties with `data`-->
<h1>{entry.data.title}</h1>
<!--Render Markdoc contents with the Content component-->
<Content />
```jsx
See the [Astro Content Collection docs](/en/guides/content-collections/) for more information.

## Pass Markdoc variables

[Section titled “Pass Markdoc variables”](#pass-markdoc-variables)

You may need to pass [variables](https://markdoc.dev/docs/variables) to your content. This is useful when passing SSR parameters like A/B tests.

Variables can be passed as props via the `Content` component:

src/pages/why-markdoc.astro

```astro
---
import { getEntry, render } from 'astro:content';


const entry = await getEntry('docs', 'why-markdoc');
const { Content } = await render(entry);
---


<!--Pass the `abTest` param as a variable-->
<Content abTestGroup={Astro.params.abTestGroup} />
```jsx
Now, `abTestGroup` is available as a variable in `docs/why-markdoc.mdoc`:

src/content/docs/why-markdoc.mdoc

```md
{% if $abTestGroup === 'image-optimization-lover' %}


Let me tell you about image optimization...


{% /if %}
```jsx
To make a variable global to all Markdoc files, you can use the `variables` attribute from your `markdoc.config.mjs|ts`:

markdoc.config.mjs

```js
import { defineMarkdocConfig } from '@astrojs/markdoc/config';


export default defineMarkdocConfig({
  variables: {
    environment: process.env.IS_PROD ? 'prod' : 'dev',
  },
});
```jsx
### Access frontmatter from your Markdoc content

[Section titled “Access frontmatter from your Markdoc content”](#access-frontmatter-from-your-markdoc-content)

To access frontmatter, you can pass the entry `data` property as a variable where you render your content:

src/pages/why-markdoc.astro

```astro
---
import { getEntry, render } from 'astro:content';


const entry = await getEntry('docs', 'why-markdoc');
const { Content } = await render(entry);
---


<Content frontmatter={entry.data} />
```jsx
This can now be accessed as `$frontmatter` in your Markdoc.

## Render components

[Section titled “Render components”](#render-components)

`@astrojs/markdoc` offers configuration options to use all of Markdoc’s features and connect UI components to your content.

### Use Astro components as Markdoc tags

[Section titled “Use Astro components as Markdoc tags”](#use-astro-components-as-markdoc-tags)

You can configure [Markdoc tags](https://markdoc.dev/docs/tags) that map to `.astro` components. You can add a new tag by creating a `markdoc.config.mjs|ts` file at the root of your project and configuring the `tag` attribute.

This example renders an `Aside` component, and allows a `type` prop to be passed as a string:

markdoc.config.mjs

```js
import { defineMarkdocConfig, component } from '@astrojs/markdoc/config';


export default defineMarkdocConfig({
  tags: {
    aside: {
      render: component('./src/components/Aside.astro'),
      attributes: {
        // Markdoc requires type defs for each attribute.
        // These should mirror the `Props` type of the component
        // you are rendering.
        // See Markdoc's documentation on defining attributes
        // https://markdoc.dev/docs/attributes#defining-attributes
        type: { type: String },
      },
    },
  },
});
```jsx
This component can now be used in your Markdoc files with the `{% aside %}` tag. Children will be passed to your component’s default slot:

```md

---

[← Previous](130-lit.md) | [Index](index.md) | [Next →](index.md)
