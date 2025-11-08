**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-image-optimization.md)

---

# Next.js Documentation

@doc-version: >=15.0.0
@doc-version-notes: Some features may have extended or refined behavior in minor or patch releases
@router: App Router
@router-note: Unless otherwise noted in each section, these documents apply to the App Router


--------------------------------------------------------------------------------
title: "Getting Started"
description: "Learn how to create full-stack web applications with the Next.js App Router."
source: "https://nextjs.org/docs/app/getting-started"
--------------------------------------------------------------------------------

# Getting Started

Welcome to the Next.js documentation!

This **Getting Started** section will help you create your first Next.js app and learn the core features you'll use in every project.

## Pre-requisite knowledge

Our documentation assumes some familiarity with web development. Before getting started, it'll help if you're comfortable with:

* HTML
* CSS
* JavaScript
* React

If you're new to React or need a refresher, we recommend starting with our [React Foundations course](/learn/react-foundations), and the [Next.js Foundations course](/learn/dashboard-app) that has you building an application as you learn.

## Next Steps

 - [Installation](/docs/app/getting-started/installation.md)
 - [Project Structure](/docs/app/getting-started/project-structure.md)
 - [Layouts and Pages](/docs/app/getting-started/layouts-and-pages.md)
 - [Linking and Navigating](/docs/app/getting-started/linking-and-navigating.md)
 - [Server and Client Components](/docs/app/getting-started/server-and-client-components.md)
 - [Cache Components](/docs/app/getting-started/cache-components.md)
 - [Fetching Data](/docs/app/getting-started/fetching-data.md)
 - [Updating Data](/docs/app/getting-started/updating-data.md)
 - [Caching and Revalidating](/docs/app/getting-started/caching-and-revalidating.md)
 - [Error Handling](/docs/app/getting-started/error-handling.md)
 - [CSS](/docs/app/getting-started/css.md)
 - [Image Optimization](/docs/app/getting-started/images.md)
 - [Font Optimization](/docs/app/getting-started/fonts.md)
 - [Metadata and OG images](/docs/app/getting-started/metadata-and-og-images.md)
 - [Route Handlers](/docs/app/getting-started/route-handlers.md)
 - [Proxy](/docs/app/getting-started/proxy.md)
 - [Deploying](/docs/app/getting-started/deploying.md)
 - [Upgrading](/docs/app/getting-started/upgrading.md)

--------------------------------------------------------------------------------
title: "Installation"
description: "Learn how to create a new Next.js application with the `create-next-app` CLI, and set up TypeScript, ESLint, and Module Path Aliases."
source: "https://nextjs.org/docs/app/getting-started/installation"
--------------------------------------------------------------------------------

# Installation

Create a new Next.js app and run it locally.

## Quick start

1. Create a new Next.js app named `my-app`
2. `cd my-app` and start the dev server.
3. Visit `http://localhost:3000`.

```bash package="pnpm"
pnpm create next-app@latest my-app --yes
cd my-app
pnpm dev
```

```bash package="npm"
npx create-next-app@latest my-app --yes
cd my-app
npm run dev
```

```bash package="yarn"
yarn create next-app@latest my-app --yes
cd my-app
yarn dev
```

```bash package="bun"
bun create next-app@latest my-app --yes
cd my-app
bun dev
```

* `--yes` skips prompts using saved preferences or defaults. The default setup enables TypeScript, Tailwind, ESLint, App Router, and Turbopack, with import alias `@/*`.

## System requirements

Before you begin, make sure your development environment meets the following requirements:

* Minimum Node.js version: [20.9](https://nodejs.org/)
* Operating systems: macOS, Windows (including WSL), and Linux.

## Supported browsers

Next.js supports modern browsers with zero configuration.

* Chrome 111+
* Edge 111+
* Firefox 111+
* Safari 16.4+

Learn more about [browser support](/docs/architecture/supported-browsers.md), including how to configure polyfills and target specific browsers.

## Create with the CLI

The quickest way to create a new Next.js app is using [`create-next-app`](/docs/app/api-reference/cli/create-next-app.md), which sets up everything automatically for you. To create a project, run:

```bash filename="Terminal"
npx create-next-app@latest
```

On installation, you'll see the following prompts:

```txt filename="Terminal"
What is your project named? my-app
Would you like to use the recommended Next.js defaults?
    Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
    No, reuse previous settings
    No, customize settings - Choose your own preferences
```

If you choose to `customize settings`, you'll see the following prompts:

```txt filename="Terminal"
Would you like to use TypeScript? No / Yes
Which linter would you like to use? ESLint / Biome / None
Would you like to use React Compiler? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

After the prompts, [`create-next-app`](/docs/app/api-reference/cli/create-next-app.md) will create a folder with your project name and install the required dependencies.

## Manual installation

To manually create a new Next.js app, install the required packages:

```bash package="pnpm"
pnpm i next@latest react@latest react-dom@latest
```

```bash package="npm"
npm i next@latest react@latest react-dom@latest
```

```bash package="yarn"
yarn add next@latest react@latest react-dom@latest
```

```bash package="bun"
bun add next@latest react@latest react-dom@latest
```

> **Good to know**: The App Router uses [React canary releases](https://react.dev/blog/2023/05/03/react-canaries) built-in, which include all the stable React 19 changes, as well as newer features being validated in frameworks. The Pages Router uses the React version you install in `package.json`.

Then, add the following scripts to your `package.json` file:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

These scripts refer to the different stages of developing an application:

* `next dev`: Starts the development server using Turbopack (default bundler).
* `next build`: Builds the application for production.
* `next start`: Starts the production server.
* `eslint`: Runs ESLint.

Turbopack is now the default bundler. To use Webpack run `next dev --webpack` or `next build --webpack`. See the [Turbopack docs](/docs/app/api-reference/turbopack.md) for configuration details.

### Create the `app` directory

Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.

Create an `app` folder. Then, inside `app`, create a `layout.tsx` file. This file is the [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout). It's required and must contain the `<html>` and `<body>` tags.

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

Create a home page `app/page.tsx` with some initial content:

```tsx filename="app/page.tsx" switcher
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

```jsx filename="app/page.js" switcher
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

Both `layout.tsx` and `page.tsx` will be rendered when the user visits the root of your application (`/`).

![App Folder Structure](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/app-getting-started.png)

> **Good to know**:
>
> * If you forget to create the root layout, Next.js will automatically create this file when running the development server with `next dev`.
> * You can optionally use a [`src` folder](/docs/app/api-reference/file-conventions/src-folder.md) in the root of your project to separate your application's code from configuration files.

### Create the `public` folder (optional)

Create a [`public` folder](/docs/app/api-reference/file-conventions/public-folder.md) at the root of your project to store static assets such as images, fonts, etc. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

You can then reference these assets using the root path (`/`). For example, `public/profile.png` can be referenced as `/profile.png`:

```tsx filename="app/page.tsx" highlight={4} switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

```jsx filename="app/page.js" highlight={4} switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

## Run the development server

1. Run `npm run dev` to start the development server.
2. Visit `http://localhost:3000` to view your application.
3. Edit the `app/page.tsx` file and save it to see the updated result in your browser.

## Set up TypeScript

> Minimum TypeScript version: `v5.1.0`

Next.js comes with built-in TypeScript support. To add TypeScript to your project, rename a file to `.ts` / `.tsx` and run `next dev`. Next.js will automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

### IDE Plugin

Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type-checking and auto-completion.

You can enable the plugin in VS Code by:

1. Opening the command palette (`Ctrl/⌘` + `Shift` + `P`)
2. Searching for "TypeScript: Select TypeScript Version"
3. Selecting "Use Workspace Version"

![TypeScript Command Palette](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/typescript-command-palette.png)

See the [TypeScript reference](/docs/app/api-reference/config/next-config-js/typescript.md) page for more information.

## Set up linting

Next.js supports linting with either ESLint or Biome. Choose a linter and run it directly via `package.json` scripts.

* Use **ESLint** (comprehensive rules):

```json filename="package.json"
{
  "scripts": {
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

* Or use **Biome** (fast linter + formatter):

```json filename="package.json"
{
  "scripts": {
    "lint": "biome check",
    "format": "biome format --write"
  }
}
```

If your project previously used `next lint`, migrate your scripts to the ESLint CLI with the codemod:

```bash filename="Terminal"
npx @next/codemod@canary next-lint-to-eslint-cli .
```

If you use ESLint, create an explicit config (recommended `eslint.config.mjs`). ESLint supports both [the legacy `.eslintrc.*` and the newer `eslint.config.mjs` formats](https://eslint.org/docs/latest/use/configure/configuration-files#configuring-eslint). See the [ESLint API reference](/docs/app/api-reference/config/eslint.md#with-core-web-vitals) for a recommended setup.

> **Good to know**: Starting with Next.js 16, `next build` no longer runs the linter automatically. Instead, you can run your linter through NPM scripts.

See the [ESLint Plugin](/docs/app/api-reference/config/eslint.md) page for more information.

## Set up Absolute Imports and Module Path Aliases

Next.js has in-built support for the `"paths"` and `"baseUrl"` options of `tsconfig.json` and `jsconfig.json` files.

These options allow you to alias project directories to absolute paths, making it easier and cleaner to import modules. For example:

```jsx
// Before
import { Button } from '../../../components/button'

// After
import { Button } from '@/components/button'
```

To configure absolute imports, add the `baseUrl` configuration option to your `tsconfig.json` or `jsconfig.json` file. For example:

```json filename="tsconfig.json or jsconfig.json"
{
  "compilerOptions": {
    "baseUrl": "src/"
  }
}
```

In addition to configuring the `baseUrl` path, you can use the `"paths"` option to `"alias"` module paths.

For example, the following configuration maps `@/components/*` to `components/*`:

```json filename="tsconfig.json or jsconfig.json"
{
  "compilerOptions": {
    "baseUrl": "src/",
    "paths": {
      "@/styles/*": ["styles/*"],
      "@/components/*": ["components/*"]
    }
  }
}
```

Each of the `"paths"` are relative to the `baseUrl` location.


--------------------------------------------------------------------------------
title: "Project structure and organization"
description: "Learn the folder and file conventions in Next.js, and how to organize your project."
source: "https://nextjs.org/docs/app/getting-started/project-structure"
--------------------------------------------------------------------------------

# Project Structure

This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

## Folder and file conventions

### Top-level folders

Top-level folders are used to organize your application's code and static assets.

![Route segments to path segments](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/top-level-folders.png)

|                                                                    |                                    |
| ------------------------------------------------------------------ | ---------------------------------- |
| [`app`](/docs/app.md)                                                 | App Router                         |
| [`pages`](/docs/pages/building-your-application/routing.md)           | Pages Router                       |
| [`public`](/docs/app/api-reference/file-conventions/public-folder.md) | Static assets to be served         |
| [`src`](/docs/app/api-reference/file-conventions/src-folder.md)       | Optional application source folder |

### Top-level files

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

|                                                                              |                                         |
| ---------------------------------------------------------------------------- | --------------------------------------- |
| **Next.js**                                                                  |                                         |
| [`next.config.js`](/docs/app/api-reference/config/next-config-js.md)            | Configuration file for Next.js          |
| [`package.json`](/docs/app/getting-started/installation.md#manual-installation) | Project dependencies and scripts        |
| [`instrumentation.ts`](/docs/app/guides/instrumentation.md)                     | OpenTelemetry and Instrumentation file  |
| [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy.md)                 | Next.js request proxy                   |
| [`.env`](/docs/app/guides/environment-variables.md)                             | Environment variables                   |
| [`.env.local`](/docs/app/guides/environment-variables.md)                       | Local environment variables             |
| [`.env.production`](/docs/app/guides/environment-variables.md)                  | Production environment variables        |
| [`.env.development`](/docs/app/guides/environment-variables.md)                 | Development environment variables       |
| [`eslint.config.mjs`](/docs/app/api-reference/config/eslint.md)                 | Configuration file for ESLint           |
| `.gitignore`                                                                 | Git files and folders to ignore         |
| `next-env.d.ts`                                                              | TypeScript declaration file for Next.js |
| `tsconfig.json`                                                              | Configuration file for TypeScript       |
| `jsconfig.json`                                                              | Configuration file for JavaScript       |

### Routing Files

Add `page` to expose a route, `layout` for shared UI such as header, nav, or footer, `loading` for skeletons, `error` for error boundaries, and `route` for APIs.

|                                                                               |                     |                              |
| ----------------------------------------------------------------------------- | ------------------- | ---------------------------- |
| [`layout`](/docs/app/api-reference/file-conventions/layout.md)                   | `.js` `.jsx` `.tsx` | Layout                       |
| [`page`](/docs/app/api-reference/file-conventions/page.md)                       | `.js` `.jsx` `.tsx` | Page                         |
| [`loading`](/docs/app/api-reference/file-conventions/loading.md)                 | `.js` `.jsx` `.tsx` | Loading UI                   |
| [`not-found`](/docs/app/api-reference/file-conventions/not-found.md)             | `.js` `.jsx` `.tsx` | Not found UI                 |
| [`error`](/docs/app/api-reference/file-conventions/error.md)                     | `.js` `.jsx` `.tsx` | Error UI                     |
| [`global-error`](/docs/app/api-reference/file-conventions/error.md#global-error) | `.js` `.jsx` `.tsx` | Global error UI              |
| [`route`](/docs/app/api-reference/file-conventions/route.md)                     | `.js` `.ts`         | API endpoint                 |
| [`template`](/docs/app/api-reference/file-conventions/template.md)               | `.js` `.jsx` `.tsx` | Re-rendered layout           |
| [`default`](/docs/app/api-reference/file-conventions/default.md)                 | `.js` `.jsx` `.tsx` | Parallel route fallback page |

### Nested routes

Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a `page` or `route` file exists.

| Path                        | URL pattern     | Notes                         |
| --------------------------- | --------------- | ----------------------------- |
| `app/layout.tsx`            | —               | Root layout wraps all routes  |
| `app/blog/layout.tsx`       | —               | Wraps `/blog` and descendants |
| `app/page.tsx`              | `/`             | Public route                  |
| `app/blog/page.tsx`         | `/blog`         | Public route                  |
| `app/blog/authors/page.tsx` | `/blog/authors` | Public route                  |

### Dynamic routes

Parameterize segments with square brackets. Use `[segment]` for a single param, `[...segment]` for catch‑all, and `[[...segment]]` for optional catch‑all. Access values via the [`params`](/docs/app/api-reference/file-conventions/page.md#params-optional) prop.

| Path                            | URL pattern                                                          |
| ------------------------------- | -------------------------------------------------------------------- |
| `app/blog/[slug]/page.tsx`      | `/blog/my-first-post`                                                |
| `app/shop/[...slug]/page.tsx`   | `/shop/clothing`, `/shop/clothing/shirts`                            |
| `app/docs/[[...slug]]/page.tsx` | `/docs`, `/docs/layouts-and-pages`, `/docs/api-reference/use-router` |

### Route groups and private folders

Organize code without changing URLs with route groups [`(group)`](/docs/app/api-reference/file-conventions/route-groups.md#convention), and colocate non-routable files with private folders [`_folder`](#private-folders).

| Path                            | URL pattern | Notes                                     |
| ------------------------------- | ----------- | ----------------------------------------- |
| `app/(marketing)/page.tsx`      | `/`         | Group omitted from URL                    |
| `app/(shop)/cart/page.tsx`      | `/cart`     | Share layouts within `(shop)`             |
| `app/blog/_components/Post.tsx` | —           | Not routable; safe place for UI utilities |
| `app/blog/_lib/data.ts`         | —           | Not routable; safe place for utils        |

### Parallel and Intercepted Routes

These features fit specific UI patterns, such as slot-based layouts or modal routing.

Use `@slot` for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.

| Pattern (docs)                                                                              | Meaning              | Typical use case                         |
| ------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------- |
| [`@folder`](/docs/app/api-reference/file-conventions/parallel-routes.md#slots)                 | Named slot           | Sidebar + main content                   |
| [`(.)folder`](/docs/app/api-reference/file-conventions/intercepting-routes.md#convention)      | Intercept same level | Preview sibling route in a modal         |
| [`(..)folder`](/docs/app/api-reference/file-conventions/intercepting-routes.md#convention)     | Intercept parent     | Open a child of the parent as an overlay |
| [`(..)(..)folder`](/docs/app/api-reference/file-conventions/intercepting-routes.md#convention) | Intercept two levels | Deeply nested overlay                    |
| [`(...)folder`](/docs/app/api-reference/file-conventions/intercepting-routes.md#convention)    | Intercept from root  | Show arbitrary route in current view     |

### Metadata file conventions

#### App icons

|                                                                                                                 |                                     |                          |
| --------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------ |
| [`favicon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#favicon)                                | `.ico`                              | Favicon file             |
| [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#icon)                                      | `.ico` `.jpg` `.jpeg` `.png` `.svg` | App Icon file            |
| [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#generate-icons-using-code-js-ts-tsx)       | `.js` `.ts` `.tsx`                  | Generated App Icon       |
| [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#apple-icon)                          | `.jpg` `.jpeg`, `.png`              | Apple App Icon file      |
| [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx`                  | Generated Apple App Icon |

#### Open Graph and Twitter images

|                                                                                                                             |                              |                            |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------- |
| [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#opengraph-image)                      | `.jpg` `.jpeg` `.png` `.gif` | Open Graph image file      |
| [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx`           | Generated Open Graph image |
| [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#twitter-image)                          | `.jpg` `.jpeg` `.png` `.gif` | Twitter image file         |
| [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#generate-images-using-code-js-ts-tsx)   | `.js` `.ts` `.tsx`           | Generated Twitter image    |

#### SEO

|                                                                                                              |             |                       |
| ------------------------------------------------------------------------------------------------------------ | ----------- | --------------------- |
| [`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap.md#sitemap-files-xml)                     | `.xml`      | Sitemap file          |
| [`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap.md#generating-a-sitemap-using-code-js-ts) | `.js` `.ts` | Generated Sitemap     |
| [`robots`](/docs/app/api-reference/file-conventions/metadata/robots.md#static-robotstxt)                        | `.txt`      | Robots file           |
| [`robots`](/docs/app/api-reference/file-conventions/metadata/robots.md#generate-a-robots-file)                  | `.js` `.ts` | Generated Robots file |

## Organizing your project

Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.

### Component hierarchy

The components defined in special files are rendered in a specific hierarchy:

* `layout.js`
* `template.js`
* `error.js` (React error boundary)
* `loading.js` (React suspense boundary)
* `not-found.js` (React error boundary for "not found" UI)
* `page.js` or nested `layout.js`

![Component Hierarchy for File Conventions](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/file-conventions-component-hierarchy.png)

The components are rendered recursively in nested routes, meaning the components of a route segment will be nested **inside** the components of its parent segment.

![Nested File Conventions Component Hierarchy](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/nested-file-conventions-component-hierarchy.png)

### Colocation

In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.

![A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-not-routable.png)

And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.

![A diagram showing how page.js and route.js files make routes publicly accessible.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-routable.png)

This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.

![A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-colocation.png)

> **Good to know**: While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](#store-project-files-outside-of-app).

### Private folders

Private folders can be created by prefixing a folder with an underscore: `_folderName`

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.

![An example folder structure using private folders](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-private-folders.png)

Since files in the `app` directory can be [safely colocated by default](#colocation), private folders are not required for colocation. However, they can be useful for:

* Separating UI logic from routing logic.
* Consistently organizing internal files across a project and the Next.js ecosystem.
* Sorting and grouping files in code editors.
* Avoiding potential naming conflicts with future Next.js file conventions.

> **Good to know**:
>
> * While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
> * You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL-encoded form of an underscore): `%5FfolderName`.
> * If you don't use private folders, it would be helpful to know Next.js [special file conventions](/docs/app/getting-started/project-structure.md#routing-files) to prevent unexpected naming conflicts.

### Route groups

Route groups can be created by wrapping a folder in parenthesis: `(folderName)`

This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![An example folder structure using route groups](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-route-groups.png)

Route groups are useful for:

* Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.
* Enabling nested layouts in the same route segment level:
  * [Creating multiple nested layouts in the same segment, including multiple root layouts](#creating-multiple-root-layouts)
  * [Adding a layout to a subset of routes in a common segment](#opting-specific-segments-into-a-layout)

### `src` folder

Next.js supports storing application code (including `app`) inside an optional [`src` folder](/docs/app/api-reference/file-conventions/src-folder.md). This separates application code from project configuration files which mostly live in the root of a project.

![An example folder structure with the src folder](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-src-directory.png)

## Examples

The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

> **Good to know**: In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.

### Store project files outside of `app`

This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.

![An example folder structure with project files outside of app](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-project-root.png)

### Store project files in top-level folders inside of `app`

This strategy stores all application code in shared folders in the **root of the `app` directory**.

![An example folder structure with project files inside app](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-app-root.png)

### Split project files by feature or route

This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.

![An example folder structure with project files split by feature or route](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-app-root-split.png)

### Organize routes without affecting the URL path

To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g. `(marketing)` or `(shop)`).

![Organizing Routes with Route Groups](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-organisation.png)

Even though routes inside `(marketing)` and `(shop)` share the same URL hierarchy, you can create a different layout for each group by adding a `layout.js` file inside their folders.

![Route Groups with Multiple Layouts](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-multiple-layouts.png)

### Opting specific segments into a layout

To opt specific routes into a layout, create a new route group (e.g. `(shop)`) and move the routes that share the same layout into the group (e.g. `account` and `cart`). The routes outside of the group will not share the layout (e.g. `checkout`).

![Route Groups with Opt-in Layouts](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-opt-in-layouts.png)

### Opting for loading skeletons on a specific route

To apply a [loading skeleton](/docs/app/api-reference/file-conventions/loading.md) via a `loading.js` file to a specific route, create a new route group (e.g., `/(overview)`) and then move your `loading.tsx` inside that route group.

![Folder structure showing a loading.tsx and a page.tsx inside the route group](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-loading.png)

Now, the `loading.tsx` file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.

### Creating multiple root layouts

To create multiple [root layouts](/docs/app/api-reference/file-conventions/layout.md#root-layout), remove the top-level `layout.js` file, and add a `layout.js` file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The `<html>` and `<body>` tags need to be added to each root layout.

![Route Groups with Multiple Root Layouts](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-multiple-root-layouts.png)

In the example above, both `(marketing)` and `(shop)` have their own root layout.


--------------------------------------------------------------------------------
title: "Layouts and Pages"
description: "Learn how to create your first pages and layouts, and link between them with the Link component."
source: "https://nextjs.org/docs/app/getting-started/layouts-and-pages"
--------------------------------------------------------------------------------

# Layouts and Pages

Next.js uses **file-system based routing**, meaning you can use folders and files to define routes. This page will guide you through how to create layouts and pages, and link between them.

## Creating a page

A **page** is UI that is rendered on a specific route. To create a page, add a [`page` file](/docs/app/api-reference/file-conventions/page.md) inside the `app` directory and default export a React component. For example, to create an index page (`/`):

![page.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/page-special-file.png)

```tsx filename="app/page.tsx" switcher
export default function Page() {
  return <h1>Hello Next.js!</h1>
}
```

```jsx filename="app/page.js" switcher
export default function Page() {
  return <h1>Hello Next.js!</h1>
}
```

## Creating a layout

A layout is UI that is **shared** between multiple pages. On navigation, layouts preserve state, remain interactive, and do not rerender.

You can define a layout by default exporting a React component from a [`layout` file](/docs/app/api-reference/file-conventions/layout.md). The component should accept a `children` prop which can be a page or another [layout](#nesting-layouts).

For example, to create a layout that accepts your index page as child, add a `layout` file inside the `app` directory:

![layout.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/layout-special-file.png)

```tsx filename="app/layout.tsx" switcher
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        {/* Place children where you want to render a page or nested layout */}
        <main>{children}</main>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function DashboardLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        {/* Place children where you want to render a page or nested layout */}
        <main>{children}</main>
      </body>
    </html>
  )
}
```

The layout above is called a [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout) because it's defined at the root of the `app` directory. The root layout is **required** and must contain `html` and `body` tags.

## Creating a nested route

A nested route is a route composed of multiple URL segments. For example, the `/blog/[slug]` route is composed of three segments:

* `/` (Root Segment)
* `blog` (Segment)
* `[slug]` (Leaf Segment)

In Next.js:

* **Folders** are used to define the route segments that map to URL segments.
* **Files** (like `page` and `layout`) are used to create UI that is shown for a segment.

To create nested routes, you can nest folders inside each other. For example, to add a route for `/blog`, create a folder called `blog` in the `app` directory. Then, to make `/blog` publicly accessible, add a `page.tsx` file:

![File hierarchy showing blog folder and a page.js file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/blog-nested-route.png)

```tsx filename="app/blog/page.tsx" switcher
// Dummy imports
import { getPosts } from '@/lib/posts'
import { Post } from '@/ui/post'

