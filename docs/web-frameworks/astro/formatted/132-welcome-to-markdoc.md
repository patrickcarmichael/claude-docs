---
title: "Welcome to Markdoc 👋"
section: 132
---

# Welcome to Markdoc 👋


{% aside type="tip" %}


Use tags like this fancy "aside" to add some _flair_ to your docs.


{% /aside %}
```jsx
### Use client-side UI components

[Section titled “Use client-side UI components”](#use-client-side-ui-components)

Tags and nodes are restricted to `.astro` files. To embed client-side UI components in Markdoc, [use a wrapper `.astro` component that renders a framework component](/en/guides/framework-components/#nesting-framework-components) with your desired `client:` directive.

This example wraps a React `Aside.tsx` component with a `ClientAside.astro` component:

src/components/ClientAside.astro

```astro
---
import Aside from './Aside';
---


<Aside {...Astro.props} client:load />
```jsx
This Astro component can now be passed to the `render` prop for any [tag](https://markdoc.dev/docs/tags) or [node](https://markdoc.dev/docs/nodes) in your config:

markdoc.config.mjs

```js
import { defineMarkdocConfig, component } from '@astrojs/markdoc/config';


export default defineMarkdocConfig({
  tags: {
    aside: {
      render: component('./src/components/ClientAside.astro'),
      attributes: {
        type: { type: String },
      },
    },
  },
});
```jsx
### Use Astro components from npm packages and TypeScript files

[Section titled “Use Astro components from npm packages and TypeScript files”](#use-astro-components-from-npm-packages-and-typescript-files)

You may need to use Astro components exposed as named exports from TypeScript or JavaScript files. This is common when using npm packages and design systems.

You can pass the import name as the second argument to the `component()` function:

markdoc.config.mjs

```js
import { defineMarkdocConfig, component } from '@astrojs/markdoc/config';


export default defineMarkdocConfig({
  tags: {
    tabs: {
      render: component('@astrojs/starlight/components', 'Tabs'),
    },
  },
});
```jsx
This generates the following import statement internally:

```ts
import { Tabs } from '@astrojs/starlight/components';
```jsx
## Markdoc Partials

[Section titled “Markdoc Partials”](#markdoc-partials)

The `{% partial /%}` tag allows you to render other `.mdoc` files inside your Markdoc content.

This is useful for reusing content across multiple documents, and allows you to have `.mdoc` content files that do not follow your collection schema.

Tip

Use an underscore `_` prefix for partial files or directories. This excludes partials from content collection queries.

This example shows a Markdoc partial for a footer to be used inside blog collection entries:

src/content/blog/\_footer.mdoc

```md
Social links:


- [Twitter / X](https://twitter.com/astrodotbuild)
- [Discord](https://astro.build/chat)
- [GitHub](https://github.com/withastro/astro)
```jsx
Use the `{% partial /%}` tag with to render the footer at the bottom of a blog post entry. Apply the `file` attribute with the path to the file, using either a relative path or an import alias:

src/content/blog/post.mdoc

```md

---

[← Previous](131-astrojsmarkdoc.md) | [Index](index.md) | [Next →](index.md)
