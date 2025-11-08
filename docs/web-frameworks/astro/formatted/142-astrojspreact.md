---
title: "@astrojs/preact"
section: 142
---

# @astrojs/preact

> Learn how to use the @astrojs/preact framework integration to extend component support in your Astro project.

This **[Astro integration](/en/guides/integrations-guide/)** enables rendering and client-side hydration for your [Preact](https://preactjs.com/) components.

## Why Preact?

[Section titled “Why Preact?”](#why-preact)

Preact is a library that lets you build interactive UI components for the web. If you want to build interactive features on your site using JavaScript, you may prefer using its component format instead of using browser APIs directly.

Preact is also a great choice if you have previously used React. Preact provides the same API as React, but in a much smaller 3kB package. It even supports rendering many React components using the `compat` configuration option (see below).

**Want to learn more about Preact before using this integration?**\
Check out [“Learn Preact”](https://preactjs.com/tutorial), an interactive tutorial on their website.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/preact`, run the following from your project directory and follow the prompts:

* npm

  ```sh
  npx astro add preact
  ```jsx
* pnpm

  ```sh
  pnpm astro add preact
  ```jsx
* Yarn

  ```sh
  yarn astro add preact
  ```jsx
If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/preact` package:

* npm

  ```sh
  npm install @astrojs/preact
  ```jsx
* pnpm

  ```sh
  pnpm add @astrojs/preact
  ```jsx
* Yarn

  ```sh
  yarn add @astrojs/preact
  ```jsx
Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'preact'` (or similar) warning when you start up Astro, you’ll need to install Preact:

* npm

  ```sh
  npm install preact
  ```jsx
* pnpm

  ```sh
  pnpm add preact
  ```jsx
* Yarn

  ```sh
  yarn add preact
  ```jsx
Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import preact from '@astrojs/preact';


export default defineConfig({
  // ...
  integrations: [preact()],
});
```jsx
And add the following code to the `tsconfig.json` file.

tsconfig.json

```diff
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"],
  +"compilerOptions": {
    +"jsx": "react-jsx",
    +"jsxImportSource": "preact"
+  }
}
```jsx
## Usage

[Section titled “Usage”](#usage)

To use your first Preact component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

* 📦 how framework components are loaded,
* 💧 client-side hydration options, and
* 🤝 opportunities to mix and nest frameworks together

Also check our [Astro Integration Documentation](/en/guides/integrations-guide/) for more on integrations.

## Configuration

[Section titled “Configuration”](#configuration)

The Astro Preact integration handles how Preact components are rendered and it has its own options. Change these in the `astro.config.mjs` file which is where your project’s integration settings live.

For basic usage, you do not need to configure the Preact integration.

### `compat`

[Section titled “compat”](#compat)

**Type:** `boolean`

**Added in:** `@astrojs/preact@0.3.0`

You can enable `preact/compat`, Preact’s compatibility layer for rendering React components without needing to install or ship React’s larger libraries to your users’ web browsers.

To do so, pass an object to the Preact integration and set `compat: true`.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import preact from '@astrojs/preact';


export default defineConfig({
  integrations: [preact({ compat: true })],
});
```jsx
With the `compat` option enabled, the Preact integration will render React components as well as Preact components in your project and also allow you to import React components inside Preact components. Read more in [“Switching to Preact (from React)”](https://preactjs.com/guide/v10/switching-to-preact) on the Preact website.

When importing React component libraries, in order to swap out the `react` and `react-dom` dependencies as `preact/compat`, you can use [`overrides`](https://docs.npmjs.com/cli/v8/configuring-npm/package-json#overrides) to do so.

package.json

```json
{
  "overrides": {
    "react": "npm:@preact/compat@latest",
    "react-dom": "npm:@preact/compat@latest"
  }
}
```jsx
Check out the [`pnpm` overrides](https://pnpm.io/package_json#pnpmoverrides) and [`yarn` resolutions](https://yarnpkg.com/configuration/manifest#resolutions) docs for their respective overrides features.

Note

Currently, the `compat` option only works for React libraries that export code as ESM. If an error happens during build-time, try adding the library to `vite.ssr.noExternal: ['the-react-library']` in your `astro.config.mjs` file.

### `devtools`

[Section titled “devtools”](#devtools)

**Type:** `boolean`

**Added in:** `@astrojs/preact@3.3.0`

You can enable [Preact devtools](https://preactjs.github.io/preact-devtools/) in development by passing an object with `devtools: true` to your `preact()` integration config:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import preact from '@astrojs/preact';


export default defineConfig({
  // ...
  integrations: [preact({ devtools: true })],
});
```jsx
## Options

[Section titled “Options”](#options)

### Combining multiple JSX frameworks

[Section titled “Combining multiple JSX frameworks”](#combining-multiple-jsx-frameworks)

When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import preact from '@astrojs/preact';
import react from '@astrojs/react';
import svelte from '@astrojs/svelte';
import vue from '@astrojs/vue';
import solid from '@astrojs/solid-js';


export default defineConfig({
  // Enable many frameworks to support all different kinds of components.
  // No `include` is needed if you are only using a single JSX framework!
  integrations: [
    preact({
      include: ['**/preact/*'],
    }),
    react({
      include: ['**/react/*'],
    }),
    solid({
      include: ['**/solid/*'],
    }),
  ],
});
```jsx
## Examples

[Section titled “Examples”](#examples)

* The [Astro Preact example](https://github.com/withastro/astro/tree/latest/examples/framework-preact) shows how to use an interactive Preact component in an Astro project.
* The [Astro Nanostores example](https://github.com/withastro/astro/tree/latest/examples/with-nanostores) shows how to share state between different components — and even different frameworks! — in an Astro project.

---

[← Previous](141-astrojspartytown.md) | [Index](index.md) | [Next →](index.md)