export default async function Page() {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </ul>
  )
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
// Dummy imports
import { getPosts } from '@/lib/posts'
import { Post } from '@/ui/post'

export default async function Page() {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </ul>
  )
}
```

You can continue nesting folders to create nested routes. For example, to create a route for a specific blog post, create a new `[slug]` folder inside `blog` and add a `page` file:

![File hierarchy showing blog folder with a nested slug folder and a page.js file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/blog-post-nested-route.png)

```tsx filename="app/blog/[slug]/page.tsx" switcher
function generateStaticParams() {}

export default function Page() {
  return <h1>Hello, Blog Post Page!</h1>
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
function generateStaticParams() {}

export default function Page() {
  return <h1>Hello, Blog Post Page!</h1>
}
```

Wrapping a folder name in square brackets (e.g. `[slug]`) creates a [dynamic route segment](/docs/app/api-reference/file-conventions/dynamic-routes.md) which is used to generate multiple pages from data. e.g. blog posts, product pages, etc.

## Nesting layouts

By default, layouts in the folder hierarchy are also nested, which means they wrap child layouts via their `children` prop. You can nest layouts by adding `layout` inside specific route segments (folders).

For example, to create a layout for the `/blog` route, add a new `layout` file inside the `blog` folder.

![File hierarchy showing root layout wrapping the blog layout](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/nested-layouts.png)

```tsx filename="app/blog/layout.tsx" switcher
export default function BlogLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

```jsx filename="app/blog/layout.js" switcher
export default function BlogLayout({ children }) {
  return <section>{children}</section>
}
```

If you were to combine the two layouts above, the root layout (`app/layout.js`) would wrap the blog layout (`app/blog/layout.js`), which would wrap the blog (`app/blog/page.js`) and blog post page (`app/blog/[slug]/page.js`).

## Creating a dynamic segment

[Dynamic segments](/docs/app/api-reference/file-conventions/dynamic-routes.md) allow you to create routes that are generated from data. For example, instead of manually creating a route for each individual blog post, you can create a dynamic segment to generate the routes based on blog post data.

To create a dynamic segment, wrap the segment (folder) name in square brackets: `[segmentName]`. For example, in the `app/blog/[slug]/page.tsx` route, the `[slug]` is the dynamic segment.

```tsx filename="app/blog/[slug]/page.tsx" switcher
export default async function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await getPost(slug)

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </div>
  )
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export default async function BlogPostPage({ params }) {
  const { slug } = await params
  const post = await getPost(slug)

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </div>
  )
}
```

Learn more about [Dynamic Segments](/docs/app/api-reference/file-conventions/dynamic-routes.md) and the [`params`](/docs/app/api-reference/file-conventions/page.md#params-optional) props.

Nested [layouts within Dynamic Segments](/docs/app/api-reference/file-conventions/layout.md#params-optional), can also access the `params` props.

## Rendering with search params

In a Server Component **page**, you can access search parameters using the [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) prop:

```tsx filename="app/page.tsx" switcher
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const filters = (await searchParams).filters
}
```

```jsx filename="app/page.jsx" switcher
export default async function Page({ searchParams }) {
  const filters = (await searchParams).filters
}
```

Using `searchParams` opts your page into [**dynamic rendering**](/docs/app/guides/caching.md#dynamic-rendering) because it requires a incoming request to read the search parameters from.

Client Components can read search params using the [`useSearchParams`](/docs/app/api-reference/functions/use-search-params.md) hook.

Learn more about `useSearchParams` in [statically rendered](/docs/app/api-reference/functions/use-search-params.md#static-rendering) and [dynamically rendered](/docs/app/api-reference/functions/use-search-params.md#dynamic-rendering) routes.

### What to use and when

* Use the `searchParams` prop when you need search parameters to **load data for the page** (e.g. pagination, filtering from a database).
* Use `useSearchParams` when search parameters are used **only on the client** (e.g. filtering a list already loaded via props).
* As a small optimization, you can use `new URLSearchParams(window.location.search)` in **callbacks or event handlers** to read search params without triggering re-renders.

## Linking between pages

You can use the [`<Link>` component](/docs/app/api-reference/components/link.md) to navigate between routes. `<Link>` is a built-in Next.js component that extends the HTML `<a>` tag to provide [prefetching](/docs/app/getting-started/linking-and-navigating.md#prefetching) and [client-side navigation](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions).

For example, to generate a list of blog posts, import `<Link>` from `next/link` and pass a `href` prop to the component:

```tsx filename="app/ui/post.tsx" highlight={1,10} switcher
import Link from 'next/link'

export default async function Post({ post }) {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.slug}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/ui/post.js" highlight={1,10}  switcher
import Link from 'next/link'

export default async function Post({ post }) {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.slug}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  )
}
```

> **Good to know**: `<Link>` is the primary way to navigate between routes in Next.js. You can also use the [`useRouter` hook](/docs/app/api-reference/functions/use-router.md) for more advanced navigation.

## Route Props Helpers

Next.js exposes utility types that infer `params` and named slots from your route structure:

* [**PageProps**](/docs/app/api-reference/file-conventions/page.md#page-props-helper): Props for `page` components, including `params` and `searchParams`.
* [**LayoutProps**](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper): Props for `layout` components, including `children` and any named slots (e.g. folders like `@analytics`).

These are globally available helpers, generated when running either `next dev`, `next build` or [`next typegen`](/docs/app/api-reference/cli/next.md#next-typegen-options).

```tsx filename="app/blog/[slug]/page.tsx"
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  return <h1>Blog post: {slug}</h1>
}
```

```tsx filename="app/dashboard/layout.tsx"
export default function Layout(props: LayoutProps<'/dashboard'>) {
  return (
    <section>
      {props.children}
      {/* If you have app/dashboard/@analytics, it appears as a typed slot: */}
      {/* {props.analytics} */}
    </section>
  )
}
```

> **Good to know**
>
> * Static routes resolve `params` to `{}`.
> * `PageProps`, `LayoutProps` are global helpers — no imports required.
> * Types are generated during `next dev`, `next build` or `next typegen`.
## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

- [Linking and Navigating](/docs/app/getting-started/linking-and-navigating.md)
  - Learn how the built-in navigation optimizations work, including prefetching, prerendering, and client-side navigation, and how to optimize navigation for dynamic routes and slow networks.
- [layout.js](/docs/app/api-reference/file-conventions/layout.md)
  - API reference for the layout.js file.
- [page.js](/docs/app/api-reference/file-conventions/page.md)
  - API reference for the page.js file.
- [Link Component](/docs/app/api-reference/components/link.md)
  - Enable fast client-side navigation with the built-in `next/link` component.
- [Dynamic Segments](/docs/app/api-reference/file-conventions/dynamic-routes.md)
  - Dynamic Route Segments can be used to programmatically generate route segments from dynamic data.


--------------------------------------------------------------------------------
title: "Linking and Navigating"
description: "Learn how the built-in navigation optimizations work, including prefetching, prerendering, and client-side navigation, and how to optimize navigation for dynamic routes and slow networks."
source: "https://nextjs.org/docs/app/getting-started/linking-and-navigating"
--------------------------------------------------------------------------------

# Linking and Navigating

In Next.js, routes are rendered on the server by default. This often means the client has to wait for a server response before a new route can be shown. Next.js comes with built-in [prefetching](#prefetching), [streaming](#streaming), and [client-side transitions](#client-side-transitions) ensuring navigation stays fast and responsive.

This guide explains how navigation works in Next.js and how you can optimize it for [dynamic routes](#dynamic-routes-without-loadingtsx) and [slow networks](#slow-networks).

## How navigation works

To understand how navigation works in Next.js, it helps to be familiar with the following concepts:

* [Server Rendering](#server-rendering)
* [Prefetching](#prefetching)
* [Streaming](#streaming)
* [Client-side transitions](#client-side-transitions)

### Server Rendering

In Next.js, [Layouts and Pages](/docs/app/getting-started/layouts-and-pages.md) are [React Server Components](https://react.dev/reference/rsc/server-components) by default. On initial and subsequent navigations, the [Server Component Payload](/docs/app/getting-started/server-and-client-components.md#how-do-server-and-client-components-work-in-nextjs) is generated on the server before being sent to the client.

There are two types of server rendering, based on *when* it happens:

* **Static Rendering (or Prerendering)** happens at build time or during [revalidation](/docs/app/getting-started/caching-and-revalidating.md) and the result is cached.
* **Dynamic Rendering** happens at request time in response to a client request.

The trade-off of server rendering is that the client must wait for the server to respond before the new route can be shown. Next.js addresses this delay by [prefetching](#prefetching) routes the user is likely to visit and performing [client-side transitions](#client-side-transitions).

> **Good to know**: HTML is also generated for the initial visit.

### Prefetching

Prefetching is the process of loading a route in the background before the user navigates to it. This makes navigation between routes in your application feel instant, because by the time a user clicks on a link, the data to render the next route is already available client side.

Next.js automatically prefetches routes linked with the [`<Link>` component](/docs/app/api-reference/components/link.md) when they enter the user's viewport.

```tsx filename="app/layout.tsx" switcher
import Link from 'next/link'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <nav>
          {/* Prefetched when the link is hovered or enters the viewport */}
          <Link href="/blog">Blog</Link>
          {/* No prefetching */}
          <a href="/contact">Contact</a>
        </nav>
        {children}
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import Link from 'next/link'

export default function Layout() {
  return (
    <html>
      <body>
        <nav>
          {/* Prefetched when the link is hovered or enters the viewport */}
          <Link href="/blog">Blog</Link>
          {/* No prefetching */}
          <a href="/contact">Contact</a>
        </nav>
        {children}
      </body>
    </html>
  )
}
```

How much of the route is prefetched depends on whether it's static or dynamic:

* **Static Route**: the full route is prefetched.
* **Dynamic Route**: prefetching is skipped, or the route is partially prefetched if [`loading.tsx`](/docs/app/api-reference/file-conventions/loading.md) is present.

By skipping or partially prefetching dynamic routes, Next.js avoids unnecessary work on the server for routes the users may never visit. However, waiting for a server response before navigation can give the users the impression that the app is not responding.

![Server Rendering without Streaming](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/server-rendering-without-streaming.png)

To improve the navigation experience to dynamic routes, you can use [streaming](#streaming).

### Streaming

Streaming allows the server to send parts of a dynamic route to the client as soon as they're ready, rather than waiting for the entire route to be rendered. This means users see something sooner, even if parts of the page are still loading.

For dynamic routes, it means they can be **partially prefetched**. That is, shared layouts and loading skeletons can be requested ahead of time.

![How Server Rendering with Streaming Works](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/server-rendering-with-streaming.png)

To use streaming, create a `loading.tsx` in your route folder:

![loading.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-special-file.png)

```tsx filename="app/dashboard/loading.tsx" switcher
export default function Loading() {
  // Add fallback UI that will be shown while the route is loading.
  return <LoadingSkeleton />
}
```

```jsx filename="app/dashboard/loading.js" switcher
export default function Loading() {
  // Add fallback UI that will be shown while the route is loading.
  return <LoadingSkeleton />
}
```

Behind the scenes, Next.js will automatically wrap the `page.tsx` contents in a `<Suspense>` boundary. The prefetched fallback UI will be shown while the route is loading, and swapped for the actual content once ready.

> **Good to know**: You can also use [`<Suspense>`](https://react.dev/reference/react/Suspense) to create loading UI for nested components.

Benefits of `loading.tsx`:

* Immediate navigation and visual feedback for the user.
* Shared layouts remain interactive and navigation is interruptible.
* Improved Core Web Vitals: [TTFB](https://web.dev/articles/ttfb), [FCP](https://web.dev/articles/fcp), and [TTI](https://web.dev/articles/tti).

To further improve the navigation experience, Next.js performs a [client-side transition](#client-side-transitions) with the `<Link>` component.

### Client-side transitions

Traditionally, navigation to a server-rendered page triggers a full page load. This clears state, resets scroll position, and blocks interactivity.

Next.js avoids this with client-side transitions using the `<Link>` component. Instead of reloading the page, it updates the content dynamically by:

* Keeping any shared layouts and UI.
* Replacing the current page with the prefetched loading state or a new page if available.

Client-side transitions are what makes a server-rendered apps *feel* like client-rendered apps. And when paired with [prefetching](#prefetching) and [streaming](#streaming), it enables fast transitions, even for dynamic routes.

## What can make transitions slow?

These Next.js optimizations make navigation fast and responsive. However, under certain conditions, transitions can still *feel* slow. Here are some common causes and how to improve the user experience:

### Dynamic routes without `loading.tsx`

When navigating to a dynamic route, the client must wait for the server response before showing the result. This can give the users the impression that the app is not responding.

We recommend adding `loading.tsx` to dynamic routes to enable partial prefetching, trigger immediate navigation, and display a loading UI while the route renders.

```tsx filename="app/blog/[slug]/loading.tsx" switcher
export default function Loading() {
  return <LoadingSkeleton />
}
```

```jsx filename="app/blog/[slug]/loading.js" switcher
export default function Loading() {
  return <LoadingSkeleton />
}
```

> **Good to know**: In development mode, you can use the Next.js Devtools to identify if the route is static or dynamic. See [`devIndicators`](/docs/app/api-reference/config/next-config-js/devIndicators.md) for more information.

### Dynamic segments without `generateStaticParams`

If a [dynamic segment](/docs/app/api-reference/file-conventions/dynamic-routes.md) could be prerendered but isn't because it's missing [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md), the route will fallback to dynamic rendering at request time.

Ensure the route is statically generated at build time by adding `generateStaticParams`:

```tsx filename="app/blog/[slug]/page.tsx" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))

export default async function Page({ params }) {
  const { slug } = await params
  // ...
}
```

### Slow networks

On slow or unstable networks, prefetching may not finish before the user clicks a link. This can affect both static and dynamic routes. In these cases, the `loading.js` fallback may not appear immediately because it hasn't been prefetched yet.

To improve perceived performance, you can use the [`useLinkStatus` hook](/docs/app/api-reference/functions/use-link-status.md) to show immediate feedback while the transition is in progress.

```tsx filename="app/ui/loading-indicator.tsx" switcher
'use client'

import { useLinkStatus } from 'next/link'

export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

```jsx filename="app/ui/loading-indicator.js" switcher
'use client'

import { useLinkStatus } from 'next/link'

export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

You can "debounce" the hint by adding an initial animation delay (e.g. 100ms) and starting as invisible (e.g. `opacity: 0`). This means the loading indicator will only be shown if the navigation takes longer than the specified delay. See the [`useLinkStatus` reference](/docs/app/api-reference/functions/use-link-status.md#gracefully-handling-fast-navigation) for a CSS example.

> **Good to know**: You can use other visual feedback patterns like a progress bar. View an example [here](https://github.com/vercel/react-transition-progress).

### Disabling prefetching

You can opt out of prefetching by setting the `prefetch` prop to `false` on the `<Link>` component. This is useful to avoid unnecessary usage of resources when rendering large lists of links (e.g. an infinite scroll table).

```tsx
<Link prefetch={false} href="/blog">
  Blog
</Link>
```

However, disabling prefetching comes with trade-offs:

* **Static routes** will only be fetched when the user clicks the link.
* **Dynamic routes** will need to be rendered on the server first before the client can navigate to it.

To reduce resource usage without fully disabling prefetch, you can prefetch only on hover. This limits prefetching to routes the user is more *likely* to visit, rather than all links in the viewport.

```tsx filename="app/ui/hover-prefetch-link.tsx" switcher
'use client'

import Link from 'next/link'
import { useState } from 'react'

function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)

  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

```jsx filename="app/ui/hover-prefetch-link.js" switcher
'use client'

import Link from 'next/link'
import { useState } from 'react'

function HoverPrefetchLink({ href, children }) {
  const [active, setActive] = useState(false)

  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

### Hydration not completed

`<Link>` is a Client Component and must be hydrated before it can prefetch routes. On the initial visit, large JavaScript bundles can delay hydration, preventing prefetching from starting right away.

React mitigates this with Selective Hydration and you can further improve this by:

* Using the [`@next/bundle-analyzer`](/docs/app/guides/package-bundling.md#analyzing-javascript-bundles) plugin to identify and reduce bundle size by removing large dependencies.
* Moving logic from the client to the server where possible. See the [Server and Client Components](/docs/app/getting-started/server-and-client-components.md) docs for guidance.

## Examples

### Native History API

Next.js allows you to use the native [`window.history.pushState`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) and [`window.history.replaceState`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) methods to update the browser's history stack without reloading the page.

`pushState` and `replaceState` calls integrate into the Next.js Router, allowing you to sync with [`usePathname`](/docs/app/api-reference/functions/use-pathname.md) and [`useSearchParams`](/docs/app/api-reference/functions/use-search-params.md).

#### `window.history.pushState`

Use it to add a new entry to the browser's history stack. The user can navigate back to the previous state. For example, to sort a list of products:

```tsx fileName="app/ui/sort-products.tsx" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SortProducts() {
  const searchParams = useSearchParams()

  function updateSorting(sortOrder: string) {
    const params = new URLSearchParams(searchParams.toString())
    params.set('sort', sortOrder)
    window.history.pushState(null, '', `?${params.toString()}`)
  }

  return (
    <>
      <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
      <button onClick={() => updateSorting('desc')}>Sort Descending</button>
    </>
  )
}
```

```jsx fileName="app/ui/sort-products.js" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SortProducts() {
  const searchParams = useSearchParams()

  function updateSorting(sortOrder) {
    const params = new URLSearchParams(searchParams.toString())
    params.set('sort', sortOrder)
    window.history.pushState(null, '', `?${params.toString()}`)
  }

  return (
    <>
      <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
      <button onClick={() => updateSorting('desc')}>Sort Descending</button>
    </>
  )
}
```

#### `window.history.replaceState`

Use it to replace the current entry on the browser's history stack. The user is not able to navigate back to the previous state. For example, to switch the application's locale:

```tsx fileName="app/ui/locale-switcher.tsx" switcher
'use client'

import { usePathname } from 'next/navigation'

export function LocaleSwitcher() {
  const pathname = usePathname()

  function switchLocale(locale: string) {
    // e.g. '/en/about' or '/fr/contact'
    const newPath = `/${locale}${pathname}`
    window.history.replaceState(null, '', newPath)
  }

  return (
    <>
      <button onClick={() => switchLocale('en')}>English</button>
      <button onClick={() => switchLocale('fr')}>French</button>
    </>
  )
}
```

```jsx fileName="app/ui/locale-switcher.js" switcher
'use client'

import { usePathname } from 'next/navigation'

export function LocaleSwitcher() {
  const pathname = usePathname()

  function switchLocale(locale) {
    // e.g. '/en/about' or '/fr/contact'
    const newPath = `/${locale}${pathname}`
    window.history.replaceState(null, '', newPath)
  }

  return (
    <>
      <button onClick={() => switchLocale('en')}>English</button>
      <button onClick={() => switchLocale('fr')}>French</button>
    </>
  )
}
```
- [Link Component](/docs/app/api-reference/components/link.md)
  - Enable fast client-side navigation with the built-in `next/link` component.
- [loading.js](/docs/app/api-reference/file-conventions/loading.md)
  - API reference for the loading.js file.
- [Prefetching](/docs/app/guides/prefetching.md)
  - Learn how to configure prefetching in Next.js


--------------------------------------------------------------------------------
title: "Server and Client Components"
description: "Learn how you can use React Server and Client Components to render parts of your application on the server or the client."
source: "https://nextjs.org/docs/app/getting-started/server-and-client-components"
--------------------------------------------------------------------------------

# Server and Client Components

By default, layouts and pages are [Server Components](https://react.dev/reference/rsc/server-components), which lets you fetch data and render parts of your UI on the server, optionally cache the result, and stream it to the client. When you need interactivity or browser APIs, you can use [Client Components](https://react.dev/reference/rsc/use-client) to layer in functionality.

This page explains how Server and Client Components work in Next.js and when to use them, with examples of how to compose them together in your application.

## When to use Server and Client Components?

The client and server environments have different capabilities. Server and Client components allow you to run logic in each environment depending on your use case.

Use **Client Components** when you need:

* [State](https://react.dev/learn/managing-state) and [event handlers](https://react.dev/learn/responding-to-events). E.g. `onClick`, `onChange`.
* [Lifecycle logic](https://react.dev/learn/lifecycle-of-reactive-effects). E.g. `useEffect`.
* Browser-only APIs. E.g. `localStorage`, `window`, `Navigator.geolocation`, etc.
* [Custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks).

Use **Server Components** when you need:

* Fetch data from databases or APIs close to the source.
* Use API keys, tokens, and other secrets without exposing them to the client.
* Reduce the amount of JavaScript sent to the browser.
* Improve the [First Contentful Paint (FCP)](https://web.dev/fcp/), and stream content progressively to the client.

For example, the `<Page>` component is a Server Component that fetches data about a post, and passes it as props to the `<LikeButton>` which handles client-side interactivity.

```tsx filename="app/[id]/page.tsx" highlight={1,12} switcher
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)

  return (
    <div>
      <main>
        <h1>{post.title}</h1>
        {/* ... */}
        <LikeButton likes={post.likes} />
      </main>
    </div>
  )
}
```

```jsx filename="app/[id]/page.js" highlight={1,12} switcher
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'

export default async function Page({ params }) {
  const post = await getPost(params.id)

  return (
    <div>
      <main>
        <h1>{post.title}</h1>
        {/* ... */}
        <LikeButton likes={post.likes} />
      </main>
    </div>
  )
}
```

```tsx filename="app/ui/like-button.tsx" highlight={1} switcher
'use client'

import { useState } from 'react'

export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```

```jsx filename="app/ui/like-button.js" highlight={1} switcher
'use client'

import { useState } from 'react'

export default function LikeButton({ likes }) {
  // ...
}
```

## How do Server and Client Components work in Next.js?

### On the server

On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks, by individual route segments ([layouts and pages](/docs/app/getting-started/layouts-and-pages.md)):

* **Server Components** are rendered into a special data format called the React Server Component Payload (RSC Payload).
* **Client Components** and the RSC Payload are used to [pre-render](/docs/app/guides/caching.md#rendering-strategies) HTML.

> **What is the React Server Component Payload (RSC)?**
>
> The RSC Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The RSC Payload contains:
>
> * The rendered result of Server Components
> * Placeholders for where Client Components should be rendered and references to their JavaScript files
> * Any props passed from a Server Component to a Client Component

### On the client (first load)

Then, on the client:

1. **HTML** is used to immediately show a fast non-interactive preview of the route to the user.
2. **RSC Payload** is used to reconcile the Client and Server Component trees.
3. **JavaScript** is used to hydrate Client Components and make the application interactive.

> **What is hydration?**
>
> Hydration is React's process for attaching [event handlers](https://react.dev/learn/responding-to-events) to the DOM, to make the static HTML interactive.

### Subsequent Navigations

On subsequent navigations:

* The **RSC Payload** is prefetched and cached for instant navigation.
* **Client Components** are rendered entirely on the client, without the server-rendered HTML.

## Examples

### Using Client Components

You can create a Client Component by adding the [`"use client"`](https://react.dev/reference/react/use-client) directive at the top of the file, above your imports.

```tsx filename="app/ui/counter.tsx" highlight={1} switcher
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>{count} likes</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
```

```jsx filename="app/ui/counter.js" highlight={1} switcher
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>{count} likes</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
```

`"use client"` is used to declare a **boundary** between the Server and Client module graphs (trees).

Once a file is marked with `"use client"`, **all its imports and child components are considered part of the client bundle**. This means you don't need to add the directive to every component that is intended for the client.

### Reducing JS bundle size

To reduce the size of your client JavaScript bundles, add `'use client'` to specific interactive components instead of marking large parts of your UI as Client Components.

For example, the `<Layout>` component contains mostly static elements like a logo and navigation links, but includes an interactive search bar. `<Search />` is interactive and needs to be a Client Component, however, the rest of the layout can remain a Server Component.

```tsx filename="app/layout.tsx" highlight={12} switcher
// Client Component
import Search from './search'
// Server Component
import Logo from './logo'

// Layout is a Server Component by default
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <nav>
        <Logo />
        <Search />
      </nav>
      <main>{children}</main>
    </>
  )
}
```

```jsx filename="app/layout.js" highlight={12} switcher
// Client Component
import Search from './search'
// Server Component
import Logo from './logo'

// Layout is a Server Component by default
export default function Layout({ children }) {
  return (
    <>
      <nav>
        <Logo />
        <Search />
      </nav>
      <main>{children}</main>
    </>
  )
}
```

```tsx filename="app/ui/search.tsx" highlight={1} switcher
'use client'

export default function Search() {
  // ...
}
```

```jsx filename="app/ui/search.js" highlight={1} switcher
'use client'

export default function Search() {
  // ...
}
```

### Passing data from Server to Client Components

You can pass data from Server Components to Client Components using props.

```tsx filename="app/[id]/page.tsx" highlight={1,7} switcher
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)

  return <LikeButton likes={post.likes} />
}
```

```jsx filename="app/[id]/page.js" highlight={1,7} switcher
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'

export default async function Page({ params }) {
  const post = await getPost(params.id)

  return <LikeButton likes={post.likes} />
}
```

```tsx filename="app/ui/like-button.tsx" highlight={1} switcher
'use client'

export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```

```jsx filename="app/ui/like-button.js" highlight={1} switcher
'use client'

export default function LikeButton({ likes }) {
  // ...
}
```

Alternatively, you can stream data from a Server Component to a Client Component with the [`use` Hook](https://react.dev/reference/react/use). See an [example](/docs/app/getting-started/fetching-data.md#streaming-data-with-the-use-hook).

> **Good to know**: Props passed to Client Components need to be [serializable](https://react.dev/reference/react/use-server#serializable-parameters-and-return-values) by React.

### Interleaving Server and Client Components

You can pass Server Components as a prop to a Client Component. This allows you to visually nest server-rendered UI within Client components.

A common pattern is to use `children` to create a *slot* in a `<ClientComponent>`. For example, a `<Cart>` component that fetches data on the server, inside a `<Modal>` component that uses client state to toggle visibility.

```tsx filename="app/ui/modal.tsx" switcher
'use client'

export default function Modal({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}
```

```jsx filename="app/ui/modal.js" switcher
'use client'

export default function Modal({ children }) {
  return <div>{children}</div>
}
```

Then, in a parent Server Component (e.g.`<Page>`), you can pass a `<Cart>` as the child of the `<Modal>`:

```tsx filename="app/page.tsx"  highlight={7} switcher
import Modal from './ui/modal'
import Cart from './ui/cart'

export default function Page() {
  return (
    <Modal>
      <Cart />
    </Modal>
  )
}
```

```jsx filename="app/page.js" highlight={7} switcher
import Modal from './ui/modal'
import Cart from './ui/cart'

export default function Page() {
  return (
    <Modal>
      <Cart />
    </Modal>
  )
}
```

In this pattern, all Server Components will be rendered on the server ahead of time, including those as props. The resulting RSC payload will contain references of where Client Components should be rendered within the component tree.

### Context providers

[React context](https://react.dev/learn/passing-data-deeply-with-context) is commonly used to share global state like the current theme. However, React context is not supported in Server Components.

To use context, create a Client Component that accepts `children`:

```tsx filename="app/theme-provider.tsx" switcher
'use client'

import { createContext } from 'react'

export const ThemeContext = createContext({})

export default function ThemeProvider({
  children,
}: {
  children: React.ReactNode
}) {
  return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>
}
```

```jsx filename="app/theme-provider.js" switcher
'use client'

import { createContext } from 'react'

export const ThemeContext = createContext({})

export default function ThemeProvider({ children }) {
  return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>
}
```

Then, import it into a Server Component (e.g. `layout`):

```tsx filename="app/layout.tsx" switcher
import ThemeProvider from './theme-provider'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import ThemeProvider from './theme-provider'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  )
}
```

Your Server Component will now be able to directly render your provider, and all other Client Components throughout your app will be able to consume this context.

> **Good to know**: You should render providers as deep as possible in the tree – notice how `ThemeProvider` only wraps `{children}` instead of the entire `<html>` document. This makes it easier for Next.js to optimize the static parts of your Server Components.

### Third-party components

When using a third-party component that relies on client-only features, you can wrap it in a Client Component to ensure it works as expected.

For example, the `<Carousel />` can be imported from the `acme-carousel` package. This component uses `useState`, but it doesn't yet have the `"use client"` directive.

If you use `<Carousel />` within a Client Component, it will work as expected:

```tsx filename="app/gallery.tsx" switcher
'use client'

import { useState } from 'react'
import { Carousel } from 'acme-carousel'

export default function Gallery() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div>
      <button onClick={() => setIsOpen(true)}>View pictures</button>
      {/* Works, since Carousel is used within a Client Component */}
      {isOpen && <Carousel />}
    </div>
  )
}
```

```jsx filename="app/gallery.js" switcher
'use client'

import { useState } from 'react'
import { Carousel } from 'acme-carousel'

export default function Gallery() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div>
      <button onClick={() => setIsOpen(true)}>View pictures</button>
      {/*  Works, since Carousel is used within a Client Component */}
      {isOpen && <Carousel />}
    </div>
  )
}
```

However, if you try to use it directly within a Server Component, you'll see an error. This is because Next.js doesn't know `<Carousel />` is using client-only features.

To fix this, you can wrap third-party components that rely on client-only features in your own Client Components:

```tsx filename="app/carousel.tsx" switcher
'use client'

import { Carousel } from 'acme-carousel'

export default Carousel
```

```jsx filename="app/carousel.js" switcher
'use client'

import { Carousel } from 'acme-carousel'

export default Carousel
```

Now, you can use `<Carousel />` directly within a Server Component:

```tsx filename="app/page.tsx" switcher
import Carousel from './carousel'

export default function Page() {
  return (
    <div>
      <p>View pictures</p>
      {/*  Works, since Carousel is a Client Component */}
      <Carousel />
    </div>
  )
}
```

```jsx filename="app/page.js" switcher
import Carousel from './carousel'

export default function Page() {
  return (
    <div>
      <p>View pictures</p>
      {/*  Works, since Carousel is a Client Component */}
      <Carousel />
    </div>
  )
}
```

> **Advice for Library Authors**
>
> If you’re building a component library, add the `"use client"` directive to entry points that rely on client-only features. This lets your users import components into Server Components without needing to create wrappers.
>
> It's worth noting some bundlers might strip out `"use client"` directives. You can find an example of how to configure esbuild to include the `"use client"` directive in the [React Wrap Balancer](https://github.com/shuding/react-wrap-balancer/blob/main/tsup.config.ts#L10-L13) and [Vercel Analytics](https://github.com/vercel/analytics/blob/main/packages/web/tsup.config.js#L26-L30) repositories.

### Preventing environment poisoning

JavaScript modules can be shared between both Server and Client Components modules. This means it's possible to accidentally import server-only code into the client. For example, consider the following function:

```ts filename="lib/data.ts" switcher
export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })

  return res.json()
}
```

```js filename="lib/data.js" switcher
export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })

  return res.json()
}
```

This function contains an `API_KEY` that should never be exposed to the client.

In Next.js, only environment variables prefixed with `NEXT_PUBLIC_` are included in the client bundle. If variables are not prefixed, Next.js replaces them with an empty string.

As a result, even though `getData()` can be imported and executed on the client, it won't work as expected.

To prevent accidental usage in Client Components, you can use the [`server-only` package](https://www.npmjs.com/package/server-only).

Then, import the package into a file that contains server-only code:

```js filename="lib/data.js"
import 'server-only'

export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })

  return res.json()
}
```

Now, if you try to import the module into a Client Component, there will be a build-time error.

The corresponding [`client-only` package](https://www.npmjs.com/package/client-only) can be used to mark modules that contain client-only logic like code that accesses the `window` object.

In Next.js, installing `server-only` or `client-only` is **optional**. However, if your linting rules flag extraneous dependencies, you may install them to avoid issues.

```bash package="npm"
npm install server-only
```

```bash package="yarn"
yarn add server-only
```

```bash package="pnpm"
pnpm add server-only
```

```bash package="bun"
bun add server-only
```

Next.js handles `server-only` and `client-only` imports internally to provide clearer error messages when a module is used in the wrong environment. The contents of these packages from NPM are not used by Next.js.

Next.js also provides its own type declarations for `server-only` and `client-only`, for TypeScript configurations where [`noUncheckedSideEffectImports`](https://www.typescriptlang.org/tsconfig/#noUncheckedSideEffectImports) is active.
## Next Steps

Learn more about the APIs mentioned in this page.

- [use client](/docs/app/api-reference/directives/use-client.md)
  - Learn how to use the use client directive to render a component on the client.


--------------------------------------------------------------------------------
title: "Cache Components"
description: "Learn how to use Cache Components and combine the benefits of static and dynamic rendering."
source: "https://nextjs.org/docs/app/getting-started/cache-components"
--------------------------------------------------------------------------------

# Cache Components

Cache Components is a new approach to rendering and caching in Next.js that provides fine-grained control over what gets cached and when, while ensuring a great user experience through **Partial Prerendering (PPR)**.

## Cache Components

When developing dynamic applications, you have to balance two primary approaches:

* **Fully static pages** load fast but can't show personalized or real-time data
* **Fully dynamic pages** can show fresh data but require rendering everything on each request, leading to slower initial loads

With Cache Components enabled, Next.js treats all routes as **dynamic by default**. Every request renders with the latest available data. However, most pages are made up of both static and dynamic parts, and not all dynamic data needs to be resolved from source on every request.

Cache Components allows you to mark data, and even parts of your UI as cacheable, which includes them in the pre-render pass alongside static parts of the page.

> **Before Cache Components**, Next.js tried to statically optimize **entire** pages automatically, which could lead to unexpected behavior when adding dynamic code.

Cache Components implements **Partial Prerendering (PPR)**, and `use cache` to give you the best of both worlds:

![Partially re-rendered Product Page showing static nav and product information, and dynamic cart and recommended products](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/learn/light/thinking-in-ppr.png)

When a user visits a route:

* The server sends a **static shell** containing cached content, ensuring a fast initial load
* Dynamic sections wrapped in `Suspense` boundaries display fallback UI in the shell
* Only the dynamic parts render to replace their fallbacks, streaming in parallel as they become ready
* You can include otherwise-dynamic data in the initial shell by caching it with `use cache`

> **🎥 Watch:** Why PPR and how it works → [YouTube (10 minutes)](https://www.youtube.com/watch?v=MTcPrTIBkpA).

## How it works

> **Good to know:** Cache Components is an opt-in feature. Enable it by setting the `cacheComponents` flag to `true` in your Next config file. See [Enabling Cache Components](#enabling-cache-components) for more details.

Cache Components gives you three key tools to control rendering:

### 1. Suspense for runtime data

Some data is only available at runtime when an actual user makes a request. APIs like [`cookies`](/docs/app/api-reference/functions/cookies.md), [`headers`](/docs/app/api-reference/functions/headers.md), and [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) access request-specific information. Wrap components using these APIs in `Suspense` boundaries so the rest of the page can be pre-rendered as a static shell.

**Runtime APIs include:**

* [`cookies`](/docs/app/api-reference/functions/cookies.md)
* [`headers`](/docs/app/api-reference/functions/headers.md)
* [`searchParams` prop](/docs/app/api-reference/file-conventions/page.md#searchparams-optional)
* [`params` prop](/docs/app/api-reference/file-conventions/page.md#params-optional) - This is runtime data unless you provide at least one example value through [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md). When provided, those specific param values are treated as static for prerendered paths, while other values remain runtime

### 2. Suspense for dynamic data

Dynamic data like [`fetch`](/docs/app/api-reference/functions/fetch.md) calls or database queries (`db.query(...)`) can change between requests but isn't user-specific. The [`connection`](/docs/app/api-reference/functions/connection.md) API is meta-dynamic—it represents waiting for a user navigation even though there's no actual data to return. Wrap components that use these in `Suspense` boundaries to enable streaming.

**Dynamic data patterns include:**

* [`fetch`](/docs/app/api-reference/functions/fetch.md) requests
* Database queries
* [`connection`](/docs/app/api-reference/functions/connection.md)

### 3. Cached data with `use cache`

Add `use cache` to any Server Component to make it cached and include it in the pre-rendered shell. You cannot use runtime APIs from inside a cached component. You can also mark utility functions as `use cache` and call them from Server Components.

```tsx
export async function getProducts() {
  'use cache'
  const data = await db.query('SELECT * FROM products')
  return data
}
```

## Using Suspense boundaries

React [Suspense](https://react.dev/reference/react/Suspense) boundaries let you define what fallback UI to use when it wraps dynamic or runtime data.

Content outside the boundary, including the fallback UI, is pre-rendered as a static shell, while content inside the boundary streams in when ready.

Here's how to use `Suspense` with Cache Components:

```tsx filename="app/page.tsx" switcher
import { Suspense } from 'react'

export default function Page() {
  return (
    <>
      <h1>This will be pre-rendered</h1>
      <Suspense fallback={<Skeleton />}>
        <DynamicContent />
      </Suspense>
    </>
  )
}

async function DynamicContent() {
  const res = await fetch('http://api.cms.com/posts')
  const { posts } = await res.json()
  return <div>{/* ... */}</div>
}
```

```jsx filename="app/page.js" switcher
import { Suspense } from 'react'

export default function Page() {
  return (
    <>
      <h1>This will be pre-rendered</h1>
      <Suspense fallback={<Skeleton />}>
        <DynamicContent />
      </Suspense>
    </>
  )
}

async function DynamicContent() {
  const res = await fetch('http://api.cms.com/posts')
  const { posts } = await res.json()
  return <div>{/* ... */}</div>
}
```

At build time, Next.js pre-renders the static content and the `fallback` UI, while the dynamic content is postponed until a user requests the route.

> **Good to know**: Wrapping a component in `Suspense` doesn't make it dynamic; your API usage does. `Suspense` acts as a boundary that encapsulates dynamic content and enables streaming.

### Missing Suspense boundaries

Cache Components enforces that dynamic code must be wrapped in a `Suspense` boundary. If you forget, you'll see the [Uncached data was accessed outside of `<Suspense>`](https://nextjs.org/docs/messages/blocking-route) error:

> **Uncached data was accessed outside of `<Suspense>`**
>
> This delays the entire page from rendering, resulting in a slow user
> experience. Next.js uses this error to ensure your app loads instantly
> on every navigation.
>
> To fix this, you can either:
>
> **Wrap the component in a `<Suspense>`** boundary. This allows Next.js to stream its contents to the user as soon as it's ready, without blocking the rest of the app.
>
> or
>
> **Move the asynchronous await into a Cache Component("use cache")**. This allows Next.js to statically prerender the component as part of the HTML document, so it's instantly visible to the user.
>
> Note that request-specific information, such as params, cookies, and headers, is not available during static prerendering, so it must be wrapped in `<Suspense>`.

This error helps prevent a situation where, instead of getting a static shell instantly, users would hit a blocking runtime render with nothing to show. To fix it, add a `Suspense` boundary or use `use cache` to cache the work instead.

### How streaming works

Streaming splits the route into chunks and progressively streams them to the client as they become ready.
This allows the user to see parts of the page immediately, before the entire content has finished
rendering.

![Diagram showing partially rendered page on the client, with loading UI for chunks that are being streamed.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/server-rendering-with-streaming.png)

With partial pre-rendering, the initial UI can be sent immediately to the browser while the dynamic parts render. This decreases time to UI and may decrease total request time depending on how much of your UI is pre-rendered.

![Diagram showing parallelization of route segments during streaming, showing data fetching,rendering, and hydration of individual chunks.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/sequential-parallel-data-fetching.png)

To reduce network overhead, the full response, including static HTML and streamed dynamic parts, is sent in a **single HTTP request**. This avoids extra round-trips and improves both initial load and overall performance.

## Using `use cache`

While `Suspense` boundaries manage dynamic content, the [`use cache`](/docs/app/api-reference/directives/use-cache.md) directive is available for caching data or computations that don't change often.

### Basic usage

Add `use cache` to cache a page, component, or async function, and define a lifetime with [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md):

```tsx filename="app/page.tsx" highlight={1,4,5} switcher
import { cacheLife } from 'next/cache'

export default async function Page() {
  'use cache'
  cacheLife('hours')
  // fetch or compute
  return <div>...</div>
}
```

```jsx filename="app/page.js" highlight={1,4,5} switcher
import { cacheLife } from 'next/cache'

export default async function Page() {
  'use cache'
  cacheLife('hours')
  // fetch or compute
  return <div>...</div>
}
```

### Caveats

When using `use cache`, keep these constraints in mind:

#### Arguments must be serializable

Like Server Actions, arguments to cached functions must be serializable. This means you can pass primitives, plain objects, and arrays, but not class instances, functions, or other complex types.

#### Accepting unserializable values without introspection

You can accept unserializable values as arguments as long as you don't introspect them. However, you can return them. This allows patterns like cached components that accept Server or Client Components as children:

```tsx filename="app/cached-wrapper.tsx" switcher
import type { ReactNode } from 'react'
import { setTimeout } from 'node:timers/promises'

async function getSiteTitle() {
  // Simulate a slow database or API call
  await setTimeout(1000) // from 'node:timers/promises'
  return 'My Website'
}

export async function CachedWrapper({ children }: { children: ReactNode }) {
  'use cache'
  const title = await getSiteTitle()

  // Don't introspect children, just pass it through
  return (
    <div className="wrapper">
      <h1>{title}</h1>
      {children}
    </div>
  )
}
```

```jsx filename="app/cached-wrapper.js" switcher
import { setTimeout } from 'node:timers/promises'

async function getSiteTitle() {
  // Simulate a slow database or API call
  await setTimeout(1000) // from 'node:timers/promises'
  return 'My Website'
}

export async function CachedWrapper({ children }) {
  'use cache'
  const title = await getSiteTitle()

  // Don't introspect children, just pass it through
  return (
    <div className="wrapper">
      <h1>{title}</h1>
      {children}
    </div>
  )
}
```

### Tagging and revalidating

Tag cached data with [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) and revalidate it after mutations using [`updateTag`](/docs/app/api-reference/functions/updateTag.md) in Server Actions for immediate updates, or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) delay in updates are acceptable.

#### With `updateTag`

Use `updateTag` when you need to expire and immediately refresh cached data within the same request:

```tsx filename="app/actions.ts" highlight={1,4,5,13}
import { cacheTag, updateTag } from 'next/cache'

export async function getCart() {
  'use cache'
  cacheTag('cart')
  // fetch data
}

export async function updateCart(itemId: string) {
  'use server'
  // write data using the itemId
  // update the user cart
  updateTag('cart')
}
```

#### With `revalidateTag`

Use `revalidateTag` when you want to invalidate only properly tagged cached entries with stale-while-revalidate behavior. This is ideal for static content that can tolerate eventual consistency.

```tsx filename="app/actions.ts" highlight={1,4,5,12}
import { cacheTag, revalidateTag } from 'next/cache'

export async function getPosts() {
  'use cache'
  cacheTag('posts')
  // fetch data
}

export async function createPost(post: FormData) {
  'use server'
  // write data using the FormData
  revalidateTag('posts', 'max')
}
```

For more detailed explanation and usage examples, see the [`use cache` API reference](/docs/app/api-reference/directives/use-cache.md).

## Enabling Cache Components

You can enable Cache Components (which includes PPR) by adding the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) option to your Next config file:

```ts filename="next.config.ts" highlight={4} switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```js filename="next.config.js" highlight={3} switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}

module.exports = nextConfig
```

### Navigation with Cache Components

When the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) flag is enabled, Next.js uses React's [`<Activity>`](https://react.dev/reference/react/Activity) component to preserve component state during client-side navigation.

Rather than unmounting the previous route when you navigate away, Next.js sets the Activity mode to [`"hidden"`](https://react.dev/reference/react/Activity#activity). This means:

* Component state is preserved when navigating between routes
* When you navigate back, the previous route reappears with its state intact
* Effects are cleaned up when a route is hidden, and recreated when it becomes visible again

This behavior improves the navigation experience by maintaining UI state (form inputs, or expanded sections) when users navigate back and forth between routes.

> **Good to know**: Next.js uses heuristics to keep a few recently visited routes [`"hidden"`](https://react.dev/reference/react/Activity#activity), while older routes are removed from the DOM to prevent excessive growth.

### Effect on route segment config

When Cache Components is enabled, several route segment config options are no longer needed or supported. Here's what changes and how to migrate:

#### `dynamic = "force-dynamic"`

**Not needed.** All pages are dynamic by default with Cache Components enabled, so this configuration is unnecessary.

```tsx
// Before - No longer needed
export const dynamic = 'force-dynamic'

export default function Page() {
  return <div>...</div>
}
```

```tsx
// After - Just remove it, pages are dynamic by default
export default function Page() {
  return <div>...</div>
}
```

#### `dynamic = "force-static"`

**Replace with `use cache`.** You must add `use cache` to each Layout and Page for the associated route instead.

Note: `force-static` previously allowed the use of runtime APIs like `cookies()`, but this is no longer supported. If you add `use cache` and see an error related to runtime data, you must remove the use of runtime APIs.

```tsx
// Before
export const dynamic = 'force-static'

export default async function Page() {
  const data = await fetch('https://api.example.com/data')
  return <div>...</div>
}
```

```tsx
// After - Use 'use cache' instead
export default async function Page() {
  'use cache'
  const data = await fetch('https://api.example.com/data')
  return <div>...</div>
}
```

#### `revalidate`

**Replace with `cacheLife`.** Use the `cacheLife` function to define cache duration instead of the route segment config.

```tsx
// Before
export const revalidate = 3600 // 1 hour

export default async function Page() {
  return <div>...</div>
}
```

```tsx
// After - Use cacheLife
import { cacheLife } from 'next/cache'

export default async function Page() {
  'use cache'
  cacheLife('hours')
  return <div>...</div>
}
```

#### `fetchCache`

**Not needed.** With `use cache`, all data fetching within a cached scope is automatically cached, making `fetchCache` unnecessary.

```tsx
// Before
export const fetchCache = 'force-cache'
```

```tsx
// After - Use 'use cache' to control caching behavior
export default async function Page() {
  'use cache'
  // All fetches here are cached
  return <div>...</div>
}
```

#### `runtime = 'edge'`

**Not supported.** Cache Components requires Node.js runtime and will throw errors with [Edge Runtime](/docs/app/api-reference/edge.md).

## Before vs. after Cache Components

Understanding how Cache Components changes your mental model:

### Before Cache Components

* **Static by default**: Next.js tried to pre-render and cache as much as possible for you unless you opted out
* **Route-level controls**: Switches like `dynamic`, `revalidate`, `fetchCache` controlled caching for the whole page
* **Limits of `fetch`**: Using `fetch` alone was incomplete, as it didn't cover direct database clients or other server-side IO. A nested `fetch` switching to dynamic (e.g., `{ cache: 'no-store' }`) could unintentionally change the entire route behavior

### With Cache Components

* **Dynamic by default**: Everything is dynamic by default. You decide which parts to cache by adding [`use cache`](/docs/app/api-reference/directives/use-cache.md) where it helps
* **Fine-grained control**: File/component/function-level [`use cache`](/docs/app/api-reference/directives/use-cache.md) and [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md) control caching exactly where you need it
* **Streaming stays**: Use `<Suspense>` or a `loading.(js|tsx)` file to stream dynamic parts while the shell shows immediately
* **Beyond `fetch`**: Using the `use cache` directive caching can be applied to all server IO (database calls, APIs, computations), not just `fetch`. Nested `fetch` calls won't silently flip an entire route because behavior is governed by explicit cache boundaries and `Suspense`

## Examples

### Dynamic APIs

When accessing runtime APIs like `cookies()`, Next.js will only pre-render the fallback UI above this component.

In this example, we have no fallback defined, so Next.js shows an error instructing us to provide one. The `<User />` component needs to be wrapped in `Suspense` because it uses the `cookies` API:

```jsx filename="app/user.js" switcher
import { cookies } from 'next/headers'

export async function User() {
  const session = (await cookies()).get('session')?.value
  return '...'
}
```

```tsx filename="app/user.tsx" switcher
import { cookies } from 'next/headers'

export async function User() {
  const session = (await cookies()).get('session')?.value
  return '...'
}
```

Now we have a `Suspense` boundary around our User component we can pre-render the Page with a Skeleton UI and stream in the `<User />` UI when a specific user makes a request

```tsx filename="app/page.tsx" switcher
import { Suspense } from 'react'
import { User, AvatarSkeleton } from './user'

export default function Page() {
  return (
    <section>
      <h1>This will be pre-rendered</h1>
      <Suspense fallback={<AvatarSkeleton />}>
        <User />
      </Suspense>
    </section>
  )
}
```

```jsx filename="app/page.js" switcher
import { Suspense } from 'react'
import { User, AvatarSkeleton } from './user'

export default function Page() {
  return (
    <section>
      <h1>This will be pre-rendered</h1>
      <Suspense fallback={<AvatarSkeleton />}>
        <User />
      </Suspense>
    </section>
  )
}
```

### Passing dynamic props

Components that access runtime values like `cookies` or `searchParams` cannot be prerendered. To prerender more of a page's content, you can pass these props down and access their values lower in the tree. For example, if you are reading `searchParams` from a `<Page />` component, you can forward this value to another component as a prop:

```tsx filename="app/page.tsx" switcher
import { Table, TableSkeleton } from './table'
import { Suspense } from 'react'

export default function Page({
  searchParams,
}: {
  searchParams: Promise<{ sort: string }>
}) {
  return (
    <section>
      <h1>This will be pre-rendered</h1>
      <Suspense fallback={<TableSkeleton />}>
        <Table searchParams={searchParams.then((search) => search.sort)} />
      </Suspense>
    </section>
  )
}
```

```jsx filename="app/page.js" switcher
import { Table, TableSkeleton } from './table'
import { Suspense } from 'react'

export default function Page({ searchParams }) {
  return (
    <section>
      <h1>This will be pre-rendered</h1>
      <Suspense fallback={<TableSkeleton />}>
        <Table searchParams={searchParams.then((search) => search.sort)} />
      </Suspense>
    </section>
  )
}
```

Inside of the table component, accessing the value from `searchParams` will make the component dynamic while the rest of the page will be pre-rendered.

```tsx filename="app/table.tsx" switcher
export async function Table({ sortPromise }: { sortPromise: Promise<string> }) {
  const sort = (await sortPromise) === 'true'
  return '...'
}
```

```jsx filename="app/table.js" switcher
export async function Table({ sortPromise }) {
  const sort = (await sortPromise) === 'true'
  return '...'
}
```

## Route Handlers with Cache Components

`GET` Route Handlers follow the same model as normal UI routes in your application. They are dynamic by default, can be pre-rendered when deterministic, and you can `use cache` to include more dynamic data in the cached response.

Dynamic example, returns a different number for every request:

```tsx filename="app/api/random-number/route.ts"
export async function GET() {
  return Response.json({
    randomNumber: Math.random(),
  })
}
```

A handler that returns only static data will be pre-rendered at build time:

```tsx filename="app/api/project-info/route.ts"
export async function GET() {
  return Response.json({
    projectName: 'Next.js',
  })
}
```

If you had a route that returned fresh dynamic data on every request, say products from a database:

```tsx filename="app/api/products/route.ts"
export async function GET() {
  const products = await db.query('SELECT * FROM products')

  return Response.json(products)
}
```

To cache this and avoid hitting the database on every request, extract the dynamic work into a `use cache` function and set `cacheLife('hours')` so the database is queried at most once per hour:

```tsx filename="app/api/products/route.ts"
import { cacheLife } from 'next/cache'

export async function GET() {
  const products = await getProducts()

  return Response.json(products)
}

async function getProducts() {
  'use cache'
  cacheLife('hours')

  return await db.query('SELECT * FROM products')
}
```

> **Good to know**
>
> * `use cache` cannot be used directly inside a Route Handler body; extract to a helper.
> * Cached responses revalidate according to `cacheLife` when a new request arrives.
> * Using runtime APIs like [`cookies()`](/docs/app/api-reference/functions/cookies.md) or [`headers()`](/docs/app/api-reference/functions/headers.md), or calling [`connection()`](/docs/app/api-reference/functions/connection.md), always defers to request time (no pre-rendering).

## Frequently Asked Questions

### Does this replace Partial Prerendering (PPR)?

No. Cache Components **implements** PPR as a feature. The old experimental PPR flag has been removed but PPR is here to stay.

PPR provides the static shell and streaming infrastructure; `use cache` lets you include optimized dynamic output in that shell when beneficial.

### What should I cache first?

What you cache should be a function of what you want your UI loading states to be. If data doesn't depend on runtime data and you're okay with a cached value being served for multiple requests over a period of time, use `use cache` with `cacheLife` to describe that behavior.

For content management systems with update mechanisms, consider using tags with longer cache durations and rely on `revalidateTag` to mark static initial UI as ready for revalidation. This pattern allows you to serve fast, cached responses while still updating content when it actually changes, rather than expiring the cache preemptively.

### How do I update cached content quickly?

Use [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) to tag your cached data, then trigger [`updateTag`](/docs/app/api-reference/functions/updateTag.md) or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md).
## Next Steps

Learn more about the config option for Cache Components.

- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
  - Learn how to enable the cacheComponents flag in Next.js.
- [use cache](/docs/app/api-reference/directives/use-cache.md)
  - Learn how to use the use cache directive to cache data in your Next.js application.
- [cacheLife](/docs/app/api-reference/functions/cacheLife.md)
  - Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.
- [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
  - Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
  - API Reference for the revalidateTag function.
- [updateTag](/docs/app/api-reference/functions/updateTag.md)
  - API Reference for the updateTag function.


--------------------------------------------------------------------------------
title: "Fetching Data"
description: "Learn how to fetch data and stream content that depends on data."
source: "https://nextjs.org/docs/app/getting-started/fetching-data"
--------------------------------------------------------------------------------

# Fetching Data

This page will walk you through how you can fetch data in [Server and Client Components](/docs/app/getting-started/server-and-client-components.md), and how to [stream](#streaming) components that depend on data.

## Fetching data

### Server Components

You can fetch data in Server Components using any asynchronous I/O, such as:

1. The [`fetch` API](#with-the-fetch-api)
2. An [ORM or database](#with-an-orm-or-database)
3. Reading from the filesystem using Node.js APIs like `fs`

#### With the `fetch` API

To fetch data with the `fetch` API, turn your component into an asynchronous function, and await the `fetch` call. For example:

```tsx filename="app/blog/page.tsx" switcher
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/blog/page.js" switcher
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

> **Good to know:**
>
> * `fetch` responses are not cached by default. However, Next.js will [pre-render](/docs/app/guides/caching.md#static-rendering) the route and the output will be cached for improved performance. If you'd like to opt into [dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering), use the `{ cache: 'no-store' }` option. See the [`fetch` API Reference](/docs/app/api-reference/functions/fetch.md).
> * During development, you can log `fetch` calls for better visibility and debugging. See the [`logging` API reference](/docs/app/api-reference/config/next-config-js/logging.md).

#### With an ORM or database

Since Server Components are rendered on the server, you can safely make database queries using an ORM or database client. Turn your component into an asynchronous function, and await the call:

```tsx filename="app/blog/page.tsx" switcher
import { db, posts } from '@/lib/db'

export default async function Page() {
  const allPosts = await db.select().from(posts)
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/blog/page.js" switcher
import { db, posts } from '@/lib/db'

export default async function Page() {
  const allPosts = await db.select().from(posts)
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

### Client Components

There are two ways to fetch data in Client Components, using:

1. React's [`use` hook](https://react.dev/reference/react/use)
2. A community library like [SWR](https://swr.vercel.app/) or [React Query](https://tanstack.com/query/latest)

#### Streaming data with the `use` hook

You can use React's [`use` hook](https://react.dev/reference/react/use) to [stream](#streaming) data from the server to client. Start by fetching data in your Server component, and pass the promise to your Client Component as prop:

```tsx filename="app/blog/page.tsx" switcher
import Posts from '@/app/ui/posts'
import { Suspense } from 'react'

export default function Page() {
  // Don't await the data fetching function
  const posts = getPosts()

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Posts posts={posts} />
    </Suspense>
  )
}
```

```jsx filename="app/blog/page.js" switcher
import Posts from '@/app/ui/posts'
import { Suspense } from 'react'

export default function Page() {
  // Don't await the data fetching function
  const posts = getPosts()

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Posts posts={posts} />
    </Suspense>
  )
}
```

Then, in your Client Component, use the `use` hook to read the promise:

```tsx filename="app/ui/posts.tsx" switcher
'use client'
import { use } from 'react'

export default function Posts({
  posts,
}: {
  posts: Promise<{ id: string; title: string }[]>
}) {
  const allPosts = use(posts)

  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/ui/posts.js" switcher
'use client'
import { use } from 'react'

export default function Posts({ posts }) {
  const allPosts = use(posts)

  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

In the example above, the `<Posts>` component is wrapped in a [`<Suspense>` boundary](https://react.dev/reference/react/Suspense). This means the fallback will be shown while the promise is being resolved. Learn more about [streaming](#streaming).

#### Community libraries

You can use a community library like [SWR](https://swr.vercel.app/) or [React Query](https://tanstack.com/query/latest) to fetch data in Client Components. These libraries have their own semantics for caching, streaming, and other features. For example, with SWR:

```tsx filename="app/blog/page.tsx" switcher
'use client'
import useSWR from 'swr'

const fetcher = (url) => fetch(url).then((r) => r.json())

export default function BlogPage() {
  const { data, error, isLoading } = useSWR(
    'https://api.vercel.app/blog',
    fetcher
  )

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <ul>
      {data.map((post: { id: string; title: string }) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/blog/page.js" switcher
'use client'

import useSWR from 'swr'

const fetcher = (url) => fetch(url).then((r) => r.json())

export default function BlogPage() {
  const { data, error, isLoading } = useSWR(
    'https://api.vercel.app/blog',
    fetcher
  )

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <ul>
      {data.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

## Deduplicate requests and cache data

One way to deduplicate `fetch` requests is with [request memoization](/docs/app/guides/caching.md#request-memoization). With this mechanism, `fetch` calls using `GET` or `HEAD` with the same URL and options in a single render pass are combined into one request. This happens automatically, and you can [opt out](/docs/app/guides/caching.md#opting-out) by passing an Abort signal to `fetch`.

Request memoization is scoped to the lifetime of a request.

You can also deduplicate `fetch` requests by using Next.js’ [Data Cache](/docs/app/guides/caching.md#data-cache), for example by setting `cache: 'force-cache'` in your `fetch` options.

Data Cache allows sharing data across the current render pass and incoming requests.

If you are *not* using `fetch`, and instead using an ORM or database directly, you can wrap your data access with the [React `cache`](https://react.dev/reference/react/cache) function.

```tsx filename="app/lib/data.ts" switcher
import { cache } from 'react'
import { db, posts, eq } from '@/lib/db'

export const getPost = cache(async (id: string) => {
  const post = await db.query.posts.findFirst({
    where: eq(posts.id, parseInt(id)),
  })
})
```

```jsx filename="app/lib/data.js" switcher
import { cache } from 'react'
import { db, posts, eq } from '@/lib/db'
import { notFound } from 'next/navigation'

export const getPost = cache(async (id) => {
  const post = await db.query.posts.findFirst({
    where: eq(posts.id, parseInt(id)),
  })
})
```

## Streaming

> **Warning:** The content below assumes the [`cacheComponents` config option](/docs/app/api-reference/config/next-config-js/cacheComponents.md) is enabled in your application. The flag was introduced in Next.js 15 canary.

When you fetch data in Server Components, the data is fetched and rendered on the server for each request. If you have any slow data requests, the whole route will be blocked from rendering until all the data is fetched.

To improve the initial load time and user experience, you can use streaming to break up the page's HTML into smaller chunks and progressively send those chunks from the server to the client.

![How Server Rendering with Streaming Works](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/server-rendering-with-streaming.png)

There are two ways you can leverage streaming in your application:

1. Wrapping a page with a [`loading.js` file](#with-loadingjs)
2. Wrapping a component with [`<Suspense>`](#with-suspense)

### With `loading.js`

You can create a `loading.js` file in the same folder as your page to stream the **entire page** while the data is being fetched. For example, to stream `app/blog/page.js`, add the file inside the `app/blog` folder.

![Blog folder structure with loading.js file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-file.png)

```tsx filename="app/blog/loading.tsx" switcher
export default function Loading() {
  // Define the Loading UI here
  return <div>Loading...</div>
}
```

```jsx filename="app/blog/loading.js" switcher
export default function Loading() {
  // Define the Loading UI here
  return <div>Loading...</div>
}
```

On navigation, the user will immediately see the layout and a [loading state](#creating-meaningful-loading-states) while the page is being rendered. The new content will then be automatically swapped in once rendering is complete.

![Loading UI](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-ui.png)

Behind-the-scenes, `loading.js` will be nested inside `layout.js`, and will automatically wrap the `page.js` file and any children below in a `<Suspense>` boundary.

![loading.js overview](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-overview.png)

This approach works well for route segments (layouts and pages), but for more granular streaming, you can use `<Suspense>`.

### With `<Suspense>`

`<Suspense>` allows you to be more granular about what parts of the page to stream. For example, you can immediately show any page content that falls outside of the `<Suspense>` boundary, and stream in the list of blog posts inside the boundary.

```tsx filename="app/blog/page.tsx" switcher
import { Suspense } from 'react'
import BlogList from '@/components/BlogList'
import BlogListSkeleton from '@/components/BlogListSkeleton'

export default function BlogPage() {
  return (
    <div>
      {/* This content will be sent to the client immediately */}
      <header>
        <h1>Welcome to the Blog</h1>
        <p>Read the latest posts below.</p>
      </header>
      <main>
        {/* If there's any dynamic content inside this boundary, it will be streamed in */}
        <Suspense fallback={<BlogListSkeleton />}>
          <BlogList />
        </Suspense>
      </main>
    </div>
  )
}
```

```jsx filename="app/blog/page.js" switcher
import { Suspense } from 'react'
import BlogList from '@/components/BlogList'
import BlogListSkeleton from '@/components/BlogListSkeleton'

export default function BlogPage() {
  return (
    <div>
      {/* This content will be sent to the client immediately */}
      <header>
        <h1>Welcome to the Blog</h1>
        <p>Read the latest posts below.</p>
      </header>
      <main>
        {/* If there's any dynamic content inside this boundary, it will be streamed in */}
        <Suspense fallback={<BlogListSkeleton />}>
          <BlogList />
        </Suspense>
      </main>
    </div>
  )
}
```

### Creating meaningful loading states

An instant loading state is fallback UI that is shown immediately to the user after navigation. For the best user experience, we recommend designing loading states that are meaningful and help users understand the app is responding. For example, you can use skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc.

In development, you can preview and inspect the loading state of your components using the [React Devtools](https://react.dev/learn/react-developer-tools).

## Examples

### Sequential data fetching

Sequential data fetching happens when one request depends on data from another.

For example, `<Playlists>` can only fetch data after `<Artist>` completes because it needs the `artistID`:

```tsx filename="app/artist/[username]/page.tsx" switcher
export default async function Page({
  params,
}: {
  params: Promise<{ username: string }>
}) {
  const { username } = await params
  // Get artist information
  const artist = await getArtist(username)

  return (
    <>
      <h1>{artist.name}</h1>
      {/* Show fallback UI while the Playlists component is loading */}
      <Suspense fallback={<div>Loading...</div>}>
        {/* Pass the artist ID to the Playlists component */}
        <Playlists artistID={artist.id} />
      </Suspense>
    </>
  )
}

async function Playlists({ artistID }: { artistID: string }) {
  // Use the artist ID to fetch playlists
  const playlists = await getArtistPlaylists(artistID)

  return (
    <ul>
      {playlists.map((playlist) => (
        <li key={playlist.id}>{playlist.name}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/artist/[username]/page.js" switcher
export default async function Page({ params }) {
  const { username } = await params
  // Get artist information
  const artist = await getArtist(username)

  return (
    <>
      <h1>{artist.name}</h1>
      {/* Show fallback UI while the Playlists component is loading */}
      <Suspense fallback={<div>Loading...</div>}>
        {/* Pass the artist ID to the Playlists component */}
        <Playlists artistID={artist.id} />
      </Suspense>
    </>
  )
}

async function Playlists({ artistID }) {
  // Use the artist ID to fetch playlists
  const playlists = await getArtistPlaylists(artistID)

  return (
    <ul>
      {playlists.map((playlist) => (
        <li key={playlist.id}>{playlist.name}</li>
      ))}
    </ul>
  )
}
```

In this example, `<Suspense>` allows the playlists to stream in after the artist data loads. However, the page still waits for the artist data before displaying anything. To prevent this, you can wrap the entire page component in a `<Suspense>` boundary (for example, using a [`loading.js` file](#with-loadingjs)) to show a loading state immediately.

Ensure your data source can resolve the first request quickly, as it blocks everything else. If you can't optimize the request further, consider [caching](#deduplicate-requests-and-cache-data) the result if the data changes infrequently.

### Parallel data fetching

Parallel data fetching happens when data requests in a route are eagerly initiated and start at the same time.

By default, [layouts and pages](/docs/app/getting-started/layouts-and-pages.md) are rendered in parallel. So each segment starts fetching data as soon as possible.

However, within *any* component, multiple `async`/`await` requests can still be sequential if placed after the other. For example, `getAlbums` will be blocked until `getArtist` is resolved:

```tsx filename="app/artist/[username]/page.tsx" switcher
import { getArtist, getAlbums } from '@/app/lib/data'

export default async function Page({ params }) {
  // These requests will be sequential
  const { username } = await params
  const artist = await getArtist(username)
  const albums = await getAlbums(username)
  return <div>{artist.name}</div>
}
```

Start multiple requests by calling `fetch`, then await them with [`Promise.all`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all). Requests begin as soon as `fetch` is called.

```tsx filename="app/artist/[username]/page.tsx" highlight={3,8,23} switcher
import Albums from './albums'

async function getArtist(username: string) {
  const res = await fetch(`https://api.example.com/artist/${username}`)
  return res.json()
}

async function getAlbums(username: string) {
  const res = await fetch(`https://api.example.com/artist/${username}/albums`)
  return res.json()
}

export default async function Page({
  params,
}: {
  params: Promise<{ username: string }>
}) {
  const { username } = await params

  // Initiate requests
  const artistData = getArtist(username)
  const albumsData = getAlbums(username)

  const [artist, albums] = await Promise.all([artistData, albumsData])

  return (
    <>
      <h1>{artist.name}</h1>
      <Albums list={albums} />
    </>
  )
}
```

```jsx filename="app/artist/[username]/page.js" highlight={3,8,19} switcher
import Albums from './albums'

async function getArtist(username) {
  const res = await fetch(`https://api.example.com/artist/${username}`)
  return res.json()
}

async function getAlbums(username) {
  const res = await fetch(`https://api.example.com/artist/${username}/albums`)
  return res.json()
}

export default async function Page({ params }) {
  const { username } = await params

  // Initiate requests
  const artistData = getArtist(username)
  const albumsData = getAlbums(username)

  const [artist, albums] = await Promise.all([artistData, albumsData])

  return (
    <>
      <h1>{artist.name}</h1>
      <Albums list={albums} />
    </>
  )
}
```

> **Good to know:** If one request fails when using `Promise.all`, the entire operation will fail. To handle this, you can use the [`Promise.allSettled`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled) method instead.

### Preloading data

You can preload data by creating an utility function that you eagerly call above blocking requests. `<Item>` conditionally renders based on the `checkIsAvailable()` function.

You can call `preload()` before `checkIsAvailable()` to eagerly initiate `<Item/>` data dependencies. By the time `<Item/>` is rendered, its data has already been fetched.

```tsx filename="app/item/[id]/page.tsx" switcher
import { getItem, checkIsAvailable } from '@/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  // starting loading item data
  preload(id)
  // perform another asynchronous task
  const isAvailable = await checkIsAvailable()

  return isAvailable ? <Item id={id} /> : null
}

const preload = (id: string) => {
  // void evaluates the given expression and returns undefined
  // https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/void
  void getItem(id)
}

export async function Item({ id }: { id: string }) {
  const result = await getItem(id)
  // ...
}
```

```jsx filename="app/item/[id]/page.js" switcher
import { getItem, checkIsAvailable } from '@/lib/data'

export default async function Page({ params }) {
  const { id } = await params
  // starting loading item data
  preload(id)
  // perform another asynchronous task
  const isAvailable = await checkIsAvailable()

  return isAvailable ? <Item id={id} /> : null
}

const preload = (id) => {
  // void evaluates the given expression and returns undefined
  // https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/void
  void getItem(id)
}

export async function Item({ id }) {
  const result = await getItem(id)
  // ...
```

Additionally, you can use React's [`cache` function](https://react.dev/reference/react/cache) and the [`server-only` package](https://www.npmjs.com/package/server-only) to create a reusable utility function. This approach allows you to cache the data fetching function and ensure that it's only executed on the server.

```ts filename="utils/get-item.ts" switcher
import { cache } from 'react'
import 'server-only'
import { getItem } from '@/lib/data'

export const preload = (id: string) => {
  void getItem(id)
}

export const getItem = cache(async (id: string) => {
  // ...
})
```

```js filename="utils/get-item.js" switcher
import { cache } from 'react'
import 'server-only'
import { getItem } from '@/lib/data'

export const preload = (id) => {
  void getItem(id)
}

export const getItem = cache(async (id) => {
  // ...
})
```
## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

- [Data Security](/docs/app/guides/data-security.md)
  - Learn the built-in data security features in Next.js and learn best practices for protecting your application's data.
- [fetch](/docs/app/api-reference/functions/fetch.md)
  - API reference for the extended fetch function.
- [loading.js](/docs/app/api-reference/file-conventions/loading.md)
  - API reference for the loading.js file.
- [logging](/docs/app/api-reference/config/next-config-js/logging.md)
  - Configure how data fetches are logged to the console when running Next.js in development mode.
- [taint](/docs/app/api-reference/config/next-config-js/taint.md)
  - Enable tainting Objects and Values.


--------------------------------------------------------------------------------
title: "Updating Data"
description: "Learn how to mutate data using Server Functions."
source: "https://nextjs.org/docs/app/getting-started/updating-data"
--------------------------------------------------------------------------------

# Updating Data

You can update data in Next.js using React's [Server Functions](https://react.dev/reference/rsc/server-functions). This page will go through how you can [create](#creating-server-functions) and [invoke](#invoking-server-functions) Server Functions.

## What are Server Functions?

A **Server Function** is an asynchronous function that runs on the server. They can be called from the client through a network request, which is why they must be asynchronous.

In an `action` or mutation context, they are also called **Server Actions**.

By convention, a Server Action is an async function used with [`startTransition`](https://react.dev/reference/react/startTransition). This happens automatically when the function is:

* Passed to a `<form>` using the `action` prop.
* Passed to a `<button>` using the `formAction` prop.

In Next.js, Server Actions integrate with the framework's [caching](/docs/app/guides/caching.md) architecture. When an action is invoked, Next.js can return both the updated UI and new data in a single server roundtrip.

Behind the scenes, actions use the `POST` method, and only this HTTP method can invoke them.

## Creating Server Functions

A Server Function can be defined by using the [`use server`](https://react.dev/reference/rsc/use-server) directive. You can place the directive at the top of an **asynchronous** function to mark the function as a Server Function, or at the top of a separate file to mark all exports of that file.

```ts filename="app/lib/actions.ts" switcher
export async function createPost(formData: FormData) {
  'use server'
  const title = formData.get('title')
  const content = formData.get('content')

  // Update data
  // Revalidate cache
}

export async function deletePost(formData: FormData) {
  'use server'
  const id = formData.get('id')

  // Update data
  // Revalidate cache
}
```

```js filename="app/lib/actions.js" switcher
export async function createPost(formData) {
  'use server'
  const title = formData.get('title')
  const content = formData.get('content')

  // Update data
  // Revalidate cache
}

export async function deletePost(formData) {
  'use server'
  const id = formData.get('id')

  // Update data
  // Revalidate cache
}
```

### Server Components

Server Functions can be inlined in Server Components by adding the `"use server"` directive to the top of the function body:

```tsx filename="app/page.tsx" switcher
export default function Page() {
  // Server Action
  async function createPost(formData: FormData) {
    'use server'
    // ...
  }

  return <></>
}
```

```jsx filename="app/page.js" switcher
export default function Page() {
  // Server Action
  async function createPost(formData: FormData) {
    'use server'
    // ...
  }

  return <></>
}
```

> **Good to know:** Server Components support progressive enhancement by default, meaning forms that call Server Actions will be submitted even if JavaScript hasn't loaded yet or is disabled.

### Client Components

It's not possible to define Server Functions in Client Components. However, you can invoke them in Client Components by importing them from a file that has the `"use server"` directive at the top of it:

```ts filename="app/actions.ts" switcher
'use server'

export async function createPost() {}
```

```js filename="app/actions.js" switcher
'use server'

export async function createPost() {}
```

```tsx filename="app/ui/button.tsx" switcher
'use client'

import { createPost } from '@/app/actions'

export function Button() {
  return <button formAction={createPost}>Create</button>
}
```

```jsx filename="app/ui/button.js" switcher
'use client'

import { createPost } from '@/app/actions'

export function Button() {
  return <button formAction={createPost}>Create</button>
}
```

> **Good to know:** In Client Components, forms invoking Server Actions will queue submissions if JavaScript isn't loaded yet, and will be prioritized for hydration. After hydration, the browser does not refresh on form submission.

### Passing actions as props

You can also pass an action to a Client Component as a prop:

```jsx
<ClientComponent updateItemAction={updateItem} />
```

```tsx filename="app/client-component.tsx" switcher
'use client'

export default function ClientComponent({
  updateItemAction,
}: {
  updateItemAction: (formData: FormData) => void
}) {
  return <form action={updateItemAction}>{/* ... */}</form>
}
```

```jsx filename="app/client-component.js" switcher
'use client'

export default function ClientComponent({ updateItemAction }) {
  return <form action={updateItemAction}>{/* ... */}</form>
}
```

## Invoking Server Functions

There are two main ways you can invoke a Server Function:

1. [Forms](#forms) in Server and Client Components
2. [Event Handlers](#event-handlers) and [useEffect](#useeffect) in Client Components

> **Good to know:** Server Functions are designed for server-side mutations. The client currently dispatches and awaits them one at a time. This is an implementation detail and may change. If you need parallel data fetching, use [data fetching](/docs/app/getting-started/fetching-data.md#server-components) in Server Components, or perform parallel work inside a single Server Function or [Route Handler](/docs/app/guides/backend-for-frontend.md#manipulating-data).

### Forms

React extends the HTML [`<form>`](https://react.dev/reference/react-dom/components/form) element to allow a Server Function to be invoked with the HTML `action` prop.

When invoked in a form, the function automatically receives the [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData/FormData) object. You can extract the data using the native [`FormData` methods](https://developer.mozilla.org/en-US/docs/Web/API/FormData#instance_methods):

```tsx filename="app/ui/form.tsx" switcher
import { createPost } from '@/app/actions'

export function Form() {
  return (
    <form action={createPost}>
      <input type="text" name="title" />
      <input type="text" name="content" />
      <button type="submit">Create</button>
    </form>
  )
}
```

```jsx filename="app/ui/form.js" switcher
import { createPost } from '@/app/actions'

export function Form() {
  return (
    <form action={createPost}>
      <input type="text" name="title" />
      <input type="text" name="content" />
      <button type="submit">Create</button>
    </form>
  )
}
```

```ts filename="app/actions.ts" switcher
'use server'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Update data
  // Revalidate cache
}
```

```js filename="app/actions.js" switcher
'use server'

export async function createPost(formData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Update data
  // Revalidate cache
}
```

### Event Handlers

You can invoke a Server Function in a Client Component by using event handlers such as `onClick`.

```tsx filename="app/like-button.tsx" switcher
'use client'

import { incrementLike } from './actions'
import { useState } from 'react'

export default function LikeButton({ initialLikes }: { initialLikes: number }) {
  const [likes, setLikes] = useState(initialLikes)

  return (
    <>
      <p>Total Likes: {likes}</p>
      <button
        onClick={async () => {
          const updatedLikes = await incrementLike()
          setLikes(updatedLikes)
        }}
      >
        Like
      </button>
    </>
  )
}
```

```jsx filename="app/like-button.js" switcher
'use client'

import { incrementLike } from './actions'
import { useState } from 'react'

export default function LikeButton({ initialLikes }) {
  const [likes, setLikes] = useState(initialLikes)

  return (
    <>
      <p>Total Likes: {likes}</p>
      <button
        onClick={async () => {
          const updatedLikes = await incrementLike()
          setLikes(updatedLikes)
        }}
      >
        Like
      </button>
    </>
  )
}
```

## Examples

### Showing a pending state

While executing a Server Function, you can show a loading indicator with React's [`useActionState`](https://react.dev/reference/react/useActionState) hook. This hook returns a `pending` boolean:

```tsx filename="app/ui/button.tsx" switcher
'use client'

import { useActionState, startTransition } from 'react'
import { createPost } from '@/app/actions'
import { LoadingSpinner } from '@/app/ui/loading-spinner'

export function Button() {
  const [state, action, pending] = useActionState(createPost, false)

  return (
    <button onClick={() => startTransition(action)}>
      {pending ? <LoadingSpinner /> : 'Create Post'}
    </button>
  )
}
```

```jsx filename="app/ui/button.js" switcher
'use client'

import { useActionState, startTransition } from 'react'
import { createPost } from '@/app/actions'
import { LoadingSpinner } from '@/app/ui/loading-spinner'

export function Button() {
  const [state, action, pending] = useActionState(createPost, false)

  return (
    <button onClick={() => startTransition(action)}>
      {pending ? <LoadingSpinner /> : 'Create Post'}
    </button>
  )
}
```

### Refreshing

After a mutation, you may want to refresh the current page to show the latest data. You can do this by calling [`refresh`](/docs/app/api-reference/functions/refresh.md) from `next/cache` in a Server Action:

```ts filename="app/lib/actions.ts" switcher
'use server'

import { refresh } from 'next/cache'

export async function updatePost(formData: FormData) {
  // Update data
  // ...

  refresh()
}
```

```js filename="app/lib/actions.js" switcher
'use server'

import { refresh } from 'next/cache'

export async function updatePost(formData) {
  // Update data
  // ...

  refresh()
}
```

This refreshes the client router, ensuring the UI reflects the latest state. The `refresh()` function does not revalidate tagged data. To revalidate tagged data, use [`updateTag`](/docs/app/api-reference/functions/updateTag.md) or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) instead.

### Revalidating

After performing an update, you can revalidate the Next.js cache and show the updated data by calling [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md) or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) within the Server Function:

```ts filename="app/lib/actions.ts" switcher
import { revalidatePath } from 'next/cache'

export async function createPost(formData: FormData) {
  'use server'
  // Update data
  // ...

  revalidatePath('/posts')
}
```

```js filename="app/actions.js" switcher
import { revalidatePath } from 'next/cache'

export async function createPost(formData) {
  'use server'
  // Update data
  // ...
  revalidatePath('/posts')
}
```

### Redirecting

You may want to redirect the user to a different page after performing an update. You can do this by calling [`redirect`](/docs/app/api-reference/functions/redirect.md) within the Server Function.

```ts filename="app/lib/actions.ts" switcher
'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  // Update data
  // ...

  revalidatePath('/posts')
  redirect('/posts')
}
```

```js filename="app/actions.js" switcher
'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData) {
  // Update data
  // ...

  revalidatePath('/posts')
  redirect('/posts')
}
```

Calling `redirect` [throws](/docs/app/api-reference/functions/redirect.md#behavior) a framework handled control-flow exception. Any code after it won't execute. If you need fresh data, call [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md) or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) beforehand.

### Cookies

You can `get`, `set`, and `delete` cookies inside a Server Action using the [`cookies`](/docs/app/api-reference/functions/cookies.md) API.

When you [set or delete](/docs/app/api-reference/functions/cookies.md#understanding-cookie-behavior-in-server-actions) a cookie in a Server Action, Next.js re-renders the current page and its layouts on the server so the **UI reflects the new cookie value**.

> **Good to know**: The server update applies to the current React tree, re-rendering, mounting, or unmounting components, as needed. Client state is preserved for re-rendered components, and effects re-run if their dependencies changed.

```ts filename="app/actions.ts" switcher
'use server'

import { cookies } from 'next/headers'

export async function exampleAction() {
  const cookieStore = await cookies()

  // Get cookie
  cookieStore.get('name')?.value

  // Set cookie
  cookieStore.set('name', 'Delba')

  // Delete cookie
  cookieStore.delete('name')
}
```

```js filename="app/actions.js" switcher
'use server'

import { cookies } from 'next/headers'

export async function exampleAction() {
  // Get cookie
  const cookieStore = await cookies()

  // Get cookie
  cookieStore.get('name')?.value

  // Set cookie
  cookieStore.set('name', 'Delba')

  // Delete cookie
  cookieStore.delete('name')
}
```

### useEffect

You can use the React [`useEffect`](https://react.dev/reference/react/useEffect) hook to invoke a Server Action when the component mounts or a dependency changes. This is useful for mutations that depend on global events or need to be triggered automatically. For example, `onKeyDown` for app shortcuts, an intersection observer hook for infinite scrolling, or when the component mounts to update a view count:

```tsx filename="app/view-count.tsx" switcher
'use client'

import { incrementViews } from './actions'
import { useState, useEffect, useTransition } from 'react'

export default function ViewCount({ initialViews }: { initialViews: number }) {
  const [views, setViews] = useState(initialViews)
  const [isPending, startTransition] = useTransition()

  useEffect(() => {
    startTransition(async () => {
      const updatedViews = await incrementViews()
      setViews(updatedViews)
    })
  }, [])

  // You can use `isPending` to give users feedback
  return <p>Total Views: {views}</p>
}
```

```jsx filename="app/view-count.js" switcher
'use client'

import { incrementViews } from './actions'
import { useState, useEffect, useTransition } from 'react'

export default function ViewCount({ initialViews }) {
  const [views, setViews] = useState(initialViews)
  const [isPending, startTransition] = useTransition()

  useEffect(() => {
    startTransition(async () => {
      const updatedViews = await incrementViews()
      setViews(updatedViews)
    })
  }, [])

  // You can use `isPending` to give users feedback
  return <p>Total Views: {views}</p>
}
```
## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

- [revalidatePath](/docs/app/api-reference/functions/revalidatePath.md)
  - API Reference for the revalidatePath function.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
  - API Reference for the revalidateTag function.
- [redirect](/docs/app/api-reference/functions/redirect.md)
  - API Reference for the redirect function.


--------------------------------------------------------------------------------
title: "Caching and Revalidating"
description: "Learn how to cache and revalidate data in your application."
source: "https://nextjs.org/docs/app/getting-started/caching-and-revalidating"
--------------------------------------------------------------------------------

# Caching and Revalidating

Caching is a technique for storing the result of data fetching and other computations so that future requests for the same data can be served faster, without doing the work again. While revalidation allows you to update cache entries without having to rebuild your entire application.

Next.js provides a few APIs to handle caching and revalidation. This guide will walk you through when and how to use them.

* [`fetch`](#fetch)
* [`cacheTag`](#cachetag)
* [`revalidateTag`](#revalidatetag)
* [`updateTag`](#updatetag)
* [`revalidatePath`](#revalidatepath)
* [`unstable_cache`](#unstable_cache) (Legacy)

## `fetch`

By default, [`fetch`](/docs/app/api-reference/functions/fetch.md) requests are not cached. You can cache individual requests by setting the `cache` option to `'force-cache'`.

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  const data = await fetch('https://...', { cache: 'force-cache' })
}
```

```jsx filename="app/page.jsx" switcher
export default async function Page() {
  const data = await fetch('https://...', { cache: 'force-cache' })
}
```

> **Good to know**: Although `fetch` requests are not cached by default, Next.js will [pre-render](/docs/app/guides/caching.md#static-rendering) routes that have `fetch` requests and cache the HTML. If you want to guarantee a route is [dynamic](/docs/app/guides/caching.md#dynamic-rendering), use the [`connection` API](/docs/app/api-reference/functions/connection.md).

To revalidate the data returned by a `fetch` request, you can use the `next.revalidate` option.

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  const data = await fetch('https://...', { next: { revalidate: 3600 } })
}
```

```jsx filename="app/page.jsx" switcher
export default async function Page() {
  const data = await fetch('https://...', { next: { revalidate: 3600 } })
}
```

This will revalidate the data after a specified amount of seconds.

You can also tag `fetch` requests to enable on-demand cache invalidation:

```tsx filename="app/lib/data.ts" switcher
export async function getUserById(id: string) {
  const data = await fetch(`https://...`, {
    next: {
      tags: ['user'],
    },
  })
}
```

```jsx filename="app/lib/data.js" switcher
export async function getUserById(id) {
  const data = await fetch(`https://...`, {
    next: {
      tags: ['user'],
    },
  })
}
```

See the [`fetch` API reference](/docs/app/api-reference/functions/fetch.md) to learn more.

## `cacheTag`

[`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) allows you to tag cached data in [Cache Components](/docs/app/getting-started/cache-components.md) so it can be revalidated on-demand. Previously, cache tagging was limited to `fetch` requests, and caching other work required the experimental `unstable_cache` API.

With Cache Components, you can use the [`use cache`](/docs/app/api-reference/directives/use-cache.md) directive to cache any computation, and `cacheTag` to tag it. This works with database queries, file system operations, and other server-side work.

```tsx filename="app/lib/data.ts" switcher
import { cacheTag } from 'next/cache'

export async function getProducts() {
  'use cache'
  cacheTag('products')

  const products = await db.query('SELECT * FROM products')
  return products
}
```

```jsx filename="app/lib/data.js" switcher
import { cacheTag } from 'next/cache'

export async function getProducts() {
  'use cache'
  cacheTag('products')

  const products = await db.query('SELECT * FROM products')
  return products
}
```

Once tagged, you can use [`revalidateTag`](#revalidatetag) or [`updateTag`](#updatetag) to invalidate the cache entry for products.

> **Good to know**: `cacheTag` is used with [Cache Components](/docs/app/getting-started/cache-components.md) and the [`use cache`](/docs/app/api-reference/directives/use-cache.md) directive. It expands the caching and revalidation story beyond `fetch`.

See the [`cacheTag` API reference](/docs/app/api-reference/functions/cacheTag.md) to learn more.

## `revalidateTag`

`revalidateTag` is used to revalidate cache entries based on a tag and following an event. The function now supports two behaviors:

* **With `profile="max"`**: Uses stale-while-revalidate semantics, serving stale content while fetching fresh content in the background
* **Without the second argument**: Legacy behavior that immediately expires the cache (deprecated)

After tagging your cached data, using [`fetch`](#fetch) with `next.tags`, or the [`cacheTag`](#cachetag) function, you may call `revalidateTag` in a [Route Handler](/docs/app/api-reference/file-conventions/route.md) or Server Action:

```tsx filename="app/lib/actions.ts" highlight={1,5} switcher
import { revalidateTag } from 'next/cache'

export async function updateUser(id: string) {
  // Mutate data
  revalidateTag('user', 'max') // Recommended: Uses stale-while-revalidate
}
```

```jsx filename="app/lib/actions.js" highlight={1,5} switcher
import { revalidateTag } from 'next/cache'

export async function updateUser(id) {
  // Mutate data
  revalidateTag('user', 'max') // Recommended: Uses stale-while-revalidate
}
```

You can reuse the same tag in multiple functions to revalidate them all at once.

See the [`revalidateTag` API reference](/docs/app/api-reference/functions/revalidateTag.md) to learn more.

## `updateTag`

`updateTag` is specifically designed for Server Actions to immediately expire cached data for read-your-own-writes scenarios. Unlike `revalidateTag`, it can only be used within Server Actions and immediately expires the cache entry.

```tsx filename="app/lib/actions.ts" highlight={1,6} switcher
import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  // Create post in database
  const post = await db.post.create({
    data: {
      title: formData.get('title'),
      content: formData.get('content'),
    },
  })

  // Immediately expire cache so the new post is visible
  updateTag('posts')
  updateTag(`post-${post.id}`)

  redirect(`/posts/${post.id}`)
}
```

```jsx filename="app/lib/actions.js" highlight={1,6} switcher
import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData) {
  // Create post in database
  const post = await db.post.create({
    data: {
      title: formData.get('title'),
      content: formData.get('content'),
    },
  })

  // Immediately expire cache so the new post is visible
  updateTag('posts')
  updateTag(`post-${post.id}`)

  redirect(`/posts/${post.id}`)
}
```

The key differences between `revalidateTag` and `updateTag`:

* **`updateTag`**: Only in Server Actions, immediately expires cache, for read-your-own-writes
* **`revalidateTag`**: In Server Actions and Route Handlers, supports stale-while-revalidate with `profile="max"`

See the [`updateTag` API reference](/docs/app/api-reference/functions/updateTag.md) to learn more.

## `revalidatePath`

`revalidatePath` is used to revalidate a route and following an event. To use it, call it in a [Route Handler](/docs/app/api-reference/file-conventions/route.md) or Server Action:

```tsx filename="app/lib/actions.ts" highlight={1} switcher
import { revalidatePath } from 'next/cache'

export async function updateUser(id: string) {
  // Mutate data
  revalidatePath('/profile')
```

```jsx filename="app/lib/actions.js" highlight={1} switcher
import { revalidatePath } from 'next/cache'

export async function updateUser(id) {
  // Mutate data
  revalidatePath('/profile')
```

See the [`revalidatePath` API reference](/docs/app/api-reference/functions/revalidatePath.md) to learn more.

## `unstable_cache`

> **Good to know**: `unstable_cache` is an experimental API. We recommend opting into [Cache Components](/docs/app/getting-started/cache-components.md) and replacing `unstable_cache` with the [`use cache`](/docs/app/api-reference/directives/use-cache.md) directive. See the [Cache Components documentation](/docs/app/getting-started/cache-components.md) for more details.

`unstable_cache` allows you to cache the result of database queries and other async functions. To use it, wrap `unstable_cache` around the function. For example:

```ts filename="app/lib/data.ts" switcher
import { db } from '@/lib/db'
export async function getUserById(id: string) {
  return db
    .select()
    .from(users)
    .where(eq(users.id, id))
    .then((res) => res[0])
}
```

```jsx filename="app/lib/data.js" switcher
import { db } from '@/lib/db'

export async function getUserById(id) {
  return db
    .select()
    .from(users)
    .where(eq(users.id, id))
    .then((res) => res[0])
}
```

```tsx filename="app/page.tsx" highlight={2,11,13} switcher
import { unstable_cache } from 'next/cache'
import { getUserById } from '@/app/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ userId: string }>
}) {
  const { userId } = await params

  const getCachedUser = unstable_cache(
    async () => {
      return getUserById(userId)
    },
    [userId] // add the user ID to the cache key
  )
}
```

```jsx filename="app/page.js" highlight={2,7,9} switcher
import { unstable_cache } from 'next/cache'
import { getUserById } from '@/app/lib/data'

export default async function Page({ params }) {
  const { userId } = await params

  const getCachedUser = unstable_cache(
    async () => {
      return getUserById(userId)
    },
    [userId] // add the user ID to the cache key
  )
}
```

The function accepts a third optional object to define how the cache should be revalidated. It accepts:

* `tags`: an array of tags used by Next.js to revalidate the cache.
* `revalidate`: the number of seconds after cache should be revalidated.

```tsx filename="app/page.tsx" highlight={6-9} switcher
const getCachedUser = unstable_cache(
  async () => {
    return getUserById(userId)
  },
  [userId],
  {
    tags: ['user'],
    revalidate: 3600,
  }
)
```

```jsx filename="app/page.js" highlight={6-9} switcher
const getCachedUser = unstable_cache(
  async () => {
    return getUserById(userId)
  },
  [userId],
  {
    tags: ['user'],
    revalidate: 3600,
  }
)
```

See the [`unstable_cache` API reference](/docs/app/api-reference/functions/unstable_cache.md) to learn more.
## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

- [fetch](/docs/app/api-reference/functions/fetch.md)
  - API reference for the extended fetch function.
- [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
  - Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
  - API Reference for the revalidateTag function.
- [updateTag](/docs/app/api-reference/functions/updateTag.md)
  - API Reference for the updateTag function.
- [revalidatePath](/docs/app/api-reference/functions/revalidatePath.md)
  - API Reference for the revalidatePath function.
- [unstable_cache](/docs/app/api-reference/functions/unstable_cache.md)
  - API Reference for the unstable_cache function.


--------------------------------------------------------------------------------
title: "Error Handling"
description: "Learn how to display expected errors and handle uncaught exceptions."
source: "https://nextjs.org/docs/app/getting-started/error-handling"
--------------------------------------------------------------------------------

# Error Handling

Errors can be divided into two categories: [expected errors](#handling-expected-errors) and [uncaught exceptions](#handling-uncaught-exceptions). This page will walk you through how you can handle these errors in your Next.js application.

## Handling expected errors

Expected errors are those that can occur during the normal operation of the application, such as those from [server-side form validation](/docs/app/guides/forms.md) or failed requests. These errors should be handled explicitly and returned to the client.

### Server Functions

You can use the [`useActionState`](https://react.dev/reference/react/useActionState) hook to handle expected errors in [Server Functions](https://react.dev/reference/rsc/server-functions).

For these errors, avoid using `try`/`catch` blocks and throw errors. Instead, model expected errors as return values.

```ts filename="app/actions.ts" switcher
'use server'

export async function createPost(prevState: any, formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  const res = await fetch('https://api.vercel.app/posts', {
    method: 'POST',
    body: { title, content },
  })
  const json = await res.json()

  if (!res.ok) {
    return { message: 'Failed to create post' }
  }
}
```

```js filename="app/actions.js" switcher
'use server'

export async function createPost(prevState, formData) {
  const title = formData.get('title')
  const content = formData.get('content')

  const res = await fetch('https://api.vercel.app/posts', {
    method: 'POST',
    body: { title, content },
  })
  const json = await res.json()

  if (!res.ok) {
    return { message: 'Failed to create post' }
  }
}
```

You can pass your action to the `useActionState` hook and use the returned `state` to display an error message.

```tsx filename="app/ui/form.tsx" highlight={11,19} switcher
'use client'

import { useActionState } from 'react'
import { createPost } from '@/app/actions'

const initialState = {
  message: '',
}

export function Form() {
  const [state, formAction, pending] = useActionState(createPost, initialState)

  return (
    <form action={formAction}>
      <label htmlFor="title">Title</label>
      <input type="text" id="title" name="title" required />
      <label htmlFor="content">Content</label>
      <textarea id="content" name="content" required />
      {state?.message && <p aria-live="polite">{state.message}</p>}
      <button disabled={pending}>Create Post</button>
    </form>
  )
}
```

```jsx filename="app/ui/form.js" highlight={11,19} switcher
'use client'

import { useActionState } from 'react'
import { createPost } from '@/app/actions'

const initialState = {
  message: '',
}

export function Form() {
  const [state, formAction, pending] = useActionState(createPost, initialState)

  return (
    <form action={formAction}>
      <label htmlFor="title">Title</label>
      <input type="text" id="title" name="title" required />
      <label htmlFor="content">Content</label>
      <textarea id="content" name="content" required />
      {state?.message && <p aria-live="polite">{state.message}</p>}
      <button disabled={pending}>Create Post</button>
    </form>
  )
}
```

### Server Components

When fetching data inside of a Server Component, you can use the response to conditionally render an error message or [`redirect`](/docs/app/api-reference/functions/redirect.md).

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!res.ok) {
    return 'There was an error.'
  }

  return '...'
}
```

```jsx filename="app/page.js" switcher
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!res.ok) {
    return 'There was an error.'
  }

  return '...'
}
```

### Not found

You can call the [`notFound`](/docs/app/api-reference/functions/not-found.md) function within a route segment and use the [`not-found.js`](/docs/app/api-reference/file-conventions/not-found.md) file to show a 404 UI.

```tsx filename="app/blog/[slug]/page.tsx" switcher
import { getPostBySlug } from '@/lib/posts'

export default async function Page({ params }: { params: { slug: string } }) {
  const { slug } = await params
  const post = getPostBySlug(slug)

  if (!post) {
    notFound()
  }

  return <div>{post.title}</div>
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
import { getPostBySlug } from '@/lib/posts'

export default async function Page({ params }) {
  const { slug } = await params
  const post = getPostBySlug(slug)

  if (!post) {
    notFound()
  }

  return <div>{post.title}</div>
}
```

```tsx filename="app/blog/[slug]/not-found.tsx" switcher
export default function NotFound() {
  return <div>404 - Page Not Found</div>
}
```

```jsx filename="app/blog/[slug]/not-found.js" switcher
export default function NotFound() {
  return <div>404 - Page Not Found</div>
}
```

## Handling uncaught exceptions

Uncaught exceptions are unexpected errors that indicate bugs or issues that should not occur during the normal flow of your application. These should be handled by throwing errors, which will then be caught by error boundaries.

### Nested error boundaries

Next.js uses error boundaries to handle uncaught exceptions. Error boundaries catch errors in their child components and display a fallback UI instead of the component tree that crashed.

Create an error boundary by adding an [`error.js`](/docs/app/api-reference/file-conventions/error.md) file inside a route segment and exporting a React component:

```tsx filename="app/dashboard/error.tsx" switcher
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```

```jsx filename="app/dashboard/error.js" switcher
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({ error, reset }) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```

Errors will bubble up to the nearest parent error boundary. This allows for granular error handling by placing `error.tsx` files at different levels in the [route hierarchy](/docs/app/getting-started/project-structure.md#component-hierarchy).

![Nested Error Component Hierarchy](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/nested-error-component-hierarchy.png)

Error boundaries don’t catch errors inside event handlers. They’re designed to catch errors [during rendering](https://react.dev/reference/react/Component#static-getderivedstatefromerror) to show a **fallback UI** instead of crashing the whole app.

In general, errors in event handlers or async code aren’t handled by error boundaries because they run after rendering.

To handle these cases, catch the error manually and store it using `useState` or `useReducer`, then update the UI to inform the user.

```tsx
'use client'

import { useState } from 'react'

export function Button() {
  const [error, setError] = useState(null)

  const handleClick = () => {
    try {
      // do some work that might fail
      throw new Error('Exception')
    } catch (reason) {
      setError(reason)
    }
  }

  if (error) {
    /* render fallback UI */
  }

  return (
    <button type="button" onClick={handleClick}>
      Click me
    </button>
  )
}
```

Note that unhandled errors inside `startTransition` from `useTransition`, will bubble up to the nearest error boundary.

```tsx
'use client'

import { useTransition } from 'react'

export function Button() {
  const [pending, startTransition] = useTransition()

  const handleClick = () =>
    startTransition(() => {
      throw new Error('Exception')
    })

  return (
    <button type="button" onClick={handleClick}>
      Click me
    </button>
  )
}
```

### Global errors

While less common, you can handle errors in the root layout using the [`global-error.js`](/docs/app/api-reference/file-conventions/error.md#global-error) file, located in the root app directory, even when leveraging [internationalization](/docs/app/guides/internationalization.md). Global error UI must define its own `<html>` and `<body>` tags, since it is replacing the root layout or template when active.

```tsx filename="app/global-error.tsx" switcher
'use client' // Error boundaries must be Client Components

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}
```

```jsx filename="app/global-error.js" switcher
'use client' // Error boundaries must be Client Components

export default function GlobalError({ error, reset }) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}
```
## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

- [redirect](/docs/app/api-reference/functions/redirect.md)
  - API Reference for the redirect function.
- [error.js](/docs/app/api-reference/file-conventions/error.md)
  - API reference for the error.js special file.
- [notFound](/docs/app/api-reference/functions/not-found.md)
  - API Reference for the notFound function.
- [not-found.js](/docs/app/api-reference/file-conventions/not-found.md)
  - API reference for the not-found.js file.


--------------------------------------------------------------------------------
title: "CSS"
description: "Learn about the different ways to add CSS to your application, including Tailwind CSS, CSS Modules, Global CSS, and more."
source: "https://nextjs.org/docs/app/getting-started/css"
--------------------------------------------------------------------------------

# CSS

Next.js provides several ways to style your application using CSS, including:

* [Tailwind CSS](#tailwind-css)
* [CSS Modules](#css-modules)
* [Global CSS](#global-css)
* [External Stylesheets](#external-stylesheets)
* [Sass](/docs/app/guides/sass.md)
* [CSS-in-JS](/docs/app/guides/css-in-js.md)

## Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework that provides low-level utility classes to build custom designs.

Install Tailwind CSS:

```bash package="pnpm"
pnpm add -D tailwindcss @tailwindcss/postcss
```

```bash package="npm"
npm install -D tailwindcss @tailwindcss/postcss
```

```bash package="yarn"
yarn add -D tailwindcss @tailwindcss/postcss
```

```bash package="bun"
bun add -D tailwindcss @tailwindcss/postcss
```

Add the PostCSS plugin to your `postcss.config.mjs` file:

```js filename="postcss.config.mjs"
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

Import Tailwind in your global CSS file:

```css filename="app/globals.css"
@import 'tailwindcss';
```

Import the CSS file in your root layout:

```tsx filename="app/layout.tsx" switcher
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import './globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

Now you can start using Tailwind's utility classes in your application:

```tsx filename="app/page.tsx" switcher
export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

```jsx filename="app/page.js" switcher
export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

> **Good to know:** If you need broader browser support for very old browsers, see the [Tailwind CSS v3 setup instructions](/docs/app/guides/tailwind-v3-css.md).

## CSS Modules

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `app` directory:

```css filename="app/blog/blog.module.css"
.blog {
  padding: 24px;
}
```

```tsx filename="app/blog/page.tsx" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

```jsx filename="app/blog/page.js" switcher
import styles from './blog.module.css'

export default function Layout() {
  return <main className={styles.blog}></main>
}
```

## Global CSS

You can use global CSS to apply styles across your application.

Create a `app/global.css` file and import it in the root layout to apply the styles to **every route** in your application:

```css filename="app/global.css"
body {
  padding: 20px 20px 60px;
  max-width: 680px;
  margin: 0 auto;
}
```

```tsx filename="app/layout.tsx" switcher
// These styles apply to every route in the application
import './global.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
// These styles apply to every route in the application
import './global.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

> **Good to know:** Global styles can be imported into any layout, page, or component inside the `app` directory. However, since Next.js uses React's built-in support for stylesheets to integrate with Suspense, this currently does not remove stylesheets as you navigate between routes which can lead to conflicts. We recommend using global styles for *truly* global CSS (like Tailwind's base styles), [Tailwind CSS](#tailwind-css) for component styling, and [CSS Modules](#css-modules) for custom scoped CSS when needed.

## External stylesheets

Stylesheets published by external packages can be imported anywhere in the `app` directory, including colocated components:

```tsx filename="app/layout.tsx" switcher
import 'bootstrap/dist/css/bootstrap.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="container">{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import 'bootstrap/dist/css/bootstrap.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="container">{children}</body>
    </html>
  )
}
```

> **Good to know:** In React 19, `<link rel="stylesheet" href="..." />` can also be used. See the [React `link` documentation](https://react.dev/reference/react-dom/components/link) for more information.

## Ordering and Merging

Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.

For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:

```tsx filename="page.tsx" switcher
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

```jsx filename="page.js" switcher
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

```tsx filename="base-button.tsx" switcher
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

```jsx filename="base-button.js" switcher
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

### Recommendations

To keep CSS ordering predictable:

* Try to contain CSS imports to a single JavaScript or TypeScript entry file
* Import global styles and Tailwind stylesheets in the root of your application.
* **Use Tailwind CSS** for most styling needs as it covers common design patterns with utility classes.
* Use CSS Modules for component-specific styles when Tailwind utilities aren't sufficient.
* Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
* Extract shared styles into shared components to avoid duplicate imports.
* Turn off linters or formatters that auto-sort imports like ESLint’s [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports).
* You can use the [`cssChunking`](/docs/app/api-reference/config/next-config-js/cssChunking.md) option in `next.config.js` to control how CSS is chunked.

## Development vs Production

* In development (`next dev`), CSS updates apply instantly with [Fast Refresh](/docs/architecture/fast-refresh.md).
* In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
* CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
* CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.
## Next Steps

Learn more about the alternatives ways you can use CSS in your application.

- [Tailwind CSS v3](/docs/app/guides/tailwind-v3-css.md)
  - Style your Next.js Application using Tailwind CSS v3 for broader browser support.
- [Sass](/docs/app/guides/sass.md)
  - Style your Next.js application using Sass.
- [CSS-in-JS](/docs/app/guides/css-in-js.md)
  - Use CSS-in-JS libraries with Next.js


--------------------------------------------------------------------------------
title: "Image Optimization"
description: "Learn how to optimize images in Next.js"
source: "https://nextjs.org/docs/app/getting-started/images"
--------------------------------------------------------------------------------


---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-image-optimization.md)
