**Navigation:** [← Previous](./10-upgrade-to-astro-v5.md) | [Index](./index.md) | [Next →](./12-configuration-reference.md)

---

# Create a dev toolbar app

> Learn how to create a dev toolbar app for your site.

Astro includes a [development toolbar](/en/guides/dev-toolbar/) that you can use to inspect your site, check for accessibility and performance issues, and more. This toolbar can be extended with custom apps.

## Build a motivational dev toolbar app

[Section titled “Build a motivational dev toolbar app”](#build-a-motivational-dev-toolbar-app)

In this recipe, you’ll learn how to create a dev toolbar app that helps you stay motivated while working on your site. This app will display a motivational message every time you toggle it on.

Tip

Just want to get started quickly? Jump start your app by creating a new Astro project with the `toolbar-app` template.

* npm

  ```shell
  npm create astro@latest -- --template toolbar-app
  ```

* pnpm

  ```shell
  pnpm create astro -- --template toolbar-app
  ```

* Yarn

  ```shell
  yarn create astro -- --template toolbar-app
  ```

Or, keep reading to learn how to build an app from scratch.

### Creating the Astro integration

[Section titled “Creating the Astro integration”](#creating-the-astro-integration)

Dev toolbar apps can only be added by [Astro Integrations](/en/guides/integrations-guide/) using [the `astro:config:setup` hook](/en/reference/integrations-reference/#astroconfigsetup). You will need to create both a toolbar app and the integration that will add it to the toolbar of your existing Astro project.

1. In the root of your existing Astro project, create a new folder named `my-toolbar-app/` for your app and integration files. Create two new files in this folder: `app.ts` and `my-integration.ts`.

   * **my-toolbar-app/**

     * **app.ts**
     * **my-integration.ts**

   * src/

     * pages/

       * …

     * …

   * astro.config.mjs

   * package.json

   * tsconfig.json

2. In `my-integration.ts`, add the following code to provide both the name of your integration and the [`addDevToolbarApp()` function](/en/reference/dev-toolbar-app-reference/#toolbar-app-integration-setup) needed to add your dev toolbar app with the `astro:config:setup` hook:

   my-toolbar-app/my-integration.ts

   ```ts
   import { fileURLToPath } from 'node:url';
   import type { AstroIntegration } from 'astro';


   export default {
     name: 'my-astro-integration',
     hooks: {
       'astro:config:setup': ({ addDevToolbarApp }) => {
         addDevToolbarApp({
           id: "my-toolbar-app",
           name: "My Toolbar App",
           icon: "🚀",
           entrypoint: fileURLToPath(new URL('./app.ts', import.meta.url))
         });
       },
     },
   } satisfies AstroIntegration;
   ```

   Using relative paths to the entrypoint

   The `entrypoint` is the path to your dev toolbar app file **relative to the root of your existing Astro project**, not to the integration folder (`my-toolbar-app`) itself.

   To use relative paths for entrypoints, get the path to the current file using `import.meta.url` and resolve the path to the entrypoint from there.

3. To use this integration in your project, add it to the `integrations` array in your `astro.config.mjs` file.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import myIntegration from './my-toolbar-app/my-integration.ts';


   export default defineConfig({
   +  integrations: [myIntegration],
   })
   ```

4. If not already running, start the dev server. If your integration has been successfully added to your project, you should see a new “undefined” app in the dev toolbar.

   But, you will also see an error message that your dev toolbar app has failed to load. This is because you have not yet built the app itself. You will do that in the next section.

See the [Astro Integration API documentation](/en/reference/integrations-reference/) for more about building Astro integrations.

### Creating the app

[Section titled “Creating the app”](#creating-the-app)

Dev toolbar apps are defined using the `defineToolbarApp()` function from the `astro/toolbar` module. This function takes an object with an `init()` function that will be called when the dev toolbar app is loaded.

This `init()` function contains your app logic to render elements to the screen, send and receive client-side events from the dev toolbar, and communicate with the server.

app.ts

```ts
import { defineToolbarApp } from "astro/toolbar";


export default defineToolbarApp({
    init(canvas, app, server) {
      // ...
    },
});
```

To display motivational messages on the screen, you will use the `canvas` property to access a standard [ShadowRoot](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot). Elements can be created and added to the ShadowRoot using the standard DOM APIs.

1. Copy the following code into `my-toolbar-app/app.ts`. This provides a list of motivational messages, and the logic to create a new `<h1>` element with a random message:

   my-toolbar-app/app.ts

   ```ts
   import { defineToolbarApp } from "astro/toolbar";


   const motivationalMessages = [
     "You're doing great!",
     "Keep up the good work!",
     "You're awesome!",
     "You're a star!",
   ];


   export default defineToolbarApp({
       init(canvas) {
         const h1 = document.createElement('h1');
         h1.textContent = motivationalMessages[Math.floor(Math.random() * motivationalMessages.length)];


         canvas.append(h1);
       },
   });
   ```

2. Start the dev server if it is not already running and toggle the app on in the dev toolbar. If your app is working successfully, you will see a motivational message displayed in the top-left corner of the screen. (And, it’s true!)

   However, this message will not change when the app is toggled on and off, as the `init()` function is only called once when the app is loaded.

3. To add client-side interactivity to your app, add the `app` argument and use `onAppToggled()` to select a new random message each time your toolbar app is toggled on:

   app.ts

   ```diff
   import { defineToolbarApp } from "astro/toolbar";


   const motivationalMessages = [
     "You're doing great!",
     "Keep up the good work!",
     "You're awesome!",
     "You're a star!",
   ];


   export default defineToolbarApp({
       init(canvas, app) {
         const h1 = document.createElement('h1');
         h1.textContent = motivationalMessages[Math.floor(Math.random() * motivationalMessages.length)];


         canvas.append(h1);


         +// Display a random message when the app is toggled
   +      app.onToggled(({ state }) => {
           +const newMessage = motivationalMessages[Math.floor(Math.random() * motivationalMessages.length)];
   +        h1.textContent = newMessage;
   +      });
       },
   });
   ```

4. In your browser preview, toggle your app on and off several times. With this change, a new random message will be selected every time you toggle the app on, providing you with an infinite source of motivation!

See the [Astro Dev Toolbar API documentation](/en/reference/dev-toolbar-app-reference/) for more about building dev toolbar apps.

## Building apps with a UI framework

[Section titled “Building apps with a UI framework”](#building-apps-with-a-ui-framework)

UI frameworks like React, Vue, or Svelte can also be used to create dev toolbar apps. These frameworks provide a more declarative way to create UIs and can make your code more maintainable and easier to read.

The same motivational dev toolbar app built into your existing Astro project earlier on this page with JavaScript can be built using a UI framework (e.g. Preact) instead. Depending on your chosen framework, you may or may not require a build step.

Note

However you choose to build your dev toolbar app, using JavaScript or a UI framework, you will still need to [create the integration](#creating-the-astro-integration) that adds your app to the dev toolbar.

### Without a build step

[Section titled “Without a build step”](#without-a-build-step)

If your framework supports it, you can create a dev toolbar app without a build step. For example, you can use Preact’s `h` function to create elements and render them directly to the ShadowRoot:

app.ts

```ts
import { defineToolbarApp } from "astro/toolbar";
import { render, h } from "preact";


const motivationalMessages = [
  "You're doing great!",
  "Keep up the good work!",
  "You're awesome!",
  "You're a star!",
];


export default defineToolbarApp({
    init(canvas) {
      const message = motivationalMessages[Math.floor(Math.random() * motivationalMessages.length)];
      render(h('h1', null, message), canvas);
    },
});
```

Alternatively, the [`htm` package](https://github.com/developit/htm) is a good choice for creating dev toolbar apps without a build step, offering native integration for React and Preact and support for other frameworks:

app.ts

```diff
import { defineToolbarApp } from "astro/toolbar";
import { render } from "preact";
+import { html } from 'htm/preact';


const motivationalMessages = [
  "You're doing great!",
  "Keep up the good work!",
  "You're awesome!",
  "You're a star!",
];


export default defineToolbarApp({
    init(canvas) {
      const message = motivationalMessages[Math.floor(Math.random() * motivationalMessages.length)];
      +render(html`<h1>${message}</h1>`, canvas);
    },
});
```

In both cases, you can now start your project and see the motivational message displayed in the top-left corner of the screen when you toggle the app on.

### With a build step

[Section titled “With a build step”](#with-a-build-step)

Astro does not preprocess JSX code in dev toolbar apps, so a build step is required in order to use JSX components in your dev toolbar app.

The following steps will use TypeScript to do this, but any other tools that compile JSX code will also work (e.g. Babel, Rollup, ESBuild).

1. Install TypeScript inside your project:

   * npm

     ```shell
     npm install --save-dev typescript
     ```

   * pnpm

     ```shell
     pnpm install --save-dev typescript
     ```

   * Yarn

     ```shell
     yarn add --dev typescript
     ```

2. Create a `tsconfig.json` file in the root of your toolbar app’s folder with the appropriate settings to build and for the framework you’re using ([React](https://react-typescript-cheatsheet.netlify.app/docs/basic/setup), [Preact](https://preactjs.com/guide/v10/typescript), [Solid](https://www.solidjs.com/guides/typescript)). For example, for Preact:

   my-toolbar-app/tsconfig.json

   ```json
   {
     "compilerOptions": {
       "skipLibCheck": true,
       "module": "NodeNext",
       "jsx": "react-jsx",
       "jsxImportSource": "preact",
     }
   }
   ```

3. Adjust the `entrypoint` in your integration to point to the compiled file, remembering that this file is relative to the root of your Astro project:

   my-integration.ts

   ```ts
   addDevToolbarApp({
     id: "my-toolbar-app",
     name: "My Toolbar App",
     icon: "🚀",
     entrypoint: join(__dirname, "./app.js"),
   });
   ```

4. Run `tsc` to build your toolbar app, or `tsc --watch` to automatically rebuild your app when you make changes.

   With these changes, you can now rename your `app.ts` file to `app.tsx` (or `.jsx`) and use JSX syntax to create your dev toolbar app:

   app.tsx

   ```tsx
   import { defineToolbarApp } from "astro/toolbar";
   import { render } from "preact";


   const motivationalMessages = [
     "You're doing great!",
     "Keep up the good work!",
     "You're awesome!",
     "You're a star!",
   ];


   export default defineToolbarApp({
       init(canvas) {
         const message = motivationalMessages[Math.floor(Math.random() * motivationalMessages.length)];
         render(<h1>{message}</h1>, canvas);
       },
   });
   ```

You should now have all the tools you need to create a dev toolbar app using a UI framework of your choice!

# Add last modified time

> Build a remark plugin to add the last modified time to your Markdown and MDX.

Learn how to build a [remark plugin](https://github.com/remarkjs/remark) that adds the last modified time to the frontmatter of your Markdown and MDX files. Use this property to display the modified time in your pages.

Uses Git history

This recipe calculates time based on your repository’s Git history and may not be accurate on some deployment platforms. Your host may be performing **shallow clones** which do not retrieve the full git history.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install Helper Packages

   Install [`Day.js`](https://www.npmjs.com/package/dayjs) to modify and format times:

   * npm

     ```shell
     npm install dayjs
     ```

   * pnpm

     ```shell
     pnpm add dayjs
     ```

   * Yarn

     ```shell
     yarn add dayjs
     ```

2. Create a Remark Plugin

   This plugin uses `execSync` to run a Git command that returns the timestamp of the latest commit in ISO 8601 format. The timestamp is then added to the frontmatter of the file.

   remark-modified-time.mjs

   ```js
   import { execSync } from "child_process";


   export function remarkModifiedTime() {
     return function (tree, file) {
       const filepath = file.history[0];
       const result = execSync(`git log -1 --pretty="format:%cI" "${filepath}"`);
       file.data.astro.frontmatter.lastModified = result.toString();
     };
   }
   ```

   Using the file system instead of Git

   Although using Git is the recommended way to get the last modified timestamp from a file, it is possible to use the file system modified time. This plugin uses `statSync` to get the `mtime` (modified time) of the file in ISO 8601 format. The timestamp is then added to the frontmatter of the file.

   remark-modified-time.mjs

   ```js
   import { statSync } from "fs";


   export function remarkModifiedTime() {
     return function (tree, file) {
       const filepath = file.history[0];
       const result = statSync(filepath);
       file.data.astro.frontmatter.lastModified = result.mtime.toISOString();
     };
   }
   ```

3. Add the plugin to your config

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { remarkModifiedTime } from './remark-modified-time.mjs';


   export default defineConfig({
     markdown: {
       remarkPlugins: [remarkModifiedTime],
     },
   });
   ```

   Now all Markdown documents will have a `lastModified` property in their frontmatter.

4. Display Last Modified Time

   If your content is stored in a [content collection](/en/guides/content-collections/), access the `remarkPluginFrontmatter` from the `render(entry)` function. Then render `lastModified` in your template wherever you would like it to appear.

   src/pages/posts/\[slug].astro

   ```astro
   ---
   import { getCollection, render } from 'astro:content';
   import dayjs from "dayjs";
   import utc from "dayjs/plugin/utc";


   dayjs.extend(utc);


   export async function getStaticPaths() {
     const blog = await getCollection('blog');
     return blog.map(entry => ({
       params: { slug: entry.id },
       props: { entry },
     }));
   }


   const { entry } = Astro.props;
   const { Content, remarkPluginFrontmatter } = await render(entry);


   const lastModified = dayjs(remarkPluginFrontmatter.lastModified)
     .utc()
     .format("HH:mm:ss DD MMMM YYYY UTC");
   ---


   <html>
     <head>...</head>
     <body>
       ...
       <p>Last Modified: {lastModified}</p>
       ...
     </body>
   </html>
   ```

   If you’re using a [Markdown layout](/en/basics/layouts/#markdown-layouts), use the `lastModified` frontmatter property from `Astro.props` in your layout template.

   src/layouts/BlogLayout.astro

   ```astro
   ---
   import dayjs from "dayjs";
   import utc from "dayjs/plugin/utc";


   dayjs.extend(utc);


   const lastModified = dayjs()
     .utc(Astro.props.frontmatter.lastModified)
     .format("HH:mm:ss DD MMMM YYYY UTC");
   ---


   <html>
     <head>...</head>
     <body>
       <p>{lastModified}</p>
       <slot />
     </body>
   </html>
   ```

# Add reading time

> Build a remark plugin to add reading time to your Markdown or MDX files.

Create a [remark plugin](https://github.com/remarkjs/remark) which adds a reading time property to the frontmatter of your Markdown or MDX files. Use this property to display the reading time for each page.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install Helper Packages

   Install these two helper packages:

   * [`reading-time`](https://www.npmjs.com/package/reading-time) to calculate minutes read
   * [`mdast-util-to-string`](https://www.npmjs.com/package/mdast-util-to-string) to extract all text from your markdown

   - npm

     ```shell
     npm install reading-time mdast-util-to-string
     ```

   - pnpm

     ```shell
     pnpm add reading-time mdast-util-to-string
     ```

   - Yarn

     ```shell
     yarn add reading-time mdast-util-to-string
     ```

2. Create a remark plugin.

   This plugin uses the `mdast-util-to-string` package to get the Markdown file’s text. This text is then passed to the `reading-time` package to calculate the reading time in minutes.

   remark-reading-time.mjs

   ```js
   import getReadingTime from 'reading-time';
   import { toString } from 'mdast-util-to-string';


   export function remarkReadingTime() {
     return function (tree, { data }) {
       const textOnPage = toString(tree);
       const readingTime = getReadingTime(textOnPage);
       // readingTime.text will give us minutes read as a friendly string,
       // i.e. "3 min read"
       data.astro.frontmatter.minutesRead = readingTime.text;
     };
   }
   ```

3. Add the plugin to your config:

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { remarkReadingTime } from './remark-reading-time.mjs';


   export default defineConfig({
     markdown: {
       remarkPlugins: [remarkReadingTime],
     },
   });
   ```

   Now all Markdown documents will have a calculated `minutesRead` property in their frontmatter.

4. Display Reading Time

   If your blog posts are stored in a [content collection](/en/guides/content-collections/), access the `remarkPluginFrontmatter` from the `render(entry)` function. Then, render `minutesRead` in your template wherever you would like it to appear.

   src/pages/posts/\[slug].astro

   ```astro
   ---
   import { getCollection, render } from 'astro:content';


   export async function getStaticPaths() {
     const blog = await getCollection('blog');
     return blog.map(entry => ({
       params: { slug: entry.id },
       props: { entry },
     }));
   }


   const { entry } = Astro.props;
   const { Content, remarkPluginFrontmatter } = await render(entry);
   ---


   <html>
     <head>...</head>
     <body>
       ...
       <p>{remarkPluginFrontmatter.minutesRead}</p>
       ...
     </body>
   </html>
   ```

   If you’re using a [Markdown layout](/en/basics/layouts/#markdown-layouts), use the `minutesRead` frontmatter property from `Astro.props` in your layout template.

   src/layouts/BlogLayout.astro

   ```astro
   ---
   const { minutesRead } = Astro.props.frontmatter;
   ---


   <html>
     <head>...</head>
     <body>
       <p>{minutesRead}</p>
       <slot />
     </body>
   </html>
   ```

# Add an RSS feed

> Add an RSS feed to your Astro site to let users subscribe to your content.

Astro supports fast, automatic RSS feed generation for blogs and other content websites. RSS feeds provide an easy way for users to subscribe to your content.

## Setting up `@astrojs/rss`

[Section titled “Setting up @astrojs/rss”](#setting-up-astrojsrss)

The package [`@astrojs/rss`](https://github.com/withastro/astro/tree/main/packages/astro-rss) provides helpers for generating RSS feeds using [API endpoints](/en/guides/endpoints/#static-file-endpoints). This unlocks both static builds *and* on-demand generation when using an [SSR adapter](/en/guides/on-demand-rendering/).

1. Install `@astrojs/rss` using your preferred package manager:

   * npm

     ```shell
     npm install @astrojs/rss
     ```

   * pnpm

     ```shell
     pnpm add @astrojs/rss
     ```

   * Yarn

     ```shell
     yarn add @astrojs/rss
     ```

   Tip

   Ensure you’ve [configured a `site`](/en/reference/configuration-reference/#site) in your project’s `astro.config`. This will be used to generate links to your RSS articles.

2. Create a file in `src/pages/` with a name of your choice and the extension `.xml.js` to be used as the output URL for your feed. Some common RSS feed URL names are `feed.xml` or `rss.xml`.

   The example file below `src/pages/rss.xml.js` will create an RSS feed at `site/rss.xml`.

3. Import the `rss()` helper from the `@astrojs/rss` package into your `.xml.js` file and export a function that returns it using the following parameters:

   src/pages/rss.xml.js

   ```js
   import rss from '@astrojs/rss';


   export function GET(context) {
     return rss({
       // `<title>` field in output xml
       title: 'Buzz’s Blog',
       // `<description>` field in output xml
       description: 'A humble Astronaut’s guide to the stars',
       // Pull in your project "site" from the endpoint context
       // https://docs.astro.build/en/reference/api-reference/#site
       site: context.site,
       // Array of `<item>`s in output xml
       // See "Generating items" section for examples using content collections and glob imports
       items: [],
       // (optional) inject custom xml
       customData: `<language>en-us</language>`,
     });
   }
   ```

See the [`@astrojs/rss` README](https://github.com/withastro/astro/tree/main/packages/astro-rss) for the full configuration reference.

## Generating `items`

[Section titled “Generating items”](#generating-items)

The `items` field accepts a list of RSS feed objects, which can be generated from content collections entries using `getCollection()` or from your page files using `pagesGlobToRssItems()`.

The RSS feed standard format includes metadata for each published item, including values such as:

* `title`: The title of the entry. Optional only if a `description` is set. Otherwise, required.
* `description`: A short excerpt from or describing the entry. Optional only if a `title` is set. Otherwise, required.
* `link`: A URL to the original source of the entry. (optional)
* `pubDate`: The date of publication of the entry. (optional)
* `content`: The full content of your post. (optional)

See the [`items` configuration reference](https://github.com/withastro/astro/tree/main/packages/astro-rss#items) for a complete list of options.

### Using content collections

[Section titled “Using content collections”](#using-content-collections)

To create an RSS feed of pages managed in [content collections](/en/guides/content-collections/), use the `getCollection()` function to retrieve the data required for your `items` array. You will need to specify the values for each desired property (e.g. `title`, `description`) from the returned data.

src/pages/rss.xml.js

```js
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';


export async function GET(context) {
  const blog = await getCollection('blog');
  return rss({
    title: 'Buzz’s Blog',
    description: 'A humble Astronaut’s guide to the stars',
    site: context.site,
    items: blog.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      // Compute RSS link from post `id`
      // This example assumes all posts are rendered as `/blog/[id]` routes
      link: `/blog/${post.id}/`,
    })),
  });
}
```

Optional: replace your existing blog collection schema to enforce the expected RSS properties.

To ensure that every blog entry produces a valid RSS feed item, you can optionally import and apply `rssSchema` instead of defining each individual property of your schema.

src/content.config.ts

```js
import { defineCollection } from 'astro:content';
import { rssSchema } from '@astrojs/rss';


const blog = defineCollection({
  schema: rssSchema,
});


export const collections = { blog };
```

### Using glob imports

[Section titled “Using glob imports”](#using-glob-imports)

**Added in:** `@astrojs/rss@2.1.0`

To create an RSS feed from documents in `src/pages/`, use the `pagesGlobToRssItems()` helper. This accepts an [`import.meta.glob`](https://vite.dev/guide/features.html#glob-import) result and outputs an array of valid RSS feed items (see [more about writing glob patterns](/en/guides/imports/#glob-patterns) for specifying which pages to include).

Caution

This function assumes, but does not verify, that all necessary feed properties are present in each document’s frontmatter. If you encounter errors, verify each page frontmatter manually.

src/pages/rss.xml.js

```js
import rss, { pagesGlobToRssItems } from '@astrojs/rss';


export async function GET(context) {
  return rss({
    title: 'Buzz’s Blog',
    description: 'A humble Astronaut’s guide to the stars',
    site: context.site,
    items: await pagesGlobToRssItems(
      import.meta.glob('./blog/*.{md,mdx}'),
    ),
  });
}
```

Using an older version?

In versions of `@astrojs/rss` before v2.1.0, pass your glob result straight to `items` without the `pagesGlobToRssItems()` wrapper:

```js
items: import.meta.glob('./blog/*.{md,mdx}'),
```

This method is deprecated for all versions of Astro since v2.1.0, and cannot be used on modern projects.

### Including full post content

[Section titled “Including full post content”](#including-full-post-content)

**Added in:** `astro@1.6.14`

Set the `content` key on `rss.items` to provide the full content of a post as HTML. This allows `@astrojs/rss` to make the full Markdown text of your post available to RSS feed readers. Images and links with full URL paths are also supported. However, images and internal links to other pages using relative paths are not.

When rendering full post content, you will have to consider images, relative links, styles, scripts, and other elements beyond standard Markdown text that you may have in your posts. You may need to include additional logic in your `src/pages/rss.xml.js` endpoint to account for these, or to remove elements that are unnecessary for an RSS feed (e.g. those that are used only for styling or interaction on your website).

You can see [one specific community implementation](https://github.com/delucis/astro-blog-full-text-rss/blob/latest/src/pages/rss.xml.ts) that addresses some of these concerns for an example of how to proceed.

Tip

A package like [`sanitize-html`](https://www.npmjs.com/package/sanitize-html) will make sure that your content is properly sanitized, escaped, and encoded. In the process, such a package might also remove some harmless elements and attributes, so make sure to verify the output and configure the package according to your needs.

When using content collections, render the post `body` using a standard Markdown parser like [`markdown-it`](https://github.com/markdown-it/markdown-it) and sanitize the result, including any extra tags (e.g. `<img>`) needed to render your content:

src/pages/rss.xml.js

```diff
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
+import sanitizeHtml from 'sanitize-html';
+import MarkdownIt from 'markdown-it';
+const parser = new MarkdownIt();


export async function GET(context) {
  const blog = await getCollection('blog');
  return rss({
    title: 'Buzz’s Blog',
    description: 'A humble Astronaut’s guide to the stars',
    site: context.site,
    items: blog.map((post) => ({
      link: `/blog/${post.id}/`,
      // Note: this will not process components or JSX expressions in MDX files.
+      content: sanitizeHtml(parser.render(post.body), {
        allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img'])
      }),
      ...post.data,
    })),
  });
}
```

When using glob imports with Markdown, you may use the `compiledContent()` helper to retrieve the rendered HTML for sanitization. Note: this feature is **not** supported for MDX files.

src/pages/rss.xml.js

```diff
import rss from '@astrojs/rss';
+import sanitizeHtml from 'sanitize-html';


export async function GET(context) {
  const postImportResult = import.meta.glob('../posts/**/*.md', { eager: true });
  const posts = Object.values(postImportResult);
  return rss({
    title: 'Buzz’s Blog',
    description: 'A humble Astronaut’s guide to the stars',
    site: context.site,
    items: await Promise.all(posts.map(async (post) => ({
      link: post.url,
+      content: sanitizeHtml((await post.compiledContent())),
      ...post.frontmatter,
    }))),
  });
}
```

## Removing trailing slashes

[Section titled “Removing trailing slashes”](#removing-trailing-slashes)

Astro’s RSS feed produces links with a trailing slash by default, no matter what value you have configured for `trailingSlash`. This means that your RSS links may not match your post URLs exactly.

If you have set `trailingSlash: "never"` on your `astro.config.mjs`, set `trailingSlash: false` in the `rss()` helper so that your feed matches your project configuration.

src/pages/rss.xml.js

```diff
import rss from '@astrojs/rss';


export function GET(context) {
  const posts = Object.values(postImportResult);
  return rss({
    title: 'Buzz’s Blog',
    description: 'A humble Astronaut’s guide to the stars',
    site: context.site,
+    trailingSlash: false,
    items: posts.map((post) => ({
      link: post.url,
      ...post.frontmatter,
    })),
  });
}
```

## Adding a stylesheet

[Section titled “Adding a stylesheet”](#adding-a-stylesheet)

Style your RSS feed for a more pleasant user experience when viewing the file in your browser.

Use the `rss` function’s `stylesheet` option to specify an absolute path to your stylesheet.

```js
rss({
  // ex. use your stylesheet from "public/rss/styles.xsl"
  stylesheet: '/rss/styles.xsl',
  // ...
});
```

Tip

If you’d prefer not to create your own stylesheet, you may use a premade stylesheet such as the [Pretty Feed v3 default stylesheet](https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl). Download the stylesheet from GitHub and save into your project’s `public/` directory.

## Enabling RSS feed auto-discovery

[Section titled “Enabling RSS feed auto-discovery”](#enabling-rss-feed-auto-discovery)

[RSS autodiscovery](https://www.rssboard.org/rss-autodiscovery) allows browsers and other software to automatically find a site’s RSS feed from the main URL.

To enable, add a `<link>` tag with the following attributes to your site’s `head` element:

```jsx
<link
    rel="alternate"
    type="application/rss+xml"
    title="Your Site's Title"
    href={new URL("rss.xml", Astro.site)}
/>
```

With this tag, readers of your blog can enter your site’s base URL into their RSS reader to subscribe to your posts without needing the specific URL of your RSS feed.

## Next Steps

[Section titled “Next Steps”](#next-steps)

After visiting your feed in the browser at `your-domain.com/rss.xml` and confirming that you can see data for each of your posts, you can now [promote your feed on your website](https://medium.com/samsung-internet-dev/add-rss-feeds-to-your-website-to-keep-your-core-readers-engaged-3179dca9c91e#:~:text=com/~deno%2Drss-,Advertising%20your%20RSS%20feed,-Now%20you%20have). Adding the standard RSS icon to your site lets your readers know that they can subscribe to your posts in their own feed reader.

## Resources

[Section titled “Resources”](#resources)

* [RSS Feeds](https://aboutfeeds.com/)

# Share state between Astro components

> Learn how to share state across Astro components with Nano Stores.

Tip

Using framework components? See [how to share state between Islands](/en/recipes/sharing-state-islands/)!

When building an Astro website, you may need to share state across components. Astro recommends the use of [Nano Stores](https://github.com/nanostores/nanostores) for shared client storage.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install Nano Stores:

   * npm

     ```shell
     npm install nanostores
     ```

   * pnpm

     ```shell
     pnpm add nanostores
     ```

   * Yarn

     ```shell
     yarn add nanostores
     ```

2. Create a store. In this example, the store tracks whether a dialog is open or not:

   src/store.js

   ```ts
   import { atom } from 'nanostores';


   export const isOpen = atom(false);
   ```

3. Import and use the store in a `<script>` tag in the components that will share state.

   The following `Button` and `Dialog` components each use the shared `isOpen` state to control whether a particular `<div>` is hidden or displayed:

   src/components/Button.astro

   ```astro
   <button id="openDialog">Open</button>


   <script>
     import { isOpen } from '../store.js';


     // Set the store to true when the button is clicked
     function openDialog() {
       isOpen.set(true);
     }


     // Add an event listener to the button
     document.getElementById('openDialog').addEventListener('click', openDialog);
   </script>
   ```

   src/components/Dialog.astro

   ```astro
   <div id="dialog" style="display: none">Hello world!</div>


   <script>
     import { isOpen } from '../store.js';


     // Listen to changes in the store, and show/hide the dialog accordingly
     isOpen.subscribe(open => {
       if (open) {
         document.getElementById('dialog').style.display = 'block';
       } else {
         document.getElementById('dialog').style.display = 'none';
       }
     })
   </script>
   ```

## Resources

[Section titled “Resources”](#resources)

* [Nano Stores on NPM](https://www.npmjs.com/package/nanostores)
* [Nano Stores documentation for Vanilla JS](https://github.com/nanostores/nanostores#vanilla-js)

# Share state between islands

> Learn how to share state across framework components with Nano Stores.

When building an Astro website with [islands architecture / partial hydration](/en/concepts/islands/), you may have run into this problem: **I want to share state between my components.**

UI frameworks like React or Vue may encourage [“context” providers](https://react.dev/learn/passing-data-deeply-with-context) for other components to consume. But when [partially hydrating components](/en/guides/framework-components/#hydrating-interactive-components) within Astro or Markdown, you can’t use these context wrappers.

Astro recommends a different solution for shared client-side storage: [**Nano Stores**](https://github.com/nanostores/nanostores).

![](/houston_chef.webp) **Related recipe:** [Share state between Astro components](/en/recipes/sharing-state/)

## Why Nano Stores?

[Section titled “Why Nano Stores?”](#why-nano-stores)

The [Nano Stores](https://github.com/nanostores/nanostores) library allows you to author stores that any component can interact with. We recommend Nano Stores because:

* **They’re lightweight.** Nano Stores ship the bare minimum JS you’ll need (less than 1 KB) with zero dependencies.
* **They’re framework-agnostic.** This means sharing state between frameworks will be seamless! Astro is built on flexibility, so we love solutions that offer a similar developer experience no matter your preference.

Still, there are a number of alternatives you can explore. These include:

* [Svelte’s built-in stores](https://svelte.dev/tutorial/writable-stores)
* [Solid signals](https://www.solidjs.com/docs/latest) outside of a component context
* [Vue’s reactivity API](https://vuejs.org/guide/scaling-up/state-management.html#simple-state-management-with-reactivity-api)
* [Sending custom browser events](https://developer.mozilla.org/en-US/docs/Web/Events/Creating_and_triggering_events) between components

FAQ

**🙋 Can I use Nano Stores in `.astro` files or other server-side components?**

Nano Stores can be used in `<script>` tags to [share state between `.astro` components](/en/recipes/sharing-state/). However, Using Nano Stores in the frontmatter of server-side components is not recommended because of the following restrictions:

* Writing to a store from a `.astro` file or [non-hydrated component](/en/guides/framework-components/#hydrating-interactive-components) will *not* affect the value received by [client-side components](/en/reference/directives-reference/#client-directives).
* You cannot pass a Nano Store as a “prop” to client-side components.
* You cannot subscribe to store changes from a `.astro` file, since Astro components do not re-render.

If you understand these restrictions and still find a use case, you can give Nano Stores a try! Just remember that Nano Stores are built for reactivity to changes on the **client** specifically.

**🙋 How do Svelte stores compare to Nano Stores?**

**Nano Stores and [Svelte stores](https://svelte.dev/tutorial/writable-stores) are very similar!** In fact, [nanostores allow you to use the same `$` shortcut](https://github.com/nanostores/nanostores#svelte) for subscriptions that you might use with Svelte stores.

If you want to avoid third-party libraries, [Svelte stores](https://svelte.dev/tutorial/writable-stores) are a great cross-island communication tool on their own. Still, you might prefer Nano Stores if a) you like their add-ons for [“objects”](https://github.com/nanostores/nanostores#maps) and [async state](https://github.com/nanostores/nanostores#lazy-stores), or b) you want to communicate between Svelte and other UI frameworks like Preact or Vue.

**🙋 How do Solid signals compare to Nano Stores?**

If you’ve used Solid for a while, you may have tried moving [signals](https://www.solidjs.com/docs/latest#createsignal) or [stores](https://www.solidjs.com/docs/latest#createstore) outside of your components. This is a great way to share state between Solid islands! Try exporting signals from a shared file:

sharedStore.js

```js
import { createSignal } from 'solid-js';


export const sharedCount = createSignal(0);
```

…and all components importing `sharedCount` will share the same state. Though this works well, you might prefer Nano Stores if a) you like their add-ons for [“objects”](https://github.com/nanostores/nanostores#maps) and [async state](https://github.com/nanostores/nanostores#lazy-stores), or b) you want to communicate between Solid and other UI frameworks like Preact or Vue.

## Installing Nano Stores

[Section titled “Installing Nano Stores”](#installing-nano-stores)

To get started, install Nano Stores alongside their helper package for your favorite UI framework:

* Preact

  ```shell
  npm install nanostores @nanostores/preact
  ```

* React

  ```shell
  npm install nanostores @nanostores/react
  ```

* Solid

  ```shell
  npm install nanostores @nanostores/solid
  ```

* Svelte

  ```shell
  npm install nanostores
  ```

  Note

  No helper package here! Nano Stores can be used like standard Svelte stores.

* Vue

  ```shell
  npm install nanostores @nanostores/vue
  ```

You can jump into the [Nano Stores usage guide](https://github.com/nanostores/nanostores#guide) from here, or follow along with our example below!

## Usage example - ecommerce cart flyout

[Section titled “Usage example - ecommerce cart flyout”](#usage-example---ecommerce-cart-flyout)

Let’s say we’re building a simple ecommerce interface with three interactive elements:

* An “add to cart” submission form
* A cart flyout to display those added items
* A cart flyout toggle

[](/videos/stores-example.mp4)

*[**Try the completed example**](https://github.com/withastro/astro/tree/main/examples/with-nanostores) on your machine or online via StackBlitz.*

Your base Astro file may look like this:

src/pages/index.astro

```astro
---
import CartFlyoutToggle from '../components/CartFlyoutToggle';
import CartFlyout from '../components/CartFlyout';
import AddToCartForm from '../components/AddToCartForm';
---


<!DOCTYPE html>
<html lang="en">
<head>...</head>
<body>
  <header>
    <nav>
      <a href="/">Astro storefront</a>
      <CartFlyoutToggle client:load />
    </nav>
  </header>
  <main>
    <AddToCartForm client:load>
    <!-- ... -->
    </AddToCartForm>
  </main>
  <CartFlyout client:load />
</body>
</html>
```

### Using “atoms”

[Section titled “Using “atoms””](#using-atoms)

Let’s start by opening our `CartFlyout` whenever `CartFlyoutToggle` is clicked.

First, create a new JS or TS file to contain our store. We’ll use an [“atom”](https://github.com/nanostores/nanostores#atoms) for this:

src/cartStore.js

```js
import { atom } from 'nanostores';


export const isCartOpen = atom(false);
```

Now, we can import this store into any file that needs to read or write. We’ll start by wiring up our `CartFlyoutToggle`:

* Preact

  src/components/CartFlyoutToggle.jsx

  ```jsx
  import { useStore } from '@nanostores/preact';
  import { isCartOpen } from '../cartStore';


  export default function CartButton() {
    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
    // write to the imported store using `.set`
    return (
      <button onClick={() => isCartOpen.set(!$isCartOpen)}>Cart</button>
    )
  }
  ```

* React

  src/components/CartFlyoutToggle.jsx

  ```jsx
  import { useStore } from '@nanostores/react';
  import { isCartOpen } from '../cartStore';


  export default function CartButton() {
    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
    // write to the imported store using `.set`
    return (
      <button onClick={() => isCartOpen.set(!$isCartOpen)}>Cart</button>
    )
  }
  ```

* Solid

  src/components/CartFlyoutToggle.jsx

  ```jsx
  import { useStore } from '@nanostores/solid';
  import { isCartOpen } from '../cartStore';


  export default function CartButton() {
    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
    // write to the imported store using `.set`
    return (
      <button onClick={() => isCartOpen.set(!$isCartOpen())}>Cart</button>
    )
  }
  ```

* Svelte

  src/components/CartFlyoutToggle.svelte

  ```svelte
  <script>
    import { isCartOpen } from '../cartStore';
  </script>


  <!--use "$" to read the store value-->
  <button on:click={() => isCartOpen.set(!$isCartOpen)}>Cart</button>
  ```

* Vue

  src/components/CartFlyoutToggle.vue

  ```vue
  <template>
    <!--write to the imported store using `.set`-->
    <button @click="isCartOpen.set(!$isCartOpen)">Cart</button>
  </template>


  <script setup>
    import { isCartOpen } from '../cartStore';
    import { useStore } from '@nanostores/vue';


    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
  </script>
  ```

Then, we can read `isCartOpen` from our `CartFlyout` component:

* Preact

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/preact';
  import { isCartOpen } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);


    return $isCartOpen ? <aside>...</aside> : null;
  }
  ```

* React

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/react';
  import { isCartOpen } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);


    return $isCartOpen ? <aside>...</aside> : null;
  }
  ```

* Solid

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/solid';
  import { isCartOpen } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);


    return $isCartOpen() ? <aside>...</aside> : null;
  }
  ```

