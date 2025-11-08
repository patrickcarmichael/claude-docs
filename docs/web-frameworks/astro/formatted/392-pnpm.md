---
title: "pnpm"
section: 392
---

# pnpm
pnpm create astro@latest demo -- --template minimal
```jsx
There are two initial files that will make up your individual package: `package.json` and `index.js`.

### `package.json`

[Section titled “package.json”](#packagejson)

The `package.json` in the package directory includes all of the information related to your package, including its description, dependencies, and any other package metadata.

```json
{
  "name": "my-component",
  "description": "Component description",
  "version": "1.0.0",
  "homepage": "https://github.com/owner/project#readme",
  "type": "module",
  "exports": {
    ".": "./index.js",
    "./astro": "./MyAstroComponent.astro",
    "./react": "./MyReactComponent.jsx"
  },
  "files": ["index.js", "MyAstroComponent.astro", "MyReactComponent.jsx"],
  "keywords": ["astro", "withastro", "astro-component", "...", "..."]
}
```jsx
#### `description`

[Section titled “description”](#description)

A short description of your component used to help others know what it does.

```json
{
  "description": "An Astro Element Generator"
}
```jsx
#### `type`

[Section titled “type”](#type)

The module format used by Node.js and Astro to interpret your `index.js` files.

```json
{
  "type": "module"
}
```jsx
Use `"type": "module"` so that your `index.js` can be used as an entrypoint with `import` and `export` .

#### `homepage`

[Section titled “homepage”](#homepage)

The url to the project homepage.

```json
{
  "homepage": "https://github.com/owner/project#readme"
}
```jsx
This is a great way to direct users to an online demo, documentation, or homepage for your project.

#### `exports`

[Section titled “exports”](#exports)

The entry points of a package when imported by name.

```json
{
  "exports": {
    ".": "./index.js",
    "./astro": "./MyAstroComponent.astro",
    "./react": "./MyReactComponent.jsx"
  }
}
```jsx
In this example, importing `my-component` would use `index.js`, while importing `my-component/astro` or `my-component/react` would use `MyAstroComponent.astro` or `MyReactComponent.jsx` respectively.

#### `files`

[Section titled “files”](#files)

An optional optimization to exclude unnecessary files from the bundle shipped to users via npm. Note that **only files listed here will be included in your package**, so if you add or change files necessary for your package to work, you must update this list accordingly.

```json
{
  "files": ["index.js", "MyAstroComponent.astro", "MyReactComponent.jsx"]
}
```jsx
#### `keywords`

[Section titled “keywords”](#keywords)

An array of keywords relevant to your component, used to help others [find your component on npm](https://www.npmjs.com/search?q=keywords:astro-component,withastro) and in any other search catalogs.

Add `astro-component` or `withastro` as a special keyword to maximize its discoverability in the Astro ecosystem.

```json
{
  "keywords": ["astro-component", "withastro", "... etc", "... etc"]
}
```jsx
Tip

Keywords are also used by our [integrations library](https://astro.build/integrations/)! [See below](#integrations-library) for a full list of keywords we look for in npm.

***

### `index.js`

[Section titled “index.js”](#indexjs)

The main **package entrypoint** used whenever your package is imported.

```js
export { default as MyAstroComponent } from './MyAstroComponent.astro';


