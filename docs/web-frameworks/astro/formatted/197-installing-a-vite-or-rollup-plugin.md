---
title: "Installing a Vite or Rollup plugin"
section: 197
---

# Installing a Vite or Rollup plugin

> Learn how you can import YAML data by adding a Rollup plugin to your project.

Astro builds on top of Vite, and supports both Vite and Rollup plugins. This recipe uses a Rollup plugin to add the ability to import a YAML (`.yml`) file in Astro.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install `@rollup/plugin-yaml`:

   * npm

     ```shell
     npm install @rollup/plugin-yaml --save-dev
     ```jsx
   * pnpm

     ```shell
     pnpm add @rollup/plugin-yaml --save-dev
     ```jsx
   * Yarn

     ```shell
     yarn add @rollup/plugin-yaml --dev
     ```jsx
2. Import the plugin in your `astro.config.mjs` and add it to the Vite plugins array:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import yaml from '@rollup/plugin-yaml';


   export default defineConfig({
   +  vite: {
   +    plugins: [yaml()]
   +  }
   });
   ```jsx
3. Finally, you can import YAML data using an `import` statement:

   ```js
   import yml from './data.yml';
   ```jsx
   Note

   While you can now import YAML data in your Astro project, your editor will not provide types for the imported data. To add types, create or find an existing `*.d.ts` file in the `src` directory of your project and add the following:

   src/files.d.ts

   ```ts
   // Specify the file extension you want to import
   declare module "*.yml" {
     const value: any; // Add type definitions here if desired
     export default value;
   }
   ```jsx
   This will allow your editor to provide type hints for your YAML data.

---

[← Previous](196-astro-recipes.md) | [Index](index.md) | [Next →](index.md)