* Svelte

  src/components/CartFlyout.svelte

  ```svelte
  <script>
    import { isCartOpen } from '../cartStore';
  </script>


  {#if $isCartOpen}
  <aside>...</aside>
  {/if}
  ```

* Vue

  src/components/CartFlyout.vue

  ```vue
  <template>
    <aside v-if="$isCartOpen">...</aside>
  </template>


  <script setup>
    import { isCartOpen } from '../cartStore';
    import { useStore } from '@nanostores/vue';


    const $isCartOpen = useStore(isCartOpen);
  </script>
  ```

### Using “maps”

[Section titled “Using “maps””](#using-maps)

Tip

**[Maps](https://github.com/nanostores/nanostores#maps) are a great choice for objects you write to regularly!** Alongside the standard `get()` and `set()` helpers an `atom` provides, you’ll also have a `.setKey()` function to efficiently update individual object keys.

Now, let’s keep track of the items inside your cart. To avoid duplicates and keep track of “quantity,” we can store your cart as an object with the item’s ID as a key. We’ll use a [Map](https://github.com/nanostores/nanostores#maps) for this.

Let’s add a `cartItem` store to our `cartStore.js` from earlier. You can also switch to a TypeScript file to define the shape if you’re so inclined.

* JavaScript

  src/cartStore.js

  ```js
  import { atom, map } from 'nanostores';


  export const isCartOpen = atom(false);


  /**
   * @typedef {Object} CartItem
   * @property {string} id
   * @property {string} name
   * @property {string} imageSrc
   * @property {number} quantity
   */


  /** @type {import('nanostores').MapStore<Record<string, CartItem>>} */
  export const cartItems = map({});
  ```

* TypeScript

  src/cartStore.ts

  ```ts
  import { atom, map } from 'nanostores';


  export const isCartOpen = atom(false);


  export type CartItem = {
    id: string;
    name: string;
    imageSrc: string;
    quantity: number;
  }


  export const cartItems = map<Record<string, CartItem>>({});
  ```

Now, let’s export an `addCartItem` helper for our components to use.

* **If that item doesn’t exist in your cart**, add the item with a starting quantity of 1.
* **If that item *does* already exist**, bump the quantity by 1.

- JavaScript

  src/cartStore.js

  ```js
  ...
  export function addCartItem({ id, name, imageSrc }) {
    const existingEntry = cartItems.get()[id];
    if (existingEntry) {
      cartItems.setKey(id, {
        ...existingEntry,
        quantity: existingEntry.quantity + 1,
      })
    } else {
      cartItems.setKey(
        id,
        { id, name, imageSrc, quantity: 1 }
      );
    }
  }
  ```

- TypeScript

  src/cartStore.ts

  ```ts
  ...
  type ItemDisplayInfo = Pick<CartItem, 'id' | 'name' | 'imageSrc'>;
  export function addCartItem({ id, name, imageSrc }: ItemDisplayInfo) {
    const existingEntry = cartItems.get()[id];
    if (existingEntry) {
      cartItems.setKey(id, {
        ...existingEntry,
        quantity: existingEntry.quantity + 1,
      });
    } else {
      cartItems.setKey(
        id,
        { id, name, imageSrc, quantity: 1 }
      );
    }
  }
  ```

Note

**🙋 Why use `.get()` here instead of a `useStore` helper?**

You may have noticed we’re calling `cartItems.get()` here, instead of grabbing that `useStore` helper from our React / Preact / Solid / Vue examples. This is because **useStore is meant to trigger component re-renders.** In other words, `useStore` should be used whenever the store value is being rendered to the UI. Since we’re reading the value when an **event** is triggered (`addToCart` in this case), and we aren’t trying to render that value, we don’t need `useStore` here.

With our store in place, we can call this function inside our `AddToCartForm` whenever that form is submitted. We’ll also open the cart flyout so you can see a full cart summary.

* Preact

  src/components/AddToCartForm.jsx

  ```jsx
  import { addCartItem, isCartOpen } from '../cartStore';


  export default function AddToCartForm({ children }) {
    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }


    return (
      <form onSubmit={addToCart}>
        {children}
      </form>
    )
  }
  ```

* React

  src/components/AddToCartForm.jsx

  ```jsx
  import { addCartItem, isCartOpen } from '../cartStore';


  export default function AddToCartForm({ children }) {
    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }


    return (
      <form onSubmit={addToCart}>
        {children}
      </form>
    )
  }
  ```

* Solid

  src/components/AddToCartForm.jsx

  ```jsx
  import { addCartItem, isCartOpen } from '../cartStore';


  export default function AddToCartForm({ children }) {
    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }


    return (
      <form onSubmit={addToCart}>
        {children}
      </form>
    )
  }
  ```

* Svelte

  src/components/AddToCartForm.svelte

  ```svelte
  <form on:submit|preventDefault={addToCart}>
    <slot></slot>
  </form>


  <script>
    import { addCartItem, isCartOpen } from '../cartStore';


    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart() {
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }
  </script>
  ```

* Vue

  src/components/AddToCartForm.vue

  ```vue
  <template>
    <form @submit="addToCart">
      <slot></slot>
    </form>
  </template>


  <script setup>
    import { addCartItem, isCartOpen } from '../cartStore';


    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }
  </script>
  ```

Finally, we’ll render those cart items inside our `CartFlyout`:

* Preact

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/preact';
  import { isCartOpen, cartItems } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);


    return $isCartOpen ? (
      <aside>
        {Object.values($cartItems).length ? (
          <ul>
            {Object.values($cartItems).map(cartItem => (
              <li>
                <img src={cartItem.imageSrc} alt={cartItem.name} />
                <h3>{cartItem.name}</h3>
                <p>Quantity: {cartItem.quantity}</p>
              </li>
            ))}
          </ul>
        ) : <p>Your cart is empty!</p>}
      </aside>
    ) : null;
  }
  ```

* React

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/react';
  import { isCartOpen, cartItems } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);


    return $isCartOpen ? (
      <aside>
        {Object.values($cartItems).length ? (
          <ul>
            {Object.values($cartItems).map(cartItem => (
              <li>
                <img src={cartItem.imageSrc} alt={cartItem.name} />
                <h3>{cartItem.name}</h3>
                <p>Quantity: {cartItem.quantity}</p>
              </li>
            ))}
          </ul>
        ) : <p>Your cart is empty!</p>}
      </aside>
    ) : null;
  }
  ```

* Solid

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/solid';
  import { isCartOpen, cartItems } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);


    return $isCartOpen() ? (
      <aside>
        {Object.values($cartItems()).length ? (
          <ul>
            {Object.values($cartItems()).map(cartItem => (
              <li>
                <img src={cartItem.imageSrc} alt={cartItem.name} />
                <h3>{cartItem.name}</h3>
                <p>Quantity: {cartItem.quantity}</p>
              </li>
            ))}
          </ul>
        ) : <p>Your cart is empty!</p>}
      </aside>
    ) : null;
  }
  ```

* Svelte

  src/components/CartFlyout.svelte

  ```svelte
  <script>
    import { isCartOpen, cartItems } from '../cartStore';
  </script>


  {#if $isCartOpen}
    {#if Object.values($cartItems).length}
      <aside>
        {#each Object.values($cartItems) as cartItem}
        <li>
          <img src={cartItem.imageSrc} alt={cartItem.name} />
          <h3>{cartItem.name}</h3>
          <p>Quantity: {cartItem.quantity}</p>
        </li>
        {/each}
      </aside>
    {:else}
      <p>Your cart is empty!</p>
    {/if}
  {/if}
  ```

* Vue

  src/components/CartFlyout.vue

  ```vue
  <template>
    <aside v-if="$isCartOpen">
      <ul v-if="Object.values($cartItems).length">
        <li v-for="cartItem in Object.values($cartItems)" v-bind:key="cartItem.name">
          <img :src=cartItem.imageSrc :alt=cartItem.name />
          <h3>{{cartItem.name}}</h3>
          <p>Quantity: {{cartItem.quantity}}</p>
        </li>
      </ul>
      <p v-else>Your cart is empty!</p>
    </aside>
  </template>


  <script setup>
    import { cartItems, isCartOpen } from '../cartStore';
    import { useStore } from '@nanostores/vue';


    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);
  </script>
  ```

Now, you should have a fully interactive ecommerce example with the smallest JS bundle in the galaxy 🚀

[**Try the completed example**](https://github.com/withastro/astro/tree/main/examples/with-nanostores) on your machine or online via StackBlitz!

# Using streaming to improve page performance

> Learn how to use streaming to improve page performance.

Astro’s SSR uses HTML streaming to send each component to the browser when available for faster page loading. To improve your page’s performance even further, you can build your components strategically to optimize their loading by avoiding blocking data fetches.

The following refactoring example demonstrates how to improve page performance by moving fetch calls to other components, moving them out of a component where they block page rendering.

The following page `await`s some data in its frontmatter. Astro will wait for all of the `fetch` calls to resolve before sending any HTML to the browser.

src/pages/index.astro

```astro
---
const personResponse = await fetch('https://randomuser.me/api/');
const personData = await personResponse.json();
const randomPerson = personData.results[0];
const factResponse = await fetch('https://catfact.ninja/fact');
const factData = await factResponse.json();
---
<html>
  <head>
    <title>A name and a fact</title>
  </head>
  <body>
    <h2>A name</h2>
    <p>{randomPerson.name.first}</p>
    <h2>A fact</h2>
    <p>{factData.fact}</p>
  </body>
</html>
```

Moving the `await` calls into smaller components allows you to take advantage of Astro’s streaming. Using the following components to perform the data fetches, Astro can render some HTML first, such as the title, and then the paragraphs when the data is ready.

src/components/RandomName.astro

```astro
---
const personResponse = await fetch('https://randomuser.me/api/');
const personData = await personResponse.json();
const randomPerson = personData.results[0];
---
<p>{randomPerson.name.first}</p>
```

src/components/RandomFact.astro

```astro
---
const factResponse = await fetch('https://catfact.ninja/fact');
const factData = await factResponse.json();
---
<p>{factData.fact}</p>
```

The Astro page below using these components can render parts of the page sooner. The `<head>`, `<body>`, and `<h2>` tags are no longer blocked by data fetches. The server will then fetch data for `RandomName` and `RandomFact` in parallel and stream the resulting HTML to the browser.

src/pages/index.astro

```astro
---
import RandomName from '../components/RandomName.astro';
import RandomFact from '../components/RandomFact.astro';
---
<html>
  <head>
    <title>A name and a fact</title>
  </head>
  <body>
    <h2>A name</h2>
    <RandomName />
    <h2>A fact</h2>
    <RandomFact />
  </body>
</html>
```

#### Including Promises directly

[Section titled “Including Promises directly”](#including-promises-directly)

You can also include promises directly in the template. Instead of blocking the entire component, it will resolve the promise in parallel and only block the markup that comes after it.

src/pages/index.astro

```astro
---
const personPromise = fetch('https://randomuser.me/api/')
  .then(response => response.json())
  .then(personData => personData.results[0].name.first);
const factPromise = fetch('https://catfact.ninja/fact')
  .then(response => response.json())
  .then(factData => factData.fact);
---
<html>
  <head>
    <title>A name and a fact</title>
  </head>
  <body>
    <h2>A name</h2>
    <p>{personPromise}</p>
    <h2>A fact</h2>
    <p>{factPromise}</p>
  </body>
</html>
```

In this example, `A name` will render while `personPromise` and `factPromise` are loading. Once `personPromise` has resolved, `A fact` will appear and `factPromise` will render when it’s finished loading.

# Style rendered Markdown with Tailwind Typography

> Learn how to use @tailwind/typography to style your rendered Markdown.

You can use [Tailwind](https://tailwindcss.com)’s Typography plugin to style rendered Markdown from sources such as Astro’s [**content collections**](/en/guides/content-collections/).

This recipe will teach you how to create a reusable Astro component to style your Markdown content using Tailwind’s utility classes.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

An Astro project that:

* has [Tailwind’s Vite plugin](/en/guides/styling/#tailwind) installed.
* uses Astro’s [content collections](/en/guides/content-collections/).

## Setting Up `@tailwindcss/typography`

[Section titled “Setting Up @tailwindcss/typography”](#setting-up-tailwindcsstypography)

First, install `@tailwindcss/typography` using your preferred package manager.

* npm

  ```shell
  npm install -D @tailwindcss/typography
  ```

* pnpm

  ```shell
  pnpm add -D @tailwindcss/typography
  ```

* Yarn

  ```shell
  yarn add --dev @tailwindcss/typography
  ```

Then, add the package as a plugin in your Tailwind configuration file.

src/styles/global.css

```diff
@import 'tailwindcss';
+@plugin '@tailwindcss/typography';
```

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `<Prose />` component to provide a wrapping `<div>` with a `<slot />` for your rendered Markdown. Add the style class `prose` alongside any desired [Tailwind element modifiers](https://tailwindcss.com/docs/typography-plugin#element-modifiers) in the parent element.

   src/components/Prose.astro

   ```astro
   ---
   ---
   <div
     class="prose dark:prose-invert
     prose-h1:font-bold prose-h1:text-xl
     prose-a:text-blue-600 prose-p:text-justify prose-img:rounded-xl
     prose-headings:underline">
     <slot />
   </div>
   ```

   Tip

   The `@tailwindcss/typography` plugin uses [**element modifiers**](https://tailwindcss.com/docs/typography-plugin#element-modifiers) to style child components of a container with the `prose` class.

   These modifiers follow the following general syntax:

   ```plaintext
   prose-[element]:class-to-apply
   ```

   For example, `prose-h1:font-bold` gives all `<h1>` tags the `font-bold` Tailwind class.

2. Query your collection entry on the page you want to render your Markdown. Pass the `<Content />` component from `await render(entry)` to `<Prose />` as a child to wrap your Markdown content in Tailwind styles.

   src/pages/index.astro

   ```astro
   ---
   import Prose from '../components/Prose.astro';
   import Layout from '../layouts/Layout.astro';
   import { getEntry, render } from 'astro:content';


   const entry = await getEntry('collection', 'entry');
   const { Content } = await render(entry);
   ---
   <Layout>
     <Prose>
       <Content />
     </Prose>
   </Layout>
   ```

## Resources

[Section titled “Resources”](#resources)

* [Tailwind Typography Documentation](https://tailwindcss.com/docs/typography-plugin)

# Astro Adapter API

Astro is designed to make it easy to deploy to any cloud provider for on-demand rendering, also known as server-side rendering (SSR). This ability is provided by **adapters**, which are [integrations](/en/reference/integrations-reference/). See the [on-demand rendering guide](/en/guides/on-demand-rendering/) to learn how to use an existing adapter.

## What is an adapter?

[Section titled “What is an adapter?”](#what-is-an-adapter)

An adapter is a special kind of [integration](/en/reference/integrations-reference/) that provides an entrypoint for server rendering at request time. An adapter does two things:

* Implements host-specific APIs for handling requests.
* Configures the build according to host conventions.

## Building an Adapter

[Section titled “Building an Adapter”](#building-an-adapter)

An adapter is an [integration](/en/reference/integrations-reference/) and can do anything that an integration can do.

An adapter **must** call the `setAdapter` API in the `astro:config:done` hook like so:

my-adapter.mjs

```js
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          supportedAstroFeatures: {
              staticOutput: 'stable'
          }
        });
      },
    },
  };
}
```

The object passed into `setAdapter` is defined as:

```ts
interface AstroAdapter {
  name: string;
  serverEntrypoint?: string;
  previewEntrypoint?: string;
  exports?: string[];
  args?: any;
  adapterFeatures?: AstroAdapterFeatures;
  supportedAstroFeatures: AstroAdapterFeatureMap;
  client?: {
    /**
     * Headers to inject into Astro's internal fetch calls (Actions, View Transitions, Server Islands, Prefetch).
     * Can be an object of headers or a function that returns headers.
     */
    internalFetchHeaders?: Record<string, string> | (() => Record<string, string>);
    /**
     * Query parameters to append to all asset URLs (images, stylesheets, scripts, etc.).
     * Useful for adapters that need to track deployment versions or other metadata.
     */
    assetQueryParams?: URLSearchParams;
  };
}


