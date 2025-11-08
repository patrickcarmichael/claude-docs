---
title: "My Markdown Page"
section: 163
---

# My Markdown Page


<!-- Local image stored at src/assets/stars.png -->
![A starry night sky.](../assets/stars.png)
```jsx
In React (`.jsx`) components, use standard JSX image syntax (`<img />`). Astro will not optimize these images, but you can install and use NPM packages for more flexibility.

You can learn more about [using images in Astro](/en/guides/images/) in the Images Guide.

### Gatsby GraphQL to Astro

[Section titled “Gatsby GraphQL to Astro”](#gatsby-graphql-to-astro)

Remove all references to GraphQL queries, and instead use [`import.meta.glob()`](/en/guides/imports/#importmetaglob) to access data from your local files.

Or, if using content collections, query your Markdown and MDX files using [`getEntry()` and `getCollection()`](/en/guides/content-collections/#generating-routes-from-content).

These data requests are made in the frontmatter of the Astro component using the data.

src/pages/index.astro

```diff
---
-import { graphql } from "gatsby"
import { getCollection } from 'astro:content';


// Get all `src/content/blog/` entries
const allBlogPosts = await getCollection('blog');


// Get all `src/pages/posts/` entries
const allPosts = Object.values(import.meta.glob('../pages/post/*.md', { eager: true }));
---


