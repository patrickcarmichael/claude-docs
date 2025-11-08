---
title: "Add icons to external links"
section: 212
---

# Add icons to external links

> Learn how to install a rehype plugin to add icons to external links in your Markdown files.

Using a rehype plugin, you can identify and modify links in your Markdown files that point to external sites. This example adds icons to the end of each external link, so that visitors will know they are leaving your site.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An Astro project using Markdown for content pages.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install the `rehype-external-links` plugin.

   * npm

     ```shell
     npm install rehype-external-links
     ```jsx
   * pnpm

     ```shell
     pnpm add rehype-external-links
     ```jsx
   * Yarn

     ```shell
     yarn add rehype-external-links
     ```jsx
2. Import the plugin into your `astro.config.mjs` file.

   Pass `rehypeExternalLinks` to the `rehypePlugins` array, along with an options object that includes a content property. Set this property’s `type` to `text` if you want to add plain text to the end of the link. To add HTML to the end of the link instead, set the property `type` to `raw`.

   ```ts
   // ...
   import rehypeExternalLinks from 'rehype-external-links';


   export default defineConfig({
     // ...
     markdown: {
       rehypePlugins: [
         [
           rehypeExternalLinks,
           {
             content: { type: 'text', value: ' 🔗' }
           }
         ],
       ]
     },
   });
   ```jsx
   Note

   The value of the `content` property is [not represented in the accessibility tree](https://developer.mozilla.org/en-US/docs/Web/CSS/content#accessibility_concerns). As such, it’s best to make clear that the link is external in the surrounding content, rather than relying on the icon alone.

## Resources

[Section titled “Resources”](#resources)

* [rehype-external-links](https://www.npmjs.com/package/rehype-external-links)

---

[← Previous](211-dynamically-import-images.md) | [Index](index.md) | [Next →](index.md)