export interface AstroAdapterFeatures {
  /**
   * Creates an edge function that will communicate with the Astro middleware.
   */
  edgeMiddleware: boolean;
  /**
   * Determine the type of build output the adapter is intended for. Defaults to `server`;
   */
  buildOutput?: 'static' | 'server';
}


export type AdapterSupportsKind = 'unsupported' | 'stable' | 'experimental' | 'deprecated' | 'limited';


export type AdapterSupportWithMessage = {
  support: Exclude<AdapterSupportsKind, 'stable'>;
  message: string;
  suppress?: 'default' | 'all';
};


export type AdapterSupport = AdapterSupportsKind | AdapterSupportWithMessage;


export type AstroAdapterFeatureMap = {
  /**
   * The adapter is able to serve static pages
   */
  staticOutput?: AdapterSupport;
  /**
   * The adapter is able to serve pages that are static or rendered via server
   */
  hybridOutput?: AdapterSupport;
  /**
   * The adapter is able to serve pages rendered on demand
   */
  serverOutput?: AdapterSupport;
  /**
   * The adapter is able to support i18n domains
   */
  i18nDomains?: AdapterSupport;
  /**
   * The adapter is able to support `getSecret` exported from `astro:env/server`
   */
  envGetSecret?: AdapterSupport;
  /**
   * The adapter supports the Sharp image service
   */
  sharpImageService?: AdapterSupport;
};
```

The properties are:

* **name**: A unique name for your adapter, used for logging.
* **serverEntrypoint**: The entrypoint for on-demand server rendering.
* **exports**: An array of named exports when used in conjunction with `createExports` (explained below).
* **adapterFeatures**: An object that enables specific features that must be supported by the adapter. These features will change the built output, and the adapter must implement the proper logic to handle the different output.
* **supportedAstroFeatures**: A map of Astro built-in features. This allows Astro to determine which features an adapter is unable or unwilling to support so appropriate error messages can be provided.

### Server Entrypoint

[Section titled “Server Entrypoint”](#server-entrypoint)

Astro’s adapter API attempts to work with any type of host, and gives a flexible way to conform to the host APIs.

#### Exports

[Section titled “Exports”](#exports)

Some serverless hosts expect you to export a function, such as `handler`:

```js
export function handler(event, context) {
  // ...
}
```

With the adapter API you achieve this by implementing `createExports` in your `serverEntrypoint`:

```js
import { App } from 'astro/app';


