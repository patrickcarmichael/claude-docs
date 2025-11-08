---
title: "Add Integrations"
section: 125
---

# Add Integrations

> Learn how to add integrations to your Astro project.

**Astro integrations** add new functionality and behaviors for your project with only a few lines of code. You can use an official integration, [integrations built by the community](#finding-more-integrations) or even [build a custom integration yourself](#building-your-own-integration).

Integrations can…

* Unlock React, Vue, Svelte, Solid, and other popular UI frameworks with a [renderer](/en/guides/framework-components/).
* Enable on-demand rendering with an [SSR adapter](/en/guides/on-demand-rendering/).
* Integrate tools like MDX, and Partytown with a few lines of code.
* Add new features to your project, like automatic sitemap generation.
* Write custom code that hooks into the build process, dev server, and more.

Integrations directory

Browse or search the complete set of hundreds of official and community integrations in our [integrations directory](https://astro.build/integrations/). Find packages to add to your Astro project for authentication, analytics, performance, SEO, accessibility, UI, developer tools, and more.

## Official Integrations

[Section titled “Official Integrations”](#official-integrations)

The following integrations are maintained by Astro.

### Front-end frameworks

* ![](/logos/alpine-js.svg)

  ### [@astrojs/​alpinejs](/en/guides/integrations-guide/alpinejs/)

* ![](/logos/preact.svg)

  ### [@astrojs/​preact](/en/guides/integrations-guide/preact/)

* ![](/logos/react.svg)

  ### [@astrojs/​react](/en/guides/integrations-guide/react/)

* ![](/logos/solid.svg)

  ### [@astrojs/​solid⁠-⁠js](/en/guides/integrations-guide/solid-js/)

* ![](/logos/svelte.svg)

  ### [@astrojs/​svelte](/en/guides/integrations-guide/svelte/)

* ![](/logos/vue.svg)

  ### [@astrojs/​vue](/en/guides/integrations-guide/vue/)

### Adapters

* ![](/logos/cloudflare-pages.svg)

  ### [@astrojs/​cloudflare](/en/guides/integrations-guide/cloudflare/)

* ![](/logos/netlify.svg)

  ### [@astrojs/​netlify](/en/guides/integrations-guide/netlify/)

* ![](/logos/node.svg)

  ### [@astrojs/​node](/en/guides/integrations-guide/node/)

* ![](/logos/vercel.svg)

  ### [@astrojs/​vercel](/en/guides/integrations-guide/vercel/)

### Other integrations

* ![](/logos/db.svg)

  ### [@astrojs/​db](/en/guides/integrations-guide/db/)

* ![](/logos/markdoc.svg)

  ### [@astrojs/​markdoc](/en/guides/integrations-guide/markdoc/)

* ![](/logos/mdx.svg)

  ### [@astrojs/​mdx](/en/guides/integrations-guide/mdx/)

* ![](/logos/partytown.svg)

  ### [@astrojs/​partytown](/en/guides/integrations-guide/partytown/)

* ![](/logos/sitemap.svg)

  ### [@astrojs/​sitemap](/en/guides/integrations-guide/sitemap/)

## Automatic Integration Setup

[Section titled “Automatic Integration Setup”](#automatic-integration-setup)

Astro includes an `astro add` command to automate the setup of official integrations. Several community plugins can also be added using this command. Please check each integration’s own documentation to see whether `astro add` is supported, or whether you must [install manually](#manual-installation).

Run the `astro add` command using the package manager of your choice and our automatic integration wizard will update your configuration file and install any necessary dependencies.

* npm

  ```shell
  npx astro add react
  ```jsx
* pnpm

  ```shell
  pnpm astro add react
  ```jsx
* Yarn

  ```shell
  yarn astro add react
  ```jsx
It’s even possible to add multiple integrations at the same time!

* npm

  ```shell
  npx astro add react sitemap partytown
  ```jsx
* pnpm

  ```shell
  pnpm astro add react sitemap partytown
  ```jsx
* Yarn

  ```shell
  yarn astro add react sitemap partytown
  ```jsx
Handling integration dependencies

If you see any warnings like `Cannot find package '[package-name]'` after adding an integration, your package manager may not have installed [peer dependencies](https://nodejs.org/en/blog/npm/peer-dependencies/) for you. To install these missing packages, run the following command:

* npm

  ```shell
  npm install [package-name]
  ```jsx
* pnpm

  ```shell
  pnpm add [package-name]
  ```jsx
* Yarn

  ```shell
  yarn add [package-name]
  ```jsx
### Manual Installation

[Section titled “Manual Installation”](#manual-installation)

Astro integrations are always added through the `integrations` property in your `astro.config.mjs` file.

There are three common ways to import an integration into your Astro project:

1. [Install an npm package integration](#installing-an-npm-package).

2. Import your own integration from a local file inside your project.

3. Write your integration inline, directly in your config file.

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import installedIntegration from '@astrojs/vue';
   import localIntegration from './my-integration.js';


   export default defineConfig({
     integrations: [
       // 1. Imported from an installed npm package
       installedIntegration(),
       // 2. Imported from a local JS file
       localIntegration(),
       // 3. An inline object
       {name: 'namespace:id', hooks: { /* ... */ }},
     ]
   });
   ```jsx
Check out the [Integration API](/en/reference/integrations-reference/) reference to learn all of the different ways that you can write an integration.

#### Installing an NPM package

[Section titled “Installing an NPM package”](#installing-an-npm-package)

Install an NPM package integration using a package manager, and then update `astro.config.mjs` manually.

For example, to install the `@astrojs/sitemap` integration:

1. Install the integration to your project dependencies using your preferred package manager:

   * npm

     ```shell
     npm install @astrojs/sitemap
     ```jsx
   * pnpm

     ```shell
     pnpm add @astrojs/sitemap
     ```jsx
   * Yarn

     ```shell
     yarn add @astrojs/sitemap
     ```jsx
2. Import the integration to your `astro.config.mjs` file, and add it to your `integrations[]` array, along with any configuration options:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import sitemap from '@astrojs/sitemap';


   export default defineConfig({
     // ...
     integrations: [sitemap()],
     // ...
   });
   ```jsx
   Note that different integrations may have different configuration settings. Read each integration’s documentation, and apply any necessary config options to your chosen integration in `astro.config.mjs`.

### Custom Options

[Section titled “Custom Options”](#custom-options)

Integrations are almost always authored as factory functions that return the actual integration object. This lets you pass arguments and options to the factory function that customize the integration for your project.

```js
integrations: [
  // Example: Customize your integration with function arguments
  sitemap({filter: true})
]
```jsx
### Toggle an Integration

[Section titled “Toggle an Integration”](#toggle-an-integration)

Falsy integrations are ignored, so you can toggle integrations on & off without worrying about left-behind `undefined` and boolean values.

```js
integrations: [
  // Example: Skip building a sitemap on Windows
  process.platform !== 'win32' && sitemap()
]
```jsx
## Upgrading Integrations

[Section titled “Upgrading Integrations”](#upgrading-integrations)

To upgrade all official integrations at once, run the `@astrojs/upgrade` command. This will upgrade both Astro and all official integrations to their latest versions.

### Automatic Upgrading

[Section titled “Automatic Upgrading”](#automatic-upgrading)

* npm

  ```shell
  # Upgrade Astro and official integrations together to latest
  npx @astrojs/upgrade
  ```jsx
* pnpm

  ```shell
  # Upgrade Astro and official integrations together to latest
  pnpm dlx @astrojs/upgrade
  ```jsx
* Yarn

  ```shell
  # Upgrade Astro and official integrations together to latest
  yarn dlx @astrojs/upgrade
  ```jsx
### Manual Upgrading

[Section titled “Manual Upgrading”](#manual-upgrading)

To upgrade one or more integrations manually, use the appropriate command for your package manager.

* npm

  ```shell
  # Example: upgrade React and Partytown integrations
  npm install @astrojs/react@latest @astrojs/partytown@latest
  ```jsx
* pnpm

  ```shell
  # Example: upgrade React and Partytown integrations
  pnpm add @astrojs/react@latest @astrojs/partytown@latest
  ```jsx
* Yarn

  ```shell
  # Example: upgrade React and Partytown integrations
  yarn add @astrojs/react@latest @astrojs/partytown@latest
  ```jsx
## Removing an Integration

[Section titled “Removing an Integration”](#removing-an-integration)

1. To remove an integration, first uninstall the integration from your project.

   * npm

     ```shell
     npm uninstall @astrojs/react
     ```jsx
   * pnpm

     ```shell
     pnpm remove @astrojs/react
     ```jsx
   * Yarn

     ```shell
     yarn remove @astrojs/react
     ```jsx
2. Next, remove the integration from your `astro.config.*` file:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';


   -import react from '@astrojs/react';


   export default defineConfig({
     integrations: [
       -react()
     ]
   });
   ```jsx
## Finding More Integrations

[Section titled “Finding More Integrations”](#finding-more-integrations)

You can find many integrations developed by the community in the [Astro Integrations Directory](https://astro.build/integrations/). Follow links there for detailed usage and configuration instructions.

## Building Your Own Integration

[Section titled “Building Your Own Integration”](#building-your-own-integration)

Astro’s Integration API is inspired by Rollup and Vite, and designed to feel familiar to anyone who has ever written a Rollup or Vite plugin before.

Check out the [Integration API](/en/reference/integrations-reference/) reference to learn what integrations can do and how to write one yourself.

---

[← Previous](124-imports-reference.md) | [Index](index.md) | [Next →](index.md)
