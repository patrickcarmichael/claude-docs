---
title: "Migrating from Gatsby"
section: 162
---

# Migrating from Gatsby

> Tips for migrating an existing Gatsby project to Astro

Here are some key concepts and migration strategies to help you get started. Use the rest of our docs and our [Discord community](https://astro.build/chat) to keep going!

## Key Similarities between Gatsby and Astro

[Section titled “Key Similarities between Gatsby and Astro”](#key-similarities-between-gatsby-and-astro)

Gatsby and Astro share some similarities that will help you migrate your project:

* The [syntax of `.astro` files is similar to JSX](/en/reference/astro-syntax/#jsx-like-expressions). Writing Astro should feel familiar.

* Astro has built-in support for [Markdown](/en/guides/markdown-content/) and an integration for using MDX files. Also, you can configure and continue to use many of your existing Markdown plugins.

* Astro also has an [official integration for using React components](/en/guides/integrations-guide/react/). Note that in Astro, React files **must** have a `.jsx` or `.tsx` extension.

* Astro has support for [installing NPM packages](/en/guides/imports/#npm-packages), including React libraries. Many of your existing dependencies will work in Astro.

* Like Gatsby, Astro projects can be SSG or [SSR with page-level prerendering](/en/guides/on-demand-rendering/).

## Key Differences between Gatsby and Astro

[Section titled “Key Differences between Gatsby and Astro”](#key-differences-between-gatsby-and-astro)

When you rebuild your Gatsby site in Astro, you will notice some important differences:

* Gatsby projects are React single-page apps and use `index.js` as your project’s root. Astro projects are multi-page sites, and `index.astro` is your home page.

* [Astro components](/en/basics/astro-components/) are not written as exported functions that return page templating. Instead, you’ll split your code into a “code fence” for your JavaScript and a body exclusively for the HTML you generate.

* [Local file data](/en/guides/imports/): Gatsby uses GraphQL to retrieve data from your project files. Astro uses ESM imports and top-level await functions (e.g. [`import.meta.glob()`](/en/guides/imports/#importmetaglob), [`getCollection()`](/en/guides/content-collections/#querying-collections)) to import data from your project files. You can manually add GraphQL to your Astro project but it is not included by default.

## Convert your Gatsby Project

[Section titled “Convert your Gatsby Project”](#convert-your-gatsby-project)

Each project migration will look different, but there are some common actions you will perform when converting from Gatsby to Astro.

### Create a new Astro project

[Section titled “Create a new Astro project”](#create-a-new-astro-project)

Use the `create astro` command for your package manager to launch Astro’s CLI wizard or choose a community theme from the [Astro Theme Showcase](https://astro.build/themes).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters (e.g. `docs`, `blog`, `portfolio`). Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  # launch the Astro CLI Wizard
  npm create astro@latest


  # create a new project with an official example
  npm create astro@latest -- --template <example-name>
  ```jsx
* pnpm

  ```shell
  # launch the Astro CLI Wizard
  pnpm create astro@latest


  # create a new project with an official example
  pnpm create astro@latest --template <example-name>
  ```jsx
* Yarn

  ```shell
  # launch the Astro CLI Wizard
  yarn create astro@latest


  # create a new project with an official example
  yarn create astro@latest --template <example-name>
  ```jsx
Then, copy your existing Gatsby project files over to your new Astro project into a separate folder outside of `src`.

Tip

Visit <https://astro.new> for the full list of official starter templates, and links for opening a new project in IDX, StackBlitz, CodeSandbox, or Gitpod.

### Install integrations (optional)

[Section titled “Install integrations (optional)”](#install-integrations-optional)

You may find it useful to install some of [Astro’s optional integrations](/en/guides/integrations-guide/) to use while converting your Gatsby project to Astro:

* **@astrojs/react**: to reuse some existing React UI components in your new Astro site or keep writing with React components.

* **@astrojs/mdx**: to bring existing MDX files from your Gatsby project, or to use MDX in your new Astro site.

### Put your code in `src`

[Section titled “Put your code in src”](#put-your-code-in-src)

Following [Astro’s project structure](/en/basics/project-structure/):

1. **Delete** Gatsby’s `public/` folder.

   Gatsby uses the `public/` directory for its build output, so you can safely discard this folder. You will no longer need a built version of your Gatsby site. (Astro uses `dist/` by default for the build output.)

2. **Rename** Gatsby’s `static/` folder to `public/`, and use it as Astro’s `public/` folder.

   Astro uses a folder called `public/` for static assets. You can alternatively copy the contents of `static/` into your existing Astro `public/` folder.

3. **Copy or Move** Gatsby’s other files and folders (e.g. `components`, `pages`, etc.) as needed into your Astro `src/` folder as you rebuild your site, following [Astro’s project structure](/en/basics/project-structure/).

   Astro’s `src/pages/` folder is a special folder used for file-based routing to create your site’s pages and posts from `.astro`, `.md` and `.mdx` files. You will not have to configure any routing behavior for your Astro, Markdown, and MDX files.

   All other folders are optional, and you can organize the contents of your `src/` folder any way you like. Other common folders in Astro projects include `src/layouts/`, `src/components`, `src/styles`, and `src/scripts`.

### Tips: Convert JSX files to `.astro` files

[Section titled “Tips: Convert JSX files to .astro files”](#tips-convert-jsx-files-to-astro-files)

Here are some tips for converting a Gatsby `.js` component into a `.astro` component:

1. Use only the `return()` of the existing Gatsby component function as your HTML template.

2. Change any [Gatsby or JSX syntax to Astro syntax](#reference-convert-to-astro-syntax) or to HTML web standards. This includes `<Link to="">`, `{children}`, and `className`, for example.

3. Move any necessary JavaScript, including import statements, into a [“code fence” (`---`)](/en/basics/astro-components/#the-component-script). Note: JavaScript to [conditionally render content](/en/reference/astro-syntax/#dynamic-html) is often written inside the HTML template directly in Astro.

4. Use [`Astro.props`](/en/reference/api-reference/#props) to access any additional props that were previously passed to your Gatsby function.

5. Decide whether any imported components also need to be converted to Astro. With the official React integration installed, you can [use existing React components in your Astro files](/en/guides/framework-components/). But, you may want to convert them to `.astro` components, especially if they do not need to be interactive!

6. Remove any GraphQL queries. Instead, use import and [`import.meta.glob()`](/en/guides/imports/#importmetaglob) statements to query your local files.

See [an example from Gatsby’s Blog starter template converted step-by-step](#guided-example-gatsby-layout-to-astro)

#### Compare: `.jsx` vs `.astro`

[Section titled “Compare: .jsx vs .astro”](#compare-jsx-vs-astro)

Compare the following Gatsby component and a corresponding Astro component:

* JSX

  component.jsx

  ```jsx
  import * as React from "react"
  import { useStaticQuery, graphql } from "gatsby"
  import Header from "./header"
  import Footer from "./footer"
  import "./layout.css"


  const Component = ({ message, children }) => {
    const data = useStaticQuery(graphql`
      query SiteTitleQuery {
        site {
          siteMetadata {
            title
          }
        }
      }
    `)
    return (
      <>
        <Header siteTitle={data.site.siteMetadata.title} />
        <div style={{ margin: `0`, maxWidth: `960`}}>{message}</div>
        <main>{children}</main>
        <Footer siteTitle={data.site.siteMetadata} />
      </>
    )
  }


  export default Component
  ```jsx
* Astro

  component.astro

  ```astro
  ---
  import Header from "./Header.astro"
  import Footer from "./Footer.astro"
  import "../styles/stylesheet.css"
  import { site } from "../data/siteMetaData.js"
  const { message } = Astro.props
  ---
  <Header siteTitle={site.title} />
    <div style="margin: 0; max-width: 960;">{message}</div>
    <main>
      <slot />
    </main>
  <Footer siteTitle={site.title} />
  ```jsx
### Migrating Layout Files

[Section titled “Migrating Layout Files”](#migrating-layout-files)

You may find it helpful to start by converting your Gatsby layouts and templates into [Astro layout components](/en/basics/layouts/).

Each Astro page explicitly requires `<html>`, `<head>`, and `<body>` tags to be present, so it is common to reuse a layout file across pages. Astro uses a [`<slot />`](/en/basics/astro-components/#slots) instead of React’s `{children}` prop for page content, with no import statement required. Your Gatsby `layout.js` and templates will not include these.

Note the standard HTML templating, and direct access to `<head>`:

src/layouts/Layout.astro

```astro
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <title>Astro</title>
  </head>
  <body>
    <!-- Wrap the slot element with your existing layout templating -->
    <slot />
  </body>
</html>
```jsx
You may also wish to reuse code from Gatsby’s `src/components/seo.js` to include additional site metadata. Notice that Astro uses neither `<Helmet>` nor `<Header>` but instead creates `<head>` directly. You may import and use components, even within `<head>`, to separate and organize your page content.

### Migrating Pages and Posts

[Section titled “Migrating Pages and Posts”](#migrating-pages-and-posts)

In Gatsby, your [pages and posts](/en/basics/astro-pages/) may exist in `src/pages/` or outside of `src` in another folder, like `content`. In Astro, all your page content must live within `src/` unless you are using [content collections](/en/guides/content-collections/).

#### React Pages

[Section titled “React Pages”](#react-pages)

Your existing Gatsby JSX (`.js`) pages will need to be [converted from JSX files to `.astro` pages](#tips-convert-jsx-files-to-astro-files). You cannot use an existing JSX page file in Astro.

These [`.astro` pages](/en/basics/astro-pages/) must be located within `src/pages/` and will have page routes generated automatically based on their file path.

#### Markdown and MDX pages

[Section titled “Markdown and MDX pages”](#markdown-and-mdx-pages)

Astro has built-in support for Markdown and an optional integration for MDX files. Your existing [Markdown and MDX files](/en/guides/markdown-content/) can be reused but may require some adjustments to their frontmatter, such as adding [Astro’s special `layout` frontmatter property](/en/basics/layouts/#markdown-layouts). They can also be placed within `src/pages/` to take advantage of automatic file-based routing.

Alternatively, you can use [content collections](/en/guides/content-collections/) in Astro to store and manage your content. You will retrieve the content yourself and [generate those pages dynamically](/en/guides/content-collections/#generating-routes-from-content).

### Migrating Tests

[Section titled “Migrating Tests”](#migrating-tests)

As Astro outputs raw HTML, it is possible to write end-to-end tests using the output of the build step. Any end-to-end tests written previously might work out-of-the-box if you have been able to match the markup of the older Gatsby site. Testing libraries such as Jest and React Testing Library can be imported and used in Astro to test your React components.

See Astro’s [testing guide](/en/guides/testing/) for more.

### Repurpose config files

[Section titled “Repurpose config files”](#repurpose-config-files)

Gatsby has several top-level configuration files that also include site and page metadata and are used for routing. You will not use any of these `gatsby-*.js` files in your Astro project, but there may be some content that you can reuse as you build your Astro project:

* `gatsby-config.js`: Move your `siteMetadata: {}` into `src/data/siteMetadata.js` (or `siteMetadata.json`) to import data about your site (title, description, social accounts, etc.) into page layouts.

* `gatsby-browser.js`: Consider adding anything used here directly into your [main layout](#migrating-layout-files)’s `<head>` tag.

* `gatsby-node.js`: You will not need to create your own nodes in Astro, but viewing the schema in this file may help you with defining types in your Astro project.

* `gatsby-ssr.js`: If you choose to use SSR in Astro, you will [add and configure the SSR adapter](/en/guides/on-demand-rendering/) of your choice directly in `astro.config.mjs`.

## Reference: Convert to Astro Syntax

[Section titled “Reference: Convert to Astro Syntax”](#reference-convert-to-astro-syntax)

The following are some examples of Gatsby-specific syntax that you will need to convert to Astro. See more [differences between Astro and JSX](/en/reference/astro-syntax/#differences-between-astro-and-jsx) in the guide to writing Astro components.

### Gatsby Links to Astro

[Section titled “Gatsby Links to Astro”](#gatsby-links-to-astro)

Convert any Gatsby `<Link to="">`, `<NavLink>` etc. components to HTML `<a href="">` tags.

```diff
-<Link to="/blog">Blog</Link>
<a href="/blog">Blog</a>
```jsx
Astro does not use any special component for links, although you are welcome to build your own `<Link>` component. You can then import and use this `<Link>` just as you would any other component.

src/components/Link.astro

```astro
---
const { to } = Astro.props
---
<a href={to}><slot /></a>
```jsx
### Gatsby Imports to Astro

[Section titled “Gatsby Imports to Astro”](#gatsby-imports-to-astro)

If necessary, update any [file imports](/en/guides/imports/) to reference relative file paths exactly. This can be done using [import aliases](/en/guides/typescript/#import-aliases), or by writing out a relative path in full.

Note that `.astro` and several other file types must be imported with their full file extension.

src/pages/authors/Fred.astro

```astro
---
import Card from `../../components/Card.astro`;
---
<Card />
```jsx
### Gatsby Children Props to Astro

[Section titled “Gatsby Children Props to Astro”](#gatsby-children-props-to-astro)

Convert any instances of `{children}` to an Astro `<slot />`. Astro does not need to receive `{children}` as a function prop and will automatically render child content in a `<slot />`.

src/components/MyComponent

```diff
---
---
-export default function MyComponent(props) {
    -return (
      <div>
        -{props.children}
      </div>
-    );
-}


<div>
  <slot />
</div>
```jsx
React components that pass multiple sets of children can be migrated to an Astro component using [named slots](/en/basics/astro-components/#named-slots).

See more about [specific `<slot />` usage in Astro](/en/basics/astro-components/#slots).

### Gatsby Styling to Astro

[Section titled “Gatsby Styling to Astro”](#gatsby-styling-to-astro)

You may need to replace any [CSS-in-JS libraries](https://github.com/withastro/astro/issues/4432) (e.g. styled-components) with other available CSS options in Astro.

If necessary, convert any inline style objects (`style={{ fontWeight: "bold" }}`) to inline HTML style attributes (`style="font-weight:bold;"`). Or, use an [Astro `<style>` tag](/en/guides/styling/#styling-in-astro) for scoped CSS styles.

src/components/Card.astro

```diff
<div style={{backgroundColor: `#f4f4f4`, padding: `1em`}}>{message}</div>
<div style="background-color: #f4f4f4; padding: 1em;">{message}</div>
```jsx
Tailwind is supported after installing the [Tailwind Vite plugin](/en/guides/styling/#tailwind). No changes to your existing Tailwind code are required!

Global styling is achieved in Gatsby using CSS imports in `gatsby-browser.js`. In Astro, you will import `.css` files directly into a main layout component to achieve global styles.

See more about [Styling in Astro](/en/guides/styling/).

### Gatsby Image Plugin to Astro

[Section titled “Gatsby Image Plugin to Astro”](#gatsby-image-plugin-to-astro)

Convert Gatsby’s `<StaticImage />` and `<GatsbyImage />` components to [Astro’s own image integration components](/en/guides/images/), or to a [standard HTML `<img>` / JSX `<img />`](/en/guides/images/#images-in-ui-framework-components) tag as appropriate in your React components.

src/pages/index.astro

```astro
---
import { Image } from 'astro:assets';
import rocket from '../assets/rocket.png';
---
<Image src={rocket} alt="A rocketship in space." />
<img src={rocket.src} alt="A rocketship in space.">
```jsx
Astro’s `<Image />` component works in `.astro` and `.mdx` files only. See a [full list of its component attributes](/en/reference/modules/astro-assets/#image-properties) and note that several will differ from Gatsby’s attributes.

To continue using [images in Markdown (`.md`) files](/en/guides/images/#images-in-markdown-files) using standard Markdown syntax (`![]()`), you may need to update the link. Using the HTML `<img>` tag directly is not supported in `.md` files for local images, and must be converted to Markdown syntax.

src/pages/post-1.md

```md

---

[← Previous](161-migrating-from-eleventy.md) | [Index](index.md) | [Next →](index.md)