export { default as MyReactComponent } from './MyReactComponent.jsx';
```jsx
This allows you to package multiple components together into a single interface.

#### Example: Using Named Imports

[Section titled “Example: Using Named Imports”](#example-using-named-imports)

```astro
---
import { MyAstroComponent } from 'my-component';
import { MyReactComponent } from 'my-component';
---
<MyAstroComponent />
<MyReactComponent />
```jsx
#### Example: Using Namespace Imports

[Section titled “Example: Using Namespace Imports”](#example-using-namespace-imports)

```astro
---
import * as Example from 'example-astro-component';
---
<Example.MyAstroComponent />
<Example.MyReactComponent />
```jsx
#### Example: Using Individual Imports

[Section titled “Example: Using Individual Imports”](#example-using-individual-imports)

```astro
---
import MyAstroComponent from 'example-astro-component/astro';
import MyReactComponent from 'example-astro-component/react';
---
<MyAstroComponent />
<MyReactComponent />
```jsx
***

## Developing your package

[Section titled “Developing your package”](#developing-your-package)

Astro does not have a dedicated “package mode” for development. Instead, you should use a demo project to develop and test your package inside of your project. This can be a private website only used for development, or a public demo/documentation website for your package.

If you are extracting components from an existing project, you can even continue to use that project to develop your now-extracted components.

## Testing your component

[Section titled “Testing your component”](#testing-your-component)

Astro does not currently ship a test runner. *(If you are interested in helping out with this, [join us on Discord!](https://astro.build/chat))*

In the meantime, our current recommendation for testing is:

1. Add a test `fixtures` directory to your `demo/src/pages` directory.

2. Add a new page for every test that you’d like to run.

3. Each page should include some different component usage that you’d like to test.

4. Run `astro build` to build your fixtures, then compare the output of the `dist/__fixtures__/` directory to what you expected.

   * my-project/demo/src/pages/\_\_fixtures\_\_/

     * test-name-01.astro
     * test-name-02.astro
     * test-name-03.astro

## Publishing your component

[Section titled “Publishing your component”](#publishing-your-component)

Once you have your package ready, you can publish it to npm using the `npm publish` command. If that fails, make sure that you have logged in via `npm login` and that your `package.json` is correct. If it succeeds, you’re done!

Notice that there was no `build` step for Astro packages. Any file type that Astro supports natively, such as `.astro`, `.ts`, `.jsx`, and `.css`, can be published directly without a build step.

If you need another file type that isn’t natively supported by Astro, add a build step to your package. This advanced exercise is left up to you.

## Integrations Library

[Section titled “Integrations Library”](#integrations-library)

Share your hard work by adding your integration to our [integrations library](https://astro.build/integrations/)!

Tip

Do you need some help building your integration, or just want to meet other integrations builders? We have a dedicated `#integrations` channel on our [Discord server](https://astro.build/chat). Come say hi!

### `package.json` data

[Section titled “package.json data”](#packagejson-data)

The library is automatically updated weekly, pulling in every package published to npm with the `astro-component` or `withastro` keyword.

The integrations library reads the `name`, `description`, `repository`, and `homepage` data from your `package.json`.

Avatars are a great way to highlight your brand in the library! Once your package is published you can [file a GitHub issue](https://github.com/withastro/astro.build/issues/new/choose) with your avatar attached and we will add it to your listing.

Tip

Need to override the information our library reads from npm? No problem! [File an issue](https://github.com/withastro/astro.build/issues/new/choose) with the updated information and we’ll make sure the custom `name`, `description`, or `homepage` is used instead.

### Categories

[Section titled “Categories”](#categories)

In addition to the required `astro-component` or `withastro` keyword, special keywords are also used to automatically organize packages. Including any of the keywords below will add your integration to the matching category in our integrations library.

| category          | keywords                                     |
| ----------------- | -------------------------------------------- |
| Accessibility     | `a11y`, `accessibility`                      |
| Adapters          | `astro-adapter`                              |
| Analytics         | `analytics`                                  |
| CSS + UI          | `css`, `ui`, `icon`, `icons`, `renderer`     |
| Frameworks        | `renderer`                                   |
| Content Loaders   | `astro-loader`                               |
| Images + Media    | `media`, `image`, `images`, `video`, `audio` |
| Performance + SEO | `performance`, `perf`, `seo`, `optimization` |
| Dev Toolbar       | `devtools`, `dev-overlay`, `dev-toolbar`     |
| Utilities         | `tooling`, `utils`, `utility`                |

Packages that don’t include any keyword matching a category will be shown as `Uncategorized`.

## Share

[Section titled “Share”](#share)

We encourage you to share your work, and we really do love seeing what our talented Astronauts create. Come and share what you create with us in our [Discord](https://astro.build/chat) or mention [@astrodotbuild](https://twitter.com/astrodotbuild) in a Tweet!

---

[← Previous](391-yarn.md) | [Index](index.md) | [Next →](index.md)