export function createExports(manifest) {
  const app = new App(manifest);


  const handler = (event, context) => {
    // ...
  };


  return { handler };
}
```

And then in your integration, where you call `setAdapter`, provide this name in `exports`:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          exports: ['handler'],
        });
      },
    },
  };
}
```

#### Start

[Section titled “Start”](#start)

Some hosts expect you to *start* the server yourselves, for example by listening to a port. For these types of hosts, the adapter API allows you to export a `start` function which will be called when the bundle script is run.

```js
import { App } from 'astro/app';


export function start(manifest) {
  const app = new App(manifest);


  addEventListener('fetch', event => {
    // ...
  });
}
```

#### `astro/app`

[Section titled “astro/app”](#astroapp)

This module is used for rendering pages that have been prebuilt through `astro build`. Astro uses the standard [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects. Hosts that have a different API for request/response should convert to these types in their adapter.

```js
import { App } from 'astro/app';
import http from 'http';


export function start(manifest) {
  const app = new App(manifest);


  addEventListener('fetch', event => {
    event.respondWith(
      app.render(event.request)
    );
  });
}
```

The following methods are provided:

##### `app.render()`

[Section titled “app.render()”](#apprender)

**Type:** `(request: Request, options?: RenderOptions) => Promise<Response>`

This method calls the Astro page that matches the request, renders it, and returns a Promise to a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object. This also works for API routes that do not render pages.

```js
const response = await app.render(request);
```

##### `RenderOptions`

[Section titled “RenderOptions”](#renderoptions)

**Type:** `{addCookieHeader?: boolean; clientAddress?: string; locals?: object; prerenderedErrorPageFetch?: (url: ErrorPagePath) => Promise<Response>; routeData?: RouteData;}`

The `app.render()` method accepts a mandatory `request` argument, and an optional `RenderOptions` object for [`addCookieHeader`](#addcookieheader), [`clientAddress`](#clientaddress), [`locals`](#locals), [`prerenderedErrorPageFetch`](#prerenderederrorpagefetch), and [`routeData`](#routedata).

###### `addCookieHeader`

[Section titled “addCookieHeader”](#addcookieheader)

**Type:** `boolean`\
**Default:** `false`

Whether or not to automatically add all cookies written by `Astro.cookie.set()` to the response headers.

When set to `true`, they will be added to the `Set-Cookie` header of the response as comma separated key-value pairs. You can use the standard `response.headers.getSetCookie()` API to read them individually. When set to `false`(default), the cookies will only be available from `App.getSetCookieFromResponse(response)`.

```js
const response = await app.render(request, { addCookieHeader: true });
```

###### `clientAddress`

[Section titled “clientAddress”](#clientaddress)

**Type:** `string`\
**Default:** `request[Symbol.for("astro.clientAddress")]`

The client IP address that will be made available as [`Astro.clientAddress`](/en/reference/api-reference/#clientaddress) in pages, and as `ctx.clientAddress` in API routes and middleware.

The example below reads the `x-forwarded-for` header and passes it as `clientAddress`. This value becomes available to the user as `Astro.clientAddress`.

```js
const clientAddress = request.headers.get("x-forwarded-for");
const response = await app.render(request, { clientAddress });
```

###### `locals`

[Section titled “locals”](#locals)

**Type:** `object`

The [`context.locals` object](/en/reference/api-reference/#locals) used to store and access information during the lifecycle of a request.

The example below reads a header named `x-private-header`, attempts to parse it as an object and pass it to `locals`, which can then be passed to any [middleware function](/en/guides/middleware/).

```js
const privateHeader = request.headers.get("x-private-header");
let locals = {};
try {
    if (privateHeader) {
        locals = JSON.parse(privateHeader);
    }
} finally {
    const response = await app.render(request, { locals });
}
```

###### `prerenderedErrorPageFetch`

[Section titled “prerenderedErrorPageFetch”](#prerenderederrorpagefetch)

**Type:** `(url: ErrorPagePath) => Promise<Response>`\
**Default:** `fetch`

**Added in:** `astro@5.6.0`

A function that allows you to provide custom implementations for fetching prerendered error pages.

This is used to override the default `fetch()` behavior, for example, when `fetch()` is unavailable or when you cannot call the server from itself.

The following example reads `500.html` and `404.html` from disk instead of performing an HTTP call:

```js
return app.render(request, {
  prerenderedErrorPageFetch: async (url: string): Promise<Response> => {
    if (url.includes("/500")) {
        const content = await fs.promises.readFile("500.html", "utf-8");
        return new Response(content, {
          status: 500,
          headers: { "Content-Type": "text/html" },
        });
    }


    const content = await fs.promises.readFile("404.html", "utf-8");
      return new Response(content, {
        status: 404,
        headers: { "Content-Type": "text/html" },
      });
});
```

If not provided, Astro will fallback to its default behavior for fetching error pages.

###### `routeData`

[Section titled “routeData”](#routedata)

**Type:** `RouteData`\
**Default:** `app.match(request)`

Provide a value for [`integrationRouteData`](/en/reference/integrations-reference/#integrationroutedata-type-reference) if you already know the route to render. Doing so will bypass the internal call to [`app.match`](#appmatch) to determine the route to render.

```js
const routeData = app.match(request);
if (routeData) {
    return app.render(request, { routeData });
} else {
    /* adapter-specific 404 response */
    return new Response(..., { status: 404 });
}
```

##### `app.match()`

[Section titled “app.match()”](#appmatch)

**Type:** `(request: Request) => RouteData | undefined`

This method is used to determine if a request is matched by the Astro app’s routing rules.

```js
if(app.match(request)) {
  const response = await app.render(request);
}
```

You can usually call `app.render(request)` without using `.match` because Astro handles 404s if you provide a `404.astro` file. Use `app.match(request)` if you want to handle 404s in a different way.

## Allow installation via `astro add`

[Section titled “Allow installation via astro add”](#allow-installation-via-astro-add)

[The `astro add` command](/en/reference/cli-reference/#astro-add) allows users to easily add integrations and adapters to their project. If you want *your* adapter to be installable with this tool, **add `astro-adapter` to the `keywords` field in your `package.json`**:

```json
{
  "name": "example",
  "keywords": ["astro-adapter"],
}
```

Once you [publish your adapter to npm](https://docs.npmjs.com/cli/v8/commands/npm-publish), running `astro add example` will install your package with any peer dependencies specified in your `package.json`. We will also instruct users to update their project config manually.

## Astro features

[Section titled “Astro features”](#astro-features)

**Added in:** `astro@3.0.0`

Astro features are a way for an adapter to tell Astro whether they are able to support a feature, and also the adapter’s level of support.

When using these properties, Astro will:

* run specific validation;
* emit contextual information to the logs;

These operations are run based on the features supported or not supported, their level of support, the [desired amount of logging](#suppress), and the user’s own configuration.

The following configuration tells Astro that this adapter has experimental support for the Sharp-powered built-in image service:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          supportedAstroFeatures: {
+            sharpImageService: 'experimental'
+          }
        });
      },
    },
  };
}
```

If the Sharp image service is used, Astro will log a warning and error to the terminal based on your adapter’s support:

```plaintext
[@example/my-adapter] The feature is experimental and subject to issues or changes.


[@example/my-adapter] The currently selected adapter `@example/my-adapter` is not compatible with the service "Sharp". Your project will NOT be able to build.
```

A message can additionally be provided to give more context to the user:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          supportedAstroFeatures: {
+            sharpImageService: {
+              support: 'limited',
+              message: 'This adapter has limited support for Sharp. Certain features may not work as expected.'
+            }
+          }
        });
      },
    },
  };
}
```

### `suppress`

[Section titled “suppress”](#suppress)

**Type:** `'default' | 'all'`

**Added in:** `astro@5.9.0`

An option to prevent showing some or all logged messages about an adapter’s support for a feature.

If Astro’s default log message is redundant, or confusing to the user in combination with your custom `message`, you can use `suppress: "default"` to suppress the default message and only log your message:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          supportedAstroFeatures: {
            sharpImageService: {
              support: 'limited',
              message: 'The adapter has limited support for Sharp. It will be used for images during build time, but will not work at runtime.',
+              suppress: 'default' // custom message is more detailed than the default
            }
          }
        });
      },
    },
  };
}
```

You can also use `suppress: "all"` to suppress all messages about support for the feature. This is useful when these messages are unhelpful to users in a specific context, such as when they have a configuration setting that means they are not using that feature. For example, you can choose to prevent logging any messages about Sharp support from your adapter:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          supportedAstroFeatures: {
            sharpImageService: {
              support: 'limited',
              message: 'This adapter has limited support for Sharp. Certain features may not work as expected.',
+              suppress: 'all'
            }
          }
        });
      },
    },
  };
}
```

## Adapter features

[Section titled “Adapter features”](#adapter-features)

A set of features that changes the output of the emitted files. When an adapter opts in to these features, they will get additional information inside specific hooks.

### `edgeMiddleware`

[Section titled “edgeMiddleware”](#edgemiddleware)

**Type:** `boolean`

Defines whether any on-demand rendering middleware code will be bundled when built.

When enabled, this prevents middleware code from being bundled and imported by all pages during the build:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+              edgeMiddleware: true
+          }
        });
      },
    },
  };
}
```

Then, consume the hook [`astro:build:ssr`](/en/reference/integrations-reference/#astrobuildssr), which will give you a `middlewareEntryPoint`, an `URL` to the physical file on the file system.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          adapterFeatures: {
              edgeMiddleware: true
          }
        });
      },


      +'astro:build:ssr': ({ middlewareEntryPoint }) => {
          +// remember to check if this property exits, it will be `undefined` if the adapter doesn't opt in to the feature
          +if (middlewareEntryPoint) {
             +createEdgeMiddleware(middlewareEntryPoint)
+          }
+      }
    },
  };
}


function createEdgeMiddleware(middlewareEntryPoint) {
    // emit a new physical file using your bundler
}
```

### envGetSecret

[Section titled “envGetSecret”](#envgetsecret)

**Type:** `AdapterSupportsKind`

This is a feature to allow your adapter to retrieve secrets configured by users in `env.schema`.

Enable the feature by passing any valid `AdapterSupportsKind` value to the adapter:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+              envGetSecret: 'stable'
+          }
        });
      },
    },
  };
}
```

The `astro/env/setup` module allows you to provide an implementation for `getSecret()`. In your server entrypoint, call `setGetEnv()` as soon as possible:

```diff
import { App } from 'astro/app';
+import { setGetEnv } from "astro/env/setup"


