---
title: "Example: Install integrations and frameworks together"
section: 184
---

# Example: Install integrations and frameworks together
npm install @astrojs/react react react-dom
```jsx
See [Astro’s integration guide](/en/guides/integrations-guide/) for instructions on adding framework renderers, CSS tools and other packages to Astro.

### Using Astro with Yarn 2+ (Berry)

[Section titled “Using Astro with Yarn 2+ (Berry)”](#using-astro-with-yarn-2-berry)

Yarn 2+, a.k.a. Berry, uses a technique called [Plug’n’Play (PnP)](https://yarnpkg.com/features/pnp) to store and manage Node modules, which can [cause problems](https://github.com/withastro/astro/issues/3450) while initializing a new Astro project using `create astro` or while working with Astro. A workaround is to set the [`nodeLinker` property](https://yarnpkg.com/configuration/yarnrc#nodeLinker) in `.yarnrc.yml` to `node-modules`:

.yarnrc.yml

```yaml
nodeLinker: "node-modules"
```jsx
### Adding dependencies to Astro in a monorepo

[Section titled “Adding dependencies to Astro in a monorepo”](#adding-dependencies-to-astro-in-a-monorepo)

When working with Astro in a monorepo setup, project dependencies should be added in each project’s own `package.json` file.

However, you may also want to use Astro in the root of the monorepo (e.g. [Nx projects recommend installing dependencies at the root](https://github.com/nrwl/nx/issues/3023#issuecomment-630558318)). In this case, manually add Astro-related dependencies (e.g. `@astrojs/vue`, `astro-component-lib`) to the `vite.ssr.noExternal` part of Astro’s config to ensure that these dependencies are properly installed and bundled:

astro.config.mjs

```js
import { defineConfig } from 'astro/config'
export default defineConfig({
  vite: {
    ssr: {
      noExternal: [
        '@astrojs/vue',
        'astro-component-lib',
      ]
    }
  }
})
```jsx
### Using `<head>` in a component

[Section titled “Using \<head> in a component”](#using-head-in-a-component)

In Astro, using a `<head>` tag works like any other HTML tag: it does not get moved to the top of the page or merged with the existing `<head>`. Because of this, you usually only want to include one `<head>` tag throughout a page. We recommend writing that single `<head>` and its contents in a [layout component](/en/basics/layouts/).

### An unexpected `<style>` is included

[Section titled “An unexpected \<style> is included”](#an-unexpected-style-is-included)

You may notice an imported component’s `<style>` tag included in your HTML source even if that component doesn’t appear in the final output. For example, this will occur with [conditionally rendered](/en/reference/astro-syntax/#dynamic-html) components that are not displayed.

Astro’s build process works on the module graph: once a component is included in the template, its `<style>` tag is processed, optimized, and bundled, whether it appears in the final output or not.

### Escaping special characters in Markdown

[Section titled “Escaping special characters in Markdown”](#escaping-special-characters-in-markdown)

Certain characters have a special meaning in Markdown. You may need to use a different syntax if you want to display them. To do this, you can use [HTML entities](https://developer.mozilla.org/en-US/docs/Glossary/Entity) for these characters instead.

For example, to prevent `<` being interpreted as the beginning of an HTML element, write `&lt;`.

## Creating minimal reproductions

[Section titled “Creating minimal reproductions”](#creating-minimal-reproductions)

When troubleshooting your code, it can be helpful to create a **minimal reproduction** of the issue that you can share. This is a smaller, simplified Astro project that demonstrates your issue. Having a working reproduction in a new project helps to confirm that this is a repeatable problem, and is not caused by something else in your personal environment or existing project.

Sharing a minimal reproduction is helpful when asking for help in our support threads and is often required when filing a bug report to Astro.

### Create a StackBlitz via [astro.new](https://astro.new/repro)

[Section titled “Create a StackBlitz via astro.new”](#create-a-stackblitz-via-astronew)

You can use [astro.new](https://astro.new/repro) to create a new Astro project with a single click. For minimal reproductions, we strongly recommend starting from the minimal (empty) example running in [StackBlitz](https://stackblitz.com), with as little extra code as possible.

StackBlitz will run this Astro project in the browser, outside of your local environment. It will also provide you with a shareable link so that any Astro maintainer or support squad member can view your minimal reproduction outside of their own local environment. This means that everyone is viewing the exact same project, with the same configuration and dependencies. This makes it easy for someone else to help troubleshoot your code. If the issue is reproducible, it allows you to verify that the issue lies within the Astro code itself and you can feel confident submitting a bug report.

Note that not every issue is reproducible in StackBlitz. For example, your issue might be dependent on a specific environment or package manager, or it may involve HTML Streaming, which isn’t supported in StackBlitz. In this case, create a new minimal (empty) Astro project using the CLI, reproduce the issue, and upload it to a GitHub repository. Instead of sharing a StackBlitz URL, provide a link to the GitHub repository of your minimal reproduction.

### Minimal code

[Section titled “Minimal code”](#minimal-code)

Once your empty project is set up, go through the steps to reproduce the issue. This can include adding packages, changing configuration, and writing code.

You should only add the minimum amount of code necessary to reproduce the issue. Do not reproduce other elements of your existing project, and remove all code that is not directly related to the issue.

### Create an issue

[Section titled “Create an issue”](#create-an-issue)

If your issue can be reproduced, then it is time to create an issue and file a bug report!

Go to the appropriate Astro repository on GitHub and open a new issue. Most repositories have an issue template that will ask questions or require information in order to submit. It’s important that you follow these templates because if you don’t provide the information we need, then we have to ask you for it… and no one is working on your issue!

Include the link to your minimal reproduction on StackBlitz (or GitHub repository, if necessary). Start with a description of the expected versus actual behavior to provide context for the issue. Then, include clear, step-by-step instructions on how to replicate the issue in an Astro project.

## Need more?

[Section titled “Need more?”](#need-more)

Come and chat with us on [Discord](https://astro.build/chat) and explain your issue in the `#support` forum channel. We’re always happy to help!

Visit the current [open Issues in Astro](https://github.com/withastro/astro/issues/) to see if you are encountering a known problem or file a bug report.

You can also visit [RFC Discussions](https://github.com/withastro/rfcs/discussions/) to see whether you’ve found a known limitation of Astro, and check to see whether there are current proposals related to your use case.

---

[← Previous](183-troubleshooting.md) | [Index](index.md) | [Next →](index.md)
