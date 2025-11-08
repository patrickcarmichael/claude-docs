---
title: "Legacy v0.x Upgrade Guide"
section: 186
---

# Legacy v0.x Upgrade Guide

> Archived guide documenting changes between pre-v1 versions of Astro

This guide will help you upgrade through breaking changes in pre-v1 versions of Astro.

You can update your project’s version of Astro to the latest version using your package manager. If you’re using Astro integrations, you’ll also want to update those to the latest version.

* npm

  ```shell
  # updates the astro dependency:
  npm upgrade astro
  # or, to update all dependencies:
  npm upgrade
  ```jsx
* pnpm

  ```shell
  # updates the astro dependency:
  pnpm upgrade astro
  # or, to update all dependencies:
  pnpm upgrade
  ```jsx
* Yarn

  ```shell
  # updates the astro dependency:
  yarn upgrade astro
  # or, to update all dependencies:
  yarn upgrade
  ```jsx
Read the guide below for major highlights and instructions on how to handle breaking changes.

## Astro 1.0

[Section titled “Astro 1.0”](#astro-10)

Astro v1.0 introduces some changes that you should be aware of when migrating from v0.x and v1.0-beta releases. See below for more details.

### Updated: Vite 3

[Section titled “Updated: Vite 3”](#updated-vite-3)

Astro v1.0 has upgraded from Vite 2 to [Vite 3](https://vite.dev/). We’ve handled most of the upgrade for you inside of Astro; however, some subtle Vite behaviors may still change between versions. Refer to the official [Vite Migration Guide](https://vite.dev/guide/migration.html#general-changes) if you run into trouble.

### Deprecated: `Astro.canonicalURL`

[Section titled “Deprecated: Astro.canonicalURL”](#deprecated-astrocanonicalurl)

You can now use the new [`Astro.url`](/en/reference/api-reference/#url) helper to construct your own canonical URL from the current page/request URL.

```js
// Before:
const canonicalURL = Astro.canonicalURL;
// After:
const canonicalURL = new URL(Astro.url.pathname, Astro.site);
```jsx
### Changed: Scoped CSS specificity

[Section titled “Changed: Scoped CSS specificity”](#changed-scoped-css-specificity)

[Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) will now be preserved in scoped CSS styles. This change will cause most scoped styles to *happen* to take precedence over global styles. But, this behavior is no longer explicitly guaranteed.

Technically, this is accomplished using [the `:where()` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:where) instead of using classes directly in Astro’s CSS output.

Let’s use the following style block in an Astro component as an example:

```astro
<style>
  div { color: red; } /* 0-0-1 specificity */
</style>
```jsx
Previously, Astro would transform this into the following CSS, which has a specificity of `0-1-1` — a higher specificity than the source CSS:

```css
div.astro-XXXXXX { color: red; } /* 0-1-1 specificity */
```jsx
Now, Astro wraps the class selector with `:where()`, maintaining the authored specificity:

```css
div:where(.astro-XXXXXX) { color: red; } /* 0-0-1 specificity */
```jsx
The previous specificity increase made it hard to combine scoped styles in Astro with other CSS files or styling libraries (e.g. Tailwind, CSS Modules, Styled Components, Stitches). This change will allow Astro’s scoped styles to work consistently alongside them while still preserving the exclusive boundaries that prevent styles from applying outside the component.

Caution

When upgrading, please visually inspect your site output to make sure everything is styled as expected. If not, find your scoped style and increase the selector specificity manually to match the old behavior.

### Deprecated: Components and JSX in Markdown

[Section titled “Deprecated: Components and JSX in Markdown”](#deprecated-components-and-jsx-in-markdown)

Astro no longer supports components or JSX expressions in Markdown pages by default. For long-term support you should migrate to the [`@astrojs/mdx`](/en/guides/integrations-guide/mdx/) integration.

To make migrating easier, a new `legacy.astroFlavoredMarkdown` flag (removed in v2.0) can be used to re-enable previous Markdown features.

### Converting existing `.md` files to `.mdx`

[Section titled “Converting existing .md files to .mdx”](#converting-existing-md-files-to-mdx)

If you’re not familiar with MDX, here are some steps you can follow to quickly convert an existing “Astro Flavored Markdown” file to MDX. As you learn more about MDX, feel free to explore other ways of writing your pages!

1. Install the [`@astrojs/mdx`](/en/guides/integrations-guide/mdx/) integration.

2. Change your existing `.md` file extensions to `.mdx`

3. Remove any `setup:` properties from your frontmatter, and write any import statements below the frontmatter instead.

   src/pages/posts/my-post.mdx

   ```diff
   ---
   layout: '../../layouts/BaseLayout.astro'
   -setup: |
     import ReactCounter from '../../components/ReactCounter.jsx'
   title: 'Migrating to MDX'
   date: 2022-07-26
   tags: ["markdown", "mdx", "astro"]
   ---
   +import ReactCounter from '../../components/ReactCounter.jsx'


   # {frontmatter.title}


   Here is my counter component, working in MDX:


   <ReactCounter client:load />
   ```jsx
4. Update any `Astro.glob()` statements that currently return `.md` files so that they will now return your `.mdx` files.

   Caution

   The object returned when importing `.mdx` files (including using Astro.glob) differs from the object returned when importing `.md` files. However, `frontmatter`, `file`, and `url` work identically.

5. Update any use of the `<Content />` component to use the default export when importing MDX:

   src/pages/index.astro

   ```astro
   ---
   // Multiple imports with Astro.glob
   const mdxPosts = await Astro.glob('./posts/*.mdx');
   ---


   {mdxPosts.map(Post => <Post.default />)}
   ```jsx
   src/pages/index.astro

   ```astro
   ---
   // Import a single page
   import { default as About } from './about.mdx';
   ---


   <About />
   ```jsx
Tip

While you are transitioning to MDX, you may wish to enable the `legacy.astroFlavoredMarkdown` flag (removed in v2.0) and include both **`.md` and `.mdx`** files, so that your site continues to function normally even before all your files have been converted. Here is one way you can do that:

```astro
---
const mdPosts = await Astro.glob('../pages/posts/*.md');
const mdxPosts = await Astro.glob('../pages/posts/*.mdx');
const allPosts = [...mdxPosts, ...mdPosts];
---
```jsx
### `<Markdown />` Component Removed

[Section titled “\<Markdown /> Component Removed”](#markdown--component-removed)

Astro’s built-in `<Markdown />` component has been moved to a separate package. To continue using this component, you will now need to install `@astrojs/markdown-component` and update your imports accordingly. For more details, see [the `@astrojs/markdown` README](https://github.com/withastro/astro/tree/main/packages/markdown/component).

Tip

Astro now has support for [MDX](https://mdxjs.com/) through our [MDX integration](https://github.com/withastro/astro/tree/main/packages/integrations/mdx). MDX gives you the ability to include both Markdown and imported components in the same file. MDX can be good alternative for the `<Markdown />` component due to its large community and stable APIs.

## Migrate to v1.0.0-beta

[Section titled “Migrate to v1.0.0-beta”](#migrate-to-v100-beta)

On April 4, 2022 we released the Astro 1.0 Beta! 🎉

If you are coming from v0.25 or earlier, make sure you have read and followed the [v0.26 Migration Guide](#migrate-to-v026) below, which contained several major breaking changes.

The `v1.0.0-beta.0` release of Astro contained no breaking changes. Below are small changes that were introduced during the beta period.

### Changed: RSS Feeds

[Section titled “Changed: RSS Feeds”](#changed-rss-feeds)

RSS feeds should now be generated using the `@astrojs/rss` package, as described in our [RSS guide](/en/recipes/rss/).

## Migrate to v0.26

[Section titled “Migrate to v0.26”](#migrate-to-v026)

### New Configuration API

[Section titled “New Configuration API”](#new-configuration-api)

Our Configuration API has been redesigned to solve a few glaring points of confusion that had built up over the last year. Most of the configuration options have just been moved or renamed, which will hopefully be a quick update for most users. A few options have been refactored more heavily, and may require a few additional changes:

* `.buildOptions.site` has been replaced with `.site` (your deployed domain) and a new `.base` (your deployed subpath) option.
* `.markdownOptions` has been replaced with `.markdown`, a mostly similar config object with some small changes to simplify Markdown configuration.
* `.sitemap` has been moved into the [@astrojs/sitemap](https://www.npmjs.com/package/@astrojs/sitemap) integration.

If you run Astro with legacy configuration, you will see a warning with instructions on how to update. See our updated [Configuration Reference](/en/reference/configuration-reference/) for more information on upgrading.

Read [RFC0019](https://github.com/withastro/rfcs/blob/main/proposals/0019-config-finalization.md) for more background on these changes.

### New Markdown API

[Section titled “New Markdown API”](#new-markdown-api)

Astro v0.26 releases a brand new Markdown API for your content. This included three major user-facing changes:

* You can now `import`/`import()` markdown content directly using an ESM import.
* A new `Astro.glob()` API, for easier glob imports (especially for Markdown).
* **BREAKING CHANGE:** `Astro.fetchContent()` has been removed and replaced by `Astro.glob()`
* **BREAKING CHANGE:** Markdown objects have an updated interface.

```diff
// v0.25
-let allPosts = Astro.fetchContent('./posts/*.md');
// v0.26+
+let allPosts = await Astro.glob('./posts/*.md');
```jsx
When migrating, be careful about the new Markdown object interface. Frontmatter, for example, has been moved to the `.frontmatter` property, so references like `post.title` should change to `post.frontmatter.title`.

This should solve many issues for Markdown users, including some nice performance boosts for larger sites.

Read [RFC0017](https://github.com/withastro/rfcs/blob/main/proposals/0017-markdown-content-redesign.md) for more background on these changes.

### New Default Script Behavior

[Section titled “New Default Script Behavior”](#new-default-script-behavior)

`<script>` tags in Astro components are now built, bundled and optimized by default. This completes a long-term move to make our Astro component syntax more consistent, matching the default-optimized behavior our `<style>` tags have today.

This includes a few changes to be aware of:

* **BREAKING:** `<script hoist>` is the new default `<script>` behavior. The `hoist` attribute has been removed. To use the new default behaviour, make sure there are no other attributes on the `<script>` tag. For example, remove `type="module"` if you were using it before.
* New `<script is:inline>` directive, to revert a `<script>` tag to previous default behavior (unbuilt, unbundled, untouched by Astro).
* New `<style is:inline>` directive, to leave a style tag inline in the page template (similar to previous `<script>` behavior).
* New `<style is:global>` directive to replace `<style global>` in a future release.

```diff
// v0.25
<script hoist type="module">
// v0.26+
<script>
```jsx
See how to use [client-side scripts](/en/guides/client-side-scripts/) in Astro for full details.

Read [RFC0016](https://github.com/withastro/rfcs/blob/main/proposals/0016-style-script-defaults.md) for more background on these changes.

### Updated `Astro.request` API

[Section titled “Updated Astro.request API”](#updated-astrorequest-api)

`Astro.request` has been changed from our custom object to a standard `Request` object. This is part of a project to use more web standard APIs, especially where SSR is concerned.

This includes a few changes to be aware of:

* Change `Astro.request` to become a [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object.
* Move `Astro.request.params` to `Astro.params`.
* Move `Astro.request.canonicalURL` to `Astro.canonicalURL`.

Read [RFC0018](https://github.com/withastro/rfcs/blob/main/proposals/0018-astro-request.md) for more background on these changes.

### Other Changes

[Section titled “Other Changes”](#other-changes)

* Improve `Astro.slots` API to support passing arguments to function-based slots. This allows for more ergonomic utility components that accept a callback function as a child.
* Update CLI output formatting, especially around error reporting.
* Update `@astrojs/compiler`, fixing some bugs related to RegExp usage in frontmatter

## Migrate to v0.25

[Section titled “Migrate to v0.25”](#migrate-to-v025)

### Astro Integrations

[Section titled “Astro Integrations”](#astro-integrations)

The `renderers` config has been replaced by a new, official integration system! This unlocks some really exciting new features for Astro. You can read our [Using Integrations](/en/guides/integrations-guide/) guide for more details on how to use this new system.

Integrations replace our original `renderers` concept, and come with a few breaking changes and new defaults for existing users. These changes are covered below.

#### Removed: Built-in Framework Support

[Section titled “Removed: Built-in Framework Support”](#removed-built-in-framework-support)

Previously, React, Preact, Svelte, and Vue were all included with Astro by default. Starting in v0.25.0, Astro no longer comes with any built-in renderers. If you did not have a `renderers` configuration entry already defined for your project, you will now need to install those frameworks yourself.

Read our [step-by-step walkthrough](/en/guides/integrations-guide/) to learn how to add a new Astro integration for the framework(s) that you currently use.

#### Deprecated: Renderers

[Section titled “Deprecated: Renderers”](#deprecated-renderers)

Note

Read this section if you have custom “renderers” already defined in your configuration file.

The new integration system replaces the previous `renderers` system, including the published `@astrojs/renderer-*` packages on npm. Going forward, `@astrojs/renderer-react` becomes `@astrojs/react`, `@astrojs/renderer-vue` becomes `@astrojs/vue`, and so on.

**To migrate:** update Astro to `v0.25.0` and then run `astro dev` or `astro build` with your old configuration file containing the outdated `"renderers"` config. You will immediately see a notice telling you the exact changes you need to make to your `astro.config.mjs` file, based on your current config. You can also update your packages yourself, using the table below.

For a deeper walkthrough, read our [step-by-step guide](/en/guides/integrations-guide/) to learn how to replace existing renderers with a new Astro framework integration.

```diff

---

[← Previous](185-typescript.md) | [Index](index.md) | [Next →](index.md)
