**Navigation:** [← Previous](./12-fonts.md) | [Index](./index.md) | [Next →](./14-static-exports.md)

---

# App Router

@router: Pages Router

This guide will help you:

* [Update your Next.js application from version 12 to version 13](#nextjs-version)
* [Upgrade features that work in both the `pages` and the `app` directories](#upgrading-new-features)
* [Incrementally migrate your existing application from `pages` to `app`](#migrating-from-pages-to-app)

## Upgrading

### Node.js Version

The minimum Node.js version is now **v18.17**. See the [Node.js documentation](https://nodejs.org/docs/latest-v18.x/api/) for more information.

### Next.js Version

To update to Next.js version 13, run the following command using your preferred package manager:

```bash filename="Terminal"
npm install next@latest react@latest react-dom@latest
```

### ESLint Version

If you're using ESLint, you need to upgrade your ESLint version:

```bash filename="Terminal"
npm install -D eslint-config-next@latest
```

> **Good to know**: You may need to restart the ESLint server in VS Code for the ESLint changes to take effect. Open the Command Palette (`cmd+shift+p` on Mac; `ctrl+shift+p` on Windows) and search for `ESLint: Restart ESLint Server`.

## Next Steps

After you've updated, see the following sections for next steps:

* [Upgrade new features](#upgrading-new-features): A guide to help you upgrade to new features such as the improved Image and Link Components.
* [Migrate from the `pages` to `app` directory](#migrating-from-pages-to-app): A step-by-step guide to help you incrementally migrate from the `pages` to the `app` directory.

## Upgrading New Features

Next.js 13 introduced the new [App Router](/docs/app.md) with new features and conventions. The new Router is available in the `app` directory and co-exists with the `pages` directory.

Upgrading to Next.js 13 does **not** require using the App Router. You can continue using `pages` with new features that work in both directories, such as the updated [Image component](#image-component), [Link component](#link-component), [Script component](#script-component), and [Font optimization](#font-optimization).

### `<Image/>` Component

Next.js 12 introduced new improvements to the Image Component with a temporary import: `next/future/image`. These improvements included less client-side JavaScript, easier ways to extend and style images, better accessibility, and native browser lazy loading.

In version 13, this new behavior is now the default for `next/image`.

There are two codemods to help you migrate to the new Image Component:

* [**`next-image-to-legacy-image` codemod**](/docs/app/guides/upgrading/codemods.md#next-image-to-legacy-image): Safely and automatically renames `next/image` imports to `next/legacy/image`. Existing components will maintain the same behavior.
* [**`next-image-experimental` codemod**](/docs/app/guides/upgrading/codemods.md#next-image-experimental): Dangerously adds inline styles and removes unused props. This will change the behavior of existing components to match the new defaults. To use this codemod, you need to run the `next-image-to-legacy-image` codemod first.

### `<Link>` Component

The [`<Link>` Component](/docs/app/api-reference/components/link.md) no longer requires manually adding an `<a>` tag as a child. This behavior was added as an experimental option in [version 12.2](https://nextjs.org/blog/next-12-2) and is now the default. In Next.js 13, `<Link>` always renders `<a>` and allows you to forward props to the underlying tag.

For example:

```jsx
import Link from 'next/link'

// Next.js 12: `<a>` has to be nested otherwise it's excluded
<Link href="/about">
  <a>About</a>
</Link>

// Next.js 13: `<Link>` always renders `<a>` under the hood
<Link href="/about">
  About
</Link>
```

To upgrade your links to Next.js 13, you can use the [`new-link` codemod](/docs/app/guides/upgrading/codemods.md#new-link).

### `<Script>` Component

The behavior of [`next/script`](/docs/app/api-reference/components/script.md) has been updated to support both `pages` and `app`, but some changes need to be made to ensure a smooth migration:

* Move any `beforeInteractive` scripts you previously included in `_document.js` to the root layout file (`app/layout.tsx`).
* The experimental `worker` strategy does not yet work in `app` and scripts denoted with this strategy will either have to be removed or modified to use a different strategy (e.g. `lazyOnload`).
* `onLoad`, `onReady`, and `onError` handlers will not work in Server Components so make sure to move them to a [Client Component](/docs/app/getting-started/server-and-client-components.md) or remove them altogether.

### Font Optimization

Previously, Next.js helped you optimize fonts by [inlining font CSS](/docs/app/api-reference/components/font.md). Version 13 introduces the new [`next/font`](/docs/app/api-reference/components/font.md) module which gives you the ability to customize your font loading experience while still ensuring great performance and privacy. `next/font` is supported in both the `pages` and `app` directories.

While [inlining CSS](/docs/app/api-reference/components/font.md) still works in `pages`, it does not work in `app`. You should use [`next/font`](/docs/app/api-reference/components/font.md) instead.

See the [Font Optimization](/docs/app/api-reference/components/font.md) page to learn how to use `next/font`.

## Migrating from `pages` to `app`

> **🎥 Watch:** Learn how to incrementally adopt the App Router → [YouTube (16 minutes)](https://www.youtube.com/watch?v=YQMSietiFm0).

Moving to the App Router may be the first time using React features that Next.js builds on top of such as Server Components, Suspense, and more. When combined with new Next.js features such as [special files](/docs/app/api-reference/file-conventions.md) and [layouts](/docs/app/api-reference/file-conventions/layout.md), migration means new concepts, mental models, and behavioral changes to learn.

We recommend reducing the combined complexity of these updates by breaking down your migration into smaller steps. The `app` directory is intentionally designed to work simultaneously with the `pages` directory to allow for incremental page-by-page migration.

* The `app` directory supports nested routes *and* layouts. [Learn more](/docs/app/getting-started/layouts-and-pages.md).
* Use nested folders to define routes and a special `page.js` file to make a route segment publicly accessible. [Learn more](#step-4-migrating-pages).
* [Special file conventions](/docs/app/api-reference/file-conventions.md) are used to create UI for each route segment. The most common special files are `page.js` and `layout.js`.
  * Use `page.js` to define UI unique to a route.
  * Use `layout.js` to define UI that is shared across multiple routes.
  * `.js`, `.jsx`, or `.tsx` file extensions can be used for special files.
* You can colocate other files inside the `app` directory such as components, styles, tests, and more. [Learn more](/docs/app.md).
* Data fetching functions like `getServerSideProps` and `getStaticProps` have been replaced with [a new API](/docs/app/getting-started/fetching-data.md) inside `app`. `getStaticPaths` has been replaced with [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md).
* `pages/_app.js` and `pages/_document.js` have been replaced with a single `app/layout.js` root layout. [Learn more](/docs/app/api-reference/file-conventions/layout.md#root-layout).
* `pages/_error.js` has been replaced with more granular `error.js` special files. [Learn more](/docs/app/getting-started/error-handling.md).
* `pages/404.js` has been replaced with the [`not-found.js`](/docs/app/api-reference/file-conventions/not-found.md) file.
* `pages/api/*` API Routes have been replaced with the [`route.js`](/docs/app/api-reference/file-conventions/route.md) (Route Handler) special file.

### Step 1: Creating the `app` directory

Update to the latest Next.js version (requires 13.4 or greater):

```bash
npm install next@latest
```

Then, create a new `app` directory at the root of your project (or `src/` directory).

### Step 2: Creating a Root Layout

Create a new `app/layout.tsx` file inside the `app` directory. This is a [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout) that will apply to all routes inside `app`.

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  // Layouts must accept a children prop.
  // This will be populated with nested layouts or pages
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
export default function RootLayout({
  // Layouts must accept a children prop.
  // This will be populated with nested layouts or pages
  children,
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

* The `app` directory **must** include a root layout.
* The root layout must define `<html>`, and `<body>` tags since Next.js does not automatically create them
* The root layout replaces the `pages/_app.tsx` and `pages/_document.tsx` files.
* `.js`, `.jsx`, or `.tsx` extensions can be used for layout files.

To manage `<head>` HTML elements, you can use the [built-in SEO support](/docs/app/getting-started/metadata-and-og-images.md):

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Home',
  description: 'Welcome to Next.js',
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'Home',
  description: 'Welcome to Next.js',
}
```

#### Migrating `_document.js` and `_app.js`

If you have an existing `_app` or `_document` file, you can copy the contents (e.g. global styles) to the root layout (`app/layout.tsx`). Styles in `app/layout.tsx` will *not* apply to `pages/*`. You should keep `_app`/`_document` while migrating to prevent your `pages/*` routes from breaking. Once fully migrated, you can then safely delete them.

If you are using any React Context providers, they will need to be moved to a [Client Component](/docs/app/getting-started/server-and-client-components.md).

#### Migrating the `getLayout()` pattern to Layouts (Optional)

Next.js recommended adding a [property to Page components](/docs/pages/building-your-application/routing/pages-and-layouts.md#layout-pattern) to achieve per-page layouts in the `pages` directory. This pattern can be replaced with native support for [nested layouts](/docs/app/api-reference/file-conventions/layout.md) in the `app` directory.

<details>
<summary>See before and after example</summary>

**Before**

```jsx filename="components/DashboardLayout.js"
export default function DashboardLayout({ children }) {
  return (
    <div>
      <h2>My Dashboard</h2>
      {children}
    </div>
  )
}
```

```jsx filename="pages/dashboard/index.js"
import DashboardLayout from '../components/DashboardLayout'

export default function Page() {
  return <p>My Page</p>
}

Page.getLayout = function getLayout(page) {
  return <DashboardLayout>{page}</DashboardLayout>
}
```

**After**

* Remove the `Page.getLayout` property from `pages/dashboard/index.js` and follow the [steps for migrating pages](#step-4-migrating-pages) to the `app` directory.

  ```jsx filename="app/dashboard/page.js"
  export default function Page() {
    return <p>My Page</p>
  }
  ```

* Move the contents of `DashboardLayout` into a new [Client Component](/docs/app/getting-started/server-and-client-components.md) to retain `pages` directory behavior.

  ```jsx filename="app/dashboard/DashboardLayout.js"
  'use client' // this directive should be at top of the file, before any imports.

  // This is a Client Component
  export default function DashboardLayout({ children }) {
    return (
      <div>
        <h2>My Dashboard</h2>
        {children}
      </div>
    )
  }
  ```

* Import the `DashboardLayout` into a new `layout.js` file inside the `app` directory.

  ```jsx filename="app/dashboard/layout.js"
  import DashboardLayout from './DashboardLayout'

  // This is a Server Component
  export default function Layout({ children }) {
    return <DashboardLayout>{children}</DashboardLayout>
  }
  ```

* You can incrementally move non-interactive parts of `DashboardLayout.js` (Client Component) into `layout.js` (Server Component) to reduce the amount of component JavaScript you send to the client.

</details>

### Step 3: Migrating `next/head`

In the `pages` directory, the `next/head` React component is used to manage `<head>` HTML elements such as `title` and `meta` . In the `app` directory, `next/head` is replaced with the new [built-in SEO support](/docs/app/getting-started/metadata-and-og-images.md).

**Before:**

```tsx filename="pages/index.tsx" switcher
import Head from 'next/head'

export default function Page() {
  return (
    <>
      <Head>
        <title>My page title</title>
      </Head>
    </>
  )
}
```

```jsx filename="pages/index.js" switcher
import Head from 'next/head'

export default function Page() {
  return (
    <>
      <Head>
        <title>My page title</title>
      </Head>
    </>
  )
}
```

**After:**

```tsx filename="app/page.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My Page Title',
}

export default function Page() {
  return '...'
}
```

```jsx filename="app/page.js" switcher
export const metadata = {
  title: 'My Page Title',
}

export default function Page() {
  return '...'
}
```

[See all metadata options](/docs/app/api-reference/functions/generate-metadata.md).

### Step 4: Migrating Pages

* Pages in the [`app` directory](/docs/app.md) are [Server Components](/docs/app/getting-started/server-and-client-components.md) by default. This is different from the `pages` directory where pages are [Client Components](/docs/app/getting-started/server-and-client-components.md).
* [Data fetching](/docs/app/getting-started/fetching-data.md) has changed in `app`. `getServerSideProps`, `getStaticProps` and `getInitialProps` have been replaced with a simpler API.
* The `app` directory uses nested folders to define routes and a special `page.js` file to make a route segment publicly accessible.
* | `pages` Directory | `app` Directory       | Route          |
  | ----------------- | --------------------- | -------------- |
  | `index.js`        | `page.js`             | `/`            |
  | `about.js`        | `about/page.js`       | `/about`       |
  | `blog/[slug].js`  | `blog/[slug]/page.js` | `/blog/post-1` |

We recommend breaking down the migration of a page into two main steps:

* Step 1: Move the default exported Page Component into a new Client Component.
* Step 2: Import the new Client Component into a new `page.js` file inside the `app` directory.

> **Good to know**: This is the easiest migration path because it has the most comparable behavior to the `pages` directory.

**Step 1: Create a new Client Component**

* Create a new separate file inside the `app` directory (i.e. `app/home-page.tsx` or similar) that exports a Client Component. To define Client Components, add the `'use client'` directive to the top of the file (before any imports).
  * Similar to the Pages Router, there is an [optimization step](/docs/app/getting-started/server-and-client-components.md#on-the-client-first-load) to prerender Client Components to static HTML on the initial page load.
* Move the default exported page component from `pages/index.js` to `app/home-page.tsx`.

```tsx filename="app/home-page.tsx" switcher
'use client'

// This is a Client Component (same as components in the `pages` directory)
// It receives data as props, has access to state and effects, and is
// prerendered on the server during the initial page load.
export default function HomePage({ recentPosts }) {
  return (
    <div>
      {recentPosts.map((post) => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  )
}
```

```jsx filename="app/home-page.js" switcher
'use client'

// This is a Client Component. It receives data as props and
// has access to state and effects just like Page components
// in the `pages` directory.
export default function HomePage({ recentPosts }) {
  return (
    <div>
      {recentPosts.map((post) => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  )
}
```

**Step 2: Create a new page**

* Create a new `app/page.tsx` file inside the `app` directory. This is a Server Component by default.

* Import the `home-page.tsx` Client Component into the page.

* If you were fetching data in `pages/index.js`, move the data fetching logic directly into the Server Component using the new [data fetching APIs](/docs/app/getting-started/fetching-data.md). See the [data fetching upgrade guide](#step-6-migrating-data-fetching-methods) for more details.

  ```tsx filename="app/page.tsx" switcher
  // Import your Client Component
  import HomePage from './home-page'

  async function getPosts() {
    const res = await fetch('https://...')
    const posts = await res.json()
    return posts
  }

  export default async function Page() {
    // Fetch data directly in a Server Component
    const recentPosts = await getPosts()
    // Forward fetched data to your Client Component
    return <HomePage recentPosts={recentPosts} />
  }
  ```

  ```jsx filename="app/page.js" switcher
  // Import your Client Component
  import HomePage from './home-page'

  async function getPosts() {
    const res = await fetch('https://...')
    const posts = await res.json()
    return posts
  }

  export default async function Page() {
    // Fetch data directly in a Server Component
    const recentPosts = await getPosts()
    // Forward fetched data to your Client Component
    return <HomePage recentPosts={recentPosts} />
  }
  ```

* If your previous page used `useRouter`, you'll need to update to the new routing hooks. [Learn more](/docs/app/api-reference/functions/use-router.md).

* Start your development server and visit [`http://localhost:3000`](http://localhost:3000). You should see your existing index route, now served through the app directory.

### Step 5: Migrating Routing Hooks

A new router has been added to support the new behavior in the `app` directory.

In `app`, you should use the three new hooks imported from `next/navigation`: [`useRouter()`](/docs/app/api-reference/functions/use-router.md), [`usePathname()`](/docs/app/api-reference/functions/use-pathname.md), and [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md).

* The new `useRouter` hook is imported from `next/navigation` and has different behavior to the `useRouter` hook in `pages` which is imported from `next/router`.
  * The [`useRouter` hook imported from `next/router`](/docs/pages/api-reference/functions/use-router.md) is not supported in the `app` directory but can continue to be used in the `pages` directory.
* The new `useRouter` does not return the `pathname` string. Use the separate `usePathname` hook instead.
* The new `useRouter` does not return the `query` object. Search parameters and dynamic route parameters are now separate. Use the `useSearchParams` and `useParams` hooks instead.
* You can use `useSearchParams` and `usePathname` together to listen to page changes. See the [Router Events](/docs/app/api-reference/functions/use-router.md#router-events) section for more details.
* These new hooks are only supported in Client Components. They cannot be used in Server Components.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useRouter, usePathname, useSearchParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // ...
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useRouter, usePathname, useSearchParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // ...
}
```

In addition, the new `useRouter` hook has the following changes:

* `isFallback` has been removed because `fallback` has [been replaced](#replacing-fallback).
* The `locale`, `locales`, `defaultLocales`, `domainLocales` values have been removed because built-in i18n Next.js features are no longer necessary in the `app` directory. [Learn more about i18n](/docs/app/guides/internationalization.md).
* `basePath` has been removed. The alternative will not be part of `useRouter`. It has not yet been implemented.
* `asPath` has been removed because the concept of `as` has been removed from the new router.
* `isReady` has been removed because it is no longer necessary. During [static rendering](/docs/app/guides/caching.md#static-rendering), any component that uses the [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md) hook will skip the prerendering step and instead be rendered on the client at runtime.
* `route` has been removed. `usePathname` or `useSelectedLayoutSegments()` provide an alternative.

[View the `useRouter()` API reference](/docs/app/api-reference/functions/use-router.md).

#### Sharing components between `pages` and `app`

To keep components compatible between the `pages` and `app` routers, refer to the [`useRouter` hook from `next/compat/router`](/docs/pages/api-reference/functions/use-router.md#the-nextcompatrouter-export).
This is the `useRouter` hook from the `pages` directory, but intended to be used while sharing components between routers. Once you are ready to use it only on the `app` router, update to the new [`useRouter` from `next/navigation`](/docs/app/api-reference/functions/use-router.md).

### Step 6: Migrating Data Fetching Methods

The `pages` directory uses `getServerSideProps` and `getStaticProps` to fetch data for pages. Inside the `app` directory, these previous data fetching functions are replaced with a [simpler API](/docs/app/getting-started/fetching-data.md) built on top of `fetch()` and `async` React Server Components.

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  // This request should be cached until manually invalidated.
  // Similar to `getStaticProps`.
  // `force-cache` is the default and can be omitted.
  const staticData = await fetch(`https://...`, { cache: 'force-cache' })

  // This request should be refetched on every request.
  // Similar to `getServerSideProps`.
  const dynamicData = await fetch(`https://...`, { cache: 'no-store' })

  // This request should be cached with a lifetime of 10 seconds.
  // Similar to `getStaticProps` with the `revalidate` option.
  const revalidatedData = await fetch(`https://...`, {
    next: { revalidate: 10 },
  })

  return <div>...</div>
}
```

```jsx filename="app/page.js" switcher
export default async function Page() {
  // This request should be cached until manually invalidated.
  // Similar to `getStaticProps`.
  // `force-cache` is the default and can be omitted.
  const staticData = await fetch(`https://...`, { cache: 'force-cache' })

  // This request should be refetched on every request.
  // Similar to `getServerSideProps`.
  const dynamicData = await fetch(`https://...`, { cache: 'no-store' })

  // This request should be cached with a lifetime of 10 seconds.
  // Similar to `getStaticProps` with the `revalidate` option.
  const revalidatedData = await fetch(`https://...`, {
    next: { revalidate: 10 },
  })

  return <div>...</div>
}
```

#### Server-side Rendering (`getServerSideProps`)

In the `pages` directory, `getServerSideProps` is used to fetch data on the server and forward props to the default exported React component in the file. The initial HTML for the page is prerendered from the server, followed by "hydrating" the page in the browser (making it interactive).

```jsx filename="pages/dashboard.js"
// `pages` directory

export async function getServerSideProps() {
  const res = await fetch(`https://...`)
  const projects = await res.json()

  return { props: { projects } }
}

export default function Dashboard({ projects }) {
  return (
    <ul>
      {projects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  )
}
```

In the App Router, we can colocate our data fetching inside our React components using [Server Components](/docs/app/getting-started/server-and-client-components.md). This allows us to send less JavaScript to the client, while maintaining the rendered HTML from the server.

By setting the `cache` option to `no-store`, we can indicate that the fetched data should [never be cached](/docs/app/getting-started/fetching-data.md). This is similar to `getServerSideProps` in the `pages` directory.

```tsx filename="app/dashboard/page.tsx" switcher
// `app` directory

// This function can be named anything
async function getProjects() {
  const res = await fetch(`https://...`, { cache: 'no-store' })
  const projects = await res.json()

  return projects
}

export default async function Dashboard() {
  const projects = await getProjects()

  return (
    <ul>
      {projects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
// `app` directory

// This function can be named anything
async function getProjects() {
  const res = await fetch(`https://...`, { cache: 'no-store' })
  const projects = await res.json()

  return projects
}

export default async function Dashboard() {
  const projects = await getProjects()

  return (
    <ul>
      {projects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  )
}
```

#### Accessing Request Object

In the `pages` directory, you can retrieve request-based data based on the Node.js HTTP API.

For example, you can retrieve the `req` object from `getServerSideProps` and use it to retrieve the request's cookies and headers.

```jsx filename="pages/index.js"
// `pages` directory

export async function getServerSideProps({ req, query }) {
  const authHeader = req.getHeaders()['authorization'];
  const theme = req.cookies['theme'];

  return { props: { ... }}
}

export default function Page(props) {
  return ...
}
```

The `app` directory exposes new read-only functions to retrieve request data:

* [`headers`](/docs/app/api-reference/functions/headers.md): Based on the Web Headers API, and can be used inside [Server Components](/docs/app/getting-started/server-and-client-components.md) to retrieve request headers.
* [`cookies`](/docs/app/api-reference/functions/cookies.md): Based on the Web Cookies API, and can be used inside [Server Components](/docs/app/getting-started/server-and-client-components.md) to retrieve cookies.

```tsx filename="app/page.tsx" switcher
// `app` directory
import { cookies, headers } from 'next/headers'

async function getData() {
  const authHeader = (await headers()).get('authorization')

  return '...'
}

export default async function Page() {
  // You can use `cookies` or `headers` inside Server Components
  // directly or in your data fetching function
  const theme = (await cookies()).get('theme')
  const data = await getData()
  return '...'
}
```

```jsx filename="app/page.js" switcher
// `app` directory
import { cookies, headers } from 'next/headers'

async function getData() {
  const authHeader = (await headers()).get('authorization')

  return '...'
}

export default async function Page() {
  // You can use `cookies` or `headers` inside Server Components
  // directly or in your data fetching function
  const theme = (await cookies()).get('theme')
  const data = await getData()
  return '...'
}
```

#### Static Site Generation (`getStaticProps`)

In the `pages` directory, the `getStaticProps` function is used to pre-render a page at build time. This function can be used to fetch data from an external API or directly from a database, and pass this data down to the entire page as it's being generated during the build.

```jsx filename="pages/index.js"
// `pages` directory

export async function getStaticProps() {
  const res = await fetch(`https://...`)
  const projects = await res.json()

  return { props: { projects } }
}

export default function Index({ projects }) {
  return projects.map((project) => <div>{project.name}</div>)
}
```

In the `app` directory, data fetching with [`fetch()`](/docs/app/api-reference/functions/fetch.md) will default to `cache: 'force-cache'`, which will cache the request data until manually invalidated. This is similar to `getStaticProps` in the `pages` directory.

```jsx filename="app/page.js"
// `app` directory

// This function can be named anything
async function getProjects() {
  const res = await fetch(`https://...`)
  const projects = await res.json()

  return projects
}

export default async function Index() {
  const projects = await getProjects()

  return projects.map((project) => <div>{project.name}</div>)
}
```

#### Dynamic paths (`getStaticPaths`)

In the `pages` directory, the `getStaticPaths` function is used to define the dynamic paths that should be pre-rendered at build time.

```jsx filename="pages/posts/[id].js"
// `pages` directory
import PostLayout from '@/components/post-layout'

export async function getStaticPaths() {
  return {
    paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
  }
}

export async function getStaticProps({ params }) {
  const res = await fetch(`https://.../posts/${params.id}`)
  const post = await res.json()

  return { props: { post } }
}

export default function Post({ post }) {
  return <PostLayout post={post} />
}
```

In the `app` directory, `getStaticPaths` is replaced with [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md).

[`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) behaves similarly to `getStaticPaths`, but has a simplified API for returning route parameters and can be used inside [layouts](/docs/app/api-reference/file-conventions/layout.md). The return shape of `generateStaticParams` is an array of segments instead of an array of nested `param` objects or a string of resolved paths.

```jsx filename="app/posts/[id]/page.js"
// `app` directory
import PostLayout from '@/components/post-layout'

export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }]
}

async function getPost(params) {
  const res = await fetch(`https://.../posts/${(await params).id}`)
  const post = await res.json()

  return post
}

export default async function Post({ params }) {
  const post = await getPost(params)

  return <PostLayout post={post} />
}
```

Using the name `generateStaticParams` is more appropriate than `getStaticPaths` for the new model in the `app` directory. The `get` prefix is replaced with a more descriptive `generate`, which sits better alone now that `getStaticProps` and `getServerSideProps` are no longer necessary. The `Paths` suffix is replaced by `Params`, which is more appropriate for nested routing with multiple dynamic segments.

***

#### Replacing `fallback`

In the `pages` directory, the `fallback` property returned from `getStaticPaths` is used to define the behavior of a page that isn't pre-rendered at build time. This property can be set to `true` to show a fallback page while the page is being generated, `false` to show a 404 page, or `blocking` to generate the page at request time.

```jsx filename="pages/posts/[id].js"
// `pages` directory

export async function getStaticPaths() {
  return {
    paths: [],
    fallback: 'blocking'
  };
}

export async function getStaticProps({ params }) {
  ...
}

export default function Post({ post }) {
  return ...
}
```

In the `app` directory the [`config.dynamicParams` property](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) controls how params outside of [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) are handled:

* **`true`**: (default) Dynamic segments not included in `generateStaticParams` are generated on demand.
* **`false`**: Dynamic segments not included in `generateStaticParams` will return a 404.

This replaces the `fallback: true | false | 'blocking'` option of `getStaticPaths` in the `pages` directory. The `fallback: 'blocking'` option is not included in `dynamicParams` because the difference between `'blocking'` and `true` is negligible with streaming.

```jsx filename="app/posts/[id]/page.js"
// `app` directory

export const dynamicParams = true;

export async function generateStaticParams() {
  return [...]
}

async function getPost(params) {
  ...
}

export default async function Post({ params }) {
  const post = await getPost(params);

  return ...
}
```

With [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) set to `true` (the default), when a route segment is requested that hasn't been generated, it will be server-rendered and cached.

#### Incremental Static Regeneration (`getStaticProps` with `revalidate`)

In the `pages` directory, the `getStaticProps` function allows you to add a `revalidate` field to automatically regenerate a page after a certain amount of time.

```jsx filename="pages/index.js"
// `pages` directory

export async function getStaticProps() {
  const res = await fetch(`https://.../posts`)
  const posts = await res.json()

  return {
    props: { posts },
    revalidate: 60,
  }
}

export default function Index({ posts }) {
  return (
    <Layout>
      <PostList posts={posts} />
    </Layout>
  )
}
```

In the `app` directory, data fetching with [`fetch()`](/docs/app/api-reference/functions/fetch.md) can use `revalidate`, which will cache the request for the specified amount of seconds.

```jsx filename="app/page.js"
// `app` directory

async function getPosts() {
  const res = await fetch(`https://.../posts`, { next: { revalidate: 60 } })
  const data = await res.json()

  return data.posts
}

export default async function PostList() {
  const posts = await getPosts()

  return posts.map((post) => <div>{post.name}</div>)
}
```

#### API Routes

API Routes continue to work in the `pages/api` directory without any changes. However, they have been replaced by [Route Handlers](/docs/app/api-reference/file-conventions/route.md) in the `app` directory.

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

```ts filename="app/api/route.ts" switcher
export async function GET(request: Request) {}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {}
```

> **Good to know**: If you previously used API routes to call an external API from the client, you can now use [Server Components](/docs/app/getting-started/server-and-client-components.md) instead to securely fetch data. Learn more about [data fetching](/docs/app/getting-started/fetching-data.md).

#### Single-Page Applications

If you are also migrating to Next.js from a Single-Page Application (SPA) at the same time, see our [documentation](/docs/app/guides/single-page-applications.md) to learn more.

### Step 7: Styling

In the `pages` directory, global stylesheets are restricted to only `pages/_app.js`. With the `app` directory, this restriction has been lifted. Global styles can be added to any layout, page, or component.

* [CSS Modules](/docs/app/getting-started/css.md#css-modules)
* [Tailwind CSS](/docs/app/getting-started/css.md#tailwind-css)
* [Global Styles](/docs/app/getting-started/css.md#global-css)
* [CSS-in-JS](/docs/app/guides/css-in-js.md)
* [External Stylesheets](/docs/app/getting-started/css.md#external-stylesheets)
* [Sass](/docs/app/guides/sass.md)

#### Tailwind CSS

If you're using Tailwind CSS, you'll need to add the `app` directory to your `tailwind.config.js` file:

```js filename="tailwind.config.js"
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}', // <-- Add this line
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
}
```

You'll also need to import your global styles in your `app/layout.js` file:

```jsx filename="app/layout.js"
import '../styles/globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

Learn more about [styling with Tailwind CSS](/docs/app/getting-started/css.md#tailwind-css)

## Using App Router together with Pages Router

When navigating between routes served by the different Next.js routers, there will be a hard navigation. Automatic link prefetching with `next/link` will not prefetch across routers.

Instead, you can [optimize navigations](https://vercel.com/guides/optimizing-hard-navigations) between App Router and Pages Router to retain the prefetched and fast page transitions. [Learn more](https://vercel.com/guides/optimizing-hard-navigations).

## Codemods

Next.js provides Codemod transformations to help upgrade your codebase when a feature is deprecated. See [Codemods](/docs/app/guides/upgrading/codemods.md) for more information.


--------------------------------------------------------------------------------
title: "How to migrate from Create React App to Next.js"
description: "Learn how to migrate your existing React application from Create React App to Next.js."
source: "https://nextjs.org/docs/pages/guides/migrating/from-create-react-app"
--------------------------------------------------------------------------------

# Create React App

@router: Pages Router

This guide will help you migrate an existing Create React App (CRA) site to Next.js.

## Why Switch?

There are several reasons why you might want to switch from Create React App to Next.js:

### Slow initial page loading time

Create React App uses purely client-side rendering. Client-side only applications, also known as [single-page applications (SPAs)](/docs/app/guides/single-page-applications.md), often experience slow initial page loading time. This happens due to a couple of reasons:

1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load data.
2. Your application code grows with every new feature and dependency you add.

### No automatic code splitting

The previous issue of slow loading times can be somewhat mitigated with code splitting. However, if you try to do code splitting manually, you can inadvertently introduce network waterfalls. Next.js provides automatic code splitting and tree-shaking built into its router and build pipeline.

### Network waterfalls

A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One pattern for data fetching in a [SPA](/docs/app/guides/single-page-applications.md) is to render a placeholder, and then fetch data after the component has mounted. Unfortunately, a child component can only begin fetching data after its parent has finished loading its own data, resulting in a “waterfall” of requests.

While client-side data fetching is supported in Next.js, Next.js also lets you move data fetching to the server. This often eliminates client-server waterfalls altogether.

### Fast and intentional loading states

With built-in support for [streaming through React Suspense](/docs/app/getting-started/linking-and-navigating.md#streaming), you can define which parts of your UI load first and in what order, without creating network waterfalls.

This enables you to build pages that are faster to load and eliminate [layout shifts](https://vercel.com/blog/how-core-web-vitals-affect-seo).

### Choose the data fetching strategy

Depending on your needs, Next.js allows you to choose your data fetching strategy on a page or component-level basis. For example, you could fetch data from your CMS and render blog posts at build time (SSG) for quick load speeds, or fetch data at request time (SSR) when necessary.

### Proxy

[Next.js Proxy](/docs/app/api-reference/file-conventions/proxy.md) allows you to run code on the server before a request is completed. For instance, you can avoid a flash of unauthenticated content by redirecting a user to a login page in the proxy for authenticated-only pages. You can also use it for features like A/B testing, experimentation, and [internationalization](/docs/app/guides/internationalization.md).

### Built-in Optimizations

[Images](/docs/app/api-reference/components/image.md), [fonts](/docs/app/api-reference/components/font.md), and [third-party scripts](/docs/app/guides/scripts.md) often have a large impact on an application’s performance. Next.js includes specialized components and APIs that automatically optimize them for you.

## Migration Steps

Our goal is to get a working Next.js application as quickly as possible so that you can then adopt Next.js features incrementally. To begin with, we’ll treat your application as a purely client-side application ([SPA](/docs/app/guides/single-page-applications.md)) without immediately replacing your existing router. This reduces complexity and merge conflicts.

> **Note**: If you are using advanced CRA configurations such as a custom `homepage` field in your `package.json`, a custom service worker, or specific Babel/webpack tweaks, please see the **Additional Considerations** section at the end of this guide for tips on replicating or adapting these features in Next.js.

### Step 1: Install the Next.js Dependency

Install Next.js in your existing project:

```bash filename="Terminal"
npm install next@latest
```

### Step 2: Create the Next.js Configuration File

Create a `next.config.ts` at the root of your project (same level as your `package.json`). This file holds your [Next.js configuration options](/docs/app/api-reference/config/next-config-js.md).

```js filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA)
  distDir: 'build', // Changes the build output directory to `build`
}

export default nextConfig
```

> **Note**: Using `output: 'export'` means you’re doing a static export. You will **not** have access to server-side features like SSR or APIs. You can remove this line to leverage Next.js server features.

### Step 3: Create the Root Layout

A Next.js [App Router](/docs/app.md) application must include a [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout) file, which is a [React Server Component](/docs/app/getting-started/server-and-client-components.md) that will wrap all your pages.

The closest equivalent of the root layout file in a CRA application is `public/index.html`, which includes your `<html>`, `<head>`, and `<body>` tags.

1. Create a new `app` directory inside your `src` folder (or at your project root if you prefer `app` at the root).
2. Inside the `app` directory, create a `layout.tsx` (or `layout.js`) file:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return '...'
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return '...'
}
```

Now copy the content of your old `index.html` into this `<RootLayout>` component. Replace `body div#root` (and `body noscript`) with `<div id="root">{children}</div>`.

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

> **Good to know**: Next.js ignores CRA’s `public/manifest.json`, additional iconography, and [testing configuration](/docs/app/guides/testing.md) by default. If you need these, Next.js has support with its [Metadata API](/docs/app/getting-started/metadata-and-og-images.md) and [Testing](/docs/app/guides/testing.md) setup.

### Step 4: Metadata

Next.js automatically includes the `<meta charset="UTF-8" />` and `<meta name="viewport" content="width=device-width, initial-scale=1" />` tags, so you can remove them from `<head>`:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

Any [metadata files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata) such as `favicon.ico`, `icon.png`, `robots.txt` are automatically added to the application `<head>` tag as long as you have them placed into the top level of the `app` directory. After moving [all supported files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata) into the `app` directory you can safely delete their `<link>` tags:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

Finally, Next.js can manage your last `<head>` tags with the [Metadata API](/docs/app/getting-started/metadata-and-og-images.md). Move your final metadata info into an exported [`metadata` object](/docs/app/api-reference/functions/generate-metadata.md#metadata-object):

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

With the above changes, you shifted from declaring everything in your `index.html` to using Next.js' convention-based approach built into the framework ([Metadata API](/docs/app/getting-started/metadata-and-og-images.md)). This approach enables you to more easily improve your SEO and web shareability of your pages.

### Step 5: Styles

Like CRA, Next.js supports [CSS Modules](/docs/app/getting-started/css.md#css-modules) out of the box. It also supports [global CSS imports](/docs/app/getting-started/css.md#global-css).

If you have a global CSS file, import it into your `app/layout.tsx`:

```tsx filename="app/layout.tsx" switcher
import '../index.css'

export const metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

If you're using Tailwind CSS, see our [installation docs](/docs/app/getting-started/css.md#tailwind-css).

### Step 6: Create the Entrypoint Page

Create React App uses `src/index.tsx` (or `index.js`) as the entry point. In Next.js (App Router), each folder inside the `app` directory corresponds to a route, and each folder should have a `page.tsx`.

Since we want to keep the app as an SPA for now and intercept **all** routes, we’ll use an [optional catch-all route](/docs/app/api-reference/file-conventions/dynamic-routes.md#optional-catch-all-segments).

1. **Create a `[[...slug]]` directory inside `app`.**

```bash
app
 ┣ [[...slug]]
 ┃ ┗ page.tsx
 ┣ layout.tsx
```

2. **Add the following to `page.tsx`**:

```tsx filename="app/[[...slug]]/page.tsx" switcher
export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

This tells Next.js to generate a single route for the empty slug (`/`), effectively mapping **all** routes to the same page. This page is a [Server Component](/docs/app/getting-started/server-and-client-components.md), prerendered into static HTML.

### Step 7: Add a Client-Only Entrypoint

Next, we’ll embed your CRA’s root App component inside a [Client Component](/docs/app/getting-started/server-and-client-components.md) so that all logic remains client-side. If this is your first time using Next.js, it's worth knowing that clients components (by default) are still prerendered on the server. You can think about them as having the additional capability of running client-side JavaScript.

Create a `client.tsx` (or `client.js`) in `app/[[...slug]]/`:

```tsx filename="app/[[...slug]]/client.tsx" switcher
'use client'

import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

```jsx filename="app/[[...slug]]/client.js" switcher
'use client'

import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

* The `'use client'` directive makes this file a **Client Component**.
* The `dynamic` import with `ssr: false` disables server-side rendering for the `<App />` component, making it truly client-only (SPA).

Now update your `page.tsx` (or `page.js`) to use your new component:

```tsx filename="app/[[...slug]]/page.tsx" switcher
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

### Step 8: Update Static Image Imports

In CRA, importing an image file returns its public URL as a string:

```tsx
import image from './img.png'

export default function App() {
  return <img src={image} />
}
```

With Next.js, static image imports return an object. The object can then be used directly with the Next.js [`<Image>` component](/docs/app/api-reference/components/image.md), or you can use the object's `src` property with your existing `<img>` tag.

The `<Image>` component has the added benefits of [automatic image optimization](/docs/app/api-reference/components/image.md). The `<Image>` component automatically sets the `width` and `height` attributes of the resulting `<img>` based on the image's dimensions. This prevents layout shifts when the image loads. However, this can cause issues if your app contains images with only one of their dimensions being styled without the other styled to `auto`. When not styled to `auto`, the dimension will default to the `<img>` dimension attribute's value, which can cause the image to appear distorted.

Keeping the `<img>` tag will reduce the amount of changes in your application and prevent the above issues. You can then optionally later migrate to the `<Image>` component to take advantage of optimizing images by [configuring a loader](/docs/app/api-reference/components/image.md#loader), or moving to the default Next.js server which has automatic image optimization.

**Convert absolute import paths for images imported from `/public` into relative imports:**

```tsx
// Before
import logo from '/logo.png'

// After
import logo from '../public/logo.png'
```

**Pass the image `src` property instead of the whole image object to your `<img>` tag:**

```tsx
// Before
<img src={logo} />

// After
<img src={logo.src} />
```

Alternatively, you can reference the public URL for the image asset based on the filename. For example, `public/logo.png` will serve the image at `/logo.png` for your application, which would be the `src` value.

> **Warning:** If you're using TypeScript, you might encounter type errors when accessing the `src` property. To fix them, you need to add `next-env.d.ts` to the [`include` array](https://www.typescriptlang.org/tsconfig#include) of your `tsconfig.json` file. Next.js will automatically generate this file when you run your application on step 9.

### Step 9: Migrate Environment Variables

Next.js supports [environment variables](/docs/app/guides/environment-variables.md) similarly to CRA but **requires** a `NEXT_PUBLIC_` prefix for any variable you want to expose in the browser.

The main difference is the prefix used to expose environment variables on the client-side. Change all environment variables with the `REACT_APP_` prefix to `NEXT_PUBLIC_`.

### Step 10: Update Scripts in `package.json`

Update your `package.json` scripts to use Next.js commands. Also, add `.next` and `next-env.d.ts` to your `.gitignore`:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "npx serve@latest ./build"
  }
}
```

```txt filename=".gitignore"
# ...
.next
next-env.d.ts
```

Now you can run:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). You should see your application now running on Next.js (in SPA mode).

### Step 11: Clean Up

You can now remove artifacts that are specific to Create React App:

* `public/index.html`
* `src/index.tsx`
* `src/react-app-env.d.ts`
* The `reportWebVitals` setup
* The `react-scripts` dependency (uninstall it from `package.json`)

## Additional Considerations

### Using a Custom `homepage` in CRA

If you used the `homepage` field in your CRA `package.json` to serve the app under a specific subpath, you can replicate that in Next.js using the [`basePath` configuration](/docs/app/api-reference/config/next-config-js/basePath.md) in `next.config.ts`:

```ts filename="next.config.ts"
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  basePath: '/my-subpath',
  // ...
}

export default nextConfig
```

### Handling a Custom `Service Worker`

If you used CRA’s service worker (e.g., `serviceWorker.js` from `create-react-app`), you can learn how to create [Progressive Web Applications (PWAs)](/docs/app/guides/progressive-web-apps.md) with Next.js.

### Proxying API Requests

If your CRA app used the `proxy` field in `package.json` to forward requests to a backend server, you can replicate this with [Next.js rewrites](/docs/app/api-reference/config/next-config-js/rewrites.md) in `next.config.ts`:

```ts filename="next.config.ts"
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://your-backend.com/:path*',
      },
    ]
  },
}
```

### Custom Webpack

If you had a custom webpack or Babel configuration in CRA, you can extend Next.js’s config in `next.config.ts`:

```ts filename="next.config.ts"
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  webpack: (config, { isServer }) => {
    // Modify the webpack config here
    return config
  },
}

export default nextConfig
```

> **Note**: This will require using Webpack by adding `--webpack` to your `dev` script.

### TypeScript Setup

Next.js automatically sets up TypeScript if you have a `tsconfig.json`. Make sure `next-env.d.ts` is listed in your `tsconfig.json` `include` array:

```json
{
  "include": ["next-env.d.ts", "app/**/*", "src/**/*"]
}
```

## Bundler Compatibility

Create React App uses webpack for bundling. Next.js now defaults to [Turbopack](/docs/app/api-reference/config/next-config-js/turbopack.md) for faster local development:

```bash
next dev  # Uses Turbopack by default
```

To use Webpack instead (similar to CRA):

```bash
next dev --webpack
```

You can still provide a [custom webpack configuration](/docs/app/api-reference/config/next-config-js/webpack.md) if you need to migrate advanced webpack settings from CRA.

## Next Steps

If everything worked, you now have a functioning Next.js application running as a single-page application. You aren’t yet leveraging Next.js features like server-side rendering or file-based routing, but you can now do so incrementally:

* **Migrate from React Router** to the [Next.js App Router](/docs/app.md) for:
  * Automatic code splitting
  * [Streaming server rendering](/docs/app/api-reference/file-conventions/loading.md)
  * [React Server Components](/docs/app/getting-started/server-and-client-components.md)
* **Optimize images** with the [`<Image>` component](/docs/app/api-reference/components/image.md)
* **Optimize fonts** with [`next/font`](/docs/app/api-reference/components/font.md)
* **Optimize third-party scripts** with the [`<Script>` component](/docs/app/guides/scripts.md)
* **Enable ESLint** with Next.js [recommended rules](/docs/app/api-reference/config/eslint.md#setup-eslint)

> **Note**: Using a static export (`output: 'export'`) [does not currently support](https://github.com/vercel/next.js/issues/54393) the `useParams` hook or other server features. To use all Next.js features, remove `output: 'export'` from your `next.config.ts`.


--------------------------------------------------------------------------------
title: "How to migrate from Vite to Next.js"
description: "Learn how to migrate your existing React application from Vite to Next.js."
source: "https://nextjs.org/docs/pages/guides/migrating/from-vite"
--------------------------------------------------------------------------------

# Vite

@router: Pages Router

This guide will help you migrate an existing Vite application to Next.js.

## Why Switch?

There are several reasons why you might want to switch from Vite to Next.js:

### Slow initial page loading time

If you have built your application with the [default Vite plugin for React](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-react), your application is a purely client-side application. Client-side only applications, also known as single-page applications (SPAs), often experience slow initial page loading time. This happens due to a couple of reasons:

1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load some data.
2. Your application code grows with every new feature and extra dependency you add.

### No automatic code splitting

The previous issue of slow loading times can be somewhat managed with code splitting. However, if you try to do code splitting manually, you'll often make performance worse. It's easy to inadvertently introduce network waterfalls when code-splitting manually. Next.js provides automatic code splitting built into its router.

### Network waterfalls

A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One common pattern for data fetching in an SPA is to initially render a placeholder, and then fetch data after the component has mounted. Unfortunately, this means that a child component that fetches data can't start fetching until the parent component has finished loading its own data.

While fetching data on the client is supported with Next.js, it also gives you the option to shift data fetching to the server, which can eliminate client-server waterfalls.

### Fast and intentional loading states

With built-in support for [streaming through React Suspense](/docs/app/getting-started/linking-and-navigating.md#streaming), you can be more intentional about which parts of your UI you want to load first and in what order without introducing network waterfalls.

This enables you to build pages that are faster to load and eliminate [layout shifts](https://vercel.com/blog/how-core-web-vitals-affect-seo).

### Choose the data fetching strategy

Depending on your needs, Next.js allows you to choose your data fetching strategy on a page and component basis. You can decide to fetch at build time, at request time on the server, or on the client. For example, you can fetch data from your CMS and render your blog posts at build time, which can then be efficiently cached on a CDN.

### Proxy

[Next.js Proxy](/docs/app/api-reference/file-conventions/proxy.md) allows you to run code on the server before a request is completed. This is especially useful to avoid having a flash of unauthenticated content when the user visits an authenticated-only page by redirecting the user to a login page. The proxy is also useful for experimentation and [internationalization](/docs/app/guides/internationalization.md).

### Built-in Optimizations

[Images](/docs/app/api-reference/components/image.md), [fonts](/docs/app/api-reference/components/font.md), and [third-party scripts](/docs/app/guides/scripts.md) often have significant impact on an application's performance. Next.js comes with built-in components that automatically optimize those for you.

## Migration Steps

Our goal with this migration is to get a working Next.js application as quickly as possible, so that
you can then adopt Next.js features incrementally. To begin with, we'll keep it as a purely
client-side application (SPA) without migrating your existing router. This helps minimize the
chances of encountering issues during the migration process and reduces merge conflicts.

### Step 1: Install the Next.js Dependency

The first thing you need to do is to install `next` as a dependency:

```bash filename="Terminal"
npm install next@latest
```

### Step 2: Create the Next.js Configuration File

Create a `next.config.mjs` at the root of your project. This file will hold your
[Next.js configuration options](/docs/app/api-reference/config/next-config-js.md).

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA).
  distDir: './dist', // Changes the build output directory to `./dist/`.
}

export default nextConfig
```

> **Good to know:** You can use either `.js` or `.mjs` for your Next.js configuration file.

### Step 3: Update TypeScript Configuration

If you're using TypeScript, you need to update your `tsconfig.json` file with the following changes
to make it compatible with Next.js. If you're not using TypeScript, you can skip this step.

1. Remove the [project reference](https://www.typescriptlang.org/tsconfig#references) to `tsconfig.node.json`
2. Add `./dist/types/**/*.ts` and `./next-env.d.ts` to the [`include` array](https://www.typescriptlang.org/tsconfig#include)
3. Add `./node_modules` to the [`exclude` array](https://www.typescriptlang.org/tsconfig#exclude)
4. Add `{ "name": "next" }` to the [`plugins` array in `compilerOptions`](https://www.typescriptlang.org/tsconfig#plugins): `"plugins": [{ "name": "next" }]`
5. Set [`esModuleInterop`](https://www.typescriptlang.org/tsconfig#esModuleInterop) to `true`: `"esModuleInterop": true`
6. Set [`jsx`](https://www.typescriptlang.org/tsconfig#jsx) to `react-jsx`: `"jsx": "react-jsx"`
7. Set [`allowJs`](https://www.typescriptlang.org/tsconfig#allowJs) to `true`: `"allowJs": true`
8. Set [`forceConsistentCasingInFileNames`](https://www.typescriptlang.org/tsconfig#forceConsistentCasingInFileNames) to `true`: `"forceConsistentCasingInFileNames": true`
9. Set [`incremental`](https://www.typescriptlang.org/tsconfig#incremental) to `true`: `"incremental": true`

Here's an example of a working `tsconfig.json` with those changes:

```json filename="tsconfig.json"
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "allowJs": true,
    "forceConsistentCasingInFileNames": true,
    "incremental": true,
    "plugins": [{ "name": "next" }]
  },
  "include": ["./src", "./dist/types/**/*.ts", "./next-env.d.ts"],
  "exclude": ["./node_modules"]
}
```

You can find more information about configuring TypeScript on the
[Next.js docs](/docs/app/api-reference/config/typescript.md#ide-plugin).

### Step 4: Create the Root Layout

A Next.js [App Router](/docs/app.md) application must include a
[root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout)
file, which is a [React Server Component](/docs/app/getting-started/server-and-client-components.md)
that will wrap all pages in your application. This file is defined at the top level of the `app`
directory.

The closest equivalent to the root layout file in a Vite application is the
[`index.html` file](https://vitejs.dev/guide/#index-html-and-project-root), which contains your
`<html>`, `<head>`, and `<body>` tags.

In this step, you'll convert your `index.html` file into a root layout file:

1. Create a new `app` directory in your `src` folder.
2. Create a new `layout.tsx` file inside that `app` directory:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return '...'
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return '...'
}
```

> **Good to know**: `.js`, `.jsx`, or `.tsx` extensions can be used for Layout files.

3. Copy the content of your `index.html` file into the previously created `<RootLayout>` component while
   replacing the `body.div#root` and `body.script` tags with `<div id="root">{children}</div>`:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

4. Next.js already includes by default the
   [meta charset](https://developer.mozilla.org/docs/Web/HTML/Element/meta#charset) and
   [meta viewport](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag) tags, so you
   can safely remove those from your `<head>`:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

5. Any [metadata files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata)
   such as `favicon.ico`, `icon.png`, `robots.txt` are automatically added to the application
   `<head>` tag as long as you have them placed into the top level of the `app` directory. After
   moving
   [all supported files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata)
   into the `app` directory you can safely delete their `<link>` tags:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

6. Finally, Next.js can manage your last `<head>` tags with the
   [Metadata API](/docs/app/getting-started/metadata-and-og-images.md). Move your final metadata
   info into an exported
   [`metadata` object](/docs/app/api-reference/functions/generate-metadata.md#metadata-object):

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My App',
  description: 'My App is a...',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'My App',
  description: 'My App is a...',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

With the above changes, you shifted from declaring everything in your `index.html` to using Next.js'
convention-based approach built into the framework
([Metadata API](/docs/app/getting-started/metadata-and-og-images.md)). This approach enables you
to more easily improve your SEO and web shareability of your pages.

### Step 5: Create the Entrypoint Page

On Next.js you declare an entrypoint for your application by creating a `page.tsx` file. The
closest equivalent of this file on Vite is your `main.tsx` file. In this step, you’ll set up the
entrypoint of your application.

1. **Create a `[[...slug]]` directory in your `app` directory.**

Since in this guide we're aiming first to set up our Next.js as an SPA (Single Page Application), you need your page entrypoint to catch all possible routes of your application. For that, create a new `[[...slug]]` directory in your `app` directory.

This directory is what is called an [optional catch-all route segment](/docs/app/api-reference/file-conventions/dynamic-routes.md#optional-catch-all-segments). Next.js uses a file-system based router where folders are used to define routes. This special directory will make sure that all routes of your application will be directed to its containing `page.tsx` file.

2. **Create a new `page.tsx` file inside the `app/[[...slug]]` directory with the following content:**

```tsx filename="app/[[...slug]]/page.tsx" switcher
import '../../index.css'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
import '../../index.css'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

> **Good to know**: `.js`, `.jsx`, or `.tsx` extensions can be used for Page files.

This file is a [Server Component](/docs/app/getting-started/server-and-client-components.md). When you run `next build`, the file is prerendered into a static asset. It does *not* require any dynamic code.

This file imports our global CSS and tells [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) we are only going to generate one route, the index route at `/`.

Now, let's move the rest of our Vite application which will run client-only.

```tsx filename="app/[[...slug]]/client.tsx" switcher
'use client'

import React from 'react'
import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

```jsx filename="app/[[...slug]]/client.js" switcher
'use client'

import React from 'react'
import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

This file is a [Client Component](/docs/app/getting-started/server-and-client-components.md), defined by the `'use client'`
directive. Client Components are still [prerendered to HTML](/docs/app/getting-started/server-and-client-components.md#how-do-server-and-client-components-work-in-nextjs) on the server before being sent to the client.

Since we want a client-only application to start, we can configure Next.js to disable prerendering from the `App` component down.

```tsx
const App = dynamic(() => import('../../App'), { ssr: false })
```

Now, update your entrypoint page to use the new component:

```tsx filename="app/[[...slug]]/page.tsx" switcher
import '../../index.css'
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
import '../../index.css'
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

### Step 6: Update Static Image Imports

Next.js handles static image imports slightly different from Vite. With Vite, importing an image
file will return its public URL as a string:

```tsx filename="App.tsx"
import image from './img.png' // `image` will be '/assets/img.2d8efhg.png' in production

export default function App() {
  return <img src={image} />
}
```

With Next.js, static image imports return an object. The object can then be used directly with the
Next.js [`<Image>` component](/docs/app/api-reference/components/image.md), or you can use the object's
`src` property with your existing `<img>` tag.

The `<Image>` component has the added benefits of
[automatic image optimization](/docs/app/api-reference/components/image.md). The `<Image>`
component automatically sets the `width` and `height` attributes of the resulting `<img>` based on
the image's dimensions. This prevents layout shifts when the image loads. However, this can cause
issues if your app contains images with only one of their dimensions being styled without the other
styled to `auto`. When not styled to `auto`, the dimension will default to the `<img>` dimension
attribute's value, which can cause the image to appear distorted.

Keeping the `<img>` tag will reduce the amount of changes in your application and prevent the above
issues. You can then optionally later migrate to the `<Image>` component to take advantage of optimizing images by [configuring a loader](/docs/app/api-reference/components/image.md#loader), or moving to the default Next.js server which has automatic image optimization.

1. **Convert absolute import paths for images imported from `/public` into relative imports:**

```tsx
// Before
import logo from '/logo.png'

// After
import logo from '../public/logo.png'
```

2. **Pass the image `src` property instead of the whole image object to your `<img>` tag:**

```tsx
// Before
<img src={logo} />

// After
<img src={logo.src} />
```

Alternatively, you can reference the public URL for the image asset based on the filename. For example, `public/logo.png` will serve the image at `/logo.png` for your application, which would be the `src` value.

> **Warning:** If you're using TypeScript, you might encounter type errors when accessing the `src`
> property. You can safely ignore those for now. They will be fixed by the end of this guide.

### Step 7: Migrate the Environment Variables

Next.js has support for `.env`
[environment variables](/docs/app/guides/environment-variables.md)
similar to Vite. The main difference is the prefix used to expose environment variables on the
client-side.

* Change all environment variables with the `VITE_` prefix to `NEXT_PUBLIC_`.

Vite exposes a few built-in environment variables on the special `import.meta.env` object which
aren’t supported by Next.js. You need to update their usage as follows:

* `import.meta.env.MODE` ⇒ `process.env.NODE_ENV`
* `import.meta.env.PROD` ⇒ `process.env.NODE_ENV === 'production'`
* `import.meta.env.DEV` ⇒ `process.env.NODE_ENV !== 'production'`
* `import.meta.env.SSR` ⇒ `typeof window !== 'undefined'`

Next.js also doesn't provide a built-in `BASE_URL` environment variable. However, you can still
configure one, if you need it:

1. **Add the following to your `.env` file:**

```bash filename=".env"
# ...
NEXT_PUBLIC_BASE_PATH="/some-base-path"
```

2. **Set [`basePath`](/docs/app/api-reference/config/next-config-js/basePath.md) to `process.env.NEXT_PUBLIC_BASE_PATH` in your `next.config.mjs` file:**

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA).
  distDir: './dist', // Changes the build output directory to `./dist/`.
  basePath: process.env.NEXT_PUBLIC_BASE_PATH, // Sets the base path to `/some-base-path`.
}

export default nextConfig
```

3. **Update `import.meta.env.BASE_URL` usages to `process.env.NEXT_PUBLIC_BASE_PATH`**

### Step 8: Update Scripts in `package.json`

You should now be able to run your application to test if you successfully migrated to Next.js. But
before that, you need to update your `scripts` in your `package.json` with Next.js related commands,
and add `.next` and `next-env.d.ts` to your `.gitignore`:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

```txt filename=".gitignore"
# ...
.next
next-env.d.ts
dist
```

Now run `npm run dev`, and open [`http://localhost:3000`](http://localhost:3000). You should see your application now running on Next.js.

> **Example:** Check out [this pull request](https://github.com/inngest/vite-to-nextjs/pull/1) for a
> working example of a Vite application migrated to Next.js.

### Step 9: Clean Up

You can now clean up your codebase from Vite related artifacts:

* Delete `main.tsx`
* Delete `index.html`
* Delete `vite-env.d.ts`
* Delete `tsconfig.node.json`
* Delete `vite.config.ts`
* Uninstall Vite dependencies

## Next Steps

If everything went according to plan, you now have a functioning Next.js application running as a
single-page application. However, you aren't yet taking advantage of most of Next.js' benefits, but
you can now start making incremental changes to reap all the benefits. Here's what you might want to
do next:

* Migrate from React Router to the [Next.js App Router](/docs/app.md) to get:
  * Automatic code splitting
  * [Streaming Server-Rendering](/docs/app/api-reference/file-conventions/loading.md)
  * [React Server Components](/docs/app/getting-started/server-and-client-components.md)
* [Optimize images with the `<Image>` component](/docs/app/api-reference/components/image.md)
* [Optimize fonts with `next/font`](/docs/app/api-reference/components/font.md)
* [Optimize third-party scripts with the `<Script>` component](/docs/app/guides/scripts.md)
* [Update your ESLint configuration to support Next.js rules](/docs/app/api-reference/config/eslint.md)


--------------------------------------------------------------------------------
title: "How to build micro-frontends using multi-zones and Next.js"
description: "Learn how to build micro-frontends using Next.js Multi-Zones to deploy multiple Next.js apps under a single domain."
source: "https://nextjs.org/docs/pages/guides/multi-zones"
--------------------------------------------------------------------------------

# Multi-Zones

@router: Pages Router

<details>
<summary>Examples</summary>

* [With Zones](https://github.com/vercel/next.js/tree/canary/examples/with-zones)

</details>

Multi-Zones are an approach to micro-frontends that separate a large application on a domain into smaller Next.js applications that each serve a set of paths. This is useful when there are collections of pages unrelated to the other pages in the application. By moving those pages to a separate zone (i.e., a separate application), you can reduce the size of each application which improves build times and removes code that is only necessary for one of the zones. Since applications are decoupled, Multi-Zones also allows other applications on the domain to use their own choice of framework.

For example, let's say you have the following set of pages that you would like to split up:

* `/blog/*` for all blog posts
* `/dashboard/*` for all pages when the user is logged-in to the dashboard
* `/*` for the rest of your website not covered by other zones

With Multi-Zones support, you can create three applications that all are served on the same domain and look the same to the user, but you can develop and deploy each of the applications independently.

![Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/multi-zones.png)

Navigating between pages in the same zone will perform soft navigations, a navigation that does not require reloading the page. For example, in this diagram, navigating from `/` to `/products` will be a soft navigation.

Navigating from a page in one zone to a page in another zone, such as from `/` to `/dashboard`, will perform a hard navigation, unloading the resources of the current page and loading the resources of the new page. Pages that are frequently visited together should live in the same zone to avoid hard navigations.

## How to define a zone

A zone is a normal Next.js application where you also configure an [assetPrefix](/docs/app/api-reference/config/next-config-js/assetPrefix.md) to avoid conflicts with pages and static files in other zones.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
}
```

Next.js assets, such as JavaScript and CSS, will be prefixed with `assetPrefix` to make sure that they don't conflict with assets from other zones. These assets will be served under `/assetPrefix/_next/...` for each of the zones.

The default application handling all paths not routed to another more specific zone does not need an `assetPrefix`.

In versions older than Next.js 15, you may also need an additional rewrite to handle the static assets. This is no longer necessary in Next.js 15.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
  async rewrites() {
    return {
      beforeFiles: [
        {
          source: '/blog-static/_next/:path+',
          destination: '/_next/:path+',
        },
      ],
    }
  },
}
```

## How to route requests to the right zone

With the Multi Zones set-up, you need to route the paths to the correct zone since they are served by different applications. You can use any HTTP proxy to do this, but one of the Next.js applications can also be used to route requests for the entire domain.

To route to the correct zone using a Next.js application, you can use [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites.md). For each path served by a different zone, you would add a rewrite rule to send that path to the domain of the other zone, and you also need to rewrite the requests for the static assets. For example:

```js filename="next.config.js"
async rewrites() {
    return [
        {
            source: '/blog',
            destination: `${process.env.BLOG_DOMAIN}/blog`,
        },
        {
            source: '/blog/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
        },
        {
            source: '/blog-static/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
        }
    ];
}
```

`destination` should be a URL that is served by the zone, including scheme and domain. This should point to the zone's production domain, but it can also be used to route requests to `localhost` in local development.

> **Good to know**: URL paths should be unique to a zone. For example, two zones trying to serve `/blog` would create a routing conflict.

### Routing requests using proxy

Routing requests through [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites.md) is recommended to minimize latency overhead for the requests, but proxy can also be used when there is a need for a dynamic decision when routing. For example, if you are using a feature flag to decide where a path should be routed such as during a migration, you can use proxy.

```js filename="proxy.js"
export async function proxy(request) {
  const { pathname, search } = req.nextUrl;
  if (pathname === '/your-path' && myFeatureFlag.isEnabled()) {
    return NextResponse.rewrite(`${rewriteDomain}${pathname}${search});
  }
}
```

## Linking between zones

Links to paths in a different zone should use an `a` tag instead of the Next.js [`<Link>`](/docs/pages/api-reference/components/link.md) component. This is because Next.js will try to prefetch and soft navigate to any relative path in `<Link>` component, which will not work across zones.

## Sharing code

The Next.js applications that make up the different zones can live in any repository. However, it is often convenient to put these zones in a [monorepo](https://en.wikipedia.org/wiki/Monorepo) to more easily share code. For zones that live in different repositories, code can also be shared using public or private NPM packages.

Since the pages in different zones may be released at different times, feature flags can be useful for enabling or disabling features in unison across the different zones.


--------------------------------------------------------------------------------
title: "How to set up instrumentation with OpenTelemetry"
description: "Learn how to instrument your Next.js app with OpenTelemetry."
source: "https://nextjs.org/docs/pages/guides/open-telemetry"
--------------------------------------------------------------------------------

# OpenTelemetry

@router: Pages Router

Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app.

As applications become more complex, it becomes increasingly difficult to identify and diagnose issues that may arise. By leveraging observability tools, such as logging and metrics, developers can gain insights into their application's behavior and identify areas for optimization. With observability, developers can proactively address issues before they become major problems and provide a better user experience. Therefore, it is highly recommended to use observability in your Next.js applications to improve performance, optimize resources, and enhance user experience.

We recommend using OpenTelemetry for instrumenting your apps.
It's a platform-agnostic way to instrument apps that allows you to change your observability provider without changing your code.
Read [Official OpenTelemetry docs](https://opentelemetry.io/docs/) for more information about OpenTelemetry and how it works.

This documentation uses terms like *Span*, *Trace* or *Exporter* throughout this doc, all of which can be found in [the OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/).

Next.js supports OpenTelemetry instrumentation out of the box, which means that we already instrumented Next.js itself.

When you enable OpenTelemetry we will automatically wrap all your code like
`getStaticProps` in *spans* with helpful attributes.

## Getting Started

OpenTelemetry is extensible but setting it up properly can be quite verbose.
That's why we prepared a package `@vercel/otel` that helps you get started quickly.

### Using `@vercel/otel`

To get started, install the following packages:

```bash filename="Terminal"
npm install @vercel/otel @opentelemetry/sdk-logs @opentelemetry/api-logs @opentelemetry/instrumentation
```

Next, create a custom [`instrumentation.ts`](/docs/pages/guides/instrumentation.md) (or `.js`) file in the **root directory** of the project (or inside `src` folder if using one):

```ts filename="your-project/instrumentation.ts" switcher
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel({ serviceName: 'next-app' })
}
```

```js filename="your-project/instrumentation.js" switcher
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel({ serviceName: 'next-app' })
}
```

See the [`@vercel/otel` documentation](https://www.npmjs.com/package/@vercel/otel) for additional configuration options.

> **Good to know**:
>
> * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
> * If you use the [`pageExtensions` config option](/docs/pages/api-reference/config/next-config-js/pageExtensions.md) to add a suffix, you will also need to update the `instrumentation` filename to match.
> * We have created a basic [with-opentelemetry](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry) example that you can use.

### Manual OpenTelemetry configuration

The `@vercel/otel` package provides many configuration options and should serve most of common use cases. But if it doesn't suit your needs, you can configure OpenTelemetry manually.

Firstly you need to install OpenTelemetry packages:

```bash filename="Terminal"
npm install @opentelemetry/sdk-node @opentelemetry/resources @opentelemetry/semantic-conventions @opentelemetry/sdk-trace-node @opentelemetry/exporter-trace-otlp-http
```

Now you can initialize `NodeSDK` in your `instrumentation.ts`.
Unlike `@vercel/otel`, `NodeSDK` is not compatible with edge runtime, so you need to make sure that you are importing them only when `process.env.NEXT_RUNTIME === 'nodejs'`. We recommend creating a new file `instrumentation.node.ts` which you conditionally import only when using node:

```ts filename="instrumentation.ts" switcher
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation.node.ts')
  }
}
```

```js filename="instrumentation.js" switcher
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation.node.js')
  }
}
```

```ts filename="instrumentation.node.ts" switcher
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
import { resourceFromAttributes } from '@opentelemetry/resources'
import { NodeSDK } from '@opentelemetry/sdk-node'
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'

const sdk = new NodeSDK({
  resource: resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'next-app',
  }),
  spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
})
sdk.start()
```

```js filename="instrumentation.node.js" switcher
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
import { resourceFromAttributes } from '@opentelemetry/resources'
import { NodeSDK } from '@opentelemetry/sdk-node'
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'

const sdk = new NodeSDK({
  resource: resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'next-app',
  }),
  spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
})
sdk.start()
```

Doing this is equivalent to using `@vercel/otel`, but it's possible to modify and extend some features that are not exposed by the `@vercel/otel`. If edge runtime support is necessary, you will have to use `@vercel/otel`.

## Testing your instrumentation

You need an OpenTelemetry collector with a compatible backend to test OpenTelemetry traces locally.
We recommend using our [OpenTelemetry dev environment](https://github.com/vercel/opentelemetry-collector-dev-setup).

If everything works well you should be able to see the root server span labeled as `GET /requested/pathname`.
All other spans from that particular trace will be nested under it.

Next.js traces more spans than are emitted by default.
To see more spans, you must set `NEXT_OTEL_VERBOSE=1`.

## Deployment

### Using OpenTelemetry Collector

When you are deploying with OpenTelemetry Collector, you can use `@vercel/otel`.
It will work both on Vercel and when self-hosted.

#### Deploying on Vercel

We made sure that OpenTelemetry works out of the box on Vercel.

Follow [Vercel documentation](https://vercel.com/docs/concepts/observability/otel-overview/quickstart) to connect your project to an observability provider.

#### Self-hosting

Deploying to other platforms is also straightforward. You will need to spin up your own OpenTelemetry Collector to receive and process the telemetry data from your Next.js app.

To do this, follow the [OpenTelemetry Collector Getting Started guide](https://opentelemetry.io/docs/collector/getting-started/), which will walk you through setting up the collector and configuring it to receive data from your Next.js app.

Once you have your collector up and running, you can deploy your Next.js app to your chosen platform following their respective deployment guides.

### Custom Exporters

OpenTelemetry Collector is not necessary. You can use a custom OpenTelemetry exporter with [`@vercel/otel`](#using-vercelotel) or [manual OpenTelemetry configuration](#manual-opentelemetry-configuration).

## Custom Spans

You can add a custom span with [OpenTelemetry APIs](https://opentelemetry.io/docs/instrumentation/js/instrumentation).

```bash filename="Terminal"
npm install @opentelemetry/api
```

The following example demonstrates a function that fetches GitHub stars and adds a custom `fetchGithubStars` span to track the fetch request's result:

```ts
import { trace } from '@opentelemetry/api'

export async function fetchGithubStars() {
  return await trace
    .getTracer('nextjs-example')
    .startActiveSpan('fetchGithubStars', async (span) => {
      try {
        return await getValue()
      } finally {
        span.end()
      }
    })
}
```

The `register` function will execute before your code runs in a new environment.
You can start creating new spans, and they should be correctly added to the exported trace.

## Default Spans in Next.js

Next.js automatically instruments several spans for you to provide useful insights into your application's performance.

Attributes on spans follow [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/). We also add some custom attributes under the `next` namespace:

* `next.span_name` - duplicates span name
* `next.span_type` - each span type has a unique identifier
* `next.route` - The route pattern of the request (e.g., `/[param]/user`).
* `next.rsc` (true/false) - Whether the request is an RSC request, such as prefetch.
* `next.page`
  * This is an internal value used by an app router.
  * You can think about it as a route to a special file (like `page.ts`, `layout.ts`, `loading.ts` and others)
  * It can be used as a unique identifier only when paired with `next.route` because `/layout` can be used to identify both `/(groupA)/layout.ts` and `/(groupB)/layout.ts`

### `[http.method] [next.route]`

* `next.span_type`: `BaseServer.handleRequest`

This span represents the root span for each incoming request to your Next.js application. It tracks the HTTP method, route, target, and status code of the request.

Attributes:

* [Common HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#common-attributes)
  * `http.method`
  * `http.status_code`
* [Server HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#http-server-semantic-conventions)
  * `http.route`
  * `http.target`
* `next.span_name`
* `next.span_type`
* `next.route`

### `render route (app) [next.route]`

* `next.span_type`: `AppRender.getBodyResult`.

This span represents the process of rendering a route in the app router.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `fetch [http.method] [http.url]`

* `next.span_type`: `AppRender.fetch`

This span represents the fetch request executed in your code.

Attributes:

* [Common HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#common-attributes)
  * `http.method`
* [Client HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#http-client)
  * `http.url`
  * `net.peer.name`
  * `net.peer.port` (only if specified)
* `next.span_name`
* `next.span_type`

This span can be turned off by setting `NEXT_OTEL_FETCH_DISABLED=1` in your environment. This is useful when you want to use a custom fetch instrumentation library.

### `executing api route (app) [next.route]`

* `next.span_type`: `AppRouteRouteHandlers.runHandler`.

This span represents the execution of an API Route Handler in the app router.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `getServerSideProps [next.route]`

* `next.span_type`: `Render.getServerSideProps`.

This span represents the execution of `getServerSideProps` for a specific route.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `getStaticProps [next.route]`

* `next.span_type`: `Render.getStaticProps`.

This span represents the execution of `getStaticProps` for a specific route.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `render route (pages) [next.route]`

* `next.span_type`: `Render.renderDocument`.

This span represents the process of rendering the document for a specific route.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `generateMetadata [next.page]`

* `next.span_type`: `ResolveMetadata.generateMetadata`.

This span represents the process of generating metadata for a specific page (a single route can have multiple of these spans).

Attributes:

* `next.span_name`
* `next.span_type`
* `next.page`

### `resolve page components`

* `next.span_type`: `NextNodeServer.findPageComponents`.

This span represents the process of resolving page components for a specific page.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `resolve segment modules`

* `next.span_type`: `NextNodeServer.getLayoutOrPageModule`.

This span represents loading of code modules for a layout or a page.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.segment`

### `start response`

* `next.span_type`: `NextNodeServer.startResponse`.

This zero-length span represents the time when the first byte has been sent in the response.


--------------------------------------------------------------------------------
title: "How to optimize package bundling"
description: "Learn how to optimize your application's server and client bundles."
source: "https://nextjs.org/docs/pages/guides/package-bundling"
--------------------------------------------------------------------------------

# Package Bundling

@router: Pages Router

Bundling external packages can significantly improve the performance of your application.  By default, packages imported into your application are not bundled. This can impact performance or might not work if external packages are not pre-bundled, for example, if imported from a monorepo or `node_modules`. This page will guide you through how to analyze and configure package bundling.

## Analyzing JavaScript bundles

[`@next/bundle-analyzer`](https://www.npmjs.com/package/@next/bundle-analyzer) is a plugin for Next.js that helps you manage the size of your application bundles. It generates a visual report of the size of each package and their dependencies. You can use the information to remove large dependencies, split, or [lazy-load](/docs/app/guides/lazy-loading.md) your code.

### Installation

Install the plugin by running the following command:

```bash
npm i @next/bundle-analyzer
# or
yarn add @next/bundle-analyzer
# or
pnpm add @next/bundle-analyzer
```

Then, add the bundle analyzer's settings to your `next.config.js`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {}

const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer(nextConfig)
```

### Generating a report

Run the following command to analyze your bundles:

```bash
ANALYZE=true npm run build
# or
ANALYZE=true yarn build
# or
ANALYZE=true pnpm build
```

The report will open three new tabs in your browser, which you can inspect. Periodically evaluating your application's bundles can help you maintain application performance over time.

## Optimizing package imports

Some packages, such as icon libraries, can export hundreds of modules, which can cause performance issues in development and production.

You can optimize how these packages are imported by adding the [`optimizePackageImports`](/docs/app/api-reference/config/next-config-js/optimizePackageImports.md) option to your `next.config.js`. This option will only load the modules you *actually* use, while still giving you the convenience of writing import statements with many named exports.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    optimizePackageImports: ['icon-library'],
  },
}

module.exports = nextConfig
```

Next.js also optimizes some libraries automatically, thus they do not need to be included in the optimizePackageImports list. See the [full list](/docs/app/api-reference/config/next-config-js/optimizePackageImports.md).

## Bundling specific packages

To bundle specific packages, you can use the [`transpilePackages`](/docs/app/api-reference/config/next-config-js/transpilePackages.md) option in your `next.config.js`. This option is useful for bundling external packages that are not pre-bundled, for example, in a monorepo or imported from `node_modules`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ['package-name'],
}

module.exports = nextConfig
```

## Bundling all packages

To automatically bundle all packages (default behavior in the App Router), you can use the [`bundlePagesRouterDependencies`](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies.md) option in your `next.config.js`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  bundlePagesRouterDependencies: true,
}

module.exports = nextConfig
```

## Opting specific packages out of bundling

If you have the [`bundlePagesRouterDependencies`](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies.md) option enabled, you can opt specific packages out of automatic bundling using the [`serverExternalPackages`](/docs/pages/api-reference/config/next-config-js/serverExternalPackages.md) option in your `next.config.js`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Automatically bundle external packages in the Pages Router:
  bundlePagesRouterDependencies: true,
  // Opt specific packages out of bundling for both App and Pages Router:
  serverExternalPackages: ['package-name'],
}

module.exports = nextConfig
```


Learn more about optimizing your application for production.

- [Production](/docs/app/guides/production-checklist.md)
  - Recommendations to ensure the best performance and user experience before taking your Next.js application to production.


--------------------------------------------------------------------------------
title: "How to configure PostCSS in Next.js"
description: "Extend the PostCSS config and plugins added by Next.js with your own."
source: "https://nextjs.org/docs/pages/guides/post-css"
--------------------------------------------------------------------------------

# PostCSS

@router: Pages Router

## Default Behavior

Next.js compiles CSS for its [built-in CSS support](/docs/app/getting-started/css.md) using PostCSS.

Out of the box, with no configuration, Next.js compiles CSS with the following transformations:

* [Autoprefixer](https://github.com/postcss/autoprefixer) automatically adds vendor prefixes to CSS rules (back to IE11).
* [Cross-browser Flexbox bugs](https://github.com/philipwalton/flexbugs) are corrected to behave like [the spec](https://www.w3.org/TR/css-flexbox-1/).
* New CSS features are automatically compiled for Internet Explorer 11 compatibility:
  * [`all` Property](https://developer.mozilla.org/docs/Web/CSS/all)
  * [Break Properties](https://developer.mozilla.org/docs/Web/CSS/break-after)
  * [`font-variant` Property](https://developer.mozilla.org/docs/Web/CSS/font-variant)
  * [Gap Properties](https://developer.mozilla.org/docs/Web/CSS/gap)
  * [Media Query Ranges](https://developer.mozilla.org/docs/Web/CSS/Media_Queries/Using_media_queries#Syntax_improvements_in_Level_4)

By default, [CSS Grid](https://www.w3.org/TR/css-grid-1/) and [Custom Properties](https://developer.mozilla.org/docs/Web/CSS/var) (CSS variables) are **not compiled** for IE11 support.

To compile [CSS Grid Layout](https://developer.mozilla.org/docs/Web/CSS/grid) for IE11, you can place the following comment at the top of your CSS file:

```css
/* autoprefixer grid: autoplace */
```

You can also enable IE11 support for [CSS Grid Layout](https://developer.mozilla.org/docs/Web/CSS/grid)
in your entire project by configuring autoprefixer with the configuration shown below (collapsed).
See ["Customizing Plugins"](#customizing-plugins) below for more information.

<details>
<summary>Click to view the configuration to enable CSS Grid Layout</summary>

```json filename="postcss.config.json"
{
  "plugins": [
    "postcss-flexbugs-fixes",
    [
      "postcss-preset-env",
      {
        "autoprefixer": {
          "flexbox": "no-2009",
          "grid": "autoplace"
        },
        "stage": 3,
        "features": {
          "custom-properties": false
        }
      }
    ]
  ]
}
```

</details>

CSS variables are not compiled because it is [not possible to safely do so](https://github.com/MadLittleMods/postcss-css-variables#caveats).
If you must use variables, consider using something like [Sass variables](https://sass-lang.com/documentation/variables) which are compiled away by [Sass](https://sass-lang.com/).

## Customizing Target Browsers

Next.js allows you to configure the target browsers (for [Autoprefixer](https://github.com/postcss/autoprefixer) and compiled css features) through [Browserslist](https://github.com/browserslist/browserslist).

To customize browserslist, create a `browserslist` key in your `package.json` like so:

```json filename="package.json"
{
  "browserslist": [">0.3%", "not dead", "not op_mini all"]
}
```

You can use the [browsersl.ist](https://browsersl.ist/?q=%3E0.3%25%2C+not+ie+11%2C+not+dead%2C+not+op_mini+all) tool to visualize what browsers you are targeting.

## CSS Modules

No configuration is needed to support CSS Modules. To enable CSS Modules for a file, rename the file to have the extension `.module.css`.

You can learn more about [Next.js' CSS Module support here](/docs/app/getting-started/css.md).

## Customizing Plugins

> **Warning**: When you define a custom PostCSS configuration file, Next.js **completely disables** the [default behavior](#default-behavior).
> Be sure to manually configure all the features you need compiled, including [Autoprefixer](https://github.com/postcss/autoprefixer).
> You also need to install any plugins included in your custom configuration manually, i.e. `npm install postcss-flexbugs-fixes postcss-preset-env`.

To customize the PostCSS configuration, create a `postcss.config.json` file in the root of your project.

This is the default configuration used by Next.js:

```json filename="postcss.config.json"
{
  "plugins": [
    "postcss-flexbugs-fixes",
    [
      "postcss-preset-env",
      {
        "autoprefixer": {
          "flexbox": "no-2009"
        },
        "stage": 3,
        "features": {
          "custom-properties": false
        }
      }
    ]
  ]
}
```

> **Good to know**: Next.js also allows the file to be named `.postcssrc.json`, or, to be read from the `postcss` key in `package.json`.

It is also possible to configure PostCSS with a `postcss.config.js` file, which is useful when you want to conditionally include plugins based on environment:

```js filename="postcss.config.js"
module.exports = {
  plugins:
    process.env.NODE_ENV === 'production'
      ? [
          'postcss-flexbugs-fixes',
          [
            'postcss-preset-env',
            {
              autoprefixer: {
                flexbox: 'no-2009',
              },
              stage: 3,
              features: {
                'custom-properties': false,
              },
            },
          ],
        ]
      : [
          // No transformations in development
        ],
}
```

> **Good to know**: Next.js also allows the file to be named `.postcssrc.js`.

Do **not use `require()`** to import the PostCSS Plugins. Plugins must be provided as strings.

> **Good to know**: If your `postcss.config.js` needs to support other non-Next.js tools in the same project, you must use the interoperable object-based format instead:
>
> ```js
> module.exports = {
>   plugins: {
>     'postcss-flexbugs-fixes': {},
>     'postcss-preset-env': {
>       autoprefixer: {
>         flexbox: 'no-2009',
>       },
>       stage: 3,
>       features: {
>         'custom-properties': false,
>       },
>     },
>   },
> }
> ```


--------------------------------------------------------------------------------
title: "How to preview content with Preview Mode in Next.js"
description: "Next.js has the preview mode for statically generated pages. You can learn how it works here."
source: "https://nextjs.org/docs/pages/guides/preview-mode"
--------------------------------------------------------------------------------

# Preview Mode

@router: Pages Router

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

> **Note**: This feature is superseded by [Draft Mode](/docs/pages/guides/draft-mode.md).

<details>
<summary>Examples</summary>

* [Agility CMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-agilitycms) ([Demo](https://next-blog-agilitycms.vercel.app/))
* [Builder.io Example](https://github.com/vercel/next.js/tree/canary/examples/cms-builder-io) ([Demo](https://cms-builder-io.vercel.app/))
* [ButterCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-buttercms) ([Demo](https://next-blog-buttercms.vercel.app/))
* [Contentful Example](https://github.com/vercel/next.js/tree/canary/examples/cms-contentful) ([Demo](https://app-router-contentful.vercel.app/))
* [Cosmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-cosmic) ([Demo](https://next-blog-cosmic.vercel.app/))
* [DatoCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-datocms) ([Demo](https://next-blog-datocms.vercel.app/))
* [DotCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-dotcms) ([Demo](https://nextjs-dotcms-blog.vercel.app/))
* [Drupal Example](https://github.com/vercel/next.js/tree/canary/examples/cms-drupal) ([Demo](https://cms-drupal.vercel.app/))
* [Enterspeed Example](https://github.com/vercel/next.js/tree/canary/examples/cms-enterspeed) ([Demo](https://next-blog-demo.enterspeed.com/))
* [GraphCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-graphcms) ([Demo](https://next-blog-graphcms.vercel.app/))
* [Keystone Example](https://github.com/vercel/next.js/tree/canary/examples/cms-keystonejs-embedded) ([Demo](https://nextjs-keystone-demo.vercel.app/))
* [Kontent.ai Example](https://github.com/vercel/next.js/tree/canary/examples/cms-kontent-ai) ([Demo](https://next-blog-kontent-ai.vercel.app/))
* [Makeswift Example](https://github.com/vercel/next.js/tree/canary/examples/cms-makeswift) ([Demo](https://nextjs-makeswift-example.vercel.app/))
* [Plasmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-plasmic) ([Demo](https://nextjs-plasmic-example.vercel.app/))
* [Prepr Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prepr) ([Demo](https://next-blog-prepr.vercel.app/))
* [Prismic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prismic) ([Demo](https://next-blog-prismic.vercel.app/))
* [Sanity Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sanity) ([Demo](https://next-blog.sanity.build/))
* [Sitecore XM Cloud Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sitecore-xmcloud) ([Demo](https://vercel-sitecore-xmcloud-demo.vercel.app/))
* [Storyblok Example](https://github.com/vercel/next.js/tree/canary/examples/cms-storyblok) ([Demo](https://next-blog-storyblok.vercel.app/))
* [Strapi Example](https://github.com/vercel/next.js/tree/canary/examples/cms-strapi) ([Demo](https://next-blog-strapi.vercel.app/))
* [TakeShape Example](https://github.com/vercel/next.js/tree/canary/examples/cms-takeshape) ([Demo](https://next-blog-takeshape.vercel.app/))
* [Tina Example](https://github.com/vercel/next.js/tree/canary/examples/cms-tina) ([Demo](https://cms-tina-example.vercel.app/))
* [Umbraco Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco) ([Demo](https://nextjs-umbraco-sample-blog.vercel.app/))
* [Umbraco Heartcore Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco-heartcore) ([Demo](https://next-blog-umbraco-heartcore.vercel.app/))
* [Webiny Example](https://github.com/vercel/next.js/tree/canary/examples/cms-webiny) ([Demo](https://webiny-headlesscms-nextjs-example.vercel.app/))
* [WordPress Example](https://github.com/vercel/next.js/tree/canary/examples/cms-wordpress) ([Demo](https://next-blog-wordpress.vercel.app/))
* [Blog Starter Example](https://github.com/vercel/next.js/tree/canary/examples/blog-starter) ([Demo](https://next-blog-starter.vercel.app/))

</details>

In the [Pages documentation](/docs/pages/building-your-application/routing/pages-and-layouts.md) and the [Data Fetching documentation](/docs/pages/building-your-application/data-fetching.md), we talked about how to pre-render a page at build time (**Static Generation**) using `getStaticProps` and `getStaticPaths`.

Static Generation is useful when your pages fetch data from a headless CMS. However, it’s not ideal when you’re writing a draft on your headless CMS and want to **preview** the draft immediately on your page. You’d want Next.js to render these pages at **request time** instead of build time and fetch the draft content instead of the published content. You’d want Next.js to bypass Static Generation only for this specific case.

Next.js has a feature called **Preview Mode** which solves this problem. Here are instructions on how to use it.

## Step 1: Create and access a preview API route

> Take a look at the [API Routes documentation](/docs/pages/building-your-application/routing/api-routes.md) first if you’re not familiar with Next.js API Routes.

First, create a **preview API route**. It can have any name - e.g. `pages/api/preview.js` (or `.ts` if using TypeScript).

In this API route, you need to call `setPreviewData` on the response object. The argument for `setPreviewData` should be an object, and this can be used by `getStaticProps` (more on this later). For now, we’ll use `{}`.

```js
export default function handler(req, res) {
  // ...
  res.setPreviewData({})
  // ...
}
```

`res.setPreviewData` sets some **cookies** on the browser which turns on the preview mode. Any requests to Next.js containing these cookies will be considered as the **preview mode**, and the behavior for statically generated pages will change (more on this later).

You can test this manually by creating an API route like below and accessing it from your browser manually:

```js filename="pages/api/preview.js"
// simple example for testing it manually from your browser.
export default function handler(req, res) {
  res.setPreviewData({})
  res.end('Preview mode enabled')
}
```

If you open your browser’s developer tools and visit `/api/preview`, you’ll notice that the `__prerender_bypass` and `__next_preview_data` cookies will be set on this request.

### Securely accessing it from your Headless CMS

In practice, you’d want to call this API route *securely* from your headless CMS. The specific steps will vary depending on which headless CMS you’re using, but here are some common steps you could take.

These steps assume that the headless CMS you’re using supports setting **custom preview URLs**. If it doesn’t, you can still use this method to secure your preview URLs, but you’ll need to construct and access the preview URL manually.

**First**, you should create a **secret token string** using a token generator of your choice. This secret will only be known by your Next.js app and your headless CMS. This secret prevents people who don’t have access to your CMS from accessing preview URLs.

**Second**, if your headless CMS supports setting custom preview URLs, specify the following as the preview URL. This assumes that your preview API route is located at `pages/api/preview.js`.

```bash filename="Terminal"
https://<your-site>/api/preview?secret=<token>&slug=<path>
```

* `<your-site>` should be your deployment domain.
* `<token>` should be replaced with the secret token you generated.
* `<path>` should be the path for the page that you want to preview. If you want to preview `/posts/foo`, then you should use `&slug=/posts/foo`.

Your headless CMS might allow you to include a variable in the preview URL so that `<path>` can be set dynamically based on the CMS’s data like so: `&slug=/posts/{entry.fields.slug}`

**Finally**, in the preview API route:

* Check that the secret matches and that the `slug` parameter exists (if not, the request should fail).
*
* Call `res.setPreviewData`.
* Then redirect the browser to the path specified by `slug`. (The following example uses a [307 redirect](https://developer.mozilla.org/docs/Web/HTTP/Status/307)).

```js
export default async (req, res) => {
  // Check the secret and next parameters
  // This secret should only be known to this API route and the CMS
  if (req.query.secret !== 'MY_SECRET_TOKEN' || !req.query.slug) {
    return res.status(401).json({ message: 'Invalid token' })
  }

  // Fetch the headless CMS to check if the provided `slug` exists
  // getPostBySlug would implement the required fetching logic to the headless CMS
  const post = await getPostBySlug(req.query.slug)

  // If the slug doesn't exist prevent preview mode from being enabled
  if (!post) {
    return res.status(401).json({ message: 'Invalid slug' })
  }

  // Enable Preview Mode by setting the cookies
  res.setPreviewData({})

  // Redirect to the path from the fetched post
  // We don't redirect to req.query.slug as that might lead to open redirect vulnerabilities
  res.redirect(post.slug)
}
```

If it succeeds, then the browser will be redirected to the path you want to preview with the preview mode cookies being set.

## Step 2: Update `getStaticProps`

The next step is to update `getStaticProps` to support the preview mode.

If you request a page which has `getStaticProps` with the preview mode cookies set (via `res.setPreviewData`), then `getStaticProps` will be called at **request time** (instead of at build time).

Furthermore, it will be called with a `context` object where:

* `context.preview` will be `true`.
* `context.previewData` will be the same as the argument used for `setPreviewData`.

```js
export async function getStaticProps(context) {
  // If you request this page with the preview mode cookies set:
  //
  // - context.preview will be true
  // - context.previewData will be the same as
  //   the argument used for `setPreviewData`.
}
```

We used `res.setPreviewData({})` in the preview API route, so `context.previewData` will be `{}`. You can use this to pass session information from the preview API route to `getStaticProps` if necessary.

If you’re also using `getStaticPaths`, then `context.params` will also be available.

### Fetch preview data

You can update `getStaticProps` to fetch different data based on `context.preview` and/or `context.previewData`.

For example, your headless CMS might have a different API endpoint for draft posts. If so, you can use `context.preview` to modify the API endpoint URL like below:

```js
export async function getStaticProps(context) {
  // If context.preview is true, append "/preview" to the API endpoint
  // to request draft data instead of published data. This will vary
  // based on which headless CMS you're using.
  const res = await fetch(`https://.../${context.preview ? 'preview' : ''}`)
  // ...
}
```

That’s it! If you access the preview API route (with `secret` and `slug`) from your headless CMS or manually, you should now be able to see the preview content. And if you update your draft without publishing, you should be able to preview the draft.

Set this as the preview URL on your headless CMS or access manually, and you should be able to see the preview.

```bash filename="Terminal"
https://<your-site>/api/preview?secret=<token>&slug=<path>
```

## More Details

> **Good to know**: during rendering `next/router` exposes an `isPreview` flag, see the [router object docs](/docs/pages/api-reference/functions/use-router.md#router-object) for more info.

### Specify the Preview Mode duration

`setPreviewData` takes an optional second parameter which should be an options object. It accepts the following keys:

* `maxAge`: Specifies the number (in seconds) for the preview session to last for.
* `path`: Specifies the path the cookie should be applied under. Defaults to `/` enabling preview mode for all paths.

```js
setPreviewData(data, {
  maxAge: 60 * 60, // The preview mode cookies expire in 1 hour
  path: '/about', // The preview mode cookies apply to paths with /about
})
```

### Clear the Preview Mode cookies

By default, no expiration date is set for Preview Mode cookies, so the preview session ends when the browser is closed.

To clear the Preview Mode cookies manually, create an API route that calls `clearPreviewData()`:

```js filename="pages/api/clear-preview-mode-cookies.js"
export default function handler(req, res) {
  res.clearPreviewData({})
}
```

Then, send a request to `/api/clear-preview-mode-cookies` to invoke the API Route. If calling this route using [`next/link`](/docs/pages/api-reference/components/link.md), you must pass `prefetch={false}` to prevent calling `clearPreviewData` during link prefetching.

If a path was specified in the `setPreviewData` call, you must pass the same path to `clearPreviewData`:

```js filename="pages/api/clear-preview-mode-cookies.js"
export default function handler(req, res) {
  const { path } = req.query

  res.clearPreviewData({ path })
}
```

### `previewData` size limits

You can pass an object to `setPreviewData` and have it be available in `getStaticProps`. However, because the data will be stored in a cookie, there’s a size limitation. Currently, preview data is limited to 2KB.

### Works with `getServerSideProps`

The preview mode works on `getServerSideProps` as well. It will also be available on the `context` object containing `preview` and `previewData`.

> **Good to know**: You shouldn't set the `Cache-Control` header when using Preview Mode because it cannot be bypassed. Instead, we recommend using [ISR](/docs/pages/guides/incremental-static-regeneration.md).

### Works with API Routes

API Routes will have access to `preview` and `previewData` under the request object. For example:

```js
export default function myApiRoute(req, res) {
  const isPreview = req.preview
  const previewData = req.previewData
  // ...
}
```

### Unique per `next build`

Both the bypass cookie value and the private key for encrypting the `previewData` change when `next build` is completed.
This ensures that the bypass cookie can’t be guessed.

> **Good to know**: To test Preview Mode locally over HTTP your browser will need to allow third-party cookies and local storage access.


--------------------------------------------------------------------------------
title: "How to optimize your Next.js application for production"
description: "Recommendations to ensure the best performance and user experience before taking your Next.js application to production."
source: "https://nextjs.org/docs/pages/guides/production-checklist"
--------------------------------------------------------------------------------

# Production

@router: Pages Router

Before taking your Next.js application to production, there are some optimizations and patterns you should consider implementing for the best user experience, performance, and security.

This page provides best practices that you can use as a reference when [building your application](#during-development) and [before going to production](#before-going-to-production), as well as the [automatic Next.js optimizations](#automatic-optimizations) you should be aware of.

## Automatic optimizations

These Next.js optimizations are enabled by default and require no configuration:

* **[Code-splitting](/docs/pages/building-your-application/routing/pages-and-layouts.md):** Next.js automatically code-splits your application code by pages. This means only the code needed for the current page is loaded on navigation. You may also consider [lazy loading](/docs/pages/guides/lazy-loading.md) third-party libraries, where appropriate.
* **[Prefetching](/docs/pages/api-reference/components/link.md#prefetch):** When a link to a new route enters the user's viewport, Next.js prefetches the route in background. This makes navigation to new routes almost instant. You can opt out of prefetching, where appropriate.
* **[Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization.md):** Next.js automatically determines that a page is static (can be pre-rendered) if it has no blocking data requirements. Optimized pages can be cached, and served to the end-user from multiple CDN locations. You may opt into [Server-side Rendering](/docs/pages/building-your-application/data-fetching/get-server-side-props.md), where appropriate.

These defaults aim to improve your application's performance, and reduce the cost and amount of data transferred on each network request.

## During development

While building your application, we recommend using the following features to ensure the best performance and user experience:

### Routing and rendering

* **[`<Link>` component](/docs/pages/building-your-application/routing/linking-and-navigating.md):** Use the `<Link>` component for client-side navigation and prefetching.
* **[Custom Errors](/docs/pages/building-your-application/routing/custom-error.md):** Gracefully handle [500](/docs/pages/building-your-application/routing/custom-error.md#500-page) and [404 errors](/docs/pages/building-your-application/routing/custom-error.md#404-page)

### Data fetching and caching

* **[API Routes](/docs/pages/building-your-application/routing/api-routes.md):** Use Route Handlers to access your backend resources, and prevent sensitive secrets from being exposed to the client.
* **[Data Caching](/docs/pages/building-your-application/data-fetching/get-static-props.md):** Verify whether your data requests are being cached or not, and opt into caching, where appropriate. Ensure requests that don't use `getStaticProps` are cached where appropriate.
* **[Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md):** Use Incremental Static Regeneration to update static pages after they've been built, without rebuilding your entire site.
* **[Static Images](/docs/pages/api-reference/file-conventions/public-folder.md):** Use the `public` directory to automatically cache your application's static assets, e.g. images.

### UI and accessibility

* **[Font Module](/docs/app/api-reference/components/font.md):** Optimize fonts by using the Font Module, which automatically hosts your font files with other static assets, removes external network requests, and reduces [layout shift](https://web.dev/articles/cls).
* **[`<Image>` Component](/docs/app/api-reference/components/image.md):** Optimize images by using the Image Component, which automatically optimizes images, prevents layout shift, and serves them in modern formats like WebP.
* **[`<Script>` Component](/docs/app/guides/scripts.md):** Optimize third-party scripts by using the Script Component, which automatically defers scripts and prevents them from blocking the main thread.
* **[ESLint](/docs/architecture/accessibility.md#linting):** Use the built-in `eslint-plugin-jsx-a11y` plugin to catch accessibility issues early.

### Security

* **[Environment Variables](/docs/app/guides/environment-variables.md):** Ensure your `.env.*` files are added to `.gitignore` and only public variables are prefixed with `NEXT_PUBLIC_`.
* **[Content Security Policy](/docs/app/guides/content-security-policy.md):** Consider adding a Content Security Policy to protect your application against various security threats such as cross-site scripting, clickjacking, and other code injection attacks.

### Metadata and SEO

* **[`<Head>` Component](/docs/pages/api-reference/components/head.md):** Use the `next/head` component to add page titles, descriptions, and more.

### Type safety

* **TypeScript and [TS Plugin](/docs/app/api-reference/config/typescript.md):** Use TypeScript and the TypeScript plugin for better type-safety, and to help you catch errors early.

## Before going to production

Before going to production, you can run `next build` to build your application locally and catch any build errors, then run `next start` to measure the performance of your application in a production-like environment.

### Core Web Vitals

* **[Lighthouse](https://developers.google.com/web/tools/lighthouse):** Run lighthouse in incognito to gain a better understanding of how your users will experience your site, and to identify areas for improvement. This is a simulated test and should be paired with looking at field data (such as Core Web Vitals).

### Analyzing bundles

Use the [`@next/bundle-analyzer` plugin](/docs/app/guides/package-bundling.md#analyzing-javascript-bundles) to analyze the size of your JavaScript bundles and identify large modules and dependencies that might be impacting your application's performance.

Additionally, the following tools can help you understand the impact of adding new dependencies to your application:

* [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
* [Package Phobia](https://packagephobia.com/)
* [Bundle Phobia](https://bundlephobia.com/)
* [bundlejs](https://bundlejs.com/)


--------------------------------------------------------------------------------
title: "How to handle redirects in Next.js"
description: "Learn the different ways to handle redirects in Next.js."
source: "https://nextjs.org/docs/pages/guides/redirecting"
--------------------------------------------------------------------------------

# Redirecting

@router: Pages Router

There are a few ways you can handle redirects in Next.js. This page will go through each available option, use cases, and how to manage large numbers of redirects.

| API                                                           | Purpose                                           | Where                 | Status Code                        |
| ------------------------------------------------------------- | ------------------------------------------------- | --------------------- | ---------------------------------- |
| [`useRouter`](#userouter-hook)                                | Perform a client-side navigation                  | Components            | N/A                                |
| [`redirects` in `next.config.js`](#redirects-in-nextconfigjs) | Redirect an incoming request based on a path      | `next.config.js` file | 307 (Temporary) or 308 (Permanent) |
| [`NextResponse.redirect`](#nextresponseredirect-in-proxy)     | Redirect an incoming request based on a condition | Proxy                 | Any                                |

## `useRouter()` hook

If you need to redirect inside a component, you can use the `push` method from the `useRouter` hook. For example:

```tsx filename="app/page.tsx" switcher
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

```jsx filename="app/page.js" switcher
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

> **Good to know**:
>
> * If you don't need to programmatically navigate a user, you should use a [`<Link>`](/docs/app/api-reference/components/link.md) component.

See the [`useRouter` API reference](/docs/pages/api-reference/functions/use-router.md) for more information.

## `redirects` in `next.config.js`

The `redirects` option in the `next.config.js` file allows you to redirect an incoming request path to a different destination path. This is useful when you change the URL structure of pages or have a list of redirects that are known ahead of time.

`redirects` supports [path](/docs/app/api-reference/config/next-config-js/redirects.md#path-matching), [header, cookie, and query matching](/docs/app/api-reference/config/next-config-js/redirects.md#header-cookie-and-query-matching), giving you the flexibility to redirect users based on an incoming request.

To use `redirects`, add the option to your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async redirects() {
    return [
      // Basic redirect
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
      // Wildcard path matching
      {
        source: '/blog/:slug',
        destination: '/news/:slug',
        permanent: true,
      },
    ]
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  async redirects() {
    return [
      // Basic redirect
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
      // Wildcard path matching
      {
        source: '/blog/:slug',
        destination: '/news/:slug',
        permanent: true,
      },
    ]
  },
}
```

See the [`redirects` API reference](/docs/app/api-reference/config/next-config-js/redirects.md) for more information.

> **Good to know**:
>
> * `redirects` can return a 307 (Temporary Redirect) or 308 (Permanent Redirect) status code with the `permanent` option.
> * `redirects` may have a limit on platforms. For example, on Vercel, there's a limit of 1,024 redirects. To manage a large number of redirects (1000+), consider creating a custom solution using [Proxy](/docs/app/api-reference/file-conventions/proxy.md). See [managing redirects at scale](#managing-redirects-at-scale-advanced) for more.
> * `redirects` runs **before** Proxy.

## `NextResponse.redirect` in Proxy

Proxy allows you to run code before a request is completed. Then, based on the incoming request, redirect to a different URL using `NextResponse.redirect`. This is useful if you want to redirect users based on a condition (e.g. authentication, session management, etc) or have [a large number of redirects](#managing-redirects-at-scale-advanced).

For example, to redirect the user to a `/login` page if they are not authenticated:

```ts filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'
import { authenticate } from 'auth-provider'

export function proxy(request: NextRequest) {
  const isAuthenticated = authenticate(request)

  // If the user is authenticated, continue as normal
  if (isAuthenticated) {
    return NextResponse.next()
  }

  // Redirect to login page if not authenticated
  return NextResponse.redirect(new URL('/login', request.url))
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { authenticate } from 'auth-provider'

export function proxy(request) {
  const isAuthenticated = authenticate(request)

  // If the user is authenticated, continue as normal
  if (isAuthenticated) {
    return NextResponse.next()
  }

  // Redirect to login page if not authenticated
  return NextResponse.redirect(new URL('/login', request.url))
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

> **Good to know**:
>
> * Proxy runs **after** `redirects` in `next.config.js` and **before** rendering.

See the [Proxy](/docs/app/api-reference/file-conventions/proxy.md) documentation for more information.

## Managing redirects at scale (advanced)

To manage a large number of redirects (1000+), you may consider creating a custom solution using Proxy. This allows you to handle redirects programmatically without having to redeploy your application.

To do this, you'll need to consider:

1. Creating and storing a redirect map.
2. Optimizing data lookup performance.

> **Next.js Example**: See our [Proxy with Bloom filter](https://redirects-bloom-filter.vercel.app/) example for an implementation of the recommendations below.

### 1. Creating and storing a redirect map

A redirect map is a list of redirects that you can store in a database (usually a key-value store) or JSON file.

Consider the following data structure:

```json
{
  "/old": {
    "destination": "/new",
    "permanent": true
  },
  "/blog/post-old": {
    "destination": "/blog/post-new",
    "permanent": true
  }
}
```

In [Proxy](/docs/app/api-reference/file-conventions/proxy.md), you can read from a database such as Vercel's [Edge Config](https://vercel.com/docs/edge-config/get-started) or [Redis](https://vercel.com/docs/redis), and redirect the user based on the incoming request:

```ts filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'
import { get } from '@vercel/edge-config'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

export async function proxy(request: NextRequest) {
  const pathname = request.nextUrl.pathname
  const redirectData = await get(pathname)

  if (redirectData && typeof redirectData === 'string') {
    const redirectEntry: RedirectEntry = JSON.parse(redirectData)
    const statusCode = redirectEntry.permanent ? 308 : 307
    return NextResponse.redirect(redirectEntry.destination, statusCode)
  }

  // No redirect found, continue without redirecting
  return NextResponse.next()
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { get } from '@vercel/edge-config'

export async function proxy(request) {
  const pathname = request.nextUrl.pathname
  const redirectData = await get(pathname)

  if (redirectData) {
    const redirectEntry = JSON.parse(redirectData)
    const statusCode = redirectEntry.permanent ? 308 : 307
    return NextResponse.redirect(redirectEntry.destination, statusCode)
  }

  // No redirect found, continue without redirecting
  return NextResponse.next()
}
```

### 2. Optimizing data lookup performance

Reading a large dataset for every incoming request can be slow and expensive. There are two ways you can optimize data lookup performance:

* Use a database that is optimized for fast reads
* Use a data lookup strategy such as a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) to efficiently check if a redirect exists **before** reading the larger redirects file or database.

Considering the previous example, you can import a generated bloom filter file into Proxy, then, check if the incoming request pathname exists in the bloom filter.

If it does, forward the request to a  [API Routes](/docs/pages/building-your-application/routing/api-routes.md) which will check the actual file and redirect the user to the appropriate URL. This avoids importing a large redirects file into Proxy, which can slow down every incoming request.

```ts filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'
import { ScalableBloomFilter } from 'bloom-filters'
import GeneratedBloomFilter from './redirects/bloom-filter.json'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

// Initialize bloom filter from a generated JSON file
const bloomFilter = ScalableBloomFilter.fromJSON(GeneratedBloomFilter as any)

export async function proxy(request: NextRequest) {
  // Get the path for the incoming request
  const pathname = request.nextUrl.pathname

  // Check if the path is in the bloom filter
  if (bloomFilter.has(pathname)) {
    // Forward the pathname to the Route Handler
    const api = new URL(
      `/api/redirects?pathname=${encodeURIComponent(request.nextUrl.pathname)}`,
      request.nextUrl.origin
    )

    try {
      // Fetch redirect data from the Route Handler
      const redirectData = await fetch(api)

      if (redirectData.ok) {
        const redirectEntry: RedirectEntry | undefined =
          await redirectData.json()

        if (redirectEntry) {
          // Determine the status code
          const statusCode = redirectEntry.permanent ? 308 : 307

          // Redirect to the destination
          return NextResponse.redirect(redirectEntry.destination, statusCode)
        }
      }
    } catch (error) {
      console.error(error)
    }
  }

  // No redirect found, continue the request without redirecting
  return NextResponse.next()
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { ScalableBloomFilter } from 'bloom-filters'
import GeneratedBloomFilter from './redirects/bloom-filter.json'

// Initialize bloom filter from a generated JSON file
const bloomFilter = ScalableBloomFilter.fromJSON(GeneratedBloomFilter)

export async function proxy(request) {
  // Get the path for the incoming request
  const pathname = request.nextUrl.pathname

  // Check if the path is in the bloom filter
  if (bloomFilter.has(pathname)) {
    // Forward the pathname to the Route Handler
    const api = new URL(
      `/api/redirects?pathname=${encodeURIComponent(request.nextUrl.pathname)}`,
      request.nextUrl.origin
    )

    try {
      // Fetch redirect data from the Route Handler
      const redirectData = await fetch(api)

      if (redirectData.ok) {
        const redirectEntry = await redirectData.json()

        if (redirectEntry) {
          // Determine the status code
          const statusCode = redirectEntry.permanent ? 308 : 307

          // Redirect to the destination
          return NextResponse.redirect(redirectEntry.destination, statusCode)
        }
      }
    } catch (error) {
      console.error(error)
    }
  }

  // No redirect found, continue the request without redirecting
  return NextResponse.next()
}
```

Then, in the API Route:

```ts filename="pages/api/redirects.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'
import redirects from '@/app/redirects/redirects.json'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const pathname = req.query.pathname
  if (!pathname) {
    return res.status(400).json({ message: 'Bad Request' })
  }

  // Get the redirect entry from the redirects.json file
  const redirect = (redirects as Record<string, RedirectEntry>)[pathname]

  // Account for bloom filter false positives
  if (!redirect) {
    return res.status(400).json({ message: 'No redirect' })
  }

  // Return the redirect entry
  return res.json(redirect)
}
```

```js filename="pages/api/redirects.js" switcher
import redirects from '@/app/redirects/redirects.json'

export default function handler(req, res) {
  const pathname = req.query.pathname
  if (!pathname) {
    return res.status(400).json({ message: 'Bad Request' })
  }

  // Get the redirect entry from the redirects.json file
  const redirect = redirects[pathname]

  // Account for bloom filter false positives
  if (!redirect) {
    return res.status(400).json({ message: 'No redirect' })
  }

  // Return the redirect entry
  return res.json(redirect)
}
```

> **Good to know:**
>
> * To generate a bloom filter, you can use a library like [`bloom-filters`](https://www.npmjs.com/package/bloom-filters).
> * You should validate requests made to your Route Handler to prevent malicious requests.
- [redirect](/docs/app/api-reference/functions/redirect.md)
  - API Reference for the redirect function.
- [permanentRedirect](/docs/app/api-reference/functions/permanentRedirect.md)
  - API Reference for the permanentRedirect function.
- [proxy.js](/docs/app/api-reference/file-conventions/proxy.md)
  - API reference for the proxy.js file.
- [redirects](/docs/app/api-reference/config/next-config-js/redirects.md)
  - Add redirects to your Next.js app.


--------------------------------------------------------------------------------
title: "How to use Sass"
description: "Style your Next.js application using Sass."
source: "https://nextjs.org/docs/pages/guides/sass"
--------------------------------------------------------------------------------

# Sass

@router: Pages Router

Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.

First, install [`sass`](https://github.com/sass/sass):

```bash filename="Terminal"
npm install --save-dev sass
```

> **Good to know**:
>
> Sass supports [two different syntaxes](https://sass-lang.com/documentation/syntax), each with their own extension.
> The `.scss` extension requires you use the [SCSS syntax](https://sass-lang.com/documentation/syntax#scss),
> while the `.sass` extension requires you use the [Indented Syntax ("Sass")](https://sass-lang.com/documentation/syntax#the-indented-syntax).
>
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the
> Indented Syntax ("Sass").

### Customizing Sass Options

If you want to configure your Sass options, use `sassOptions` in `next.config`.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */

const nextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}

module.exports = nextConfig
```

#### Implementation

You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the [`sass`](https://www.npmjs.com/package/sass) package.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */

const nextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}

module.exports = nextConfig
```

### Sass Variables

Next.js supports Sass variables exported from CSS Module files.

For example, using the exported `primaryColor` Sass variable:

```scss filename="app/variables.module.scss"
$primary-color: #64ff00;

:export {
  primaryColor: $primary-color;
}
```

```jsx filename="pages/_app.js"
import variables from '../styles/variables.module.scss'

export default function MyApp({ Component, pageProps }) {
  return (
    <Layout color={variables.primaryColor}>
      <Component {...pageProps} />
    </Layout>
  )
}
```


--------------------------------------------------------------------------------
title: "How to load and optimize scripts"
description: "Optimize 3rd party scripts with the built-in Script component."
source: "https://nextjs.org/docs/pages/guides/scripts"
--------------------------------------------------------------------------------

# Scripts

@router: Pages Router

### Application Scripts

To load a third-party script for all routes, import `next/script` and include the script directly in your custom `_app`:

```jsx filename="pages/_app.js"
import Script from 'next/script'

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

This script will load and execute when *any* route in your application is accessed. Next.js will ensure the script will **only load once**, even if a user navigates between multiple pages.

> **Recommendation**: We recommend only including third-party scripts in specific pages or layouts in order to minimize any unnecessary impact to performance.

### Strategy

Although the default behavior of `next/script` allows you to load third-party scripts in any page or layout, you can fine-tune its loading behavior by using the `strategy` property:

* `beforeInteractive`: Load the script before any Next.js code and before any page hydration occurs.
* `afterInteractive`: (**default**) Load the script early but after some hydration on the page occurs.
* `lazyOnload`: Load the script later during browser idle time.
* `worker`: (experimental) Load the script in a web worker.

Refer to the [`next/script`](/docs/app/api-reference/components/script.md#strategy) API reference documentation to learn more about each strategy and their use cases.

### Offloading Scripts To A Web Worker (experimental)

> **Warning:** The `worker` strategy is not yet stable and does not yet work with the App Router. Use with caution.

Scripts that use the `worker` strategy are offloaded and executed in a web worker with [Partytown](https://partytown.builder.io/). This can improve the performance of your site by dedicating the main thread to the rest of your application code.

This strategy is still experimental and can only be used if the `nextScriptWorkers` flag is enabled in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  experimental: {
    nextScriptWorkers: true,
  },
}
```

Then, run `next` (normally `npm run dev` or `yarn dev`) and Next.js will guide you through the installation of the required packages to finish the setup:

```bash filename="Terminal"
npm run dev
```

You'll see instructions like these: Please install Partytown by running `npm install @builder.io/partytown`

Once setup is complete, defining `strategy="worker"` will automatically instantiate Partytown in your application and offload the script to a web worker.

```tsx filename="pages/home.tsx" switcher
import Script from 'next/script'

export default function Home() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="worker" />
    </>
  )
}
```

```jsx filename="pages/home.js" switcher
import Script from 'next/script'

export default function Home() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="worker" />
    </>
  )
}
```

There are a number of trade-offs that need to be considered when loading a third-party script in a web worker. Please see Partytown's [tradeoffs](https://partytown.builder.io/trade-offs) documentation for more information.

#### Using custom Partytown configuration

Although the `worker` strategy does not require any additional configuration to work, Partytown supports the use of a config object to modify some of its settings, including enabling `debug` mode and forwarding events and triggers.

If you would like to add additional configuration options, you can include it within the `<Head />` component used in a [custom `_document.js`](/docs/pages/building-your-application/routing/custom-document.md):

```jsx filename="_pages/document.jsx"
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head>
        <script
          data-partytown-config
          dangerouslySetInnerHTML={{
            __html: `
              partytown = {
                lib: "/_next/static/~partytown/",
                debug: true
              };
            `,
          }}
        />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

In order to modify Partytown's configuration, the following conditions must be met:

1. The `data-partytown-config` attribute must be used in order to overwrite the default configuration used by Next.js
2. Unless you decide to save Partytown's library files in a separate directory, the `lib: "/_next/static/~partytown/"` property and value must be included in the configuration object in order to let Partytown know where Next.js stores the necessary static files.

> **Note**: If you are using an [asset prefix](/docs/pages/api-reference/config/next-config-js/assetPrefix.md) and would like to modify Partytown's default configuration, you must include it as part of the `lib` path.

Take a look at Partytown's [configuration options](https://partytown.builder.io/configuration) to see the full list of other properties that can be added.

### Inline Scripts

Inline scripts, or scripts not loaded from an external file, are also supported by the Script component. They can be written by placing the JavaScript within curly braces:

```jsx
<Script id="show-banner">
  {`document.getElementById('banner').classList.remove('hidden')`}
</Script>
```

Or by using the `dangerouslySetInnerHTML` property:

```jsx
<Script
  id="show-banner"
  dangerouslySetInnerHTML={{
    __html: `document.getElementById('banner').classList.remove('hidden')`,
  }}
/>
```

> **Warning**: An `id` property must be assigned for inline scripts in order for Next.js to track and optimize the script.

### Executing Additional Code

Event handlers can be used with the Script component to execute additional code after a certain event occurs:

* `onLoad`: Execute code after the script has finished loading.
* `onReady`: Execute code after the script has finished loading and every time the component is mounted.
* `onError`: Execute code if the script fails to load.

These handlers will only work when `next/script` is imported and used inside of a [Client Component](/docs/app/getting-started/server-and-client-components.md) where `"use client"` is defined as the first line of code:

```tsx filename="pages/index.tsx" switcher
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onLoad={() => {
          console.log('Script has loaded')
        }}
      />
    </>
  )
}
```

```jsx filename="pages/index.js" switcher
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onLoad={() => {
          console.log('Script has loaded')
        }}
      />
    </>
  )
}
```

Refer to the [`next/script`](/docs/pages/api-reference/components/script.md#onload) API reference to learn more about each event handler and view examples.

### Additional Attributes

There are many DOM attributes that can be assigned to a `<script>` element that are not used by the Script component, like [`nonce`](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce) or [custom data attributes](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/data-*). Including any additional attributes will automatically forward it to the final, optimized `<script>` element that is included in the HTML.

```tsx filename="pages/index.tsx" switcher
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        id="example-script"
        nonce="XUENAJFW"
        data-test="script"
      />
    </>
  )
}
```

```jsx filename="pages/index.js" switcher
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        id="example-script"
        nonce="XUENAJFW"
        data-test="script"
      />
    </>
  )
}
```
## API Reference

Learn more about the next/script API.

- [Script Component](/docs/app/api-reference/components/script.md)
  - Optimize third-party scripts in your Next.js application using the built-in `next/script` Component.


--------------------------------------------------------------------------------
title: "How to self-host your Next.js application"
description: "Learn how to self-host your Next.js application on a Node.js server, Docker image, or static HTML files (static exports)."
source: "https://nextjs.org/docs/pages/guides/self-hosting"
--------------------------------------------------------------------------------

# Self-Hosting

@router: Pages Router

When [deploying](/docs/app/getting-started/deploying.md) your Next.js app, you may want to configure how different features are handled based on your infrastructure.

> **🎥 Watch:** Learn more about self-hosting Next.js → [YouTube (45 minutes)](https://www.youtube.com/watch?v=sIVL4JMqRfc).

## Reverse Proxy

When self-hosting, it's recommended to use a reverse proxy (like nginx) in front of your Next.js server rather than exposing it directly to the internet. A reverse proxy can handle malformed requests, slow connection attacks, payload size limits, rate limiting, and other security concerns, offloading these tasks from the Next.js server. This allows the server to dedicate its resources to rendering rather than request validation.

## Image Optimization

[Image Optimization](/docs/app/api-reference/components/image.md) through `next/image` works self-hosted with zero configuration when deploying using `next start`. If you would prefer to have a separate service to optimize images, you can [configure an image loader](/docs/app/api-reference/components/image.md#loader).

Image Optimization can be used with a [static export](/docs/app/guides/static-exports.md#image-optimization) by defining a custom image loader in `next.config.js`. Note that images are optimized at runtime, not during the build.

> **Good to know:**
>
> * On glibc-based Linux systems, Image Optimization may require [additional configuration](https://sharp.pixelplumbing.com/install#linux-memory-allocator) to prevent excessive memory usage.
> * Learn more about the [caching behavior of optimized images](/docs/app/api-reference/components/image.md#minimumcachettl) and how to configure the TTL.
> * You can also [disable Image Optimization](/docs/app/api-reference/components/image.md#unoptimized) and still retain other benefits of using `next/image` if you prefer. For example, if you are optimizing images yourself separately.

## Proxy

[Proxy](/docs/app/api-reference/file-conventions/proxy.md) works self-hosted with zero configuration when deploying using `next start`. Since it requires access to the incoming request, it is not supported when using a [static export](/docs/app/guides/static-exports.md).

Proxy uses the [Edge runtime](/docs/app/api-reference/edge.md), a subset of all available Node.js APIs to help ensure low latency, since it may run in front of every route or asset in your application. If you do not want this, you can use the [full Node.js runtime](/blog/next-15-2#nodejs-middleware-experimental) to run Proxy.

If you are looking to add logic (or use an external package) that requires all Node.js APIs, you might be able to move this logic to a [layout](/docs/app/api-reference/file-conventions/layout.md) as a [Server Component](/docs/app/getting-started/server-and-client-components.md). For example, checking [headers](/docs/app/api-reference/functions/headers.md) and [redirecting](/docs/app/api-reference/functions/redirect.md). You can also use headers, cookies, or query parameters to [redirect](/docs/app/api-reference/config/next-config-js/redirects.md#header-cookie-and-query-matching) or [rewrite](/docs/app/api-reference/config/next-config-js/rewrites.md#header-cookie-and-query-matching) through `next.config.js`. If that does not work, you can also use a [custom server](/docs/pages/guides/custom-server.md).

## Environment Variables

Next.js can support both build time and runtime environment variables.

**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.

To read runtime environment variables, we recommend using `getServerSideProps` or [incrementally adopting the App Router](/docs/app/guides/migrating/app-router-migration.md).

This allows you to use a singular Docker image that can be promoted through multiple environments with different values.

> **Good to know:**
>
> * You can run code on server startup using the [`register` function](/docs/app/guides/instrumentation.md).

## Caching and ISR

Next.js can cache responses, generated static pages, build outputs, and other static assets like images, fonts, and scripts.

Caching and revalidating pages (with [Incremental Static Regeneration](/docs/app/guides/incremental-static-regeneration.md)) use the **same shared cache**. By default, this cache is stored to the filesystem (on disk) on your Next.js server. **This works automatically when self-hosting** using both the Pages and App Router.

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.

### Automatic Caching

* Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` to truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](/docs/app/getting-started/images.md#local-images). You can [configure the TTL](/docs/app/api-reference/components/image.md#minimumcachettl) for images.
* Incremental Static Regeneration (ISR) sets the `Cache-Control` header of `s-maxage: <revalidate in getStaticProps>, stale-while-revalidate`. This revalidation time is defined in your [`getStaticProps` function](/docs/pages/building-your-application/data-fetching/get-static-props.md) in seconds. If you set `revalidate: false`, it will default to a one-year cache duration.
* Dynamically rendered pages set a `Cache-Control` header of `private, no-cache, no-store, max-age=0, must-revalidate` to prevent user-specific data from being cached. This applies to both the App Router and Pages Router. This also includes [Draft Mode](/docs/app/guides/draft-mode.md).

### Static Assets

If you want to host static assets on a different domain or CDN, you can use the `assetPrefix` [configuration](/docs/app/api-reference/config/next-config-js/assetPrefix.md) in `next.config.js`. Next.js will use this asset prefix when retrieving JavaScript or CSS files. Separating your assets to a different domain does come with the downside of extra time spent on DNS and TLS resolution.

[Learn more about `assetPrefix`](/docs/app/api-reference/config/next-config-js/assetPrefix.md).

### Configuring Caching

By default, generated cache assets will be stored in memory (defaults to 50mb) and on disk. If you are hosting Next.js using a container orchestration platform like Kubernetes, each pod will have a copy of the cache. To prevent stale data from being shown since the cache is not shared between pods by default, you can configure the Next.js cache to provide a cache handler and disable in-memory caching.

To configure the ISR/Data Cache location when self-hosting, you can configure a custom handler in your `next.config.js` file:

```jsx filename="next.config.js"
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

Then, create `cache-handler.js` in the root of your project, for example:

```jsx filename="cache-handler.js"
const cache = new Map()

module.exports = class CacheHandler {
  constructor(options) {
    this.options = options
  }

  async get(key) {
    // This could be stored anywhere, like durable storage
    return cache.get(key)
  }

  async set(key, data, ctx) {
    // This could be stored anywhere, like durable storage
    cache.set(key, {
      value: data,
      lastModified: Date.now(),
      tags: ctx.tags,
    })
  }

  async revalidateTag(tags) {
    // tags is either a string or an array of strings
    tags = [tags].flat()
    // Iterate over all entries in the cache
    for (let [key, value] of cache) {
      // If the value's tags include the specified tag, delete this entry
      if (value.tags.some((tag) => tags.includes(tag))) {
        cache.delete(key)
      }
    }
  }

  // If you want to have temporary in memory cache for a single request that is reset
  // before the next request you can leverage this method
  resetRequestCache() {}
}
```

Using a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application. For instance, you can save the cached values anywhere, like [Redis](https://github.com/vercel/next.js/tree/canary/examples/cache-handler-redis) or AWS S3.

> **Good to know:**
>
> * `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call the `revalidateTag` function with a special default tag for the provided page.

## Build Cache

Next.js generates an ID during `next build` to identify which version of your application is being served. The same build should be used and boot up multiple containers.

If you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the `generateBuildId` command in `next.config.js`:

```jsx filename="next.config.js"
module.exports = {
  generateBuildId: async () => {
    // This could be anything, using the latest git hash
    return process.env.GIT_HASH
  },
}
```

## Version Skew

Next.js will automatically mitigate most instances of [version skew](https://www.industrialempathy.com/posts/version-skew/) and automatically reload the application to retrieve new assets when detected. For example, if there is a mismatch in the `deploymentId`, transitions between pages will perform a hard navigation versus using a prefetched value.

When the application is reloaded, there may be a loss of application state if it's not designed to persist between page navigations. For example, using URL state or local storage would persist state after a page refresh. However, component state like `useState` would be lost in such navigations.

## Manual Graceful Shutdowns

When self-hosting, you might want to run code when the server shuts down on `SIGTERM` or `SIGINT` signals.

You can set the env variable `NEXT_MANUAL_SIG_HANDLE` to `true` and then register a handler for that signal inside your `_document.js` file. You will need to register the environment variable directly in the `package.json` script, and not in the `.env` file.

> **Good to know**: Manual signal handling is not available in `next dev`.

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "NEXT_MANUAL_SIG_HANDLE=true next start"
  }
}
```

```js filename="pages/_document.js"
if (process.env.NEXT_MANUAL_SIG_HANDLE) {
  process.on('SIGTERM', () => {
    console.log('Received SIGTERM: cleaning up')
    process.exit(0)
  })
  process.on('SIGINT', () => {
    console.log('Received SIGINT: cleaning up')
    process.exit(0)
  })
}
```


--------------------------------------------------------------------------------
title: "How to create a static export of your Next.js application"
description: "Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server."
source: "https://nextjs.org/docs/pages/guides/static-exports"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./12-fonts.md) | [Index](./index.md) | [Next →](./14-static-exports.md)