+setGetEnv((key) => process.env[key])


export function createExports(manifest) {
  const app = new App(manifest);


  const handler = (event, context) => {
    // ...
  };


  return { handler };
}
```

If you support secrets, be sure to call `setGetEnv()` before `getSecret()` when your environment variables are tied to the request:

```diff
import type { SSRManifest } from 'astro';
import { App } from 'astro/app';
+import { setGetEnv } from 'astro/env/setup';
import { createGetEnv } from '../utils/env.js';


type Env = {
  [key: string]: unknown;
};


export function createExports(manifest: SSRManifest) {
  const app = new App(manifest);


  const fetch = async (request: Request, env: Env) => {
    +setGetEnv(createGetEnv(env));


    const response = await app.render(request);


    return response;
  };


  return { default: { fetch } };
}
```

### buildOutput

[Section titled “buildOutput”](#buildoutput)

**Type:** `'static' | 'server'`

**Added in:** `astro@5.0.0`

This property allows you to force a specific output shape for the build. This can be useful for adapters that only work with a specific output type, for instance, your adapter might expect a static website, but uses an adapter to create host-specific files. Defaults to `server` if not specified.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+            buildOutput: 'static'
+          }
        });
      },
    },
  };
}
```

### experimentalStaticHeaders

[Section titled “experimentalStaticHeaders”](#experimentalstaticheaders)

**Type:** `true | false`

**Added in:** `astro@5.9.3`

When this feature is enabled, Astro will return a map of the `Headers` emitted by the static pages. This map `experimentalRouteToHeaders` is available in the `astro:build:generated` hook.

The value of the headers might change based on the features enabled/used by the application.

For example, if CSP enabled, the `<meta http-equiv="content-security-policy">` element is not added to the static page. Instead its `content` is available in the `experimentalRouteToHeaders` map.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+            experimentalStaticHeaders: true,
+          },
        });
      },
      'astro:build:generated': ({ experimentalRouteToHeaders }) => {
        // use `experimentalRouteToHeaders` to generate a configuration file
        // for your virtual host of choice
      },
    },
  };
}
```

# Astro render context

When rendering a page, Astro provides a runtime API specific to the current render. This includes useful information such as the current page URL as well as APIs to perform actions like redirecting to another page.

In `.astro` components, this context is available from the `Astro` global object. Endpoint functions are also called with this same context object as their first argument, whose properties mirror the Astro global properties.

Some properties are only available for routes rendered on demand or may have limited functionality on prerendered pages.

The `Astro` global object is available to all `.astro` files. Use the `context` object in [endpoint functions](/en/guides/endpoints/) to serve static or live server endpoints and in [middleware](/en/guides/middleware/) to inject behavior when a page or endpoint is about to be rendered.

## The context object

[Section titled “The context object”](#the-context-object)

The following properties are available on the `Astro` global (e.g. `Astro.props`, `Astro.redirect()`) and are also available on the context object (e.g. `context.props`, `context.redirect()`) passed to endpoint functions and middleware.

### `props`

[Section titled “props”](#props)

`props` is an object containing any values that have been passed as [component attributes](/en/basics/astro-components/#component-props).

src/components/Heading.astro

```astro
---
const { title, date } = Astro.props;
---
<div>
  <h1>{title}</h1>
  <p>{date}</p>
</div>
```

src/pages/index.astro

```astro
---
import Heading from '../components/Heading.astro';
---
<Heading title="My First Post" date="09 Aug 2022" />
```

Learn more about how [Markdown and MDX layouts](/en/guides/markdown-content/#frontmatter-layout-property) handle props.

The `props` object also contains any `props` passed from `getStaticPaths()` when rendering static routes.

* Astro.props

  src/pages/posts/\[id].astro

  ```astro
  ---
  export function getStaticPaths() {
    return [
      { params: { id: '1' }, props: { author: 'Blu' } },
      { params: { id: '2' }, props: { author: 'Erika' } },
      { params: { id: '3' }, props: { author: 'Matthew' } }
    ];
  }


  const { id } = Astro.params;
  const { author } = Astro.props;
  ---
  ```

* context.props

  src/pages/posts/\[id].json.ts

  ```ts
  import type { APIContext } from 'astro';


  export function getStaticPaths() {
    return [
      { params: { id: '1' }, props: { author: 'Blu' } },
      { params: { id: '2' }, props: { author: 'Erika' } },
      { params: { id: '3' }, props: { author: 'Matthew' } }
    ];
  }


  export function GET({ props }: APIContext) {
    return new Response(
      JSON.stringify({ author: props.author }),
    );
  }
  ```

See also: [Data Passing with `props`](/en/reference/routing-reference/#data-passing-with-props)

### `params`

[Section titled “params”](#params)

`params` is an object containing the values of dynamic route segments matched for a request. Its keys must match the [parameters](/en/guides/routing/#dynamic-routes) in the page or endpoint file path.

In static builds, this will be the `params` returned by `getStaticPaths()` used for prerendering [dynamic routes](/en/guides/routing/#dynamic-routes):

* Astro.params

  src/pages/posts/\[id].astro

  ```astro
  ---
  export function getStaticPaths() {
    return [
      { params: { id: '1' } },
      { params: { id: '2' } },
      { params: { id: '3' } }
    ];
  }
  const { id } = Astro.params;
  ---
  <h1>{id}</h1>
  ```

* context.params

  src/pages/posts/\[id].json.ts

  ```ts
  import type { APIContext } from 'astro';


  export function getStaticPaths() {
    return [
      { params: { id: '1' } },
      { params: { id: '2' } },
      { params: { id: '3' } }
    ];
  }


  export function GET({ params }: APIContext) {
    return new Response(
      JSON.stringify({ id: params.id }),
    );
  }
  ```

When routes are rendered on demand, `params` can be any value matching the path segments in the dynamic route pattern.

src/pages/posts/\[id].astro

```astro
---
import { getPost } from '../api';


const post = await getPost(Astro.params.id);


// No posts found with this ID
if (!post) {
  return Astro.redirect("/404")
}
---
<html>
  <h1>{post.name}</h1>
</html>
```

See also: [`params`](/en/reference/routing-reference/#params)

### `url`

[Section titled “url”](#url)

**Type:** `URL`

**Added in:** `astro@1.0.0`

`url` is a [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) object constructed from the current `request.url` value. It is useful for interacting with individual properties of the request URL, like pathname and origin.

`Astro.url` is equivalent to doing `new URL(Astro.request.url)`.

`url` will be a `localhost` URL in dev mode. When building a site, prerendered routes will receive a URL based on the [`site`](/en/reference/configuration-reference/#site) and [`base`](/en/reference/configuration-reference/#base) options. If `site` is not configured, prerendered pages will receive a `localhost` URL during builds as well.

src/pages/index.astro

```astro
<h1>The current URL is: {Astro.url}</h1>
<h1>The current URL pathname is: {Astro.url.pathname}</h1>
<h1>The current URL origin is: {Astro.url.origin}</h1>
```

You can also use `url` to create new URLs by passing it as an argument to [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL).

src/pages/index.astro

```astro
---
// Example: Construct a canonical URL using your production domain
const canonicalURL = new URL(Astro.url.pathname, Astro.site);
// Example: Construct a URL for SEO meta tags using your current domain
const socialImageURL = new URL('/images/preview.png', Astro.url);
---
<link rel="canonical" href={canonicalURL} />
<meta property="og:image" content={socialImageURL} />
```

### `site`

[Section titled “site”](#site)

**Type:** `URL | undefined`

`site` returns a `URL` made from `site` in your Astro config. It returns `undefined` if you have not set a value for [`site`](/en/reference/configuration-reference/#site) in your Astro config.

src/pages/index.astro

```astro
<link
    rel="alternate"
    type="application/rss+xml"
    title="Your Site's Title"
    href={new URL("rss.xml", Astro.site)}
/>
```

### `clientAddress`

[Section titled “clientAddress”](#clientaddress)

**Type:** `string`

**Added in:** `astro@1.0.0`

`clientAddress` specifies the [IP address](https://en.wikipedia.org/wiki/IP_address) of the request. This property is only available for routes rendered on demand and cannot be used on prerendered pages.

* Astro.clientAddress

  src/pages/ip-address.astro

  ```astro
  ---
  export const prerender = false; // Not needed in 'server' mode
  ---


  <div>Your IP address is: <span class="address">{Astro.clientAddress}</span></div>
  ```

* context.clientAddress

  src/pages/ip-address.ts

  ```ts
  export const prerender = false; // Not needed in 'server' mode
  import type { APIContext } from 'astro';


  export function GET({ clientAddress }: APIContext) {
    return new Response(`Your IP address is: ${clientAddress}`);
  }
  ```

### `isPrerendered`

[Section titled “isPrerendered”](#isprerendered)

**Type**: `boolean`

**Added in:** `astro@5.0.0`

A boolean representing whether or not the current page is prerendered.

You can use this property to run conditional logic in middleware, for example, to avoid accessing headers in prerendered pages.

### `generator`

[Section titled “generator”](#generator)

**Type:** `string`

**Added in:** `astro@1.0.0`

`generator` provides the current version of Astro your project is running. This is a convenient way to add a [`<meta name="generator">`](https://html.spec.whatwg.org/multipage/semantics.html#meta-generator) tag with your current version of Astro. It follows the format `"Astro v5.x.x"`.

* Astro.generator

  src/pages/site-info.astro

  ```astro
  <html>
    <head>
      <meta name="generator" content={Astro.generator} />
    </head>
    <body>
      <footer>
        <p>Built with <a href="https://astro.build">{Astro.generator}</a></p>
      </footer>
    </body>
  </html>
  ```

* context.generator

  src/pages/site-info.json.ts

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ generator, site }: APIContext) {
    const body = JSON.stringify({ generator, site });
    return new Response(body);
  }
  ```

### `request`

[Section titled “request”](#request)

**Type:** `Request`

`request` is a standard [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object. It can be used to get the `url`, `headers`, `method`, and even the body of the request.

* Astro.request

  src/pages/index.astro

  ```astro
  <p>Received a {Astro.request.method} request to "{Astro.request.url}".</p>
  <p>Received request headers:</p>
  <p><code>{JSON.stringify(Object.fromEntries(Astro.request.headers))}</code></p>
  ```

* context.request

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ request }: APIContext) {
    return new Response(`Hello ${request.url}`);
  }
  ```

Note

On prerendered pages, `request.url` does not contain search parameters, like `?type=new`, as it’s not possible to determine them ahead of time during static builds. However, `request.url` does contain search parameters for pages rendered on-demand as they can be determined from a server request.

### `response`

[Section titled “response”](#response)

**Type:** `ResponseInit & { readonly headers: Headers }`

`response` is a standard `ResponseInit` object. It has the following structure.

* `status`: The numeric status code of the response, e.g., `200`.
* `statusText`: The status message associated with the status code, e.g., `'OK'`.
* `headers`: A [`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers) instance that you can use to set the HTTP headers of the response.

