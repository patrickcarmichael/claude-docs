---
title: "@astrojs/svelte"
section: 147
---

# @astrojs/svelte

> Learn how to use the @astrojs/svelte framework integration to extend component support in your Astro project.

This **[Astro integration](/en/guides/integrations-guide/)** enables rendering and client-side hydration for your [Svelte](https://svelte.dev/) 5 components. For Svelte 3 and 4 support, install `@astrojs/svelte@5` instead.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/svelte`, run the following from your project directory and follow the prompts:

* npm

  ```sh
  npx astro add svelte
  ```jsx
* pnpm

  ```sh
  pnpm astro add svelte
  ```jsx
* Yarn

  ```sh
  yarn astro add svelte
  ```jsx
If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/svelte` package:

* npm

  ```sh
  npm install @astrojs/svelte
  ```jsx
* pnpm

  ```sh
  pnpm add @astrojs/svelte
  ```jsx
* Yarn

  ```sh
  yarn add @astrojs/svelte
  ```jsx
Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'svelte'` (or similar) warning when you start up Astro, you’ll need to install Svelte and TypeScript:

* npm

  ```sh
  npm install svelte typescript
  ```jsx
* pnpm

  ```sh
  pnpm add svelte typescript
  ```jsx
* Yarn

  ```sh
  yarn add svelte typescript
  ```jsx
Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import svelte from '@astrojs/svelte';


export default defineConfig({
  // ...
  integrations: [svelte()],
});
```jsx
And create a new file called `svelte.config.js` in your project root directory and add the following code:

svelte.config.js

```js
import { vitePreprocess } from '@astrojs/svelte';


export default {
  preprocess: vitePreprocess(),
}
```jsx
## Getting started

[Section titled “Getting started”](#getting-started)

To use your first Svelte component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

* 📦 how framework components are loaded,
* 💧 client-side hydration options, and
* 🤝 opportunities to mix and nest frameworks together

## Options

[Section titled “Options”](#options)

This integration is powered by `@sveltejs/vite-plugin-svelte`. To customize the Svelte compiler, options can be provided to the integration. See the [`@sveltejs/vite-plugin-svelte` docs](https://github.com/sveltejs/vite-plugin-svelte/blob/HEAD/docs/config.md) for more details.

You can set options either by passing them to the `svelte` integration in `astro.config.mjs` or in `svelte.config.js`. The options in `astro.config.mjs` will take precedence over the options in `svelte.config.js` if both are present:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import svelte from '@astrojs/svelte';


export default defineConfig({
  integrations: [svelte({ extensions: ['.svelte'] })],
});
```jsx
svelte.config.js

```js
export default {
  extensions: ['.svelte'],
};
```jsx
## Preprocessors

[Section titled “Preprocessors”](#preprocessors)

**Added in:** `@astrojs/svelte@2.0.0`

If you’re using SCSS or Stylus in your Svelte files, you can create a `svelte.config.js` file so that they are preprocessed by Svelte, and the Svelte IDE extension can correctly parse the Svelte files.

svelte.config.js

```js
import { vitePreprocess } from '@astrojs/svelte';


export default {
  preprocess: vitePreprocess(),
};
```jsx
This config file will be automatically added for you when you run `astro add svelte`. See the [`@sveltejs/vite-plugin-svelte` docs](https://github.com/sveltejs/vite-plugin-svelte/blob/HEAD/docs/preprocess.md) for more details about `vitePreprocess`.

---

[← Previous](146-astrojssolid-js.md) | [Index](index.md) | [Next →](index.md)
