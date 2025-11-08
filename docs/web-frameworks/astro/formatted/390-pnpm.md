---
title: "pnpm"
section: 390
---

# pnpm
pnpm create astro@latest my-new-component-directory -- --template component
```jsx
## Creating a package

[Section titled “Creating a package”](#creating-a-package)

Prerequisites

Before diving in, it will help to have a basic understanding of:

* [Node Modules](https://docs.npmjs.com/creating-node-js-modules)
* [Package Manifest (`package.json`)](https://docs.npmjs.com/creating-a-package-json-file)
* [Workspaces](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#workspaces)

To create a new package, configure your development environment to use **workspaces** within your project. This will allow you to develop your component alongside a working copy of Astro.

* my-new-component-directory/

  * demo/

    * … for testing and demonstration

  * package.json

  * packages/

    * my-component/

      * index.js
      * package.json
      * … additional files used by the package

This example, named `my-project`, creates a project with a single package, named `my-component`, and a `demo/` directory for testing and demonstrating the component.

This is configured in the project root’s `package.json` file:

```json
{
  "name": "my-project",
  "workspaces": ["demo", "packages/*"]
}
```jsx
In this example, multiple packages can be developed together from the `packages` directory. These packages can also be referenced from `demo`, where you can install a working copy of Astro.

```shell
npm create astro@latest demo -- --template minimal

---

[← Previous](389-yarn.md) | [Index](index.md) | [Next →](index.md)