`Astro.response` is used to set the `status`, `statusText`, and `headers` for a page’s response.

```astro
---
if (condition) {
  Astro.response.status = 404;
  Astro.response.statusText = 'Not found';
}
---
```

Or to set a header:

```astro
---
Astro.response.headers.set('Set-Cookie', 'a=b; Path=/;');
---
```

### `redirect()`

[Section titled “redirect()”](#redirect)

**Type:** `(path: string, status?: number) => Response`

**Added in:** `astro@1.5.0`

`redirect()` returns a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object that allows you to redirect to another page, and optionally provide an [HTTP response status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages) as a second parameter.

A page (and not a child component) must `return` the result of `Astro.redirect()` for the redirect to occur.

For statically-generated routes, this will produce a client redirect using a [`<meta http-equiv="refresh">` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#http-equiv) and does not support status codes.

For on-demand rendered routes, setting a custom status code is supported when redirecting. If not specified, redirects will be served with a `302` status code.

The following example redirects a user to a login page:

* Astro.redirect()

  src/pages/account.astro

  ```astro
  ---
  import { isLoggedIn } from '../utils';


  const cookie = Astro.request.headers.get('cookie');


  // If the user is not logged in, redirect them to the login page
  if (!isLoggedIn(cookie)) {
    return Astro.redirect('/login');
  }
  ---


  <p>User information</p>
  ```

* context.redirect()

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ redirect, request }: APIContext) {
    const cookie = request.headers.get('cookie');
    if (!isLoggedIn(cookie)) {
      return redirect('/login', 302);
    } else {
      // return user information
    }
  }
  ```

### `rewrite()`

[Section titled “rewrite()”](#rewrite)

**Type:** `(rewritePayload: string | URL | Request) => Promise<Response>`

**Added in:** `astro@4.13.0`

`rewrite()` allows you to serve content from a different URL or path without redirecting the browser to a new page.

The method accepts either a string, a `URL`, or a `Request` for the location of the path.

Use a string to provide an explicit path:

* Astro.rewrite()

  src/pages/index.astro

  ```astro
  ---
  return Astro.rewrite("/login")
  ---
  ```

* context.rewrite()

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ rewrite }: APIContext) {
    return rewrite('/login');
  }
  ```

Use a `URL` type when you need to construct the URL path for the rewrite. The following example renders a page’s parent path by creating a new URL from the relative `"../"` path:

* Astro.rewrite()

  src/pages/blog/index.astro

  ```astro
  ---
  return Astro.rewrite(new URL("../", Astro.url))
  ---
  ```

* context.rewrite()

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ rewrite }: APIContext) {
    return rewrite(new URL("../", Astro.url));
  }
  ```

Use a `Request` type for complete control of the `Request` sent to the server for the new path. The following example sends a request to render the parent page while also providing headers:

* Astro.rewrite()

  src/pages/blog/index.astro

  ```astro
  ---
  return Astro.rewrite(new Request(new URL("../", Astro.url), {
    headers: {
      "x-custom-header": JSON.stringify(Astro.locals.someValue)
    }
  }))
  ---
  ```

* context.rewrite()

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ rewrite }: APIContext) {
    return rewrite(new Request(new URL("../", Astro.url), {
      headers: {
        "x-custom-header": JSON.stringify(Astro.locals.someValue)
      }
    }));
  }
  ```

### `originPathname`

