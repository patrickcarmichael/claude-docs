**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-actions.md)

---

# Why Astro?

> Astro is the web framework for building content-driven websites like blogs, marketing, and e-commerce. Learn why Astro might be a good choice for your next website.

**Astro** is the web framework for building **content-driven websites** like blogs, marketing, and e-commerce. Astro is best-known for pioneering a new [frontend architecture](/en/concepts/islands/) to reduce JavaScript overhead and complexity compared to other frameworks. If you need a website that loads fast and has great SEO, then Astro is for you.

## Features

[Section titled “Features”](#features)

**Astro is an all-in-one web framework.** It includes everything you need to create a website, built-in. There are also hundreds of different [integrations](https://astro.build/integrations/) and [API hooks](/en/reference/integrations-reference/) available to customize a project to your exact use case and needs.

Some highlights include:

* **[Islands](/en/concepts/islands/):** A component-based web architecture optimized for content-driven websites.
* **[UI-agnostic](/en/guides/framework-components/):** Supports React, Preact, Svelte, Vue, Solid, HTMX, web components, and more.
* **[Server-first](/en/guides/on-demand-rendering/):** Moves expensive rendering off of your visitors’ devices.
* **[Zero JS, by default](/en/basics/astro-components/):** Less client-side JavaScript to slow your site down.
* **[Content collections](/en/guides/content-collections/):** Organize, validate, and provide TypeScript type-safety for your Markdown content.
* **[Customizable](/en/guides/integrations-guide/):** Partytown, MDX, and hundreds of integrations to choose from.

## Design Principles

[Section titled “Design Principles”](#design-principles)

Here are five core design principles to help explain why we built Astro, the problems that it exists to solve, and why Astro may be the best choice for your project or team.

Astro is…

1. **[Content-driven](#content-driven):** Astro was designed to showcase your content.
2. **[Server-first](#server-first):** Websites run faster when they render HTML on the server.
3. **[Fast by default](#fast-by-default):** It should be impossible to build a slow website in Astro.
4. **[Easy to use](#easy-to-use):** You don’t need to be an expert to build something with Astro.
5. **[Developer-focused](#developer-focused):** You should have the resources you need to be successful.

### Content-driven

[Section titled “Content-driven”](#content-driven)

**Astro was designed for building content-rich websites.** This includes marketing sites, publishing sites, documentation sites, blogs, portfolios, landing pages, community sites, and e-commerce sites. If you have content to show, it needs to reach your reader quickly.

By contrast, most modern web frameworks were designed for building *web applications*. These frameworks excel at building more complex, application-like experiences in the browser: logged-in admin dashboards, inboxes, social networks, todo lists, and even native-like applications like [Figma](https://figma.com/) and [Ping](https://ping.gg/). However with that complexity, they can struggle to provide great performance when delivering your content.

Astro’s focus on content from its beginnings as a static site builder have allowed Astro to **sensibly scale up to performant, powerful, dynamic web applications** that still respect your content and your audience. Astro’s unique focus on content lets Astro make tradeoffs and deliver unmatched performance features that wouldn’t make sense for more application-focused web frameworks to implement.

### Server-first

[Section titled “Server-first”](#server-first)

**Astro leverages server rendering over client-side rendering in the browser as much as possible.** This is the same approach that traditional server-side frameworks -- PHP, WordPress, Laravel, Ruby on Rails, etc. -- have been using for decades. But you don’t need to learn a second server-side language to unlock it. With Astro, everything is still just HTML, CSS, and JavaScript (or TypeScript, if you prefer).

This approach stands in contrast to other modern JavaScript web frameworks like Next.js, SvelteKit, Nuxt, Remix, and others. These frameworks were built for client-side rendering of your entire website and include server-side rendering mainly to address performance concerns. This approach has been dubbed the **Single-Page App (SPA)**, in contrast with Astro’s **Multi-Page App (MPA)** approach.

The SPA model has its benefits. However, these come at the expense of additional complexity and performance tradeoffs. These tradeoffs harm page performance -- critical metrics like [Time to Interactive (TTI)](https://web.dev/interactive/) -- which doesn’t make much sense for content-focused websites where first-load performance is essential.

Astro’s server-first approach allows you to opt in to client-side rendering only if, and exactly as, necessary. You can choose to add UI framework components that run on the client. You can take advantage of Astro’s view transitions router for finer control over select page transitions and animations. Astro’s server-first rendering, either pre-rendered or on-demand, provides performant defaults that you can enhance and extend.

### Fast by default

[Section titled “Fast by default”](#fast-by-default)

Good performance is always important, but it is *especially* critical for websites whose success depends on displaying your content. It has been well-proven that poor performance loses you engagement, conversions, and money. For example:

* Every 100ms faster → 1% more conversions ([Mobify](https://web.dev/why-speed-matters/), earning +$380,000/yr)
* 50% faster → 12% more sales ([AutoAnything](https://www.digitalcommerce360.com/2010/08/19/web-accelerator-revs-conversion-and-sales-autoanything/))
* 20% faster → 10% more conversions ([Furniture Village](https://www.thinkwithgoogle.com/intl/en-gb/marketing-strategies/app-and-mobile/furniture-village-and-greenlight-slash-page-load-times-boosting-user-experience/))
* 40% faster → 15% more sign-ups ([Pinterest](https://medium.com/pinterest-engineering/driving-user-growth-with-performance-improvements-cfc50dafadd7))
* 850ms faster → 7% more conversions ([COOK](https://web.dev/why-speed-matters/))
* Every 1 second slower → 10% fewer users ([BBC](https://www.creativebloq.com/features/how-the-bbc-builds-websites-that-scale))

In many web frameworks, it is easy to build a website that looks great during development only to load painfully slow once deployed. JavaScript is often the culprit, since many phones and lower-powered devices rarely match the speed of a developer’s laptop.

Astro’s magic is in how it combines the two values explained above -- a content focus with a server-first architecture -- to make tradeoffs and deliver features that other frameworks cannot. The result is amazing web performance for every website, out of the box. Our goal: **It should be nearly impossible to build a slow website with Astro.**

An Astro website can [load 40% faster with 90% less JavaScript](https://twitter.com/t3dotgg/status/1437195415439360003) than the same site built with the most popular React web framework. But don’t take our word for it: watch Astro’s performance leave Ryan Carniato (creator of Solid.js and Marko) [speechless](https://youtu.be/2ZEMb_H-LYE?t=8163).

### Easy to use

[Section titled “Easy to use”](#easy-to-use)

**Astro’s goal is to be accessible to every web developer.** Astro was designed to feel familiar and approachable regardless of skill level or past experience with web development.

The `.astro` UI language is a superset of HTML: any valid HTML is valid Astro templating syntax! So, if you can write HTML, you can write Astro components! But, it also combines some of our favorite features borrowed from other component languages like JSX expressions (React) and CSS scoping by default (Svelte and Vue). This closeness to HTML also makes it easier to use progressive enhancement and common accessibility patterns without any overhead.

We then made sure that you could also use your favorite UI component languages that you already know, and even reuse components you might already have. React, Preact, Svelte, Vue, Solid, and others, including web components, are all supported for authoring UI components in an Astro project.

Astro was designed to be less complex than other UI frameworks and languages. One big reason for this is that Astro was designed to render on the server, not in the browser. That means that you don’t need to worry about: hooks (React), stale closures (also React), refs (Vue), observables (Svelte), atoms, selectors, reactions, or derivations. There is no reactivity on the server, so all of that complexity melts away.

One of our favorite sayings is: **opt in to complexity.** We designed Astro to remove as much “required complexity” as possible from the developer experience, especially as you onboard for the first time. You can build a “Hello World” example website in Astro with just HTML and CSS. Then, when you need to build something more powerful, you can incrementally reach for new features and APIs as you go.

### Developer-focused

[Section titled “Developer-focused”](#developer-focused)

We strongly believe that Astro is only a successful project if people love using it. Astro has everything you need to support you as you build with Astro.

Astro invests in developer tools like a great CLI experience from the moment you open your terminal, an official VS Code extension for syntax highlighting, TypeScript and Intellisense, and documentation actively maintained by hundreds of community contributors and available in 14 languages.

Our welcoming, respectful, inclusive community on Discord is ready to provide support, motivation, and encouragement. Open a `#support` thread to get help with your project. Visit our dedicated `#showcase` channel for sharing your Astro sites, blog posts, videos, and even work-in-progress for safe feedback and constructive criticism. Participate in regular live events such as our weekly community call, “Talking and Doc’ing,” and API/bug bashes.

As an open-source project, we welcome contributions of all types and sizes from community members of all experience levels. You are invited to join in roadmap discussions to shape the future of Astro, and we hope you’ll contribute fixes and features to the core codebase, compiler, docs, language tools, websites, and other projects.

# Islands architecture

> Learn about how Astro's islands architecture helps keep sites fast.

Astro helped pioneer and popularize a new frontend architecture pattern called **Islands Architecture.** Islands architecture works by rendering the majority of your page to fast, static HTML with smaller “islands” of JavaScript added when interactivity or personalization is needed on the page (an image carousel, for example). This avoids the monolithic JavaScript payloads that slow down the responsiveness of many other, modern JavaScript web frameworks.

## A brief history

[Section titled “A brief history”](#a-brief-history)

The term “component island” was first coined by Etsy’s frontend architect [Katie Sylor-Miller](https://sylormiller.com/) in 2019. This idea was then expanded on and documented in [this post](https://jasonformat.com/islands-architecture/) by Preact creator Jason Miller on August 11, 2020.

> The general idea of an “Islands” architecture is deceptively simple: render HTML pages on the server, and inject placeholders or slots around highly dynamic regions \[…] that can then be “hydrated” on the client into small self-contained widgets, reusing their server-rendered initial HTML.\
> — Jason Miller, Creator of Preact

The technique that this architectural pattern builds on is also known as **partial** or **selective hydration.**

In contrast, most JavaScript-based web frameworks hydrate & render an entire website as one large JavaScript application (also known as a single-page application, or SPA). SPAs provide simplicity and power but suffer from page-load performance problems due to heavy client-side JavaScript usage.

SPAs have their place, even [embedded inside an Astro page](/en/guides/migrate-to-astro/from-create-react-app/). But, SPAs lack the native ability to selectively and strategically hydrate, making them a heavy-handed choice for most projects on the web today.

Astro became popular as the first mainstream JavaScript web framework with selective hydration built-in, using that same component islands pattern first coined by Sylor-Miller. We’ve since expanded and evolved on Sylor-Miller’s original work, which helped to inspire a similar component island approach to dynamically server-rendered content.

## What is an island?

[Section titled “What is an island?”](#what-is-an-island)

In Astro, an island is an enhanced UI component on an otherwise static page of HTML.

A [**client island**](#client-islands) is an interactive JavaScript UI component that is hydrated separately from the rest of the page, while a [**server island**](#server-islands) is a UI component that server-renders its dynamic content separately from the rest of the page.

Both islands run expensive or slower processes independently, on a per-component basis, for optimized page loads.

## Island components

[Section titled “Island components”](#island-components)

Astro components are the building blocks of your page template. They render to static HTML with no client-side runtime.

Think of a client island as an interactive widget floating in a sea of otherwise static, lightweight, server-rendered HTML. Server islands can be added for personalized or dynamic server-rendered elements, such as a logged in visitor’s profile picture.

Header (interactive island)

Sidebar (static HTML)

Static content like text, images, etc.

Image carousel (interactive island)

Footer (static HTML)

Source: [Islands Architecture: Jason Miller](https://jasonformat.com/islands-architecture/)

An island always runs in isolation from other islands on the page, and multiple islands can exist on a page. Client islands can still share state and communicate with each other, even though they run in different component contexts.

This flexibility allows Astro to support multiple UI frameworks like [React](https://react.dev/), [Preact](https://preactjs.com/), [Svelte](https://svelte.dev/), [Vue](https://vuejs.org/), and [SolidJS](https://www.solidjs.com/). Because they are independent, you can even mix several frameworks on each page.

Tip

Although most developers will stick to just one UI framework, Astro supports multiple frameworks in the same project. This allows you to:

* Choose the framework that is best for each component.
* Learn a new framework without needing to start a new project.
* Collaborate with others even when working in different frameworks.
* Incrementally convert an existing site to another framework with no downtime.

## Client Islands

[Section titled “Client Islands”](#client-islands)

By default, Astro will automatically render every UI component to just HTML & CSS, **stripping out all client-side JavaScript automatically.**

src/pages/index.astro

```astro
<MyReactComponent />
```

This may sound strict, but this behavior is what keeps Astro websites fast by default and protects developers from accidentally sending unnecessary or unwanted JavaScript that might slow down their website.

Turning any static UI component into an interactive island requires only a `client:*` directive. Astro then automatically builds and bundles your client-side JavaScript for optimized performance.

src/pages/index.astro

```astro
<!-- This component is now interactive on the page!
     The rest of your website remains static. -->
<MyReactComponent client:load />
```

With islands, client-side JavaScript is only loaded for the explicit interactive components that you mark using `client:*` directives.

And because interaction is configured at the component-level, you can handle different loading priorities for each component based on its usage. For example, `client:idle` tells a component to load when the browser becomes idle, and `client:visible` tells a component to load only once it enters the viewport.

### Benefits of client islands

The most obvious benefit of building with Astro Islands is performance: the majority of your website is converted to fast, static HTML and JavaScript is only loaded for the individual components that need it. JavaScript is one of the slowest assets that you can load per-byte, so every byte counts.

Another benefit is parallel loading. In the example illustration above, the low-priority “image carousel” island doesn’t need to block the high-priority “header” island. The two load in parallel and hydrate in isolation, meaning that the header becomes interactive immediately without having to wait for the heavier carousel lower down the page.

Even better, you can tell Astro exactly how and when to render each component. If that image carousel is really expensive to load, you can attach a special [client directive](/en/reference/directives-reference/#client-directives) that tells Astro to only load the carousel when it becomes visible on the page. If the user never sees it, it never loads.

In Astro, it’s up to you as the developer to explicitly tell Astro which components on the page need to also run in the browser. Astro will only hydrate exactly what’s needed on the page and leave the rest of your site as static HTML.

**Client islands are the secret to Astro’s fast-by-default performance story!**

Read more about [using JavaScript framework components](/en/guides/framework-components/) in your project.

## Server islands

[Section titled “Server islands”](#server-islands)

Server islands are a way to move expensive or slow server-side code out of the way of the main rendering process, making it easy to combine high-performance static HTML and dynamic server-generated components.

Add the [`server:defer` directive](/en/reference/directives-reference/#server-directives) to any Astro component on your page to turn it into its own server island:

src/pages/index.astro

```astro
---
import Avatar from "../components/Avatar.astro";
---
<Avatar server:defer />
```

This breaks up your page with smaller areas of server-rendered content that each load in parallel.

Your page’s main content can be rendered immediately with placeholder content, such as a generic avatar until your island’s own content is available. With server islands, having small components of personalized content does not delay the rendering of an otherwise static page.

This rendering pattern was built to be portable. It does not depend on any server infrastructure so it will work with any host, from a Node.js server in a Docker container to the serverless provider of your choice.

### Benefits of server islands

One benefit of server islands is the ability to render the more highly dynamic parts of your page on the fly. This allows the outer shell and main content to be more aggressively cached, providing faster performance.

Another benefit is providing a great visitor experience. Server islands are optimized and load quickly, often even before the browser has even painted the page. But in the short time it takes for your islands to render, you can display custom fallback content and prevent any layout shift.

An example of a site that benefits from Astro’s server islands is an e-commerce storefront. Although the main content of product pages change infrequently, these pages typically have some dynamic pieces:

* The user’s avatar in the header.
* Special deals and sales for the product.
* User reviews.

Using server islands for these elements, your visitor will see the most important part of the page, your product, immediately. Generic avatars, loading spinners, and store announcements can be displayed as fallback content until the personalized parts are available.

Read more about [using server islands](/en/guides/server-islands/) in your project.

# Install Astro

> How to install Astro and start a new project.

The [`create astro` CLI command](#install-from-the-cli-wizard) is the fastest way to start a new Astro project from scratch. It will walk you through every step of setting up your new Astro project and allow you to choose from a few different official starter templates.

You can also run the CLI command with the `template` flag to begin your project using any existing theme or starter template. Explore our [themes and starters showcase](https://astro.build/themes/) where you can browse themes for blogs, portfolios, documentation sites, landing pages, and more!

To install Astro manually instead, see our [step-by-step manual installation guide](#manual-setup).

Online previews

Prefer to try Astro in your browser? Visit [astro.new](https://astro.new/) to browse our starter templates and spin up a new Astro project without ever leaving your browser.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* **Node.js** - `v18.20.8` or `v20.3.0`, `v22.0.0` or higher. (`v19` and `v21` are not supported.)
* **Text editor** - We recommend [VS Code](https://code.visualstudio.com/) with our [Official Astro extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode).
* **Terminal** - Astro is accessed through its command-line interface (CLI).

## Browser compatibility

[Section titled “Browser compatibility”](#browser-compatibility)

Astro is built with Vite which targets browsers with modern JavaScript support by default. For a complete reference, you can see the [list of currently supported browser versions in Vite](https://vite.dev/guide/build.html#browser-compatibility).

## Install from the CLI wizard

[Section titled “Install from the CLI wizard”](#install-from-the-cli-wizard)

You can run `create astro` anywhere on your machine, so there’s no need to create a new empty directory for your project before you begin. If you don’t have an empty directory yet for your new project, the wizard will help create one for you automatically.

1. Run the following command in your terminal to start the install wizard:

   * npm

     ```shell
     # create a new project with npm
     npm create astro@latest
     ```

   * pnpm

     ```shell
     # create a new project with pnpm
     pnpm create astro@latest
     ```

   * Yarn

     ```shell
     # create a new project with yarn
     yarn create astro
     ```

   If all goes well, you will see a success message followed by some recommended next steps.

2. Now that your project has been created, you can `cd` into your new project directory to begin using Astro.

3. If you skipped the “Install dependencies?” step during the CLI wizard, then be sure to install your dependencies before continuing.

   * npm

     ```shell
     npm install
     ```

   * pnpm

     ```shell
     pnpm install
     ```

   * Yarn

     ```shell
     yarn install
     ```

4. You can now [start the Astro dev server](/en/develop-and-build/#start-the-astro-dev-server) and see a live preview of your project while you build!

## CLI installation flags

[Section titled “CLI installation flags”](#cli-installation-flags)

You can run the `create astro` command with additional flags to customize the setup process (e.g. answering “yes” to all questions, skipping the Houston animation) or your new project (e.g. install git or not, add integrations).

See [all the available `create astro` command flags](https://github.com/withastro/astro/blob/main/packages/create-astro/README.md).

### Add integrations

[Section titled “Add integrations”](#add-integrations)

You can start a new Astro project and install any [official integrations](/en/guides/integrations-guide/) or community integrations that support the `astro add` command at the same time by passing the `--add` argument to the `create astro` command.

Run the following command in your terminal, substituting any integration that supports the `astro add` command:

* npm

  ```shell
  # create a new project with React and Partytown
  npm create astro@latest -- --add react --add partytown
  ```

* pnpm

  ```shell
  # create a new project with React and Partytown
  pnpm create astro@latest --add react --add partytown
  ```

* Yarn

  ```shell
  # create a new project with React and Partytown
  yarn create astro --add react --add partytown
  ```

### Use a theme or starter template

[Section titled “Use a theme or starter template”](#use-a-theme-or-starter-template)

You can start a new Astro project based on an [official example](https://github.com/withastro/astro/tree/main/examples) or the `main` branch of any GitHub repository by passing a `--template` argument to the `create astro` command.

Run the following command in your terminal, substituting the official Astro starter template name, or the GitHub username and repository of the theme you want to use:

* npm

  ```shell
  # create a new project with an official example
  npm create astro@latest -- --template <example-name>


  # create a new project based on a GitHub repository’s main branch
  npm create astro@latest -- --template <github-username>/<github-repo>
  ```

* pnpm

  ```shell
  # create a new project with an official example
  pnpm create astro@latest --template <example-name>


  # create a new project based on a GitHub repository’s main branch
  pnpm create astro@latest --template <github-username>/<github-repo>
  ```

* Yarn

  ```shell
  # create a new project with an official example
  yarn create astro --template <example-name>


  # create a new project based on a GitHub repository’s main branch
  yarn create astro --template <github-username>/<github-repo>
  ```

By default, this command will use the template repository’s `main` branch. To use a different branch name, pass it as part of the `--template` argument: `<github-username>/<github-repo>#<branch>`.

## Manual Setup

[Section titled “Manual Setup”](#manual-setup)

This guide will walk you through the steps to manually install and configure a new Astro project.

If you prefer not to use our automatic `create astro` CLI tool, you can set up your project yourself by following the guide below.

1. Create your directory

   Create an empty directory with the name of your project, and then navigate into it.

   ```bash
   mkdir my-astro-project
   cd my-astro-project
   ```

   Once you are in your new directory, create your project `package.json` file. This is how you will manage your project dependencies, including Astro. If you aren’t familiar with this file format, run the following command to create one.

   * npm

     ```shell
     npm init --yes
     ```

   * pnpm

     ```shell
     pnpm init
     ```

   * Yarn

     ```shell
     yarn init --yes
     ```

2. Install Astro

   First, install the Astro project dependencies inside your project.

   Important

   Astro must be installed locally, not globally. Make sure you are *not* running `npm install -g astro` `pnpm add -g astro` or `yarn add global astro`.

   * npm

     ```shell
     npm install astro
     ```

   * pnpm

     ```shell
     pnpm add astro
     ```

   * Yarn

     ```shell
     yarn add astro
     ```

   Then, replace any placeholder “scripts” section of your `package.json` with the following:

   package.json

   ```diff
   {
     "scripts": {
       -"test": "echo \"Error: no test specified\" && exit 1",
       +"dev": "astro dev",
       +"build": "astro build",
       +"preview": "astro preview"
     },
   }
   ```

   You’ll use these scripts later in the guide to start Astro and run its different commands.

3. Create your first page

   In your text editor, create a new file in your directory at `src/pages/index.astro`. This will be your first Astro page in the project.

   For this guide, copy and paste the following code snippet (including `---` dashes) into your new file:

   src/pages/index.astro

   ```astro
   ---
   // Welcome to Astro! Everything between these triple-dash code fences
   // is your "component frontmatter". It never runs in the browser.
   console.log('This runs in your terminal, not the browser!');
   ---
   <!-- Below is your "component template." It's just HTML, but with
       some magic sprinkled in to help you build great templates. -->
   <html>
     <body>
       <h1>Hello, World!</h1>
     </body>
   </html>
   <style>
     h1 {
       color: orange;
     }
   </style>
   ```

4. Create your first static asset

   You will also want to create a `public/` directory to store your static assets. Astro will always include these assets in your final build, so you can safely reference them from inside your component templates.

   In your text editor, create a new file in your directory at `public/robots.txt`. `robots.txt` is a simple file that most sites will include to tell search bots like Google how to treat your site.

   For this guide, copy and paste the following code snippet into your new file:

   public/robots.txt

   ```diff
   # Example: Allow all bots to scan and index your site.
   # Full syntax: https://developers.google.com/search/docs/advanced/robots/create-robots-txt
   User-agent: *
   Allow: /
   ```

5. Create `astro.config.mjs`

   Astro is configured using `astro.config.mjs`. This file is optional if you do not need to configure Astro, but you may wish to create it now.

   Create `astro.config.mjs` at the root of your project, and copy the code below into it:

   astro.config.mjs

   ```js
   import { defineConfig } from "astro/config";


   // https://astro.build/config
   export default defineConfig({});
   ```

   If you want to include [UI framework components](/en/guides/framework-components/) such as React, Svelte, etc. or use other tools such as MDX or Partytown in your project, here is where you will [manually import and configure integrations](/en/guides/integrations-guide/).

   Read Astro’s [API configuration reference](/en/reference/configuration-reference/) for more information.

6. Add TypeScript support

   TypeScript is configured using `tsconfig.json`. Even if you don’t write TypeScript code, this file is important so that tools like Astro and VS Code know how to understand your project. Some features (like npm package imports) aren’t fully supported in the editor without a `tsconfig.json` file.

   If you do intend to write TypeScript code, using Astro’s `strict` or `strictest` template is recommended. You can view and compare the three template configurations at [astro/tsconfigs/](https://github.com/withastro/astro/blob/main/packages/astro/tsconfigs/).

   Create `tsconfig.json` at the root of your project, and copy the code below into it. (You can use `base`, `strict`, or `strictest` for your TypeScript template):

   tsconfig.json

   ```json
   {
     "extends": "astro/tsconfigs/base"
   }
   ```

   Read Astro’s [TypeScript setup guide](/en/guides/typescript/#setup) for more information.

7. Next Steps

   If you have followed the steps above, your project directory should now look like this:

   * node\_modules/

     * …

   * public/

     * robots.txt

   * src/

     * pages/

       * index.astro

   * astro.config.mjs

   * package-lock.json or `yarn.lock`, `pnpm-lock.yaml`, etc.

   * package.json

   * tsconfig.json

8. You can now [start the Astro dev server](/en/develop-and-build/#start-the-astro-dev-server) and see a live preview of your project while you build!

# Project structure

> An introduction to the basic file structure of an Astro project.

Your new Astro project generated from the `create astro` CLI wizard already includes some files and folders. Others, you will create yourself and add to Astro’s existing file structure.

Here’s how an Astro project is organized, and some files you will find in your new project.

## Directories and Files

[Section titled “Directories and Files”](#directories-and-files)

Astro leverages an opinionated folder layout for your project. Every Astro project root should include the following directories and files:

* `src/*` - Your project source code (components, pages, styles, images, etc.)
* `public/*` - Your non-code, unprocessed assets (fonts, icons, etc.)
* `package.json` - A project manifest.
* `astro.config.mjs` - An Astro configuration file. (recommended)
* `tsconfig.json` - A TypeScript configuration file. (recommended)

### Example Project Tree

[Section titled “Example Project Tree”](#example-project-tree)

A common Astro project directory might look like this:

* public/

  * robots.txt
  * favicon.svg
  * my-cv.pdf

* src/

  * blog/

    * post1.md
    * post2.md
    * post3.md

  * components/

    * Header.astro
    * Button.jsx

  * images/

    * image1.jpg
    * image2.jpg
    * image3.jpg

  * layouts/

    * PostLayout.astro

  * pages/

    * posts/

      * \[post].astro

    * about.astro

    * **index.astro**

    * rss.xml.js

  * styles/

    * global.css

  * content.config.ts

* astro.config.mjs

* package.json

* tsconfig.json

### `src/`

[Section titled “src/”](#src)

The `src/` folder is where most of your project source code lives. This includes:

* [Pages](/en/basics/astro-pages/)
* [Layouts](/en/basics/layouts/)
* [Astro components](/en/basics/astro-components/)
* [UI framework components (React, etc.)](/en/guides/framework-components/)
* [Styles (CSS, Sass)](/en/guides/styling/)
* [Markdown](/en/guides/markdown-content/)
* [Images to be optimized and processed by Astro](/en/guides/images/)

Astro processes, optimizes, and bundles your `src/` files to create the final website that is shipped to the browser. Unlike the static `public/` directory, your `src/` files are built and handled for you by Astro.

Some files (like Astro components) are not even sent to the browser as written but are instead rendered to static HTML. Other files (like CSS) are sent to the browser but may be optimized or bundled with other CSS files for performance.

Tip

While this guide describes some popular conventions used in the Astro community, the only directory reserved by Astro is `src/pages/`. You are free to rename and reorganize any other directories in a way that works best for you.

### `src/pages`

[Section titled “src/pages”](#srcpages)

Pages routes are created for your site by adding [supported file types](/en/basics/astro-pages/#supported-page-files) to this directory.

Caution

`src/pages` is a **required** sub-directory in your Astro project. Without it, your site will have no pages or routes!

### `src/components`

[Section titled “src/components”](#srccomponents)

**Components** are reusable units of code for your HTML pages. These could be [Astro components](/en/basics/astro-components/), or [UI framework components](/en/guides/framework-components/) like React or Vue. It is common to group and organize all of your project components together in this folder.

This is a common convention in Astro projects, but it is not required. Feel free to organize your components however you like!

### `src/layouts`

[Section titled “src/layouts”](#srclayouts)

[Layouts](/en/basics/layouts/) are Astro components that define the UI structure shared by one or more [pages](/en/basics/astro-pages/).

Just like `src/components`, this directory is a common convention but not required.

### `src/styles`

[Section titled “src/styles”](#srcstyles)

It is a common convention to store your CSS or Sass files in a `src/styles` directory, but this is not required. As long as your styles live somewhere in the `src/` directory and are imported correctly, Astro will handle and optimize them.

### `public/`

[Section titled “public/”](#public)

The `public/` directory is for files and assets in your project that do not need to be processed during Astro’s build process. The files in this folder will be copied into the build folder untouched, and then your site will be built.

This behavior makes `public/` ideal for common assets that do not require any processing, like some images and fonts, or special files such as `robots.txt` and `manifest.webmanifest`.

You can place CSS and JavaScript in your `public/` directory, but be aware that those files will not be bundled or optimized in your final build.

Tip

As a general rule, any CSS or JavaScript that you write yourself should live in your `src/` directory.

### `package.json`

[Section titled “package.json”](#packagejson)

This is a file used by JavaScript package managers to manage your dependencies. It also defines the scripts that are commonly used to run Astro (ex: `npm run dev`, `npm run build`).

There are [two kinds of dependencies](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file) you can specify in a `package.json`: `dependencies` and `devDependencies`. In most cases, these work the same: Astro needs all dependencies at build time, and your package manager will install both. We recommend putting all of your dependencies in `dependencies` to start, and only use `devDependencies` if you find a specific need to do so.

For help creating a new `package.json` file for your project, check out the [manual setup](/en/install-and-setup/#manual-setup) instructions.

### `astro.config.mjs`

[Section titled “astro.config.mjs”](#astroconfigmjs)

This file is generated in every starter template and includes configuration options for your Astro project. Here you can specify integrations to use, build options, server options, and more.

Astro supports several file formats for its JavaScript configuration file: `astro.config.js`, `astro.config.mjs`, `astro.config.cjs` and `astro.config.ts`. We recommend using `.mjs` in most cases or `.ts` if you want to write TypeScript in your config file.

TypeScript config file loading is handled using [`tsm`](https://github.com/lukeed/tsm) and will respect your project’s `tsconfig` options.

See the [configuration reference](/en/reference/configuration-reference/) for complete details.

### `tsconfig.json`

[Section titled “tsconfig.json”](#tsconfigjson)

This file is generated in every starter template and includes TypeScript configuration options for your Astro project. Some features (like npm package imports) aren’t fully supported in the editor without a `tsconfig.json` file.

See the [TypeScript Guide](/en/guides/typescript/) for details on setting configurations.

# Develop and build

> How to start working on a new project.

Once you have an Astro project, now you’re ready to build with Astro! 🚀

## Edit your project

[Section titled “Edit your project”](#edit-your-project)

To make changes to your project, open your project folder in your code editor. Working in development mode with the dev server running allows you to see updates to your site as you edit the code.

You can also [customize aspects of your development environment](#configure-your-dev-environment) such as configuring TypeScript or installing the official Astro editor extensions.

### Start the Astro dev server

[Section titled “Start the Astro dev server”](#start-the-astro-dev-server)

Astro comes with a built-in development server that has everything you need for project development. The `astro dev` CLI command will start the local development server so that you can see your new website in action for the very first time.

Every starter template comes with a pre-configured script that will run `astro dev` for you. After navigating into your project directory, use your favorite package manager to run this command and start the Astro development server.

* npm

  ```shell
  npm run dev
  ```

* pnpm

  ```shell
  pnpm run dev
  ```

* Yarn

  ```shell
  yarn run dev
  ```

If all goes well, Astro will now be serving your project on <http://localhost:4321/>. Visit that link in your browser and see your new site!

### Work in development mode

[Section titled “Work in development mode”](#work-in-development-mode)

Astro will listen for live file changes in your `src/` directory and update your site preview as you build, so you will not need to restart the server as you make changes during development. You will always be able to see an up-to-date version of your site in your browser when the dev server is running.

When viewing your site in the browser, you’ll have access to the [Astro dev toolbar](/en/guides/dev-toolbar/). As you build, it will help you inspect your [islands](/en/concepts/islands/), spot accessibility issues, and more.

If you aren’t able to open your project in the browser after starting the dev server, go back to the terminal where you ran the `dev` command and check the message displayed. It should tell you if an error occurred, or if your project is being served at a different URL than <http://localhost:4321/>.

## Build and preview your site

[Section titled “Build and preview your site”](#build-and-preview-your-site)

To check the version of your site that will be created at build time, quit the dev server (`Ctrl` + `C`) and run the appropriate build command for your package manager in your terminal:

* npm

  ```shell
  npm run build
  ```

* pnpm

  ```shell
  pnpm build
  ```

* Yarn

  ```shell
  yarn run build
  ```

Astro will build a deploy-ready version of your site in a separate folder (`dist/` by default) and you can watch its progress in the terminal. This will alert you to any build errors in your project before you deploy to production. If TypeScript is configured to `strict` or `strictest`, the `build` script will also check your project for type errors.

When the build is finished, run the appropriate `preview` command (e.g. `npm run preview`) in your terminal and you can view the built version of your site locally in the same browser preview window.

Note that this previews your code as it existed when the build command was last run. This is meant to give you a preview of how your site will look when it is deployed to the web. Any later changes you make to your code after building will **not** be reflected while you preview your site until you run the build command again.

Use (`Ctrl` + `C`) to quit the preview and run another terminal command, such as restarting the dev server to go back to [working in development mode](#work-in-development-mode) which does update as you edit to show a live preview of your code changes.

Read more about [the Astro CLI](/en/reference/cli-reference/) and the terminal commands you will use as you build with Astro.

Tip

You may wish to [deploy your new site right away](/en/guides/deploy/), before you begin to add or change too much code. This is helpful to get a minimal, working version of your site published and can save you extra time and effort troubleshooting your deployment later.

## Next Steps

[Section titled “Next Steps”](#next-steps)

Success! You are now ready to start building with Astro! 🥳

Here are a few things that we recommend exploring next. You can read them in any order. You can even leave our documentation for a bit and go play in your new Astro project codebase, coming back here whenever you run into trouble or have a question.

### Configure your dev environment

[Section titled “Configure your dev environment”](#configure-your-dev-environment)

Explore the guides below to customize your development experience.

[Editor Setup ](/en/editor-setup/)Customize your code editor to improve the Astro developer experience and unlock new features.

[Dev Toolbar ](/en/guides/dev-toolbar/)Explore the helpful features of the dev toolbar.

[TypeScript Configuration ](/en/guides/typescript/)Configure options for type-checking, IntelliSense, and more.

### Explore Astro’s Features

[Section titled “Explore Astro’s Features”](#explore-astros-features)

[Understand your codebase ](/en/basics/project-structure/)Learn about Astro’s file structure in our Project Structure guide.

[Create content collections ](/en/guides/content-collections/)Add content to your new site with frontmatter validation and automatic type-safety.

[Add view transitions ](/en/guides/view-transitions/)Create seamless page transitions and animations.

[Learn about Islands ](/en/concepts/islands/)Read about Astro's islands architecture.

### Take the introductory tutorial

[Section titled “Take the introductory tutorial”](#take-the-introductory-tutorial)

Build a fully functional Astro blog starting from a single blank page in our [introductory tutorial](/en/tutorial/0-introduction/).

This is a great way to see how Astro works and walks you through the basics of pages, layouts, components, routing, islands, and more. It also includes an optional, beginner-friendly unit for those newer to web development concepts in general, which will guide you through installing the necessary applications on your computer, creating a GitHub account, and deploying your site.

# Configuration overview

> Get to know the ways you can configure and customize your new project and your development experience.

Astro is a flexible, unopinionated framework that allows you to configure your project in many different ways. This means that getting started with a new project might feel overwhelming: there is no “one best way” to set up your Astro project!

The guides in this “Configuration” section will help you familiarize yourself with the various files that allow you to configure and customize aspects of your project and development environment.

If this is your first Astro project, or if it’s been a while since you’ve set up a new project, use the following guides and reference in the documentation for assistance.

## The Astro config File

[Section titled “The Astro config File”](#the-astro-config-file)

The [Astro config file](/en/reference/configuration-reference/) is a JavaScript file included at the root of every starter project:

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
  // your configuration options here...
});
```

It is only required if you have something to configure, but most projects will use this file. The `defineConfig()` helper provides automatic IntelliSense in your IDE and is where you will add all your configuration options to tell Astro how to build and render your project to HTML.

We recommend using the default file format `.mjs` in most cases, or `.ts` if you want to write TypeScript in your config file. However, `astro.config.js` and `astro.config.cjs` are also supported.

Read Astro’s [configuration reference](/en/reference/configuration-reference/) for a full overview of all supported configuration options.

## The TypeScript config File

[Section titled “The TypeScript config File”](#the-typescript-config-file)

Every Astro starter project includes a `tsconfig.json` file in your project. Astro’s [component script](/en/basics/astro-components/#the-component-script) is Typescript, which provides Astro’s editor tooling and allows you to optionally add syntax to your JavaScript for type checking of your own project code.

Use the `tsconfig.json` file to configure the TypeScript template that will perform type checks on your code, configure TypeScript plugins, set import aliases, and more.

Read Astro’s [TypeScript guide](/en/guides/typescript/) for a full overview of TypeScript options and Astro’s built-in utility types.

## Development Experience

[Section titled “Development Experience”](#development-experience)

While you work in development mode, you can take advantage of your code editor and other tools to improve the Astro developer experience.

Astro provides its own official VS Code extension and is compatible with several other popular editor tools. Astro also provides a customizable toolbar that displays in your browser preview while the dev server is running. You can install and even build your own toolbar apps for additional functionality.

Read Astro’s guides to [editor setup options](/en/editor-setup/) and [using the dev toolbar](/en/guides/dev-toolbar/) to learn how to customize your development experience.

## Common new project tasks

[Section titled “Common new project tasks”](#common-new-project-tasks)

Here are some first steps you might choose to take with a new Astro project.

### Add your deployment domain

[Section titled “Add your deployment domain”](#add-your-deployment-domain)

For generating your sitemap and creating canonical URLs, configure your deployment URL in the [`site`](/en/reference/configuration-reference/#site) option. If you are deploying to a path (e.g. `www.example.com/docs`), you can also configure a [`base`](/en/reference/configuration-reference/#base) for the root of your project.

Additionally, different deployment hosts may have different behavior regarding trailing slashes at the end of your URLs. (e.g. `example.com/about` vs `example.com/about/`). Once your site is deployed, you may need to configure your [`trailingSlash`](/en/reference/configuration-reference/#trailingslash) preference.

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
  site: "https://www.example.com",
  base: "/docs",
  trailingSlash: "always",
});
```

### Add site metadata

[Section titled “Add site metadata”](#add-site-metadata)

Astro does not use its configuration file for common SEO or meta data, only for information required to build your project code and render it to HTML.

Instead, this information is added to your page `<head>` using standard HTML `<link>` and `<meta>` tags, just as if you were writing plain HTML pages.

One common pattern for Astro sites is to create a `<Head />` [`.astro` component](/en/basics/astro-components/) that can be added to a common [layout component](/en/basics/layouts/) so it can apply to all your pages.

src/components/MainLayout.astro

```astro
---
import Head from "./Head.astro";


const { ...props } = Astro.props;
---
<html>
  <head>
    <meta charset="utf-8">
    <Head />
    <!-- Additional head elements -->
  </head>
  <body>
    <!-- Page content goes here -->
  </body>
</html>
```

Because `Head.astro` is just a regular Astro component, you can import files and receive props passed from other components, such as a specific page title.

src/components/Head.astro

```astro
---
import Favicon from "../assets/Favicon.astro";
import SomeOtherTags from "./SomeOtherTags.astro";


const { title = "My Astro Website", ...props } = Astro.props;
---
<link rel="sitemap" href="/sitemap-index.xml">
<title>{title}</title>
<meta name="description" content="Welcome to my new Astro site!">


<!-- Web analytics -->
<script data-goatcounter="https://my-account.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>


<!-- Open Graph tags -->
<meta property="og:title" content="My New Astro Website" />
<meta property="og:type" content="website" />
<meta property="og:url" content="http://www.example.com/" />
<meta property="og:description" content="Welcome to my new Astro site!" />
<meta property="og:image" content="https://www.example.com/_astro/seo-banner.BZD7kegZ.webp">
<meta property="og:image:alt" content="">


<SomeOtherTags />


<Favicon />
```

# Astro Courses

> Learn Astro with out-of-this-world courses and tutorials.

Want to get started learning Astro with a course or tutorial?

You can learn the basics of Astro with our [official docs Build a Blog tutorial](/en/tutorial/0-introduction/), or explore our collection of recommended Astro educational content.

## Education Partners

[Section titled “Education Partners”](#education-partners)

Support Astro while you learn

Use Astro’s affiliate links for discounts with our education partners and some of your purchase goes directly back to funding development of the Astro open source project!

Learn Astro from trusted Astro educators, with video lessons, interactive challenges, and projects!

[Learn Astro with Coding in Public ](https://learnastro.dev/?code=ASTRO_PROMO)A premium interactive course with 150+ video lessons that teaches you how to use Astro’s built-in tooling and features.

[Learn Astro with James Q Quick ](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)Build your first Astro site with 35 interactive Scrimba lessons, with video and IDE merged into one unique learning platform.

## Community learning resources

[Section titled “Community learning resources”](#community-learning-resources)

Learn from your fellow astronauts with curated collections of guides, articles, and blog posts.

[Astro Tips ](https://astro-tips.dev/)Advanced, unusual, experimental, and community-written recipes, tutorials, and quick tips.

[Astro Support Squid ](https://get.supportsquid.ink/)An open, public Astro support forum and knowledge base outside of the Astro Discord.

# Components

> An introduction to Astro components.

**Astro components** are the basic building blocks of any Astro project. They are HTML-only templating components with no client-side runtime and use the `.astro` file extension.

Note

If you know HTML, you already know enough to write your first Astro component.

Learn more in the [Astro syntax reference](/en/reference/astro-syntax/).

Astro components are extremely flexible. An Astro component can be as small as a snippet of HTML, like a collection of common `<meta>` tags that make SEO easy to work with. Components can be reusable UI elements, like a header or a profile card. Astro components can even contain an entire page layout or, when located in the special `src/pages/` folder, be an entire page itself.

The most important thing to know about Astro components is that they **don’t render on the client**. They render to HTML either at build-time or on-demand. You can include JavaScript code inside of your component frontmatter, and all of it will be stripped from the final page sent to your users’ browsers. The result is a faster site, with zero JavaScript footprint added by default.

When your Astro component does need client-side interactivity, you can add [standard HTML `<script>` tags](/en/guides/client-side-scripts/) or [UI Framework components](/en/guides/framework-components/#hydrating-interactive-components) as “client islands”.

For components that need to render personalized or dynamic content, you can defer their server rendering by adding a [server directive](/en/reference/directives-reference/#server-directives). These “server islands” will render their content when it is available, without delaying the entire page load.

## Component Structure

[Section titled “Component Structure”](#component-structure)

An Astro component is made up of two main parts: the **Component Script** and the **Component Template**. Each part performs a different job, but together they provide a framework that is both easy to use and expressive enough to handle whatever you might want to build.

src/components/EmptyComponent.astro

```astro
---
// Component Script (JavaScript)
---
<!-- Component Template (HTML + JS Expressions) -->
```

### The Component Script

[Section titled “The Component Script”](#the-component-script)

Astro uses a code fence (`---`) to identify the component script in your Astro component. If you’ve ever written Markdown before, you may already be familiar with a similar concept called *frontmatter.* Astro’s idea of a component script was directly inspired by this concept.

You can use the component script to write any JavaScript code that you need to render your template. This can include:

* importing other Astro components
* importing other framework components, like React
* importing data, like a JSON file
* fetching content from an API or database
* creating variables that you will reference in your template

src/components/MyComponent.astro

```astro
---
import SomeAstroComponent from '../components/SomeAstroComponent.astro';
import SomeReactComponent from '../components/SomeReactComponent.jsx';
import someData from '../data/pokemon.json';


// Access passed-in component props, like `<X title="Hello, World" />`
const { title } = Astro.props;


// Fetch external data, even from a private API or database
const data = await fetch('SOME_SECRET_API_URL/users').then(r => r.json());
---
<!-- Your template here! -->
```

The code fence is designed to guarantee that the JavaScript that you write in it is “fenced in.” It won’t escape into your frontend application, or fall into your user’s hands. You can safely write code here that is expensive or sensitive (like a call to your private database) without worrying about it ever ending up in your user’s browser.

Note

The Astro component script is TypeScript, which allows you to add additional syntax to JavaScript for editor tooling, and error checking.

Read more about Astro’s [built-in TypeScript support](/en/guides/typescript/).

### The Component Template

[Section titled “The Component Template”](#the-component-template)

The component template is below the code fence and determines the HTML output of your component.

If you write plain HTML here, your component will render that HTML in any Astro page it is imported and used.

However, [Astro’s component template syntax](/en/reference/astro-syntax/) also supports **JavaScript expressions**, Astro [`<style>`](/en/guides/styling/#styling-in-astro) and [`<script>`](/en/guides/client-side-scripts/) tags, **imported components**, and [**special Astro directives**](/en/reference/directives-reference/). Data and values defined in the component script can be used in the component template to produce dynamically-created HTML.

src/components/MyFavoritePokemon.astro

```astro
---
// Your component script here!
import Banner from '../components/Banner.astro';
import Avatar from '../components/Avatar.astro';
import ReactPokemonComponent from '../components/ReactPokemonComponent.jsx';
const myFavoritePokemon = [/* ... */];
const { title } = Astro.props;
---
<!-- HTML comments supported! -->
{/* JS comment syntax is also valid! */}


<Banner />
<h1>Hello, world!</h1>


<!-- Use props and other variables from the component script: -->
<p>{title}</p>


<!-- Delay component rendering and provide fallback loading content: -->
<Avatar server:defer>
  <svg slot="fallback" class="generic-avatar" transition:name="avatar">...</svg>
</Avatar>


<!-- Include other UI framework components with a `client:` directive to hydrate: -->
<ReactPokemonComponent client:visible />


<!-- Mix HTML with JavaScript expressions, similar to JSX: -->
<ul>
  {myFavoritePokemon.map((data) => <li>{data.name}</li>)}
</ul>


<!-- Use a template directive to build class names from multiple strings or even objects! -->
<p class:list={["add", "dynamic", { classNames: true }]} />
```

## Component-based design

[Section titled “Component-based design”](#component-based-design)

Components are designed to be **reusable** and **composable**. You can use components inside of other components to build more and more advanced UI. For example, a `Button` component could be used to create a `ButtonGroup` component:

src/components/ButtonGroup.astro

```astro
---
import Button from './Button.astro';
---
<div>
  <Button title="Button 1" />
  <Button title="Button 2" />
  <Button title="Button 3" />
</div>
```

## Component Props

[Section titled “Component Props”](#component-props)

An Astro component can define and accept props. These props then become available to the component template for rendering HTML. Props are available on the `Astro.props` global in your frontmatter script.

Here is an example of a component that receives a `greeting` prop and a `name` prop. Notice that the props to be received are destructured from the global `Astro.props` object.

src/components/GreetingHeadline.astro

```astro
---
// Usage: <GreetingHeadline greeting="Howdy" name="Partner" />
const { greeting, name } = Astro.props;
---
<h2>{greeting}, {name}!</h2>
```

This component, when imported and rendered in other Astro components, layouts or pages, can pass these props as attributes:

src/components/GreetingCard.astro

```astro
---
import GreetingHeadline from './GreetingHeadline.astro';
const name = 'Astro';
---
<h1>Greeting Card</h1>
<GreetingHeadline greeting="Hi" name={name} />
<p>I hope you have a wonderful day!</p>
```

You can also define your props with TypeScript with a `Props` type interface. Astro will automatically pick up the `Props` interface in your frontmatter and give type warnings/errors. These props can also be given default values when destructured from `Astro.props`.

src/components/GreetingHeadline.astro

```diff
---
+interface Props {
+  name: string;
+  greeting?: string;
+}


const { greeting = "Hello", name } = Astro.props;
---
<h2>{greeting}, {name}!</h2>
```

Component props can be given default values to use when none are provided.

src/components/GreetingHeadline.astro

```astro
---
const { greeting = "Hello", name = "Astronaut" } = Astro.props;
---
<h2>{greeting}, {name}!</h2>
```

## Slots

[Section titled “Slots”](#slots)

The `<slot />` element is a placeholder for external HTML content, allowing you to inject (or “slot”) child elements from other files into your component template.

By default, all child elements passed to a component will be rendered in its `<slot />`.

Note

Unlike *props*, which are attributes passed to an Astro component available for use throughout your component with `Astro.props`, *slots* render child HTML elements where they are written.

src/components/Wrapper.astro

```astro
---
import Header from './Header.astro';
import Logo from './Logo.astro';
import Footer from './Footer.astro';


const { title } = Astro.props;
---
<div id="content-wrapper">
  <Header />
  <Logo />
  <h1>{title}</h1>
  <slot />  <!-- children will go here -->
  <Footer />
</div>
```

src/pages/fred.astro

```astro
---
import Wrapper from '../components/Wrapper.astro';
---
<Wrapper title="Fred's Page">
  <h2>All about Fred</h2>
  <p>Here is some stuff about Fred.</p>
</Wrapper>
```

This pattern is the basis of an [Astro layout component](/en/basics/layouts/): an entire page of HTML content can be “wrapped” with `<SomeLayoutComponent></SomeLayoutComponent>` tags and sent to the component to render inside of common page elements defined there.

See the [`Astro.slots` utility functions](/en/reference/astro-syntax/#astroslots) for more ways to access and render slot content.

### Named Slots

[Section titled “Named Slots”](#named-slots)

An Astro component can also have named slots. This allows you to pass only HTML elements with the corresponding slot name into a slot’s location.

Slots are named using the `name` attribute:

src/components/Wrapper.astro

```astro
---
import Header from './Header.astro';
import Logo from './Logo.astro';
import Footer from './Footer.astro';


const { title } = Astro.props;
---
<div id="content-wrapper">
  <Header />
  <!--  children with the `slot="after-header"` attribute will go here -->
  <slot name="after-header" />
  <Logo />
  <h1>{title}</h1>
  <!--  children without a `slot`, or with `slot="default"` attribute will go here -->
  <slot />
  <Footer />
  <!--  children with the `slot="after-footer"` attribute will go here -->
  <slot name="after-footer" />
</div>
```

To inject HTML content into a particular slot, use the `slot` attribute on any child element to specify the name of the slot. All other child elements of the component will be injected into the default (unnamed) `<slot />`.

src/pages/fred.astro

```astro
---
import Wrapper from '../components/Wrapper.astro';
---
<Wrapper title="Fred's Page">
  <img src="https://my.photo/fred.jpg" slot="after-header" />
  <h2>All about Fred</h2>
  <p>Here is some stuff about Fred.</p>
  <p slot="after-footer">Copyright 2022</p>
</Wrapper>
```

Tip

Use a `slot="my-slot"` attribute on the child element that you want to pass through to a matching `<slot name="my-slot" />` placeholder in your component.

To pass multiple HTML elements into a component’s `<slot/>` placeholder without a wrapping `<div>`, use the `slot=""` attribute on [Astro’s `<Fragment/>` component](/en/reference/astro-syntax/#fragments):

src/components/CustomTable.astro

```astro
---
// Create a custom table with named slot placeholders for header and body content
---
<table class="bg-white">
  <thead class="sticky top-0 bg-white"><slot name="header" /></thead>
  <tbody class="[&_tr:nth-child(odd)]:bg-gray-100"><slot name="body" /></tbody>
</table>
```

Inject multiple rows and columns of HTML content using a `slot=""` attribute to specify the `"header"` and `"body"` content. Individual HTML elements can also be styled:

src/components/StockTable.astro

```astro
---
import CustomTable from './CustomTable.astro';
---
<CustomTable>
  <Fragment slot="header"> <!-- pass table header -->
    <tr><th>Product name</th><th>Stock units</th></tr>
  </Fragment>


  <Fragment slot="body"> <!-- pass table body -->
    <tr><td>Flip-flops</td><td>64</td></tr>
    <tr><td>Boots</td><td>32</td></tr>
    <tr><td>Sneakers</td><td class="text-red-500">0</td></tr>
  </Fragment>
</CustomTable>
```

Note that named slots must be an immediate child of the component. You cannot pass named slots through nested elements.

Tip

Named slots can also be passed to [UI framework components](/en/guides/framework-components/)!

Note

It is not possible to dynamically generate an Astro slot name, such as within a [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) function. If this feature is needed within UI framework components, it might be best to generate these dynamic slots within the framework itself.

### Fallback Content for Slots

[Section titled “Fallback Content for Slots”](#fallback-content-for-slots)

Slots can also render **fallback content**. When there are no matching children passed to a slot, a `<slot />` element will render its own placeholder children.

src/components/Wrapper.astro

```astro
---
import Header from './Header.astro';
import Logo from './Logo.astro';
import Footer from './Footer.astro';


const { title } = Astro.props;
---
<div id="content-wrapper">
  <Header />
  <Logo />
  <h1>{title}</h1>
  <slot>
    <p>This is my fallback content, if there is no child passed into slot</p>
  </slot>
  <Footer />
</div>
```

Fallback content will only be displayed when there are no matching elements with the `slot="name"` attribute being passed in to a named slot.

Astro will pass an empty slot when a slot element exists but has no content to pass. Fallback content cannot be used as a default when an empty slot is passed. Fallback content is only displayed when no slot element can be found.

### Transferring slots

[Section titled “Transferring slots”](#transferring-slots)

Slots can be transferred to other components. For example, when creating nested layouts:

src/layouts/BaseLayout.astro

```astro
---
---
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <slot name="head" />
  </head>
  <body>
    <slot />
  </body>
</html>
```

src/layouts/HomeLayout.astro

```astro
---
import BaseLayout from './BaseLayout.astro';
---
<BaseLayout>
  <slot name="head" slot="head" />
  <slot />
</BaseLayout>
```

Note

Named slots can be transferred to another component using both the `name` and `slot` attributes on a `<slot />` tag.

Now, the default and `head` slots passed to `HomeLayout` will be transferred to the `BaseLayout` parent.

src/pages/index.astro

```astro
---
import HomeLayout from '../layouts/HomeLayout.astro';
---
<HomeLayout>
  <title slot="head">Astro</title>
  <h1>Astro</h1>
</HomeLayout>
```

## HTML Components

[Section titled “HTML Components”](#html-components)

Astro supports importing and using `.html` files as components or placing these files within the `src/pages/` subdirectory as pages. You may want to use HTML components if you’re reusing code from an existing site built without a framework, or if you want to ensure that your component has no dynamic features.

HTML components must contain only valid HTML, and therefore lack key Astro component features:

* They don’t support frontmatter, server-side imports, or dynamic expressions.
* Any `<script>` tags are left unbundled, treated as if they had an [`is:inline` directive](/en/reference/directives-reference/#isinline).
* They can only [reference assets that are in the `public/` folder](/en/basics/project-structure/#public).

Note

A [`<slot />` element](/en/basics/astro-components/#slots) inside an HTML component will work as it would in an Astro component. In order to use the [HTML Web Component Slot](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot) element instead, add `is:inline` to your `<slot>` element.

## Next Steps

[Section titled “Next Steps”](#next-steps)

Read more about using [UI framework components](/en/guides/framework-components/) in your Astro project.

# Pages

> An introduction to Astro pages.

**Pages** are files that live in the `src/pages/` subdirectory of your Astro project. They are responsible for handling routing, data loading, and overall page layout for every page in your website.

## Supported page files

[Section titled “Supported page files”](#supported-page-files)

Astro supports the following file types in the `src/pages/` directory:

* [`.astro`](#astro-pages)
* [`.md`](#markdownmdx-pages)
* `.mdx` (with the [MDX Integration installed](/en/guides/integrations-guide/mdx/#installation))
* [`.html`](#html-pages)
* `.js`/`.ts` (as [endpoints](/en/guides/endpoints/))

## File-based routing

[Section titled “File-based routing”](#file-based-routing)

Astro leverages a routing strategy called **file-based routing**. Each file in your `src/pages/` directory becomes an endpoint on your site based on its file path.

A single file can also generate multiple pages using [dynamic routing](/en/guides/routing/#dynamic-routes). This allows you to create pages even if your content lives outside of the special `/pages/` directory, such as in a [content collection](/en/guides/content-collections/) or a [CMS](/en/guides/cms/).

Read more about [Routing in Astro](/en/guides/routing/).

### Link between pages

[Section titled “Link between pages”](#link-between-pages)

Write standard HTML [`<a>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) in your Astro pages to link to other pages on your site. Use a **URL path relative to your root domain** as your link, not a relative file path.

For example, to link to `https://example.com/authors/sonali/` from any other page on `example.com`:

src/pages/index.astro

```astro
Read more <a href="/authors/sonali/">about Sonali</a>.
```

## Astro Pages

[Section titled “Astro Pages”](#astro-pages)

Astro pages use the `.astro` file extension and support the same features as [Astro components](/en/basics/astro-components/).

src/pages/index.astro

```astro
---
---
<html lang="en">
  <head>
    <title>My Homepage</title>
  </head>
  <body>
    <h1>Welcome to my website!</h1>
  </body>
</html>
```

A page must produce a full HTML document. If not explicitly included, Astro will add the necessary `<!DOCTYPE html>` declaration and `<head>` content to any `.astro` component located within `src/pages/` by default. You can opt-out of this behavior on a per-component basis by marking it as a [partial](#page-partials) page.

To avoid repeating the same HTML elements on every page, you can move common `<head>` and `<body>` elements into your own [layout components](/en/basics/layouts/). You can use as many or as few layout components as you’d like.

src/pages/index.astro

```astro
---
import MySiteLayout from "../layouts/MySiteLayout.astro";
---
<MySiteLayout>
  <p>My page content, wrapped in a layout!</p>
</MySiteLayout>
```

Read more about [layout components](/en/basics/layouts/) in Astro.

## Markdown/MDX Pages

[Section titled “Markdown/MDX Pages”](#markdownmdx-pages)

Astro also treats any Markdown (`.md`) files inside of `src/pages/` as pages in your final website. If you have the [MDX Integration installed](/en/guides/integrations-guide/mdx/#installation), it also treats MDX (`.mdx`) files the same way.

Tip

Consider creating [content collections](/en/guides/content-collections/) instead of pages for directories of related Markdown files that share a similar structure, such as blog posts or product items.

Markdown files can use the special `layout` frontmatter property to specify a [layout component](/en/basics/layouts/) that will wrap their Markdown content in a full `<html>...</html>` page document.

src/pages/page.md

```md
---
layout: ../layouts/MySiteLayout.astro
title: My Markdown page
---
# Title


This is my page, written in **Markdown.**
```

Read more about [Markdown](/en/guides/markdown-content/) in Astro.

## HTML Pages

[Section titled “HTML Pages”](#html-pages)

Files with the `.html` file extension can be placed in the `src/pages/` directory and used directly as pages on your site. Note that some key Astro features are not supported in [HTML Components](/en/basics/astro-components/#html-components).

## Custom 404 Error Page

[Section titled “Custom 404 Error Page”](#custom-404-error-page)

For a custom 404 error page, you can create a `404.astro` or `404.md` file in `src/pages`.

This will build to a `404.html` page. Most [deploy services](/en/guides/deploy/) will find and use it.

## Custom 500 Error Page

[Section titled “Custom 500 Error Page”](#custom-500-error-page)

For a custom 500 error page to show for pages that are [rendered on demand](/en/guides/on-demand-rendering/), create the file `src/pages/500.astro`. This custom page is not available for prerendered pages.

If an error occurs rendering this page, your host’s default 500 error page will be shown to your visitor.

**Added in:** `astro@4.10.3`

During development, if you have a `500.astro`, the error thrown at runtime is logged in your terminal, as opposed to being shown in the error overlay.

### `error`

[Section titled “error”](#error)

**Added in:** `astro@4.11.0`

`src/pages/500.astro` is a special page that is automatically passed an `error` prop for any error thrown during rendering. This allows you to use the details of an error (e.g. from a page, from middleware, etc.) to display information to your visitor.

The `error` prop’s data type can be anything, which may affect how you type or use the value in your code:

src/pages/500.astro

```astro
---
interface Props {
  error: unknown;
}


const { error } = Astro.props;
---
<div>{error instanceof Error ? error.message : "Unknown error"}</div>
```

To avoid leaking sensitive information when displaying content from the `error` prop, consider evaluating the error first, and returning appropriate content based on the error thrown. For example, you should avoid displaying the error’s stack as it contains information about how your code is structured on the server.

## Page Partials

[Section titled “Page Partials”](#page-partials)

**Added in:** `astro@3.4.0`

Caution

Page partials are intended to be used in conjunction with a front-end library, such as [htmx](https://htmx.org/) or [Unpoly](https://unpoly.com/). You can also use them if you are comfortable writing low-level front-end JavaScript. For this reason they are an advanced feature.

Additionally, partials should not be used if the component contains scoped styles or scripts, as these elements will be stripped from the HTML output. If you need scoped styles, it is better to use regular, non-partial pages along with a frontend library that knows how to merge the contents into the head.

Partials are page components located within `src/pages/` that are not intended to render as full pages.

Like components located outside of this folder, these files do not automatically include the `<!DOCTYPE html>` declaration, nor any `<head>` content such as scoped styles and scripts.

However, because they are located in the special `src/pages/` directory, the generated HTML is available at a URL corresponding to its file path. This allows a rendering library (e.g. [htmx](https://htmx.org/), [Stimulus](https://stimulus.hotwired.dev/), [jQuery](https://jquery.com/)) to access it on the client and load sections of HTML dynamically on a page without a browser refresh or page navigation.

Partials, when combined with a rendering library, provide an alternative to [Astro islands](/en/concepts/islands/) and [`<script>` tags](/en/guides/client-side-scripts/) for building dynamic content in Astro.

Page files that can export a value for [`partial`](/en/reference/routing-reference/#partial) (e.g. `.astro` and `.mdx`, but not `.md`) can be marked as partials.

src/pages/partial.astro

```diff
---
+export const partial = true;
---
<li>I'm a partial!</li>
```

### Using with a library

[Section titled “Using with a library”](#using-with-a-library)

Partials are used to dynamically update a section of a page using a library such as [htmx](https://htmx.org/).

The following example shows an `hx-post` attribute set to a partial’s URL. The content from the partial page will be used to update the targeted HTML element on this page.

src/pages/index.astro

```astro
<html>
  <head>
    <title>My page</title>
    <script src="https://unpkg.com/htmx.org@1.9.6"
      integrity="sha384-FhXw7b6AlE/jyjlZH5iHa/tTe9EpJ1Y55RjcgPbjeWMskSxZt1v9qkxLJWNJaGni"
      crossorigin="anonymous"></script>
  </head>
  <body>
    <section>
      <div id="parent-div">Target here</div>


      <button hx-post="/partials/clicked/"
        hx-trigger="click"
        hx-target="#parent-div"
        hx-swap="innerHTML"
      >
        Click Me!
      </button>
    </section>
  </body>
</html>
```

The `.astro` partial must exist at the corresponding file path, and include an export defining the page as a partial:

src/pages/partials/clicked.astro

```astro
---
export const partial = true;
---
<div>I was clicked!</div>
```

See the [htmx documentation](https://htmx.org/docs/) for more details on using htmx.

# Layouts

> An introduction to layouts in Astro.

**Layouts** are [Astro components](/en/basics/astro-components/) used to provide a reusable UI structure, such as a page template.

We conventionally use the term “layout” for Astro components that provide common UI elements shared across pages such as headers, navigation bars, and footers. A typical Astro layout component provides [Astro, Markdown or MDX pages](/en/basics/astro-pages/) with:

* a **page shell** (`<html>`, `<head>` and `<body>` tags)
* a [**`<slot />`**](/en/basics/astro-components/#slots) to specify where individual page content should be injected.

But, there is nothing special about a layout component! They can [accept props](/en/basics/astro-components/#component-props) and [import and use other components](/en/basics/astro-components/#component-structure) like any other Astro component. They can include [UI frameworks components](/en/guides/framework-components/) and [client-side scripts](/en/guides/client-side-scripts/). They do not even have to provide a full page shell, and can instead be used as partial UI templates.

However, if a layout component does contain a page shell, its `<html>` element must be the parent of all other elements in the component.

Layout components are commonly placed in a `src/layouts` directory in your project for organization, but this is not a requirement; you can choose to place them anywhere in your project. You can even colocate layout components alongside your pages by [prefixing the layout names with `_`](/en/guides/routing/#excluding-pages).

## Sample Layout

[Section titled “Sample Layout”](#sample-layout)

src/layouts/MySiteLayout.astro

```astro
---
import BaseHead from '../components/BaseHead.astro';
import Footer from '../components/Footer.astro';
const { title } = Astro.props;
---
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <BaseHead title={title}/>
  </head>
  <body>
    <nav>
      <a href="#">Home</a>
      <a href="#">Posts</a>
      <a href="#">Contact</a>
    </nav>
    <h1>{title}</h1>
    <article>
      <slot /> <!-- your content is injected here -->
    </article>
    <Footer />
  </body>
  <style>
    h1 {
      font-size: 2rem;
    }
  </style>
</html>
```

src/pages/index.astro

```astro
---
import MySiteLayout from '../layouts/MySiteLayout.astro';
---
<MySiteLayout title="Home Page">
  <p>My page content, wrapped in a layout!</p>
</MySiteLayout>
```

Learn more about [slots](/en/basics/astro-components/#slots).

## Using TypeScript with layouts

[Section titled “Using TypeScript with layouts”](#using-typescript-with-layouts)

Any Astro layout can be modified to introduce type safety & autocompletion by providing the types for your props:

src/components/MyLayout.astro

```diff
---
+interface Props {
+  title: string;
+  description: string;
+  publishDate: string;
+  viewCount: number;
+}
const { title, description, publishDate, viewCount } = Astro.props;
---
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="description" content={description}>
    <title>{title}</title>
  </head>
  <body>
    <header>
      <p>Published on {publishDate}</p>
      <p>Viewed by {viewCount} folks</p>
    </header>
    <main>
      <slot />
    </main>
  </body>
</html>
```

## Markdown Layouts

[Section titled “Markdown Layouts”](#markdown-layouts)

Page layouts are especially useful for individual Markdown pages which otherwise would not have any page formatting.

Astro provides a special `layout` frontmatter property intended for [individual `.md` files located within `src/pages/` using file-based routing](/en/guides/markdown-content/#individual-markdown-pages) to specify which `.astro` component to use as the page layout. This component allows you to provide `<head>` content like meta tags (e.g. `<meta charset="utf-8">`) and styles for the Markdown page. By default, this specified component can automatically access data from the Markdown file.

This is not recognized as a special property when using [content collections](/en/guides/content-collections/) to query and render your content.

src/pages/page.md

```markdown
---
layout: ../layouts/BlogPostLayout.astro
title: "Hello, World!"
author: "Matthew Phillips"
date: "09 Aug 2022"
---
All frontmatter properties are available as props to an Astro layout component.


The `layout` property is the only special one provided by Astro.


You can use it in Markdown files located within `src/pages/`.
```

A typical layout for a Markdown page includes:

1. The `frontmatter` prop to access the Markdown page’s frontmatter and other data.
2. A default [`<slot />`](/en/basics/astro-components/#slots) to indicate where the page’s Markdown content should be rendered.

src/layouts/BlogPostLayout.astro

```astro
---
// 1. The frontmatter prop gives access to frontmatter and other data
const { frontmatter } = Astro.props;
---
<html>
  <head>
    <!-- Add other Head elements here, like styles and meta tags. -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8">
    <title>{frontmatter.title}</title>
  </head>
  <body>
    <!-- Add other UI components here, like common headers and footers. -->
    <h1>{frontmatter.title} by {frontmatter.author}</h1>
    <!-- 2. Rendered HTML will be passed into the default slot. -->
    <slot />
    <p>Written on: {frontmatter.date}</p>
  </body>
</html>
```

You can set a layout’s [`Props` type](/en/guides/typescript/#component-props) with the `MarkdownLayoutProps` helper:

src/layouts/BlogPostLayout.astro

```diff
---
+import type { MarkdownLayoutProps } from 'astro';


+type Props = MarkdownLayoutProps<{
  +// Define frontmatter props here
+  title: string;
+  author: string;
+  date: string;
+}>;


// Now, `frontmatter`, `url`, and other Markdown layout properties
// are accessible with type safety
const { frontmatter, url } = Astro.props;
---
<html>
  <head>
    <meta charset="utf-8">
    <link rel="canonical" href={new URL(url, Astro.site).pathname}>
    <title>{frontmatter.title}</title>
  </head>
  <body>
    <h1>{frontmatter.title} by {frontmatter.author}</h1>
    <slot />
    <p>Written on: {frontmatter.date}</p>
  </body>
</html>
```

### Markdown Layout Props

[Section titled “Markdown Layout Props”](#markdown-layout-props)

A Markdown layout will have access to the following information via `Astro.props`:

* **`file`** - The absolute path of this file (e.g. `/home/user/projects/.../file.md`).

* **`url`** - The URL of the page (e.g. `/en/guides/markdown-content`).

* **`frontmatter`** - All frontmatter from the Markdown or MDX document.

  * **`frontmatter.file`** - The same as the top-level `file` property.
  * **`frontmatter.url`** - The same as the top-level `url` property.

* **`headings`** - A list of headings (`h1 -> h6`) in the Markdown or MDX document with associated metadata. This list follows the type: `{ depth: number; slug: string; text: string }[]`.

* **`rawContent()`** - A function that returns the raw Markdown document as a string.

* **`compiledContent()`** - An async function that returns the Markdown document compiled to an HTML string.

Note

A Markdown layout will have access to all the Markdown file’s [available properties](/en/guides/markdown-content/#available-properties) from `Astro.props` **with two key differences:**

* Heading information (i.e. `h1 -> h6` elements) is available via the `headings` array, rather than a `getHeadings()` function.

* `file` and `url` are *also* available as nested `frontmatter` properties (i.e. `frontmatter.url` and `frontmatter.file`).

### Importing Layouts Manually (MDX)

[Section titled “Importing Layouts Manually (MDX)”](#importing-layouts-manually-mdx)

You can also use the special Markdown layout property in the frontmatter of MDX files to pass `frontmatter` and `headings` props directly to a specified layout component in the same way.

To pass information to your MDX layout that does not (or cannot) exist in your frontmatter, you can instead import and use a `<Layout />` component. This works like any other Astro component, and will not receive any props automatically. Pass it any necessary props directly:

src/pages/posts/first-post.mdx

```diff
---
-layout: ../../layouts/BaseLayout.astro
title: 'My first MDX post'
publishDate: '21 September 2022'
---
+import BaseLayout from '../../layouts/BaseLayout.astro';


export function fancyJsHelper() {
  return "Try doing that with YAML!";
}


<BaseLayout title={frontmatter.title} fancyJsHelper={fancyJsHelper}>
  Welcome to my new Astro blog, using MDX!
</BaseLayout>
```

Then, your values are available to you through `Astro.props` in your layout, and your MDX content will be injected into the page where your `<slot />` component is written:

src/layouts/BaseLayout.astro

```astro
---
const { title, fancyJsHelper } = Astro.props;
---
<html>
  <head>
    <!-- -->
    <meta charset="utf-8">
  </head>
  <body>
    <!-- -->
    <h1>{title}</h1>
    <slot /> <!-- your content is injected here -->
    <p>{fancyJsHelper()}</p>
    <!-- -->
  </body>
</html>
```

When using any layout (either through the frontmatter `layout` property or by importing a layout), you must include the `<meta charset="utf-8">` tag in your layout as Astro will no longer add it automatically to your MDX page.

Learn more about Astro’s Markdown and MDX support in our [Markdown guide](/en/guides/markdown-content/).

## Nesting Layouts

[Section titled “Nesting Layouts”](#nesting-layouts)

Layout components do not need to contain an entire page worth of HTML. You can break your layouts into smaller components, and combine layout components to create even more flexible, page templates. This pattern is useful when you want to share some code across multiple layouts.

For example, a `BlogPostLayout.astro` layout component could style a post’s title, date and author. Then, a site-wide `BaseLayout.astro` could handle the rest of your page template, like navigation, footers, SEO meta tags, global styles, and fonts. You can also pass props received from your post to another layout, just like any other nested component.

src/layouts/BlogPostLayout.astro

```astro
---
import BaseLayout from './BaseLayout.astro';
const { frontmatter } = Astro.props;
---
<BaseLayout url={frontmatter.url}>
  <h1>{frontmatter.title}</h1>
  <h2>Post author: {frontmatter.author}</h2>
  <slot />
</BaseLayout>
```

# Contribute to Astro

> How to get involved and contribute to Astro.

We welcome contributions of any size and contributors of any skill level. As an open-source project, we believe in giving back to our contributors. We are happy to help with guidance on PRs, technical writing, and turning any feature idea into a reality.

Open Issues

Browse [all of Astro’s open GitHub issues tagged `help wanted` and `good first issues`](https://github.com/search?q=org%3Awithastro+label%3A%22good+first+issue%22%2C%22help+wanted%22%2C+state%3Aopen\&type=issues) for all the code repositories: Astro code, documentation, Starlight, Astro websites, language tools, GitHub Actions, bots, the compiler… there are lots of places to contribute!

Want to get even more involved? See our [Governance doc](https://github.com/withastro/.github/blob/main/GOVERNANCE.md) for detailed descriptions of different roles, maintainer nomination processes, code review processes, and Code of Conduct enforcement.

## Ways to Contribute

[Section titled “Ways to Contribute”](#ways-to-contribute)

### Project repositories

[Section titled “Project repositories”](#project-repositories)

There are lots of ways to contribute to the Astro Project! Every Astro repository has a README with a link to a `CONTRIBUTING.md` file in the root of the project.

Visit [Astro’s GitHub profile](https://github.com/withastro) to find the repositories for:

* The [main Astro codebase](https://github.com/withastro/astro), including official integrations and starter templates.

* [Astro Docs](https://github.com/withastro/docs), an entire Astro website! Contribute not just written content, but also Astro code addressing a11y, CSS, UI, and UX concerns. We also make our documentation available in several languages, so we need help translating the entire site.

* The [Astro compiler](https://github.com/withastro/compiler), written in Go, distributed as WASM.

* Astro’s [language tools](https://github.com/withastro/language-tools), the editor tooling required for the Astro language (`.astro` files).

* [Starlight](https://github.com/withastro/starlight), Astro’s official documentation framework.

* The [Astro Roadmap](https://github.com/withastro/roadmap) where the future of Astro is shaped! Ideas, suggestions, and formal RFC proposals for the Astro project.

### Types of contributions

[Section titled “Types of contributions”](#types-of-contributions)

In addition to contributing your own code or content, you can also make a huge contribution by getting involved by leaving review comments on PRs, adding ideas in existing GitHub Issues and Discussions, and participating in our “Pinned” issue maintenance tasks!

Every PR, especially translation PRs, needs reviewers! Reviewing PRs and leaving comments, suggestions, or an approving “LGTM!” (“Looks Good To Me!”) is a great way to get started in any repository, and to learn more about Astro.

We also have a very active [Discord](https://astro.build/chat) community! We value the contributions of those who welcome new members, answer support questions, and share what they have built with and for Astro! Beyond traditional GitHub contributions, Astro recognizes and supports community members who engage with our community, share Astro in blog posts, videos and conference talks, and help maintain the health of our community.

## Contributing to Docs

[Section titled “Contributing to Docs”](#contributing-to-docs)

We have several guides available to assist you with contributing to Astro Docs.

Whether it’s your very first contribution to open-source, or you need to add docs for the new Astro feature you just built, or you’re an experienced translator looking for the next page to translate, or you’d like to learn more about helping as a PR reviewer… we’ve got you covered!

Please visit our dedicated site [*Astro Docs* Docs](https://contribute.docs.astro.build), where you’ll find our documentation to help you contribute to Astro Docs as a typo-fixer, a writer, a translator, a feature-builder, and even as a PR reviewer.

## Our contributors

[Section titled “Our contributors”](#our-contributors)

These docs are brought to you by all these helpful people. [Join us on GitHub!](https://github.com/withastro/docs)

<!-- Thanks to @5t3ph for https://smolcss.dev/#smol-avatar-list! -->

* [![jsparkdev](https://avatars.githubusercontent.com/u/39112954?s=64 "jsparkdev")](https://github.com/jsparkdev)
* [![ArmandPhilippot](https://avatars.githubusercontent.com/u/59021693?s=64 "ArmandPhilippot")](https://github.com/ArmandPhilippot)
* [![sarah11918](https://avatars.githubusercontent.com/u/5098874?s=64 "sarah11918")](https://github.com/sarah11918)
* [![dreyfus92](https://avatars.githubusercontent.com/u/85648028?s=64 "dreyfus92")](https://github.com/dreyfus92)
* [![Nin3lee](https://avatars.githubusercontent.com/u/30520689?s=64 "Nin3lee")](https://github.com/Nin3lee)
* [![delucis](https://avatars.githubusercontent.com/u/357379?s=64 "delucis")](https://github.com/delucis)
* [![liruifengv](https://avatars.githubusercontent.com/u/25167721?s=64 "liruifengv")](https://github.com/liruifengv)
* [![astrobot-houston](https://avatars.githubusercontent.com/u/108291165?s=64 "astrobot-houston")](https://github.com/astrobot-houston)
* [![Waxer59](https://avatars.githubusercontent.com/u/78129249?s=64 "Waxer59")](https://github.com/Waxer59)
* [![100gle](https://avatars.githubusercontent.com/u/36526527?s=64 "100gle")](https://github.com/100gle)
* [![huyikai](https://avatars.githubusercontent.com/u/25839948?s=64 "huyikai")](https://github.com/huyikai)
* [![yanthomasdev](https://avatars.githubusercontent.com/u/61414485?s=64 "yanthomasdev")](https://github.com/yanthomasdev)
* [![thomasbnt](https://avatars.githubusercontent.com/u/14293805?s=64 "thomasbnt")](https://github.com/thomasbnt)
* [![morinokami](https://avatars.githubusercontent.com/u/7889778?s=64 "morinokami")](https://github.com/morinokami)
* [![FredKSchott](https://avatars.githubusercontent.com/u/622227?s=64 "FredKSchott")](https://github.com/FredKSchott)
* [![McFlyPartages](https://avatars.githubusercontent.com/u/44530252?s=64 "McFlyPartages")](https://github.com/McFlyPartages)
* [![mearashadowfax](https://avatars.githubusercontent.com/u/125820963?s=64 "mearashadowfax")](https://github.com/mearashadowfax)
* [![kevinzunigacuellar](https://avatars.githubusercontent.com/u/46791833?s=64 "kevinzunigacuellar")](https://github.com/kevinzunigacuellar)
* [![Jutanium](https://avatars.githubusercontent.com/u/4033662?s=64 "Jutanium")](https://github.com/Jutanium)
* [![hippotastic](https://avatars.githubusercontent.com/u/6137925?s=64 "hippotastic")](https://github.com/hippotastic)
* [![viniciusdeliz](https://avatars.githubusercontent.com/u/5748616?s=64 "viniciusdeliz")](https://github.com/viniciusdeliz)
* [![Alynva](https://avatars.githubusercontent.com/u/12958674?s=64 "Alynva")](https://github.com/Alynva)
* [![TheOtterlord](https://avatars.githubusercontent.com/u/64310361?s=64 "TheOtterlord")](https://github.com/TheOtterlord)
* [![bholmesdev](https://avatars.githubusercontent.com/u/51384119?s=64 "bholmesdev")](https://github.com/bholmesdev)
* [![trueberryless](https://avatars.githubusercontent.com/u/99918022?s=64 "trueberryless")](https://github.com/trueberryless)
* [![Chrissdroid](https://avatars.githubusercontent.com/u/29927270?s=64 "Chrissdroid")](https://github.com/Chrissdroid)
* [![AitorMT](https://avatars.githubusercontent.com/u/25897764?s=64 "AitorMT")](https://github.com/AitorMT)
* [![kecrily](https://avatars.githubusercontent.com/u/45708948?s=64 "kecrily")](https://github.com/kecrily)
* [![jp-knj](https://avatars.githubusercontent.com/u/70939128?s=64 "jp-knj")](https://github.com/jp-knj)
* [![ematipico](https://avatars.githubusercontent.com/u/602478?s=64 "ematipico")](https://github.com/ematipico)
* [![vrabe](https://avatars.githubusercontent.com/u/8216525?s=64 "vrabe")](https://github.com/vrabe)
* [![kyosuke](https://avatars.githubusercontent.com/u/13069?s=64 "kyosuke")](https://github.com/kyosuke)
* [![Fryuni](https://avatars.githubusercontent.com/u/11063910?s=64 "Fryuni")](https://github.com/Fryuni)
* [![jasikpark](https://avatars.githubusercontent.com/u/10626596?s=64 "jasikpark")](https://github.com/jasikpark)
* [![alexnguyennz](https://avatars.githubusercontent.com/u/54233296?s=64 "alexnguyennz")](https://github.com/alexnguyennz)
* [![ElianCodes](https://avatars.githubusercontent.com/u/15145918?s=64 "ElianCodes")](https://github.com/ElianCodes)
* [![Princesseuh](https://avatars.githubusercontent.com/u/3019731?s=64 "Princesseuh")](https://github.com/Princesseuh)
* [![matthewp](https://avatars.githubusercontent.com/u/361671?s=64 "matthewp")](https://github.com/matthewp)
* [![jonathantneal](https://avatars.githubusercontent.com/u/188426?s=64 "jonathantneal")](https://github.com/jonathantneal)
* [![agustinmulet](https://avatars.githubusercontent.com/u/31162600?s=64 "agustinmulet")](https://github.com/agustinmulet)
* [![at-the-vr](https://avatars.githubusercontent.com/u/88548999?s=64 "at-the-vr")](https://github.com/at-the-vr)
* [![Genteure](https://avatars.githubusercontent.com/u/11240579?s=64 "Genteure")](https://github.com/Genteure)
* [![HiDeoo](https://avatars.githubusercontent.com/u/494699?s=64 "HiDeoo")](https://github.com/HiDeoo)
* [![casungo](https://avatars.githubusercontent.com/u/25723446?s=64 "casungo")](https://github.com/casungo)
* [![mingjunlu](https://avatars.githubusercontent.com/u/40516784?s=64 "mingjunlu")](https://github.com/mingjunlu)
* [![bluwy](https://avatars.githubusercontent.com/u/34116392?s=64 "bluwy")](https://github.com/bluwy)
* [![Egpereira](https://avatars.githubusercontent.com/u/12275019?s=64 "Egpereira")](https://github.com/Egpereira)
* [![natemoo-re](https://avatars.githubusercontent.com/u/7118177?s=64 "natemoo-re")](https://github.com/natemoo-re)
* [![Hanawa02](https://avatars.githubusercontent.com/u/11237366?s=64 "Hanawa02")](https://github.com/Hanawa02)
* [![aFuzzyBear](https://avatars.githubusercontent.com/u/28299972?s=64 "aFuzzyBear")](https://github.com/aFuzzyBear)
* [![JuanPabloDiaz](https://avatars.githubusercontent.com/u/25883220?s=64 "JuanPabloDiaz")](https://github.com/JuanPabloDiaz)
* [![MoustaphaDev](https://avatars.githubusercontent.com/u/81974850?s=64 "MoustaphaDev")](https://github.com/MoustaphaDev)
* [![pioupia](https://avatars.githubusercontent.com/u/49518790?s=64 "pioupia")](https://github.com/pioupia)
* [![fredoist](https://avatars.githubusercontent.com/u/7684330?s=64 "fredoist")](https://github.com/fredoist)
* [![sasoria](https://avatars.githubusercontent.com/u/7903076?s=64 "sasoria")](https://github.com/sasoria)
* [![florian-lefebvre](https://avatars.githubusercontent.com/u/69633530?s=64 "florian-lefebvre")](https://github.com/florian-lefebvre)
* [![renovate\[bot\]](https://avatars.githubusercontent.com/u/29139614?s=64 "renovate\[bot\]")](https://github.com/renovate\[bot])
* [![maxchang3](https://avatars.githubusercontent.com/u/36927158?s=64 "maxchang3")](https://github.com/maxchang3)
* [![piro-hiroki](https://avatars.githubusercontent.com/u/103011756?s=64 "piro-hiroki")](https://github.com/piro-hiroki)
* [![sarasate](https://avatars.githubusercontent.com/u/1528803?s=64 "sarasate")](https://github.com/sarasate)
* [![mxuee](https://avatars.githubusercontent.com/u/232656354?s=64 "mxuee")](https://github.com/mxuee)
* [![JuanM04](https://avatars.githubusercontent.com/u/16712703?s=64 "JuanM04")](https://github.com/JuanM04)
* [![mrienstra](https://avatars.githubusercontent.com/u/669326?s=64 "mrienstra")](https://github.com/mrienstra)
* [![bjohansebas](https://avatars.githubusercontent.com/u/103585995?s=64 "bjohansebas")](https://github.com/bjohansebas)
* [![VoxelMC](https://avatars.githubusercontent.com/u/20650404?s=64 "VoxelMC")](https://github.com/VoxelMC)
* [![ascorbic](https://avatars.githubusercontent.com/u/213306?s=64 "ascorbic")](https://github.com/ascorbic)
* [![dragomano](https://avatars.githubusercontent.com/u/229402?s=64 "dragomano")](https://github.com/dragomano)
* [![kirii86](https://avatars.githubusercontent.com/u/47194884?s=64 "kirii86")](https://github.com/kirii86)
* [![glopzel](https://avatars.githubusercontent.com/u/74939915?s=64 "glopzel")](https://github.com/glopzel)
* [![tarikrital](https://avatars.githubusercontent.com/u/52907282?s=64 "tarikrital")](https://github.com/tarikrital)
* [![antonyfaris](https://avatars.githubusercontent.com/u/11766500?s=64 "antonyfaris")](https://github.com/antonyfaris)
* [![afucher](https://avatars.githubusercontent.com/u/3756185?s=64 "afucher")](https://github.com/afucher)
* [![kimulaco](https://avatars.githubusercontent.com/u/11986753?s=64 "kimulaco")](https://github.com/kimulaco)
* [![shuuji3](https://avatars.githubusercontent.com/u/1425259?s=64 "shuuji3")](https://github.com/shuuji3)
* [![helmerdx](https://avatars.githubusercontent.com/u/11061182?s=64 "helmerdx")](https://github.com/helmerdx)
* [![DerTimonius](https://avatars.githubusercontent.com/u/103483059?s=64 "DerTimonius")](https://github.com/DerTimonius)
* [![martrapp](https://avatars.githubusercontent.com/u/94928215?s=64 "martrapp")](https://github.com/martrapp)
* [![luoingly](https://avatars.githubusercontent.com/u/101558384?s=64 "luoingly")](https://github.com/luoingly)
* [![mayank99](https://avatars.githubusercontent.com/u/9084735?s=64 "mayank99")](https://github.com/mayank99)
* [![AbrahamX3](https://avatars.githubusercontent.com/u/78459953?s=64 "AbrahamX3")](https://github.com/AbrahamX3)
* [![lilnasy](https://avatars.githubusercontent.com/u/69170106?s=64 "lilnasy")](https://github.com/lilnasy)
* [![asgoshawk](https://avatars.githubusercontent.com/u/42184309?s=64 "asgoshawk")](https://github.com/asgoshawk)
* [![clemenzi](https://avatars.githubusercontent.com/u/77632836?s=64 "clemenzi")](https://github.com/clemenzi)
* [![itskitto](https://avatars.githubusercontent.com/u/12174733?s=64 "itskitto")](https://github.com/itskitto)
* [![CaptainOfPhB](https://avatars.githubusercontent.com/u/30765485?s=64 "CaptainOfPhB")](https://github.com/CaptainOfPhB)
* [![diegognt](https://avatars.githubusercontent.com/u/181699?s=64 "diegognt")](https://github.com/diegognt)
* [![karolhas](https://avatars.githubusercontent.com/u/99908851?s=64 "karolhas")](https://github.com/karolhas)
* [![itsmatteomanf](https://avatars.githubusercontent.com/u/20746019?s=64 "itsmatteomanf")](https://github.com/itsmatteomanf)
* [![zadeviggers](https://avatars.githubusercontent.com/u/74938858?s=64 "zadeviggers")](https://github.com/zadeviggers)
* [![randomguy-2650](https://avatars.githubusercontent.com/u/150704902?s=64 "randomguy-2650")](https://github.com/randomguy-2650)
* [![yuto343](https://avatars.githubusercontent.com/u/43196286?s=64 "yuto343")](https://github.com/yuto343)
* [![Eric-llos](https://avatars.githubusercontent.com/u/85624552?s=64 "Eric-llos")](https://github.com/Eric-llos)
* [![XindiShang](https://avatars.githubusercontent.com/u/89835661?s=64 "XindiShang")](https://github.com/XindiShang)
* [![SnowDingo](https://avatars.githubusercontent.com/u/101443426?s=64 "SnowDingo")](https://github.com/SnowDingo)
* [![BryceRussell](https://avatars.githubusercontent.com/u/19967622?s=64 "BryceRussell")](https://github.com/BryceRussell)
* [![leoj3n](https://avatars.githubusercontent.com/u/990216?s=64 "leoj3n")](https://github.com/leoj3n)
* [![alexanderniebuhr](https://avatars.githubusercontent.com/u/45965090?s=64 "alexanderniebuhr")](https://github.com/alexanderniebuhr)
* [![codersjj](https://avatars.githubusercontent.com/u/44868357?s=64 "codersjj")](https://github.com/codersjj)
* [![ryuapp](https://avatars.githubusercontent.com/u/114303361?s=64 "ryuapp")](https://github.com/ryuapp)
* [![agriffard](https://avatars.githubusercontent.com/u/703248?s=64 "agriffard")](https://github.com/agriffard)
* [![anaxite](https://avatars.githubusercontent.com/u/89195061?s=64 "anaxite")](https://github.com/anaxite)
* [![apatel369](https://avatars.githubusercontent.com/u/33442948?s=64 "apatel369")](https://github.com/apatel369)
* [![yeonjulee1005](https://avatars.githubusercontent.com/u/57179957?s=64 "yeonjulee1005")](https://github.com/yeonjulee1005)
* [![teinett](https://avatars.githubusercontent.com/u/1038168?s=64 "teinett")](https://github.com/teinett)
* [![mottox2](https://avatars.githubusercontent.com/u/7007253?s=64 "mottox2")](https://github.com/mottox2)
* [![RezixDev](https://avatars.githubusercontent.com/u/128291517?s=64 "RezixDev")](https://github.com/RezixDev)
* [![OliverSpeir](https://avatars.githubusercontent.com/u/115520730?s=64 "OliverSpeir")](https://github.com/OliverSpeir)
* [![JusticeMatthew](https://avatars.githubusercontent.com/u/72817096?s=64 "JusticeMatthew")](https://github.com/JusticeMatthew)
* [![louisescher](https://avatars.githubusercontent.com/u/66965600?s=64 "louisescher")](https://github.com/louisescher)
* [![hkbertoson](https://avatars.githubusercontent.com/u/44106297?s=64 "hkbertoson")](https://github.com/hkbertoson)
* [![Eyozy](https://avatars.githubusercontent.com/u/110926935?s=64 "Eyozy")](https://github.com/Eyozy)
* [![HashCookie](https://avatars.githubusercontent.com/u/92775570?s=64 "HashCookie")](https://github.com/HashCookie)
* [![tkskto](https://avatars.githubusercontent.com/u/12536486?s=64 "tkskto")](https://github.com/tkskto)
* [![n-tong009](https://avatars.githubusercontent.com/u/66517416?s=64 "n-tong009")](https://github.com/n-tong009)
* [![autroshot](https://avatars.githubusercontent.com/u/95019875?s=64 "autroshot")](https://github.com/autroshot)
* [![Adammatthiesen](https://avatars.githubusercontent.com/u/30383579?s=64 "Adammatthiesen")](https://github.com/Adammatthiesen)
* [![crutchcorn](https://avatars.githubusercontent.com/u/9100169?s=64 "crutchcorn")](https://github.com/crutchcorn)
* [![clearlyTHUYDOAN](https://avatars.githubusercontent.com/u/22087604?s=64 "clearlyTHUYDOAN")](https://github.com/clearlyTHUYDOAN)
* [![fhiromasa](https://avatars.githubusercontent.com/u/74556046?s=64 "fhiromasa")](https://github.com/fhiromasa)
* [![magnum-zx](https://avatars.githubusercontent.com/u/46154381?s=64 "magnum-zx")](https://github.com/magnum-zx)
* [![arisa-fukuzaki](https://avatars.githubusercontent.com/u/25793187?s=64 "arisa-fukuzaki")](https://github.com/arisa-fukuzaki)
* [![caioferrarezi](https://avatars.githubusercontent.com/u/14830190?s=64 "caioferrarezi")](https://github.com/caioferrarezi)
* [![Elib27](https://avatars.githubusercontent.com/u/92606530?s=64 "Elib27")](https://github.com/Elib27)
* [![jdwilkin4](https://avatars.githubusercontent.com/u/67210629?s=64 "jdwilkin4")](https://github.com/jdwilkin4)
* [![Jothsa](https://avatars.githubusercontent.com/u/58094796?s=64 "Jothsa")](https://github.com/Jothsa)
* [![Panelinio](https://avatars.githubusercontent.com/u/139560930?s=64 "Panelinio")](https://github.com/Panelinio)
* [![palmiak](https://avatars.githubusercontent.com/u/2342458?s=64 "palmiak")](https://github.com/palmiak)
* [![sujang958](https://avatars.githubusercontent.com/u/59335584?s=64 "sujang958")](https://github.com/sujang958)
* [![NinuzIBZ](https://avatars.githubusercontent.com/u/68387835?s=64 "NinuzIBZ")](https://github.com/NinuzIBZ)
* [![tejapaturu](https://avatars.githubusercontent.com/u/37566594?s=64 "tejapaturu")](https://github.com/tejapaturu)
* [![pyronaur](https://avatars.githubusercontent.com/u/988095?s=64 "pyronaur")](https://github.com/pyronaur)
* [![milovangudelj](https://avatars.githubusercontent.com/u/49202538?s=64 "milovangudelj")](https://github.com/milovangudelj)
* [![michaelbe812](https://avatars.githubusercontent.com/u/29756792?s=64 "michaelbe812")](https://github.com/michaelbe812)
* [![wtchnm](https://avatars.githubusercontent.com/u/37726261?s=64 "wtchnm")](https://github.com/wtchnm)
* [![Pukimaa](https://avatars.githubusercontent.com/u/58347116?s=64 "Pukimaa")](https://github.com/Pukimaa)
* [![RafidMuhymin](https://avatars.githubusercontent.com/u/63650415?s=64 "RafidMuhymin")](https://github.com/RafidMuhymin)
* [![ralacerda](https://avatars.githubusercontent.com/u/19380403?s=64 "ralacerda")](https://github.com/ralacerda)
* [![chenxsan](https://avatars.githubusercontent.com/u/1091472?s=64 "chenxsan")](https://github.com/chenxsan)
* [![chalkygames123](https://avatars.githubusercontent.com/u/5608239?s=64 "chalkygames123")](https://github.com/chalkygames123)
* [![gacek1123](https://avatars.githubusercontent.com/u/78506637?s=64 "gacek1123")](https://github.com/gacek1123)
* [![minjongbaek](https://avatars.githubusercontent.com/u/48359052?s=64 "minjongbaek")](https://github.com/minjongbaek)
* [![Maxframe](https://avatars.githubusercontent.com/u/51922004?s=64 "Maxframe")](https://github.com/Maxframe)
* [![manchan4869](https://avatars.githubusercontent.com/u/65327974?s=64 "manchan4869")](https://github.com/manchan4869)
* [![staticWagomU](https://avatars.githubusercontent.com/u/34824645?s=64 "staticWagomU")](https://github.com/staticWagomU)
* [![imbant](https://avatars.githubusercontent.com/u/17983739?s=64 "imbant")](https://github.com/imbant)
* [![BassamXYZ](https://avatars.githubusercontent.com/u/100040151?s=64 "BassamXYZ")](https://github.com/BassamXYZ)
* [![garysassano](https://avatars.githubusercontent.com/u/10464497?s=64 "garysassano")](https://github.com/garysassano)
* [![bandantonio](https://avatars.githubusercontent.com/u/16765690?s=64 "bandantonio")](https://github.com/bandantonio)
* [![angelmarfil](https://avatars.githubusercontent.com/u/59626670?s=64 "angelmarfil")](https://github.com/angelmarfil)
* [![olets](https://avatars.githubusercontent.com/u/3282350?s=64 "olets")](https://github.com/olets)
* [![IgorKowalczyk](https://avatars.githubusercontent.com/u/49127376?s=64 "IgorKowalczyk")](https://github.com/IgorKowalczyk)
* [![Singebob](https://avatars.githubusercontent.com/u/24290044?s=64 "Singebob")](https://github.com/Singebob)
* [![Kenzo-Wada](https://avatars.githubusercontent.com/u/79452224?s=64 "Kenzo-Wada")](https://github.com/Kenzo-Wada)
* [![ankddev](https://avatars.githubusercontent.com/u/190183925?s=64 "ankddev")](https://github.com/ankddev)
* [![lorenzolewis](https://avatars.githubusercontent.com/u/15347255?s=64 "lorenzolewis")](https://github.com/lorenzolewis)
* [![marsidev](https://avatars.githubusercontent.com/u/56328053?s=64 "marsidev")](https://github.com/marsidev)
* [![mhstrkmp](https://avatars.githubusercontent.com/u/5558193?s=64 "mhstrkmp")](https://github.com/mhstrkmp)
* [![tinymachine](https://avatars.githubusercontent.com/u/171986?s=64 "tinymachine")](https://github.com/tinymachine)
* [![mogeko](https://avatars.githubusercontent.com/u/26341224?s=64 "mogeko")](https://github.com/mogeko)
* [![nermalcat69](https://avatars.githubusercontent.com/u/73933669?s=64 "nermalcat69")](https://github.com/nermalcat69)
* [![NightFeather0615](https://avatars.githubusercontent.com/u/77222233?s=64 "NightFeather0615")](https://github.com/NightFeather0615)
* [![Njong392](https://avatars.githubusercontent.com/u/81039882?s=64 "Njong392")](https://github.com/Njong392)
* [![AkashRajpurohit](https://avatars.githubusercontent.com/u/30044630?s=64 "AkashRajpurohit")](https://github.com/AkashRajpurohit)
* [![dorasans](https://avatars.githubusercontent.com/u/75212478?s=64 "dorasans")](https://github.com/dorasans)
* [![ktym4a](https://avatars.githubusercontent.com/u/51779800?s=64 "ktym4a")](https://github.com/ktym4a)
* [![mantaroh](https://avatars.githubusercontent.com/u/3241026?s=64 "mantaroh")](https://github.com/mantaroh)
* [![melon95](https://avatars.githubusercontent.com/u/35761035?s=64 "melon95")](https://github.com/melon95)
* [![miroim](https://avatars.githubusercontent.com/u/22488175?s=64 "miroim")](https://github.com/miroim)
* [![nokazn](https://avatars.githubusercontent.com/u/41154684?s=64 "nokazn")](https://github.com/nokazn)
* [![paulrudy](https://avatars.githubusercontent.com/u/1110792?s=64 "paulrudy")](https://github.com/paulrudy)
* [![santiemanuel](https://avatars.githubusercontent.com/u/3680835?s=64 "santiemanuel")](https://github.com/santiemanuel)
* [![openscript](https://avatars.githubusercontent.com/u/1105080?s=64 "openscript")](https://github.com/openscript)
* [![chriswburke](https://avatars.githubusercontent.com/u/362261?s=64 "chriswburke")](https://github.com/chriswburke)
* [![mitian233](https://avatars.githubusercontent.com/u/13678847?s=64 "mitian233")](https://github.com/mitian233)
* [![lostra01](https://avatars.githubusercontent.com/u/9054858?s=64 "lostra01")](https://github.com/lostra01)
* [![florluzduarte](https://avatars.githubusercontent.com/u/77161808?s=64 "florluzduarte")](https://github.com/florluzduarte)
* [![danielcuque](https://avatars.githubusercontent.com/u/81493003?s=64 "danielcuque")](https://github.com/danielcuque)
* [![guidiego](https://avatars.githubusercontent.com/u/10289071?s=64 "guidiego")](https://github.com/guidiego)
* [![JavGuerra](https://avatars.githubusercontent.com/u/6777224?s=64 "JavGuerra")](https://github.com/JavGuerra)
* [![selfire1](https://avatars.githubusercontent.com/u/70809675?s=64 "selfire1")](https://github.com/selfire1)
* [![KoriIku](https://avatars.githubusercontent.com/u/86508666?s=64 "KoriIku")](https://github.com/KoriIku)
* [![lumamontes](https://avatars.githubusercontent.com/u/60052718?s=64 "lumamontes")](https://github.com/lumamontes)
* [![marcelwenner](https://avatars.githubusercontent.com/u/28953458?s=64 "marcelwenner")](https://github.com/marcelwenner)
* [![Hopelezz](https://avatars.githubusercontent.com/u/72772558?s=64 "Hopelezz")](https://github.com/Hopelezz)
* [![ohansemmanuel](https://avatars.githubusercontent.com/u/10930234?s=64 "ohansemmanuel")](https://github.com/ohansemmanuel)
* [![richeklein](https://avatars.githubusercontent.com/u/99479?s=64 "richeklein")](https://github.com/richeklein)
* [![ItzRoBeerT](https://avatars.githubusercontent.com/u/105317145?s=64 "ItzRoBeerT")](https://github.com/ItzRoBeerT)
* [![seppegadeyne](https://avatars.githubusercontent.com/u/18264851?s=64 "seppegadeyne")](https://github.com/seppegadeyne)
* [![simonswiss](https://avatars.githubusercontent.com/u/485747?s=64 "simonswiss")](https://github.com/simonswiss)
* [![tordans](https://avatars.githubusercontent.com/u/111561?s=64 "tordans")](https://github.com/tordans)
* [![vuecat](https://avatars.githubusercontent.com/u/16623919?s=64 "vuecat")](https://github.com/vuecat)
* [![dependabot\[bot\]](https://avatars.githubusercontent.com/u/49699333?s=64 "dependabot\[bot\]")](https://github.com/dependabot\[bot])
* [![coderfee](https://avatars.githubusercontent.com/u/18255987?s=64 "coderfee")](https://github.com/coderfee)
* [![vedxp](https://avatars.githubusercontent.com/u/87353286?s=64 "vedxp")](https://github.com/vedxp)
* [![tony-sull](https://avatars.githubusercontent.com/u/15836226?s=64 "tony-sull")](https://github.com/tony-sull)
* [![arty-name](https://avatars.githubusercontent.com/u/133055?s=64 "arty-name")](https://github.com/arty-name)
* [![timfee](https://avatars.githubusercontent.com/u/3246342?s=64 "timfee")](https://github.com/timfee)
* [![Tc-001](https://avatars.githubusercontent.com/u/55956895?s=64 "Tc-001")](https://github.com/Tc-001)
* [![hexWars](https://avatars.githubusercontent.com/u/61684793?s=64 "hexWars")](https://github.com/hexWars)
* [![SatanshuMishra](https://avatars.githubusercontent.com/u/63601536?s=64 "SatanshuMishra")](https://github.com/SatanshuMishra)
* [![ManorSailor](https://avatars.githubusercontent.com/u/53308129?s=64 "ManorSailor")](https://github.com/ManorSailor)
* [![BlackdestinyXX](https://avatars.githubusercontent.com/u/65021823?s=64 "BlackdestinyXX")](https://github.com/BlackdestinyXX)
* [![DevRohit06](https://avatars.githubusercontent.com/u/66678395?s=64 "DevRohit06")](https://github.com/DevRohit06)
* [![radenpioneer](https://avatars.githubusercontent.com/u/7355835?s=64 "radenpioneer")](https://github.com/radenpioneer)
* [![thepassle](https://avatars.githubusercontent.com/u/17054057?s=64 "thepassle")](https://github.com/thepassle)
* [![nicdun](https://avatars.githubusercontent.com/u/28926450?s=64 "nicdun")](https://github.com/nicdun)
* [![darusk](https://avatars.githubusercontent.com/u/110596249?s=64 "darusk")](https://github.com/darusk)
* [![emily-shen](https://avatars.githubusercontent.com/u/69125074?s=64 "emily-shen")](https://github.com/emily-shen)
* [![VLTHellolin](https://avatars.githubusercontent.com/u/119287439?s=64 "VLTHellolin")](https://github.com/VLTHellolin)
* [![Lilian97](https://avatars.githubusercontent.com/u/53004404?s=64 "Lilian97")](https://github.com/Lilian97)
* [![matdexir](https://avatars.githubusercontent.com/u/58453130?s=64 "matdexir")](https://github.com/matdexir)
* [![nadar](https://avatars.githubusercontent.com/u/3417221?s=64 "nadar")](https://github.com/nadar)
* [![okonomi](https://avatars.githubusercontent.com/u/74355?s=64 "okonomi")](https://github.com/okonomi)
* [![oki07](https://avatars.githubusercontent.com/u/22608727?s=64 "oki07")](https://github.com/oki07)
* [![renanleonel](https://avatars.githubusercontent.com/u/62075475?s=64 "renanleonel")](https://github.com/renanleonel)
* [![situ2001](https://avatars.githubusercontent.com/u/28241963?s=64 "situ2001")](https://github.com/situ2001)
* [![space-otter](https://avatars.githubusercontent.com/u/27896533?s=64 "space-otter")](https://github.com/space-otter)
* [![tobiasschmidt89](https://avatars.githubusercontent.com/u/75863044?s=64 "tobiasschmidt89")](https://github.com/tobiasschmidt89)
* [![ws-rush](https://avatars.githubusercontent.com/u/37883750?s=64 "ws-rush")](https://github.com/ws-rush)
* [![ykcory](https://avatars.githubusercontent.com/u/124225078?s=64 "ykcory")](https://github.com/ykcory)
* [![bengeois](https://avatars.githubusercontent.com/u/20949060?s=64 "bengeois")](https://github.com/bengeois)
* [![fflaten](https://avatars.githubusercontent.com/u/3436158?s=64 "fflaten")](https://github.com/fflaten)
* [![favanso](https://avatars.githubusercontent.com/u/71955135?s=64 "favanso")](https://github.com/favanso)
* [![evadecker](https://avatars.githubusercontent.com/u/4117920?s=64 "evadecker")](https://github.com/evadecker)
* [![eric-burel](https://avatars.githubusercontent.com/u/7983005?s=64 "eric-burel")](https://github.com/eric-burel)
* [![dsomel21](https://avatars.githubusercontent.com/u/17516559?s=64 "dsomel21")](https://github.com/dsomel21)
* [![Dillonpw](https://avatars.githubusercontent.com/u/136388405?s=64 "Dillonpw")](https://github.com/Dillonpw)
* [![davidumoru](https://avatars.githubusercontent.com/u/92310163?s=64 "davidumoru")](https://github.com/davidumoru)
* [![David-Large](https://avatars.githubusercontent.com/u/87678248?s=64 "David-Large")](https://github.com/David-Large)
* [![cravend](https://avatars.githubusercontent.com/u/7117993?s=64 "cravend")](https://github.com/cravend)
* [![CBID2](https://avatars.githubusercontent.com/u/105683440?s=64 "CBID2")](https://github.com/CBID2)
* [![csarnataro](https://avatars.githubusercontent.com/u/11388820?s=64 "csarnataro")](https://github.com/csarnataro)
* [![emjio](https://avatars.githubusercontent.com/u/26915891?s=64 "emjio")](https://github.com/emjio)
* [![breadadams](https://avatars.githubusercontent.com/u/5795227?s=64 "breadadams")](https://github.com/breadadams)
* [![Because789](https://avatars.githubusercontent.com/u/867257?s=64 "Because789")](https://github.com/Because789)
* [![deining](https://avatars.githubusercontent.com/u/18169566?s=64 "deining")](https://github.com/deining)
* [![ahmed-n-abdeltwab](https://avatars.githubusercontent.com/u/62723180?s=64 "ahmed-n-abdeltwab")](https://github.com/ahmed-n-abdeltwab)
* [![0xflotus](https://avatars.githubusercontent.com/u/26602940?s=64 "0xflotus")](https://github.com/0xflotus)
* [![Morritz](https://avatars.githubusercontent.com/u/12800230?s=64 "Morritz")](https://github.com/Morritz)
* [![leen-neel](https://avatars.githubusercontent.com/u/49027876?s=64 "leen-neel")](https://github.com/leen-neel)
* [![pReya](https://avatars.githubusercontent.com/u/4677417?s=64 "pReya")](https://github.com/pReya)
* [![mhdcodes](https://avatars.githubusercontent.com/u/9967336?s=64 "mhdcodes")](https://github.com/mhdcodes)
* [![debiru](https://avatars.githubusercontent.com/u/36402166?s=64 "debiru")](https://github.com/debiru)
* [![baevm](https://avatars.githubusercontent.com/u/91272406?s=64 "baevm")](https://github.com/baevm)
* [![MartinFerret](https://avatars.githubusercontent.com/u/90469240?s=64 "MartinFerret")](https://github.com/MartinFerret)
* [![kannansuresh](https://avatars.githubusercontent.com/u/61264139?s=64 "kannansuresh")](https://github.com/kannansuresh)
* [![LiHowe](https://avatars.githubusercontent.com/u/30686223?s=64 "LiHowe")](https://github.com/LiHowe)
* [![newtoallofthis123](https://avatars.githubusercontent.com/u/78465651?s=64 "newtoallofthis123")](https://github.com/newtoallofthis123)
* [![jacobdalamb](https://avatars.githubusercontent.com/u/44789941?s=64 "jacobdalamb")](https://github.com/jacobdalamb)
* [![swift502](https://avatars.githubusercontent.com/u/24359130?s=64 "swift502")](https://github.com/swift502)
* [![kanadgupta](https://avatars.githubusercontent.com/u/8854718?s=64 "kanadgupta")](https://github.com/kanadgupta)
* [![jdbruxelles](https://avatars.githubusercontent.com/u/18559798?s=64 "jdbruxelles")](https://github.com/jdbruxelles)
* [![Je12emy](https://avatars.githubusercontent.com/u/34408108?s=64 "Je12emy")](https://github.com/Je12emy)
* [![sunapi386](https://avatars.githubusercontent.com/u/1029022?s=64 "sunapi386")](https://github.com/sunapi386)
* [![jhuleatt](https://avatars.githubusercontent.com/u/3759507?s=64 "jhuleatt")](https://github.com/jhuleatt)
* [![millette](https://avatars.githubusercontent.com/u/50741?s=64 "millette")](https://github.com/millette)
* [![XinChou16](https://avatars.githubusercontent.com/u/24493056?s=64 "XinChou16")](https://github.com/XinChou16)
* [![Rolanddoda](https://avatars.githubusercontent.com/u/18482346?s=64 "Rolanddoda")](https://github.com/Rolanddoda)
* [![RolginRoman](https://avatars.githubusercontent.com/u/5978625?s=64 "RolginRoman")](https://github.com/RolginRoman)
* [![ffxsam](https://avatars.githubusercontent.com/u/12532733?s=64 "ffxsam")](https://github.com/ffxsam)
* [![SandraRodgers](https://avatars.githubusercontent.com/u/45321563?s=64 "SandraRodgers")](https://github.com/SandraRodgers)
* [![SebasG22](https://avatars.githubusercontent.com/u/17608169?s=64 "SebasG22")](https://github.com/SebasG22)
* [![SergioDiez](https://avatars.githubusercontent.com/u/9643358?s=64 "SergioDiez")](https://github.com/SergioDiez)
* [![ShamarYarde](https://avatars.githubusercontent.com/u/19520829?s=64 "ShamarYarde")](https://github.com/ShamarYarde)
* [![surjithctly](https://avatars.githubusercontent.com/u/1884712?s=64 "surjithctly")](https://github.com/surjithctly)
* [![V3RON](https://avatars.githubusercontent.com/u/8137511?s=64 "V3RON")](https://github.com/V3RON)
* [![motss](https://avatars.githubusercontent.com/u/10607759?s=64 "motss")](https://github.com/motss)
* [![tem235](https://avatars.githubusercontent.com/u/5091416?s=64 "tem235")](https://github.com/tem235)
* [![tobySolutions](https://avatars.githubusercontent.com/u/96334363?s=64 "tobySolutions")](https://github.com/tobySolutions)
* [![inwardmovement](https://avatars.githubusercontent.com/u/9438102?s=64 "inwardmovement")](https://github.com/inwardmovement)
* [![Trombach](https://avatars.githubusercontent.com/u/19306765?s=64 "Trombach")](https://github.com/Trombach)
* [![lukemcdonald](https://avatars.githubusercontent.com/u/299173?s=64 "lukemcdonald")](https://github.com/lukemcdonald)
* [![MaxTheTurtle0](https://avatars.githubusercontent.com/u/129096443?s=64 "MaxTheTurtle0")](https://github.com/MaxTheTurtle0)
* [![mingXta](https://avatars.githubusercontent.com/u/37586974?s=64 "mingXta")](https://github.com/mingXta)
* [![xun082](https://avatars.githubusercontent.com/u/73689580?s=64 "xun082")](https://github.com/xun082)
* [![stormynight9](https://avatars.githubusercontent.com/u/81434423?s=64 "stormynight9")](https://github.com/stormynight9)
* [![NavyStack](https://avatars.githubusercontent.com/u/137406386?s=64 "NavyStack")](https://github.com/NavyStack)
* [![nikhilhenry](https://avatars.githubusercontent.com/u/25770025?s=64 "nikhilhenry")](https://github.com/nikhilhenry)
* [![Ekwuno](https://avatars.githubusercontent.com/u/35943047?s=64 "Ekwuno")](https://github.com/Ekwuno)
* [![okikio](https://avatars.githubusercontent.com/u/17222836?s=64 "okikio")](https://github.com/okikio)
* [![omarr45](https://avatars.githubusercontent.com/u/58887202?s=64 "omarr45")](https://github.com/omarr45)
* [![dibaxu](https://avatars.githubusercontent.com/u/123599427?s=64 "dibaxu")](https://github.com/dibaxu)
* [![9thQuadrant](https://avatars.githubusercontent.com/u/14833423?s=64 "9thQuadrant")](https://github.com/9thQuadrant)
* [![serhalp](https://avatars.githubusercontent.com/u/1377702?s=64 "serhalp")](https://github.com/serhalp)
* [![Scalamando](https://avatars.githubusercontent.com/u/16595528?s=64 "Scalamando")](https://github.com/Scalamando)
* [![wobsoriano](https://avatars.githubusercontent.com/u/13049130?s=64 "wobsoriano")](https://github.com/wobsoriano)
* [![RobertAKARobin](https://avatars.githubusercontent.com/u/6268177?s=64 "RobertAKARobin")](https://github.com/RobertAKARobin)
* [![lhz960904](https://avatars.githubusercontent.com/u/29157111?s=64 "lhz960904")](https://github.com/lhz960904)
* [![lstephensca](https://avatars.githubusercontent.com/u/31998110?s=64 "lstephensca")](https://github.com/lstephensca)
* [![my-astro](https://avatars.githubusercontent.com/u/190968675?s=64 "my-astro")](https://github.com/my-astro)
* [![pilcrowonpaper](https://avatars.githubusercontent.com/u/80624252?s=64 "pilcrowonpaper")](https://github.com/pilcrowonpaper)
* [![ref-thomasledoux1](https://avatars.githubusercontent.com/u/74651094?s=64 "ref-thomasledoux1")](https://github.com/ref-thomasledoux1)
* [![sentisso](https://avatars.githubusercontent.com/u/38100632?s=64 "sentisso")](https://github.com/sentisso)
* [![t0yohei](https://avatars.githubusercontent.com/u/30691457?s=64 "t0yohei")](https://github.com/t0yohei)
* [![JPVan](https://avatars.githubusercontent.com/u/11825317?s=64 "JPVan")](https://github.com/JPVan)
* [![woshierha](https://avatars.githubusercontent.com/u/79536204?s=64 "woshierha")](https://github.com/woshierha)
* [![yiyuan9](https://avatars.githubusercontent.com/u/53341550?s=64 "yiyuan9")](https://github.com/yiyuan9)
* [![zreren](https://avatars.githubusercontent.com/u/70315161?s=64 "zreren")](https://github.com/zreren)
* [![dei8bit](https://avatars.githubusercontent.com/u/83183656?s=64 "dei8bit")](https://github.com/dei8bit)
* [![shinonomelon](https://avatars.githubusercontent.com/u/70379917?s=64 "shinonomelon")](https://github.com/shinonomelon)
* [![Tsukistar](https://avatars.githubusercontent.com/u/36409869?s=64 "Tsukistar")](https://github.com/Tsukistar)
* [![zhuchentong](https://avatars.githubusercontent.com/u/4535888?s=64 "zhuchentong")](https://github.com/zhuchentong)
* [![abhikjain360](https://avatars.githubusercontent.com/u/43034252?s=64 "abhikjain360")](https://github.com/abhikjain360)
* [![vitoriapena](https://avatars.githubusercontent.com/u/16581093?s=64 "vitoriapena")](https://github.com/vitoriapena)
* [![vivitt](https://avatars.githubusercontent.com/u/91918142?s=64 "vivitt")](https://github.com/vivitt)
* [![Zastinian](https://avatars.githubusercontent.com/u/82119938?s=64 "Zastinian")](https://github.com/Zastinian)
* [![peng](https://avatars.githubusercontent.com/u/26745086?s=64 "peng")](https://github.com/peng)
* [![AsazuTaiga](https://avatars.githubusercontent.com/u/48325984?s=64 "AsazuTaiga")](https://github.com/AsazuTaiga)
* [![magurotabetai](https://avatars.githubusercontent.com/u/3165765?s=64 "magurotabetai")](https://github.com/magurotabetai)
* [![Bluex-xx](https://avatars.githubusercontent.com/u/30541686?s=64 "Bluex-xx")](https://github.com/Bluex-xx)
* [![carsakiller](https://avatars.githubusercontent.com/u/61925890?s=64 "carsakiller")](https://github.com/carsakiller)
* [![djdeo](https://avatars.githubusercontent.com/u/32230775?s=64 "djdeo")](https://github.com/djdeo)
* [![fabriciodev26](https://avatars.githubusercontent.com/u/133163553?s=64 "fabriciodev26")](https://github.com/fabriciodev26)
* [![eurghwhy](https://avatars.githubusercontent.com/u/26926272?s=64 "eurghwhy")](https://github.com/eurghwhy)
* [![gtnbssn](https://avatars.githubusercontent.com/u/10359074?s=64 "gtnbssn")](https://github.com/gtnbssn)
* [![guiguir68](https://avatars.githubusercontent.com/u/46498821?s=64 "guiguir68")](https://github.com/guiguir68)
* [![eiis](https://avatars.githubusercontent.com/u/88193046?s=64 "eiis")](https://github.com/eiis)
* [![jose8a](https://avatars.githubusercontent.com/u/817855?s=64 "jose8a")](https://github.com/jose8a)
* [![kikonavarro](https://avatars.githubusercontent.com/u/78880702?s=64 "kikonavarro")](https://github.com/kikonavarro)
* [![aaronlamz](https://avatars.githubusercontent.com/u/3964466?s=64 "aaronlamz")](https://github.com/aaronlamz)
* [![coding-in-public](https://avatars.githubusercontent.com/u/86967271?s=64 "coding-in-public")](https://github.com/coding-in-public)
* [![colbyfayock](https://avatars.githubusercontent.com/u/1045274?s=64 "colbyfayock")](https://github.com/colbyfayock)
* [![conradagramont](https://avatars.githubusercontent.com/u/41589731?s=64 "conradagramont")](https://github.com/conradagramont)
* [![WooDaeHyun](https://avatars.githubusercontent.com/u/113018070?s=64 "WooDaeHyun")](https://github.com/WooDaeHyun)
* [![DavidEGiraldo](https://avatars.githubusercontent.com/u/113148688?s=64 "DavidEGiraldo")](https://github.com/DavidEGiraldo)
* [![Sparkhand](https://avatars.githubusercontent.com/u/39919361?s=64 "Sparkhand")](https://github.com/Sparkhand)
* [![ekafyi](https://avatars.githubusercontent.com/u/6597211?s=64 "ekafyi")](https://github.com/ekafyi)
* [![estruyf](https://avatars.githubusercontent.com/u/2900833?s=64 "estruyf")](https://github.com/estruyf)
* [![emma-sg](https://avatars.githubusercontent.com/u/5727389?s=64 "emma-sg")](https://github.com/emma-sg)
* [![Erik-McKelvey](https://avatars.githubusercontent.com/u/43917961?s=64 "Erik-McKelvey")](https://github.com/Erik-McKelvey)
* [![PanConDev](https://avatars.githubusercontent.com/u/10679967?s=64 "PanConDev")](https://github.com/PanConDev)
* [![Franqsanz](https://avatars.githubusercontent.com/u/44296203?s=64 "Franqsanz")](https://github.com/Franqsanz)
* [![falvarador](https://avatars.githubusercontent.com/u/8008909?s=64 "falvarador")](https://github.com/falvarador)
* [![felixsanz](https://avatars.githubusercontent.com/u/6182099?s=64 "felixsanz")](https://github.com/felixsanz)
* [![ogabrielp](https://avatars.githubusercontent.com/u/15015260?s=64 "ogabrielp")](https://github.com/ogabrielp)
* [![gaeulbyul](https://avatars.githubusercontent.com/u/830515?s=64 "gaeulbyul")](https://github.com/gaeulbyul)
* [![addonion](https://avatars.githubusercontent.com/u/51356696?s=64 "addonion")](https://github.com/addonion)
* [![AdamPrendergast](https://avatars.githubusercontent.com/u/550193?s=64 "AdamPrendergast")](https://github.com/AdamPrendergast)
* [![afonsojramos](https://avatars.githubusercontent.com/u/19473034?s=64 "afonsojramos")](https://github.com/afonsojramos)
* [![Alex-S-Davies](https://avatars.githubusercontent.com/u/46956435?s=64 "Alex-S-Davies")](https://github.com/Alex-S-Davies)
* [![Astisme](https://avatars.githubusercontent.com/u/96465880?s=64 "Astisme")](https://github.com/Astisme)
* [![alfredogonzalezmartinez](https://avatars.githubusercontent.com/u/48945157?s=64 "alfredogonzalezmartinez")](https://github.com/alfredogonzalezmartinez)
* [![alvgaona](https://avatars.githubusercontent.com/u/13088001?s=64 "alvgaona")](https://github.com/alvgaona)
* [![alvinometric](https://avatars.githubusercontent.com/u/107407814?s=64 "alvinometric")](https://github.com/alvinometric)
* [![andremralves](https://avatars.githubusercontent.com/u/71379045?s=64 "andremralves")](https://github.com/andremralves)
* [![ArinaKosiakov](https://avatars.githubusercontent.com/u/112902422?s=64 "ArinaKosiakov")](https://github.com/ArinaKosiakov)
* [![atilafassina](https://avatars.githubusercontent.com/u/2382552?s=64 "atilafassina")](https://github.com/atilafassina)
* [![avilyre](https://avatars.githubusercontent.com/u/66757451?s=64 "avilyre")](https://github.com/avilyre)
* [![bartosztrusinski](https://avatars.githubusercontent.com/u/33166095?s=64 "bartosztrusinski")](https://github.com/bartosztrusinski)
* [![branberry](https://avatars.githubusercontent.com/u/20285369?s=64 "branberry")](https://github.com/branberry)
* [![calebeby](https://avatars.githubusercontent.com/u/13206945?s=64 "calebeby")](https://github.com/calebeby)
* [![CheukTsai](https://avatars.githubusercontent.com/u/58281730?s=64 "CheukTsai")](https://github.com/CheukTsai)
* [![jazzypants1989](https://avatars.githubusercontent.com/u/102560332?s=64 "jazzypants1989")](https://github.com/jazzypants1989)
* [![Jhon-H](https://avatars.githubusercontent.com/u/88730883?s=64 "Jhon-H")](https://github.com/Jhon-H)
* [![jcha0713](https://avatars.githubusercontent.com/u/29053796?s=64 "jcha0713")](https://github.com/jcha0713)
* [![Jvictorvieira](https://avatars.githubusercontent.com/u/62016742?s=64 "Jvictorvieira")](https://github.com/Jvictorvieira)
* [![juanburg98](https://avatars.githubusercontent.com/u/106132925?s=64 "juanburg98")](https://github.com/juanburg98)
* [![juansemprun](https://avatars.githubusercontent.com/u/33623712?s=64 "juansemprun")](https://github.com/juansemprun)
* [![juliamrch](https://avatars.githubusercontent.com/u/101819212?s=64 "juliamrch")](https://github.com/juliamrch)
* [![jurajkapsz](https://avatars.githubusercontent.com/u/2209893?s=64 "jurajkapsz")](https://github.com/jurajkapsz)
* [![justinnoel](https://avatars.githubusercontent.com/u/81643826?s=64 "justinnoel")](https://github.com/justinnoel)
* [![yt-kevincarrera](https://avatars.githubusercontent.com/u/144747596?s=64 "yt-kevincarrera")](https://github.com/yt-kevincarrera)
* [![ixkaito](https://avatars.githubusercontent.com/u/5457539?s=64 "ixkaito")](https://github.com/ixkaito)
* [![yeskunall](https://avatars.githubusercontent.com/u/14703164?s=64 "yeskunall")](https://github.com/yeskunall)
* [![kylebutts](https://avatars.githubusercontent.com/u/19961439?s=64 "kylebutts")](https://github.com/kylebutts)
* [![leoxs22](https://avatars.githubusercontent.com/u/9098977?s=64 "leoxs22")](https://github.com/leoxs22)
* [![leohxj](https://avatars.githubusercontent.com/u/1506900?s=64 "leohxj")](https://github.com/leohxj)
* [![LuMiSxh](https://avatars.githubusercontent.com/u/76248448?s=64 "LuMiSxh")](https://github.com/LuMiSxh)
* [![neotherapper](https://avatars.githubusercontent.com/u/1514154?s=64 "neotherapper")](https://github.com/neotherapper)
* [![HALQME](https://avatars.githubusercontent.com/u/68320771?s=64 "HALQME")](https://github.com/HALQME)
* [![TKDev7](https://avatars.githubusercontent.com/u/30705623?s=64 "TKDev7")](https://github.com/TKDev7)
* [![X7md](https://avatars.githubusercontent.com/u/54203033?s=64 "X7md")](https://github.com/X7md)
* [![HawtinZeng](https://avatars.githubusercontent.com/u/73981739?s=64 "HawtinZeng")](https://github.com/HawtinZeng)
* [![hfournier](https://avatars.githubusercontent.com/u/13371332?s=64 "hfournier")](https://github.com/hfournier)
* [![iainsimmons](https://avatars.githubusercontent.com/u/8390324?s=64 "iainsimmons")](https://github.com/iainsimmons)
* [![teplostanski](https://avatars.githubusercontent.com/u/56846024?s=64 "teplostanski")](https://github.com/teplostanski)
* [![isaac-mcfadyen](https://avatars.githubusercontent.com/u/6243993?s=64 "isaac-mcfadyen")](https://github.com/isaac-mcfadyen)
* [![isamardzija](https://avatars.githubusercontent.com/u/74252988?s=64 "isamardzija")](https://github.com/isamardzija)
* [![jacksmithxyz](https://avatars.githubusercontent.com/u/122728490?s=64 "jacksmithxyz")](https://github.com/jacksmithxyz)
* [![AsyncBanana](https://avatars.githubusercontent.com/u/58297401?s=64 "AsyncBanana")](https://github.com/AsyncBanana)
* [![vandorsx](https://avatars.githubusercontent.com/u/140852203?s=64 "vandorsx")](https://github.com/vandorsx)
* [![DerYeger](https://avatars.githubusercontent.com/u/7950094?s=64 "DerYeger")](https://github.com/DerYeger)
* [![JEverhart383](https://avatars.githubusercontent.com/u/7818951?s=64 "JEverhart383")](https://github.com/JEverhart383)
* [![jeffdrumgod](https://avatars.githubusercontent.com/u/504327?s=64 "jeffdrumgod")](https://github.com/jeffdrumgod)
* [![alextison](https://avatars.githubusercontent.com/u/59065561?s=64 "alextison")](https://github.com/alextison)
* [![thekidisalright](https://avatars.githubusercontent.com/u/125706322?s=64 "thekidisalright")](https://github.com/thekidisalright)
* [![alex-drocks](https://avatars.githubusercontent.com/u/69808183?s=64 "alex-drocks")](https://github.com/alex-drocks)
* [![haasal](https://avatars.githubusercontent.com/u/104835302?s=64 "haasal")](https://github.com/haasal)
* [![AlexNodex](https://avatars.githubusercontent.com/u/17162626?s=64 "AlexNodex")](https://github.com/AlexNodex)
* [![alexpdraper](https://avatars.githubusercontent.com/u/6441503?s=64 "alexpdraper")](https://github.com/alexpdraper)
* [![amaimus](https://avatars.githubusercontent.com/u/35699916?s=64 "amaimus")](https://github.com/amaimus)
* [![albertogiunta](https://avatars.githubusercontent.com/u/5568337?s=64 "albertogiunta")](https://github.com/albertogiunta)
* [![wonderbeel](https://avatars.githubusercontent.com/u/1643060?s=64 "wonderbeel")](https://github.com/wonderbeel)
* [![altano](https://avatars.githubusercontent.com/u/1009?s=64 "altano")](https://github.com/altano)
* [![hrynko](https://avatars.githubusercontent.com/u/28267443?s=64 "hrynko")](https://github.com/hrynko)
* [![heldinz](https://avatars.githubusercontent.com/u/851278?s=64 "heldinz")](https://github.com/heldinz)
* [![gachikuku](https://avatars.githubusercontent.com/u/11743804?s=64 "gachikuku")](https://github.com/gachikuku)
* [![alvarosabu](https://avatars.githubusercontent.com/u/4699008?s=64 "alvarosabu")](https://github.com/alvarosabu)
* [![amxmln](https://avatars.githubusercontent.com/u/15271679?s=64 "amxmln")](https://github.com/amxmln)
* [![amirzezo201](https://avatars.githubusercontent.com/u/104027530?s=64 "amirzezo201")](https://github.com/amirzezo201)
* [![yoyo837](https://avatars.githubusercontent.com/u/6134547?s=64 "yoyo837")](https://github.com/yoyo837)
* [![grace-anand](https://avatars.githubusercontent.com/u/95082903?s=64 "grace-anand")](https://github.com/grace-anand)
* [![ancaemcken](https://avatars.githubusercontent.com/u/1617798?s=64 "ancaemcken")](https://github.com/ancaemcken)
* [![notjb](https://avatars.githubusercontent.com/u/3164034?s=64 "notjb")](https://github.com/notjb)
* [![3w36zj6](https://avatars.githubusercontent.com/u/52315048?s=64 "3w36zj6")](https://github.com/3w36zj6)
* [![aaronkai](https://avatars.githubusercontent.com/u/1002694?s=64 "aaronkai")](https://github.com/aaronkai)
* [![arafays](https://avatars.githubusercontent.com/u/6192554?s=64 "arafays")](https://github.com/arafays)
* [![alfawal](https://avatars.githubusercontent.com/u/61620817?s=64 "alfawal")](https://github.com/alfawal)
* [![abisekhsubedi](https://avatars.githubusercontent.com/u/20342543?s=64 "abisekhsubedi")](https://github.com/abisekhsubedi)
* [![adamlevoy](https://avatars.githubusercontent.com/u/81095429?s=64 "adamlevoy")](https://github.com/adamlevoy)
* [![AdamGEmerson](https://avatars.githubusercontent.com/u/35545129?s=64 "AdamGEmerson")](https://github.com/AdamGEmerson)
* [![adamgajzlerowicz](https://avatars.githubusercontent.com/u/675615?s=64 "adamgajzlerowicz")](https://github.com/adamgajzlerowicz)
* [![adam-lynch](https://avatars.githubusercontent.com/u/1427241?s=64 "adam-lynch")](https://github.com/adam-lynch)
* [![armgitaar](https://avatars.githubusercontent.com/u/30202878?s=64 "armgitaar")](https://github.com/armgitaar)
* [![ADRlANO](https://avatars.githubusercontent.com/u/35582648?s=64 "ADRlANO")](https://github.com/ADRlANO)
* [![adrian-burkhart](https://avatars.githubusercontent.com/u/59536294?s=64 "adrian-burkhart")](https://github.com/adrian-burkhart)
* [![adrianlyjak](https://avatars.githubusercontent.com/u/2024018?s=64 "adrianlyjak")](https://github.com/adrianlyjak)
* [![apz-gh](https://avatars.githubusercontent.com/u/20273871?s=64 "apz-gh")](https://github.com/apz-gh)
* [![ahmedrowaihi](https://avatars.githubusercontent.com/u/67356781?s=64 "ahmedrowaihi")](https://github.com/ahmedrowaihi)
* [![aidankmcalister](https://avatars.githubusercontent.com/u/105178005?s=64 "aidankmcalister")](https://github.com/aidankmcalister)
* [![AishaBlake](https://avatars.githubusercontent.com/u/7365296?s=64 "AishaBlake")](https://github.com/AishaBlake)
* [![aboudard](https://avatars.githubusercontent.com/u/767767?s=64 "aboudard")](https://github.com/aboudard)

# Editor setup

> Set up your code editor to build with Astro.

Customize your code editor to improve the Astro developer experience and unlock new features.

## VS Code

[Section titled “VS Code”](#vs-code)

[VS Code](https://code.visualstudio.com/) is a popular code editor for web developers, built by Microsoft. The VS Code engine also powers popular in-browser code editors like [GitHub Codespaces](https://github.com/features/codespaces) and [Gitpod](https://gitpod.io/).

Astro works with any code editor. However, VS Code is our recommended editor for Astro projects. We maintain an official [Astro VS Code Extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode) that unlocks several key features and developer experience improvements for Astro projects.

* Syntax highlighting for `.astro` files.
* TypeScript type information for `.astro` files.
* [VS Code Intellisense](https://code.visualstudio.com/docs/editor/intellisense) for code completion, hints and more.

To get started, install the [Astro VS Code Extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode) today.

See how to [set up TypeScript](/en/guides/typescript/) in your Astro project.

## Zed

[Section titled “Zed”](#zed)

[Zed](https://zed.dev/) is a high-performance, multiplayer code editor that is optimized for speed and large projects. Their [Astro extension](https://zed.dev/extensions/astro) includes features like syntax highlighting for `.astro` files, code completion, formatting, diagnostics, and go-to-definition.

## JetBrains IDEs

[Section titled “JetBrains IDEs”](#jetbrains-ides)

[Webstorm](https://www.jetbrains.com/webstorm/) is a JavaScript and TypeScript IDE that added support for the Astro Language Server in version 2024.2. This update brings features like syntax highlighting, code completion, and formatting.

Install the official plugin through [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/20959-astro) or by searching for “Astro” in the IDE’s Plugins tab. You can toggle the language server in `Settings | Languages & Frameworks | TypeScript | Astro`.

For more information on Astro support in Webstorm, check out [the official Webstorm Astro Documentation](https://www.jetbrains.com/help/webstorm/astro.html).

## Other Code Editors

[Section titled “Other Code Editors”](#other-code-editors)

Our amazing community maintains several extensions for other popular editors, including:

* [VS Code Extension on Open VSX](https://open-vsx.org/extension/astro-build/astro-vscode) Official - The official Astro VS Code Extension, available on the Open VSX registry for editors like [Cursor](https://cursor.com) or [VSCodium](https://vscodium.com/).
* [Vim Plugin](https://github.com/wuelnerdotexe/vim-astro) Community - Provides syntax highlighting, indentation, and code folding support for Astro inside of Vim or Neovim
* Neovim [LSP](https://github.com/neovim/nvim-lspconfig/blob/master/doc/configs.md#astro) and [TreeSitter](https://github.com/virchau13/tree-sitter-astro) Plugins Community - Provides syntax highlighting, treesitter parsing, and code completion for Astro inside of Neovim
* Emacs - See instructions for [Configuring Emacs and Eglot](https://medium.com/@jrmjrm/configuring-emacs-and-eglot-to-work-with-astro-language-server-9408eb709ab0) Community to work with Astro
* [Astro syntax highlighting for Sublime Text](https://packagecontrol.io/packages/Astro) Community - The Astro package for Sublime Text, available on the Sublime Text package manager.
* [Nova Extension](https://extensions.panic.com/extensions/sciencefidelity/sciencefidelity.astro/) Community - Provides syntax highlighting and code completion for Astro inside of Nova

## In-Browser Editors

[Section titled “In-Browser Editors”](#in-browser-editors)

In addition to local editors, Astro also runs well on in-browser hosted editors, including:

* [StackBlitz](https://stackblitz.com/) and [CodeSandbox](https://codesandbox.io/) - online editors that run in your browser, with built-in syntax highlighting support for `.astro` files. No installation or configuration required!
* [GitHub.dev](https://github.dev/) - allows you to install the Astro VS Code extension as a [web extension](https://code.visualstudio.com/api/extension-guides/web-extensions), which gives you access to only some of the full extension features. Currently, only syntax highlighting is supported.
* [IDX](https://idx.dev) and [Gitpod](https://gitpod.io/) - a full dev environment in the cloud that can install the official Astro VS Code Extension from Open VSX.

## Other tools

[Section titled “Other tools”](#other-tools)

### ESLint

[Section titled “ESLint”](#eslint)

[ESLint](https://eslint.org/) is a popular linter for JavaScript and JSX. For Astro support, [a community maintained plugin](https://github.com/ota-meshi/eslint-plugin-astro) can be installed.

See [the project’s User Guide](https://ota-meshi.github.io/eslint-plugin-astro/user-guide/) for more information on how to install and set up ESLint for your project.

### Stylelint

[Section titled “Stylelint”](#stylelint)

[Stylelint](https://stylelint.io/) is a popular linter for CSS. [A community maintained Stylelint configuration](https://github.com/ota-meshi/stylelint-config-html) provides Astro support.

Installation instructions, editor integration, and additional information can be found in the project’s README.

### Biome

[Section titled “Biome”](#biome)

[Biome](https://biomejs.dev/) is an all-in-one linter and formatter for the web. [Biome currently has experimental support for `.astro` files](https://biomejs.dev/internals/language-support/#html-super-languages-support), and can be used to lint and format the frontmatter in `.astro` files.

### Prettier

[Section titled “Prettier”](#prettier)

[Prettier](https://prettier.io/) is a popular formatter for JavaScript, HTML, CSS, and more. If you’re using the [Astro VS Code Extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode), code formatting with Prettier is included.

To add support for formatting `.astro` files outside of the editor (e.g. CLI) or inside editors that don’t support our editor tooling, install [the official Astro Prettier plugin](https://github.com/withastro/prettier-plugin-astro).

1. Install `prettier` and `prettier-plugin-astro`.

   * npm

     ```shell
     npm install --save-dev --save-exact prettier prettier-plugin-astro
     ```

   * pnpm

     ```shell
     pnpm add --save-dev --save-exact prettier prettier-plugin-astro
     ```

   * Yarn

     ```shell
     yarn add --dev --exact prettier prettier-plugin-astro
     ```

2. Create a `.prettierrc` configuration file (or `.prettierrc.json`, `.prettierrc.mjs`, or [other supported formats](https://prettier.io/docs/configuration)) in the root of your project and add `prettier-plugin-astro` to it.

   In this file, also manually specify the parser for Astro files.

   .prettierrc

   ```json
   {
     "plugins": ["prettier-plugin-astro"],
     "overrides": [
       {
         "files": "*.astro",
         "options": {
           "parser": "astro"
         }
       }
     ]
   }
   ```

3. Optionally, install other Prettier plugins for your project, and add them to the configuration file. These additional plugins may need to be listed in a specific order. For example, if you use Tailwind, `prettier-plugin-tailwindcss` must be [the last Prettier plugin in the plugins array](https://github.com/tailwindlabs/prettier-plugin-tailwindcss#compatibility-with-other-prettier-plugins).

   .prettierrc

   ```json
   {
     "plugins": [
       "prettier-plugin-astro",
       "prettier-plugin-tailwindcss" // needs to be last
     ],
     "overrides": [
       {
         "files": "*.astro",
         "options": {
           "parser": "astro"
         }
       }
     ]
   }
   ```

4. Run the following command in your terminal to format your files.

   * npm

     ```shell
     npx prettier . --write
     ```

   * pnpm

     ```shell
     pnpm exec prettier . --write
     ```

   * Yarn

     ```shell
     yarn exec prettier . --write
     ```

See the [Prettier plugin’s README](https://github.com/withastro/prettier-plugin-astro/blob/main/README.md) for more information about its supported options, how to set up Prettier inside VS Code, and more.

### dprint

[Section titled “dprint”](#dprint)

[dprint](https://dprint.dev/) is a highly-configurable code formatter that supports many languages, including JavaScript, TypeScript, CSS, and more. Support for `.astro` files can be added using the [markup\_fmt plugin](https://github.com/g-plane/markup_fmt).

# Astro Docs

> Guides, resources, and API references to help you build with Astro.

What will you build with Astro?

Explore [Astro starter themes](https://astro.build/themes/) for blogs, portfolios, docs, landing pages, SaaS, marketing, ecommerce sites, and more!

Take a guided tour

Complete our introductory [Build a Blog Tutorial](/en/tutorial/0-introduction/) to learn the basics and create your first Astro site.

Start a new project

```sh
# create a new project with npm
npm create astro@latest
```

Our [installation guide](/en/install-and-setup/) has step-by-step instructions for installing Astro using our CLI wizard, creating a new project from an existing Astro GitHub repository, and for installing Astro manually.

Learn

* [Astro’s main features](/en/concepts/why-astro/)
* [Islands architecture](/en/concepts/islands/)
* [Astro components](/en/basics/astro-components/)
* [The Astro template syntax](/en/reference/astro-syntax/)

Extend

* [Add integrations like React and Partytown](/en/guides/integrations-guide/)
* [Create type safe content collections](/en/guides/content-collections/)
* [Enhance navigation with view transitions](/en/guides/view-transitions/)
* [Connect a headless CMS to your project](/en/guides/cms/)

## Have a question or want to get involved?

![](/_astro/houston_love.BttrNCcZ_Ok6Ar.webp) [Join our Discord](https://astro.build/chat)


---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-actions.md)
