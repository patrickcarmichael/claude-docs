---
title: "Add an RSS feed"
section: 421
---

# Add an RSS feed

> Tutorial: Build your first Astro blog —
Install Astro's official package for creating a feed that your readers can subscribe to

Get ready to…

* Install an Astro package for creating an RSS feed for your website
* Create a feed that can be subscribed to and read by RSS feed readers

## Install Astro’s RSS package

[Section titled “Install Astro’s RSS package”](#install-astros-rss-package)

Astro provides a custom package to quickly add an RSS feed to your website.

This official package generates a non-HTML document with information about all of your blog posts that can be read by **feed readers** like Feedly, The Old Reader, and more. This document is updated every time your site is rebuilt.

Individuals can subscribe to your feed in a feed reader, and receive a notification when you publish a new blog post on your site, making it a popular blog feature.

1. In your terminal, quit the Astro development server (`Ctrl + C`) and run the following command to install Astro’s RSS package.

   * npm

     ```shell
     npm install @astrojs/rss
     ```jsx
   * pnpm

     ```shell
     pnpm add @astrojs/rss
     ```jsx
   * Yarn

     ```shell
     yarn add @astrojs/rss
     ```jsx
2. Restart the dev server to begin working on your Astro project again.

   * npm

     ```shell
     npm run dev
     ```jsx
   * pnpm

     ```shell
     pnpm run dev
     ```jsx
   * Yarn

     ```shell
     yarn run dev
     ```jsx
## Create an `.xml` feed document

[Section titled “Create an .xml feed document”](#create-an-xml-feed-document)

1. Create a new file in `src/pages/` called `rss.xml.js`

2. Copy the following code into this new document. Customize the `title` and `description` properties, and if necessary, specify a different language in `customData`:

   src/pages/rss.xml.js

   ```js
   import rss, { pagesGlobToRssItems } from '@astrojs/rss';


   export async function GET(context) {
     return rss({
       title: 'Astro Learner | Blog',
       description: 'My journey learning Astro',
       site: context.site,
       items: await pagesGlobToRssItems(import.meta.glob('./**/*.md')),
       customData: `<language>en-us</language>`,
     });
   }
   ```jsx
3. Add the `site` property to the Astro config with your site’s own unique Netlify URL.

   astro.config.mjs

   ```diff
   import { defineConfig } from "astro/config";


   export default defineConfig({
   +  site: "https://example.com"
   });
   ```jsx
4. Visit `http://localhost:4321/rss.xml` and verify that you can see (unformatted) text on the page with an `item` for each of your `.md` files. Each item should contain blog post information such as `title`, `url`, and `description`.

   View your RSS feed in a reader

   Download a feed reader, or sign up for an online feed reader service and subscribe to your site by adding your own Netlify URL. You can also share this link with others so they can subscribe to your posts, and be notified when a new one is published.

## Checklist

[Section titled “Checklist”](#checklist)

* I can install an Astro package using the command line.
* I can create an RSS feed for my website.

### Resources

[Section titled “Resources”](#resources)

* [RSS item generation in Astro](/en/recipes/rss/#using-glob-imports)

---

[← Previous](420-build-a-tag-index-page.md) | [Index](index.md) | [Next →](index.md)