[Section titled “originPathname”](#originpathname)

**Type:** `string`

**Added in:** `astro@5.0.0`

`originPathname` defines the original pathname of the request, before rewrites were applied.

* Astro.originPathname

  src/pages/404.astro

  ```astro
  <p>The origin path is {Astro.originPathname}</p>
  <p>The rewritten path is {Astro.url.pathname}</p>
  ```

* context.originPathname

  src/middleware.ts

  ```ts
  import { defineMiddleware } from 'astro:middleware';


  export const onRequest = defineMiddleware(async (context, next) => {
    // Record the original pathname before any rewrites
    recordPageVisit(context.originPathname);
    return next();
  });
  ```

### `locals`

[Section titled “locals”](#locals)

**Added in:** `astro@2.4.0`

`locals` is an object used to store and access arbitrary information during the lifecycle of a request. `Astro.locals` is an object containing any values from the `context.locals` object set by middleware. Use this to access data returned by middleware in your `.astro` files.

Middleware functions can both read and write the values of `context.locals`:

src/middleware.ts

```ts
import type { MiddlewareHandler } from 'astro';


export const onRequest: MiddlewareHandler = ({ locals }, next) => {
  if (!locals.title) {
    locals.title = "Default Title";
  }
  return next();
}
```

Astro components and API endpoints can read values from `locals` when they render:

* Astro.locals

  src/pages/Orders.astro

  ```astro
  ---
  const title = Astro.locals.title;
  ---
  <h1>{title}</h1>
  ```

* context.locals

  src/pages/hello.ts

  ```ts
  import type { APIContext } from 'astro';


  export function GET({ locals }: APIContext) {
    return new Response(locals.title); // "Default Title"
  }
  ```

### `preferredLocale`

[Section titled “preferredLocale”](#preferredlocale)

**Type:** `string | undefined`

**Added in:** `astro@3.5.0`

`preferredLocale` is a computed value to find the best match between your visitor’s browser language preferences and the locales supported by your site.

It is computed by checking the configured locales in your [`i18n.locales`](/en/reference/configuration-reference/#i18nlocales) array and the locales supported by the user’s browser via the header `Accept-Language`. This value is `undefined` if no such match exists.

This property is only available for routes rendered on demand and cannot be used on prerendered, static pages.

### `preferredLocaleList`

[Section titled “preferredLocaleList”](#preferredlocalelist)

**Type:** `string[] | undefined`

**Added in:** `astro@3.5.0`

`preferredLocaleList` represents the array of all locales that are both requested by the browser and supported by your website. This produces a list of all compatible languages between your site and your visitor.

If none of the browser’s requested languages are found in your locales array, then the value is `[]`. This occurs when you do not support any of your visitor’s preferred locales.

If the browser does not specify any preferred languages, then this value will be [`i18n.locales`](/en/reference/configuration-reference/#i18nlocales): all of your supported locales will be considered equally preferred by a visitor with no preferences.

This property is only available for routes rendered on demand and cannot be used on prerendered, static pages.

### `currentLocale`

[Section titled “currentLocale”](#currentlocale)

**Type:** `string | undefined`

**Added in:** `astro@3.5.6`

The locale computed from the current URL, using the syntax specified in your `locales` configuration. If the URL does not contain a `/[locale]/` prefix, then the value will default to [`i18n.defaultLocale`](/en/reference/configuration-reference/#i18ndefaultlocale).

### `getActionResult()`

[Section titled “getActionResult()”](#getactionresult)

**Type:** `(action: TAction) => ActionReturnType<TAction> | undefined`

**Added in:** `astro@4.15.0`

`getActionResult()` is a function that returns the result of an [Action](/en/guides/actions/) submission. This accepts an action function as an argument (e.g. `actions.logout`) and returns a `data` or `error` object when a submission is received. Otherwise, it will return `undefined`.

src/pages/index.astro

```astro
---
import { actions } from 'astro:actions';


const result = Astro.getActionResult(actions.logout);
---


<form action={actions.logout}>
  <button type="submit">Log out</button>
</form>
{result?.error && <p>Failed to log out. Please try again.</p>}
```

### `callAction()`

[Section titled “callAction()”](#callaction)

**Added in:** `astro@4.15.0`

`callAction()` is a function used to call an Action handler directly from your Astro component. This function accepts an Action function as the first argument (e.g. `actions.logout`) and any input that action receives as the second argument. It returns the result of the action as a promise.

src/pages/index.astro

```astro
---
import { actions } from 'astro:actions';


const { data, error } = await Astro.callAction(actions.logout, { userId: '123' });
---
```

### `routePattern`

[Section titled “routePattern”](#routepattern)

**Type**: `string`

**Added in:** `astro@5.0.0`

The route pattern responsible for generating the current page or route. In file-based routing, this resembles the file path in your project used to create the route. When integrations create routes for your project, `context.routePattern` is identical to the value for `injectRoute.pattern`.

The value will start with a leading slash and look similar to the path of a page component relative to your `src/pages/` folder without a file extension.

For example, the file `src/pages/en/blog/[slug].astro` will return `/en/blog/[slug]` for `routePattern`. Every page on your site generated by that file (e.g. `/en/blog/post-1/`, `/en/blog/post-2/`, etc.) shares the same value for `routePattern`. In the case of `index.*` routes, the route pattern will not include the word “index.” For example, `src/pages/index.astro` will return `/`.

You can use this property to understand which route is rendering your component. This allows you to target or analyze similarly-generated page URLs together. For example, you can use it to conditionally render certain information, or collect metrics about which routes are slower.

### `cookies`

[Section titled “cookies”](#cookies)

**Type:** `AstroCookies`

**Added in:** `astro@1.4.0`

`cookies` contains utilities for reading and manipulating cookies for [routes rendered on demand](/en/guides/on-demand-rendering/).

#### Cookie utilities

[Section titled “Cookie utilities”](#cookie-utilities)

##### `cookies.get()`

[Section titled “cookies.get()”](#cookiesget)

**Type:** `(key: string, options?: AstroCookieGetOptions) => AstroCookie | undefined`

Gets the cookie as an [`AstroCookie`](#astrocookie-type) object, which contains the `value` and utility functions for converting the cookie to non-string types.

##### `cookies.has()`

[Section titled “cookies.has()”](#cookieshas)

**Type:** `(key: string, options?: AstroCookieGetOptions) => boolean`

Whether this cookie exists. If the cookie has been set via `Astro.cookies.set()` this will return true, otherwise, it will check cookies in the `Astro.request`.

##### `cookies.set()`

[Section titled “cookies.set()”](#cookiesset)

**Type:** `(key: string, value: string | object, options?: AstroCookieSetOptions) => void`

Sets the cookie `key` to the given value. This will attempt to convert the cookie value to a string. Options provide ways to set [cookie features](https://www.npmjs.com/package/cookie#options-1), such as the `maxAge` or `httpOnly`.

##### `cookies.delete()`

[Section titled “cookies.delete()”](#cookiesdelete)

**Type:** `(key: string, options?: AstroCookieDeleteOptions) => void`

Invalidates a cookie by setting the expiration date in the past (0 in Unix time).

Once a cookie is “deleted” (expired), `Astro.cookies.has()` will return `false` and `Astro.cookies.get()` will return an [`AstroCookie`](#astrocookie-type) with a `value` of `undefined`. Options available when deleting a cookie are: `domain`, `path`, `httpOnly`, `sameSite`, and `secure`.

##### `cookies.merge()`

[Section titled “cookies.merge()”](#cookiesmerge)

**Type:** `(cookies: AstroCookies) => void`

Merges a new `AstroCookies` instance into the current instance. Any new cookies will be added to the current instance and any cookies with the same name will overwrite existing values.

##### `cookies.headers()`

[Section titled “cookies.headers()”](#cookiesheaders)

**Type:** `() => Iterator<string>`

Gets the header values for `Set-Cookie` that will be sent out with the response.

#### `AstroCookie` Type

[Section titled “AstroCookie Type”](#astrocookie-type)

The type returned from getting a cookie via `Astro.cookies.get()`. It has the following properties:

##### `value`

[Section titled “value”](#value)

**Type:** `string`

The raw string value of the cookie.

##### `json`

[Section titled “json”](#json)

**Type:** `() => Record<string, any>`

Parses the cookie value via `JSON.parse()`, returning an object. Throws if the cookie value is not valid JSON.

##### `number`

[Section titled “number”](#number)

**Type:** `() => number`

Parses the cookie value as a Number. Returns NaN if not a valid number.

##### `boolean`

[Section titled “boolean”](#boolean)

**Type:** `() => boolean`

Converts the cookie value to a boolean.

#### `AstroCookieGetOptions`

[Section titled “AstroCookieGetOptions”](#astrocookiegetoptions)

**Added in:** `astro@4.1.0`

The `AstroCookieGetOption` interface allows you to specify options when you get a cookie.

##### `decode`

[Section titled “decode”](#decode)

**Type:** `(value: string) => string`

Allows customization of how a cookie is deserialized into a value.

#### `AstroCookieSetOptions`

[Section titled “AstroCookieSetOptions”](#astrocookiesetoptions)

**Added in:** `astro@4.1.0`

`AstroCookieSetOptions` is an object that can be passed to `Astro.cookies.set()` when setting a cookie to customize how the cookie is serialized.

##### `domain`

[Section titled “domain”](#domain)

**Type:** `string`

Specifies the domain. If no domain is set, most clients will interpret to apply to the current domain.

##### `expires`

[Section titled “expires”](#expires)

**Type:** `Date`

Specifies the date on which the cookie will expire.

##### `httpOnly`

[Section titled “httpOnly”](#httponly)

**Type:** `boolean`

If true, the cookie will not be accessible client-side.

##### `maxAge`

[Section titled “maxAge”](#maxage)

**Type:** `number`

Specifies a number, in seconds, for which the cookie is valid.

##### `path`

[Section titled “path”](#path)

**Type:** `string`

Specifies a subpath of the domain in which the cookie is applied.

##### `sameSite`

[Section titled “sameSite”](#samesite)

**Type:** `boolean | 'lax' | 'none' | 'strict'`

Specifies the value of the [SameSite](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-09#section-5.4.7) cookie header.

##### `secure`

[Section titled “secure”](#secure)

**Type:** `boolean`

If true, the cookie is only set on https sites.

##### `encode`

[Section titled “encode”](#encode)

**Type:** `(value: string) => string`

Allows customizing how the cookie is serialized.

### `session`

[Section titled “session”](#session)

**Type:** `AstroSession`

**Added in:** `astro@5.7.0`

`session` is an object that allows data to be stored between requests for [routes rendered on demand](/en/guides/on-demand-rendering/). It is associated with a cookie that contains the session ID only: the data itself is not stored in the cookie.

The session is created when first used, and the session cookie is automatically set. The `session` object is `undefined` if no session storage has been configured, or if the current route is prerendered, and will log an error if you try to use it.

See [the session guide](/en/guides/sessions/) for more information on how to use sessions in your Astro project.

#### `get()`

[Section titled “get()”](#get)

**Type**: `(key: string) => Promise<any>`

Returns the value of the given key in the session. If the key does not exist, it returns `undefined`.

* Astro.session

  src/components/Cart.astro

  ```astro
  ---
  const cart = await Astro.session?.get('cart');
  ---
  <button>🛒 {cart?.length}</button>
  ```

* context.session

  src/pages/api/cart.ts

  ```ts
  import type { APIContext } from 'astro';


  export async function GET({ session }: APIContext) {
    const cart = await session.get('cart');
    return Response.json({ cart });
  }
  ```

#### `set()`

[Section titled “set()”](#set)

**Type**: `(key: string, value: any, options?: { ttl: number }) => void`

Sets the value of the given key in the session. The value can be any serializable type. This method is synchronous and the value is immediately available for retrieval, but it is not saved to the backend until the end of the request.

* Astro.session

  src/pages/products/\[slug].astro

  ```astro
  ---
  const { slug } = Astro.params;
  Astro.session?.set('lastViewedProduct', slug);
  ---
  ```

* context.session

  src/pages/api/add-to-cart.ts

  ```ts
  import type { APIContext } from 'astro';


  export async function POST({ session, request }: APIContext) {
    const cart = await session.get('cart');
    const newItem = await request.json();
    cart.push(newItem);
    // Save the updated cart to the session
    session.set('cart', cart);
    return Response.json({ cart });
  }
  ```

#### `regenerate()`

[Section titled “regenerate()”](#regenerate)

**Type**: `() => void`

Regenerates the session ID. Call this when a user logs in or escalates their privileges, to prevent session fixation attacks.

* Astro.session

  src/pages/welcome.astro

  ```astro
  ---
  Astro.session?.regenerate();
  ---
  ```

* context.session

  src/pages/api/login.ts

  ```ts
  import type { APIContext } from 'astro';


  export async function POST({ session }: APIContext) {
    // Authenticate the user...
    doLogin();
    // Regenerate the session ID to prevent session fixation attacks
    session.regenerate();
    return Response.json({ success: true });
  }
  ```

#### `destroy()`

[Section titled “destroy()”](#destroy)

**Type**: `() => void`

Destroys the session, deleting the cookie and the object from the backend. Call this when a user logs out or their session is otherwise invalidated.

* Astro.session

  src/pages/logout.astro

  ```astro
  ---
  Astro.session?.destroy();
  return Astro.redirect('/login');
  ---
  ```

* context.session

  src/pages/api/logout.ts

  ```ts
  import type { APIContext } from 'astro';


  export async function POST({ session }: APIContext) {
    session.destroy();
    return Response.json({ success: true });
  }
  ```

#### `load()`

[Section titled “load()”](#load)

**Type**: `(id: string) => Promise<void>`

Loads a session by ID. In normal use, a session is loaded automatically from the request cookie. Use this method to load a session from a different ID. This is useful if you are handling the session ID yourself, or if you want to keep track of a session without using cookies.

* Astro.session

  src/pages/cart.astro

  ```astro
  ---
  // Load the session from a header instead of cookies
  const sessionId = Astro.request.headers.get('x-session-id');
  await Astro.session?.load(sessionId);
  const cart = await Astro.session?.get('cart');
  ---
  <h1>Your cart</h1>
  <ul>
    {cart?.map((item) => (
      <li>{item.name}</li>
    ))}
  </ul>
  ```

* context.session

  src/pages/api/load-session.ts

  ```ts
  import type { APIRoute } from 'astro';


  export const GET: APIRoute = async ({ session, request }) => {
    // Load the session from a header instead of cookies
    const sessionId = request.headers.get('x-session-id');
    await session.load(sessionId);
    const cart = await session.get('cart');
    return Response.json({ cart });
  };
  ```

### Deprecated object properties

[Section titled “Deprecated object properties”](#deprecated-object-properties)

#### `Astro.glob()`

[Section titled “Astro.glob()”](#astroglob)

Deprecated in v5.0

Use [Vite’s `import.meta.glob`](https://vite.dev/guide/features.html#glob-import) to query project files.

`Astro.glob('../pages/post/*.md')` can be replaced with:

`Object.values(import.meta.glob('../pages/post/*.md', { eager: true }));`

See the [imports guide](/en/guides/imports/#importmetaglob) for more information and usage.

`Astro.glob()` is a way to load many local files into your static site setup.

src/components/my-component.astro

```astro
---
const posts = await Astro.glob('../pages/post/*.md'); // returns an array of posts that live at ./src/pages/post/*.md
---


<div>
{posts.slice(0, 3).map((post) => (
  <article>
    <h2>{post.frontmatter.title}</h2>
    <p>{post.frontmatter.description}</p>
    <a href={post.url}>Read more</a>
  </article>
))}
</div>
```

`.glob()` only takes one parameter: a relative URL glob of which local files you’d like to import. It’s asynchronous and returns an array of the exports from matching files.

`.glob()` can’t take variables or strings that interpolate them, as they aren’t statically analyzable. (See [the imports guide](/en/guides/imports/#supported-values) for a workaround.) This is because `Astro.glob()` is a wrapper of Vite’s [`import.meta.glob()`](https://vite.dev/guide/features.html#glob-import).

Note

You can also use `import.meta.glob()` itself in your Astro project. You may want to do this when:

* You need this feature in a file that isn’t `.astro`, like an API route. `Astro.glob()` is only available in `.astro` files, while `import.meta.glob()` is available anywhere in the project.
* You don’t want to load each file immediately. `import.meta.glob()` can return functions that import the file content, rather than returning the content itself. Note that this import includes all styles and scripts for any imported files. These will be bundled and added to the page whether or not a file is actually used, as this is decided by static analysis, not at runtime.
* You want access to each file’s path. `import.meta.glob()` returns a map of a file’s path to its content, while `Astro.glob()` returns a list of content.
* You want to pass multiple patterns; for example, you want to add a “negative pattern” that filters out certain files. `import.meta.glob()` can optionally take an array of glob strings, rather than a single string.

Read more in the [Vite documentation](https://vite.dev/guide/features.html#glob-import).

##### Markdown Files

[Section titled “Markdown Files”](#markdown-files)

Markdown files loaded with `Astro.glob()` return the following `MarkdownInstance` interface:

```ts
export interface MarkdownInstance<T extends Record<string, any>> {
  /* Any data specified in this file's YAML/TOML frontmatter */
  frontmatter: T;
  /* The absolute file path of this file */
  file: string;
  /* The rendered path of this file */
  url: string | undefined;
  /* Astro Component that renders the contents of this file */
  Content: AstroComponentFactory;
  /** (Markdown only) Raw Markdown file content, excluding layout HTML and YAML/TOML frontmatter */
  rawContent(): string;
  /** (Markdown only) Markdown file compiled to HTML, excluding layout HTML */
  compiledContent(): string;
  /* Function that returns an array of the h1...h6 elements in this file */
  getHeadings(): Promise<{ depth: number; slug: string; text: string }[]>;
  default: AstroComponentFactory;
}
```

You can optionally provide a type for the `frontmatter` variable using a TypeScript generic.

```astro
---
interface Frontmatter {
  title: string;
  description?: string;
}
const posts = await Astro.glob<Frontmatter>('../pages/post/*.md');
---


<ul>
  {posts.map(post => <li>{post.frontmatter.title}</li>)}
</ul>
```

##### Astro Files

[Section titled “Astro Files”](#astro-files)

Astro files have the following interface:

```ts
export interface AstroInstance {
  /* The file path of this file */
  file: string;
  /* The URL for this file (if it is in the pages directory) */
  url: string | undefined;
  default: AstroComponentFactory;
}
```

##### Other Files

[Section titled “Other Files”](#other-files)

Other files may have various different interfaces, but `Astro.glob()` accepts a TypeScript generic if you know exactly what an unrecognized file type contains.

```ts
---
interface CustomDataFile {
  default: Record<string, any>;
}
const data = await Astro.glob<CustomDataFile>('../data/**/*.js');
---
```

# Template expressions reference

Astro component syntax is a superset of HTML. The syntax was designed to feel familiar to anyone with experience writing HTML or JSX, and adds support for including components and JavaScript expressions.

## JSX-like Expressions

[Section titled “JSX-like Expressions”](#jsx-like-expressions)

You can define local JavaScript variables inside of the frontmatter component script between the two code fences (`---`) of an Astro component. You can then inject these variables into the component’s HTML template using JSX-like expressions!

Dynamic vs reactive

Using this approach, you can include **dynamic** values that are calculated in the frontmatter. But once included, these values are not **reactive** and will never change. Astro components are templates that only run once, during the rendering step.

See below for more examples of [differences between Astro and JSX](#differences-between-astro-and-jsx).

### Variables

[Section titled “Variables”](#variables)

Local variables can be added into the HTML using the curly braces syntax:

src/components/Variables.astro

```astro
---
const name = "Astro";
---
<div>
  <h1>Hello {name}!</h1>  <!-- Outputs <h1>Hello Astro!</h1> -->
</div>
```

### Dynamic Attributes

[Section titled “Dynamic Attributes”](#dynamic-attributes)

Local variables can be used in curly braces to pass attribute values to both HTML elements and components:

src/components/DynamicAttributes.astro

```astro
---
const name = "Astro";
---
<h1 class={name}>Attribute expressions are supported</h1>


<MyComponent templateLiteralNameAttribute={`MyNameIs${name}`} />
```

Caution

HTML attributes will be converted to strings, so it is not possible to pass functions and objects to HTML elements. For example, you can’t assign an event handler to an HTML element in an Astro component:

dont-do-this.astro

```astro
---
function handleClick () {
    console.log("button clicked!");
}
---
<!-- ❌ This doesn't work! ❌ -->
<button onClick={handleClick}>Nothing will happen when you click me!</button>
```

Instead, use a client-side script to add the event handler, like you would in vanilla JavaScript:

do-this-instead.astro

```astro
---
---
<button id="button">Click Me</button>
<script>
  function handleClick () {
    console.log("button clicked!");
  }
  document.getElementById("button").addEventListener("click", handleClick);
</script>
```

### Dynamic HTML

[Section titled “Dynamic HTML”](#dynamic-html)

Local variables can be used in JSX-like functions to produce dynamically-generated HTML elements:

src/components/DynamicHtml.astro

```astro
---
const items = ["Dog", "Cat", "Platypus"];
---
<ul>
  {items.map((item) => (
    <li>{item}</li>
  ))}
</ul>
```

Astro can conditionally display HTML using JSX logical operators and ternary expressions.

src/components/ConditionalHtml.astro

```astro
---
const visible = true;
---
{visible && <p>Show me!</p>}


{visible ? <p>Show me!</p> : <p>Else show me!</p>}
```

### Dynamic Tags

[Section titled “Dynamic Tags”](#dynamic-tags)

You can also use dynamic tags by assigning an HTML tag name to a variable or with a component import reassignment:

src/components/DynamicTags.astro

```astro
---
import MyComponent from "./MyComponent.astro";
const Element = 'div'
const Component = MyComponent;
---
<Element>Hello!</Element> <!-- renders as <div>Hello!</div> -->
<Component /> <!-- renders as <MyComponent /> -->
```

When using dynamic tags:

* **Variable names must be capitalized.** For example, use `Element`, not `element`. Otherwise, Astro will try to render your variable name as a literal HTML tag.

* **Hydration directives are not supported.** When using [`client:*` hydration directives](/en/guides/framework-components/#hydrating-interactive-components), Astro needs to know which components to bundle for production, and the dynamic tag pattern prevents this from working.

* **The [define:vars directive](/en/reference/directives-reference/#definevars) is not supported.** If you cannot wrap the children with an extra element (e.g `<div>`), then you can manually add a ``style={`--myVar:${value}`}`` to your Element.

### Fragments

[Section titled “Fragments”](#fragments)

Astro supports `<> </>` notation and also provides a built-in `<Fragment />` component. This component can be useful to avoid wrapper elements when adding [`set:*` directives](/en/reference/directives-reference/#sethtml) to inject an HTML string.

The following example renders paragraph text using the `<Fragment />` component:

src/components/SetHtml.astro

```astro
---
const htmlString = '<p>Raw HTML content</p>';
---
<Fragment set:html={htmlString} />
```

### Differences between Astro and JSX

[Section titled “Differences between Astro and JSX”](#differences-between-astro-and-jsx)

Astro component syntax is a superset of HTML. It was designed to feel familiar to anyone with HTML or JSX experience, but there are a couple of key differences between `.astro` files and JSX.

#### Attributes

[Section titled “Attributes”](#attributes)

In Astro, you use the standard `kebab-case` format for all HTML attributes instead of the `camelCase` used in JSX. This even works for `class`, which is not supported by React.

example.astro

```diff
<div className="box" dataValue="3" />
<div class="box" data-value="3" />
```

#### Multiple Elements

[Section titled “Multiple Elements”](#multiple-elements)

An Astro component template can render multiple elements with no need to wrap everything in a single `<div>` or `<>`, unlike JavaScript or JSX.

src/components/RootElements.astro

```astro
---
// Template with multiple elements
---
<p>No need to wrap elements in a single containing element.</p>
<p>Astro supports multiple root elements in a template.</p>
```

#### Comments

[Section titled “Comments”](#comments)

In Astro, you can use standard HTML comments or JavaScript-style comments.

example.astro

```astro
---
---
<!-- HTML comment syntax is valid in .astro files -->
{/* JS comment syntax is also valid */}
```

Caution

HTML-style comments will be included in browser DOM, while JS ones will be skipped. To leave TODO messages or other development-only explanations, you may wish to use JavaScript-style comments instead.

## Component utilities

[Section titled “Component utilities”](#component-utilities)

### `Astro.slots`

[Section titled “Astro.slots”](#astroslots)

`Astro.slots` contains utility functions for modifying an Astro component’s slotted children.

#### `Astro.slots.has()`

[Section titled “Astro.slots.has()”](#astroslotshas)

**Type:** `(slotName: string) => boolean`

You can check whether content for a specific slot name exists with `Astro.slots.has()`. This can be useful when you want to wrap slot contents but only want to render the wrapper elements when the slot is being used.

src/pages/index.astro

```astro
---
---
<slot />


{Astro.slots.has('more') && (
  <aside>
    <h2>More</h2>
    <slot name="more" />
  </aside>
)}
```

#### `Astro.slots.render()`

[Section titled “Astro.slots.render()”](#astroslotsrender)

**Type:** `(slotName: string, args?: any[]) => Promise<string>`

You can asynchronously render the contents of a slot to a string of HTML using `Astro.slots.render()`.

```astro
---
const html = await Astro.slots.render('default');
---
<Fragment set:html={html} />
```

Note

This is for advanced use cases! In most circumstances, it is simpler to render slot contents with [the `<slot />` element](/en/basics/astro-components/#slots).

`Astro.slots.render()` optionally accepts a second argument: an array of parameters that will be forwarded to any function children. This can be useful for custom utility components.

For example, this `<Shout />` component converts its `message` prop to uppercase and passes it to the default slot:

src/components/Shout.astro

```astro
---
const message = Astro.props.message.toUpperCase();
let html = '';
if (Astro.slots.has('default')) {
  html = await Astro.slots.render('default', [message]);
}
---
<Fragment set:html={html} />
```

A callback function passed as `<Shout />`’s child will receive the all-caps `message` parameter:

src/pages/index.astro

```astro
---
import Shout from "../components/Shout.astro";
---
<Shout message="slots!">
  {(message) => <div>{message}</div>}
</Shout>


<!-- renders as <div>SLOTS!</div> -->
```

Callback functions can be passed to named slots inside a wrapping HTML element tag with a `slot` attribute. This element is only used to transfer the callback to a named slot and will not be rendered onto the page.

```astro
<Shout message="slots!">
  <fragment slot="message">
    {(message) => <div>{message}</div>}
  </fragment>
</Shout>
```

Use a standard HTML element for the wrapping tag or any lowercase tag (e.g. `<fragment>` instead of `<Fragment />`) that will not be interpreted as a component. Do not use the HTML `<slot>` element as this will be interpreted as an Astro slot.

### `Astro.self`

[Section titled “Astro.self”](#astroself)

`Astro.self` allows Astro components to be recursively called. This behavior lets you render an Astro component from within itself by using `<Astro.self>` in the component template. This can help iterate over large data stores and nested data structures.

NestedList.astro

```astro
---
const { items } = Astro.props;
---
<ul class="nested-list">
  {items.map((item) => (
    <li>
      <!-- If there is a nested data-structure we render `<Astro.self>` -->
      <!-- and can pass props through with the recursive call -->
      {Array.isArray(item) ? (
        <Astro.self items={item} />
      ) : (
        item
      )}
    </li>
  ))}
</ul>
```

This component could then be used like this:

```astro
---
import NestedList from './NestedList.astro';
---
<NestedList items={['A', ['B', 'C'], 'D']} />
```

And would render HTML like this:

```html
<ul class="nested-list">
  <li>A</li>
  <li>
    <ul class="nested-list">
      <li>B</li>
      <li>C</li>
    </ul>
  </li>
  <li>D</li>
</ul>
```

# CLI Commands

You can use the Command-Line Interface (CLI) provided by Astro to develop, build, and preview your project from a terminal window.

### `astro` commands

[Section titled “astro commands”](#astro-commands)

Use the CLI by running one of the **commands** documented on this page with your preferred package manager, optionally followed by any **flags**. Flags customize the behavior of a command.

One of the commands you’ll use most often is `astro dev`. This command starts the development server and gives you a live, updating preview of your site in a browser as you work:

* npm

  ```shell
  # start the development server
  npx astro dev
  ```

* pnpm

  ```shell
  # start the development server
  pnpm astro dev
  ```

* Yarn

  ```shell
  # start the development server
  yarn astro dev
  ```

You can type `astro --help` in your terminal to display a list of all available commands:

* npm

  ```shell
  npx astro --help
  ```

* pnpm

  ```shell
  pnpm astro --help
  ```

* Yarn

  ```shell
  yarn astro --help
  ```

The following message will display in your terminal:

```bash
astro [command] [...flags]


Commands
              add  Add an integration.
            build  Build your project and write it to disk.
            check  Check your project for errors.
       create-key  Create a cryptography key
              dev  Start the development server.
             docs  Open documentation in your web browser.
             info  List info about your current Astro setup.
          preview  Preview your build locally.
             sync  Generate TypeScript types for all Astro modules.
      preferences  Configure user preferences.
        telemetry  Configure telemetry settings.


Global Flags
  --config <path>  Specify your config file.
    --root <path>  Specify your project root folder.
     --site <url>  Specify your project site.
--base <pathname>  Specify your project base.
        --verbose  Enable verbose logging.
         --silent  Disable all logging.
        --version  Show the version number and exit.
           --help  Show this help message.
```

You can add the `--help` flag after any command to get a list of all the flags for that command.

* npm

  ```shell
  # get a list of all flags for the `dev` command
  npm run dev -- --help
  ```

* pnpm

  ```shell
  # get a list of all flags for the `dev` command
  pnpm dev --help
  ```

* Yarn

  ```shell
  # get a list of all flags for the `dev` command
  yarn dev --help
  ```

The following message will display in your terminal:

```bash
astro dev [...flags]


Flags
                 --port  Specify which port to run on. Defaults to 4321.
                 --host  Listen on all addresses, including LAN and public addresses.
--host <custom-address>  Expose on a network IP address at <custom-address>
                 --open  Automatically open the app in the browser on server start
                --force  Clear the content layer cache, forcing a full rebuild.
            --help (-h)  See all available flags.
```

Note

The extra `--` before any flag is necessary for `npm` to pass your flags to the `astro` command.

### `package.json` scripts

[Section titled “package.json scripts”](#packagejson-scripts)

You can also use scripts in `package.json` for shorter versions of these commands. Using a script allows you to use the same commands that you may be familiar with from other projects, such as `npm run build`.

The following scripts for the most common `astro` commands (`astro dev`, `astro build`, and `astro preview`) are added for you automatically when you create a project using [the `create astro` wizard](/en/install-and-setup/).

When you follow the instructions to [install Astro manually](/en/install-and-setup/#manual-setup), you are instructed to add these scripts yourself. You can also add more scripts to this list manually for any commands you use frequently.

package.json

```json
{
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  }
}
```

You will often use these `astro` commands, or the scripts that run them, without any flags. Add flags to the command when you want to customize the command’s behavior. For example, you may wish to start the development server on a different port, or build your site with verbose logs for debugging.

* npm

  ```shell
  # run the dev server on port 8080 using the `dev` script in `package.json`
  npm run dev -- --port 8080


  # build your site with verbose logs using the `build` script in `package.json`
  npm run build -- --verbose
  ```

* pnpm

  ```shell
  # run the dev server on port 8080 using the `dev` script in `package.json`
  pnpm dev --port 8080


  # build your site with verbose logs using the `build` script in `package.json`
  pnpm build --verbose
  ```

* Yarn

  ```shell
  # run the dev server on port 8080 using the `dev` script in `package.json`
  yarn dev --port 8080


  # build your site with verbose logs using the `build` script in `package.json`
  yarn build --verbose
  ```

## `astro dev`

[Section titled “astro dev”](#astro-dev)

Runs Astro’s development server. This is a local HTTP server that doesn’t bundle assets. It uses Hot Module Replacement (HMR) to update your browser as you save changes in your editor.

The following hotkeys can be used in the terminal where the Astro development server is running:

* `s + enter` to sync the content layer data (content and types).
* `o + enter` to open your Astro site in the browser.
* `q + enter` to quit the development server.

## `astro build`

[Section titled “astro build”](#astro-build)

Builds your site for deployment. By default, this will generate static files and place them in a `dist/` directory. If any routes are [rendered on demand](/en/guides/on-demand-rendering/), this will generate the necessary server files to serve your site.

### Flags

[Section titled “Flags”](#flags)

The command accepts [common flags](#common-flags) and the following additional flags:

#### `--devOutput`

[Section titled “--devOutput”](#--devoutput)

**Added in:** `astro@5.0.0`

Outputs a development-based build similar to code transformed in `astro dev`. This can be useful to test build-only issues with additional debugging information included.

## `astro preview`

[Section titled “astro preview”](#astro-preview)

Starts a local server to serve the contents of your static directory (`dist/` by default) created by running `astro build`.

This command allows you to preview your site locally [after building](#astro-build) to catch any errors in your build output before deploying it. It is not designed to be run in production. For help with production hosting, check out our guide on [Deploying an Astro Website](/en/guides/deploy/).

Since Astro 1.5.0, the [Node adapter](/en/guides/integrations-guide/node/) supports `astro preview` for builds generated with on-demand rendering.

Can be combined with the [common flags](#common-flags) documented below.

## `astro check`

[Section titled “astro check”](#astro-check)

Runs diagnostics (such as type-checking within `.astro` files) against your project and reports errors to the console. If any errors are found the process will exit with a code of **1**.

This command is intended to be used in CI workflows.

### Flags

Use these flags to customize the behavior of the command.

#### `--watch`

[Section titled “--watch”](#--watch)

The command will watch for any changes in your project, and will report any errors.

#### `--root <path-to-dir>`

[Section titled “--root \<path-to-dir>”](#--root-path-to-dir)

Specifies a different root directory to check. Uses the current working directory by default.

#### `--tsconfig <path-to-file>`

[Section titled “--tsconfig \<path-to-file>”](#--tsconfig-path-to-file)

Specifies a `tsconfig.json` file to use manually. If not provided, Astro will attempt to find a config, or infer the project’s config automatically.

#### `--minimumFailingSeverity <error|warning|hint>`

[Section titled “--minimumFailingSeverity \<error|warning|hint>”](#--minimumfailingseverity-errorwarninghint)

Specifies the minimum severity needed to exit with an error code. Defaults to `error`.

For example, running `astro check --minimumFailingSeverity warning` will cause the command to exit with an error if any warnings are detected.

#### `--minimumSeverity <error|warning|hint>`

[Section titled “--minimumSeverity \<error|warning|hint>”](#--minimumseverity-errorwarninghint)

Specifies the minimum severity to output. Defaults to `hint`.

For example, running `astro check --minimumSeverity warning` will show errors and warning, but not hints.

#### `--preserveWatchOutput`

[Section titled “--preserveWatchOutput”](#--preservewatchoutput)

Specifies not to clear the output between checks when in watch mode.

#### `--noSync`

[Section titled “--noSync”](#--nosync)

Specifies not to run `astro sync` before checking the project.

Read more about [type checking in Astro](/en/guides/typescript/#type-checking).

## `astro sync`

[Section titled “astro sync”](#astro-sync)

**Added in:** `astro@2.0.0`

Tip

Running `astro dev`, `astro build` or `astro check` will run the `sync` command as well.

Generates TypeScript types for all Astro modules. This sets up a [`.astro/types.d.ts` file](/en/guides/typescript/#setup) for type inferencing, and defines modules for features that rely on generated types:

* The `astro:content` module for the [Content Collections API](/en/guides/content-collections/).
* The `astro:db` module for [Astro DB](/en/guides/astro-db/).
* The `astro:env` module for [Astro Env](/en/guides/environment-variables/).
* The `astro:actions` module for [Astro Actions](/en/guides/actions/)

## `astro add`

[Section titled “astro add”](#astro-add)

Adds an integration to your configuration. Read more in [the integrations guide](/en/guides/integrations-guide/#automatic-integration-setup).

## `astro docs`

[Section titled “astro docs”](#astro-docs)

Launches the Astro Docs website directly from the terminal.

## `astro info`

[Section titled “astro info”](#astro-info)

Reports useful information about your current Astro environment. Useful for providing information when opening an issue.

```shell
astro info
```

Example output:

```plaintext
Astro                    v5.14.1
Vite                     v6.3.6
Node                     v22.17.1
System                   macOS (arm64)
Package Manager          npm
Output                   static
Adapter                  none
Integrations             @astrojs/starlight (v0.35.3)
```

## `astro preferences`

[Section titled “astro preferences”](#astro-preferences)

Manage user preferences with the `astro preferences` command. User preferences are specific to individual Astro users, unlike the `astro.config.mjs` file which changes behavior for everyone working on a project.

User preferences are scoped to the current project by default, stored in a local `.astro/settings.json` file.

Using the `--global` flag, user preferences can also be applied to every Astro project on the current machine. Global user preferences are stored in an operating system-specific location.

### Available preferences

* `devToolbar` — Enable or disable the development toolbar in the browser. (Default: `true`)
* `checkUpdates` — Enable or disable automatic update checks for the Astro CLI. (Default: `true`)

The `list` command prints the current settings of all configurable user preferences. It also supports a machine-readable `--json` output.

```shell
astro preferences list
```

Example terminal output:

| Preference           | Value |
| -------------------- | ----- |
| devToolbar.enabled   | true  |
|                      |       |
| checkUpdates.enabled | true  |

You can `enable`, `disable`, or `reset` preferences to their default.

For example, to disable the devToolbar in a specific Astro project:

```shell
astro preferences disable devToolbar
```

To disable the devToolbar in all Astro projects on the current machine:

```shell
astro preferences disable --global devToolbar
```

The devToolbar can later be enabled with:

```shell
astro preferences enable devToolbar
```

The `reset` command resets a preference to its default value:

```shell
astro preferences reset devToolbar
```

## `astro telemetry`

[Section titled “astro telemetry”](#astro-telemetry)

Sets telemetry configuration for the current CLI user. Telemetry is anonymous data that provides the Astro team insights into which Astro features are most often used. For more information see [Astro’s telemetry page](https://astro.build/telemetry/).

Telemetry can be disabled with this CLI command:

```shell
astro telemetry disable
```

Telemetry can later be re-enabled with:

```shell
astro telemetry enable
```

The `reset` command resets the telemetry data:

```shell
astro telemetry reset
```

Want to disable telemetry in CI environments?

Add the `astro telemetry disable` command to your CI scripts or set the `ASTRO_TELEMETRY_DISABLED` environment variable.

## `astro create-key`

[Section titled “astro create-key”](#astro-create-key)

Generates a key to encrypt props passed to server islands.

```shell
astro create-key
```

Set this key as the `ASTRO_KEY` environment variable (e.g. in a `.env` file) and include it in your CI/CD or host’s build settings when you need [a constant encryption key for your server islands](/en/guides/server-islands/#reusing-the-encryption-key) for situations like rolling deployments, multi-region hosting or a CDN that caches pages containing server islands.

## Common flags

[Section titled “Common flags”](#common-flags)

### `--root <path>`

[Section titled “--root \<path>”](#--root-path)

Specifies the path to the project root. If not specified, the current working directory is assumed to be the root.

The root is used for finding the Astro configuration file.

```shell
astro --root myRootFolder/myProjectFolder dev
```

### `--config <path>`

[Section titled “--config \<path>”](#--config-path)

Specifies the path to the config file relative to the project root. Defaults to `astro.config.mjs`. Use this if you use a different name for your configuration file or have your config file in another folder.

```shell
astro --config config/astro.config.mjs dev
```

### `--force <string>`

[Section titled “--force \<string>”](#--force-string)

**Added in:** `astro@5.0.0`

Clear the [content layer cache](/en/guides/content-collections/#defining-the-collection-loader), forcing a full rebuild.

### `--mode <string>`

[Section titled “--mode \<string>”](#--mode-string)

**Added in:** `astro@5.0.0`

Configures the [`mode`](/en/reference/programmatic-reference/#mode) inline config for your project.

### `--outDir <path>`

[Section titled “--outDir \<path>”](#--outdir-path)

**Added in:** `astro@3.3.0`

Configures the [`outDir`](/en/reference/configuration-reference/#outdir) for your project. Passing this flag will override the `outDir` value in your `astro.config.mjs` file, if one exists.

### `--site <url>`

[Section titled “--site \<url>”](#--site-url)

Configures the [`site`](/en/reference/configuration-reference/#site) for your project. Passing this flag will override the `site` value in your `astro.config.mjs` file, if one exists.

### `--base <pathname>`

[Section titled “--base \<pathname>”](#--base-pathname)

**Added in:** `astro@1.4.1`

Configures the [`base`](/en/reference/configuration-reference/#base) for your project. Passing this flag will override the `base` value in your `astro.config.mjs` file, if one exists.

### `--port <number>`

[Section titled “--port \<number>”](#--port-number)

Specifies which port to run the dev server and preview server on. Defaults to `4321`.

### `--host [optional host address]`

[Section titled “--host \[optional host address\]”](#--host-optional-host-address)

Sets which network IP addresses the dev server and preview server should listen on (i.e. non-localhost IPs). This can be useful for testing your project on local devices like a mobile phone during development.

* `--host` — listen on all addresses, including LAN and public addresses
* `--host <custom-address>` — expose on a network IP address at `<custom-address>`

Caution

Do not use the `--host` flag to expose the dev server and preview server in a production environment. The servers are designed for local use while developing your site only.

### `--allowed-hosts`

[Section titled “--allowed-hosts”](#--allowed-hosts)

**Added in:** `astro@5.4.0`

Specifies the hostnames that Astro is allowed to respond to in `dev` or `preview` modes. Can be passed a comma-separated list of hostnames or `true` to allow any hostname.

Refer to [Vite’s `allowedHosts` feature](https://vite.dev/config/server-options.html#server-allowedhosts) for more information, including security implications of allowing hostnames.

### `--verbose`

[Section titled “--verbose”](#--verbose)

Enables verbose logging, which is helpful when debugging an issue.

### `--silent`

[Section titled “--silent”](#--silent)

Enables silent logging, which will run the server without any console output.

### `--open`

[Section titled “--open”](#--open)

Automatically opens the app in the browser on server start. Can be passed a full URL string (e.g. `--open http://example.com`) or a pathname (e.g. `--open /about`) to specify the URL to open.

## Global flags

[Section titled “Global flags”](#global-flags)

Use these flags to get information about the `astro` CLI.

### `--version`

[Section titled “--version”](#--version)

Prints the Astro version number and exits.

### `--help`

[Section titled “--help”](#--help)

Prints the help message and exits.


---

**Navigation:** [← Previous](./10-upgrade-to-astro-v5.md) | [Index](./index.md) | [Next →](./12-configuration-reference.md)
