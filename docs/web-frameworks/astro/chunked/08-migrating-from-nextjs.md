**Navigation:** [← Previous](./07-astrojsvercel.md) | [Index](./index.md) | [Next →](./09-testing.md)

---

# Migrating from Next.js

> Tips for migrating an existing Next.js project to Astro

Here are some key concepts and migration strategies to help you get started. Use the rest of our docs and our [Discord community](https://astro.build/chat) to keep going!

## Key Similarities between Next.js and Astro

[Section titled “Key Similarities between Next.js and Astro”](#key-similarities-between-nextjs-and-astro)

Next.js and Astro share some similarities that will help you migrate your project:

* The [syntax of `.astro` files is similar to JSX](/en/reference/astro-syntax/#differences-between-astro-and-jsx). Writing Astro should feel familiar.
* Astro projects can also be SSG or [SSR with page-level prerendering](/en/guides/on-demand-rendering/).
* Astro uses file-based routing, and [allows specially named pages to create dynamic routes](/en/guides/routing/#dynamic-routes).
* Astro is [component-based](/en/basics/astro-components/), and your markup structure will be similar before and after your migration.
* Astro has [official integrations for React, Preact, and Solid](/en/guides/integrations-guide/react/) so you can use your existing JSX components. Note that in Astro, these files **must** have a `.jsx` or `.tsx` extension.
* Astro has support for [installing NPM packages](/en/guides/imports/#npm-packages), including React libraries. Many of your existing dependencies will work in Astro.

## Key Differences between Next.js and Astro

[Section titled “Key Differences between Next.js and Astro”](#key-differences-between-nextjs-and-astro)

When you rebuild your Next.js site in Astro, you will notice some important differences:

* Next.js is a React single-page app, and uses `index.js` as your project’s root. Astro is a multi-page site, and `index.astro` is your home page.

* [`.astro` components](/en/basics/astro-components/) are not written as exported functions that return page templating. Instead, you’ll split your code into a “code fence” for your JavaScript and a body exclusively for the HTML you generate.

* [content-driven](/en/concepts/why-astro/#content-driven): Astro was designed to showcase your content and to allow you to opt-in to interactivity only as needed. An existing Next.js app might be built for high client-side interactivity and may require advanced Astro techniques to include items that are more challenging to replicate using `.astro` components, such as dashboards.

## Convert your Next.js Project

[Section titled “Convert your Next.js Project”](#convert-your-nextjs-project)

Each project migration will look different, but there are some common actions you will perform when converting from Next.js to Astro.

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
  ```

* pnpm

  ```shell
  # launch the Astro CLI Wizard
  pnpm create astro@latest


  # create a new project with an official example
  pnpm create astro@latest --template <example-name>
  ```

* Yarn

  ```shell
  # launch the Astro CLI Wizard
  yarn create astro@latest


  # create a new project with an official example
  yarn create astro@latest --template <example-name>
  ```

Then, copy your existing Next project files over to your new Astro project in a separate folder outside of `src`.

Tip

Visit <https://astro.new> for the full list of official starter templates, and links for opening a new project in IDX, StackBlitz, CodeSandbox, or Gitpod.

### Install integrations (optional)

[Section titled “Install integrations (optional)”](#install-integrations-optional)

You may find it useful to install some of [Astro’s optional integrations](/en/guides/integrations-guide/) to use while converting your Next project to Astro:

* **@astrojs/react**: to reuse some existing React UI components in your new Astro site, or keep writing with React components.

* **@astrojs/mdx**: to bring existing MDX files from your Next project, or to use MDX in your new Astro site.

### Put your source code in `src`

[Section titled “Put your source code in src”](#put-your-source-code-in-src)

Following [Astro’s project structure](/en/basics/project-structure/):

1. **Keep** Next’s `public/` folder untouched.

   Astro uses the `public/` directory for static assets, just like Next. There is no change needed to this folder, nor its contents.

2. **Copy or Move** Next’s other files and folders (e.g. `pages`, `styles` etc.) into Astro’s `src/` folder as you rebuild your site, following [Astro’s project structure](/en/basics/project-structure/).

   Like Next, Astro’s `src/pages/` folder is a special folder used for file-based routing. All other folders are optional, and you can organize the contents of your `src/` folder any way you like. Other common folders in Astro projects include `src/layouts/`, `src/components`, `src/styles`, `src/scripts`.

### The Astro config file

[Section titled “The Astro config file”](#the-astro-config-file)

Astro has a configuration file at the root of your project called [`astro.config.mjs`](/en/guides/configuring-astro/). This is used only for configuring your Astro project and any installed integrations, including [SSR adapters](/en/guides/deploy/).

### Tips: Convert JSX files to `.astro` files

[Section titled “Tips: Convert JSX files to .astro files”](#tips-convert-jsx-files-to-astro-files)

Here are some tips for converting a Next `.js` component into a `.astro` component:

1. Use the returned JSX of the existing Next.js component function as the basis for your HTML template.

2. Change any [Next or JSX syntax to Astro](#reference-convert-nextjs-syntax-to-astro) or to HTML web standards. This includes `<Link>`, `<Script>`, `{children}`, and `className`, for example.

3. Move any necessary JavaScript, including import statements, into a [“code fence” (`---`)](/en/basics/astro-components/#the-component-script). Note: JavaScript to [conditionally render content](/en/reference/astro-syntax/#dynamic-html) is often written inside the HTML template directly in Astro.

4. Use [`Astro.props`](/en/reference/api-reference/#props) to access any additional props that were previously passed to your Next function.

5. Decide whether any imported components also need to be converted to Astro. With the official integration installed, you can [use existing React components in your Astro file](/en/guides/framework-components/). But, you may want to convert them to `.astro` components, especially if they do not need to be interactive!

6. Replace `getStaticProps()` with import statements or [`import.meta.glob()`](/en/guides/imports/#importmetaglob) to query your local files. Use `fetch()` to fetch external data.

See [an example of a Next `.js` file converted step-by-step](#guided-example-next-data-fetching-to-astro).

#### Compare: JSX vs Astro

[Section titled “Compare: JSX vs Astro”](#compare-jsx-vs-astro)

Compare the following Next component and a corresponding Astro component:

* JSX

  StarCount.jsx

  ```jsx
  import Header from "./header";
  import Footer from "./footer";
  import "./layout.css";


  export async function getStaticProps() {
      const res = await fetch("https://api.github.com/repos/withastro/astro");
      const json = await res.json();
      return {
          props: { message: json.message, stars: json.stargazers_count || 0 },
      }
  }


  const Component = ({ stars, message }) => {


      return (
          <>
              <Header />
              <p style={{
                  backgroundColor: `#f4f4f4`,
                  padding: `1em 1.5em`,
                  textAlign: `center`,
                  marginBottom: `1em`
              }}>Astro has {stars} 🧑‍🚀</p>
              <Footer />
          </>
      )
  }


  export default Component;
  ```

* Astro

  StarCount.astro

  ```astro
  ---
  import Header from "./header";
  import Footer from "./footer";
  import "./layout.css";


  const res = await fetch("https://api.github.com/repos/withastro/astro");
  const json = await res.json();
  const message = json.message;
  const stars = json.stargazers_count || 0;
  ---
  <Header />
  <p class="banner">Astro has {stars} 🧑‍🚀</p>
  <Footer />


  <style>
    .banner {
      background-color: #f4f4f4;
      padding: 1em 1.5em;
      text-align: center;
      margin-bottom: 1em;
    }
  <style>
  ```

### Migrating Layout Files

[Section titled “Migrating Layout Files”](#migrating-layout-files)

You may find it helpful to start by converting your Next.js layouts and templates into [Astro layout components](/en/basics/layouts/).

Next has two different methods for creating layout files, each of which handles layouts differently than Astro:

* The `pages` directory

* [The `/app` directory](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts#layouts)

Each Astro page explicitly requires `<html>`, `<head>`, and `<body>` tags to be present, so it is common to reuse a layout file across pages. Astro uses a [`<slot />`](/en/basics/astro-components/#slots) for page content, with no import statement required. Note the standard HTML templating, and direct access to `<head>`:

src/layouts/Layout.astro

```astro
---
---
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <!-- Wrap the slot element with your existing layout templating -->
    <slot />
  </body>
</html>
```

#### Migrating from Next.js’ `pages` directory

[Section titled “Migrating from Next.js’ pages directory”](#migrating-from-nextjs-pages-directory)

Your Next project may have a `pages/_document.jsx` file that imports React components to customize your app’s `<head>`:

pages/\_document.jsx

```jsx
import Document, { Html, Head, Main, NextScript } from "next/document";


export default class MyDocument extends Document {
  render() {
    return (
      <Html lang="en">
        <Head>
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
```

1. Make a new Astro layout file using only the returned JSX.

2. Replace any React components with `<html>`, `<head>`, `<slot>`, and other HTML standard tags.

   src/layouts/Document.astro

   ```astro
   <html lang="en">
     <head>
         <link rel="icon" href="/favicon.ico" />
     </head>
     <body>
       <slot/>
     </body>
   </html>
   ```

#### Migrating from Next.js’ `/app` directory

[Section titled “Migrating from Next.js’ /app directory”](#migrating-from-nextjs-app-directory)

Next.js’ `app/` directory layout files are created with two files: a `layout.jsx` file to customize the `<html>` and `<body>` contents, and a `head.jsx` file to customize the `<head>` element contents.

app/layout.jsx

```jsx
export default function Layout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

app/head.jsx

```jsx
export default function Head() {
  return (
    <>
      <title>My Page</title>
    </>
  );
}
```

1. Make a new Astro layout file using only the returned JSX.

2. Replace both these files with a single Astro layout file that contains a page shell (`<html>`, `<head>`, and `<body>` tags) and a `<slot/>` instead of React’s `{children}` prop:

   src/layouts/Layout.astro

   ```astro
   <html lang="en">
     <head>
         <title>My Page</title>
     </head>
     <body>
       <slot/>
     </body>
   </html>
   ```

### Migrating Pages and Posts

[Section titled “Migrating Pages and Posts”](#migrating-pages-and-posts)

In Next.js, your posts either live in `/pages` or `/app/routeName/page.jsx`.

In Astro, all your page content must live within `src/` unless you are using [content collections](/en/guides/content-collections/).

#### React pages

[Section titled “React pages”](#react-pages)

Your existing Next JSX (`.js`) pages will need to be [converted from JSX files to `.astro` pages](#tips-convert-jsx-files-to-astro-files). You cannot use an existing JSX page file in Astro.

These [`.astro` pages](/en/basics/astro-pages/) must be located within `src/pages/` and will have page routes generated automatically based on their file path.

#### Markdown and MDX pages

[Section titled “Markdown and MDX pages”](#markdown-and-mdx-pages)

Astro has built-in support for Markdown and an optional integration for MDX files. You can reuse any existing [Markdown and MDX files](/en/guides/markdown-content/), but they may require some adjustments to their frontmatter, such as adding [Astro’s special `layout` frontmatter property](/en/basics/layouts/#markdown-layouts). You will no longer need to manually create pages for each Markdown-generated route. These files can be placed within `src/pages/` to take advantage of automatic file-based routing.

Alternatively, you can use [content collections](/en/guides/content-collections/) in Astro to store and manage your content. You will retrieve the content yourself and [generate those pages dynamically](/en/guides/content-collections/#generating-routes-from-content).

### Migrating Tests

[Section titled “Migrating Tests”](#migrating-tests)

As Astro outputs raw HTML, it is possible to write end-to-end tests using the output of the build step. Any end-to-end tests written previously might work out-of-the-box if you have been able to match the markup of your Next site. Testing libraries such as Jest and React Testing Library can be imported and used in Astro to test your React components.

See Astro’s [testing guide](/en/guides/testing/) for more.

## Reference: Convert Next.js Syntax to Astro

[Section titled “Reference: Convert Next.js Syntax to Astro”](#reference-convert-nextjs-syntax-to-astro)

### Next Links to Astro

[Section titled “Next Links to Astro”](#next-links-to-astro)

Convert any Next `<Link to="">`, `<NavLink>` etc. components to HTML `<a href="">` tags.

```diff
-<Link to="/blog">Blog</Link>
<a href="/blog">Blog</a>
```

Astro does not use any special component for links, although you are welcome to build your own `<Link>` component. You can then import and use this `<Link>` just as you would any other component.

src/components/Link.astro

```astro
---
const { to } = Astro.props;
---
<a href={to}><slot /></a>
```

### Next Imports to Astro

[Section titled “Next Imports to Astro”](#next-imports-to-astro)

Update any [file imports](/en/guides/imports/) to reference relative file paths exactly. This can be done using [import aliases](/en/guides/typescript/#import-aliases), or by writing out a relative path in full.

Note that `.astro` and several other file types must be imported with their full file extension.

src/pages/authors/Fred.astro

```astro
---
import Card from "../../components/Card.astro";
---
<Card />
```

### Next Children Props to Astro

[Section titled “Next Children Props to Astro”](#next-children-props-to-astro)

Convert any instances of `{children}` to an Astro `<slot />`. Astro does not need to receive `{children}` as a function prop and will automatically render child content in a `<slot />`.

src/components/MyComponent.astro

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
```

React components that pass multiple sets of children can be migrated to an Astro component using [named slots](/en/basics/astro-components/#named-slots).

See more about [specific `<slot />` usage in Astro](/en/basics/astro-components/#slots).

### Next Data Fetching to Astro

[Section titled “Next Data Fetching to Astro”](#next-data-fetching-to-astro)

Convert any instances of `getStaticProps()` to either `import.meta.glob()` or `getCollection()`/`getEntry()` in order to access data from other files in your project source. To [fetch remote data](/en/guides/data-fetching/), use `fetch()`.

These data requests are made in the frontmatter of the Astro component and use top-level await.

src/pages/index.astro

```astro
---
import { getCollection } from 'astro:content';


// Get all `src/content/blog/` entries
const allBlogPosts = await getCollection('blog');


// Get all `src/pages/posts/` entries
const allPosts = Object.values(import.meta.glob('../pages/posts/*.md', { eager: true }));


const response = await fetch('https://randomuser.me/api/');
const data = await response.json();
const randomUser = data.results[0];
---
```

See more about local files imports with [`import.meta.glob()`](/en/guides/imports/#importmetaglob), [querying using the Collections API](/en/guides/content-collections/#querying-collections) or [fetching remote data](/en/guides/data-fetching/).

### Next Styling to Astro

[Section titled “Next Styling to Astro”](#next-styling-to-astro)

You may need to replace any [CSS-in-JS libraries](https://github.com/withastro/astro/issues/4432) (e.g. styled-components) with other available CSS options in Astro.

If necessary, convert any inline style objects (`style={{ fontWeight: "bold" }}`) to inline HTML style attributes (`style="font-weight:bold;"`). Or, use an [Astro `<style>` tag](/en/guides/styling/#styling-in-astro) for scoped CSS styles.

src/components/Card.astro

```diff
<div style={{backgroundColor: `#f4f4f4`, padding: `1em`}}>{message}</div>
<div style="background-color: #f4f4f4; padding: 1em;">{message}</div>
```

Tailwind is supported after installing the [Tailwind Vite plugin](/en/guides/styling/#tailwind). No changes to your existing Tailwind code are required!

See more about [Styling in Astro](/en/guides/styling/).

### Next Image Plugin to Astro

[Section titled “Next Image Plugin to Astro”](#next-image-plugin-to-astro)

Convert any Next `<Image />` components to [Astro’s own image component](/en/guides/images/) in `.astro` or `.mdx` files, or to a [standard HTML `<img>` / JSX `<img />`](/en/guides/images/#images-in-ui-framework-components) tag as appropriate in your React components.

Astro’s `<Image />` component works in `.astro` and `.mdx` files only. See a [full list of its component attributes](/en/reference/modules/astro-assets/#image-properties) and note that several will differ from Next’s attributes.

src/pages/index.astro

```astro
---
import { Image } from 'astro:assets';
import rocket from '../assets/rocket.png';
---
<Image src={rocket} alt="A rocketship in space." />
<img src={rocket.src} alt="A rocketship in space.">
```

In React (`.jsx`) components, use standard JSX image syntax (`<img />`). Astro will not optimize these images, but you can install and use NPM packages for more flexibility.

You can learn more about [using images in Astro](/en/guides/images/) in the Images Guide.

## Guided example: Next data fetching to Astro

[Section titled “Guided example: Next data fetching to Astro”](#guided-example-next-data-fetching-to-astro)

Here is an example of Next.js Pokédex data fetch converted to Astro.

`pages/index.js` fetches and displays a list of the first 151 Pokémon using [the REST PokéAPI](https://pokeapi.co/).

Here’s how to recreate that in `src/pages/index.astro`, replacing `getStaticProps()` with `fetch()`.

1. Identify the return() JSX.

   pages/index.js

   ```jsx
   import Link from 'next/link'
   import styles from '../styles/poke-list.module.css';


   export default function Home({ pokemons }) {
       return (
           <>
               <ul className={`plain-list ${styles.pokeList}`}>
                   {pokemons.map((pokemon) => (
                       <li className={styles.pokemonListItem} key={pokemon.name}>
                           <Link className={styles.pokemonContainer} as={`/pokemon/${pokemon.name}`} href="/pokemon/[name]">
                               <p className={styles.pokemonId}>No. {pokemon.id}</p>
                               <img className={styles.pokemonImage} src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`} alt={`${pokemon.name} picture`}></img>
                               <h2 className={styles.pokemonName}>{pokemon.name}</h2>
                           </Link>
                       </li>
                   ))}
               </ul>
           </>
       )
   }


   export const getStaticProps = async () => {
       const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151")
       const resJson = await res.json();
       const pokemons = resJson.results.map(pokemon => {
           const name = pokemon.name;
           // https://pokeapi.co/api/v2/pokemon/1/
           const url = pokemon.url;
           const id = url.split("/")[url.split("/").length - 2];
           return {
               name,
               url,
               id
           }
       });
       return {
           props: {
               pokemons,
           },
       }
   }
   ```

2. Create `src/pages/index.astro`

   Use the return value of the Next function. Convert any Next or React syntax to Astro, including changing the case of any [HTML global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes).

   Note that:

   * `.map` just works!

   * `className` becomes `class`.

   * `<Link>` becomes `<a>`.

   * The `<> </>` fragment is not required in Astro templating.

   * `key` is a React attribute, and is not an attribute of `li` in Astro.

   src/pages/index.astro

   ```astro
   ---
   ---
   <ul class="plain-list pokeList">
       {pokemons.map((pokemon) => (
           <li class="pokemonListItem">
               <a class="pokemonContainer" href={`/pokemon/${pokemon.name}`}>
                   <p class="pokemonId">No. {pokemon.id}</p>
                   <img class="pokemonImage" src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`} alt={`${pokemon.name} picture`}/>
                   <h2 class="pokemonName">{pokemon.name}</h2>
               </a>
           </li>
       ))}
   </ul>
   ```

3. Add any needed imports, props, and JavaScript

   Note that:

   * the `getStaticProps` function is no longer needed. Data from the API is fetched directly in the code fence.
   * A `<Layout>` component is imported and wraps the page templating.

   src/pages/index.astro

   ```diff
   ---
   +import Layout from '../layouts/layout.astro';


   +const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151");
   +const resJson = await res.json();
   +const pokemons = resJson.results.map(pokemon => {
       const name = pokemon.name;
       +// https://pokeapi.co/api/v2/pokemon/1/
       const url = pokemon.url;
       const id = url.split("/")[url.split("/").length - 2];
       return {
           +name,
           +url,
           +id
       }
   +});
   ---


   +<Layout>
     <ul class="plain-list pokeList">
         {pokemons.map((pokemon) => (
             <li class="pokemonListItem" key={pokemon.name}>
                 <a class="pokemonContainer" href={`/pokemon/${pokemon.name}`}>
                     <p class="pokemonId">No. {pokemon.id}</p>
                     <img class="pokemonImage" src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`} alt={`${pokemon.name} picture`}/>
                     <h2 class="pokemonName">{pokemon.name}</h2>
                 </a>
             </li>
         ))}
     </ul>
   +</Layout>
   ```

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Why we switched to Astro (and why it might interest you) ](https://www.datocms.com/blog/why-we-switched-to-astro)

[Migrating from Next.js to Astro ](https://johnzanussi.com/posts/nextjs-to-astro-migration)

[From NextJS to Astro ](https://vanntile.com/blog/next-to-astro)

[Converting Next.js to Astro ](https://ericclemmons.com/blog/converting-nextjs-to-astro)

[Migrating to Astro (from Next.js) ](https://www.raygesualdo.com/posts/migrating-to-astro-the-beginning/)

[Astro.js as an alternative to Next.js ](https://www.railyard.works/blog/astro-as-alternative-to-next)

[Why I Switched My Website from Next.js to Astro ](https://praveenjuge.com/blog/why-i-switched-my-website-from-nextjs-to-astro/)

[NextJS to Astro: more control = faster sites ](https://www.youtube.com/watch?v=PSzCtdM20Fc)

[How Astro made my site 100x faster ](https://www.youtube.com/watch?v=cOxA3kMYtkM)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Next.js site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-nextjs.mdx)!

# Migrating from NuxtJS

> Tips for migrating an existing NuxtJS project to Astro

Here are some key concepts and migration strategies to help you get started. Use the rest of our docs and our [Discord community](https://astro.build/chat) to keep going!

> This guide is referring to [Nuxt 2](https://nuxtjs.org/), not the newer Nuxt 3. While some of the concepts are similar, Nuxt 3 is a newer version of the framework and may require different strategies for parts of your migration.

## Key Similarities between Nuxt and Astro

[Section titled “Key Similarities between Nuxt and Astro”](#key-similarities-between-nuxt-and-astro)

Nuxt and Astro share some similarities that will help you migrate your project:

* Astro projects can also be SSG or [SSR with page level prerendering](/en/guides/on-demand-rendering/).
* Astro uses file-based routing, and [allows specially named pages to create dynamic routes](/en/guides/routing/#dynamic-routes).
* Astro is [component-based](/en/basics/astro-components/), and your markup structure will be similar before and after your migration.
* Astro has [an official integration for using Vue components](/en/guides/integrations-guide/vue/).
* Astro has support for [installing NPM packages](/en/guides/imports/#npm-packages), including Vue libraries. You may be able to keep some or all of your existing Vue components and dependencies.

## Key Differences between Nuxt and Astro

[Section titled “Key Differences between Nuxt and Astro”](#key-differences-between-nuxt-and-astro)

When you rebuild your Nuxt site in Astro, you will notice some important differences:

* Nuxt is a Vue-based SPA (single-page application). Astro sites are multi-page apps built using `.astro` components, but can also support React, Preact, Vue.js, Svelte, SolidJS, AlpineJS, and raw HTML templating.

* [Page Routing](/en/basics/astro-pages/#file-based-routing): Nuxt uses `vue-router` for SPA routing, and `vue-meta` for managing `<head>`. In Astro, you will create separate HTML page routes and control your page `<head>` directly, or in a layout component.

* [content-driven](/en/concepts/why-astro/#content-driven): Astro was designed to showcase your content and to allow you to opt-in to interactivity only as needed. An existing Nuxt app may be built for high client-side interactivity. Astro has built-in capabilities for working with your content, such as page generation, but may require advanced Astro techniques to include items that are more challenging to replicate using `.astro` components, such as dashboards.

## Convert your NuxtJS Project

[Section titled “Convert your NuxtJS Project”](#convert-your-nuxtjs-project)

Each project migration will look different, but there are some common actions you will perform when converting from Nuxt to Astro.

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
  ```

* pnpm

  ```shell
  # launch the Astro CLI Wizard
  pnpm create astro@latest


  # create a new project with an official example
  pnpm create astro@latest --template <example-name>
  ```

* Yarn

  ```shell
  # launch the Astro CLI Wizard
  yarn create astro@latest


  # create a new project with an official example
  yarn create astro@latest --template <example-name>
  ```

Then, copy your existing Nuxt project files over to your new Astro project in a separate folder outside of `src`.

Tip

Visit <https://astro.new> for the full list of official starter templates, and links for opening a new project in IDX, StackBlitz, CodeSandbox, or Gitpod.

### Install integrations (optional)

[Section titled “Install integrations (optional)”](#install-integrations-optional)

You may find it useful to install some of [Astro’s optional integrations](/en/guides/integrations-guide/) to use while converting your Nuxt project to Astro:

* **@astrojs/vue**: to reuse some existing Vue UI components in your new Astro site, or keep writing with Vue components.

* **@astrojs/mdx**: to bring existing MDX files from your Nuxt project, or to use MDX in your new Astro site.

### Put your source code in `src`

[Section titled “Put your source code in src”](#put-your-source-code-in-src)

1. **Move** the contents of Nuxt’s `static/` folder into `public/`.

   Astro uses the `public/` directory for static assets, similar to Nuxt’s `static/` folder.

2. **Copy or Move** Nuxt’s other files and folders (e.g. `pages`, `layouts` etc.) into Astro’s `src/` folder.

   Like Nuxt, Astro’s `src/pages/` folder is a special folder used for file-based routing. All other folders are optional, and you can organize the contents of your `src/` folder any way you like. Other common folders in Astro projects include `src/layouts/`, `src/components`, `src/styles`, `src/scripts`.

### Convert Vue SFC pages to `.astro` files

[Section titled “Convert Vue SFC pages to .astro files”](#convert-vue-sfc-pages-to-astro-files)

Here are some tips for converting a Nuxt `.vue` component into a `.astro` component:

1. Use the `<template>` of the existing NuxtJS component function as the basis for your HTML template.

2. Change any [Nuxt or Vue syntax to Astro](#reference-convert-nuxtjs-syntax-to-astro) or to HTML web standards. This includes `<NuxtLink>`, `:class`, `{{variable}}`, and `v-if`, for example.

3. Move `<script>` JavaScript, into a “code fence” (`---`). Convert your component’s data-fetching properties to server-side JavaScript - see [Nuxt data fetching to Astro](#nuxt-data-fetching-to-astro).

4. Use `Astro.props` to access any additional props that were previously passed to your Vue component.

5. Decide whether any imported components also need to be converted to Astro. With the official integration installed, you can [use existing Vue components in your Astro file](/en/guides/integrations-guide/vue/). But, you may want to convert them to Astro, especially if they do not need to be interactive!

See [an example from a Nuxt app converted step-by-step](#guided-example-see-the-steps).

#### Compare: Vue vs Astro

[Section titled “Compare: Vue vs Astro”](#compare-vue-vs-astro)

Compare the following Nuxt component and a corresponding Astro component:

* Vue

  Page.vue

  ```vue
  <template>
    <div>
      <p v-if="message === 'Not found'">
        The repository you're looking up doesn't exist
      </p>
      <div v-else>
        <Header/>
        <p class="banner">Astro has {{stars}} 🧑‍🚀</p>
        <Footer />
      </div>
    </div>
  </template>


  <script>
  import Vue from 'vue'


  export default Vue.extend({
    name: 'IndexPage',
    async asyncData() {
      const res = await fetch('https://api.github.com/repos/withastro/astro')
      const json = await res.json();
      return {
        message: json.message,
        stars: json.stargazers_count || 0,
      };
    }
  });
  </script>


  <style scoped>
  .banner {
    background-color: #f4f4f4;
    padding: 1em 1.5em;
    text-align: center;
    margin-bottom: 1em;
  }
  <style>
  ```

* Astro

  Page.astro

  ```astro
  ---
  import Header from "./header";
  import Footer from './footer';
  import "./layout.css";


  const res = await fetch('https://api.github.com/repos/withastro/astro')
  const json = await res.json()
  const message = json.message;
  const stars = json.stargazers_count || 0;
  ---


  {message === "Not Found" ?
        <p>The repository you're looking up doesn't exist</p> :
        <>
              <Header />
              <p class="banner">Astro has {stars} 🧑‍🚀</p>
              <Footer />
          </>
  }


  <style>
    .banner {
      background-color: #f4f4f4;
      padding: 1em 1.5em;
      text-align: center;
      margin-bottom: 1em;
    }
  <style>
  ```

### Migrating Layout Files

[Section titled “Migrating Layout Files”](#migrating-layout-files)

You may find it helpful to start by converting your Nuxt layouts and templates into [Astro layout components](/en/basics/layouts/).

Each Astro page explicitly requires `<html>`, `<head>`, and `<body>` tags to be present. Your Nuxt `layout.vue` and templates will not include these.

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
```

You may also wish to reuse code from [your Nuxt’s page’s `head` property](https://nuxtjs.org/docs/configuration-glossary/configuration-head/#the-head-property) to include additional site metadata. Notice that Astro uses neither `vue-meta` nor a component’s `head` property but instead creates `<head>` directly. You may import and use components, even within `<head>`, to separate and organize your page content.

### Migrating Pages and Posts

[Section titled “Migrating Pages and Posts”](#migrating-pages-and-posts)

In NuxtJS, your [pages](/en/basics/astro-pages/) live in `/pages`. In Astro, all your page content must live within `src/` unless you are using [content collections](/en/guides/content-collections/).

#### Vue Pages

[Section titled “Vue Pages”](#vue-pages)

Your existing Nuxt Vue (`.vue`) pages will need to be [converted from Vue files to `.astro` pages](#convert-vue-sfc-pages-to-astro-files). You cannot use an existing Vue page file in Astro.

These [`.astro` pages](/en/basics/astro-pages/) must be located within `src/pages/` and will have page routes generated automatically based on their file path.

##### Dynamic File Path Naming

[Section titled “Dynamic File Path Naming”](#dynamic-file-path-naming)

In Nuxt, your dynamic pages use an underscore to represent a dynamic page property that’s then passed to the page generation:

* pages/

  * pokemon/

    * \_name.vue

  * index.vue

* nuxt.config.js

To convert to Astro, change this underscored dynamic path property (e.g. `_name.vue`) to be wrapped in a pair of square brackets (e.g. `[name].astro`):

* src/

  * pages/

    * pokemon/

      * \[name].astro

    * index.astro

* astro.config.mjs

#### Markdown and MDX pages

[Section titled “Markdown and MDX pages”](#markdown-and-mdx-pages)

Astro has built-in support for Markdown and an optional integration for MDX files. You can reuse any existing Markdown and MDX pages, but they may require some adjustments to their frontmatter, such as adding [Astro’s special `layout` frontmatter property](/en/basics/layouts/#markdown-layouts).

You will no longer need to manually create pages for each Markdown-generated route or use an external package like `@nuxt/content`. These files can be placed within `src/pages/` to take advantage of automatic file-based routing.

When part of a [content collection](/en/guides/content-collections/), you will [generate pages dynamically](/en/guides/content-collections/#generating-routes-from-content) from your content entries.

### Migrating Tests

[Section titled “Migrating Tests”](#migrating-tests)

As Astro outputs raw HTML, it is possible to write end-to-end tests using the output of the build step. Any end-to-end tests written previously might work out-of-the-box, if you have been able to match the markup of your Nuxt site. Testing libraries such as Jest and Vue Testing Library can be imported and used in Astro to test your Vue components.

See Astro’s [testing guide](/en/guides/testing/) for more.

## Reference: Convert NuxtJS Syntax to Astro

[Section titled “Reference: Convert NuxtJS Syntax to Astro”](#reference-convert-nuxtjs-syntax-to-astro)

### Nuxt Local Variables to Astro

[Section titled “Nuxt Local Variables to Astro”](#nuxt-local-variables-to-astro)

To use local variables in an Astro component’s HTML, change the set of two curly braces to one set of curly braces:

src/components/Component.astro

```diff
---
const message = "Hello!"
---
<p>{{message}}</p>
<p>{message}</p>
```

### Nuxt Property Passing to Astro

[Section titled “Nuxt Property Passing to Astro”](#nuxt-property-passing-to-astro)

To bind an attribute or component property in an Astro component, change this syntax to the following:

src/components/Component.astro

```diff
---
---
<p v-bind:aria-label="message">...</p>
-<!-- Or -->
<p :aria-label="message">...</p>
-<!-- Also support component props -->
-<Header title="Page"/>


<p aria-label={message}>...</p>
+<!-- Also support component props -->
+<Header title={"Page"}/>
```

### Nuxt Links to Astro

[Section titled “Nuxt Links to Astro”](#nuxt-links-to-astro)

Convert any Nuxt `<NuxtLink to="">` components to HTML `<a href="">` tags.

```diff
-<NuxtLink to="/blog">Blog</Link>
<a href="/blog">Blog</a>
```

Astro does not use any special component for links, although you are welcome to build custom link components. You can then import and use this `<Link>` just as you would any other component.

src/components/Link.astro

```astro
---
const { to } = Astro.props
---
<a href={to}><slot /></a>
```

### Nuxt Imports to Astro

[Section titled “Nuxt Imports to Astro”](#nuxt-imports-to-astro)

If necessary, update any [file imports](/en/guides/imports/) to reference relative file paths exactly. This can be done using [import aliases](/en/guides/typescript/#import-aliases), or by writing out a relative path in full.

Note that `.astro` and several other file types must be imported with their full file extension.

src/pages/authors/Fred.astro

```astro
---
import Card from `../../components/Card.astro`;
---
<Card />
```

### Nuxt Dynamic Page Generation to Astro

[Section titled “Nuxt Dynamic Page Generation to Astro”](#nuxt-dynamic-page-generation-to-astro)

In Nuxt, to generate a dynamic page you either must:

* Use SSR.
* [Use the `generate` function in `nuxt.config.js`](https://nuxtjs.org/docs/configuration-glossary/configuration-generate/) to define all possible static routes.

In Astro, you similarly have two choices:

* [Use SSR](/en/guides/on-demand-rendering/).
* Export a `getStaticPaths()` function in the frontmatter of an Astro page to tell the framework which [static routes to generate dynamically](/en/guides/routing/#dynamic-routes).

#### Convert a `generate` function in Nuxt to a `getStaticPaths` function in Astro.

[Section titled “Convert a generate function in Nuxt to a getStaticPaths function in Astro.”](#convert-a-generate-function-in-nuxt-to-a-getstaticpaths-function-in-astro)

To generate multiple pages, replace the function to create routes in your `nuxt.config.js` with `getStaticPaths()` directly inside a dynamic routing page itself:

nuxt.config.js

```javascript
{
  // ...
    generate: {
        async routes() {
          // Axios is required here unless you're using Node 18
          const res = await axios.get("https://pokeapi.co/api/v2/pokemon?limit=151")
          const pokemons = res.data.results;
          return pokemons.map(pokemon => {
            return '/pokemon/' + pokemon.name
          })
        }
      }
}
```

src/pages/pokemon/\[name].astro

```astro
---
export const getStaticPaths = async () => {
  const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151")
  const resJson = await res.json();
  const pokemons = resJson.results;
  return pokemons.map(({ name }) => ({
      params: { name },
    }))
}
// ...
---
<!-- Your template here -->
```

### Nuxt Data Fetching to Astro

[Section titled “Nuxt Data Fetching to Astro”](#nuxt-data-fetching-to-astro)

Nuxt has two methods of fetching server-side data:

* [`asyncData` options API](https://nuxtjs.org/docs/features/data-fetching/#async-data)
* [`fetch` hook](https://nuxtjs.org/docs/features/data-fetching/#the-fetch-hook)

In Astro, fetch data inside of your page’s code fence.

Migrate the following:

pages/index.vue

```vue
{
  // ...
  async asyncData() {
    const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151")
    const resJson = await res.json();
    const pokemons = resJson.results;
    return {
      pokemons,
    }
  },
}
```

To a code fence without a wrapper function:

src/pages/index.astro

```astro
---
const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151")
const resJson = await res.json();
const pokemons = resJson.results;
---


<!-- Your template here -->
```

### Nuxt Styling to Astro

[Section titled “Nuxt Styling to Astro”](#nuxt-styling-to-astro)

Nuxt utilizes Vue’s component styling to generate a page’s style.

pages/index.vue

```vue
<template>
  <!-- Your template here -->
</template>


<script>
  // Your server logic here
</script>


<style scoped>
    .class {
        color: red;
    }
</style>
```

Similarly, in Astro you can drop in a `<style>` element in your page’s template to provide scoped styles to the component.

src/pages/index.vue

```astro
---
// Your server logic here
---


<style>
    .class {
        color: red;
    }
</style>
```

#### Global Styling

[Section titled “Global Styling”](#global-styling)

`<style>` tags are `scoped` by default in Astro. To make a `<style>` tag global, mark it with the `is:global` attribute:

src/pages/index.vue

```astro
<style is:global>
  p {
    color: red;
  }
</style>
```

#### Pre-processor support

[Section titled “Pre-processor support”](#pre-processor-support)

[Astro supports the most popular CSS preprocessors](/en/guides/styling/#css-preprocessors) by installing them as a dev dependency. For example, to use SCSS:

```shell
npm install -D sass
```

After doing so, you’re then able to use `.scss` or `.sass` styled without modification from your Vue components.

src/layouts/Layout.astro

```astro
<p>Hello, world</p>
<style lang="scss">
p {
   color: black;


   &:hover {
       color: red;
   }
}
</style>
```

See more about [Styling in Astro](/en/guides/styling/).

### Nuxt Image Plugin to Astro

[Section titled “Nuxt Image Plugin to Astro”](#nuxt-image-plugin-to-astro)

Convert any [Nuxt `<nuxt-img/>` or `<nuxt-picture/>` components](https://image.nuxt.com/usage/nuxt-img) to [Astro’s own image component](/en/guides/images/) in `.astro` or `.mdx` files, or to a [standard HTML `<img>`](/en/guides/images/#images-in-ui-framework-components) or `<picture>` tag as appropriate in your Vue components.

Astro’s `<Image />` component works in `.astro` and `.mdx` files only. See a [full list of its component attributes](/en/reference/modules/astro-assets/#image-properties) and note that several will differ from Nuxt’s attributes.

src/pages/index.astro

```astro
---
import { Image } from 'astro:assets';
import rocket from '../assets/rocket.png';
---
<Image src={rocket} alt="A rocketship in space." />
<img src={rocket.src} alt="A rocketship in space.">
```

In Vue (`.vue`) components within your Astro app, use standard JSX image syntax (`<img />`). Astro will not optimize these images, but you can install and use NPM packages for more flexibility.

You can learn more about [using images in Astro](/en/guides/images/) in the Images Guide.

## Guided example: See the steps!

[Section titled “Guided example: See the steps!”](#guided-example-see-the-steps)

Here is an example of Nuxt Pokédex data fetch converted to Astro.

`pages/index.vue` fetches and displays a list of the first 151 Pokémon using [the REST PokéAPI](https://pokeapi.co/).

Here’s how to recreate that in `src/pages/index.astro`, replacing `asyncData()` with `fetch()`.

1. Identify the `<template>` and `<style>` in the Vue SFC.

   pages/index.vue

   ```jsx
   <template>
     <ul class="plain-list pokeList">
               <li v-for="pokemon of pokemons" class="pokemonListItem" :key="pokemon.name">
                   <NuxtLink class="pokemonContainer" :to="`/pokemon/${pokemon.name}`">
                       <p class="pokemonId">No. {{pokemon.id}}</p>
                       <img
                         class="pokemonImage"
                         :src="`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`"
                         :alt="`${pokemon.name} picture`"/>
                       <h2 class="pokemonName">{{pokemon.name}}</h2>
                   </NuxtLink>
               </li>
       </ul>
   </template>


   <script>
   import Vue from 'vue'
   export default Vue.extend({
     name: 'IndexPage',
     layout: 'default',
     async asyncData() {
       const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151")
       const resJson = await res.json();
       const pokemons = resJson.results.map(pokemon => {
           const name = pokemon.name;
           // https://pokeapi.co/api/v2/pokemon/1/
           const url = pokemon.url;
           const id = url.split("/")[url.split("/").length - 2];
           return {
               name,
               url,
               id
           }
       });
       return {
         pokemons,
       }
     },
     head() {
       return {
         title: "Pokedex: Generation 1"
       }
     }
   });
   </script>


   <style scoped>
   .pokeList {
     display: grid;
     grid-template-columns: repeat( auto-fit, minmax(250px, 1fr) );
     gap: 1rem;
   }


   /* ... */
   </style>
   ```

2. Create `src/pages/index.astro`

   Use the `<template>` and `<style>` tags of the Nuxt SFC. Convert any Nuxt or Vue syntax to Astro.

   Note that:

   * `<template>` is removed

   * `<style>` has its `scoped` attribute removed

   * `v-for` becomes `.map`.

   * `:attr="val"` becomes `attr={val}`

   * `<NuxtLink>` becomes `<a>`.

   * The `<> </>` fragment is not required in Astro templating.

   src/pages/index.astro

   ```astro
   ---
   ---
   <ul class="plain-list pokeList">
       {pokemons.map((pokemon) => (
           <li class="pokemonListItem" key={pokemon.name}>
               <a class="pokemonContainer" href={`/pokemon/${pokemon.name}`}>
                   <p class="pokemonId">No. {pokemon.id}</p>
                   <img class="pokemonImage" src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`} alt={`${pokemon.name} picture`}/>
                   <h2 class="pokemonName">{pokemon.name}</h2>
               </a>
           </li>
       ))}
   </ul>


   <style>
   .pokeList {
     display: grid;
     grid-template-columns: repeat( auto-fit, minmax(250px, 1fr) );
     gap: 1rem;
   }


   /* ... */
   </style>
   ```

3. Add any needed imports, props and JavaScript

   Note that:

   * The `asyncData` function is no longer needed. Data from the API is fetched directly in the code fence.
   * A `<Layout>` component is imported, and wraps the page templating.
     * Our `head()` Nuxt method is passed to the `<Layout>` component, which is passed to the `<title>` element as a property.

   src/pages/index.astro

   ```diff
   ---
   +import Layout from '../layouts/layout.astro';


   +const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=151");
   +const resJson = await res.json();
   +const pokemons = resJson.results.map(pokemon => {
       const name = pokemon.name;
       +// https://pokeapi.co/api/v2/pokemon/1/
       const url = pokemon.url;
       const id = url.split("/")[url.split("/").length - 2];
       return {
           +name,
           +url,
           +id
       }
   +});
   ---


   +<Layout title="Pokedex: Generation 1">
     <ul class="plain-list pokeList">
         {pokemons.map((pokemon) => (
             <li class="pokemonListItem" key={pokemon.name}>
                 <a class="pokemonContainer" href={`/pokemon/${pokemon.name}`}>
                     <p class="pokemonId">No. {pokemon.id}</p>
                     <img class="pokemonImage" src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png`} alt={`${pokemon.name} picture`}/>
                     <h2 class="pokemonName">{pokemon.name}</h2>
                 </a>
             </li>
         ))}
     </ul>
   +</Layout>


   <style>
   .pokeList {
     display: grid;
     grid-template-columns: repeat( auto-fit, minmax(250px, 1fr) );
     gap: 1rem;
   }


   /* ... */
   </style>
   ```

## Community Resources

[Section titled “Community Resources”](#community-resources)

[From Nuxt to Astro - rebuilding with Astro ](https://dev.to/lindsaykwardell/from-nuxt-to-astro-rebuilding-with-astro-5ann)

[Nuxt 2 to Astro 3 Replatforming – from Setup to Production ](https://stevenwoodson.com/blog/replatforming-from-nuxtjs-2-to-astro/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Nuxt site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-nuxtjs.mdx)!

# Migrating from Pelican

> Tips for migrating an existing Pelican project to Astro

[Pelican](https://getpelican.com) is an open-source static site generator built on Python.

## Key Similarities between Pelican and Astro

[Section titled “Key Similarities between Pelican and Astro”](#key-similarities-between-pelican-and-astro)

Pelican and Astro share some similarities that will help you migrate your project:

* Pelican and Astro are both static-site generators, ideally suited to [content-driven websites](/en/concepts/why-astro/#content-driven) like blogs.

* Pelican and Astro both have built-in support for [writing in Markdown](/en/guides/markdown-content/), including frontmatter YAML properties for page metadata. However, Astro has very few reserved frontmatter properties compared to Pelican. Even though many of your existing Pelican frontmatter properties will not be “special” in Astro, you can continue to use your existing Markdown files and frontmatter values.

## Key Differences between Pelican and Astro

[Section titled “Key Differences between Pelican and Astro”](#key-differences-between-pelican-and-astro)

When you rebuild your Pelican site in Astro, you will notice some important differences:

* Pelican supports writing content in Markdown and reStructured Text (`.rst`). Astro supports [creating pages from Markdown and MDX](/en/guides/markdown-content/) files, but does not support reStructured Text.

* Pelican uses HTML files and Jinja syntax for templating. [Astro syntax](/en/basics/astro-components/) is a JSX-like superset of HTML. All valid HTML is valid `.astro` syntax.

* Pelican was designed to build content-rich websites like blogs and has some built-in, blog features that you would have to build yourself in Astro. Instead, Astro offers some of these features included in an [official blog theme](https://github.com/withastro/astro/tree/latest/examples/blog).

## Switch from Pelican to Astro

[Section titled “Switch from Pelican to Astro”](#switch-from-pelican-to-astro)

To convert a Pelican documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template starlight
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template starlight
  ```

* Yarn

  ```shell
  yarn create astro --template starlight
  ```

Bring your existing Markdown content files to [create Markdown pages](/en/guides/markdown-content/). You can still take advantage of [file-based routing](/en/guides/routing/) by copying these documents from Pelican’s `content/` folder into `src/pages/` in Astro. You may wish to read about [Astro’s project structure](/en/basics/project-structure/) to learn where files should be located.

Pelican may have handled much of your site layout and metadata for you. You may wish to read about [building Astro Layouts as Markdown page wrappers](/en/basics/layouts/#markdown-layouts) to see how to manage templating yourself in Astro, including your page `<head>`.

Like Pelican, Astro has many plugins that extend its functionality. Explore the [official list of integrations](/en/guides/integrations-guide/) for adding features such as MDX support, and find hundreds more of community-maintained integrations in the [Astro Integrations Directory](https://astro.build/integrations/). You can even use the [Astro Integration API](/en/reference/integrations-reference/) to build your own custom integration to extend your project’s features.

To convert other types of sites, such as a portfolio or a blog, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Pelican site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-pelican.mdx)!

# Migrating from SvelteKit

> Tips for migrating an existing SvelteKit project to Astro

[SvelteKit](https://kit.svelte.dev) is a framework for building web applications on top of Svelte.

## Key Similarities between SvelteKit and Astro

[Section titled “Key Similarities between SvelteKit and Astro”](#key-similarities-between-sveltekit-and-astro)

SvelteKit and Astro share some similarities that will help you migrate your project:

* Both SvelteKit and Astro are modern JavaScript static-site generators and server-side rendering frameworks.

* Both SvelteKit and Astro use a [`src/` folder for your project files](/en/basics/project-structure/#src) and a [special folder for file-based routing](/en/basics/astro-pages/). Creating and managing pages for your site should feel familiar.

* Astro has [an official integration for using Svelte components](/en/guides/integrations-guide/svelte/) and supports [installing NPM packages](/en/guides/imports/#npm-packages), including several for Svelte. You will be able to write Svelte UI components, and may be able to keep some or all of your existing components and dependencies.

* Astro and SvelteKit both allow you to use a [headless CMS, APIs or Markdown files for data](/en/guides/data-fetching/). You can continue to use your preferred content authoring system, and will be able to keep your existing content.

## Key Differences between SvelteKit and Astro

[Section titled “Key Differences between SvelteKit and Astro”](#key-differences-between-sveltekit-and-astro)

When you rebuild your SvelteKit site in Astro, you will notice some important differences:

* Astro sites are multi-page apps, whereas SvelteKit defaults to SPAs (single-page applications) with server-side rendering, but can also create MPAs, traditional SPAs, or you can mix and match these techniques within an app.

* [Components](/en/basics/astro-components/): SvelteKit uses [Svelte](https://svelte.dev). Astro pages are built using [`.astro` components](/en/basics/astro-components/), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](/en/guides/framework-components/) and raw HTML templating.

* [content-driven](/en/concepts/why-astro/#content-driven): Astro was designed to showcase your content and to allow you to opt-in to interactivity only as needed. An existing SvelteKit app might be built for high client-side interactivity. Astro has built-in capabilities for working with your content, such as page generation, but may require advanced Astro techniques to include items that are more challenging to replicate using `.astro` components, such as dashboards.

* [Markdown-ready](/en/guides/markdown-content/): Astro includes built-in Markdown support, and includes a [special frontmatter YAML `layout` property](/en/basics/layouts/#markdown-layouts) used per-file for page templating. If you are converting a SvelteKit Markdown-based blog, you will not have to install a separate Markdown integration and you will not set a layout via a configuration file. You can bring your existing Markdown files, but you may need to reorganize as Astro’s file-based routing does not require a folder for each page route.

## Switch from SvelteKit to Astro

[Section titled “Switch from SvelteKit to Astro”](#switch-from-sveltekit-to-astro)

To convert a SvelteKit blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template blog
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template blog
  ```

* Yarn

  ```shell
  yarn create astro --template blog
  ```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](/en/guides/markdown-content/).

While file-based routing and layout components are similar in Astro, you may wish to read about [Astro’s project structure](/en/basics/project-structure/) to learn where files should be located.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Rewriting my blog from SvelteKit to Astro ](https://kharann.com/blog/rewriting-my-blog/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a SvelteKit site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-sveltekit.mdx)!

# Migrating from VuePress

> Tips for migrating an existing VuePress project to Astro

[VuePress](https://vuePress.vuejs.org) is an open-source static site generator built on Vue.

## Key Similarities between VuePress and Astro

[Section titled “Key Similarities between VuePress and Astro”](#key-similarities-between-vuepress-and-astro)

VuePress and Astro share some similarities that will help you migrate your project:

* Both VuePress and Astro are modern JavaScript static-site generators with similar project file structures. Both use a [special `src/pages/` folder for file-based routing](/en/basics/astro-pages/). Creating and managing pages for your site should feel familiar.

* Astro and VuePress are both designed for [content-driven websites](/en/concepts/why-astro/#content-driven), with excellent built-in support for Markdown files. Writing in Markdown will feel familiar, and you will be able to keep your existing content.

* Astro has [an official integration for using Vue components](/en/guides/integrations-guide/vue/) and supports [installing NPM packages](/en/guides/imports/#npm-packages), including several for Vue. You will be able to write Vue UI components, and may be able to keep some or all of your existing Vue components and dependencies.

## Key Differences between VuePress and Astro

[Section titled “Key Differences between VuePress and Astro”](#key-differences-between-vuepress-and-astro)

When you rebuild your VuePress site in Astro, you will notice some important differences.

* VuePress is a Vue-based single-page application (SPA). Astro sites are multi-page apps built using [`.astro` components](/en/basics/astro-components/), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](/en/guides/framework-components/) and raw HTML templating.

* [Layout templates](/en/basics/layouts/): VuePress sites are created using Markdown (`.md`) files for page content and HTML (`.html`) templates for layout. Astro is component-based, and uses Astro components, which include HTML templating for pages, layouts and individual UI elements. Astro can also create [pages from `.md` and `.mdx` files](/en/guides/markdown-content/), using an Astro layout component for wrapping Markdown content in a page template.

* VuePress was designed to build content-heavy, Markdown-centric sites and has some built-in, documentation-specific website features that you would have to build yourself in Astro. Instead, Astro offers some documentation-specific features through an [official docs theme](https://starlight.astro.build). This website was the inspiration for that template! You can also find more [community docs themes](https://astro.build/themes?search=\&categories%5B%5D=docs) with built-in features in our Themes Showcase.

## Switch from VuePress to Astro

[Section titled “Switch from VuePress to Astro”](#switch-from-vuepress-to-astro)

To convert a VuePress documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=\&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template starlight
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template starlight
  ```

* Yarn

  ```shell
  yarn create astro --template starlight
  ```

Bring your existing Markdown content files to [create Markdown pages](/en/guides/markdown-content/). You can still take advantage of [file-based routing](/en/guides/routing/) by moving these documents from `docs` in VuePress to `src/pages/` in Astro. Create folders with names that correspond to your existing VuePress project, and you should be able to keep your existing URLs.

VuePress, or any theme you installed, probably handled much of your site layout and metadata for you. You may wish to read about [building Astro Layouts as Markdown page wrappers](/en/basics/layouts/#markdown-layouts) to see how to manage templating yourself in Astro, including your page `<head>`.

You can find Astro’s docs starter, and other templates, on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a VuePress site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-vuepress.mdx)!

# Migrating from WordPress

> Tips for migrating an existing WordPress project to Astro

[WordPress](https://wordpress.org) is an open-source, personal publishing system built on PHP and MySQL.

Tip

You can [use WordPress as a headless CMS for your Astro project](/en/guides/cms/wordpress/). Follow our guide to use your existing WordPress content in a new Astro project.

## Key Similarities between WordPress and Astro

[Section titled “Key Similarities between WordPress and Astro”](#key-similarities-between-wordpress-and-astro)

WordPress and Astro share some similarities that will help you migrate your project:

* Both WordPress and Astro are ideal for [content-driven websites](/en/concepts/why-astro/#content-driven) like blogs and support writing your content in Markdown (requires a plugin in WordPress). Although the process for adding new content is different, [writing in Markdown files](/en/guides/markdown-content/) for your Astro blog should feel familiar if you have used Markdown syntax in your WordPress editor.

* Both WordPress and Astro encourage you to [think about the design of your site in “blocks”](/en/concepts/islands/) (components). In Astro you will probably [write more of your own code to create these blocks](/en/basics/astro-components/) rather than rely on pre-built plugins. But thinking about the individual pieces of your site and how they are presented on the page should feel familiar.

## Key Differences between WordPress and Astro

[Section titled “Key Differences between WordPress and Astro”](#key-differences-between-wordpress-and-astro)

When you rebuild your WordPress site in Astro, you will notice some important differences:

* A WordPress site is edited using an online dashboard. In Astro, you will use a [code editor](/en/editor-setup/) and development environment to maintain your site. You can develop locally on your machine, or choose a cloud editor/development environment like IDX, StackBlitz, CodeSandbox or Gitpod.

* WordPress has an extensive plugin and theme market. In Astro, you will find some themes and [integrations](https://astro.build/integrations/) available, but you may now have to build many of your existing features yourself instead of looking for third-party solutions. Or, you can choose to start with an [Astro theme](https://astro.build/themes) with built-in features!

* WordPress stores your content in a database. In Astro, you will have individual files (typically Markdown or MDX) in your [project directory](/en/basics/project-structure/) for each page’s content. Or, you can choose to use a [CMS for your content](/en/guides/cms/), even your existing WordPress site, and use Astro to fetch and present the data.

## Switch from WordPress to Astro

[Section titled “Switch from WordPress to Astro”](#switch-from-wordpress-to-astro)

To convert a WordPress blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template blog
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template blog
  ```

* Yarn

  ```shell
  yarn create astro --template blog
  ```

You can continue to [use your existing WordPress blog as your CMS for Astro](/en/guides/cms/wordpress/), which means you will keep using your WordPress dashboard for writing your posts. Your content will be managed at WordPress, but all other aspects of your Astro site will be built in your code editing environment, and you will [deploy your Astro site](/en/guides/deploy/) separately from your WordPress site. (Be sure to update your domain at your host to keep the same website URL!)

You may wish to take [Astro’s Build a Blog Tutorial](/en/tutorial/0-introduction/) if you are new to working in a code editor and using GitHub to store and deploy your site. It will walk you through all the accounts and setup you need! You will also learn how to [build Astro components yourself](/en/tutorial/3-components/), and it will show you how to [add blog posts directly in Astro](/en/tutorial/2-pages/2/) if you choose not to use WordPress to write your content.

If you want to move all of your existing post content to Astro, you may find this [tool for exporting Markdown from WordPress helpful](https://github.com/lonekorean/wordpress-export-to-markdown). You may need to make some adjustments to the result if you have to [convert a large or complicated WordPress site to Markdown](https://swizec.com/blog/how-to-export-a-large-wordpress-site-to-markdown/).

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Goodbye Wordpress, hello Astro! ](https://trib.tv/posts/2025/wordpress-to-astro/)

[How I Migrated from Wordpress to Astro ](https://itsthatlady.dev/blog/migrate-from-wordpress-to-astro/)

[How and Why I Moved My Blog from WordPress to Astro and Markdown ](https://levelup.gitconnected.com/how-and-why-i-moved-my-blog-from-wordpress-to-astro-and-markdown-3549672d5a86)

[How I Migrated From Wordpress to Astro: Boosted Pagespeed Scores to 100% and Cut 100% Hosting cost ](https://devaradise.com/wordpress-to-static-website-astro/)

[WordPress to Astro site conversion ](https://share.transistor.fm/s/d86496cd)

[How to Convert a Wordpress blog to an Astro Static Site ](https://blog.okturtles.org/2024/10/convert-wordpress-to-static-site/)

[Why I switched from WordPress to Astro ](https://dev.to/fratzinger/why-i-switched-from-wordpress-to-astro-5ge)

[Why I ditched WordPress for Astro ](https://vbartalis.xyz/en/blog/why-i-ditched-wordpress-for-astro-js/)

[DeWP: utility to use your WordPress data in Astro projects ](https://delucis.github.io/dewp/)

[Astro vs. WordPress: Rendering Patterns of the Modern Web ](https://andrewkepson.com/blog/headless-wordpress/astro-vs-wordpress-rendering-patterns/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a WordPress site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-wordpress.mdx)!

# On-demand rendering

> Generate server-rendered pages and routes on demand with an adapter.

Your Astro project code must be **rendered** to HTML in order to be displayed on the web.

By default, Astro pages, routes, and API endpoints will be pre-rendered at build time as static pages. However, you can choose to render some or all of your routes on demand by a server when a route is requested.

On-demand rendered pages and routes are generated per visit, and can be customized for each viewer. For example, a page rendered on demand can show a logged-in user their account information or display freshly updated data without requiring a full-site rebuild.

On-demand rendering on the server at request time is also known as **server-side rendering (SSR)**.

## Server adapters

[Section titled “Server adapters”](#server-adapters)

To render any page on demand, you need to add an **adapter**. Each adapter allows Astro to output a script that runs your project on a specific **runtime**: the environment that runs code on the server to generate pages when they are requested (e.g. Netlify, Cloudflare).

You may also wish to add an adapter even if your site is entirely static and you are not rendering any pages on demand. For example, the [Netlify adapter](/en/guides/integrations-guide/netlify/) enables Netlify’s Image CDN, and [server islands](/en/guides/server-islands/) require an adapter installed to use `server:defer` on a component.

### Adapters

* ![](/logos/cloudflare-pages.svg)

  ### [@astrojs/​cloudflare](/en/guides/integrations-guide/cloudflare/)

* ![](/logos/netlify.svg)

  ### [@astrojs/​netlify](/en/guides/integrations-guide/netlify/)

* ![](/logos/node.svg)

  ### [@astrojs/​node](/en/guides/integrations-guide/node/)

* ![](/logos/vercel.svg)

  ### [@astrojs/​vercel](/en/guides/integrations-guide/vercel/)

Astro maintains official adapters for [Node.js](https://nodejs.org/), [Netlify](https://www.netlify.com/), [Vercel](https://vercel.com/), and [Cloudflare](https://www.cloudflare.com/). You can find both [official and community adapters in our integrations directory](https://astro.build/integrations/?search=\&categories%5B%5D=adapters). Choose the one that corresponds to your [deployment environment](/en/guides/deploy/).

### Add an Adapter

[Section titled “Add an Adapter”](#add-an-adapter)

You can add any of the [official adapter integrations maintained by Astro](/en/guides/integrations-guide/#official-integrations) with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

For example, to install the Netlify adapter, run:

* npm

  ```shell
  npx astro add netlify
  ```

* pnpm

  ```shell
  pnpm astro add netlify
  ```

* Yarn

  ```shell
  yarn astro add netlify
  ```

You can also [add an adapter manually by installing the NPM package](/en/guides/integrations-guide/#installing-an-npm-package) (e.g. `@astrojs/netlify`) and updating `astro.config.mjs` yourself.

Note that different adapters may have different configuration settings. Read each adapter’s documentation, and apply any necessary config options to your chosen adapter in `astro.config.mjs`

## Enabling on-demand rendering

[Section titled “Enabling on-demand rendering”](#enabling-on-demand-rendering)

**By default, your entire Astro site will be prerendered**, and static HTML pages will be sent to the browser. However, you may opt out of prerendering on any routes that require server rendering, for example, a page that checks for cookies and displays personalized content.

First, [add an adapter integration](#add-an-adapter) for your server runtime to enable on-demand server rendering in your Astro project.

Then, add `export const prerender = false` at the top of the individual page or endpoint you want to render on demand. The rest of your site will remain a static site:

src/pages/page-rendered-on-demand.astro

```diff
---
+export const prerender = false
---
<html>
<!--
This content will be server-rendered on demand!
Just add an adapter integration for a server runtime!
All other pages are statically-generated at build time!
-->
<html>
```

The following example shows opting out of prerendering in order to display a random number each time the endpoint is hit:

src/pages/randomnumber.js

```diff
+export const prerender = false;


export async function GET() {
  let number = Math.random();
  return new Response(
    JSON.stringify({
      number,
      message: `Here's a random number: ${number}`,
    }),
  );
}
```

### `'server'` mode

[Section titled “'server' mode”](#server-mode)

For a **highly dynamic app**, after adding an adapter, you can [set your build output configuration to `output: 'server'`](/en/reference/configuration-reference/#output) to **server-render all your pages by default**. This is the equivalent of opting out of prerendering on every page.

Then, if needed, you can choose to prerender any individual pages that do not require a server to execute, such as a privacy policy or about page.

src/pages/about-my-app.astro

```diff
---
+export const prerender = true
---
<html>
<!--
`output: 'server'` is configured, but this page is static!
The rest of my site is rendered on demand!
-->
<html>
```

Add `export const prerender = true` to any page or route to prerender a static page or endpoint:

src/pages/myendpoint.js

```diff
+export const prerender = true;


export async function GET() {
  return new Response(
    JSON.stringify({
      message: `This is my static endpoint`,
    }),
  );
}
```

Tip

Start with the default `'static'` mode until you are sure that **most or all** of your pages will be rendered on demand! This ensures that your site is as performant as possible, not relying on a server function to render static content.

The `'server'` output mode does not bring any additional functionality. It only switches the default rendering behavior.

See more about the [`output` setting](/en/reference/configuration-reference/#output) in the configuration reference.

## On-demand rendering features

[Section titled “On-demand rendering features”](#on-demand-rendering-features)

### HTML streaming

[Section titled “HTML streaming”](#html-streaming)

With HTML streaming, a document is broken up into chunks, sent over the network in order, and rendered on the page in that order. Astro uses HTML streaming in on-demand rendering to send each component to the browser as it renders them. This makes sure the user sees your HTML as fast as possible, although network conditions can cause large documents to be downloaded slowly, and waiting for data fetches can block page rendering.

![](/houston_chef.webp) **Related recipe:** [Using streaming to improve page performance](/en/recipes/streaming-improve-page-performance/)

Caution

Features that modify the [Response headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header) are only available at the **page level**. (You can’t use them inside of components, including layout components.) By the time Astro runs your component code, it has already sent the Response headers and they cannot be modified.

### Cookies

[Section titled “Cookies”](#cookies)

A page or API endpoint rendered on demand can check, set, get, and delete cookies.

The example below updates the value of a cookie for a page view counter:

src/pages/index.astro

```astro
---
export const prerender = false; // Not needed in 'server' mode


let counter = 0


if (Astro.cookies.has('counter')) {
  const cookie = Astro.cookies.get('counter')
  const value = cookie?.number()
  if (value !== undefined && !isNaN(value)) counter = value + 1
}


Astro.cookies.set('counter', String(counter))
---
<html>
  <h1>Counter = {counter}</h1>
</html>
```

See more details about [`Astro.cookies` and the `AstroCookie` type](/en/reference/api-reference/#cookies) in the API reference.

### `Response`

[Section titled “Response”](#response)

[`Astro.response`](/en/reference/api-reference/#response) is a standard [`ResponseInit`](https://developer.mozilla.org/en-US/docs/Web/API/Response/Response#options) object. It can be used to set the response status and headers.

The example below sets a response status and status text for a product page when the product does not exist:

src/pages/product/\[id].astro

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getProduct } from '../api';


const product = await getProduct(Astro.params.id);


// No product found
if (!product) {
  Astro.response.status = 404;
  Astro.response.statusText = 'Not found';
}
---
<html>
  <!-- Page here... -->
</html>
```

#### `Astro.response.headers`

[Section titled “Astro.response.headers”](#astroresponseheaders)

You can set headers using the `Astro.response.headers` object:

src/pages/index.astro

```astro
---
export const prerender = false; // Not needed in 'server' mode


Astro.response.headers.set('Cache-Control', 'public, max-age=3600');
---
<html>
  <!-- Page here... -->
</html>
```

#### Return a `Response` object

[Section titled “Return a Response object”](#return-a-response-object)

You can also return a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object directly from any page using on-demand rendering either manually or with [`Astro.redirect`](/en/reference/api-reference/#redirect).

The example below looks up an ID in the database on a dynamic page and either it returns a 404 if the product does not exist, or it redirects the user to another page if the product is no longer available, or it displays the product:

src/pages/product/\[id].astro

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getProduct } from '../api';


const product = await getProduct(Astro.params.id);


// No product found
if (!product) {
  return new Response(null, {
    status: 404,
    statusText: 'Not found'
  });
}


// The product is no longer available
if (!product.isAvailable) {
  return Astro.redirect("/products", 301);
}
---
<html>
  <!-- Page here... -->
</html>
```

### `Request`

[Section titled “Request”](#request)

`Astro.request` is a standard [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object. It can be used to get the `url`, `headers`, `method`, and even the body of the request.

You can access additional information from this object for pages that are not statically generated.

#### `Astro.request.headers`

[Section titled “Astro.request.headers”](#astrorequestheaders)

The headers for the request are available on `Astro.request.headers`. This works like the browser’s [`Request.headers`](https://developer.mozilla.org/en-US/docs/Web/API/Request/headers). It is a [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers) object where you can retrieve headers such as the cookie.

src/pages/index.astro

```astro
---
export const prerender = false; // Not needed in 'server' mode


const cookie = Astro.request.headers.get('cookie');
// ...
---
<html>
  <!-- Page here... -->
</html>
```

#### `Astro.request.method`

[Section titled “Astro.request.method”](#astrorequestmethod)

The HTTP method used in the request is available as `Astro.request.method`. This works like the browser’s [`Request.method`](https://developer.mozilla.org/en-US/docs/Web/API/Request/method). It returns the string representation of the HTTP method used in the request.

src/pages/index.astro

```astro
---
export const prerender = false; // Not needed in 'server' mode


console.log(Astro.request.method) // GET (when navigated to in the browser)
---
```

See more details about [`Astro.request`](/en/reference/api-reference/#request) in the API reference.

### Server Endpoints

[Section titled “Server Endpoints”](#server-endpoints)

A server endpoint, also known as an **API route**, is a special function exported from a `.js` or `.ts` file within the `src/pages/` folder. A powerful feature of server-side rendering on demand, API routes are able to securely execute code on the server.

The function takes an [endpoint context](/en/reference/api-reference/) and returns a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response).

To learn more, see our [Endpoints Guide](/en/guides/endpoints/#server-endpoints-api-routes).

# Prefetch

> Prefetch links for snappier navigation between pages.

Page load times play a big role in the usability and overall enjoyment of a site. Astro’s **opt-in prefetching** brings the benefits of near-instant page navigations to your multi-page application (MPA) as your visitors interact with the site.

## Enable prefetching

[Section titled “Enable prefetching”](#enable-prefetching)

You can enable prefetching with the `prefetch` config:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  prefetch: true
});
```

A prefetch script will be added to all pages of your site. You can then add the `data-astro-prefetch` attribute to any `<a />` links on your site to opt-in to prefetching. When you hover over the link, the script will fetch the page in the background.

```html
<a href="/about" data-astro-prefetch>
```

Note that prefetching only works for links within your site, and not external links.

## Prefetch configuration

[Section titled “Prefetch configuration”](#prefetch-configuration)

The `prefetch` config also accepts an option object to further customize prefetching.

### Prefetch strategies

[Section titled “Prefetch strategies”](#prefetch-strategies)

Astro supports 4 prefetch strategies for various use cases:

* `hover` (default): Prefetch when you hover over or focus on the link.
* `tap`: Prefetch just before you click on the link.
* `viewport`: Prefetch as the links enter the viewport.
* `load`: Prefetch all links on the page after the page is loaded.

You can specify a strategy for an individual link by passing it to the `data-astro-prefetch` attribute:

```html
<a href="/about" data-astro-prefetch="tap">About</a>
```

Each strategy is fine-tuned to only prefetch when needed and save your users’ bandwidth. For example:

* If a visitor is using [data saver mode](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/saveData) or has a [slow connection](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/effectiveType), prefetch will fallback to the `tap` strategy.
* Quickly hovering or scrolling over links will not prefetch them.

### Default prefetch strategy

[Section titled “Default prefetch strategy”](#default-prefetch-strategy)

The default prefetch strategy when adding the `data-astro-prefetch` attribute is `hover`. To change it, you can configure [`prefetch.defaultStrategy`](/en/reference/configuration-reference/#prefetchdefaultstrategy) in your `astro.config.mjs` file:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  prefetch: {
+    defaultStrategy: 'viewport'
+  }
});
```

### Prefetch all links by default

[Section titled “Prefetch all links by default”](#prefetch-all-links-by-default)

If you want to prefetch all links, including those without the `data-astro-prefetch` attribute, you can set [`prefetch.prefetchAll`](/en/reference/configuration-reference/#prefetchprefetchall) to `true`:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  prefetch: {
+    prefetchAll: true
+  }
});
```

You can then opt-out of prefetching for individual links by setting `data-astro-prefetch="false"`:

```html
<a href="/about" data-astro-prefetch="false">About</a>
```

The default prefetch strategy for all links can be changed with `prefetch.defaultStrategy` as shown in the [Default prefetch strategy section](#default-prefetch-strategy).

## Prefetch programmatically

[Section titled “Prefetch programmatically”](#prefetch-programmatically)

As some navigation might not always appear as `<a />` links, you can also prefetch programmatically with the `prefetch()` API from the `astro:prefetch` module:

```astro
<button id="btn">Click me</button>


<script>
  import { prefetch } from 'astro:prefetch';


  const btn = document.getElementById('btn');
  btn.addEventListener('click', () => {
    prefetch('/about');
  });
</script>
```

The `prefetch()` API includes the same [data saver mode](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/saveData) and [slow connection](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/effectiveType) detection so that it only prefetches when needed.

To ignore slow connection detection, you can use the `ignoreSlowConnection` option:

```js
// Prefetch even on data saver mode or slow connection
prefetch('/about', { ignoreSlowConnection: true });
```

### `eagerness`

[Section titled “eagerness”](#eagerness)

**Type:** `'immediate' | 'eager' | 'moderate' | 'conservative'`\
**Default:** `'immediate'`

**Added in:** `astro@5.6.0`

With the experimental [`clientPrerender`](/en/reference/experimental-flags/client-prerender/) flag enabled, you can use the `eagerness` option on `prefetch()` to suggest to the browser how eagerly it should prefetch/prerender link targets.

This follows the same API described in the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script/type/speculationrules#eagerness) and defaults to `immediate` (the most eager option). In decreasing order of eagerness, the other options are `eager`, `moderate`, and `conservative`.

The `eagerness` option allows you to balance the benefit of reduced wait times against bandwidth, memory, and CPU costs for your site visitors. Some browsers, such as Chrome, have [limits in place to guard against over-speculating](https://developer.chrome.com/blog/speculation-rules-improvements#chrome-limits) (prerendering/prefetching too many links).

```astro
---
---
<script>
// Control prefetching eagerness with `experimental.clientPrerender`
import { prefetch } from 'astro:prefetch';


// This page is resource-intensive
prefetch('/data-heavy-dashboard', { eagerness: 'conservative' });


// This page is critical to the visitor's journey
prefetch('/getting-started'); // defaults to `{ eagerness: 'immediate' }`


// This page may not be visited
prefetch('/terms-of-service', { eagerness: 'moderate' });
</script>
```

To use `prefetch()` programmatically with large sets of links, you can set `eagerness: 'moderate'` to take advantage of [First In, First Out (FIFO)](https://en.wikipedia.org/wiki/FIFO_\(computing_and_electronics\)) strategies and browser heuristics to let the browser decide when to prerender/prefetch them and in what order:

```astro
<a class="link-moderate" href="/nice-link-1">A Nice Link 1</a>
<a class="link-moderate" href="/nice-link-2">A Nice Link 2</a>
<a class="link-moderate" href="/nice-link-3">A Nice Link 3</a>
<a class="link-moderate" href="/nice-link-4">A Nice Link 4</a>
...
<a class="link-moderate" href="/nice-link-20">A Nice Link 20</a>


<script>
  import { prefetch } from 'astro:prefetch';


  const linkModerate = document.getElementsByClassName('link-moderate');
  linkModerate.forEach((link) => prefetch(link.getAttribute('href'), {eagerness: 'moderate'}));


</script>
```

Make sure to only import `prefetch()` in client-side scripts as it relies on browser APIs.

## Using with View Transitions

[Section titled “Using with View Transitions”](#using-with-view-transitions)

When you use [Astro’s `<ClientRouter />`](/en/guides/view-transitions/#enabling-view-transitions-spa-mode) on a page, prefetching will also be enabled by default. It sets a default configuration of `{ prefetchAll: true }` which enables [prefetching for all links](#prefetch-all-links-by-default) on the page.

You can customize the prefetch configuration in `astro.config.mjs` to override the default. For example:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  // Disable prefetch completely
  prefetch: false
});
```

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  // Keep prefetch, but only prefetch for links with `data-astro-prefetch`
  prefetch: {
    prefetchAll: false
  }
});
```

## Browser support

[Section titled “Browser support”](#browser-support)

Astro’s prefetching uses [`<link rel="prefetch">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/prefetch) if supported by the browser, and falls back to the [`fetch()` API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) otherwise.

The most common browsers support Astro’s prefetching with subtle differences:

### Chrome

[Section titled “Chrome”](#chrome)

Chrome supports `<link rel="prefetch">`. Prefetching works as intended.

It also fully supports `<script type="speculationrules">` from the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API), which can be used to further describe [prefetching strategies and rules](#eagerness), enhancing user experience for your Chrome users. You’ll need to enable [`clientPrerender`](/en/reference/experimental-flags/client-prerender/) experiment to utilize this functionality with `prefetch()`

### Firefox

[Section titled “Firefox”](#firefox)

Firefox supports `<link rel="prefetch">` but may display errors or fail entirely:

* Without an explicit cache header (e.g. [`Cache-Control`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) or [`Expires`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires)), prefetching will error with `NS_BINDING_ABORTED`.
* Even in the event of an error, if the response has a proper [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header, it will be re-used on navigation.
* Otherwise, if it errors with no other cache headers, the prefetch will not work.

### Safari

[Section titled “Safari”](#safari)

Safari does not support `<link rel="prefetch">` and will fall back to the `fetch()` API which requires cache headers (e.g. [`Cache-Control`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control), [`Expires`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires), and [`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)) to be set. Otherwise, the prefetch will not work.

**Edge case:** `ETag` headers do not work in private windows.

### Recommendations

[Section titled “Recommendations”](#recommendations)

To best support all browsers, make sure your pages have the proper cache headers.

For static or prerendered pages, the `ETag` header is often automatically set by the deployment platform and is expected to work out of the box.

For dynamic and server-side rendered pages, set the appropriate cache headers yourself based on the page content. Visit the [MDN documentation on HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) for more information.

## Migrating from `@astrojs/prefetch`

[Section titled “Migrating from @astrojs/prefetch”](#migrating-from-astrojsprefetch)

The `@astrojs/prefetch` integration was deprecated in v3.5.0 and will eventually be removed entirely. Use the following instructions to migrate to Astro’s built-in prefetching which replaces this integration.

1. Remove the `@astrojs/prefetch` integration and enable the `prefetch` config in `astro.config.mjs`:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   -import prefetch from '@astrojs/prefetch';


   export default defineConfig({
   -  integrations: [prefetch()],
   +  prefetch: true
   });
   ```

2. Convert from `@astrojs/prefetch`’s configuration options:

   * The deprecated integration used the `selector` config option to specify which links should be prefetched upon entering the viewport.

     Add `data-astro-prefetch="viewport"` to these individual links instead.

     ```html
     <a href="/about" data-astro-prefetch="viewport">
     ```

   * The deprecated integration used the `intentSelector` config option to specify which links should be prefetched when they were hovered over or focused.

     Add `data-astro-prefetch` or `data-astro-prefetch="hover"` to these individual links instead:

     ```html
     <!-- You can omit the value if `defaultStrategy` is set to `hover` (default) -->
     <a href="/about" data-astro-prefetch>


     <!-- Otherwise, you can explicitly define the prefetch strategy -->
     <a href="/about" data-astro-prefetch="hover">
     ```

   * The `throttles` option from `@astrojs/prefetch` is no longer needed as the new prefetch feature will automatically schedule and prefetch optimally.

# Routing

> An intro to routing with Astro.

Astro uses **file-based routing** to generate your build URLs based on the file layout of your project `src/pages/` directory.

## Navigating between pages

[Section titled “Navigating between pages”](#navigating-between-pages)

Astro uses standard HTML [`<a>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) to navigate between routes. There is no framework-specific `<Link>` component provided.

src/pages/index.astro

```astro
<p>Read more <a href="/about/">about</a> Astro!</p>


<!-- With `base: "/docs"` configured -->
<p>Learn more in our <a href="/docs/reference/">reference</a> section!</p>
```

## Static routes

[Section titled “Static routes”](#static-routes)

`.astro` [page components](/en/basics/astro-pages/) as well as Markdown and MDX Files (`.md`, `.mdx`) within the `src/pages/` directory **automatically become pages on your website**. Each page’s route corresponds to its path and filename within the `src/pages/` directory.

```diff
# Example: Static routes
src/pages/index.astro        -> mysite.com/
src/pages/about.astro        -> mysite.com/about
src/pages/about/index.astro  -> mysite.com/about
src/pages/about/me.astro     -> mysite.com/about/me
src/pages/posts/1.md         -> mysite.com/posts/1
```

Tip

There is no separate “routing config” to maintain in an Astro project! When you add a file to the `src/pages/` directory, a new route is automatically created for you. In static builds, you can customize the file output format using the [`build.format`](/en/reference/configuration-reference/#buildformat) configuration option.

## Dynamic routes

[Section titled “Dynamic routes”](#dynamic-routes)

An Astro page file can specify dynamic route parameters in its filename to generate multiple, matching pages. For example, `src/pages/authors/[author].astro` generates a bio page for every author on your blog. `author` becomes a *parameter* that you can access from inside the page.

In Astro’s default static output mode, these pages are generated at build time, and so you must predetermine the list of `author`s that get a corresponding file. In SSR mode, a page will be generated on request for any route that matches.

### Static (SSG) Mode

[Section titled “Static (SSG) Mode”](#static-ssg-mode)

Because all routes must be determined at build time, a dynamic route must export a `getStaticPaths()` that returns an array of objects with a `params` property. Each of these objects will generate a corresponding route.

`[dog].astro` defines the dynamic `dog` parameter in its filename, so the objects returned by `getStaticPaths()` must include `dog` in their `params`. The page can then access this parameter using `Astro.params`.

src/pages/dogs/\[dog].astro

```astro
---
export function getStaticPaths() {
  return [
    { params: { dog: "clifford" }},
    { params: { dog: "rover" }},
    { params: { dog: "spot" }},
  ];
}


const { dog } = Astro.params;
---
<div>Good dog, {dog}!</div>
```

This will generate three pages: `/dogs/clifford`, `/dogs/rover`, and `/dogs/spot`, each displaying the corresponding dog name.

The filename can include multiple parameters, which must all be included in the `params` objects in `getStaticPaths()`:

src/pages/\[lang]-\[version]/info.astro

```astro
---
export function getStaticPaths() {
  return [
    { params: { lang: "en", version: "v1" }},
    { params: { lang: "fr", version: "v2" }},
  ];
}


const { lang, version } = Astro.params;
---
```

This will generate `/en-v1/info` and `/fr-v2/info`.

Parameters can be included in separate parts of the path. For example, the file `src/pages/[lang]/[version]/info.astro` with the same `getStaticPaths()` above will generate the routes `/en/v1/info` and `/fr/v2/info`.

#### Decoding `params`

[Section titled “Decoding params”](#decoding-params)

The `params` provided to the function `getStaticPaths()` function are not decoded. Use the function [`decodeURI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) when you need to decode parameter values.

src/pages/\[slug].astro

```astro
---
export function getStaticPaths() {
  return [
    { params: { slug: decodeURI("%5Bpage%5D") }}, // decodes to "[page]"
  ]
}
---
```

Learn more about [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths).

![](/houston_chef.webp) **Related recipe:** [Add i18n features](/en/recipes/i18n/)

#### Rest parameters

[Section titled “Rest parameters”](#rest-parameters)

If you need more flexibility in your URL routing, you can use a [rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters) (`[...path]`) in your `.astro` filename to match file paths of any depth:

src/pages/sequences/\[...path].astro

```astro
---
export function getStaticPaths() {
  return [
    { params: { path: "one/two/three" }},
    { params: { path: "four" }},
    { params: { path: undefined }}
  ]
}


const { path } = Astro.params;
---
```

This will generate `/sequences/one/two/three`, `/sequences/four`, and `/sequences`. (Setting the rest parameter to `undefined` allows it to match the top level page.)

Rest parameters can be used with **other named parameters**. For example, GitHub’s file viewer can be represented with the following dynamic route:

```plaintext
/[org]/[repo]/tree/[branch]/[...file]
```

In this example, a request for `/withastro/astro/tree/main/docs/public/favicon.svg` would be split into the following named parameters:

```js
{
  org: "withastro",
  repo: "astro",
  branch: "main",
  file: "docs/public/favicon.svg"
}
```

#### Example: Dynamic pages at multiple levels

[Section titled “Example: Dynamic pages at multiple levels”](#example-dynamic-pages-at-multiple-levels)

In the following example, a rest parameter (`[...slug]`) and the [`props`](/en/reference/routing-reference/#data-passing-with-props) feature of `getStaticPaths()` generate pages for slugs of different depths.

src/pages/\[...slug].astro

```astro
---
export function getStaticPaths() {
  const pages = [
    {
      slug: undefined,
      title: "Astro Store",
      text: "Welcome to the Astro store!",
    },
    {
      slug: "products",
      title: "Astro products",
      text: "We have lots of products for you",
    },
    {
      slug: "products/astro-handbook",
      title: "The ultimate Astro handbook",
      text: "If you want to learn Astro, you must read this book.",
    },
  ];


  return pages.map(({ slug, title, text }) => {
    return {
      params: { slug },
      props: { title, text },
    };
  });
}


const { title, text } = Astro.props;
---
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <p>{text}</p>
  </body>
</html>
```

### On-demand dynamic routes

[Section titled “On-demand dynamic routes”](#on-demand-dynamic-routes)

For [on-demand rendering](/en/guides/on-demand-rendering/) with an adapter, dynamic routes are defined the same way: include `[param]` or `[...path]` brackets in your file names to match arbitrary strings or paths. But because the routes are no longer built ahead of time, the page will be served to any matching route. Since these are not “static” routes, `getStaticPaths` should not be used.

For on-demand rendered routes, only one rest parameter using the spread notation may be used in the file name (e.g. `src/pages/[locale]/[...slug].astro` or `src/pages/[...locale]/[slug].astro`, but not `src/pages/[...locale]/[...slug].astro`).

src/pages/resources/\[resource]/\[id].astro

```astro
---
export const prerender = false; // Not needed in 'server' mode
const { resource, id } = Astro.params;
---
<h1>{resource}: {id}</h1>
```

This page will be served for any value of `resource` and `id`: `resources/users/1`, `resources/colors/blue`, etc.

#### Modifying the `[...slug]` example for SSR

[Section titled “Modifying the \[...slug\] example for SSR”](#modifying-the-slug-example-for-ssr)

Because SSR pages can’t use `getStaticPaths()`, they can’t receive props. The [previous example](#example-dynamic-pages-at-multiple-levels) can be adapted for SSR mode by looking up the value of the `slug` param in an object. If the route is at the root (”/”), the `slug` param will be `undefined`. If the value doesn’t exist in the object, we redirect to a 404 page.

src/pages/\[...slug].astro

```astro
---
const pages = [
  {
    slug: undefined,
    title: 'Astro Store',
    text: 'Welcome to the Astro store!',
  },
  {
    slug: 'products',
    title: 'Astro products',
    text: 'We have lots of products for you',
  },
  {
    slug: 'products/astro-handbook',
    title: 'The ultimate Astro handbook',
    text: 'If you want to learn Astro, you must read this book.',
  }
];


const { slug } = Astro.params;
const page = pages.find((page) => page.slug === slug);
if (!page) return Astro.redirect("/404");
const { title, text } = page;
---
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <p>{text}</p>
  </body>
</html>
```

## Redirects

[Section titled “Redirects”](#redirects)

Sometimes you will need to redirect your readers to a new page, either permanently because your site structure has changed or in response to an action such as logging in to an authenticated route.

You can define rules to [redirect users to permanently-moved pages](#configured-redirects) in your Astro config. Or, [redirect users dynamically](#dynamic-redirects) as they use your site.

### Configured Redirects

[Section titled “Configured Redirects”](#configured-redirects)

**Added in:** `astro@2.9.0`

You can specify a mapping of permanent redirects in your Astro config with the [`redirects`](/en/reference/configuration-reference/#redirects) value.

For internal redirects, this is a mapping of an old route path to the new route. As of Astro v5.2.0, it is also possible to redirect to external URLs that start with `http` or `https` and [can be parsed](https://developer.mozilla.org/en-US/docs/Web/API/URL/canParse_static):

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
  redirects: {
    "/old-page": "/new-page",
    "/blog": "https://example.com/blog"
  }
});
```

These redirects follow [the same priority rules as file-based routes](#route-priority-order) and will always take lower precedence than an existing page file of the same name in your project. For example, `/old-page` will not redirect to `/new-page` if your project contains the file `src/pages/old-page.astro`.

Dynamic routes are allowed as long as both the new and old routes contain the same parameters, for example:

```js
{
  "/blog/[...slug]": "/articles/[...slug]"
}
```

Using SSR or a static adapter, you can also provide an object as the value, allowing you to specify the `status` code in addition to the new `destination`:

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
  redirects: {
    "/old-page": {
      status: 302,
      destination: "/new-page"
    },
    "/news": {
      status: 302,
      destination: "https://example.com/news"
    }
  }
});
```

When running `astro build`, Astro will output HTML files with the [meta refresh](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#examples) tag by default. Supported adapters will instead write out the host’s configuration file with the redirects.

The status code is `301` by default. If building to HTML files the status code is not used by the server.

### Dynamic redirects

[Section titled “Dynamic redirects”](#dynamic-redirects)

On the `Astro` global, the `Astro.redirect` method allows you to redirect to another page dynamically. You might do this after checking if the user is logged in by getting their session from a cookie.

src/pages/account.astro

```astro
---
import { isLoggedIn } from "../utils";


const cookie = Astro.request.headers.get("cookie");


// If the user is not logged in, redirect them to the login page
if (!isLoggedIn(cookie)) {
  return Astro.redirect("/login");
}
---
```

Because Astro uses [HTML streaming](/en/guides/on-demand-rendering/#html-streaming) in on-demand rendering, redirects must be done at the page level, not inside child components.

## Rewrites

[Section titled “Rewrites”](#rewrites)

**Added in:** `astro@4.13.0`

A rewrite allows you to serve a different route without redirecting the browser to a different page. The browser will show the original address in the URL bar, but will instead display the content of the URL provided to [`Astro.rewrite()`](/en/reference/api-reference/#rewrite).

Tip

For content that has permanently moved, or to direct your user to a different page with a new URL (e.g. a user dashboard after logging in), use a [redirect](#redirects) instead.

Rewrites can be useful for showing the same content at multiple paths (e.g. `/products/shoes/men/` and `/products/men/shoes/`) without needing to maintain two different source files.

Rewrites are also useful for SEO purposes and user experience. They allow you to display content that otherwise would require redirecting your visitor to a different page or would return a 404 status. One common use of rewrites is to show the same localized content for different variants of a language.

The following example uses a rewrite to render the `/es/` version of a page when the `/es-CU/` (Cuban Spanish) URL path is visited. When a visitor navigates to the URL `/es-cu/articles/introduction`, Astro will render the content generated by the file `src/pages/es/articles/introduction.astro`.

src/pages/es-cu/articles/introduction.astro

```astro
---
return Astro.rewrite("/es/articles/introduction");
---
```

Use `context.rewrite()` in your endpoint files to reroute to a different page:

src/pages/api.js

```js
export function GET(context) {
  if (!context.locals.allowed) {
    return context.rewrite("/");
  }
}
```

If the URL passed to `Astro.rewrite()` emits a runtime error, Astro will show the overlay error in development and return a 500 status code in production. If the URL does not exist in your project, a 404 status code will be returned.

You can intentionally create a rewrite to render your `/404` page, for example to indicate that a product in your e-commerce shop is no longer available:

src/pages/\[item].astro

```astro
---
const { item } = Astro.params;


if (!itemExists(item)) {
  return Astro.rewrite("/404");
}
---
```

You can also conditionally rewrite based on an HTTP response status, for example to display a certain page on your site when visiting a URL that doesn’t exist:

src/middleware.mjs

```js
export const onRequest = async (context, next) => {
  const response = await next();
  if (response.status === 404) {
    return context.rewrite("/");
  }
  return response;
}
```

Before displaying the content from the specified rewrite path, the function `Astro.rewrite()` will trigger a new, complete rendering phase. This re-executes any middleware for the new route/request.

See the [`Astro.rewrite()` API reference](/en/reference/api-reference/#rewrite) for more information.

## Route Priority Order

[Section titled “Route Priority Order”](#route-priority-order)

It’s possible for multiple defined routes to attempt to build the same URL path. For example, all of these routes could build `/posts/create`:

* src/pages/

  * \[…slug].astro

  * posts/

    * create.astro
    * \[page].astro
    * \[pid].ts
    * \[…slug].astro

Astro needs to know which route should be used to build the page. To do so, it sorts them according to the following rules in order:

* Astro [reserved routes](#reserved-routes)
* Routes with more path segments will take precedence over less specific routes. In the example above, all routes under `/posts/` take precedence over `/[...slug].astro` at the root.
* Static routes without path parameters will take precedence over dynamic routes. E.g. `/posts/create.astro` takes precedence over all the other routes in the example.
* Dynamic routes using named parameters take precedence over rest parameters. E.g. `/posts/[page].astro` takes precedence over `/posts/[...slug].astro`.
* Pre-rendered dynamic routes take precedence over server dynamic routes.
* Endpoints take precedence over pages.
* File-based routes take precedence over redirects.
* If none of the rules above decide the order, routes are sorted alphabetically based on the default locale of your Node installation.

Given the example above, here are a few examples of how the rules will match a requested URL to the route used to build the HTML:

* `pages/posts/create.astro` - Will build only `/posts/create`
* `pages/posts/[pid].ts` - Will build `/posts/abc`, `/posts/xyz`, etc. But not `/posts/create`
* `pages/posts/[page].astro` - Will build `/posts/1`, `/posts/2`, etc. But not `/posts/create`, `/posts/abc` nor `/posts/xyz`
* `pages/posts/[...slug].astro` - Will build `/posts/1/2`, `/posts/a/b/c`, etc. But not `/posts/create`, `/posts/1`, `/posts/abc`, etc.
* `pages/[...slug].astro` - Will build `/abc`, `/xyz`, `/abc/xyz`, etc. But not `/posts/create`, `/posts/1`, `/posts/abc`, etc.

### Reserved routes

[Section titled “Reserved routes”](#reserved-routes)

Internal routes take priority over any user-defined or integration-defined routes as they are required for Astro features to work. The following are Astro’s reserved routes:

* `_astro/`: Serves all of the static assets to the client, including CSS documents, bundled client scripts, optimized images, and any Vite assets.
* `_server_islands/`: Serves the dynamic components deferred into a [server island](/en/guides/server-islands/).
* `_actions/`: Serves any defined [actions](/en/guides/actions/).

## Pagination

[Section titled “Pagination”](#pagination)

Astro supports built-in pagination for large collections of data that need to be split into multiple pages. Astro will generate common pagination properties, including previous/next page URLs, total number of pages, and more.

Paginated route names should use the same `[bracket]` syntax as a standard dynamic route. For instance, the file name `/astronauts/[page].astro` will generate routes for `/astronauts/1`, `/astronauts/2`, etc, where `[page]` is the generated page number.

You can use the `paginate()` function to generate these pages for an array of values like so:

src/pages/astronauts/\[page].astro

```astro
---
export function getStaticPaths({ paginate }) {
  const astronautPages = [
    { astronaut: "Neil Armstrong" },
    { astronaut: "Buzz Aldrin" },
    { astronaut: "Sally Ride" },
    { astronaut: "John Glenn" },
  ];


  // Generate pages from our array of astronauts, with 2 to a page
  return paginate(astronautPages, { pageSize: 2 });
}
// All paginated data is passed on the "page" prop
const { page } = Astro.props;
---
<!-- Display the current page number. `Astro.params.page` can also be used! -->
<h1>Page {page.currentPage}</h1>
<ul>
  <!-- List the array of astronaut info -->
  {page.data.map(({ astronaut }) => <li>{astronaut}</li>)}
</ul>
```

This generates the following pages, with 2 items to a page:

* `/astronauts/1` - Page 1: Displays “Neil Armstrong” and “Buzz Aldrin”
* `/astronauts/2` - Page 2: Displays “Sally Ride” and “John Glenn”

### The `page` prop

[Section titled “The page prop”](#the-page-prop)

When you use the `paginate()` function, each page will be passed its data via a `page` prop. The `page` prop has many useful properties that you can use to build pages and links between them:

```ts
interface Page<T = any> {
  /** array containing the page’s slice of data that you passed to the paginate() function */
  data: T[];
  /** metadata */
  /** the count of the first item on the page, starting from 0 */
  start: number;
  /** the count of the last item on the page, starting from 0 */
  end: number;
  /** total number of results */
  total: number;
  /** the current page number, starting from 1 */
  currentPage: number;
  /** number of items per page (default: 10) */
  size: number;
  /** number of last page */
  lastPage: number;
  url: {
    /** url of the current page */
    current: string;
    /** url of the previous page (if there is one) */
    prev: string | undefined;
    /** url of the next page (if there is one) */
    next: string | undefined;
    /** url of the first page (if the current page is not the first page) */
    first: string | undefined;
    /** url of the last page (if the current page in not the last page) */
    last: string | undefined;
  };
}
```

The following example displays current information for the page along with links to navigate between pages:

src/pages/astronauts/\[page].astro

```astro
---
// Paginate same list of `{ astronaut }` objects as the previous example
export function getStaticPaths({ paginate }) { /* ... */ }
const { page } = Astro.props;
---
<h1>Page {page.currentPage}</h1>
<ul>
  {page.data.map(({ astronaut }) => <li>{astronaut}</li>)}
</ul>
{page.url.first ? <a href={page.url.first}>First</a> : null}
{page.url.prev ? <a href={page.url.prev}>Previous</a> : null}
{page.url.next ? <a href={page.url.next}>Next</a> : null}
{page.url.last ? <a href={page.url.last}>Last</a> : null}
```

Learn more about [the pagination `page` prop](/en/reference/routing-reference/#the-pagination-page-prop).

### Nested Pagination

[Section titled “Nested Pagination”](#nested-pagination)

A more advanced use-case for pagination is **nested pagination.** This is when pagination is combined with other dynamic route params. You can use nested pagination to group your paginated collection by some property or tag.

For example, if you want to group your paginated Markdown posts by some tag, you would use nested pagination by creating a `/src/pages/[tag]/[page].astro` page that would match the following URLS:

* `/red/1` (tag=red)
* `/red/2` (tag=red)
* `/blue/1` (tag=blue)
* `/green/1` (tag=green)

Nested pagination works by returning an array of `paginate()` results from `getStaticPaths()`, one for each grouping.

In the following example, we will implement nested pagination to build the URLs listed above:

src/pages/\[tag]/\[page].astro

```astro
---
export function getStaticPaths({ paginate }) {
  const allTags = ["red", "blue", "green"];
  const allPosts = Object.values(import.meta.glob("../pages/post/*.md", { eager: true }));
  // For every tag, return a `paginate()` result.
  // Make sure that you pass `{ params: { tag }}` to `paginate()`
  // so that Astro knows which tag grouping the result is for.
  return allTags.flatMap((tag) => {
    const filteredPosts = allPosts.filter((post) => post.frontmatter.tag === tag);
    return paginate(filteredPosts, {
      params: { tag },
      pageSize: 10
    });
  });
}


const { page } = Astro.props;
const params = Astro.params;
```

## Excluding pages

[Section titled “Excluding pages”](#excluding-pages)

You can exclude pages or directories within `src/pages` from being built by prefixing their names with an underscore (`_`). Files with the `_` prefix won’t be recognized by the router and won’t be placed into the `dist/` directory.

You can use this to temporarily disable pages, and also to put tests, utilities, and components in the same folder as their related pages.

In this example, only `src/pages/index.astro` and `src/pages/projects/project1.md` will be built as page routes and HTML files.

* src/pages/

  * \_hidden-directory/

    * page1.md
    * page2.md

  * \_hidden-page.astro

  * **index.astro**

  * projects/

    * \_SomeComponent.astro
    * \_utils.js
    * **project1.md**

# Server islands

> Combine high performance static HTML with dynamic server-rendered content.

Server islands allow you to on-demand render dynamic or personalized “islands” individually, without sacrificing the performance of the rest of the page.

This means your visitor will see the most important parts of your page sooner, and allows your main content to be more aggressively cached, providing faster performance.

## Server island components

[Section titled “Server island components”](#server-island-components)

A server island is a normal server-rendered [Astro component](/en/basics/astro-components/) that is instructed to delay rendering until its contents are available.

Your page will be rendered immediately with any specified [fallback content as a placeholder](#server-island-fallback-content). Then, the component’s own contents are fetched on the client and displayed when available.

With [an adapter installed](/en/guides/on-demand-rendering/#server-adapters) to perform the delayed rendering, add the [`server:defer` directive](/en/reference/directives-reference/#server-directives) to any component on your page to turn it into its own island:

src/pages/index.astro

```astro
---
import Avatar from '../components/Avatar.astro';
---
<Avatar server:defer />
```

These components can do [anything you normally would in an on-demand rendered page](/en/guides/on-demand-rendering/#on-demand-rendering-features) using an adapter, such as fetch content, and access cookies:

src/components/Avatar.astro

```astro
---
import { getUserAvatar } from '../sessions';
const userSession = Astro.cookies.get('session');
const avatarURL = await getUserAvatar(userSession);
---
<img alt="User avatar" src={avatarURL} />
```

### Passing props to server islands

[Section titled “Passing props to server islands”](#passing-props-to-server-islands)

Props provided to server island components must be [serializable](https://developer.mozilla.org/en-US/docs/Glossary/Serialization): able to be translated into a format suitable for transfer over a network, or storage. Additionally, Astro does not serialize every type of serializable data structure. Therefore, there are some limitations on what can be passed as props to a server island.

Notably, functions cannot be passed to components marked with `server:defer` as they cannot be serialized. Objects with circular references are also not serializable.

The following prop types are supported: plain object, `number`, `string`, `Array`, `Map`, `Set`, `RegExp`, `Date`, `BigInt`, `URL`, `Uint8Array`, `Uint16Array`, `Uint32Array`, and `Infinity`

## Server island fallback content

[Section titled “Server island fallback content”](#server-island-fallback-content)

When using the `server:defer` attribute on a component to delay its rendering, you can “slot” in default loading content using the included named `"fallback"` slot.

Your fallback content will be rendered along with the rest of the page initially on page load and will be replaced with your component’s content when available.

To add fallback content, add `slot="fallback"` on a child (other components or HTML elements) passed to your server island component:

```astro
---
import Avatar from '../components/Avatar.astro';
import GenericAvatar from '../components/GenericAvatar.astro';
---
<Avatar server:defer>
  <GenericAvatar slot="fallback" />
</Avatar>
```

This fallback content can be things like:

* A generic avatar instead of the user’s own.
* Placeholder UI such as custom messages.
* Loading indicators such as spinners.

## How it works

[Section titled “How it works”](#how-it-works)

Server island implementation happens mostly at build-time where component content is swapped out for a small script.

Each of the islands marked with `server:defer` is split off into its own special route which the script fetches at run time. When Astro builds your site it will omit the component and inject a script in its place, and any content you’ve marked with `slot="fallback"`.

When the page loads in the browser, these components will be requested to a special endpoint that renders them and returns the HTML. This means that users will see the most critical parts of the page instantly. Fallback content will be visible for a short amount of time before the dynamic islands are then loaded.

Each island is loaded independently from the rest. This means a slower island won’t delay the rest of your personalized content from being available.

This rendering pattern was built to be portable. It does not depend on any server infrastructure so it will work with any host you have, from a Node.js server in a Docker container to the serverless provider of your choice.

## Caching

[Section titled “Caching”](#caching)

The data for server islands is retrieved via a `GET` request, passing props as an encrypted string in the URL query. This allows caching data with the [`Cache-Control` HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) using standard `Cache-Control` directives.

However, [the browser limits URLs to a maximum length of 2048 bytes](https://chromium.googlesource.com/chromium/src/+/master/docs/security/url_display_guidelines/url_display_guidelines.md#url-length) for practical reasons and to avoid causing denial-of-service problems. If your query string causes your URL to exceed this limit, Astro will instead send a `POST` request that contains all props in the body.

`POST` requests are not cached by browsers because they are used to submit data, and could cause data integrity or security issues. Therefore, any existing caching logic in your project will break. Whenever possible, pass only necessary props to your server islands and avoid sending entire data objects and arrays to keep your query small.

## Accessing the page URL in a server island

[Section titled “Accessing the page URL in a server island”](#accessing-the-page-url-in-a-server-island)

In most cases you, your server island component can get information about the page rendering it by [passing props](/en/basics/astro-components/#component-props) like in normal components.

However, server islands run in their own isolated context outside of the page request. `Astro.url` and `Astro.request.url` in a server island component both return a URL that looks like `/_server-islands/Avatar` instead of the current page’s URL in the browser. Additionally, if you are prerendering the page you will not have access to information such as query parameters in order to pass as props.

To access information from the page’s URL, you can check the [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header, which will contain the address of the page that is loading the island in the browser:

```astro
---
const referer = Astro.request.headers.get('Referer');
const url = new URL(referer);
const productId = url.searchParams.get('product');
---
```

## Reusing the encryption key

[Section titled “Reusing the encryption key”](#reusing-the-encryption-key)

Astro uses [cryptography](https://developer.mozilla.org/en-US/docs/Glossary/Cryptography) to encrypt props passed to server islands, protecting sensitive data from accidental exposure. This encryption relies on a new, random key that is generated on each build and embedded in the server bundle.

Most deploy hosts will handle keeping your front end and back end in sync automatically. However, you may need a constant encryption key if you are using rolling deployments, multi-region hosting or a CDN that caches pages containing server islands.

In environments with rolling deployments (e.g., Kubernetes) where your frontend assets (which encrypt props) and your backend functions (which decrypt props) may be temporarily using different keys, or when a CDN is still serving pages built with an old key, encrypted props passed to your server island cannot be decrypted.

In these situations, use the Astro CLI to generate a reusable, encoded encryption key to set as an environment variable in your build environment:

```shell
astro create-key
```

Use this value to configure the `ASTRO_KEY` environment variable (e.g. in a `.env` file) and include it in your CI/CD or host’s build settings. This ensures the same key is always reused in the generated bundle so that encryption and decryption remain in sync.

# Sessions

> Share data between requests for on-demand rendered pages.

**Added in:** `astro@5.7.0`

Sessions are used to share data between requests for [on-demand rendered pages](/en/guides/on-demand-rendering/).

Unlike [`cookies`](/en/guides/on-demand-rendering/#cookies), sessions are stored on the server, so you can store larger amounts of data without worrying about size limits or security issues. They are useful for storing things like user data, shopping carts, and form state, and they work without any client-side JavaScript:

src/components/CartButton.astro

```astro
---
export const prerender = false; // Not needed with 'server' output
const cart = await Astro.session?.get('cart');
---


<a href="/checkout">🛒 {cart?.length ?? 0} items</a>
```

## Configuring sessions

[Section titled “Configuring sessions”](#configuring-sessions)

Sessions require a storage driver to store the session data. The [Node](/en/guides/integrations-guide/node/#sessions), [Cloudflare](/en/guides/integrations-guide/cloudflare/#sessions), and [Netlify](/en/guides/integrations-guide/netlify/#sessions) adapters automatically configure a default driver for you, but other adapters currently require you to [specify a driver manually](/en/reference/configuration-reference/#sessiondriver).

astro.config.mjs

```diff
  {
    adapter: vercel(),
    session: {
+      driver: "redis",
    },
  }
```

See [the `session` configuration option](/en/reference/configuration-reference/#session-options) for more details on setting a storage driver, and other configurable options.

## Interacting with session data

[Section titled “Interacting with session data”](#interacting-with-session-data)

The [`session` object](/en/reference/api-reference/#session) allows you to interact with the stored user state (e.g. adding items to a shopping cart) and the session ID (e.g. deleting the session ID cookie when logging out). The object is accessible as `Astro.session` in your Astro components and pages and as `context.session` object in API endpoints, middleware, and actions.

The session is generated automatically when it is first used and can be regenerated at any time with [`session.regenerate()`](/en/reference/api-reference/#regenerate) or destroyed with [`session.destroy()`](/en/reference/api-reference/#destroy).

For many use cases, you will only need to use [`session.get()`](/en/reference/api-reference/#get) and [`session.set()`](/en/reference/api-reference/#set).

See [the Sessions API reference](/en/reference/api-reference/#session) for more details.

### Astro components and pages

[Section titled “Astro components and pages”](#astro-components-and-pages)

In `.astro` components and pages, you can access the session object via the global `Astro` object. For example, to display the number of items in a shopping cart:

src/components/CartButton.astro

```astro
---
export const prerender = false; // Not needed with 'server' output
const cart = await Astro.session?.get('cart');
---


<a href="/checkout">🛒 {cart?.length ?? 0} items</a>
```

### API endpoints

[Section titled “API endpoints”](#api-endpoints)

In API endpoints, the session object is available on the `context` object. For example, to add an item to a shopping cart:

src/pages/api/addToCart.ts

```ts
export async function POST(context: APIContext) {
  const cart = await context.session?.get('cart') || [];
  const data = await context.request.json<{ item: string }>();
  if(!data?.item) {
    return new Response('Item is required', { status: 400 });
  }
  cart.push(data.item);
  await context.session?.set('cart', cart);
  return Response.json(cart);
}
```

### Actions

[Section titled “Actions”](#actions)

In actions, the session object is available on the `context` object. For example, to add an item to a shopping cart:

src/actions/addToCart.ts

```ts
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  addToCart: defineAction({
    input: z.object({ productId: z.string() }),
    handler: async (input, context) => {
      const cart = await context.session?.get('cart');
      cart.push(input.productId);
      await context.session?.set('cart', cart);
      return cart;
    },
  }),
};
```

### Middleware

[Section titled “Middleware”](#middleware)

Note

Sessions are not supported in edge middleware.

In middleware, the session object is available on the `context` object. For example, to set the last visit time in the session:

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';


export const onRequest = defineMiddleware(async (context, next) => {
  context.session?.set('lastVisit', new Date());
  return next();
});
```

## Session data types

[Section titled “Session data types”](#session-data-types)

By default session data is untyped, and you can store arbitrary data in any key. Values are serialized and deserialized using [devalue](https://github.com/Rich-Harris/devalue), which is the same library used in content collections and actions. This means that supported types are the same, and include strings, numbers, `Date`, `Map`, `Set`, `URL`, arrays, and plain objects.

You can optionally [define TypeScript types](/en/guides/typescript/#extending-global-types) for your session data by creating a `src/env.d.ts` file and adding a declaration for the `App.SessionData` type:

src/env.d.ts

```ts
declare namespace App {
  interface SessionData {
    user: {
      id: string;
      name: string;
    };
    cart: string[];
  }
}
```

This will allow you to access the session data with type-checking and auto-completion in your editor:

src/components/CartButton.astro

```ts
---
const cart = await Astro.session?.get('cart');
// const cart: string[] | undefined


const something = await Astro.session?.get('something');
// const something: any


Astro.session?.set('user', { id: 1, name: 'Houston' });
// Error: Argument of type '{ id: number; name: string }' is not assignable to parameter of type '{ id: string; name: string; }'.
---
```

Caution

This is only used for type-checking and does not affect the runtime behavior of the session. Take extra care if you change the type when users have stored data in the session, as this could cause runtime errors.

# Styles and CSS

> Learn how to style components in Astro with scoped styles, external CSS, and tooling like Sass and PostCSS.

Astro was designed to make styling and writing CSS a breeze. Write your own CSS directly inside of an Astro component or import your favorite CSS library like [Tailwind](https://tailwindcss.com/docs/installation/framework-guides/astro). Advanced styling languages like [Sass](https://sass-lang.com/) and [Less](https://lesscss.org/) are also supported.

## Styling in Astro

[Section titled “Styling in Astro”](#styling-in-astro)

Styling an Astro component is as easy as adding a `<style>` tag to your component or page template. When you place a `<style>` tag inside of an Astro component, Astro will detect the CSS and handle your styles for you, automatically.

src/components/MyComponent.astro

```astro
<style>
  h1 { color: red; }
</style>
```

### Scoped Styles

[Section titled “Scoped Styles”](#scoped-styles)

Astro `<style>` CSS rules are automatically **scoped by default**. Scoped styles are compiled behind-the-scenes to only apply to HTML written inside of that same component. The CSS that you write inside of an Astro component is automatically encapsulated inside of that component.

This CSS:

src/pages/index.astro

```astro
<style>
  h1 {
    color: red;
  }


  .text {
    color: blue;
  }
</style>
```

Compiles to this:

```astro
<style>
  h1[data-astro-cid-hhnqfkh6] {
     color: red;
  }


  .text[data-astro-cid-hhnqfkh6] {
    color: blue;
  }
</style>
```

Scoped styles don’t leak and won’t impact the rest of your site. In Astro, it is okay to use low-specificity selectors like `h1 {}` or `p {}` because they will be compiled with scopes in the final output.

Scoped styles also won’t apply to other Astro components contained inside of your template. If you need to style a child component, consider wrapping that component in a `<div>` (or other element) that you can then style.

The specificity of scoped styles is preserved, allowing them to work consistently alongside other CSS files or CSS libraries while still preserving the exclusive boundaries that prevent styles from applying outside the component.

### Global Styles

[Section titled “Global Styles”](#global-styles)

While we recommend scoped styles for most components, you may eventually find a valid reason to write global, unscoped CSS. You can opt-out of automatic CSS scoping with the `<style is:global>` attribute.

src/components/GlobalStyles.astro

```astro
<style is:global>
  /* Unscoped, delivered as-is to the browser.
     Applies to all <h1> tags on your site. */
  h1 { color: red; }
</style>
```

You can also mix global & scoped CSS rules together in the same `<style>` tag using the `:global()` selector. This becomes a powerful pattern for applying CSS styles to children of your component.

src/components/MixedStyles.astro

```astro
<style>
  /* Scoped to this component, only. */
  h1 { color: red; }
  /* Mixed: Applies to child `h1` elements only. */
  article :global(h1) {
    color: blue;
  }
</style>
<h1>Title</h1>
<article><slot /></article>
```

This is a great way to style things like blog posts, or documents with CMS-powered content where the contents live outside of Astro. But be careful: components whose appearance differs based on whether or not they have a certain parent component can become difficult to troubleshoot.

Scoped styles should be used as often as possible. Global styles should be used only as-needed.

### Combining classes with `class:list`

[Section titled “Combining classes with class:list”](#combining-classes-with-classlist)

If you need to combine classes on an element dynamically, you can use the `class:list` utility attribute in `.astro` files.

src/components/ClassList.astro

```astro
---
const { isRed } = Astro.props;
---
<!-- If `isRed` is truthy, class will be "box red". -->
<!-- If `isRed` is falsy, class will be "box". -->
<div class:list={['box', { red: isRed }]}><slot /></div>


<style>
  .box { border: 1px solid blue; }
  .red { border-color: red; }
</style>
```

See our [directives reference](/en/reference/directives-reference/#classlist) page to learn more about `class:list`.

### CSS Variables

[Section titled “CSS Variables”](#css-variables)

**Added in:** `astro@0.21.0`

The Astro `<style>` can reference any CSS variables available on the page. You can also pass CSS variables directly from your component frontmatter using the `define:vars` directive.

src/components/DefineVars.astro

```astro
---
const foregroundColor = "rgb(221 243 228)";
const backgroundColor = "rgb(24 121 78)";
---
<style define:vars={{ foregroundColor, backgroundColor }}>
  h1 {
    background-color: var(--backgroundColor);
    color: var(--foregroundColor);
  }
</style>
<h1>Hello</h1>
```

See our [directives reference](/en/reference/directives-reference/#definevars) page to learn more about `define:vars`.

### Passing a `class` to a child component

[Section titled “Passing a class to a child component”](#passing-a-class-to-a-child-component)

In Astro, HTML attributes like `class` do not automatically pass through to child components.

Instead, accept a `class` prop in the child component and apply it to the root element. When destructuring, you must rename it, because `class` is a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words) in JavaScript.

Using the default scoped style strategy, you must also pass the `data-astro-cid-*` attribute. You can do this by passing the `...rest` of the props to the component. If you have changed `scopedStyleStrategy` to `'class'` or `'where'`, the `...rest` prop is not necessary.

src/components/MyComponent.astro

```astro
---
const { class: className, ...rest } = Astro.props;
---
<div class={className} {...rest}>
  <slot/>
</div>
```

src/pages/index.astro

```astro
---
import MyComponent from "../components/MyComponent.astro"
---
<style>
  .red {
    color: red;
  }
</style>
<MyComponent class="red">This will be red!</MyComponent>
```

Scoped styles from parent components

Because the `data-astro-cid-*` attribute includes the child in its parent’s scope, it is possible for styles to cascade from parent to child. To avoid this having unintended side effects, ensure you use unique class names in the child component.

### Inline styles

[Section titled “Inline styles”](#inline-styles)

You can style HTML elements inline using the `style` attribute. This can be a CSS string or an object of CSS properties:

src/pages/index.astro

```astro
// These are equivalent:
<p style={{ color: "brown", textDecoration: "underline" }}>My text</p>
<p style="color: brown; text-decoration: underline;">My text</p>
```

## External Styles

[Section titled “External Styles”](#external-styles)

There are two ways to resolve external global stylesheets: an ESM import for files located within your project source, and an absolute URL link for files in your `public/` directory, or hosted outside of your project.

Read more about using [static assets](/en/guides/imports/) located in `public/` or `src/`.

### Import a local stylesheet

[Section titled “Import a local stylesheet”](#import-a-local-stylesheet)

Using an npm package?

You may need to update your `astro.config` when importing from npm packages. See the [“import stylesheets from an npm package” section](#import-a-stylesheet-from-an-npm-package) below.

You can import stylesheets in your Astro component frontmatter using ESM import syntax. CSS imports work like [any other ESM import in an Astro component](/en/basics/astro-components/#the-component-script), which should be referenced as **relative to the component** and must be written at the **top** of your component script, with any other imports.

src/pages/index.astro

```astro
---
// Astro will bundle and optimize this CSS for you automatically
// This also works for preprocessor files like .scss, .styl, etc.
import '../styles/utils.css';
---
<html><!-- Your page here --></html>
```

CSS `import` via ESM are supported inside of any JavaScript file, including JSX components like React & Preact. This can be useful for writing granular, per-component styles for your React components.

### Import a stylesheet from an npm package

[Section titled “Import a stylesheet from an npm package”](#import-a-stylesheet-from-an-npm-package)

You may also need to load stylesheets from an external npm package. This is especially common for utilities like [Open Props](https://open-props.style/). If your package **recommends using a file extension** (i.e. `package-name/styles.css` instead of `package-name/styles`), this should work like any local stylesheet:

src/pages/random-page.astro

```astro
---
import 'package-name/styles.css';
---
<html><!-- Your page here --></html>
```

If your package **does not suggest using a file extension** (i.e. `package-name/styles`), you’ll need to update your Astro config first!

Say you are importing a CSS file from `package-name` called `normalize` (with the file extension omitted). To ensure we can prerender your page correctly, add `package-name` to [the `vite.ssr.noExternal` array](https://vite.dev/config/ssr-options.html#ssr-noexternal):

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
  vite: {
    ssr: {
+      noExternal: ['package-name'],
    }
  }
})
```

Note

This is a [Vite-specific setting](https://vite.dev/config/ssr-options.html#ssr-noexternal) that does *not* relate to (or require) [Astro SSR](/en/guides/on-demand-rendering/).

Now, you are free to import `package-name/normalize`. This will be bundled and optimized by Astro like any other local stylesheet.

src/pages/random-page.astro

```astro
---
import 'package-name/normalize';
---
<html><!-- Your page here --></html>
```

### Load a static stylesheet via “link” tags

[Section titled “Load a static stylesheet via “link” tags”](#load-a-static-stylesheet-via-link-tags)

You can also use the `<link>` element to load a stylesheet on the page. This should be an absolute URL path to a CSS file located in your `/public` directory, or an URL to an external website. Relative `<link>` href values are not supported.

src/pages/index.astro

```astro
<head>
  <!-- Local: /public/styles/global.css -->
  <link rel="stylesheet" href="/styles/global.css" />
  <!-- External -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.24.1/themes/prism-tomorrow.css" />
</head>
```

Because this approach uses the `public/` directory, it skips the normal CSS processing, bundling and optimizations that are provided by Astro. If you need these transformations, use the [Import a Stylesheet](#import-a-local-stylesheet) method above.

## Cascading Order

[Section titled “Cascading Order”](#cascading-order)

Astro components will sometimes have to evaluate multiple sources of CSS. For example, your component might import a CSS stylesheet, include its own `<style>` tag, *and* be rendered inside a layout that imports CSS.

When conflicting CSS rules apply to the same element, browsers first use *specificity* and then *order of appearance* to determine which value to show.

If one rule is more *specific* than another, no matter where the CSS rule appears, its value will take precedence:

src/components/MyComponent.astro

```astro
<style>
  h1 { color: red }
  div > h1 {
    color: purple
  }
</style>
<div>
  <h1>
    This header will be purple!
  </h1>
</div>
```

If two rules have the same specificity, then the *order of appearance* is evaluated, and the last rule’s value will take precedence:

src/components/MyComponent.astro

```astro
<style>
  h1 { color: purple }
  h1 { color: red }
</style>
<div>
  <h1>
    This header will be red!
  </h1>
</div>
```

Astro CSS rules are evaluated in this order of appearance:

* **`<link>` tags in the head** (lowest precedence)
* **imported styles**
* **scoped styles** (highest precedence)

### Scoped Styles

[Section titled “Scoped Styles”](#scoped-styles-1)

Depending on your chosen value for [`scopedStyleStrategy`](/en/reference/configuration-reference/#scopedstylestrategy), scoped styles may or may not increase the [CLASS column specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity#class_column).

However, [scoped styles](#scoped-styles) will always come last in the order of appearance. These styles will therefore take precedence over other styles of the same specificity. For example, if you import a stylesheet that conflicts with a scoped style, the scoped style’s value will apply:

src/components/make-it-purple.css

```css
h1 {
  color: purple;
}
```

src/components/MyComponent.astro

```astro
---
import "./make-it-purple.css"
---
<style>
  h1 { color: red }
</style>
<div>
  <h1>
    This header will be red!
  </h1>
</div>
```

Scoped styles will be overwritten if the imported style is more specific. The style with a higher specificity will take precedence over the scoped style:

src/components/make-it-purple.css

```css
#intro {
  color: purple;
}
```

src/components/MyComponent.astro

```astro
---
import "./make-it-purple.css"
---
<style>
  h1 { color: red }
</style>
<div>
  <h1 id="intro">
    This header will be purple!
  </h1>
</div>
```

### Import Order

[Section titled “Import Order”](#import-order)

When importing multiple stylesheets in an Astro component, the CSS rules are evaluated in the order that they are imported. A higher specificity will always determine which styles to show, no matter when the CSS is evaluated. But, when conflicting styles have the same specificity, the *last one imported* wins:

src/components/make-it-purple.css

```css
div > h1 {
  color: purple;
}
```

src/components/make-it-green.css

```css
div > h1 {
  color: green;
}
```

src/components/MyComponent.astro

```astro
---
import "./make-it-green.css"
import "./make-it-purple.css"
---
<style>
  h1 { color: red }
</style>
<div>
  <h1>
    This header will be purple!
  </h1>
</div>
```

While `<style>` tags are scoped and only apply to the component that declares them, *imported* CSS can “leak”. Importing a component applies any CSS it imports, even if the component is never used:

src/components/PurpleComponent.astro

```astro
---
import "./make-it-purple.css"
---
<div>
  <h1>I import purple CSS.</h1>
</div>
```

src/components/MyComponent.astro

```astro
---
import "./make-it-green.css"
import PurpleComponent from "./PurpleComponent.astro";
---
<style>
  h1 { color: red }
</style>
<div>
  <h1>
    This header will be purple!
  </h1>
</div>
```

Tip

A common pattern in Astro is to import global CSS inside a [Layout component](/en/basics/layouts/). Be sure to import the Layout component before other imports so that it has the lowest precedence.

### Link Tags

[Section titled “Link Tags”](#link-tags)

Style sheets loaded via [link tags](#load-a-static-stylesheet-via-link-tags) are evaluated in order, before any other styles in an Astro file. Therefore, these styles will have lower precedence than imported stylesheets and scoped styles:

src/pages/index.astro

```astro
---
import "../components/make-it-purple.css"
---


<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
    <link rel="stylesheet" href="/styles/make-it-blue.css" />
  </head>
  <body>
    <div>
      <h1>This will be purple</h1>
    </div>
  </body>
</html>
```

## Tailwind

[Section titled “Tailwind”](#tailwind)

Astro comes with support for adding popular CSS libraries, tools, and frameworks to your project like [Tailwind](https://tailwindcss.com) and more!

Astro supports both Tailwind 3 and 4. You can [add Tailwind 4 support through a Vite plugin](#add-tailwind-4) to your project with a CLI command, or install legacy dependencies manually to add [Tailwind 3 support through an Astro integration](#legacy-tailwind-3-support).

To [upgrade your Astro project from Tailwind 3 to 4](#upgrade-from-tailwind-3) you will need to both add Tailwind 4 support, and remove legacy Tailwind 3 support.

### Add Tailwind 4

[Section titled “Add Tailwind 4”](#add-tailwind-4)

In Astro `>=5.2.0`, use the `astro add tailwind` command for your package manager to install the official Vite Tailwind plugin. To add Tailwind 4 support to earlier versions of Astro, follow the [instructions in the Tailwind docs](https://tailwindcss.com/docs/installation/framework-guides/astro) to add the `@tailwindcss/vite` Vite plugin manually.

* npm

  ```shell
  npx astro add tailwind
  ```

* pnpm

  ```shell
  pnpm astro add tailwind
  ```

* Yarn

  ```shell
  yarn astro add tailwind
  ```

Then, import `tailwindcss` into `src/styles/global.css` (or another CSS file of your choosing) to make Tailwind classes available to your Astro project. This file including the import will be created by default if you used the `astro add tailwind` command to install the Vite plugin.

src/styles/global.css

```css
@import "tailwindcss";
```

Import this file in the pages where you want Tailwind to apply. This is often done in a layout component so that Tailwind styles can be used on all pages sharing that layout:

src/layouts/Layout.astro

```astro
---
import "../styles/global.css";
---
```

### Upgrade from Tailwind 3

[Section titled “Upgrade from Tailwind 3”](#upgrade-from-tailwind-3)

Follow the steps to update an existing Astro project using Tailwind v3 (using the `@astrojs/tailwind` integration) to Tailwind 4 (using [the `@tailwindcss/vite` plugin](https://tailwindcss.com/docs/installation/framework-guides/astro)).

1. [Add Tailwind 4 support to your project](#add-tailwind-4) through the CLI for the latest version of Astro, or by adding the Vite plugin manually.

2. Uninstall the `@astrojs/tailwind` integration from your project:

   * npm

     ```shell
     npm uninstall @astrojs/tailwind
     ```

   * pnpm

     ```shell
     pnpm remove @astrojs/tailwind
     ```

   * Yarn

     ```shell
     yarn remove @astrojs/tailwind
     ```

3. Remove the `@astrojs/tailwind` integration from your `astro.config.mjs`:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   -import tailwind from '@astrojs/tailwind';


   export default defineConfig({
     // ...
     integrations: [tailwind()],
     // ...
   });
   ```

4. Then, upgrade your project according to [Tailwind’s v4 upgrade guide](https://tailwindcss.com/docs/upgrade-guide#changes-from-v3).

### Legacy Tailwind 3 support

[Section titled “Legacy Tailwind 3 support”](#legacy-tailwind-3-support)

To add (or keep) support for Tailwind 3, you will need to have both `tailwindcss@3` and the official Astro Tailwind integration `@astrojs/tailwind` installed. Installing these dependencies manually is only used for legacy Tailwind 3 compatibility, and is not required for Tailwind 4. You will also need a [legacy Tailwind configuration](https://v3.tailwindcss.com/docs/configuration#creating-your-configuration-file):

1. Install Tailwind and the Astro Tailwind integration to your project dependencies using your preferred package manager:

   * npm

     ```shell
     npm install tailwindcss@3 @astrojs/tailwind
     ```

   * pnpm

     ```shell
     pnpm add tailwindcss@3 @astrojs/tailwind
     ```

   * Yarn

     ```shell
     yarn add tailwindcss@3 @astrojs/tailwind
     ```

2. Import the integration to your `astro.config.mjs` file, and add it to your `integrations[]` array:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import tailwind from '@astrojs/tailwind';


   export default defineConfig({
     // ...
     integrations: [tailwind()],
     // ...
   });
   ```

3. Create a `tailwind.config.mjs` file in your project’s root directory. You can use the following command to generate a basic configuration file for you:

   * npm

     ```shell
     npx tailwindcss init
     ```

   * pnpm

     ```shell
     pnpm dlx tailwindcss init
     ```

   * Yarn

     ```shell
     yarn dlx tailwindcss init
     ```

4. Add the following basic configuration to your `tailwind.config.mjs` file:

   tailwind.config.mjs

   ```diff
   /** @type {import('tailwindcss').Config} */
   export default {
   +  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
     theme: {
       extend: {},
     },
     plugins: [],
   };
   ```

![](/houston_chef.webp) **Related recipe:** [Style rendered Markdown with Tailwind Typography](/en/recipes/tailwind-rendered-markdown/)

## CSS Preprocessors

[Section titled “CSS Preprocessors”](#css-preprocessors)

Astro supports CSS preprocessors such as [Sass](https://sass-lang.com/), [Stylus](https://stylus-lang.com/), and [Less](https://lesscss.org/) through [Vite](https://vite.dev/guide/features.html#css-pre-processors).

### Sass and SCSS

[Section titled “Sass and SCSS”](#sass-and-scss)

```shell
npm install sass
```

Use `<style lang="scss">` or `<style lang="sass">` in `.astro` files.

### Stylus

[Section titled “Stylus”](#stylus)

```shell
npm install stylus
```

Use `<style lang="styl">` or `<style lang="stylus">` in `.astro` files.

### Less

[Section titled “Less”](#less)

```shell
npm install less
```

Use `<style lang="less">` in `.astro` files.

### LightningCSS

[Section titled “LightningCSS”](#lightningcss)

```shell
npm install lightningcss
```

Update your `vite` configuration in `astro.config.mjs`:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config'


export default defineConfig({
+  vite: {
+    css: {
+      transformer: "lightningcss",
+    },
+  },
})
```

### In framework components

[Section titled “In framework components”](#in-framework-components)

You can also use all of the above CSS preprocessors within JS frameworks as well! Be sure to follow the patterns each framework recommends:

* **React** / **Preact**: `import Styles from './styles.module.scss';`
* **Vue**: `<style lang="scss">`
* **Svelte**: `<style lang="scss">`

## PostCSS

[Section titled “PostCSS”](#postcss)

Astro comes with PostCSS included as part of [Vite](https://vite.dev/guide/features.html#postcss). To configure PostCSS for your project, create a `postcss.config.cjs` file in the project root. You can import plugins using `require()` after installing them (for example `npm install autoprefixer`).

postcss.config.cjs

```diff
module.exports = {
  plugins: [
    +require('autoprefixer'),
    +require('cssnano'),
  ],
};
```

## Frameworks and Libraries

[Section titled “Frameworks and Libraries”](#frameworks-and-libraries)

### 📘 React / Preact

[Section titled “📘 React / Preact”](#-react--preact)

`.jsx` files support both global CSS and CSS Modules. To enable the latter, use the `.module.css` extension (or `.module.scss`/`.module.sass` if using Sass).

src/components/MyReactComponent.jsx

```jsx
import './global.css'; // include global CSS
import Styles from './styles.module.css'; // Use CSS Modules (must end in `.module.css`, `.module.scss`, or `.module.sass`!)
```

### 📗 Vue

[Section titled “📗 Vue”](#-vue)

Vue in Astro supports the same methods as `vue-loader` does:

* [vue-loader - Scoped CSS](https://vue-loader.vuejs.org/guide/scoped-css.html)
* [vue-loader - CSS Modules](https://vue-loader.vuejs.org/guide/css-modules.html)

### 📕 Svelte

[Section titled “📕 Svelte”](#-svelte)

Svelte in Astro also works exactly as expected: [Svelte Styling Docs](https://svelte.dev/docs#component-format-style).

## Markdown Styling

[Section titled “Markdown Styling”](#markdown-styling)

Any Astro styling methods are available to a [Markdown layout component](/en/basics/layouts/#markdown-layouts), but different methods will have different styling effects on your page.

You can apply global styles to your Markdown content by adding [imported stylesheets](#external-styles) to the layout that wraps your page content. It is also possible to style your Markdown with [`<style is:global>` tags](#global-styles) in the layout component. Note that any styles added are subject to [Astro’s cascading order](#cascading-order), and you should check your rendered page carefully to ensure your styles are being applied as intended.

You can also add CSS integrations including [Tailwind](/en/recipes/tailwind-rendered-markdown/). If you are using Tailwind, the [typography plugin](https://tailwindcss.com/docs/typography-plugin) can be useful for styling Markdown.

## Production

[Section titled “Production”](#production)

### Bundle control

[Section titled “Bundle control”](#bundle-control)

When Astro builds your site for production deployment, it minifies and combines your CSS into chunks. Each page on your site gets its own chunk, and additionally, CSS that is shared between multiple pages is further split off into their own chunks for reuse.

However, when you have several pages sharing styles, some shared chunks can become really small. If all of them were sent separately, it would lead to many stylesheets requests and affect site performance. Therefore, by default Astro will link only those in your HTML above 4kB in size as `<link rel="stylesheet">` tags, while inlining smaller ones into `<style type="text/css">`. This approach provides a balance between the number of additional requests and the volume of CSS that can be cached between pages.

You can configure the size at which stylesheets will be linked externally (in bytes) using the `assetsInlineLimit` vite build option. Note that this option affects script and image inlining as well.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  vite: {
    build: {
      assetsInlineLimit: 1024,
    }
  };
});
```

If you would rather all project styles remain external, you can configure the `inlineStylesheets` build option.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  build: {
    inlineStylesheets: 'never'
  }
});
```

You can also set this option to `'always'` which will inline all stylesheets.

## Advanced

[Section titled “Advanced”](#advanced)

Caution

Be careful when bypassing Astro’s built-in CSS bundling! Styles won’t be automatically included in the built output, and it is your responsibility to make sure that the referenced file is properly included in the final page output.

### `?raw` CSS Imports

[Section titled “?raw CSS Imports”](#raw-css-imports)

For advanced use cases, CSS can be read directly from disk without being bundled or optimized by Astro. This can be useful when you need complete control over some snippet of CSS, and need to bypass Astro’s automatic CSS handling.

This is not recommended for most users.

src/components/RawInlineStyles.astro

```astro
---
// Advanced example! Not recommended for most users.
import rawStylesCSS from '../styles/main.css?raw';
---
<style is:inline set:html={rawStylesCSS}></style>
```

See [Vite’s docs](https://vite.dev/guide/assets.html#importing-asset-as-string) for full details.

### `?url` CSS Imports

[Section titled “?url CSS Imports”](#url-css-imports)

For advanced use cases, you can import a direct URL reference for a CSS file inside of your project `src/` directory. This can be useful when you need complete control over how a CSS file is loaded on the page. However, this will prevent the optimization of that CSS file with the rest of your page CSS .

This is not recommended for most users. Instead, place your CSS files inside of `public/` to get a consistent URL reference.

Caution

Importing a smaller CSS file with `?url` may return the base64 encoded contents of the CSS file as a data URL in your final build. Either write your code to support encoded data URLs (`data:text/css;base64,...`) or set the [`vite.build.assetsInlineLimit`](https://vite.dev/config/#build-assetsinlinelimit) config option to `0` to disable this feature.

src/components/RawStylesUrl.astro

```astro
---
// Advanced example! Not recommended for most users.
import stylesUrl from '../styles/main.css?url';
---
<link rel="preload" href={stylesUrl} as="style">
<link rel="stylesheet" href={stylesUrl}>
```

See [Vite’s docs](https://vite.dev/guide/assets.html#importing-asset-as-url) for full details.

# Syntax Highlighting

> Learn how to highlight your code blocks in Astro.

Astro comes with built-in support for [Shiki](https://shiki.style/) and [Prism](https://prismjs.com/). This provides syntax highlighting for:

* all [code fences (\`\`\`)](#markdown-code-blocks) used in a Markdown or MDX file.
* content within the [built-in `<Code />` component](#code-) (powered by Shiki) in `.astro` files.
* content within the [`<Prism />` component](#prism-) (powered by Prism) in `.astro` files.

Add [community integrations such as Expressive Code](https://astro.build/integrations/?search=syntax+highlight) for even more text marking and annotation options in your code blocks.

## Markdown code blocks

[Section titled “Markdown code blocks”](#markdown-code-blocks)

A Markdown code block is indicated by a block with three backticks \`\`\` at the start and end. You can indicate the programming language being used after the opening backticks to indicate how to color and style your code to make it easier to read.

````markdown
```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l);
  return true;
};
```
````

Astro’s Markdown code blocks are styled by Shiki by default, preconfigured with the `github-dark` theme. The compiled output will be limited to inline `style`s without any extraneous CSS classes, stylesheets, or client-side JS.

You can [add a Prism stylesheet and switch to Prism’s highlighting](#add-a-prism-stylesheet), or disable Astro’s syntax highlighting entirely, with the [`markdown.syntaxHighlight`](/en/reference/configuration-reference/#markdownsyntaxhighlight) configuration option.

See the full [`markdown.shikiConfig` reference](/en/reference/configuration-reference/#markdownshikiconfig) for the complete set of Markdown syntax highlighting options available when using Shiki.

### Setting a default Shiki theme

[Section titled “Setting a default Shiki theme”](#setting-a-default-shiki-theme)

You can configure any [built-in Shiki theme](https://shiki.style/themes) for your Markdown code blocks in your Astro config:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  markdown: {
    shikiConfig: {
      theme: 'dracula',
    },
  },
});
```

See the full [Shiki config reference](/en/reference/configuration-reference/#markdownshikiconfig) for the complete set of Markdown code block options.

### Setting light and dark mode themes

[Section titled “Setting light and dark mode themes”](#setting-light-and-dark-mode-themes)

You can specify dual Shiki themes for light and dark mode in your Astro config:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  markdown: {
    shikiConfig: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
    },
  },
});
```

Then, [add Shiki’s dark mode CSS variables via media query or classes](https://shiki.style/guide/dual-themes#query-based-dark-mode) to apply to all your Markdown code blocks by default. Replace the `.shiki` class in the examples from Shiki’s documentation with `.astro-code`:

src/styles/global.css

```diff
@media (prefers-color-scheme: dark) {
  -.shiki,
  -.shiki span {
+  .astro-code,
+  .astro-code span {
    color: var(--shiki-dark) !important;
    background-color: var(--shiki-dark-bg) !important;
    /* Optional, if you also want font styles */
    font-style: var(--shiki-dark-font-style) !important;
    font-weight: var(--shiki-dark-font-weight) !important;
    text-decoration: var(--shiki-dark-text-decoration) !important;
  }
}
```

See the full [Shiki config reference](/en/reference/configuration-reference/#markdownshikiconfig) for the complete set of Markdown code block options.

### Adding your own Shiki theme

[Section titled “Adding your own Shiki theme”](#adding-your-own-shiki-theme)

Instead of using one of Shiki’s predefined themes, you can import a custom Shiki theme from a local file.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import customTheme from './my-shiki-theme.json';


export default defineConfig({
  markdown: {
    shikiConfig: {
+      theme: customTheme,
    },
  },
});
```

### Customizing Shiki themes

[Section titled “Customizing Shiki themes”](#customizing-shiki-themes)

You can follow [Shiki’s own theme documentation](https://shiki.style/themes) for more customization options for themes, [light vs dark mode toggles](https://shiki.style/guide/dual-themes), or styling via [CSS variables](https://shiki.style/guide/theme-colors#css-variables-theme).

You will need to adjust the examples from Shiki’s documentation for your Astro project by making the following substitutions:

* Code blocks are styled using the `.astro-code` class instead of `.shiki`
* When using the `css-variables` theme, custom properties are prefixed with `--astro-code-` instead of `--shiki-`

## Components for code blocks

[Section titled “Components for code blocks”](#components-for-code-blocks)

There are two Astro components available for `.astro` and `.mdx` files to render code blocks: [`<Code />`](#code-) and [`<Prism />`](#prism-).

You can reference the `Props` of these components using the [`ComponentProps` type](/en/guides/typescript/#componentprops-type) utility.

### `<Code />`

[Section titled “\<Code />”](#code-)

This component is powered internally by Shiki. It supports all popular Shiki themes and languages as well as several other Shiki options such as custom themes, languages, [transformers](#transformers), and default colors.

These values are passed to the `<Code />` component using the `theme`, `lang`, `transformers`, and `defaultColor` attributes respectively as props. The `<Code />` component will not inherit your `shikiConfig` settings for Markdown code blocks.

```astro
---
import { Code } from 'astro:components';
---
<!-- Syntax highlight some JavaScript code. -->
<Code code={`const foo = 'bar';`} lang="js" />
<!-- Optional: Customize your theme. -->
<Code code={`const foo = 'bar';`} lang="js" theme="dark-plus" />
<!-- Optional: Enable word wrapping. -->
<Code code={`const foo = 'bar';`} lang="js" wrap />
<!-- Optional: Output inline code. -->
<p>
  <Code code={`const foo = 'bar';`} lang="js" inline />
  will be rendered inline.
</p>
<!-- Optional: defaultColor -->
<Code code={`const foo = 'bar';`} lang="js" defaultColor={false} />
```

#### Transformers

[Section titled “Transformers”](#transformers)

**Added in:** `astro@4.11.0`

[Shiki transformers](https://shiki.style/packages/transformers#shikijs-transformers) can optionally be applied to code by passing them in through the `transformers` property as an array. Since Astro v4.14.0, you can also provide a string for [Shiki’s `meta` attribute](https://shiki.style/guide/transformers#meta) to pass options to transformers.

Note that `transformers` only applies classes and you must provide your own CSS rules to target the elements of your code block.

src/pages/index.astro

```astro
---
import { transformerNotationFocus, transformerMetaHighlight } from '@shikijs/transformers'
import { Code } from 'astro:components'
const code = `const foo = 'hello'
const bar = ' world'
console.log(foo + bar) // [!code focus]
`
---
<Code
  code={code}
  lang="js"
  transformers={[transformerMetaHighlight()]}
  meta="{1,3}"
/>


<style is:global>
  pre.has-focused .line:not(.focused) {
    filter: blur(1px);
  }
</style>
```

### `<Prism />`

[Section titled “\<Prism />”](#prism-)

This component provides language-specific syntax highlighting for code blocks by applying Prism’s CSS classes. Note that you must [provide a Prism CSS stylesheet](#add-a-prism-stylesheet) (or bring your own) to style the classes.

To use the `Prism` highlighter component, you must install the `@astrojs/prism` package:

* npm

  ```shell
  npm install @astrojs/prism
  ```

* pnpm

  ```shell
  pnpm add @astrojs/prism
  ```

* Yarn

  ```shell
  yarn add @astrojs/prism
  ```

Then, you can import and use the `<Prism />` component like any other Astro component, passing a language and the code to render.

```astro
---
import { Prism } from '@astrojs/prism';
---
<Prism lang="js" code={`const foo = 'bar';`} />
```

In addition to the [list of languages supported by Prism](https://prismjs.com/#supported-languages), you can also use `lang="astro"` to display Astro code blocks.

## Add a Prism stylesheet

[Section titled “Add a Prism stylesheet”](#add-a-prism-stylesheet)

If you opt to use Prism (either by configuring `markdown.syntaxHighlight: 'prism'` or with the `<Prism />` component), Astro will apply Prism’s CSS classes instead of Shiki’s to your code. You will need to bring your own CSS stylesheet for syntax highlighting to appear.

1. Choose a premade stylesheet from the available [Prism Themes](https://github.com/PrismJS/prism-themes).

2. Add this stylesheet to [your project’s `public/` directory](/en/basics/project-structure/#public).

3. Load this into your page’s `<head>` in a [layout component](/en/basics/layouts/) via a `<link>` tag. (See [Prism basic usage](https://prismjs.com/#basic-usage).)

You can also visit the [list of languages supported by Prism](https://prismjs.com/#supported-languages) for options and usage.


---

**Navigation:** [← Previous](./07-astrojsvercel.md) | [Index](./index.md) | [Next →](./09-testing.md)