-export const pageQuery = graphql`
  -{
    -allMarkdownRemark(sort: { frontmatter: { date: DESC } }) {
-      nodes {
-        excerpt
-        fields {
-          slug
-        }
-        frontmatter {
          -date(formatString: "MMMM DD, YYYY")
-          title
-          description
-        }
-      }
-    }
  -}
-`
```jsx
## Guided example: Gatsby layout to Astro

[Section titled “Guided example: Gatsby layout to Astro”](#guided-example-gatsby-layout-to-astro)

This example converts the main project layout (`layout.js`) from Gatsby’s blog starter to `src/layouts/Layout.astro`.

This page layout shows one header when visiting the home page, and a different header with a link back to Home for all other pages.

1. Identify the `return()` JSX.

   layout.js

   ```jsx
   import * as React from "react"
   import { Link } from "gatsby"
   const Layout = ({ location, title, children }) => {
     const rootPath = `${__PATH_PREFIX__}/`
     const isRootPath = location.pathname === rootPath
     let header
     if (isRootPath) {
       header = (
         <h1 className="main-heading">
           <Link to="/">{title}</Link>
         </h1>
       )
     } else {
       header = (
         <Link className="header-link-home" to="/">
           Home
         </Link>
       )
     }
     return (
       <div className="global-wrapper" data-is-root-path={isRootPath}>
         <header className="global-header">{header}</header>
         <main>{children}</main>
         <footer>
           © {new Date().getFullYear()}, Built with
           {` `}
           <a href="https://www.gatsbyjs.com">Gatsby</a>
         </footer>
       </div>
     )
   }
   export default Layout
   ```jsx
2. Create `Layout.astro` and add this `return` value, [converted to Astro syntax](#reference-convert-to-astro-syntax).

   Note that:

   * `{new Date().getFullYear()}` just works 🎉
   * `{children}` becomes `<slot />` 🦥
   * `className` becomes `class` 📛
   * `Gatsby` becomes `Astro` 🚀

   src/layouts/Layout.astro

   ```astro
   ---
   ---
   <div class="global-wrapper" data-is-root-path={isRootPath}>
     <header class="global-header">{header}</header>
     <main><slot /></main>
     <footer>
       © {new Date().getFullYear()}, Built with
       {` `}
       <a href="https://www.astro.build">Astro</a>
     </footer>
   </div>
   ```jsx
3. Add a page shell so that your layout provides each page with the necessary parts of an HTML document:

   src/layouts/Layout.astro

   ```diff
   ---
   ---
   <html>
     <head>
       <meta charset="utf-8" />
       <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
       <meta name="viewport" content="width=device-width" />
       <title>Astro</title>
     </head>
     <body>
       <div class="global-wrapper" data-is-root-path={isRootPath}>
         <header class="global-header">{header}</header>
         <main>
           <slot />
         </main>
         <footer>
           &#169; {new Date().getFullYear()}, Built with
           {` `}
           <a href="https://www.astro.build">Astro</a>
         </footer>
       </div>
     </body>
   </html>
   ```jsx
4. Add any needed imports, props, and JavaScript

   To conditionally render a header based on the page route and title in Astro:

   * Provide the props via `Astro.props`. (Remember: your Astro templating accesses props from its frontmatter, not passed into a function.)
   * Use a ternary operator to show one heading if this is the home page, and a different heading otherwise.
   * Remove variables for `{header}` and `{isRootPath}` as they are no longer needed.
   * Replace Gatsby’s `<Link/>` tags with `<a>` anchor tags.
   * Use `class` instead of `className`.
   * Import a local stylesheet from your project for the class names to take effect.

   src/layouts/Layout.astro

   ```diff
   ---
   +import '../styles/style.css';
   +const { title, pathname } = Astro.props
   ---
   <html>
     <head>
       <meta charset="utf-8" />
       <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
       <meta name="viewport" content="width=device-width" />
       <title>Astro</title>
     </head>
     <body>
       <div class="global-wrapper">
         <header class="global-header">
           +{ pathname === "/"
           +?
             <h1 class="main-heading">
             <a href="/">{title}</a>
             </h1>
           +:
             <h1 class="main-heading">
             <a class="header-link-home" href="/">Home</a>
             </h1>
           +}
         </header>
         <main>
           <slot />
         </main>
         <footer>
           &#169; {new Date().getFullYear()}, Built with
           {` `}
           <a href="https://www.astro.build">Astro</a>
         </footer>
       </div>
     </body>
   </html>
   ```jsx
5. Update `index.astro` to use this new layout and pass it the necessary `title` and `pathname` props:

   src/pages/index.astro

   ```astro
   ---
   import Layout from '../layouts/Layout.astro';
   const pagePathname = Astro.url.pathname
   ---
   <Layout title="Home Page" pathname={pagePathname}>
       <p>Astro</p>
   </Layout>
   ```jsx
   Tip

   You can [get the current page’s path using `Astro.url`](/en/reference/api-reference/#url).

6. To test the conditional header, create a second page, `about.astro` using the same pattern:

   src/pages/about.astro

   ```astro
   ---
   import Layout from '../layouts/Layout.astro';
   const pagePathname = Astro.url.pathname
   ---
   <Layout title="About" pathname={pagePathname}>
       <p>About</p>
   </Layout>
   ```jsx
   You should see a link to “Home” only when visiting the About page.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Migrating from Gatsby to Astro ](https://loige.co/migrating-from-gatsby-to-astro/)How and why I migrated this blog from Gatsby to Astro and what I learned in the process.

[Migrating to Astro was EZ ](https://joelhooks.com/migrating-to-astro-was-ez)This is about the process of migrating from Gatsby to Astro, and why I chose Astro.

[My Switch from Gatsby to Astro ](https://www.joshfinnie.com/blog/my-switch-from-gatsby-to-astro/)The switch to Astro is definitely worth a blog post! It’s revolutionizing the static web development scene for the better.

[Why I moved to Astro from Gatsby ](https://dev.to/askrodney/why-i-moved-to-astro-from-gatsby-3fck)Taking a quick look at what made me want to switch and why Astro was a good fit.

[Another Migration: From Gatsby to Astro ](https://logarithmicspirals.com/blog/migrating-from-gatsby-to-astro/)Learn about how I transitioned my personal website from Gatsby to Astro as I share insights and experiences from the migration process.

[From Gatsby gridlock to Astro bliss: my personal site redesign ](https://jwn.gr/posts/migrating-from-gatsby-to-astro/)Gatsby has shown its age and I found myself seeking a modern alternative. Enter Astro — a framework that has breathed some new life into this site.

[Why and how I moved my blog away from Gatsby and React to Astro Js and Preact ](https://www.helmerdavila.com/blog/en/why-and-how-i-moved-my-blog-away-from-gatsby-and-react-to-astro-js-and-preact)All is about simplicity and power at the same time.

[How I rewrote my HUGE Gatsby site in Astro and learned to love it in the process ](https://dunedinsound.com/blog/how_i_rewrote_my_huge_gatsby_site_in_astro_and_learned_to_love_it_in_the_process/)Everything is faster. Happier. More productive.

[How I switched from Gatsby to Astro (While Keeping Drupal in the Mix) ](https://albert.skibinski.nl/en/blog/how-i-switched-gatsby-astro-while-keeping-drupal-mix/)I came across the relatively new Astro, which ticked all the boxes.

[Migrating my website from Gatsby to Astro ](https://dev.to/flashblaze/migrating-my-website-from-gatsby-to-astro-2ej5)Astro has entered the chat.

[Gatsby to Astro ](https://alvin.codes/writing/gatsby-to-astro)Why and how I migrated this website from Gatsby to Astro.

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Gatsby site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-gatsby.mdx)!

---

[← Previous](162-migrating-from-gatsby.md) | [Index](index.md) | [Next →](index.md)
