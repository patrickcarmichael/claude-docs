---
title: "Use Bun with Astro"
section: 202
---

# Use Bun with Astro

> Learn how to use Bun with your Astro site.

[Bun](https://bun.sh/) is an all-in-one JavaScript runtime & toolkit. See [Bun’s documentation](https://bun.sh/docs) for more information.

Caution

Using Bun with Astro may reveal rough edges. Some integrations may not work as expected. Consult [Bun’s official documentation for working with Astro](https://bun.sh/guides/ecosystem/astro) for details.

If you have any problems using Bun, please [open an Issue on GitHub with Bun directly](https://github.com/oven-sh/bun/issues/new/choose).

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Bun installed locally on your machine. See the [installation instructions](https://bun.sh/docs/installation) in Bun’s official documentation.

## Create a new Astro project with Bun

[Section titled “Create a new Astro project with Bun”](#create-a-new-astro-project-with-bun)

Create a new Astro project with Bun using the following `create-astro` command:

```bash
bun create astro my-astro-project-using-bun
```jsx
## Install dependencies

[Section titled “Install dependencies”](#install-dependencies)

If you skipped the “Install dependencies?” step during the CLI wizard, then be sure to install your dependencies before continuing.

```bash
bun install
```jsx
## Add Types

[Section titled “Add Types”](#add-types)

Bun publishes the [`@types/bun`](https://www.npmjs.com/package/@types/bun) package, containing the runtime types for Bun.

Install `@types/bun` using the following command:

```sh
bun add -d @types/bun
```jsx
## CLI installation flags

[Section titled “CLI installation flags”](#cli-installation-flags)

### Using integrations

[Section titled “Using integrations”](#using-integrations)

You can also use any of the official Astro integrations with the `astro add` command:

```bash
bun astro add react
```jsx
### Use a theme or starter template

[Section titled “Use a theme or starter template”](#use-a-theme-or-starter-template)

You can start a new Astro project based on an [official example](https://github.com/withastro/astro/tree/main/examples) or the main branch of any GitHub repository by passing a `--template` argument to the `create astro` command.

Run the following command in your terminal, substituting the official Astro starter template name, or the GitHub username and repository of the theme you want to use:

```bash

---

[← Previous](201-build-forms-with-api-routes.md) | [Index](index.md) | [Next →](index.md)
